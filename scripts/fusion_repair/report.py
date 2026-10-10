"""Collect source hashes, acceptance stages, and comparison coverage."""
import hashlib
import json
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/'docs/animation_work_status/fusion_bake_feet_repair'
IDENTIFIERS=['fusion_box_basic','fusion_compression_stretch','fusion_forward_back_basic','fusion_promenade_walk','fusion_send_out_return','fusion_shadow','fusion_shadow_walk','fusion_side_basic','fusion_triple_step']


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUTPUT.mkdir(parents=True,exist_ok=True)
    catalog=json.loads((ROOT/'catalog.json').read_text())
    entries={entry['id']:entry for entry in catalog['animations']}
    baseline=json.loads((ROOT/'.cache/fusion-repair/baseline-summary.json').read_text())
    (OUTPUT/'baseline.json').write_text(json.dumps(baseline,indent=2)+'\n')
    baseline_output=OUTPUT/'baseline'
    baseline_output.mkdir(exist_ok=True)
    for record in baseline:
        shutil.copy2(ROOT/'.cache/fusion-repair/baseline'/record['id']/'report.json',baseline_output/(record['id']+'.json'))
    results=[]
    for identifier in IDENTIFIERS:
        directory=ROOT/'.cache/motion-recovery'/identifier
        report=json.loads((directory/'checkpoint.json').read_text())
        destination=OUTPUT/identifier
        destination.mkdir(exist_ok=True)
        evidence={}
        for stage in ('checkpoint','contacts','runtime','surfaces','loop','installation','installed-source','runtime-installed'):
            path=directory/(stage+'.json')
            if path.exists():
                evidence[stage]=json.loads(path.read_text())
                shutil.copy2(path,destination/path.name)
        matches=[path for path in (ROOT/'.cache/fusion-repair/visual'/identifier).glob('*/coverage.json') if json.loads(path.read_text())['exportSha256']==report['exportSha256']]
        capture=max(matches,key=lambda path:path.stat().st_mtime)
        shutil.copy2(capture,destination/'visual.json')
        shutil.copy2(capture.parent/'front-side.mp4',destination/'front-side.mp4')
        shutil.copy2(capture.parent/'review-contact-sheet.jpg',destination/'review-contact-sheet.jpg')
        assert evidence['installation']['exactCurveParity']
        assert evidence['installed-source']['passed'] and evidence['runtime-installed']['passed']
        entry=entries[identifier]
        assets={role:dict(file=entry[key],sha256=digest(ROOT/entry[key]),bytes=(ROOT/entry[key]).stat().st_size) for role,key in [('source','sourceFile'),('export','file')]}
        results.append(dict(id=identifier,assets=assets,candidateSourceSha256=report['sourceSha256'],performers=report['performers'],storedRange=report['storedRange'],rate=report['rate'],playbackEnd=report['storedRange'][1]-1,
            sourceState=report['stage'],installedSourceState='portable descriptor and curve parity checked',visualState='12 sequential playback samples reviewed in two views; 97-frame video available',bakePositionError=report['validation']['bakeSubframePositionError'],skinPlantDrift=evidence['surfaces']['maximumPlantDrift'],runtimePositionError=evidence['runtime']['maximumJointPositionError'],
            numericalAcceptance=all(evidence[stage]['passed'] for stage in ('contacts','runtime','surfaces','loop','installed-source','runtime-installed')),visual=dict(file=str((destination/'front-side.mp4').relative_to(ROOT)).replace('\\','/'),sha256=digest(destination/'front-side.mp4'),renderedFrames=97,reviewFrames=[0,6,18,27,33,42,54,66,75,81,90,96],views=['front at 15 degrees','side']),studyStatus=entry.get('studyStatus',entry['status'])))
    regressions=[]
    for record in baseline:
        if record['id'] not in IDENTIFIERS:
            entry=entries[record['id']]
            matches=digest(ROOT/entry['sourceFile'])==record['sourceSha256'] and digest(ROOT/entry['file'])==record['exportSha256']
            assert matches,record['id']
            regressions.append(dict(id=record['id'],sourceAndExportHashParity=matches,maximumBonePositionError=record['maximumBonePositionError']))
    summary=dict(clips=results,comparisonClips=regressions,baseCommit='039e2626b490e07a1c95192c265e5635cc77f07c',blender='5.2.1 LTS / 9e2066aef7ef',units='meters, seconds, frames',tolerances=dict(plantDrift=.003,nativeSubframePosition=.002,runtimePosition=.002,savedSourceMatrix=.0001),
                 models={actor:dict(file=entry['file'],sha256=digest(ROOT/entry['file'])) for actor,entry in catalog['models'].items()},
                 generators={str(path.relative_to(ROOT)).replace('\\','/'):digest(path) for path in (ROOT/'scripts/fusion_repair').glob('*') if path.is_file()},processState='complete; task Blender workers exited',publication='PR review; main integration follows user approval')
    (OUTPUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    for filename in ('batch.json','batch-initial.json'):
        shutil.copy2(ROOT/'.cache/fusion-repair'/filename,OUTPUT/filename)
    print('EVIDENCE',len(results),'repairs',len(regressions),'comparison clips')


if __name__=='__main__':
    main()
