param([string]$Script, [string[]]$Clips)
$ErrorActionPreference = 'Stop'
$projectDirectory = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$profileDirectory = Join-Path $projectDirectory '.cache/fusion-repair/profile'
$env:BLENDER_USER_RESOURCES = $profileDirectory
$env:BLENDER_USER_CONFIG = Join-Path $profileDirectory 'config'
$env:BLENDER_USER_SCRIPTS = Join-Path $profileDirectory 'scripts'
$env:BLENDER_USER_EXTENSIONS = Join-Path $profileDirectory 'extensions'
$env:TEMP = Join-Path $projectDirectory '.cache/fusion-repair/tmp'
$env:TMP = $env:TEMP
foreach ($clip in $Clips) {
    $logPath = Join-Path $projectDirectory ('.cache/fusion-repair/' + [IO.Path]::GetFileNameWithoutExtension($Script) + '-' + $clip + '.log')
    & 'C:\Program Files\Blender Foundation\Blender 5.2\blender.exe' --factory-startup --background --threads 2 --python-exit-code 1 --python $Script -- $clip *> $logPath
    $result = $LASTEXITCODE
    Write-Output "$clip : $result"
    if ($result -ne 0) { Get-Content $logPath -Tail 24; throw 'Inspect the clip log.' }
}
