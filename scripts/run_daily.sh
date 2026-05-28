#!/bin/zsh
# 매일 자동 실행되는 큐레이션 파이프라인 (launchd가 호출).
#
# 흐름: collect → summarize (auto: claude-cli → ollama → codex-api) → publish → git push
# Mac이 꺼져 있던 기간이 있으면, 마지막 완료일 다음 날짜부터 오늘까지 자동 catch-up.
#
# 로그: logs/YYYY-MM-DD.log
# 종료 코드: 0 성공, 1 실패

set -u
PROJECT_DIR="${HOME}/llm-mcp-weekly"
cd "$PROJECT_DIR" || exit 1

DATE=$(date +%Y-%m-%d)
LOG_DIR="$PROJECT_DIR/logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/${DATE}.log"
SUMMARY_BACKEND="${SUMMARY_BACKEND:-ollama}"

# pyenv·nvm 등 사용자 PATH 로드 (launchd는 최소 환경으로 시작).
# nvm을 맨 앞에 둬야 claude CLI가 시스템 node(구버전)가 아닌 nvm node를 사용함.
NVM_NODE_BIN=$(ls -d $HOME/.nvm/versions/node/*/bin 2>/dev/null | sort -V | tail -1)
export PATH="${NVM_NODE_BIN}:$HOME/.pyenv/shims:$HOME/.pyenv/bin:/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

run_step() {
  local name="$1"
  shift
  log "▶ $name"
  if "$@" >> "$LOG_FILE" 2>&1; then
    log "✓ $name 완료"
    return 0
  else
    log "✗ $name 실패 (exit $?)"
    return 1
  fi
}

date_complete() {
  local target_date="$1"
  local post_file="$PROJECT_DIR/_posts/${target_date}-llm-mcp-daily.md"
  local summarized_file="$PROJECT_DIR/.summarized/${target_date}.json"

  if [[ -f "$post_file" ]]; then
    return 0
  fi

  if [[ -f "$summarized_file" ]]; then
    local item_count
    item_count=$(python3 - "$summarized_file" <<'PY'
import json, sys
from pathlib import Path
p = Path(sys.argv[1])
try:
    data = json.loads(p.read_text())
    print(len(data.get("items", [])))
except Exception:
    print(-1)
PY
)
    if [[ "$item_count" == "0" ]]; then
      return 0
    fi
  fi

  return 1
}

pending_dates() {
  python3 - "$PROJECT_DIR" "$DATE" <<'PY'
import json
import sys
from datetime import date, timedelta
from pathlib import Path

root = Path(sys.argv[1])
today = date.fromisoformat(sys.argv[2])
posts_dir = root / "_posts"
summ_dir = root / ".summarized"

completed = set()
post_dates = []

for post in posts_dir.glob("*-llm-mcp-daily.md"):
    try:
      d = date.fromisoformat(post.name[:10])
    except ValueError:
      continue
    completed.add(d)
    post_dates.append(d)

for summary in summ_dir.glob("*.json"):
    try:
      d = date.fromisoformat(summary.stem)
      data = json.loads(summary.read_text())
    except Exception:
      continue
    if len(data.get("items", [])) == 0:
      completed.add(d)

anchor = max(completed) if completed else today
current = anchor + timedelta(days=1)
while current <= today:
    if current not in completed:
        print(current.isoformat())
    current += timedelta(days=1)
PY
}

log "=== 큐레이션 시작: $DATE ==="

typeset -a DATES_TO_RUN
if [[ "${FORCE_RUN:-0}" == "1" ]]; then
  DATES_TO_RUN=("$DATE")
else
  while IFS= read -r line; do
    [[ -n "$line" ]] && DATES_TO_RUN+=("$line")
  done < <(pending_dates)
fi

if (( ${#DATES_TO_RUN[@]} == 0 )); then
  log "빠진 날짜가 없어 catch-up 없이 종료합니다."
  exit 0
fi

log "처리 대상 날짜: ${DATES_TO_RUN[*]}"

for TARGET_DATE in "${DATES_TO_RUN[@]}"; do
  if date_complete "$TARGET_DATE"; then
    log "이미 완료된 날짜라 건너뜁니다: $TARGET_DATE"
    continue
  fi

  log "--- $TARGET_DATE 처리 시작 ---"
  run_step "collect.py ($TARGET_DATE)" python3 scripts/collect.py --date "$TARGET_DATE" || exit 1
  run_step "summarize.py (${SUMMARY_BACKEND}, $TARGET_DATE)" python3 scripts/summarize.py --date "$TARGET_DATE" --backend "$SUMMARY_BACKEND" || exit 1
  run_step "publish.py ($TARGET_DATE)" python3 scripts/publish.py --date "$TARGET_DATE" || exit 1
  log "--- $TARGET_DATE 처리 완료 ---"
done

# git push (변경 있을 때만)
if git diff --quiet _posts/ data/seen.json; then
  log "변경 없음 — push 스킵"
else
  log "▶ git commit & push"
  git add _posts/ data/seen.json >> "$LOG_FILE" 2>&1
  git -c user.name="llm-mcp-weekly-bot" -c user.email="bot@local" \
    commit -m "chore: daily curation up to $DATE" >> "$LOG_FILE" 2>&1
  if git push origin main >> "$LOG_FILE" 2>&1; then
    log "✓ push 완료"
  else
    log "✗ push 실패 — 수동 처리 필요"
    exit 1
  fi
fi

log "=== 완료 ==="
exit 0
