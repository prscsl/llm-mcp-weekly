#!/usr/bin/env python3
"""
수집 항목을 한국어로 요약·번역·태깅.

세 가지 요약 백엔드 지원:
- claude-cli: `claude -p` 헤드리스 호출 → Claude 구독 사용
- ollama: 로컬 Ollama HTTP API 호출 → 로컬 모델 사용, 비용 0원
- codex-api: OpenAI Responses API 호출 → OPENAI_API_KEY 필요

기본값 `auto`는 claude-cli를 먼저 시도하고, 불가하면 ollama, 마지막으로 codex-api로 fallback 한다.

입력: .raw/YYYY-MM-DD.json
출력: .summarized/YYYY-MM-DD.json
캐시: .cache/summary_{hash}.json — 동일 항목 재요약 방지

사용:
    python3 summarize.py                              # auto (claude-cli → ollama → codex-api)
    python3 summarize.py --backend=claude-cli
    python3 summarize.py --backend=ollama
    python3 summarize.py --backend=codex-api
    python3 summarize.py --date 2026-04-15
    python3 summarize.py --dry-run                    # 외부 호출 없이 stub 생성
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / ".raw"
SUM_DIR = ROOT / ".summarized"
CACHE_DIR = ROOT / ".cache"

CLI_TIMEOUT = 90  # claude -p 호출 타임아웃 (초)
CODEX_MODEL = os.environ.get("OPENAI_MODEL", "gpt-5.2-codex")
CODEX_MAX_OUTPUT_TOKENS = 600
BACKEND_AUTO = "auto"
BACKEND_CLAUDE = "claude-cli"
BACKEND_OLLAMA = "ollama"
BACKEND_CODEX = "codex-api"
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "qwen3:8b")
OLLAMA_TIMEOUT = 180
SUMMARY_SCHEMA = {
    "type": "object",
    "properties": {
        "ko_title": {"type": "string"},
        "one_line_summary": {"type": "string"},
        "ko_summary": {"type": "string"},
        "what_happened": {"type": "string"},
        "why_it_matters": {"type": "string"},
        "practical_takeaway": {"type": "string"},
        "who_should_read": {"type": "string"},
        "tags": {
            "type": "array",
            "items": {"type": "string"},
        },
        "category": {
            "type": "string",
            "enum": ["release", "tutorial", "news", "opinion", "tool", "research"],
        },
    },
    "required": [
        "ko_title",
        "one_line_summary",
        "ko_summary",
        "what_happened",
        "why_it_matters",
        "practical_takeaway",
        "who_should_read",
        "tags",
        "category",
    ],
    "additionalProperties": False,
}
GENERIC_TITLE_PATTERNS = [
    "ai 기반",
    "혁신 촉진",
    "기회 제공",
    "개발자 혁신",
    "클라우드 플랫폼",
    "새로운 기술",
    "서비스 시작",
]
COMMON_ANCHOR_STOPWORDS = {
    "show", "hn", "the", "and", "for", "with", "into", "from", "that", "this",
    "model", "models", "tool", "tools", "calling", "platform", "release",
    "releases", "blog", "news", "github", "com", "www", "http", "https",
}

PROMPT_TEMPLATE = """다음은 LLM/MCP 관련 영문 콘텐츠입니다. 한국 개발자를 위해 한국어로 가공해주세요.

**중요 규칙**:
- 원문을 그대로 인용·번역하지 말 것 (저작권)
- 자체 해석과 한국 개발자 관점의 의미를 추가
- 과장·낚시 제목 금지 — 정확한 정보 전달
- 추측 금지 — 원문에 없는 사실 추가하지 말 것
- URL에 직접 접속하거나 추가 도구를 사용하지 말 것
- 모호한 표현 금지: 'AI 기반', '새로운 기술', '혁신 촉진', '기회 제공' 같은 빈 문구를 피할 것
- 제품명, 조직명, 프로젝트명, 기능명 같은 고유명사를 최소 1개 이상 포함할 것

**원문 정보**:
- 출처: {source}
- 원제: {title}
- URL: {url}
- 본문 일부: {summary_raw}

