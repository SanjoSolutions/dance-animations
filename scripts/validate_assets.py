"""Check asset coverage, provenance, GLB ranges, and GitHub Pages size limits."""
from collections import Counter
import hashlib
import gzip
import json
from pathlib import Path
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from import_assets import read_glb


def main():
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    sources = json.loads((ROOT / 'source-inventory.json').read_text())
    identifiers = set()
    sizes = []
    for entry in catalog['animations']:
        assert entry['id'] not in identifiers, f'Duplicate clip: {entry["id"]}'
        identifiers.add(entry['id'])
        path = ROOT / entry['file']
        assert path.is_file(), path
        assert path.relative_to(ROOT).parts[:2] == ('animations', entry['style'])
        document, binary = read_glb(path)
        assert len(document['animations']) == 1, entry['id']
        assert document['animations'][0]['name'] == entry['animationName'], entry['id']
        for view in document['bufferViews']:
            compression = view.get('extensions', {}).get('EXT_meshopt_compression')
            if compression:
                assert compression.get('byteOffset', 0) + compression['byteLength'] <= len(binary), path
            else:
                assert view.get('byteOffset', 0) + view['byteLength'] <= len(binary), path
        for animation in document['animations']:
            for sampler in animation['samplers']:
                times = document['accessors'][sampler['input']]
                values = document['accessors'][sampler['output']]
                assert times['count'] > 0 and values['count'] >= times['count'], entry['id']
        sizes.append(len(gzip.compress(path.read_bytes(), compresslevel=9, mtime=0)))
    for entry in sources:
        path = ROOT / entry['file']
        assert path.is_file(), path
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256'], path
    counts = Counter(entry['style'] for entry in catalog['animations'])
    for style in catalog['styles']:
        assert style['playable'] == counts[style['id']], style['id']
    for model in catalog['models'].values():
        document, _ = read_glb(ROOT / model['file'])
        assert document['meshes'] and document['skins'], model['file']
        assert not document.get('animations'), model['file']
        sizes.append((ROOT / model['file']).stat().st_size)
    sizes.extend((ROOT / prop['file']).stat().st_size for prop in catalog.get('props',{}).values())
    wardrobe = catalog.get('wardrobe')
    if wardrobe:
        assert wardrobe['default'] in wardrobe['profiles']
        for profile in wardrobe['profiles'].values():
            for model in profile['models'].values():
                path = ROOT / model['file']
                document, _ = read_glb(path)
                assert document['images'] and document['skins'], model['file']
                assert len(document['meshes']) > 1, model['file']
                sizes.append(path.stat().st_size)
    assert sum(sizes) < 1024**3, 'Runtime assets exceed the GitHub Pages 1 GiB site limit'
    print(f'Validated {len(identifiers)} clips, {len(sources)} source hashes, '
          f'{len(counts)} playable styles; runtime assets {sum(sizes)/1024**2:.1f} MiB.')


if __name__ == '__main__':
    main()
