"""Decode publisher recordings and measure their steady pulse near the published tempo."""
from pathlib import Path
import shutil
import subprocess

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SAMPLE_RATE = 22050


class RecordingDecoder:
    def __init__(self):
        self.executable = shutil.which('ffmpeg')
        if self.executable is None:
            raise RuntimeError('Install FFmpeg and include its directory in PATH to prepare recordings.')

    def decode(self, path):
        result = subprocess.run([self.executable, '-v', 'error', '-i', str(path),
                                 '-f', 'f32le', '-ac', '1', '-ar', str(SAMPLE_RATE), 'pipe:1'],
                                check=True, capture_output=True)
        return np.frombuffer(result.stdout, dtype='<f4').copy()


class BeatGridAnalyzer:
    """Find a steady pulse using positive spectral changes and bass accents.

    The publisher's tempo supplies the musical interpretation; analysis refines
    the period and phase. Results remain an editable accompaniment choice.
    """

    def analyze(self, samples, recording):
        hop = 110
        width = 1024
        section = samples[:min(len(samples), SAMPLE_RATE * 75)]
        frames = np.lib.stride_tricks.sliding_window_view(section, width)[::hop]
        spectrum = np.abs(np.fft.rfft(frames * np.hanning(width), axis=1))
        compressed = np.log1p(spectrum * 10)
        changes = np.maximum(0, np.diff(compressed, axis=0))
        bass = changes[:, 1:10].mean(axis=1)
        broadband = changes.mean(axis=1)
        accents = bass / max(float(bass.max()), .001) + .6 * broadband / max(float(broadband.max()), .001)
        # Frame-start timestamps place excerpt edges slightly ahead of the attack.
        times = np.arange(len(accents)) * hop / SAMPLE_RATE
        declared = recording['publisherTempo']
        best = (-1, declared, 0)
        for tempo in np.linspace(declared * .98, declared * 1.02, 161):
            period = 60 / tempo
            phases = np.linspace(0, period, 120, endpoint=False)
            beats = np.arange(8, int(min(65, times[-1]) / period)) * period
            positions = phases[:, None] + beats
            score = np.interp(positions.ravel(), times, accents).reshape(positions.shape).mean(axis=1)
            index = int(score.argmax())
            if score[index] > best[0]:
                best = (float(score[index]), float(tempo), float(phases[index]))
        score, tempo, phase = best
        period = 60 / tempo
        if phase > period / 2:
            phase -= period
        meter = recording['meter']
        count = recording['beats']
        # The recording's first measure anchors complete-measure excerpts.
        first = 8 + (-8 % meter)
        candidate_beats = np.arange(first, min(70, int(times[-1] / period) - count), meter)
        starts = phase + candidate_beats * period
        strengths = np.interp(starts, times, bass)
        chosen = int(candidate_beats[int(strengths.argmax())])
        start = phase + chosen * period
        return {'tempo': round(tempo, 6), 'loopStart': round(start, 6),
                'pulseScore': round(score / max(float(accents.mean()), .001), 3),
                'analysis': 'Spectral-onset grid near publisher tempo; strongest bass accent starts the excerpt.'}
