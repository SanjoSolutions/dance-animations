"""Render original, sample-free practice music from the checked-in arrangements.

Usage: python scripts/music/compose.py
Requires the project's NumPy dependency. Output is deterministic mono PCM WAV.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import wave

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SAMPLE_RATE = 22050


class Instruments:
    def __init__(self, seed):
        self.random = np.random.default_rng(seed)

    def note(self, pitch, duration, voice):
        time = np.arange(round(duration * SAMPLE_RATE)) / SAMPLE_RATE
        frequency = 440 * 2 ** ((pitch - 69) / 12)
        phase = 2 * np.pi * frequency * time
        attack = 1 - np.exp(-time * 180)
        release = np.minimum(1, (duration - time) * 35)
        if voice == 'piano':
            signal = sum(np.sin(phase * harmonic) * np.exp(-time * (2 + harmonic)) / harmonic ** 1.6
                         for harmonic in range(1, 7))
        elif voice == 'pluck':
            signal = sum(np.sin(phase * harmonic) / harmonic ** 1.2 for harmonic in range(1, 9)) * np.exp(-time * 8)
        elif voice == 'reed':
            signal = sum(np.sin(phase * harmonic) / harmonic ** 1.7 for harmonic in (1, 2, 3, 5)) * np.exp(-time * 2)
        elif voice == 'bell':
            signal = (np.sin(phase) + .35 * np.sin(phase * 2.01) + .13 * np.sin(phase * 3.98)) * np.exp(-time * 4)
        elif voice == 'bass':
            signal = (np.sin(phase) + .25 * np.sin(phase * 2)) * np.exp(-time * 4)
        else:
            signal = (np.sin(phase) + .22 * np.sin(phase * 2) + .1 * np.sin(phase * 3)) * np.exp(-time * 1.2)
            attack = 1 - np.exp(-time * 18)
        return signal * attack * release

    def percussion(self, voice):
        duration = .32 if voice in ('kick', 'tom') else .15
        time = np.arange(round(duration * SAMPLE_RATE)) / SAMPLE_RATE
        noise = self.random.uniform(-1, 1, len(time))
        if voice == 'kick':
            signal = np.sin(2 * np.pi * (48 * time + 4 * (1 - np.exp(-time * 30)))) * np.exp(-time * 18)
        elif voice == 'tom':
            signal = (np.sin(2 * np.pi * 140 * time) + .2 * noise) * np.exp(-time * 25)
        elif voice == 'snare':
            signal = (.65 * noise + .35 * np.sin(2 * np.pi * 185 * time)) * np.exp(-time * 32)
        elif voice == 'clave':
            signal = np.sin(2 * np.pi * 1800 * time) * np.exp(-time * 130)
        else:
            signal = np.diff(noise, prepend=noise[0]) * np.exp(-time * 65)
        return signal * np.minimum(time * 1200, 1)


class Arrangement:
    def __init__(self, style, profile):
        self.style = style
        self.profile = profile
        self.seed = int.from_bytes(hashlib.sha256(style['id'].encode()).digest()[:4], 'little')
        self.instruments = Instruments(self.seed)
        self.beat = 60 / profile['tempo']
        self.meter = profile['meter']
        self.bars = 8
        self.audio = np.zeros(round(self.bars * self.meter * self.beat * SAMPLE_RATE))

    def place(self, beat, sound, gain):
        indices = (round(beat * self.beat * SAMPLE_RATE) + np.arange(len(sound))) % len(self.audio)
        np.add.at(self.audio, indices, sound * gain)

    def note(self, beat, pitch, length, voice, gain):
        self.place(beat, self.instruments.note(pitch, length * self.beat, voice), gain)

    def drum(self, beat, voice, gain):
        self.place(beat, self.instruments.percussion(voice), gain)

    def render(self):
        profile = self.profile
        groove = profile['groove']
        minor = groove in ('tropical', 'afro', 'dembow', 'trap', 'march', 'arabic', 'flamenco', 'ambient')
        third = 3 if minor else 4
        root = 48 + self.seed % 7
        progression = [0, 0, 5, 5, 7, 5, 0, 7]
        melody = np.random.default_rng(self.seed + 1).choice([0, 2, third, 5, 7, 9 if not minor else 10, 12], 8)
        for bar in range(self.bars):
            start = bar * self.meter
            chord = root + progression[bar]
            # Eight-bar harmony and an original two-bar melodic motif.
            for interval in (0, third, 7):
                self.note(start, chord + 12 + interval, self.meter * .9, 'pad' if groove == 'ambient' else 'piano', .055)
            for index in range(self.meter):
                beat = start + index
                bass_pitch = chord - 12 + (7 if index % 2 else 0)
                self.note(beat, bass_pitch, .8, 'bass', .24 if index == 0 else .16)
                if groove == 'waltz':
                    self.drum(beat, 'kick' if index == 0 else 'hat', .16 if index == 0 else .025)
                    if index:
                        for interval in (third, 7):
                            self.note(beat, chord + 12 + interval, .6, profile['voice'], .07)
                elif groove == 'ambient':
                    self.note(beat, chord + 12 + (0, third, 7, 12)[index % 4], 1.7, 'bell', .055)
                elif groove == 'march':
                    self.drum(beat, 'kick' if index % 2 == 0 else 'snare', .27)
                    self.drum(beat + .5, 'snare', .05)
                elif groove == 'flamenco':
                    self.drum(beat, 'clave', .28 if index in (2, 5, 7, 9, 11) else .1)
                    self.drum(beat + .5, 'hat', .035)
                else:
                    four_on_floor = groove in ('house', 'disco', 'polka')
                    if four_on_floor or index % 4 in (0, 2):
                        self.drum(beat, 'kick', .32)
                    if index % 4 in (1, 3):
                        self.drum(beat, 'snare', .18)
                    subdivision = 2 / 3 if groove in ('swing', 'country') else .5
                    self.drum(beat, 'hat', .04)
                    self.drum(beat + subdivision, 'hat', .075)
                    if groove in ('latin', 'samba', 'tropical', 'afro', 'arabic', 'bhangra', 'dembow'):
                        self.drum(beat + .75, 'tom', .09)
                        self.drum(beat + .5, 'clave', .09 if index % 2 else .045)
                    if groove in ('trap', 'dembow') and index % 4 == 2:
                        self.drum(beat + .75, 'kick', .18)
                    if groove == 'trap':
                        self.drum(beat + .25, 'hat', .035)
                        self.drum(beat + .75, 'hat', .035)
                    if groove == 'samba':
                        self.drum(beat + .75, 'kick', .16)
                    if groove in ('latin', 'tropical', 'bhangra', 'arabic'):
                        self.note(beat + .5, chord + 12 + third, .45, 'pluck', .09)
                offset = 2 / 3 if groove in ('swing', 'country') else .5
                for half, phase in enumerate((0, offset)):
                    if (index + half + bar) % 3:
                        pitch = root + 24 + int(melody[(bar % 2 * self.meter + index * 2 + half) % 8])
                        self.note(beat + phase, pitch, .65 if groove == 'ambient' else .42, profile['voice'], .09)
        # Wrapped instrument tails preserve the periodic boundary.
        peak = np.max(np.abs(self.audio))
        self.audio *= .82 / peak
        return np.round(self.audio * 32767).astype('<i2').tobytes()

    def write(self):
        path = ROOT / 'assets/music' / (self.style['id'] + '.wav')
        pcm = self.render()
        with wave.open(str(path), 'wb') as output:
            output.setnchannels(1)
            output.setsampwidth(2)
            output.setframerate(SAMPLE_RATE)
            output.writeframes(pcm)
        return {
            'style': self.style['id'], 'title': self.profile['title'],
            'file': path.relative_to(ROOT).as_posix(),
            'tempo': self.profile['tempo'], 'meter': self.meter,
            'beats': self.bars * self.meter,
            'duration': len(pcm) / 2 / SAMPLE_RATE,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'license': 'MIT-0', 'licenseFile': 'third-party/project-MIT-0.txt',
            'provenance': 'Original composition and synthesized instruments by Codex for this project.',
            'arrangement': 'assets/music/arrangements.json',
            'timingBasis': self.profile['timingBasis'],
            'endingHold': self.profile.get('endingHold', 0),
        }


def main():
    styles = json.loads((ROOT / 'catalog.json').read_text())['styles']
    profiles = json.loads((ROOT / 'assets/music/arrangements.json').read_text())
    assert set(profiles) == {style['id'] for style in styles}
    tracks = [Arrangement(style, profiles[style['id']]).write() for style in styles]
    (ROOT / 'music.json').write_text(json.dumps({'version': 1, 'tracks': tracks}, indent=2) + '\n', newline='\n')
    print(f'Composed {len(tracks)} original style tracks.')


if __name__ == '__main__':
    main()
