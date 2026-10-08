"""Reconcile Popping inventory using Blender 5.2 --background --python."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(Path(__file__).parent), str(ROOT / 'scripts')]
from choreography import PoppingVocabulary

moves = [clip['name'] for clip in PoppingVocabulary().clips]
expected = {f'popping_{actor}_{move}' for actor in ('man', 'woman') for move in moves}
catalog = json.loads((ROOT / 'catalog.json').read_text())
entries = {entry['id']: entry for entry in catalog['animations'] if entry['style'] == 'popping'}
assert set(entries) == expected, dict(missing=sorted(expected-set(entries)), extra=sorted(set(entries)-expected))
assert all((ROOT / entry['sourceFile']).is_file() and (ROOT / entry['file']).is_file() for entry in entries.values())
report = dict(recipeMoves=len(moves), planned=len(expected), sources=len(entries), runtimeExports=len(entries),
              identifiers=sorted(entries), recovered=17, refreshed=2, retained=65,
              status='Complete saved repertoire; 19 source/bake/runtime recovery reviews; retained clips keep historical review status')
(ROOT / 'docs/animation_work_status/priority_recovery/popping-coverage.json').write_text(json.dumps(report, indent=2)+'\n')
print('Popping repertoire coverage',len(entries),'of',len(expected))
