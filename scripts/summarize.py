#!/usr/bin/env python3
"""
수집 항목을 한국어로 요약·번역·태깅.

두 가지 백엔드 지원:
- claude-cli (default): `claude -p` 헤드리스 호출 → Max 플랜 사용량으로 차감 (비용 0)
- api: anthropic SDK 호출 → API 키 필요, 토큰당 별도 과금 (~$0.002/건)

입력: .raw/YYYY-MM-DD.json
출력: .summarized/YYYY-MM-DD.json
캐시: .cache/summary_{hash}.json — 동일 항목 재요약 방지

사용:
    python3 summarize.py                              # claude-cli 백엔드 (기본)
    python3 summarize.py --backend=api                # API 백엔드
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
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / ".raw"
SUM_DIR = ROOT / ".summarized"
CACHE_DIR = ROOT / ".cache"

API_MODEL = "claude-haiku-4-5-20251001"
API_MAX_TOKENS = 600
CLI_TIMEOUT = 90  # claude -p 호출 타임아웃 (초)

PROMPT_TEMPLATE = """다음은 LLM/MCP 관련 영문 콘텐츠입니다. 한국 개발자를 위해 한국어로 가공해주세요.

**중요 규칙**:
- 원문을 그대로 인용·번역하지 말 것 (저작권)
- 자체 해석과 한국 개발자 관점의 의미를 추가
- 과장·낚시 제목 금지 — 정확한 정보 전달
- 추측 금지 — 원문에 없는 사실 추가하지 말 것

**원문 정보**:
- 출처: {source}
- 원제: {title}
- URL: {url}
- 본문 일부: {summary_raw}

**출력 형식 (JSON only, 다른 텍스트·코드펜스 금지)**:
{{
  "ko_title": "한국어 제목 (40자 이내, SEO 키워드 포함)",
  "ko_summary": "2~3문장 요약 + 한국 개발자 관점 의미 1문장 (총 200~300자)",
  "tags": ["태그1", "태그2", "태그3"],
  "category": "release|tutorial|news|opinion|tool|research"
}}
"""


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
        "ko_summary": f"[DRY-RUN] {item['source']}에서 가져온 항목입니다. 실제 요약은 백엔드 호출 시 생성됩니다.",
        "tags": item.get("tags", ["stub"]),
        "category": "news",
    }


def extract_json(text: str) -> dict:
    """Claude 응답에서 JSON 객체 추출 (코드펜스·서두 텍스트 허용)."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```\s*$", "", text)
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError(f"JSON 객체를 찾을 수 없음. 원본: {text[:200]}")
    return json.loads(match.group(0))


def summarize_with_api(client: Any, item: dict) -> dict:
    prompt = PROMPT_TEMPLATE.format(
        source=item["source"],
        title=item["title"],
        url=item["url"],
        summary_raw=item.get("summary_raw", "")[:1500],
    )
    msg = client.messages.create(
        model=API_MODEL,
        max_tokens=API_MAX_TOKENS,
        messages=[{"role": "user", "content": prompt}],
    )
    return extract_json(msg.content[0].text)


def summarize_with_cli(item: dict) -> dict:
    prompt = PROMPT_TEMPLATE.format(
        source=item["source"],
        title=item["title"],
        url=item["url"],
        summary_raw=item.get("summary_raw", "")[:1500],
    )
    result = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True,
        text=True,
        timeout=CLI_TIMEOUT,
        env={**os.environ, "ANTHROPIC_API_KEY": ""},  # API 키가 있어도 Max 자격증명 사용 강제
    )
    if result.returncode != 0:
        raise RuntimeError(f"claude CLI 실패: {result.stderr[:300]}")
    return extract_json(result.stdout)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--backend",
        choices=["claude-cli", "api"],
        default="claude-cli",
        help="요약 백엔드: claude-cli (Max 플랜, 비용 0) 또는 api (별도 과금)",
    )
    args = parser.parse_args()

    date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    raw = load_raw(date)
    items = raw["items"]
    print(f"요약 시작: {date}, 입력 {len(items)}건, backend={args.backend}, dry-run={args.dry_run}")

    CACHE_DIR.mkdir(exist_ok=True)
    SUM_DIR.mkdir(exist_ok=True)

    api_client = None
    if not args.dry_run and args.backend == "api":
        try:
            from anthropic import Anthropic
        except ImportError:
            print("오류: anthropic SDK 미설치 (pip install anthropic)", file=sys.stderr)
            return 1
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            print("오류: ANTHROPIC_API_KEY 환경변수 없음", file=sys.stderr)
            return 1
        api_client = Anthropic(api_key=api_key)
    elif not args.dry_run and args.backend == "claude-cli":
        try:
            subprocess.run(["claude", "--version"], capture_output=True, check=True, timeout=5)
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            print("오류: claude CLI를 찾을 수 없음. 'claude --version'으로 확인 필요", file=sys.stderr)
            return 1

    summarized: list[dict] = []
    cache_hits = backend_calls = errors = 0

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
                if args.backend == "api":
                    ko = summarize_with_api(api_client, item)
                else:
                    ko = summarize_with_cli(item)
                with cp.open("w") as f:
                    json.dump(ko, f, indent=2, ensure_ascii=False)
                backend_calls += 1
                time.sleep(0.3)
            except Exception as e:
                print(f"  [요약 실패] {item['title'][:50]}: {e}", file=sys.stderr)
                errors += 1
                continue

        summarized.append({**item, "ko": ko})

    out_path = SUM_DIR / f"{date}.json"
    with out_path.open("w") as f:
        json.dump({"date": date, "items": summarized}, f, indent=2, ensure_ascii=False)

    print(f"완료: 캐시히트 {cache_hits}, {args.backend} 호출 {backend_calls}, 실패 {errors}")
    print(f"저장: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
