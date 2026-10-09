"""Capture sequential surface and visual evidence after native generation finishes."""
import json,os,subprocess,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
result_path=ROOT/'.cache/motion-recovery/waacking-results.json'
manifest=json.loads((result_path.parent/'waacking-batch.json').read_text())
expected={identifier for identifier in manifest['clips']}
while True:
    try: results=json.loads(result_path.read_text())
    except (FileNotFoundError,json.JSONDecodeError):results=[]
    if {result['id'] for result in results} == expected:break
    time.sleep(10)
assert all(result['phases'][-1]['phase'] == 'review' and result['phases'][-1]['returncode'] == 0 for result in results), results
identifiers=[entry['id'] for entry in json.loads((ROOT/'catalog.json').read_text())['animations'] if entry['style']=='waacking']
results=[]
for identifier in identifiers:
    directory=ROOT/'.cache/motion-recovery'/identifier
    if (directory/'motion-review.json').exists():
        phases=[]
        for script in ('surface_review','render_review'):
            with (directory/(script+'.log')).open('w') as log:
                process=subprocess.run(['powershell','-NoProfile','-File','scripts/waacking/run_blender.ps1','-Script',f'scripts/waacking/{script}.py','-Clips',identifier],cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
            phases.append(dict(phase=script,returncode=process.returncode))
        results.append(dict(id=identifier,phases=phases))
        (ROOT/'.cache/waacking-visual-process.json').write_text(json.dumps(results,indent=2)+'\n')
        print(identifier,json.dumps(phases),flush=True)
