"""Check redistributable model credits, runtime notices, and authoring archives."""
import json
import html
from pathlib import Path
import zipfile
from import_assets import read_glb

ROOT = Path(__file__).resolve().parents[1]


def main():
    music = json.loads((ROOT / 'music.json').read_text())
    music_notices = (ROOT / 'public/third-party/music-notices.txt').read_text(encoding='utf-8')
    credits = (ROOT / 'licenses.html').read_text(encoding='utf-8')
    for track in music['tracks']:
        assert track['license'] == 'CC-BY-4.0' and track['provenance'] and track['evidence']
        assert track['licenseUrl'] == 'https://creativecommons.org/licenses/by/4.0/'
        assert (ROOT / 'public' / track['licenseFile']).is_file()
        for value in (track['title'], track['author'], track['source'], track['changes']):
            assert value in music_notices, (track['style'], value)
            assert html.escape(value) in credits, (track['style'], value)
        assert track['sourceSha256'] in music_notices
        assert track['contributors'] in music_notices
    notices = (ROOT / 'public/third-party/npm-notices.txt').read_text()
    for name in ('three', 'bootstrap'):
        package = json.loads((ROOT / 'node_modules' / name / 'package.json').read_text())
        assert f'{name} {package["version"]}' in notices
        assert (ROOT / 'node_modules' / name / 'LICENSE').read_text() in notices
    assert (ROOT / 'public/third-party/meshoptimizer-0.22-MIT.txt').read_text() in notices
    assets = json.loads((ROOT / 'assets/mpfb/attribution.json').read_text())
    wardrobe = json.loads((ROOT / 'wardrobe.json').read_text())
    for profile, configuration in wardrobe['profiles'].items():
        for actor in ('man', 'woman'):
            document, _ = read_glb(ROOT / f'models/wardrobe/{profile}/mpfb-{actor}.glb')
            credits = {record['asset']: record for record in document['asset']['extras']['credits']}
            for identifier in configuration[actor]:
                credit = credits['clothes/' + identifier]
                assert credit['author'] == assets['clothes/' + identifier]['author']
                assert credit['licenseUrl'].startswith('https://creativecommons.org/')
                assert credit['source'].startswith('https://') and credit['changes'] and credit['title']
    with zipfile.ZipFile(ROOT / 'tools/game-rig-tools-dance-animations-4.3.0.zip') as archive:
        assert archive.read('LICENSE') == (ROOT / 'scripts/blender/extensions/game_rig_tools/LICENSE').read_bytes()
        assert archive.read('NOTICE.md') == (ROOT / 'scripts/blender/extensions/game_rig_tools/NOTICE.md').read_bytes()
        for path in (ROOT / 'scripts/blender/extensions/game_rig_tools').rglob('*.py'):
            assert archive.read(path.relative_to(ROOT / 'scripts/blender/extensions/game_rig_tools').as_posix()) == path.read_bytes()
    print('Runtime copyright notices, model credits, and complete GPL extension source passed.')


if __name__ == '__main__':
    main()
