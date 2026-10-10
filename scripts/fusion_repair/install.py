"""Install accepted Fusion candidates through the portable source writer."""
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts/motion_recovery'))
from install import CandidateInstaller

identifiers=sys.argv[sys.argv.index('--')+1:]
for identifier in identifiers:
    directory=ROOT/'.cache/motion-recovery'/identifier
    report=json.loads((directory/'checkpoint.json').read_text())
    assert report['stage']=='saved source and bake validated',identifier
    for stage in ('contacts','runtime','surfaces','loop'):
        result=json.loads((directory/(stage+'.json')).read_text())
        assert result['passed'],(identifier,stage)
        if 'sourceSha256' in result:
            assert result['sourceSha256']==report['sourceSha256'],(identifier,stage)
        if 'exportSha256' in result:
            assert result['exportSha256']==report['exportSha256'],(identifier,stage)
installer=CandidateInstaller()
for identifier in identifiers:
    installer.install(identifier)
    installer.sources[identifier]['runtimeExport']=installer.sources[identifier]['runtimeExport'].replace('\\','/')
    installer.save_catalogs()

for path in (installer.catalog_path, installer.inventory_path):
    path.write_text(path.read_text(), newline='\n')
