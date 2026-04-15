# Windows Task Scheduler에서 llm-mcp-weekly-daily 태스크 제거.
#
# 사용:
#   powershell -ExecutionPolicy Bypass -File scripts\uninstall_task.ps1

$TaskName = "llm-mcp-weekly-daily"

$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if (-not $existing) {
    Write-Host "태스크가 등록되어 있지 않음: $TaskName"
    exit 0
}

Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
Write-Host "✓ 제거 완료: $TaskName"
