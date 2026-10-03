# Download original recordings through Windows certificate validation.
$ErrorActionPreference = 'Stop'
$taskMusicRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '../..')).Path
$taskMusicSelections = Get-Content -LiteralPath (Join-Path $taskMusicRoot 'assets/music/selections.json') -Raw | ConvertFrom-Json
foreach ($taskMusicRecording in $taskMusicSelections.recordings.PSObject.Properties.Value) {
    $taskMusicDestination = Join-Path $taskMusicRoot $taskMusicRecording.sourceFile
    New-Item -ItemType Directory -Force -Path (Split-Path $taskMusicDestination) | Out-Null
    if (!(Test-Path -LiteralPath $taskMusicDestination)) {
        Invoke-WebRequest -Uri $taskMusicRecording.download -OutFile $taskMusicDestination
    }
    if ($taskMusicRecording.sourceSha256) {
        $taskMusicDigest = (Get-FileHash -LiteralPath $taskMusicDestination -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($taskMusicDigest -ne $taskMusicRecording.sourceSha256) {
            throw "Review the source hash for $($taskMusicRecording.title)."
        }
    }
}
