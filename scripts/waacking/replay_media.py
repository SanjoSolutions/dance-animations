"""Save compact animated playback from the hash-bound browser capture."""
import hashlib
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / '.cache/waacking-runtime-frames'
OUTPUT = ROOT / 'docs/animation_work_status/waacking_repair/previews'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    capture = json.loads((DIRECTORY / 'capture.json').read_text())
    OUTPUT.mkdir(parents=True, exist_ok=True)
    animations = []
    for view in ('front', 'side', 'back'):
        records = [frame for frame in capture['frames'] if frame['view'] == view]
        frames = []
        for record in records:
            source = ROOT / record['file']
            assert digest(source) == record['sha256'], source
            with Image.open(source) as image:
                frames.append(image.resize((1000, 1007), Image.Resampling.LANCZOS).convert('P', palette=Image.Palette.ADAPTIVE, colors=128))
        destination = OUTPUT / ('runtime-' + view + '.gif')
        # GIF timing uses centiseconds; alternating delays retain the four-second phrase.
        delays = [120 if index % 2 == 0 else 130 for index in range(len(frames))]
        frames[0].save(destination, save_all=True, append_images=frames[1:], duration=delays, loop=0, optimize=False)
        animations.append(dict(view=view, file=destination.relative_to(ROOT).as_posix(), sha256=digest(destination), frames=len(frames), duration=sum(delays) / 1000))
    capture['animations'] = animations
    capture['generatorSha256'] = digest(Path(__file__))
    (OUTPUT.parent / 'runtime-capture.json').write_text(json.dumps(capture, indent=2) + '\n')
    print(json.dumps(animations))


if __name__ == '__main__':
    main()
