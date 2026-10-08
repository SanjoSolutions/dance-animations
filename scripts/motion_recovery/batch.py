"""Run isolated source writers and fresh-process validators with durable logs."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]


def run(identifier):
    directory = ROOT / '.cache/motion-recovery' / identifier
    directory.mkdir(parents=True, exist_ok=True)
    result = dict(id=identifier)
    for phase in ('repair', 'validate'):
        with (directory / (phase + '.log')).open('w') as log:
            process = subprocess.run(['blender', '-t', '2', '--background', '--factory-startup',
                                      '--python-exit-code', '1', '--python',
                                      f'scripts/motion_recovery/{phase}.py', '--', identifier],
                                     cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
        result[phase] = process.returncode
        if process.returncode:
            break
    (directory / 'process.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--styles', nargs='+', default=['hip_hop', 'salsa'])
    parser.add_argument('--clips', nargs='+')
    parser.add_argument('--workers', type=int, default=3)
    arguments = parser.parse_args()
    records = json.loads((ROOT / 'catalog.json').read_text())['animations']
    selected = arguments.clips or [record['id'] for record in records if record['style'] in arguments.styles]
    directory = ROOT / '.cache/motion-recovery'
    directory.mkdir(parents=True, exist_ok=True)
    manifest = dict(clips=selected, generators={name: hashlib.sha256((Path(__file__).parent / name).read_bytes()).hexdigest()
                                               for name in ('repair.py', 'validate.py', 'batch.py')})
    (directory / 'batch.json').write_text(json.dumps(manifest, indent=2) + '\n')
    with ThreadPoolExecutor(max_workers=arguments.workers) as pool:
        results = list(pool.map(run, selected))
    (directory / 'batch-results.json').write_text(json.dumps(results, indent=2) + '\n')
    assert all(result.get('validate') == 0 for result in results), 'Review the per-clip diagnostics'


if __name__ == '__main__':
    main()
