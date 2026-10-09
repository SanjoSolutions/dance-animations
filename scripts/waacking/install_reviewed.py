"""Install the 16 reviewed Waacking candidates through the native recovery writer."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/motion_recovery'))
from install import CandidateInstaller, digest


def main():
    installer = CandidateInstaller()
    identifiers = [entry['id'] for entry in installer.catalog['animations'] if entry['style'] == 'waacking']
    assert len(identifiers) == 16, identifiers
    for identifier in identifiers:
        directory = ROOT / '.cache/motion-recovery' / identifier
        checkpoint = json.loads((directory / 'checkpoint.json').read_text())
        for name in ('motion-review', 'clearance'):
            review = json.loads((directory / (name + '.json')).read_text())
            assert review['sourceSha256'] == checkpoint['sourceSha256'] and review['passed'], (identifier, name)
            assert review['exportSha256'] == checkpoint['exportSha256']
            if name == 'clearance':
                assert all(count > 0 for count in review['regionPolygons'].values())
        visual = json.loads((directory / 'visual-capture.json').read_text())
        assert visual['sourceSha256'] == checkpoint['sourceSha256']
        assert visual['exportSha256'] == checkpoint['exportSha256']
        assert digest(ROOT / visual['contactSheet']['file']) == visual['contactSheet']['sha256']
        assert visual.get('reviewDisposition') == 'sampled poses reviewed', identifier
    for identifier in identifiers:
        installer.install(identifier)
        entry = installer.entries[identifier]
        entry['status'] = 'Native deformation bake'
        entry['studyStatus'] = 'Procedural study; source, bake, runtime, sampled surfaces and poses reviewed'
        entry['reviewRecord'] = f'docs/animation_work_status/waacking_repair/{identifier}.json'
        installer.sources[identifier]['runtimeExport'] = entry['file']
        installer.save_catalogs()
    for path in (installer.catalog_path, installer.inventory_path):
        path.write_bytes(path.read_text().encode('utf-8'))


if __name__ == '__main__':
    main()
