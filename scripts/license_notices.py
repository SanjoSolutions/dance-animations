"""Collect supplied dependency licenses and asset credits for distribution."""
import html
import json
from pathlib import Path
import shutil
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from import_assets import read_glb, write_glb

ROOT = Path(__file__).resolve().parents[1]


class LicenseNotices:
    def __init__(self):
        self.destination = ROOT / 'public/third-party'
        self.destination.mkdir(parents=True, exist_ok=True)

    def collect_packages(self):
        packages = json.loads((ROOT / 'package-lock.json').read_text())['packages']
        sections = []
        for folder in sorted(packages):
            directory = ROOT / folder
            if folder and directory.is_dir():
                package = json.loads((directory / 'package.json').read_text())
                files = sorted(path for path in directory.iterdir() if path.is_file()
                               and path.name.lower().startswith(('license', 'copying', 'notice')))
                # Platform-specific build binaries use their parent package's license.
                if not files and package['name'].startswith('@esbuild/'):
                    files = [ROOT / 'node_modules/esbuild/LICENSE.md']
                if not files and package['name'].startswith('@rollup/rollup-'):
                    files = [ROOT / 'node_modules/rollup/LICENSE.md']
                if not files:
                    raise ValueError('Supply the original license notice for ' + package['name'])
                heading = f"{package['name']} {package['version']} ({package.get('license', 'see notice')})"
                sections.append(heading + '\n' + '\n'.join(path.read_text(encoding='utf-8') for path in files))
        sections.append('Embedded meshoptimizer 0.22 decoder in Three.js\n' +
                        (self.destination / 'meshoptimizer-0.22-MIT.txt').read_text())
        (self.destination / 'npm-notices.txt').write_text('\n\n'.join(sections) + '\n', newline='\n')

    def collect_assets(self):
        assets = json.loads((ROOT / 'assets/mpfb/attribution.json').read_text())
        sections = [(ROOT / 'licenses/makehuman-base-notice.txt').read_text()]
        rows = []
        for folder, record in assets.items():
            directory = ROOT / 'assets/mpfb' / folder
            headers = sorted(directory.glob('*.mhclo')) or sorted(directory.glob('*.mhmat'))
            if not headers:
                raise ValueError('Supply original asset notices for ' + folder)
            source = '\n'.join(line for path in headers for line in path.read_text(errors='replace').splitlines()
                               if line.startswith('#') or line.startswith('name '))
            license = ' '.join(record['license'].split())
            if license.startswith('CC0'):
                identifier = 'CC0-1.0'
            elif license == 'CC BY 3.0':
                identifier = 'CC-BY-3.0'
            elif license == 'CC BY 4.0':
                identifier = 'CC-BY-4.0'
            else:
                raise ValueError('Review the asset license for ' + folder + ': ' + license)
            title = next((line[5:] for line in source.splitlines() if line.startswith('name ')), folder)
            record['title'] = title
            record['licenseUrl'] = {'CC0-1.0': 'https://creativecommons.org/publicdomain/zero/1.0/',
                                    'CC-BY-3.0': 'https://creativecommons.org/licenses/by/3.0/',
                                    'CC-BY-4.0': 'https://creativecommons.org/licenses/by/4.0/'}[identifier]
            sections.append(f'{folder}\n{json.dumps(record, indent=2)}\n{source}')
            rows.append('<tr>' + ''.join(f'<td>{html.escape(value)}</td>' for value in (title, record['author'])) +
                        f'<td><a href="third-party/{identifier}.txt">{html.escape(license)}</a></td>' +
                        f'<td><a href="{html.escape(record["source"])}">Source</a></td></tr>')
        text = json.dumps(assets, indent=2) + '\n'
        (ROOT / 'assets/mpfb/attribution.json').write_text(text, newline='\n')
        (self.destination / 'asset-notices.txt').write_text('\n\n'.join(sections) + '\n', newline='\n')
        return '\n'.join(rows)

    def write(self):
        self.collect_packages()
        rows = self.collect_assets()
        shutil.copyfile(ROOT / 'LICENSE', self.destination / 'project-MIT-0.txt')
        shutil.copyfile(ROOT / 'scripts/blender/extensions/game_rig_tools/LICENSE', self.destination / 'GPL-3.0.txt')
        page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Asset credits and license terms for Dance animations.">
