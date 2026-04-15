# 한국어 LLM·MCP 위클리

Claude·MCP·LLM 생태계 소식을 매일 자동 큐레이션·한국어 요약하는 Jekyll 블로그.

`/Users/prscsl/.claude/plans/logical-snuggling-sutherland.md` 의 **모델 1 (니치 큐레이션 사이트)** 구현체.

## 아키텍처

```
[RSS / GitHub / HN]  →  collect.py  →  .raw/YYYY-MM-DD.json
                                         ↓
                       summarize.py  →  .summarized/YYYY-MM-DD.json
                       (claude -p, Max 플랜)
                                         ↓
                         publish.py  →  _posts/YYYY-MM-DD-llm-mcp-daily.md
                                         ↓
                              GitHub Pages (Jekyll)  →  공개 사이트
```

## 두 가지 운영 모델

| 항목 | **Max 플랜 + launchd (권장)** | API + GitHub Actions |
|------|-----------------------------|---------------------|
| 비용 | **0원** (Max 플랜에 포함) | ~$1.5/월 (별도 결제) |
| 백엔드 | `claude -p` 헤드리스 | anthropic SDK |
| 스케줄 | macOS launchd | GitHub Actions cron |
| PC 의존 | 켜져 있어야 함 (sleep도 launchd가 깨움) | 없음 |
| 셋업 난이도 | 쉬움 (plist 1개 로드) | 중간 (secret·permissions 설정) |
| 적합 케이스 | 개인 PC가 항시 가동 중 | 클라우드 무인 운영 필요 |

## 디렉토리 구조

```
llm-mcp-weekly/
├── _config.yml              ← Jekyll 사이트 설정
├── Gemfile                  ← Ruby 의존성
├── requirements.txt         ← Python 의존성
├── index.md / about.md      ← 정적 페이지
├── _posts/                  ← 자동 생성된 일일 큐레이션 (커밋됨)
├── data/
│   ├── sources.yml          ← RSS·GitHub·HN 소스 정의
│   └── seen.json            ← 중복 방지 해시 (커밋됨)
├── scripts/
│   ├── collect.py           ← 외부 소스 수집
│   ├── summarize.py         ← Claude API 요약
│   └── publish.py           ← Jekyll 마크다운 생성
├── .raw/                    ← 수집 원본 (gitignore)
├── .summarized/             ← 요약 결과 (gitignore)
├── .cache/                  ← 항목별 요약 캐시 (gitignore)
└── .github/workflows/daily.yml  ← 매일 06:00 KST 자동 실행
```

## 로컬 실행

### 사전 준비

```bash
cd llm-mcp-weekly
pip3 install -r requirements.txt

# Max 플랜 사용 시: claude CLI만 있으면 됨 (별도 API 키 불필요)
claude --version

# API 백엔드 사용 시에만:
# export ANTHROPIC_API_KEY="sk-ant-..."
```

Jekyll 미리보기는 별도로 Ruby 환경 필요 (선택):

```bash
gem install bundler
bundle install
bundle exec jekyll serve  # http://localhost:4000
```

### 파이프라인 수동 실행

```bash
# 1. 외부 소스 수집 (오늘 날짜)
python3 scripts/collect.py

# 2. 한국어 요약 (Max 플랜 사용, 비용 0)
python3 scripts/summarize.py --backend=claude-cli

# 또는 API 사용 (별도 과금)
# python3 scripts/summarize.py --backend=api

# 3. Jekyll 포스트 생성
python3 scripts/publish.py
```

각 스크립트는 `--date YYYY-MM-DD`로 특정 날짜 처리 가능.

### Dry-run (외부 호출 없이 구조 확인)

```bash
python3 scripts/collect.py --dry-run
python3 scripts/summarize.py --dry-run
python3 scripts/publish.py
```

## launchd 셋업 (Max 플랜 모드, 권장)

```bash
# 1. plist 설치
cp scripts/com.prscsl.llm-mcp-weekly.daily.plist ~/Library/LaunchAgents/

# 2. 로드 (다음 06:00부터 매일 자동 실행)
launchctl load ~/Library/LaunchAgents/com.prscsl.llm-mcp-weekly.daily.plist

# 3. 즉시 1회 실행 테스트
launchctl start com.prscsl.llm-mcp-weekly.daily

# 4. 로그 확인
tail -f logs/$(date +%Y-%m-%d).log
tail -f /tmp/llm-mcp-weekly.stderr.log

# 제거
launchctl unload ~/Library/LaunchAgents/com.prscsl.llm-mcp-weekly.daily.plist
```

