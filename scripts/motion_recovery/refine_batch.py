"""Refine selected priority clips and retain per-phase process evidence."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
SPECIAL_REFINEMENTS = {
    'new_york_hustle_inside_turn_pass': 'scripts/new_york_hustle/refine_turn.py',
    'new_york_hustle_shadow_entry_exit': 'scripts/new_york_hustle/refine_shadow.py',
    'salsa_leader_left_turn': 'scripts/salsa/refine_turn.py',
}


def run(identifier):
    directory = ROOT / '.cache/motion-recovery' / identifier
    directory.mkdir(parents=True, exist_ok=True)
    style = 'new_york_hustle' if identifier.startswith('new_york_hustle_') else 'salsa'
    results = []
    review_status = 0
    special = SPECIAL_REFINEMENTS.get(identifier)
    for sampling in ((8,) if special else (4, 8, 16)):
        author = (special, []) if special else (f'scripts/{style}/refine_motion.py', ['--sampling', str(sampling)])
        phases = [author, ('scripts/motion_recovery/validate.py', [])]
        phases.append((f'scripts/{style}/review_recovery.py', []))
        for script, arguments in phases:
            with (directory / (Path(script).stem + '.log')).open('w') as log:
                process = subprocess.run(['blender', '-t', '1', '-b', '--factory-startup', '--python-exit-code', '1', '--python', script, '--', identifier, *arguments], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
            results.append(dict(script=script, sampling=sampling, returncode=process.returncode))
            if process.returncode:
                break
        (directory / 'refinement-process.json').write_text(json.dumps(results, indent=2) + '\n')
        if process.returncode == 0:
            review_status = 0
            for script in ('surfaces.mjs', 'loop_review.mjs'):
                with (directory / (script + '.log')).open('w') as log:
                    review = subprocess.run(['node', 'scripts/motion_recovery/' + script, identifier], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
                results.append(dict(script=script, sampling=sampling, returncode=review.returncode))
                review_status = max(review_status, abs(review.returncode))
            (directory / 'refinement-process.json').write_text(json.dumps(results, indent=2) + '\n')
            break
        report = json.loads((directory / 'checkpoint.json').read_text())
        if set(report.get('failures', {})) != {'bakeSubframePositionError'}:
            break
    print(identifier, json.dumps(results), flush=True)
    return process.returncode or review_status


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('identifiers', nargs='+')
    parser.add_argument('--workers', type=int, default=3)
    arguments = parser.parse_args()
    sources = ['scripts/motion_recovery/repair.py', 'scripts/motion_recovery/validate.py', 'scripts/new_york_hustle/refine_motion.py', 'scripts/new_york_hustle/review_recovery.py', 'scripts/salsa/refine_motion.py', 'scripts/salsa/review_recovery.py', 'scripts/motion_recovery/sole_calibration.py', 'scripts/player_assets/animation_files.py', 'scripts/track_chooser.py']
    sources.extend(SPECIAL_REFINEMENTS.values())
    sources.append('scripts/motion_recovery/foot_pivots.py')
    sources.extend(['scripts/new_york_hustle/polish.py', 'scripts/motion_recovery/surfaces.mjs', 'scripts/motion_recovery/loop_review.mjs'])
    (ROOT / '.cache/motion-recovery/refinement-batch.json').write_text(json.dumps(dict(clips=arguments.identifiers, generators={path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for path in sources}), indent=2) + '\n')
    with ThreadPoolExecutor(max_workers=arguments.workers) as pool:
        results = list(pool.map(run, arguments.identifiers))
    assert all(result == 0 for result in results), results


if __name__ == '__main__':
    main()
