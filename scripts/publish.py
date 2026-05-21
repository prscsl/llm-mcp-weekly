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
SEEN_FILE = ROOT / "data" / "seen.json"

CATEGORY_LABELS = {
    "release": "릴리스 소식",
    "tutorial": "튜토리얼 / 가이드",
    "news": "업계 뉴스",
    "opinion": "의견 / 분석",
    "tool": "도구 / 라이브러리",
    "research": "연구 / 논문",
}
CATEGORY_ORDER = ["release", "tool", "tutorial", "news", "research", "opinion"]


def load_seen() -> dict:
    if not SEEN_FILE.exists():
        return {"version": 1, "items": {}}
    with SEEN_FILE.open() as f:
        return json.load(f)


def save_seen(seen: dict) -> None:
    with SEEN_FILE.open("w") as f:
        json.dump(seen, f, indent=2, ensure_ascii=False)


def mark_seen(items: list[dict], date: str) -> int:
    seen = load_seen()
    updated = 0
    for item in items:
        item_hash = item.get("_hash")
        url = item.get("url")
        if not item_hash or not url or item_hash in seen["items"]:
            continue
        seen["items"][item_hash] = {
            "url": url,
            "first_seen": date,
        }
        updated += 1
    if updated:
        save_seen(seen)
    return updated


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
    deduped_items: list[dict] = []
    seen_keys: set[str] = set()
    for item in items:
        key = item.get("_hash") or item.get("url") or ""
        if key and key in seen_keys:
            continue
        if key:
            seen_keys.add(key)
        deduped_items.append(item)

    by_cat: dict[str, list[dict]] = {}
    all_tags: set[str] = set()
    for item in deduped_items:
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
        f"오늘 큐레이션된 항목: 총 **{len(deduped_items)}건**. ",
        "Anthropic, MCP 생태계, HuggingFace, HackerNews 등에서 자동 수집·요약했습니다.",
        "",
    ]

    body: list[str] = []
    for cat in CATEGORY_ORDER:
        if cat not in by_cat:
            continue
        body.append(f"### {CATEGORY_LABELS[cat]} ({len(by_cat[cat])})")
        body.append("{: .cat-section .cat-" + cat + "}")
        body.append("")
        for item in by_cat[cat]:
            body.append(render_item(item))

    return "\n".join(front + body)


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
    seen_updates = mark_seen(items, date)
    print(f"발행: {out_path} ({len(items)}건, seen {seen_updates}건 반영)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
