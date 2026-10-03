"""Check distributed notices across platform-specific build dependencies."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import license_notices


class LicenseNoticesTests(unittest.TestCase):
    def test_runtime_and_embedded_notices_with_linux_build_dependency(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            runtime = root / 'node_modules/runtime-library'
            runtime.mkdir(parents=True)
            runtime.joinpath('package.json').write_text(json.dumps({
                'name': 'runtime-library', 'version': '1.0.0', 'license': 'MIT',
            }))
            runtime.joinpath('LICENSE').write_text('Original runtime copyright and license.\n')
            platform = root / 'node_modules/@napi-rs/lzma-linux-x64-gnu'
            platform.mkdir(parents=True)
            platform.joinpath('package.json').write_text(json.dumps({
                'name': '@napi-rs/lzma-linux-x64-gnu', 'version': '1.5.1',
            }))
            root.joinpath('package-lock.json').write_text(json.dumps({'packages': {
                '': {},
                'node_modules/runtime-library': {},
                'node_modules/@napi-rs/lzma-linux-x64-gnu': {'dev': True},
            }}))
            destination = root / 'public/third-party'
            destination.mkdir(parents=True)
            destination.joinpath('meshoptimizer-0.22-MIT.txt').write_text(
                'Original embedded decoder copyright and license.\n')

            with patch.object(license_notices, 'ROOT', root):
                license_notices.LicenseNotices().collect_packages()

            self.assertEqual(destination.joinpath('npm-notices.txt').read_text(),
                             'runtime-library 1.0.0 (MIT)\n'
                             'Original runtime copyright and license.\n\n\n'
                             'Embedded meshoptimizer 0.22 decoder in Three.js\n'
                             'Original embedded decoder copyright and license.\n\n')


if __name__ == '__main__':
    unittest.main()