**Mac sleep 대응**: `pmset` 또는 시스템 환경설정 → 에너지 절약자 → "예약된 시간에 켜기"로 매일 05:55 wake 설정 권장.

## Windows 이전 가이드 (개인 노트북)

macOS launchd와 등가인 Windows Task Scheduler 버전이 `scripts/*.ps1`에 포함되어 있습니다.

### 전제
- Windows 10/11, 개인 소유, 인터넷 연결
- Claude Max 플랜 로그인 가능 (브라우저 OAuth)
- **주의**: macOS와 Windows를 동시에 돌리면 git push 충돌 — 반드시 한쪽만 활성화

### 1단계 — 필수 도구 설치 (새 PowerShell 창)

```powershell
winget install Python.Python.3.10
winget install OpenJS.NodeJS.LTS
winget install Git.Git
# 설치 후 창을 새로 열어 PATH 반영 확인
python --version; node --version; git --version
```

### 2단계 — Claude Code 설치 + Max 플랜 로그인

```powershell
npm install -g @anthropic-ai/claude-code
claude login          # 브라우저 OAuth로 Max 플랜 인증
claude --version
```

### 3단계 — 프로젝트 clone + Python 의존성

```powershell
cd $env:USERPROFILE
git clone https://github.com/prscsl/llm-mcp-weekly.git
cd llm-mcp-weekly
pip install -r requirements.txt
```

### 4단계 — 수동 1회 테스트

```powershell
powershell -ExecutionPolicy Bypass -File scripts\run_daily.ps1
# 로그: logs\<오늘>.log
```

### 5단계 — Task Scheduler 등록 (매일 06:00 자동)

```powershell
powershell -ExecutionPolicy Bypass -File scripts\install_task.ps1
Start-ScheduledTask -TaskName llm-mcp-weekly-daily    # 즉시 테스트
```

### 6단계 — 절전/배터리 설정

Task Scheduler 자체에 `-WakeToRun`·`-AllowStartIfOnBatteries`가 포함되어 있지만, 설정 → 시스템 → 전원 및 절전 → **"절전 모드 해제 타이머 허용"을 ON**으로 확인.

### 7단계 — macOS 자동화 정지 (Windows 검증 완료 후)

```bash
# 맥에서 실행
launchctl unload ~/Library/LaunchAgents/com.prscsl.llm-mcp-weekly.daily.plist
sudo pmset repeat cancel
```

### 제거

```powershell
powershell -ExecutionPolicy Bypass -File scripts\uninstall_task.ps1
```

## 비용 추정

| 모드 | 월 비용 | 비고 |
|------|---------|-----|
| **Max 플랜 + launchd** | **0원** | Max 플랜 사용량 풀 차감 |
| API + GitHub Actions | ~$1.5 | Haiku 4.5, 하루 30건 기준 |
| GitHub Pages | 0원 | 무료 호스팅 |
| 도메인 (선택) | 연 $10~15 | gh-pages 서브도메인 사용 시 0원 |

## GitHub Pages 활성화

1. 본 디렉토리를 GitHub 저장소로 push
2. 저장소 Settings → Pages → Source: `Deploy from a branch`, Branch: `main` / `(root)`
3. 약 1~2분 후 `https://<username>.github.io/<repo>/`에서 사이트 확인

## (선택) GitHub Actions 셋업 — API 백엔드용

Max 플랜 launchd 대신 GitHub Actions로 무인 운영하려면:

1. Settings → Secrets → Actions → 신규 시크릿: `ANTHROPIC_API_KEY` = `sk-ant-...`
2. Settings → Actions → General → Workflow permissions: `Read and write permissions` 체크
3. `.github/workflows/daily.yml`은 이미 포함됨 — Actions 탭에서 수동 트리거로 첫 실행 검증

## 운영 체크리스트

- **주 1회 (5분)**: 자동 발행된 포스트 1~2개 샘플 확인. 이상한 요약 발견 시 수정
- **월 1회 (30분)**: `data/sources.yml`에 새 소스 추가 / 약한 소스 제거
- **분기 1회 (1시간)**: Google Search Console로 검색 트래픽 확인. 인기 키워드를 사이트 SEO에 반영

## 수익화 단계

1. **사이트 개설 + 1개월**: 콘텐츠 30개 누적 → AdSense 신청
2. **3~6개월**: SEO 누적, 월 방문 1만 도달 시도
3. **6개월~**: 월 방문 5만 → 월 30~50만원 광고 수익 (주제·CPC에 따라 변동)

## 라이선스

- 코드: MIT
- 콘텐츠: 각 항목의 원저작권자에게 귀속, 본 사이트는 한국어 요약과 원문 링크만 제공
