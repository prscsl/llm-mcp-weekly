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
import re
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


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def anchor_slug(value: str, fallback: str) -> str:
    slug = re.sub(r"[^a-z0-9가-힣]+", "-", value.lower()).strip("-")
    return slug[:64] or fallback


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


def render_item(item: dict, index: int) -> str:
    ko = item["ko"]
    one_line = ko.get("one_line_summary", ko.get("ko_summary", ""))
    what_happened = ko.get("what_happened", ko.get("ko_summary", ""))
    why_it_matters = ko.get("why_it_matters", "")
    practical_takeaway = ko.get("practical_takeaway", "")
    who_should_read = ko.get("who_should_read", "")
    item_id = anchor_slug(ko["ko_title"], f"item-{index}")
    lines = [
        '<section class="brief-card" markdown="1">',
        f'<h4 id="{item_id}" class="brief-card__title">{ko["ko_title"]}</h4>',
        "",
        f"**한 줄 요약**  \n{one_line}",
        "",
        f"**무슨 내용인가**  \n{what_happened}",
        "",
        f"**왜 중요한가**  \n{why_it_matters}",
        "",
        f"**실무 포인트**  \n{practical_takeaway}",
        "",
    ]
    if who_should_read:
        lines.append(f"**추천 독자**  \n{who_should_read}")
        lines.append("")
    if item.get("type") == "hackernews" and item.get("hn_points"):
        lines.append(
            f"> HN {item['hn_points']}점 · "
            f"[토론 보기]({item['hn_url']})"
        )
        lines.append("")
    lines.append(f"[원문 보기 →]({item['url']}) ({item['source']})")
    lines.append("")
    lines.append("</section>")
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

    nav_lines = [
        '<aside class="post-outline" markdown="0">',
        '<div class="post-outline__inner">',
        '<p class="post-outline__eyebrow">이 글의 항목</p>',
    ]
    nav_index = 1
    for cat in CATEGORY_ORDER:
        if cat not in by_cat:
            continue
        nav_lines.append(
            f'<p class="post-outline__group">{CATEGORY_LABELS[cat]}</p>'
        )
        nav_lines.append('<ul class="post-outline__list">')
        for item in by_cat[cat]:
            title = item["ko"]["ko_title"]
            item_id = anchor_slug(title, f"item-{nav_index}")
            nav_lines.append(
                f'<li><a href="#{item_id}"><span class="post-outline__num">{nav_index:02d}</span>{title}</a></li>'
            )
            nav_index += 1
        nav_lines.append("</ul>")
    nav_lines.extend([
        "</div>",
        "</aside>",
        "",
    ])

    tag_lines = [f"  - {yaml_quote(tag)}" for tag in sorted(all_tags)] or ['  - "llm"']
    front = [
        "---",
        "layout: post",
        f'title: "{date} LLM·MCP 위클리"',
        f"date: {date} 09:00:00 +0900",
        "categories:",
        '  - "weekly"',
        "tags:",
        *tag_lines,
        "---",
        "",
        f"## {date} 한국어 LLM·MCP 큐레이션",
        "",
        f"오늘 큐레이션된 항목: 총 **{len(deduped_items)}건**. ",
        "Anthropic, MCP 생태계, HuggingFace, HackerNews 등에서 자동 수집·요약했습니다.",
        "",
    ]

    top_items = deduped_items[:3]
    if top_items:
        front.extend([
            "### 오늘의 포인트",
            "",
        ])
        for item in top_items:
            one_line = item["ko"].get("one_line_summary", item["ko"].get("ko_summary", ""))
            front.append(f"- **{item['ko']['ko_title']}** — {one_line}")
        front.append("")
    front.extend(nav_lines)

    body: list[str] = []
    item_index = 1
    for cat in CATEGORY_ORDER:
        if cat not in by_cat:
            continue
        body.append(f"### {CATEGORY_LABELS[cat]} ({len(by_cat[cat])})")
        body.append("{: .cat-section .cat-" + cat + "}")
        body.append("")
        for item in by_cat[cat]:
            body.append(render_item(item, item_index))
            item_index += 1

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
