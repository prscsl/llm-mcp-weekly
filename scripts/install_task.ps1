# Windows Task Scheduler 등록 스크립트.
#
# 사용 (관리자 권한 PowerShell):
#   powershell -ExecutionPolicy Bypass -File scripts\install_task.ps1
#
# 매일 06:00에 run_daily.ps1 실행. 노트북이 sleep이어도 깨워 실행.
# 배터리 전원에서도 실행 (노트북 사용 고려).

$TaskName = "llm-mcp-weekly-daily"
$ProjectDir = Join-Path $env:USERPROFILE "llm-mcp-weekly"
$ScriptPath = Join-Path $ProjectDir "scripts\run_daily.ps1"

if (-not (Test-Path $ScriptPath)) {
    Write-Error "스크립트를 찾을 수 없음: $ScriptPath"
    exit 1
}

# 기존 태스크 제거 (있으면)
$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "기존 태스크 제거 중..."
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

$Action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-ExecutionPolicy Bypass -WindowStyle Hidden -File `"$ScriptPath`"" `
    -WorkingDirectory $ProjectDir

$Trigger = New-ScheduledTaskTrigger -Daily -At 6am

$Settings = New-ScheduledTaskSettingsSet `
    -WakeToRun `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 15)

$Principal = New-ScheduledTaskPrincipal `
    -UserId $env:USERNAME `
    -LogonType Interactive `
    -RunLevel Limited

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $Action `
    -Trigger $Trigger `
    -Settings $Settings `
    -Principal $Principal `
    -Description "LLM·MCP 위클리 매일 자동 큐레이션 (06:00 KST)" `
    -Force

Write-Host "`n✓ Task Scheduler 등록 완료: $TaskName"
Write-Host "`n=== 등록된 태스크 정보 ==="
Get-ScheduledTask -TaskName $TaskName | Format-List TaskName, State, Description
Get-ScheduledTaskInfo -TaskName $TaskName | Format-List LastRunTime, NextRunTime, LastTaskResult

Write-Host "`n즉시 1회 실행 테스트:"
Write-Host "  Start-ScheduledTask -TaskName $TaskName"
Write-Host "`n로그 모니터링:"
Write-Host "  Get-Content logs\$(Get-Date -Format yyyy-MM-dd).log -Wait -Tail 20"