**출력 형식 (JSON only, 다른 텍스트·코드펜스 금지)**:
{{
  "ko_title": "한국어 제목 (40자 이내, SEO 키워드 포함)",
  "one_line_summary": "핵심을 한 줄로 요약 (45~80자)",
  "ko_summary": "3~4문장 요약문 (총 260~420자)",
  "what_happened": "무슨 발표/변경/출시였는지 2~3문장",
  "why_it_matters": "왜 중요한지 2문장",
  "practical_takeaway": "한국 개발자가 실무에서 참고할 포인트 2~3문장",
  "who_should_read": "누가 특히 봐야 하는지 짧은 문구",
  "tags": ["태그1", "태그2", "태그3", "태그4"],
  "category": "release|tutorial|news|opinion|tool|research"
}}
"""


class ClaudeCliFatalError(RuntimeError):
    """로그인 누락 등 재시도로 해결되지 않는 CLI 상태."""


class BackendUnavailableError(RuntimeError):
    """환경 또는 자격 증명 문제로 현재 백엔드를 쓸 수 없는 상태."""


def load_raw(date: str) -> dict[str, Any]:
    path = RAW_DIR / f"{date}.json"
    if not path.exists():
        print(f"오류: {path} 없음. collect.py 먼저 실행 필요", file=sys.stderr)
        sys.exit(1)
    with path.open() as f:
        return json.load(f)


def cache_path(item_hash: str) -> Path:
    return CACHE_DIR / f"summary_{item_hash}.json"


def stub_summary(item: dict) -> dict:
    return {
        "ko_title": f"[STUB] {item['title'][:40]}",
        "one_line_summary": "[DRY-RUN] 실제 한 줄 요약은 백엔드 호출 시 생성됩니다.",
        "ko_summary": f"[DRY-RUN] {item['source']}에서 가져온 항목입니다. 실제 요약은 백엔드 호출 시 생성됩니다.",
        "what_happened": "[DRY-RUN] 원문 변경 사항 정리는 실제 호출 시 생성됩니다.",
        "why_it_matters": "[DRY-RUN] 중요도 설명은 실제 호출 시 생성됩니다.",
        "practical_takeaway": "[DRY-RUN] 실무 포인트는 실제 호출 시 생성됩니다.",
        "who_should_read": "LLM·MCP 실무자",
        "tags": item.get("tags", ["stub"]),
        "category": "news",
    }


def extract_json(text: str) -> dict:
    """백엔드 응답에서 JSON 객체 추출 (코드펜스·서두 텍스트 허용)."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```\s*$", "", text)
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError(f"JSON 객체를 찾을 수 없음. 원본: {text[:200]}")
    return json.loads(match.group(0))


def build_prompt(item: dict) -> str:
    return PROMPT_TEMPLATE.format(
        source=item["source"],
        title=item["title"],
        url=item["url"],
        summary_raw=item.get("summary_raw", "")[:1500],
    )


def synthesize_legacy_summary(output: dict[str, Any]) -> str:
    parts = [
        str(output.get("what_happened", "")).strip(),
        str(output.get("why_it_matters", "")).strip(),
        str(output.get("practical_takeaway", "")).strip(),
    ]
    return " ".join(part for part in parts if part).strip()


