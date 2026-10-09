"""Check completed native candidates on the MPFB runtime models during a serial build."""
import json,subprocess,time,hashlib
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
identifiers=[entry['id'] for entry in json.loads((ROOT/'catalog.json').read_text())['animations'] if entry['style']=='waacking']
manifest=json.loads((ROOT/'.cache/motion-recovery/waacking-batch.json').read_text())
expected={identifier for identifier in manifest['clips']}
completed={}
while len(completed)<len(identifiers):
    for identifier in identifiers:
        directory=ROOT/'.cache/motion-recovery'/identifier
        checkpoint=directory/'checkpoint.json';motion=directory/'motion-review.json'
        if identifier not in completed and checkpoint.exists() and motion.exists():
            report=json.loads(checkpoint.read_text());review=json.loads(motion.read_text())
            if review['sourceSha256']==report['sourceSha256'] and report['stage']=='saved source and bake validated':
                results=[]
                commands=[['.cache/waacking-venv/Scripts/python.exe','scripts/motion_recovery/runtime_batch.py',identifier],['node','scripts/motion_recovery/surfaces.mjs',identifier],['node','scripts/motion_recovery/loop_review.mjs',identifier]]
                for command in commands:
                    with (directory/(Path(command[1]).stem+'-process.log')).open('w') as log:
                        process=subprocess.run(command,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
                    results.append(dict(command=command,returncode=process.returncode))
                matrices=np.load(directory/'authored.npz')['matrices'][:,0];names=report['boneNames'][0]
                wrists={};feet={}
                for side in 'LR':
                    first=matrices[:,names.index('DEF-forearm.'+side+'.001'),:3,1];second=matrices[:,names.index('DEF-hand.'+side),:3,1]
                    cosine=np.sum(first*second,axis=-1)/(np.linalg.norm(first,axis=-1)*np.linalg.norm(second,axis=-1));angles=np.degrees(np.arccos(np.clip(cosine,-1,1)))
                    wrists[side]=dict(maximum=float(angles.max()),frame=report['sampledFrames'][int(angles.argmax())])
                    points=matrices[:,names.index('DEF-foot.'+side),:3,3];drift=np.linalg.norm(points-points[0],axis=-1)
                    feet[side]=dict(maximumJointDrift=float(drift.max()),frame=report['sampledFrames'][int(drift.argmax())])
                (directory/'deform-contacts.json').write_text(json.dumps(dict(sourceSha256=report['sourceSha256'],exportSha256=report['exportSha256'],generatorSha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),wrists=wrists,feet=feet,samples=len(matrices),units='degrees and meters',coverage='Evaluated authored deform hand and forearm axes; foot joint drift during standing support'),indent=2)+'\n')
                completed[identifier]=dict(results=results,sourceSha256=report['sourceSha256'])
                print(identifier,json.dumps(results),flush=True)
                (ROOT/'.cache/waacking-runtime-process.json').write_text(json.dumps(completed,indent=2)+'\n')
    results_path=ROOT/'.cache/motion-recovery/waacking-results.json'
    if results_path.exists():
        try:results=json.loads(results_path.read_text())
        except json.JSONDecodeError:results=[]
        if {result['id'] for result in results} == expected:
            for result in results:
                if result['id'] not in completed and result['phases'][-1]['returncode']:
                    completed[result['id']]=dict(nativeFailure=result['phases'][-1])
    if len(completed)<len(identifiers):time.sleep(10)
(ROOT/'.cache/waacking-runtime-process.json').write_text(json.dumps(completed,indent=2)+'\n')

assert all('results' in result and all(phase['returncode'] == 0 for phase in result['results']) for result in completed.values()), completed
