"""Prepare beat-aligned excerpts of attributed human compositions for the viewer."""
import hashlib
import json
import wave

import numpy as np

from recordings import RecordingDecoder, ROOT, SAMPLE_RATE


class MusicPreparer:
    def __init__(self):
        self.decoder = RecordingDecoder()

    def prepare(self, identifier, recording):
        original = ROOT / recording['sourceFile']
        digest = hashlib.sha256(original.read_bytes()).hexdigest()
        if recording.get('sourceSha256') and recording['sourceSha256'] != digest:
            raise ValueError('Review the publisher recording hash for ' + recording['title'])
        recording['sourceSha256'] = digest
        samples = self.decoder.decode(original)
        start = round(recording['loopStart'] * SAMPLE_RATE)
        length = round(recording['beats'] * 60 / recording['tempo'] * SAMPLE_RATE)
        excerpt = samples[start:start + length].copy()
        assert len(excerpt) == length, recording['title']
        # Short edge fades retain the beat period while smoothing the cyclic seam.
        fade = round(.008 * SAMPLE_RATE)
        excerpt[:fade] *= np.linspace(0, 1, fade)
        excerpt[-fade:] *= np.linspace(1, 0, fade)
        excerpt *= .9 / max(float(np.abs(excerpt).max()), .001)
        output = ROOT / f'assets/music/{identifier}.wav'
        with wave.open(str(output), 'wb') as audio:
            audio.setparams((1, 2, SAMPLE_RATE, length, 'NONE', 'PCM'))
            audio.writeframes(np.round(excerpt * 32767).astype('<i2').tobytes())
        return {'file': output.relative_to(ROOT).as_posix(), 'sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
                'duration': length / SAMPLE_RATE,
                'changes': 'Excerpted at a measured beat, converted to mono 22050 Hz PCM, peak normalized, and given 8-millisecond edge fades for looping. Recorded tempo and pitch preserved.'}

    def run(self):
        path = ROOT / 'assets/music/selections.json'
        selections = json.loads(path.read_text(encoding='utf-8'))
        prepared = {identifier: self.prepare(identifier, recording)
                    for identifier, recording in selections['recordings'].items()}
        tracks = []
        for style, selection in selections['styles'].items():
            identifier = selection['recording']
            recording = selections['recordings'][identifier]
            fields = ('title', 'author', 'composer', 'contributors', 'source', 'download', 'published',
                      'publisherTempo', 'tempo', 'meter', 'beats', 'loopStart', 'sourceSha256',
                      'license', 'licenseUrl', 'licenseFile', 'pulseScore', 'analysis')
            tracks.append({'style': style, **selection, **{field: recording[field] for field in fields},
                           **prepared[identifier], 'provenance': 'Human composition and publisher recording; see dated source and human-creation evidence in assets/music/selections.json.',
                           'evidence': 'assets/music/selections.json'})
        path.write_text(json.dumps(selections, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
        (ROOT / 'music.json').write_text(json.dumps({'version': 2, 'tracks': tracks}, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
        print(f'Prepared {len(prepared)} human recordings for {len(tracks)} dance styles.')


if __name__ == '__main__':
    MusicPreparer().run()
