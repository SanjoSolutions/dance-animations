param([string[]]$Clips)
$ErrorActionPreference = 'Stop'
$taskRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$generatorPaths = @('scripts/fusion_repair/repair_supports.py','scripts/fusion_repair/review.py','scripts/fusion_repair/surfaces.mjs','scripts/fusion_repair/run.ps1','scripts/motion_recovery/repair.py','scripts/motion_recovery/validate.py','scripts/motion_recovery/runtime.mjs','scripts/motion_recovery/loop_review.mjs')
$revisions = @{}
foreach ($path in $generatorPaths) { $revisions[$path] = (Get-FileHash (Join-Path $taskRoot $path) -Algorithm SHA256).Hash.ToLower() }
@{clips=$Clips;generators=$revisions;workers=1} | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 (Join-Path $taskRoot '.cache/fusion-repair/batch.json')
$accepted = $true
foreach ($clip in $Clips) {
    $record = @{id=$clip;steps=@();accepted=$false}
    try {
        foreach ($script in @('scripts/fusion_repair/repair_supports.py','scripts/motion_recovery/validate.py','scripts/fusion_repair/review.py')) {
            & (Join-Path $PSScriptRoot 'run.ps1') -Script $script -Clips $clip
            $record.steps += @{script=$script;exitCode=0}
        }
        foreach ($script in @('scripts/motion_recovery/runtime.mjs','scripts/fusion_repair/surfaces.mjs','scripts/motion_recovery/loop_review.mjs')) {
            & node $script $clip
            $record.steps += @{script=$script;exitCode=$LASTEXITCODE}
        }
        $directory = Join-Path $taskRoot ('.cache/motion-recovery/' + $clip)
        $record.accepted = $true
        foreach ($name in @('contacts','runtime','surfaces','loop')) {
            $report = Get-Content (Join-Path $directory ($name + '.json')) -Raw | ConvertFrom-Json
            $record.accepted = $record.accepted -and $report.passed
        }
    } catch {
        $record.error = $_.ToString()
        Write-Output $record.error
    }
    $record | ConvertTo-Json -Depth 8 | Set-Content -Encoding utf8 (Join-Path $taskRoot ('.cache/fusion-repair/process-' + $clip + '.json'))
    $accepted = $accepted -and $record.accepted
    Write-Output ("CHECKPOINT " + $clip + " accepted=" + $record.accepted)
}

if (-not $accepted) { exit 1 }
