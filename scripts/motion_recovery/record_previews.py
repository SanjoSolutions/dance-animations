"""Record source, model, and media revisions for reviewed playback highlights."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'docs/animation_work_status/priority_recovery'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    entries = {entry['id']: entry for entry in catalog['animations']}
    results = []
    for path in sorted(OUTPUT.glob('*.mp4')):
        identifier = path.stem
        directory = ROOT / '.cache/motion-recovery' / identifier
        report = json.loads((directory / 'checkpoint.json').read_text())
        capture = json.loads((directory / 'preview-source.json').read_text())
        assert capture['sourceSha256'] == report['sourceSha256']
        assert capture['exportSha256'] == report['exportSha256']
        entry = entries[identifier]
        wardrobe = catalog['wardrobe']
        profile = next((profile for profile in wardrobe['profiles'].values() if entry['style'] in profile['styles']),
                       wardrobe['profiles'][wardrobe['default']])
        models = {actor: dict(file=model['file'], sha256=digest(ROOT / model['file'])) for actor, model in profile['models'].items()}
        results.append(dict(id=identifier, file=str(path.relative_to(ROOT)), sha256=digest(path),
                            capture=capture, models=models, installedSourceSha256=entry['sourceSha256'],
                            installedExportSha256=digest(ROOT / entry['file'])))
    (OUTPUT / 'previews.json').write_text(json.dumps(results, indent=2) + '\n')
    print('Hash-matched playback previews', len(results))


if __name__ == '__main__':
    main()
