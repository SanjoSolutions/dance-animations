"""Run one sequential Waacking repair pass with independent source processes."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--blender', default=r'C:\Program Files\Blender Foundation\Blender 5.2\blender.exe')
    parser.add_argument('--clips', nargs='*')
    arguments = parser.parse_args()
    selected = arguments.clips or [entry['id'] for entry in json.loads((ROOT/'catalog.json').read_text())['animations'] if entry['style']=='waacking']
    profile = ROOT/'.cache/waacking-profile'
    environment = os.environ.copy()
    for key, suffix in [('BLENDER_USER_RESOURCES',''),('BLENDER_USER_CONFIG','config'),('BLENDER_USER_SCRIPTS','scripts'),('BLENDER_USER_EXTENSIONS','extensions')]:
        path=profile/suffix;path.mkdir(parents=True,exist_ok=True);environment[key]=str(path)
    temporary=ROOT/'.cache/waacking-temp';temporary.mkdir(exist_ok=True)
    environment.update(TEMP=str(temporary),TMP=str(temporary))
    sources=['scripts/waacking/sole_repair.py','scripts/waacking/refine_motion.py','scripts/waacking/review.py','scripts/waacking/diagnose.py','scripts/motion_recovery/repair.py','scripts/motion_recovery/validate.py']
    manifest=dict(clips=selected,generators={path:hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in sources},blender=arguments.blender,workers=1,started=time.time())
    destination=ROOT/'.cache/motion-recovery/waacking-batch.json'
    destination.write_text(json.dumps(manifest,indent=2)+'\n')
    results=[]
    for identifier in selected:
        directory=ROOT/'.cache/motion-recovery'/identifier;directory.mkdir(parents=True,exist_ok=True)
        phases=[]
        for phase in ('diagnose','refine_motion','review'):
            with (directory/(phase+'.log')).open('w') as log:
                process=subprocess.run([arguments.blender,'--factory-startup','--background','-t','2','--python-exit-code','1','--python',f'scripts/waacking/{phase}.py','--',identifier],cwd=ROOT,env=environment,stdout=log,stderr=subprocess.STDOUT)
            phases.append(dict(phase=phase,returncode=process.returncode,completed=time.time()))
            (directory/'process.json').write_text(json.dumps(phases,indent=2)+'\n')
            if process.returncode:
                break
        results.append(dict(id=identifier,phases=phases))
        (destination.parent/'waacking-results.json').write_text(json.dumps(results,indent=2)+'\n')
        print(identifier,json.dumps(phases),flush=True)
    assert all(result['phases'][-1]['phase']=='review' and result['phases'][-1]['returncode']==0 for result in results)


if __name__=='__main__':
    main()
