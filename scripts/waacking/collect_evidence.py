"""Collect hash-bound Waacking checkpoints into durable per-clip review evidence."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'docs/animation_work_status/waacking_repair'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    inventory = {entry['id']: entry for entry in json.loads((ROOT / 'source-inventory.json').read_text())}
    selected = [entry for entry in catalog['animations'] if entry['style'] == 'waacking']
    OUTPUT.mkdir(parents=True, exist_ok=True)
    records = []
    names = ('baseline', 'checkpoint', 'motion-review', 'deform-contacts', 'runtime', 'surfaces', 'loop',
             'clearance', 'visual-capture', 'installation', 'installed-source', 'runtime-installed', 'process')
    for entry in selected:
        directory = ROOT / '.cache/motion-recovery' / entry['id']
        checks = {name: json.loads((directory / (name + '.json')).read_text()) for name in names if (directory / (name + '.json')).exists()}
        checkpoint = checks.get('checkpoint', {})
        installation = checks.get('installation', {})
        source = ROOT / entry['sourceFile']
        export = ROOT / entry['file']
        installed = bool(installation) and digest(source) == installation['sourceSha256']
        if installed:
            assert entry['sourceSha256'] == inventory[entry['id']]['sha256'] == digest(source)
            if 'runtime-installed' in checks:
                assert checks['runtime-installed']['exportSha256'] == digest(export)
                assert checks['runtime-installed']['passed']
            if 'installed-source' in checks:
                assert checks['installed-source']['passed']
            assert installation['candidateSourceSha256'] == checkpoint['sourceSha256']
            assert all(digest(ROOT / path) == value for path, value in checkpoint['dependencies'].items())
        stages = dict(authoredControls=checks.get('motion-review', {}).get('passed', False),
                      freshSource=checkpoint.get('validation', {}).get('savedSourceMatrixError', 1) <= .0001,
                      nativeBake=checkpoint.get('stage') == 'saved source and bake validated' and checks.get('motion-review', {}).get('passed', False),
                      runtime=checks.get('runtime-installed' if installed else 'runtime', {}).get('passed', False),
                      sampledClearance=checks.get('clearance', {}).get('passed', False),
                      visualCapture='visual-capture' in checks,
                      visualReview=checks.get('visual-capture', {}).get('reviewDisposition', 'pending'),
                      installed=installed)
        record = dict(id=entry['id'], performers=entry['performers'], source=entry['sourceFile'], export=entry['file'],
                      sourceSha256=digest(source), exportSha256=digest(export), sourceSize=source.stat().st_size,
                      exportSize=export.stat().st_size, sizeUnit='bytes', originalSourceSha256=inventory[entry['id']].get('originalSha256'),
                      originalExportSha256=entry.get('originalExportSha256'), status=entry['status'], studyStatus=entry.get('studyStatus'),
                      stages=stages, checks=checks)
        (OUTPUT / (entry['id'] + '.json')).write_text(json.dumps(record, indent=2) + '\n')
        records.append({key: value for key, value in record.items() if key != 'checks'})
    dependency_paths = [ROOT / 'animations/shared_scene_data.blend', ROOT / 'assets/characters/mpfb-characters.blend', ROOT / 'assets/characters/rig-schema.json']
    dependency_paths.extend((ROOT / 'assets/wardrobe').glob('*.blend'))
    dependency_paths.extend(ROOT / model['file'] for model in catalog['models'].values())
    result = dict(scope='Existing 16 Waacking source/export pairs', planned=16, recorded=len(records),
                  installed=sum(record['stages']['installed'] for record in records),
                  baselineCommit='039e2626b490e07a1c95192c265e5635cc77f07c',
                  worktree=str(ROOT), branch=subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip(),
                  clips=records, dependencies={path.relative_to(ROOT).as_posix(): digest(path) for path in dependency_paths},
                  generators={path.relative_to(ROOT).as_posix(): digest(path) for path in (ROOT / 'scripts/waacking').glob('*') if path.is_file()},
                  coverage=dict(nativeSampling='1537 samples per clip, half stored frames at 192 fps; every deform bone',
                                runtime='Actual Three.js MPFB model playback, all joint positions/orientations, duration, finite transforms and loop seam',
                                surfaces='MPFB sole vertices plus native weighted skin regions at 193 samples',
                                visuals='12 native poses from front, side and back for each clip; 32 runtime samples per view across the complete four-second loop',
                                additionalReview='Proximal shoulder surfaces, individual finger self-contact, dynamic balance and expert dance review retain study coverage'))
    capture_path = OUTPUT / 'runtime-capture.json'
    if capture_path.exists():
        capture = json.loads(capture_path.read_text())
        assert all(digest(ROOT / animation['file']) == animation['sha256'] for animation in capture['animations'])
        for candidate in capture['inputs']:
            checkpoint = json.loads((ROOT / '.cache/motion-recovery' / candidate['id'] / 'checkpoint.json').read_text())
            assert candidate['sourceSha256'] == checkpoint['sourceSha256']
            assert candidate['exportSha256'] == checkpoint['exportSha256']
        result['runtimeCapture'] = dict(file=capture_path.relative_to(ROOT).as_posix(), sha256=digest(capture_path), reviewDisposition=capture.get('reviewDisposition', 'pending'))
    (OUTPUT / 'evidence.json').write_text(json.dumps(result, indent=2) + '\n')
    for name in ('waacking-batch.json', 'waacking-results.json'):
        path = ROOT / '.cache/motion-recovery' / name
        if path.exists(): shutil.copy2(path, OUTPUT / name)
    for name in ('waacking-studio.json', 'waacking-runtime-process.json', 'waacking-visual-process.json'):
        path = ROOT / '.cache' / name
        if path.exists(): shutil.copy2(path, OUTPUT / name)
    print(json.dumps(dict(recorded=len(records), installed=result['installed'])))


if __name__ == '__main__':
    main()
