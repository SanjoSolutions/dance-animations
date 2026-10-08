"""Compare directed Hip-hop transitions with their saved named pose clips."""
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def main():
    directory = ROOT / '.cache/motion-recovery'
    for actor in ('man', 'woman'):
        for first, last in (('neutral', 'low'), ('low', 'neutral'), ('neutral', 'wide'), ('wide', 'neutral')):
            identifier = f'hip_hop_{actor}_{first}_to_{last}'
            matrices = np.load(directory / identifier / 'authored.npz')['matrices']
            references = [f'hip_hop_{actor}_pose_{pose}' for pose in (first, last)]
            targets = [np.load(directory / target / 'authored.npz')['matrices'][0] for target in references]
            errors = [float(np.abs(matrices[index] - target).max()) for index, target in zip((0, -1), targets)]
            hashes = {clip: json.loads((directory / clip / 'checkpoint.json').read_text())['sourceSha256'] for clip in [identifier, *references]}
            report = dict(references=references, sourceHashes=hashes, matrixErrors=errors, limit=.0001, passed=max(errors) < .0001)
            (directory / identifier / 'transitions.json').write_text(json.dumps(report, indent=2) + '\n')
            print(identifier, report)
            assert report['passed'], identifier


if __name__ == '__main__':
    main()
