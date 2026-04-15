# Windows 매일 자동 실행 파이프라인 (Task Scheduler가 호출).
# run_daily.sh (zsh)의 PowerShell 포트.
#
# 흐름: collect → summarize (claude -p) → publish → git push
# 로그: logs\YYYY-MM-DD.log
# 종료 코드: 0 성공, 1 실패

$ErrorActionPreference = "Continue"
$ProjectDir = Join-Path $env:USERPROFILE "llm-mcp-weekly"
Set-Location -LiteralPath $ProjectDir

$Date = Get-Date -Format "yyyy-MM-dd"
$LogDir = Join-Path $ProjectDir "logs"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$LogFile = Join-Path $LogDir "$Date.log"

# 콘솔·파일 출력 UTF-8 강제 (한글 깨짐 방지)
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

function Write-Log {
    param([string]$Msg)
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line = "[$ts] $Msg"
    Write-Host $line
    $line | Out-File -FilePath $LogFile -Append -Encoding utf8
}

function Invoke-Step {
    param([string]$Name, [scriptblock]$Block)
    Write-Log "▶ $Name"
    & $Block *>&1 | Tee-Object -FilePath $LogFile -Append
    if ($LASTEXITCODE -eq 0) {
        Write-Log "✓ $Name 완료"
        return $true
    }
    Write-Log "✗ $Name 실패 (exit $LASTEXITCODE)"
    return $false
}

Write-Log "=== 큐레이션 시작: $Date ==="

if (-not (Invoke-Step "collect.py"             { python scripts\collect.py --date $Date })) { exit 1 }
if (-not (Invoke-Step "summarize.py (claude-cli)" { python scripts\summarize.py --date $Date --backend=claude-cli })) { exit 1 }
if (-not (Invoke-Step "publish.py"             { python scripts\publish.py --date $Date })) { exit 1 }

# 변경 감지 후 git push
& git diff --quiet _posts/ data/seen.json
if ($LASTEXITCODE -eq 0) {
    Write-Log "변경 없음 — push 스킵"
} else {
    Write-Log "▶ git commit & push"
    & git add _posts/ data/seen.json | Tee-Object -FilePath $LogFile -Append
    & git -c user.name="llm-mcp-weekly-bot" -c user.email="bot@local" commit -m "chore: daily curation $Date" | Tee-Object -FilePath $LogFile -Append
    & git push origin main *>&1 | Tee-Object -FilePath $LogFile -Append
    if ($LASTEXITCODE -eq 0) {
        Write-Log "✓ push 완료"
    } else {
        Write-Log "✗ push 실패 — 수동 확인 필요"
        exit 1
    }
}

Write-Log "=== 완료 ==="
exit 0
