"""Record editable pulse measurements for downloaded human compositions."""
import json

from recordings import BeatGridAnalyzer, RecordingDecoder, ROOT


def main():
    path = ROOT / 'assets/music/selections.json'
    selections = json.loads(path.read_text(encoding='utf-8'))
    decoder = RecordingDecoder()
    analyzer = BeatGridAnalyzer()
    for identifier, recording in selections['recordings'].items():
        if (ROOT / recording['sourceFile']).is_file():
            recording.update(analyzer.analyze(decoder.decode(ROOT / recording['sourceFile']), recording))
            print(f'{recording["title"]}: {recording["tempo"]:g} BPM, start {recording["loopStart"]:g}, pulse {recording["pulseScore"]:g}', flush=True)
        else:
            raise FileNotFoundError(recording['sourceFile'])
    path.write_text(json.dumps(selections, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
