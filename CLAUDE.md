# CLAUDE.md — llm-mcp-weekly

## 프로젝트 개요

매일 자동으로 LLM·MCP 생태계 영문 소식을 수집·요약·발행하는 Jekyll 정적 블로그.
대상 독자: 한국 백엔드·데이터 엔지니어.
배포: GitHub Pages (`https://prscsl.github.io/llm-mcp-weekly/`)

## 작업 규칙

- **"수정해"라고 명시적으로 말하기 전에는 절대 코드를 수정하지 말 것**
- 운영 서비스에 영향을 주는 변경(push, 스크립트 실행 등)은 보고 후 승인받아 진행
- 한국어로 응답할 것

## 디렉토리 구조

```
llm-mcp-weekly/
├── scripts/
│   ├── collect.py          ← RSS/GH/HN 수집 → .raw/YYYY-MM-DD.json
│   ├── summarize.py        ← 한국어 요약 → .summarized/YYYY-MM-DD.json
│   ├── publish.py          ← 마크다운 포스트 생성 → _posts/
│   ├── run_daily.sh        ← launchd가 호출하는 진입점 (zsh)
│   └── com.prscsl.llm-mcp-weekly.daily.plist  ← LaunchAgent plist 원본
├── data/
│   ├── sources.yml         ← 수집 소스 정의 (RSS / GitHub / HN)
│   └── seen.json           ← 중복 방지용 수집 이력
├── .raw/                   ← 원본 수집 결과 (git 제외)
├── .summarized/            ← 요약 결과 (git 제외)
├── .cache/                 ← 요약 캐시 (git 제외)
├── logs/                   ← 파이프라인 실행 로그 (git 제외)
├── _posts/                 ← Jekyll 포스트 (파이프라인이 자동 생성)
├── _layouts/post.html      ← layout: post → single 위임 ({{ content }} 필수)
├── _data/navigation.yml    ← 상단 네비게이션
├── assets/images/          ← og-default.png, logo.png
├── _config.yml             ← Jekyll 설정 (Minimal Mistakes 테마)
├── Gemfile                 ← minimal-mistakes-jekyll 젬
└── .github/workflows/deploy.yml  ← Ruby 3.3 빌드 + GitHub Pages 배포
```

## 파이프라인

```
[launchd 06:00 KST]
  run_daily.sh
    → collect.py --date YYYY-MM-DD
        sources.yml 기준 RSS/GitHub/HN 수집
        신규 항목만 .raw/YYYY-MM-DD.json 저장
        data/seen.json 업데이트

    → summarize.py --date YYYY-MM-DD --backend=claude-cli
        기본: claude -p 헤드리스 호출 (Max 플랜 사용량, 비용 0)
        대안: --backend=api (anthropic SDK, 토큰당 과금)
        캐시: .cache/summary_{hash}.json (동일 항목 재요약 방지)
        출력: .summarized/YYYY-MM-DD.json

    → publish.py --date YYYY-MM-DD
        카테고리별 그룹화 마크다운 생성
        출력: _posts/YYYY-MM-DD-llm-mcp-daily.md

    → git commit & push (변경 있을 때만)
        → GitHub Actions: Ruby 3.3 Jekyll 빌드 → GitHub Pages 배포
```

## Jekyll 설정 핵심

- 테마: `minimal-mistakes-jekyll` (gem 직접 사용, remote_theme 아님)
- `baseurl: /llm-mcp-weekly` — 이미지·링크 경로는 `/assets/...` 형태로 작성 (baseurl 중복 방지)
- `_layouts/post.html`에 반드시 `{{ content }}` 포함 — 없으면 본문 전체 누락
- 플러그인: jekyll-feed, jekyll-seo-tag, jekyll-sitemap, jekyll-paginate, jekyll-include-cache
- `future: true` — 06:00~09:00 실행 시 당일 포스트 누락 방지

## 수동 실행

```bash
# 파이프라인 전체 수동 실행
launchctl start com.prscsl.llm-mcp-weekly.daily

# 단계별 직접 실행 (디버그용)
cd ~/llm-mcp-weekly/scripts
python3 collect.py --date 2026-04-23
python3 summarize.py --date 2026-04-23 --backend=claude-cli
python3 publish.py --date 2026-04-23

# 로그 확인
tail -f ~/llm-mcp-weekly/logs/$(date +%Y-%m-%d).log
cat /tmp/llm-mcp-weekly.stdout.log
cat /tmp/llm-mcp-weekly.stderr.log
```

## 소스 추가 방법

`data/sources.yml` 편집:
- `rss`: url, weight(1~10), tags
- `github_releases`: repo(org/repo), weight, tags
- `hn`: query(검색어), weight, tags

## 알려진 주의사항

- `_config.yml`의 `logo:`, `og_image:` 값에 `/llm-mcp-weekly/` 접두어 붙이지 말 것 → 이중 경로 404
- `_layouts/post.html`에서 `{{ content }}` 삭제 시 모든 포스트 본문 사라짐
- LaunchAgent는 로그인 세션(Aqua)에서만 동작 — Mac이 06:00 이전에 로그인 상태여야 실행됨
- launchd는 놓친 일정을 소급 실행하지 않음 → 수동: `launchctl start com.prscsl.llm-mcp-weekly.daily`