def normalize_summary_output(item: dict, output: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(output)
    normalized["ko_title"] = str(normalized.get("ko_title", "")).strip()[:40]
    normalized["one_line_summary"] = str(normalized.get("one_line_summary", "")).strip()
    normalized["what_happened"] = str(normalized.get("what_happened", "")).strip()
    normalized["why_it_matters"] = str(normalized.get("why_it_matters", "")).strip()
    normalized["practical_takeaway"] = str(normalized.get("practical_takeaway", "")).strip()
    normalized["who_should_read"] = str(normalized.get("who_should_read", "")).strip()

    if not normalized["ko_title"]:
        normalized["ko_title"] = build_fallback_title(item)
    if not normalized["one_line_summary"]:
        normalized["one_line_summary"] = normalized["ko_title"]
    if not normalized["what_happened"]:
        normalized["what_happened"] = str(normalized.get("ko_summary", "")).strip()
    if not normalized["why_it_matters"]:
        normalized["why_it_matters"] = "한국 개발자 입장에서 참고할 변화가 있는 항목입니다."
    if not normalized["practical_takeaway"]:
        normalized["practical_takeaway"] = "도입 여부와 적용 범위를 원문 기준으로 직접 확인하는 것이 좋습니다."
    if not normalized["who_should_read"]:
        normalized["who_should_read"] = "LLM·MCP 실무자"

    legacy = str(normalized.get("ko_summary", "")).strip()
    if len(legacy) < 120:
        normalized["ko_summary"] = synthesize_legacy_summary(normalized)
    else:
        normalized["ko_summary"] = legacy

    tags = normalized.get("tags")
    if not isinstance(tags, list):
        tags = []
    cleaned_tags: list[str] = []
    for tag in tags:
        text = str(tag).strip()
        if text and text not in cleaned_tags:
            cleaned_tags.append(text[:24])
    if not cleaned_tags:
        cleaned_tags = item.get("tags", []) or ["llm"]
    normalized["tags"] = cleaned_tags[:4]

    if normalized.get("category") not in {"release", "tutorial", "news", "opinion", "tool", "research"}:
        normalized["category"] = "news"
    return normalized


def extract_anchor_terms(item: dict) -> list[str]:
    primary_text = " ".join(str(item.get(k, "")) for k in ("source", "title"))
    secondary_text = str(item.get("url", ""))
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9+:-]{1,}", primary_text)
    tokens += re.findall(r"[A-Za-z][A-Za-z0-9+._:-]{1,}", secondary_text)
    anchors: list[str] = []
    seen: set[str] = set()
    for token in tokens:
        normalized = token.strip(".,:;()[]{}<>").lower()
        if (
            len(normalized) < 3
            or normalized in COMMON_ANCHOR_STOPWORDS
            or normalized.endswith(".com")
            or "http" in normalized
            or normalized.startswith("www.")
            or normalized.isdigit()
            or normalized in seen
        ):
            continue
        seen.add(normalized)
        anchors.append(token.strip(".,:;()[]{}<>"))
    return anchors[:8]


def ollama_output_needs_repair(item: dict, output: dict[str, Any]) -> bool:
    title = str(output.get("ko_title", "")).strip()
    summary = str(output.get("ko_summary", "")).strip()
    what_happened = str(output.get("what_happened", "")).strip()
    why_it_matters = str(output.get("why_it_matters", "")).strip()
    practical_takeaway = str(output.get("practical_takeaway", "")).strip()
    lowered_title = title.lower()
    if not title or not summary or not what_happened or not why_it_matters or not practical_takeaway:
        return True
    if len(summary) < 120 or len(what_happened) < 40 or len(why_it_matters) < 35 or len(practical_takeaway) < 35:
        return True
    if any(pattern in title for pattern in GENERIC_TITLE_PATTERNS):
        return True
    anchors = extract_anchor_terms(item)
    if anchors:
        if not any(anchor.lower() in lowered_title for anchor in anchors):
            return True
    return False


def build_ollama_repair_prompt(item: dict, bad_output: dict[str, Any]) -> str:
    anchors = ", ".join(extract_anchor_terms(item)) or item.get("title", "")
    return f"""이전 JSON 결과를 더 구체적으로 다시 작성해주세요.

반드시 지킬 규칙:
- ko_title에는 다음 고유명사 중 최소 1개를 반드시 포함: {anchors}
- 추상 표현 금지: 'AI 기반', '혁신 촉진', '기회 제공', '새로운 기술', '클라우드 플랫폼'
- 제목은 무엇이 발표/출시/변경되었는지 바로 드러나야 함
- 출력은 JSON only

원문 정보:
- 출처: {item.get('source', '')}
- 원제: {item.get('title', '')}
- URL: {item.get('url', '')}
- 본문 일부: {str(item.get('summary_raw', ''))[:1500]}

이전 결과:
{json.dumps(bad_output, ensure_ascii=False)}
"""


def build_fallback_title(item: dict) -> str:
    anchors = extract_anchor_terms(item)
    primary = anchors[0] if anchors else "LLM"
    secondary = ""
    for anchor in anchors[1:]:
        if anchor.lower() not in primary.lower():
            secondary = anchor
            break

    lower_title = str(item.get("title", "")).lower()
    if "release" in lower_title or "릴리스" in lower_title:
        suffix = "릴리스"
    elif "show hn" in lower_title:
        suffix = "프로젝트 공개"
    elif "platform" in lower_title:
        suffix = "플랫폼 공개"
    elif "tool" in lower_title or "tools" in lower_title:
        suffix = "도구 공개"
    elif "model" in lower_title:
        suffix = "모델 공개"
    else:
        suffix = "업데이트"

    parts = [primary]
    if secondary and secondary.lower() not in COMMON_ANCHOR_STOPWORDS:
        parts.append(secondary)
    parts.append(suffix)
    return " ".join(parts)[:40]


