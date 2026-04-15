#!/usr/bin/env python3
"""
LLM·MCP 위클리 데이터 수집기.

sources.yml에 정의된 RSS / GitHub Releases / HackerNews에서
최근 N일 항목을 수집해 .raw/YYYY-MM-DD.json으로 저장.
seen.json으로 중복 제거.

사용:
    python3 collect.py                    # 오늘 날짜로 수집
    python3 collect.py --date 2026-04-15  # 특정 날짜
    python3 collect.py --dry-run          # 외부 호출 없이 구조만 확인
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

import feedparser  # type: ignore
import yaml  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
RAW_DIR = ROOT / ".raw"
SOURCES_FILE = DATA_DIR / "sources.yml"
SEEN_FILE = DATA_DIR / "seen.json"

USER_AGENT = "llm-mcp-weekly-bot/1.0 (+https://github.com/prscsl/llm-mcp-weekly)"
HTTP_TIMEOUT = 15


def load_sources() -> dict[str, Any]:
    with SOURCES_FILE.open() as f:
        return yaml.safe_load(f)


def load_seen() -> dict[str, Any]:
    if not SEEN_FILE.exists():
        return {"version": 1, "items": {}}
    with SEEN_FILE.open() as f:
        return json.load(f)


def save_seen(seen: dict[str, Any]) -> None:
    with SEEN_FILE.open("w") as f:
        json.dump(seen, f, indent=2, ensure_ascii=False)


def url_hash(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def http_get_json(url: str) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def parse_date(value: Any) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, time.struct_time):
        return datetime(*value[:6], tzinfo=timezone.utc)
    if isinstance(value, str):
        for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%d"):
            try:
                return datetime.strptime(value, fmt).replace(tzinfo=timezone.utc)
            except ValueError:
                continue
    return None


def collect_rss(source: dict, cutoff: datetime) -> list[dict]:
    items: list[dict] = []
    try:
        feed = feedparser.parse(source["url"], agent=USER_AGENT)
    except Exception as e:
        print(f"  [RSS 실패] {source['name']}: {e}", file=sys.stderr)
        return items

    for entry in feed.entries:
        published = parse_date(entry.get("published_parsed") or entry.get("updated_parsed"))
        if published and published < cutoff:
            continue
        items.append({
            "type": "rss",
            "source": source["name"],
            "title": entry.get("title", "").strip(),
            "url": entry.get("link", ""),
            "summary_raw": (entry.get("summary") or "")[:2000],
            "published": published.isoformat() if published else None,
            "weight": source.get("weight", 5),
            "tags": source.get("tags", []),
        })
    return items


def collect_github_releases(source: dict, cutoff: datetime) -> list[dict]:
    items: list[dict] = []
    repo = source["repo"]
    url = f"https://api.github.com/repos/{repo}/releases?per_page=10"
    try:
        releases = http_get_json(url)
    except urllib.error.HTTPError as e:
        print(f"  [GitHub 실패] {repo}: HTTP {e.code}", file=sys.stderr)
        return items
    except Exception as e:
        print(f"  [GitHub 실패] {repo}: {e}", file=sys.stderr)
        return items

    for rel in releases:
        published = parse_date(rel.get("published_at"))
        if published and published < cutoff:
            continue
        if rel.get("draft") or rel.get("prerelease"):
            continue
        items.append({
            "type": "github_release",
            "source": f"GitHub: {repo}",
            "title": f"{repo} {rel.get('tag_name', '')} 릴리스",
            "url": rel.get("html_url", ""),
            "summary_raw": (rel.get("body") or "")[:3000],
            "published": published.isoformat() if published else None,
            "weight": source.get("weight", 5),
            "tags": source.get("tags", []),
        })
    return items


def collect_hackernews(source: dict, cutoff: datetime) -> list[dict]:
    items: list[dict] = []
    keyword = source["keyword"]
    min_points = source.get("min_points", 10)
    cutoff_ts = int(cutoff.timestamp())
    url = (
        "https://hn.algolia.com/api/v1/search"
        f"?query={urllib.request.quote(keyword)}"
        f"&tags=story&numericFilters=created_at_i>{cutoff_ts},points>{min_points}"
        "&hitsPerPage=20"
    )
    try:
        data = http_get_json(url)
    except Exception as e:
        print(f"  [HN 실패] {keyword}: {e}", file=sys.stderr)
        return items

    for hit in data.get("hits", []):
        if not hit.get("url"):
            continue
        items.append({
            "type": "hackernews",
            "source": f"HN ({keyword})",
            "title": hit.get("title", "").strip(),
            "url": hit.get("url"),
            "summary_raw": f"HN points: {hit.get('points')}, comments: {hit.get('num_comments')}",
            "published": datetime.fromtimestamp(hit.get("created_at_i", 0), timezone.utc).isoformat(),
            "weight": source.get("weight", 5) + min(hit.get("points", 0) // 50, 5),
            "tags": ["hackernews"],
            "hn_points": hit.get("points"),
            "hn_url": f"https://news.ycombinator.com/item?id={hit.get('objectID')}",
        })
    return items


def deduplicate(items: list[dict], seen: dict) -> list[dict]:
    fresh: list[dict] = []
    for item in items:
        if not item.get("url"):
            continue
        h = url_hash(item["url"])
        if h in seen["items"]:
            continue
        item["_hash"] = h
        fresh.append(item)
    return fresh


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None, help="수집 기준일 (YYYY-MM-DD)")
    parser.add_argument("--dry-run", action="store_true", help="외부 호출 없이 구조만 확인")
    args = parser.parse_args()

    today = datetime.strptime(args.date, "%Y-%m-%d").replace(tzinfo=timezone.utc) if args.date else datetime.now(timezone.utc)
    sources = load_sources()
    cutoff = today - timedelta(days=sources["policy"]["lookback_days"])

    print(f"수집 시작: 기준일={today.date()}, lookback={sources['policy']['lookback_days']}일")

    if args.dry_run:
        print("[DRY-RUN] 외부 호출 생략. 소스 정의만 출력:")
        for k, v in sources.items():
            if isinstance(v, list):
                print(f"  {k}: {len(v)}개")
        return 0

    seen = load_seen()
    all_items: list[dict] = []

    for s in sources.get("rss", []):
        print(f"  [RSS] {s['name']}...")
        all_items.extend(collect_rss(s, cutoff))

    for s in sources.get("github_releases", []):
        print(f"  [GH] {s['repo']}...")
        all_items.extend(collect_github_releases(s, cutoff))
        time.sleep(0.5)

    for s in sources.get("hackernews_keywords", []):
        print(f"  [HN] {s['keyword']}...")
        all_items.extend(collect_hackernews(s, cutoff))

    fresh = deduplicate(all_items, seen)
    fresh.sort(key=lambda x: x.get("weight", 0), reverse=True)
    fresh = fresh[: sources["policy"]["max_items_per_run"]]

    print(f"수집 결과: 전체 {len(all_items)}건 → 신규 {len(fresh)}건")

    RAW_DIR.mkdir(exist_ok=True)
    out_path = RAW_DIR / f"{today.date()}.json"
    with out_path.open("w") as f:
        json.dump({"date": str(today.date()), "items": fresh}, f, indent=2, ensure_ascii=False)
    print(f"저장: {out_path}")

    for item in fresh:
        seen["items"][item["_hash"]] = {"url": item["url"], "first_seen": str(today.date())}
    save_seen(seen)
    print(f"seen.json 업데이트: 총 {len(seen['items'])}개 추적 중")

    return 0


if __name__ == "__main__":
    sys.exit(main())
