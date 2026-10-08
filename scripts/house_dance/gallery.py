"""Publish the local dual-view review captures beside the measured clip evidence."""
import hashlib
import json
from pathlib import Path
import shutil

from PIL import Image, ImageDraw

from repertoire import CATALOG

ROOT = Path(__file__).resolve().parents[2]


def main():
    destination = ROOT / 'docs/house_dance_review'
    media = destination / 'media'
    media.mkdir(parents=True, exist_ok=True)
    clips = []
    for phrase, module in CATALOG:
        for actor in ('man', 'woman'):
            name = f'house_{actor}_{phrase.name}'
            captures = ROOT / '.cache/house/visual' / name
            coverage = json.loads((captures / 'coverage.json').read_text())
            exported = ROOT / '.cache/house/candidates' / (name + '.glb')
            assert coverage['exportSha256'] == hashlib.sha256(exported.read_bytes()).hexdigest(), name
            assert coverage['motion'] and len(coverage['frames']) == 33
            shutil.copyfile(captures / 'motion.webm', media / (name + '.webm'))
            shutil.copyfile(captures / 'frame-000.jpg', media / (name + '-poster.jpg'))
            sheet = Image.new('RGB', (1280, 398), '#e9eef4')
            draw = ImageDraw.Draw(sheet)
            for index, frame in enumerate((0, 6, 18, 30, 42, 54, 78, 96)):
                image = Image.open(captures / f'frame-{frame // 3:03}.jpg')
                image.thumbnail((320, 176))
                x, y = index % 4 * 320, index // 4 * 199
                sheet.paste(image, (x, y + 23))
                draw.text((x + 8, y + 5), f'Frame {frame}', fill='#182333')
            sheet.save(media / (name + '.jpg'), quality=85)
            clips.append(dict(id=name, phrase=phrase.name.replace('_', ' ').capitalize(), actor=actor,
                              family=phrase.family, loop=module != 'transitions', description=phrase.description))
    (destination / 'gallery.json').write_text(json.dumps(clips, indent=2) + '\n')
    print(f'Saved {len(clips)} review videos and dual-view contact sheets')


if __name__ == '__main__':
    main()
