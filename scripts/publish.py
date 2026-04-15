#!/usr/bin/env python3
"""
.summarized/YYYY-MM-DD.json → _posts/YYYY-MM-DD-llm-mcp-daily.md 생성.

Jekyll front matter + 카테고리별 그룹화된 마크다운 본문.

사용:
    python3 publish.py                       # 오늘 날짜
    python3 publish.py --date 2026-04-15
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUM_DIR = ROOT / ".summarized"
POSTS_DIR = ROOT / "_posts"

CATEGORY_LABELS = {
    "release": "릴리스 소식",
    "tutorial": "튜토리얼 / 가이드",
    "news": "업계 뉴스",
    "opinion": "의견 / 분석",
    "tool": "도구 / 라이브러리",
    "research": "연구 / 논문",
}
CATEGORY_ORDER = ["release", "tool", "tutorial", "news", "research", "opinion"]


def render_item(item: dict) -> str:
    ko = item["ko"]
    lines = [
        f"#### {ko['ko_title']}",
        "",
        ko["ko_summary"],
        "",
    ]
    if item.get("type") == "hackernews" and item.get("hn_points"):
        lines.append(
            f"> HN {item['hn_points']}점 · "
            f"[토론 보기]({item['hn_url']})"
        )
        lines.append("")
    lines.append(f"[원문 보기 →]({item['url']}) ({item['source']})")
    lines.append("")
    return "\n".join(lines)


def render_post(date: str, items: list[dict]) -> str:
    by_cat: dict[str, list[dict]] = {}
    all_tags: set[str] = set()
    for item in items:
        cat = item["ko"].get("category", "news")
        by_cat.setdefault(cat, []).append(item)
        for t in item["ko"].get("tags", []):
            all_tags.add(t.lower().strip())

    front = [
        "---",
        "layout: post",
        f'title: "{date} LLM·MCP 위클리"',
        f"date: {date} 09:00:00 +0900",
        "categories: [weekly]",
        f"tags: [{', '.join(sorted(all_tags))}]",
        "---",
        "",
        f"## {date} 한국어 LLM·MCP 큐레이션",
        "",
        f"오늘 큐레이션된 항목: 총 **{len(items)}건**. ",
        "Anthropic, MCP 생태계, HuggingFace, HackerNews 등에서 자동 수집·요약했습니다.",
        "",
    ]

    body: list[str] = []
    for cat in CATEGORY_ORDER:
        if cat not in by_cat:
            continue
        body.append(f"### {CATEGORY_LABELS[cat]} ({len(by_cat[cat])})")
        body.append("")
        for item in by_cat[cat]:
            body.append(render_item(item))

    footer = [
        "---",
        "",
        "*본 포스트는 Claude Haiku 4.5로 자동 큐레이션·요약되었습니다. ",
        "각 항목의 저작권은 원저작자에게 있으며, 본 사이트는 한국어 요약과 원문 링크만 제공합니다. ",
        "오류·문의는 [이슈](https://github.com/prscsl/llm-mcp-weekly/issues)로 남겨주세요.*",
        "",
    ]
    return "\n".join(front + body + footer)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None)
    args = parser.parse_args()

    date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    sum_path = SUM_DIR / f"{date}.json"
    if not sum_path.exists():
        print(f"오류: {sum_path} 없음. summarize.py 먼저 실행 필요", file=sys.stderr)
        return 1

    with sum_path.open() as f:
        data = json.load(f)
    items = data["items"]
    if not items:
        print(f"항목이 없음. 포스트를 생성하지 않음.")
        return 0

    POSTS_DIR.mkdir(exist_ok=True)
    out_path = POSTS_DIR / f"{date}-llm-mcp-daily.md"
    out_path.write_text(render_post(date, items), encoding="utf-8")
    print(f"발행: {out_path} ({len(items)}건)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
