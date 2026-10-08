"""List completed paired candidates awaiting installation."""
import json
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--runtime-checked', action='store_true')
parser.add_argument('--runtime-pending', action='store_true')
arguments = parser.parse_args()
identifiers = []
for path in sorted((ROOT / '.cache/motion-recovery').glob('*/checkpoint.json')):
    report = json.loads(path.read_text())
    if report['style'] in ('salsa', 'new_york_hustle') and report['stage'] == 'saved source and bake validated':
        directory = path.parent
        required = ['contacts', 'surfaces'] + (['loop'] if report['loop'] else [])
        if all((directory / (name + '.json')).exists() for name in required):
            checks = {name: json.loads((directory / (name + '.json')).read_text()) for name in required}
            ready = checks['contacts']['passed'] and checks['contacts']['sourceSha256'] == report['sourceSha256']
            ready &= checks['surfaces']['exportSha256'] == report['exportSha256']
            ready &= min(foot['minimum'] for foot in checks['surfaces']['feet']) >= -.002
            if report['loop']:
                ready &= checks['loop']['passed'] and checks['loop']['exportSha256'] == report['exportSha256']
            installed = directory / 'installation.json'
            if installed.exists():
                ready &= json.loads(installed.read_text())['candidateSourceSha256'] != report['sourceSha256']
            runtime_path = directory / 'runtime.json'
            checked = False
            if runtime_path.exists():
                runtime = json.loads(runtime_path.read_text())
                current = runtime['sourceSha256'] == report['sourceSha256'] and runtime['exportSha256'] == report['exportSha256']
                ready &= not (current and not runtime['passed'])
                checked = current and runtime['passed']
            ready &= checked if arguments.runtime_checked else True
            ready &= not checked if arguments.runtime_pending else True
            if ready:
                identifiers.append(report['id'])
print(' '.join(identifiers))