def summarize_with_codex(client: Any, item: dict) -> dict:
    prompt = build_prompt(item)
    response = client.responses.create(
        model=CODEX_MODEL,
        input=[{"role": "user", "content": prompt}],
        max_output_tokens=CODEX_MAX_OUTPUT_TOKENS,
        text={
            "format": {
                "type": "json_schema",
                "name": "curation_summary",
                "strict": True,
                "schema": SUMMARY_SCHEMA,
            }
        },
    )
    output_text = getattr(response, "output_text", "") or ""
    if not output_text.strip():
        raise RuntimeError("OpenAI Responses API가 빈 응답을 반환했습니다.")
    return normalize_summary_output(item, json.loads(output_text))


def ollama_post(path: str, payload: dict[str, Any]) -> dict[str, Any]:
    req = urllib.request.Request(
        f"{OLLAMA_HOST}{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=OLLAMA_TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def summarize_with_ollama(item: dict) -> dict:
    prompt = build_prompt(item)
    data = ollama_post(
        "/api/generate",
        {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "format": SUMMARY_SCHEMA,
            "options": {"temperature": 0.2},
        },
    )
    response_text = (data.get("response") or "").strip()
    if not response_text:
        raise RuntimeError("Ollama가 빈 응답을 반환했습니다.")
    output = extract_json(response_text)
    if ollama_output_needs_repair(item, output):
        repaired = ollama_post(
            "/api/generate",
            {
                "model": OLLAMA_MODEL,
                "prompt": build_ollama_repair_prompt(item, output),
                "stream": False,
                "format": SUMMARY_SCHEMA,
                "options": {"temperature": 0.2},
            },
        )
        repaired_text = (repaired.get("response") or "").strip()
        if repaired_text:
            repaired_output = extract_json(repaired_text)
            if not ollama_output_needs_repair(item, repaired_output):
                return normalize_summary_output(item, repaired_output)
    if ollama_output_needs_repair(item, output):
        output["ko_title"] = build_fallback_title(item)
    return normalize_summary_output(item, output)


def summarize_with_claude(item: dict) -> dict:
    prompt = build_prompt(item)
    result = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True,
        text=True,
        timeout=CLI_TIMEOUT,
        env={**os.environ, "ANTHROPIC_API_KEY": ""},  # API 키가 있어도 Claude 구독 자격증명 사용 강제
    )
    if result.returncode != 0:
        detail = "\n".join(
            part.strip() for part in (result.stderr, result.stdout) if part and part.strip()
        )[:300]
        if "Not logged in" in detail or "/login" in detail:
            raise ClaudeCliFatalError("claude CLI가 로그인되지 않았습니다. `claude login` 후 다시 실행하세요.")
        raise RuntimeError(f"claude CLI 실패: {detail or '원인 불명'}")
    return normalize_summary_output(item, extract_json(result.stdout))


def get_backend_order(name: str) -> list[str]:
    if name == BACKEND_AUTO:
        return [BACKEND_CLAUDE, BACKEND_OLLAMA, BACKEND_CODEX]
    return [name]


def init_codex_client() -> Any:
    try:
        from openai import OpenAI
    except ImportError as e:
        raise BackendUnavailableError("openai SDK 미설치 (pip install openai)") from e

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise BackendUnavailableError("OPENAI_API_KEY 환경변수 없음")
    return OpenAI(api_key=api_key)


def ensure_claude_cli_ready() -> None:
    try:
        subprocess.run(["claude", "--version"], capture_output=True, check=True, timeout=5)
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired) as e:
        raise BackendUnavailableError("claude CLI를 찾을 수 없음. 'claude --version'으로 확인 필요") from e


def ensure_ollama_ready() -> None:
    try:
        req = urllib.request.Request(f"{OLLAMA_HOST}/api/tags", method="GET")
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise BackendUnavailableError(f"Ollama에 연결할 수 없음: {OLLAMA_HOST} ({e.reason})") from e
    except Exception as e:
        raise BackendUnavailableError(f"Ollama 상태 확인 실패: {e}") from e

    models = {
        model.get("model") or model.get("name")
        for model in data.get("models", [])
        if isinstance(model, dict)
    }
    if OLLAMA_MODEL not in models:
        available = ", ".join(sorted(m for m in models if m)) or "없음"
        raise BackendUnavailableError(
            f"Ollama 모델 '{OLLAMA_MODEL}' 없음. 현재 모델: {available}"
        )


