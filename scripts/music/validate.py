"""Validate complete music coverage, provenance, samples, and loop timing."""
import hashlib
import json
from pathlib import Path
import wave

import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def validate_music(catalog):
    tracks = json.loads((ROOT / 'music.json').read_text())['tracks']
    assert len(tracks) == len(catalog['styles'])
    assert {track['style'] for track in tracks} == {style['id'] for style in catalog['styles']}
    profiles = json.loads((ROOT / 'assets/music/arrangements.json').read_text())
    hashes = set()
    sizes = []
    for track in tracks:
        path = ROOT / track['file']
        assert path.parent == ROOT / 'assets/music'
        assert track['license'] == 'MIT-0'
        assert 'Original composition' in track['provenance']
        assert (ROOT / 'public' / track['licenseFile']).is_file()
        assert track['timingBasis'] == profiles[track['style']]['timingBasis']
        assert track['tempo'] == profiles[track['style']]['tempo']
        assert track['beats'] % track['meter'] == 0
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        assert digest == track['sha256']
        assert digest not in hashes, track['style']
        hashes.add(digest)
        with wave.open(str(path)) as audio:
            assert audio.getnchannels() == 1 and audio.getsampwidth() == 2
            samples = np.frombuffer(audio.readframes(audio.getnframes()), dtype='<i2').astype(float) / 32768
            duration = audio.getnframes() / audio.getframerate()
            assert duration == track['duration']
            assert abs(duration - track['beats'] * 60 / track['tempo']) <= 1 / audio.getframerate()
            assert .025 < np.sqrt(np.mean(samples ** 2)) < .4, track['style']
            assert .75 < np.max(np.abs(samples)) < .99, track['style']
            assert abs(samples[-1] - samples[0]) < .08, track['style']
        sizes.append(path.stat().st_size)
    print(f'Validated {len(tracks)} original MIT-0 music tracks, samples, loop boundaries, and hashes.')
    return sizes


if __name__ == '__main__':
    validate_music(json.loads((ROOT / 'catalog.json').read_text()))
