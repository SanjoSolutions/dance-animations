"""Run isolated House workers and checkpoint each completed source or export."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

from repertoire import CATALOG

ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stage', choices=('author', 'export', 'validate', 'finalize'))
    parser.add_argument('clips', nargs='*')
    parser.add_argument('--workers', type=int, default=3)
    parser.add_argument('--standing', action='store_true')
    parser.add_argument('--floor', action='store_true')
    parser.add_argument('--resume', action='store_true')
    arguments = parser.parse_args()
    names = arguments.clips or ['house_' + actor + '_' + phrase.name for phrase, module in CATALOG
                               if (module != 'floor' or not arguments.standing)
                               and (module == 'floor' or not arguments.floor)
                               for actor in ('man', 'woman')]
    subset = '-standing' if arguments.standing else '-floor' if arguments.floor else (
        '-' + hashlib.sha256('\n'.join(sorted(names)).encode()).hexdigest()[:8] if arguments.clips else '')
    directory = ROOT / '.cache/house' / (arguments.stage + subset + '-batch')
    directory.mkdir(parents=True, exist_ok=True)
    recipes = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
               for path in sorted(Path(__file__).parent.glob('*')) if path.suffix in ('.py', '.json')}
    manifest = directory / 'checkpoint.json'
    previous = json.loads(manifest.read_text()) if arguments.resume and manifest.exists() else {}
    results = previous.get('clips', {})
    requested = [name for name in names if not (arguments.resume and results.get(name, {}).get('exitCode') == 0)]
    script = {'author': 'build_clip.py', 'export': 'export_clip.py', 'validate': 'validate_clip.py', 'finalize': 'finalize_clip.py'}[arguments.stage]

    def run(name):
        started = time.monotonic()
        with (directory / (name + '.log')).open('w') as log:
            result = subprocess.run([os.environ.get('BLENDER', 'blender'), '-t', '2', '--background',
                                     '--factory-startup', '--python-exit-code', '1', '--python',
                                     str(Path(__file__).with_name(script)), '--', name], cwd=ROOT,
                                    stdout=log, stderr=subprocess.STDOUT)
        return name, dict(exitCode=result.returncode, seconds=round(time.monotonic()-started, 2))

    with ThreadPoolExecutor(max_workers=arguments.workers) as executor:
        jobs = [executor.submit(run, name) for name in requested]
        for job in as_completed(jobs):
            name, result = job.result()
            results[name] = result
            manifest.write_text(json.dumps(dict(stage=arguments.stage, recipes=recipes, clips=results), indent=2)+'\n')
            print(name, json.dumps(result), flush=True)
    failed = [name for name in names if results[name]['exitCode']]
    print(json.dumps(dict(completed=len(names)-len(failed), failed=failed)), flush=True)
    raise SystemExit(bool(failed))


if __name__ == '__main__':
    main()
