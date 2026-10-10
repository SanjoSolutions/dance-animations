"""Build contact sheets from consecutive runtime playback captures."""
import json
from pathlib import Path
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[2]
FRAMES=[0,6,18,27,33,42,54,66,75,81,90,96]


def main():
    for clip in (ROOT/'.cache/fusion-repair/visual').iterdir():
        checkpoint=json.loads((ROOT/'.cache/motion-recovery'/clip.name/'checkpoint.json').read_text())
        captures=[path for path in clip.glob('*/coverage.json') if json.loads(path.read_text())['exportSha256']==checkpoint['exportSha256']]
        if captures:
            capture=max(captures,key=lambda path:path.stat().st_mtime)
            sheet=Image.new('RGB',(1440,1160),'white')
            draw=ImageDraw.Draw(sheet)
            for index,frame in enumerate(FRAMES):
                image=Image.open(capture.parent/f'frame-{frame:03}.jpg')
                image.thumbnail((480,270))
                left=(index%3)*480
                top=(index//3)*290
                sheet.paste(image,(left,top+20))
                draw.text((left+8,top+3),f'{clip.name} | {frame/24:.3f} s',fill='black')
            destination=capture.parent/'review-contact-sheet.jpg'
            sheet.save(destination,quality=90)
            print(destination)


if __name__=='__main__':
    main()
