#!/bin/zsh
# 매일 자동 실행되는 큐레이션 파이프라인 (launchd가 호출).
#
# 흐름: collect → summarize (claude -p) → publish → git push
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

log "=== 큐레이션 시작: $DATE ==="

run_step "collect.py" python3 scripts/collect.py --date "$DATE" || exit 1
run_step "summarize.py (claude-cli)" python3 scripts/summarize.py --date "$DATE" --backend=claude-cli || exit 1
run_step "publish.py" python3 scripts/publish.py --date "$DATE" || exit 1

# git push (변경 있을 때만)
if git diff --quiet _posts/ data/seen.json; then
  log "변경 없음 — push 스킵"
else
  log "▶ git commit & push"
  git add _posts/ data/seen.json >> "$LOG_FILE" 2>&1
  git -c user.name="llm-mcp-weekly-bot" -c user.email="bot@local" \
    commit -m "chore: daily curation $DATE" >> "$LOG_FILE" 2>&1
  if git push origin main >> "$LOG_FILE" 2>&1; then
    log "✓ push 완료"
  else
    log "✗ push 실패 — 수동 처리 필요"
    exit 1
  fi
fi

log "=== 완료 ==="
exit 0
