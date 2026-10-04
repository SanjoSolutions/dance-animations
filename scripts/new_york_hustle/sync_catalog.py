"""Reconcile completed Hustle export workers with the shared asset catalogs."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    catalog_path = ROOT / 'catalog.json'
    inventory_path = ROOT / 'source-inventory.json'
    catalog = json.loads(catalog_path.read_text())
    inventory = json.loads(inventory_path.read_text())
    sources = {entry['id']: entry for entry in inventory}
    completed = 0
    for entry in catalog['animations']:
        report_path = ROOT / '.cache/hustle-polish' / (entry['id'] + '.json')
        if entry['style'] == 'new_york_hustle' and report_path.is_file():
            report = json.loads(report_path.read_text())
            source = ROOT / entry['sourceFile']
            current = hashlib.sha256(source.read_bytes()).hexdigest()
            if current == report['sourceSha256']:
                entry.update(sourceSha256=current, animationName=report['animationName'],
                             duration=float(report['duration']), studyStatus='Procedural study; hand-contact polish')
                record = sources[entry['id']]
                record.setdefault('originalSha256', record['sha256'])
                record.update(sha256=current, bytes=source.stat().st_size, runtimeExport=entry['file'])
                completed += 1
    catalog_path.write_text(json.dumps(catalog, indent=2) + '\n')
    inventory_path.write_text(json.dumps(inventory, indent=2) + '\n')
    print(f'Reconciled {completed} Hustle source/export pairs.')


if __name__ == '__main__':
    main()
