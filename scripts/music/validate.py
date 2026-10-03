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
    selections = json.loads((ROOT / 'assets/music/selections.json').read_text(encoding='utf-8'))
    assert selections['licenseEvidence']['source'].startswith('https://incompetech.com/')
    assert selections['humanCreationEvidence']['source'].startswith('https://incompetech.com/')
    files = set()
    sizes = []
    for track in tracks:
        path = ROOT / track['file']
        assert path.parent == ROOT / 'assets/music'
        profile = selections['styles'][track['style']]
        recording = selections['recordings'][profile['recording']]
        assert track['license'] == 'CC-BY-4.0'
        assert track['author'] == 'Kevin MacLeod' and track['published'] < '2020-01-01'
        assert track['source'] == recording['source']
        assert track['sourceSha256'] == recording['sourceSha256'] and len(track['sourceSha256']) == 64
        assert track['changes'] and track['provenance'] and track['fit']
        assert track['pulseScore'] > 1.7, track['title']
        assert (ROOT / 'public' / track['licenseFile']).is_file()
        assert track['timingBasis'] == profile['timingBasis']
        assert track['animationTempo'] == profile['animationTempo'] > 0
        assert track['changeInterval'] == profile['changeInterval'] >= 0
        assert track['tempo'] == recording['tempo'] > 0
        assert track['meter'] == recording['meter']
        assert track['beats'] % track['meter'] == 0
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        assert digest == track['sha256']
        original = ROOT / recording['sourceFile']
        if original.is_file():
            assert hashlib.sha256(original.read_bytes()).hexdigest() == track['sourceSha256']
        with wave.open(str(path)) as audio:
            assert audio.getnchannels() == 1 and audio.getsampwidth() == 2
            samples = np.frombuffer(audio.readframes(audio.getnframes()), dtype='<i2').astype(float) / 32768
            duration = audio.getnframes() / audio.getframerate()
            assert duration == track['duration']
            assert abs(duration - track['beats'] * 60 / track['tempo']) <= 1 / audio.getframerate()
            assert .025 < np.sqrt(np.mean(samples ** 2)) < .4, track['style']
            assert .75 < np.max(np.abs(samples)) < .99, track['style']
            assert abs(samples[-1] - samples[0]) < .08, track['style']
        if path not in files:
            sizes.append(path.stat().st_size)
            files.add(path)
    assert files == set((ROOT / 'assets/music').glob('*.wav'))
    print(f'Validated {len(tracks)} styles with {len(files)} attributed human music excerpts, samples, loop boundaries, and hashes.')
    return sizes


if __name__ == '__main__':
    validate_music(json.loads((ROOT / 'catalog.json').read_text()))
