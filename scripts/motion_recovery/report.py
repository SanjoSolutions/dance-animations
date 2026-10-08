"""Collect installed, hash-matched recovery evidence for local quality review."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'docs/animation_work_status/priority_recovery'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--complete', action='store_true')
    arguments = parser.parse_args()
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    entries = {entry['id']: entry for entry in catalog['animations']}
    results, pending = [], []
    for path in sorted((ROOT / '.cache/motion-recovery').glob('*/checkpoint.json')):
        report = json.loads(path.read_text())
        directory = path.parent
        names = ['runtime-installed', 'installed-source', 'installation', 'surfaces']
        if report['loop']:
            names.append('loop')
        if report['style'] in ('salsa', 'new_york_hustle'):
            names.append('contacts')
        evidence = {name: json.loads((directory / (name + '.json')).read_text()) for name in names if (directory / (name + '.json')).exists()}
        entry = entries.get(report['id'])
        complete = len(evidence) == len(names) and report['stage'] == 'saved source and bake validated'
        if complete:
            complete = evidence['installation']['candidateSourceSha256'] == report['sourceSha256']
            complete &= evidence['runtime-installed']['passed'] and evidence['installed-source']['passed']
            complete &= evidence['runtime-installed']['sourceSha256'] == entry['sourceSha256'] == evidence['installed-source']['sourceSha256']
            complete &= evidence['surfaces']['exportSha256'] == report['exportSha256']
            complete &= min(foot['minimum'] for foot in evidence['surfaces']['feet']) >= -.002
            if report['loop']:
                complete &= evidence['loop']['passed'] and evidence['loop']['exportSha256'] == report['exportSha256']
            if 'contacts' in evidence:
                complete &= evidence['contacts']['passed'] and evidence['contacts']['sourceSha256'] == report['sourceSha256']
        if complete:
            assert digest(ROOT / entry['sourceFile']) == entry['sourceSha256']
            assert digest(ROOT / entry['file']) == evidence['runtime-installed']['exportSha256']
            assert all(digest(ROOT / dependency) == value for dependency, value in report['dependencies'].items())
            report['candidateSourceSha256'] = report.pop('sourceSha256')
            report['candidateExportSha256'] = report.pop('exportSha256')
            report['source'] = entry['sourceFile']
            report['export'] = entry['file']
            report['sourceSha256'] = entry['sourceSha256']
            report['exportSha256'] = evidence['runtime-installed']['exportSha256']
            report['sourceBytes'] = (ROOT / entry['sourceFile']).stat().st_size
            report['exportBytes'] = (ROOT / entry['file']).stat().st_size
            frames = report.pop('sampledFrames')
            report['sampling'] = dict(first=frames[0], last=frames[-1], step=.5, count=len(frames), units='stored frames')
            report['deformBones'] = {actor: names for actor, names in zip(report['performers'], report.pop('boneNames'))}
            report['checks'] = evidence
            transition = directory / 'transitions.json'
            if transition.exists():
                report['checks']['transitions'] = json.loads(transition.read_text())
                assert report['checks']['transitions']['passed']
            report['stage'] = 'installed; source, bake, runtime, and targeted motion checks passed'
            results.append(report)
        else:
            pending.append(dict(id=report['id'], stage=report['stage'], failures=report.get('failures', {})))
    recorded = {report['id'] for report in results + pending}
    expected = {entry['id'] for entry in catalog['animations'] if entry['style'] in ('hip_hop', 'new_york_hustle', 'salsa')}
    pending.extend(dict(id=identifier, stage='queued', failures={}) for identifier in sorted(expected - recorded))
    OUTPUT.mkdir(parents=True, exist_ok=True)
    counts = dict(Counter(report['style'] for report in results))
    result = dict(scope='Hip-hop, New York Hustle, Salsa, and interrupted Popping coverage', clips=results, pending=pending,
                  installedCounts=counts, sourceCount=catalog['sourceCount'], runtimeClipCount=len(catalog['animations']),
                  runtimeModels={actor: dict(file=model['file'], sha256=digest(ROOT / model['file'])) for actor, model in catalog['models'].items()},
                  visualCoverage='Representative MPFB front/side pose sheets and playback highlights; see accompanying review notes',
                  additionalReview='Full mesh collision, detailed support balance, and expert dance review retain procedural-study status')
    (OUTPUT / 'evidence.json').write_text(json.dumps(result, indent=2) + '\n')
    print('Installed and verified', len(results), counts, 'pending', len(pending))
    if arguments.complete:
        assert counts == dict(hip_hop=76, popping=19, salsa=35, new_york_hustle=40), counts
        assert not pending, pending


if __name__ == '__main__':
    main()
