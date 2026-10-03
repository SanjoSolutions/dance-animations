param([string]$Blender = 'C:\Program Files\Blender Foundation\Blender 5.2\blender.exe', [string]$Source = 'main.blend')
& $Blender --factory-startup (Join-Path $PSScriptRoot $Source) --python (Join-Path $PSScriptRoot 'scripts/open_studio.py')