<title>Licenses and credits · Dance animations</title>
<link rel="stylesheet" href="/src/legal.css">
</head>
<body>
<div class="legal-page credits-page">
<header><a href="./">Dance animations</a></header>
<main>
<h1>Licenses and credits</h1>
<p>Original project content uses MIT-0 adapted to content. Third-party assets and code retain their licenses.</p>
<p><a href="third-party/project-MIT-0.txt">Project license</a> · <a href="third-party/npm-notices.txt">Dependency licenses and copyrights</a> · <a href="third-party/asset-notices.txt">Original asset notices and modifications</a></p>
<h2>Characters and clothing</h2>
<p>MakeHuman/MPFB hm08 base mesh and system assets: Data Collection AB, Joel Palmius, Jonas Hauquier; <a href="third-party/CC0-1.0.txt">CC0</a> (September 2020 release).</p>
<div class="table-responsive" tabindex="0" role="region" aria-label="Character and clothing credits">
<table class="table"><thead><tr><th scope="col">Asset</th><th scope="col">Author</th><th scope="col">License</th><th scope="col">Source</th></tr></thead><tbody>{rows}</tbody></table>
</div>
<p>Adaptations: character fitting, deformation weights, body coverage masks, PBR material conversion, and Blender/glTF packaging. The navy suit's tie geometry was removed. Full-length practice garments include additional body masks. Preserve the relevant asset credits when redistributing character models.</p>
<h2>Blender authoring code</h2>
<p>Game Rig Tools: TinkerBoi/CGDive and contributors; <a href="third-party/GPL-3.0.txt">GPL version 3</a>, allowed by its GPL-2.0-or-later manifest. Complete modified source, changelog, and installation archive are included in the repository.</p>
<p>Embedded Rigify UI scripts: Blender Foundation and contributors; <a href="third-party/GPL-2.0.txt">GPL-2.0-or-later</a>. Readable copies accompany the studio files in the repository.</p>
<h2>Website dependencies</h2><p>Three.js, Bootstrap, and the meshoptimizer 0.22 decoder use MIT. Their full notices accompany this site.</p>
</main>
<footer class="legal-footer"><nav aria-label="Legal information"><a href="./imprint.html">Imprint</a><a href="./privacy.html">Privacy notice</a><a href="./licenses.html" aria-current="page">Licenses and credits</a></nav></footer>
</div>
</body>
</html>'''
        (ROOT / 'licenses.html').write_text(page + '\n', newline='\n')
        self.credit_models()
        print('Collected dependency licenses, original asset notices, and website credits.')

    @staticmethod
    def credit_models():
        assets = json.loads((ROOT / 'assets/mpfb/attribution.json').read_text())
        wardrobe = json.loads((ROOT / 'wardrobe.json').read_text())
        for path in sorted((ROOT / 'models').rglob('*.glb')):
            document, binary = read_glb(path)
            if document.get('skins'):
                actor = 'man' if path.name == 'mpfb-man.glb' else 'woman'
                clothes = set()
                if path.parent.parent.name == 'wardrobe':
                    clothes = set(wardrobe['profiles'][path.parent.name][actor])
                credits = [dict(asset='MakeHuman hm08 base mesh', author='Data Collection AB, Joel Palmius, Jonas Hauquier',
                                license='CC0 1.0', licenseUrl='https://creativecommons.org/publicdomain/zero/1.0/',
                                source='https://static.makehumancommunity.org/', changes='Fitted standard body, skinning, Blender/glTF packaging.')]
                credits.extend(dict(asset=folder, **record) for folder, record in assets.items()
                               if not folder.startswith('clothes/') or folder.removeprefix('clothes/') in clothes)
                document['asset']['copyright'] = 'MakeHuman asset authors. See asset.extras.credits for authors, licenses, sources, and modifications.'
                document['asset'].setdefault('extras', {})['credits'] = credits
                write_glb(path, document, binary)


if __name__ == '__main__':
    LicenseNotices().write()
