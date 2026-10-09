param(
    [Parameter(Mandatory = $true)][string]$Script,
    [string[]]$Clips,
    [string]$Blender = 'C:\Program Files\Blender Foundation\Blender 5.2\blender.exe'
)
$ErrorActionPreference = 'Stop'
$taskRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$profileRoot = Join-Path $taskRoot '.cache/waacking-profile'
$temporaryDirectory = Join-Path $taskRoot '.cache/waacking-temp'
foreach ($directory in @($profileRoot, "$profileRoot/config", "$profileRoot/scripts", "$profileRoot/extensions", $temporaryDirectory)) {
    New-Item -ItemType Directory -Force $directory | Out-Null
}
$env:BLENDER_USER_RESOURCES = $profileRoot
$env:BLENDER_USER_CONFIG = Join-Path $profileRoot 'config'
$env:BLENDER_USER_SCRIPTS = Join-Path $profileRoot 'scripts'
$env:BLENDER_USER_EXTENSIONS = Join-Path $profileRoot 'extensions'
$env:TEMP = $temporaryDirectory
$env:TMP = $temporaryDirectory
Push-Location $taskRoot
try {
    & $Blender --factory-startup --background -t 2 --python-exit-code 1 --python $Script -- @Clips
    $result = $LASTEXITCODE
} finally {
    Pop-Location
}
exit $result