def summarize_with_backend(backend: str, clients: dict[str, Any], item: dict) -> dict:
    if backend == BACKEND_CLAUDE:
        ensure_claude_cli_ready()
        return summarize_with_claude(item)
    if backend == BACKEND_OLLAMA:
        ensure_ollama_ready()
        return summarize_with_ollama(item)
    if backend == BACKEND_CODEX:
        client = clients.get(BACKEND_CODEX)
        if client is None:
            raise BackendUnavailableError("codex-api 사용 준비가 되지 않았습니다.")
        return summarize_with_codex(client, item)
    raise ValueError(f"알 수 없는 backend: {backend}")


def summarize_with_fallback(item: dict, backends: list[str], clients: dict[str, Any]) -> tuple[dict, str]:
    failures: list[str] = []
    for backend in backends:
        try:
            return summarize_with_backend(backend, clients, item), backend
        except BackendUnavailableError as e:
            failures.append(f"{backend}: {e}")
        except ClaudeCliFatalError as e:
            failures.append(f"{backend}: {e}")
        except Exception as e:
            failures.append(f"{backend}: {e}")
    raise RuntimeError(" / ".join(failures))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--backend",
        choices=[BACKEND_AUTO, BACKEND_CLAUDE, BACKEND_OLLAMA, BACKEND_CODEX],
        default=BACKEND_AUTO,
        help="요약 백엔드: auto(claude-cli→ollama→codex-api), claude-cli, ollama, codex-api",
    )
    args = parser.parse_args()

    date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    raw = load_raw(date)
    items = raw["items"]
    print(f"요약 시작: {date}, 입력 {len(items)}건, backend={args.backend}, dry-run={args.dry_run}")

    CACHE_DIR.mkdir(exist_ok=True)
    SUM_DIR.mkdir(exist_ok=True)

    backend_order = get_backend_order(args.backend)
    clients: dict[str, Any] = {}
    if not args.dry_run and BACKEND_CODEX in backend_order:
        try:
            clients[BACKEND_CODEX] = init_codex_client()
        except BackendUnavailableError as e:
            if args.backend == BACKEND_CODEX:
                print(f"오류: {e}", file=sys.stderr)
                return 1
            print(f"[backend 준비 실패] {BACKEND_CODEX}: {e}", file=sys.stderr)
    if not args.dry_run and args.backend == BACKEND_CLAUDE:
        try:
            ensure_claude_cli_ready()
        except BackendUnavailableError as e:
            print(f"오류: {e}", file=sys.stderr)
            return 1
    if not args.dry_run and args.backend == BACKEND_OLLAMA:
        try:
            ensure_ollama_ready()
        except BackendUnavailableError as e:
            print(f"오류: {e}", file=sys.stderr)
            return 1

    summarized: list[dict] = []
    cache_hits = errors = 0
    backend_calls = {BACKEND_CLAUDE: 0, BACKEND_OLLAMA: 0, BACKEND_CODEX: 0}

    for item in items:
        h = item.get("_hash", "")
        cp = cache_path(h)

        if cp.exists():
            with cp.open() as f:
                ko = json.load(f)
            cache_hits += 1
        elif args.dry_run:
            ko = stub_summary(item)
        else:
            try:
                ko, backend_used = summarize_with_fallback(item, backend_order, clients)
                with cp.open("w") as f:
                    json.dump(ko, f, indent=2, ensure_ascii=False)
                backend_calls[backend_used] += 1
                time.sleep(0.3)
            except Exception as e:
                print(f"  [요약 실패] {item['title'][:50]}: {e}", file=sys.stderr)
                errors += 1
                continue

        summarized.append({**item, "ko": ko})

    if items and not summarized and not args.dry_run:
        print("오류: 모든 항목 요약에 실패했습니다. 결과 파일을 쓰지 않습니다.", file=sys.stderr)
        return 1

    out_path = SUM_DIR / f"{date}.json"
    with out_path.open("w") as f:
        json.dump({"date": date, "items": summarized}, f, indent=2, ensure_ascii=False)

    backend_stats = ", ".join(
        f"{name} {count}건" for name, count in backend_calls.items() if count
    ) or "실제 호출 0건"
    print(f"완료: 캐시히트 {cache_hits}, {backend_stats}, 실패 {errors}")
    print(f"저장: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
