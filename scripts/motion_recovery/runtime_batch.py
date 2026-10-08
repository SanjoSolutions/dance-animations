"""Compare validated native candidates on the actual Three.js MPFB models."""
import argparse
import json
from pathlib import Path
import subprocess

import numpy as np
from scipy.spatial.transform import Rotation

ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('identifiers', nargs='*')
    arguments = parser.parse_args()
    directory = ROOT / '.cache/motion-recovery'
    paths = [directory / identifier / 'checkpoint.json' for identifier in arguments.identifiers] if arguments.identifiers else sorted(directory.glob('*/checkpoint.json'))
    identifiers = []
    for path in paths:
        report = json.loads(path.read_text())
        if report['stage'] == 'saved source and bake validated':
            matrices = np.load(path.parent / 'authored.npz')['matrices']
            rotations = matrices[..., :3, :3].copy()
            rotations /= np.linalg.norm(rotations, axis=-2, keepdims=True)
            rotations = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]]) @ rotations
            quaternions = Rotation.from_matrix(rotations.reshape(-1, 3, 3)).as_quat().reshape(*matrices.shape[:-2], 4)
            matrices[..., :3, 3].astype('<f4').tofile(path.parent / 'runtime-positions.bin')
            quaternions.astype('<f4').tofile(path.parent / 'runtime-rotations.bin')
            (path.parent / 'runtime-reference.json').write_text(json.dumps(dict(positionsFile='runtime-positions.bin', rotationsFile='runtime-rotations.bin', shape=list(matrices.shape[:-2]))))
            identifiers.append(report['id'])
    print('Runtime review:', len(identifiers), flush=True)
    subprocess.run(['node', 'scripts/motion_recovery/runtime.mjs', *identifiers], cwd=ROOT, check=True)


if __name__ == '__main__':
    main()
