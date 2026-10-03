"""Package the bundled Game Rig Tools fork for Blender's Install from Disk."""
from pathlib import Path
import tomllib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'scripts/blender/extensions/game_rig_tools'


def main():
    manifest = tomllib.loads((SOURCE / 'blender_manifest.toml').read_text())
    destination = ROOT / 'tools' / f'game-rig-tools-dance-animations-{manifest["version"]}.zip'
    destination.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(SOURCE.rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc':
                archive.write(path, path.relative_to(SOURCE).as_posix())
    with zipfile.ZipFile(destination) as archive:
        assert {'__init__.py', 'blender_manifest.toml', 'LICENSE', 'NOTICE.md'} <= set(archive.namelist())
    print('Blender extension archive:', destination.relative_to(ROOT), destination.stat().st_size, 'bytes')


if __name__ == '__main__':
    main()
