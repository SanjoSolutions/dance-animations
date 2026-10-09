"""Assemble review contact sheets from hash-matched Blender captures."""
from pathlib import Path
import json,hashlib,sys
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[2]
output=ROOT/'docs/animation_work_status/waacking_repair/previews';output.mkdir(parents=True,exist_ok=True)
for identifier in sys.argv[1:]:
    directory=ROOT/'.cache/motion-recovery'/identifier
    capture=json.loads((directory/'visual-capture.json').read_text())
    sheet=Image.new('RGB',(1440,2088),'#20242b');draw=ImageDraw.Draw(sheet)
    for index,sample in enumerate(capture['frames']):
        path=ROOT/sample['file'];assert hashlib.sha256(path.read_bytes()).hexdigest()==sample['sha256']
        x=(index%6)*240;y=(index//6)*348;sheet.paste(Image.open(path).convert('RGB'),(x,y+28));draw.text((x+7,y+7),f"{sample['view']} | {sample['frame']/192:.3f} s",fill='white')
    destination=output/(identifier+'.jpg');sheet.save(destination,quality=88)
    capture['contactSheet']=dict(file=destination.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(destination.read_bytes()).hexdigest())
    (directory/'visual-capture.json').write_text(json.dumps(capture,indent=2)+'\n')
    print(destination)
