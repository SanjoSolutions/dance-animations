"""Promote reviewed candidates with portable descriptors and exact curve parity.

Run with Blender, followed by compression, audit_installed.py, and runtime.mjs.
"""

import hashlib
import json
import os
from pathlib import Path
import shutil
import sys

import bpy
import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fingerprint(actions):
    result = hashlib.sha256(b'motion-curves-v2')
    def encode(value):
        result.update(json.dumps(value, separators=(',', ':')).encode())
        result.update(b'\n')
    for action in sorted(actions, key=lambda action: action.name):
        encode([action.name, list(action.frame_range), action.use_frame_range, action.use_cyclic,
                [(slot.identifier, slot.handle) for slot in action.slots]])
        for layer in action.layers:
            for strip in layer.strips:
                for bag in strip.channelbags:
                    for curve in bag.fcurves:
                        points = curve.keyframe_points
                        encode([bag.slot_handle, curve.data_path, curve.array_index, curve.extrapolation, curve.mute, len(points)])
                        values = np.empty(len(points) * 2, dtype=np.float32)
                        for attribute in ('co', 'handle_left', 'handle_right'):
                            points.foreach_get(attribute, values)
                            result.update(values.astype('<f4', copy=False).tobytes())
                        encode([[point.interpolation, point.handle_left_type, point.handle_right_type] for point in points])
    return result.hexdigest()


class CandidateInstaller:
    def __init__(self):
        self.catalog_path = ROOT / 'catalog.json'
        self.inventory_path = ROOT / 'source-inventory.json'
        self.catalog = json.loads(self.catalog_path.read_text())
        self.inventory = json.loads(self.inventory_path.read_text())
        self.entries = {entry['id']: entry for entry in self.catalog['animations']}
        self.sources = {entry['id']: entry for entry in self.inventory}

    def install(self, identifier):
        directory = ROOT / '.cache/motion-recovery' / identifier
        report = json.loads((directory / 'checkpoint.json').read_text())
        runtime = json.loads((directory / 'runtime.json').read_text())
        assert report['stage'] == 'saved source and bake validated'
        assert runtime['passed'] and runtime['sourceSha256'] == report['sourceSha256']
        assert digest(ROOT / report['source']) == report['sourceSha256']
        assert digest(ROOT / report['export']) == runtime['exportSha256'] == report['exportSha256']
        assert all(digest(ROOT / path) == value for path, value in report['dependencies'].items())
        surfaces = json.loads((directory / 'surfaces.json').read_text())
        assert surfaces['exportSha256'] == report['exportSha256']
        assert min(foot['minimum'] for foot in surfaces['feet']) >= -.002, identifier
        if report['loop']:
            loop = json.loads((directory / 'loop.json').read_text())
            assert loop['passed'] and loop['exportSha256'] == report['exportSha256'], identifier
        if report['style'] in ('new_york_hustle', 'salsa'):
            contacts = json.loads((directory / 'contacts.json').read_text())
            assert contacts['passed'] and contacts['sourceSha256'] == report['sourceSha256']
        entry = self.entries.get(identifier)
        source = ROOT / 'animations' / report['style'] / 'sources' / (identifier + '.blend')
        export = source.parent.parent / (identifier + '.glb')
        backup = directory / 'baseline'
        backup.mkdir(exist_ok=True)
        if entry:
            assert digest(source) == report['baselineSource'], identifier
            assert digest(export) == report['baselineExport'], identifier
            for path, revision in ((source, report['baselineSource']), (export, report['baselineExport'])):
                if not (backup / path.name).exists():
                    shutil.copy2(path, backup / path.name)
                else:
                    shutil.copy2(path, backup / (path.stem + '-' + revision + path.suffix))
        else:
            assert not source.exists() and not export.exists(), identifier
            entry = dict(id=identifier, style=report['style'], label=identifier.removeprefix(report['style'] + '_').replace('_', ' ').capitalize(),
                         performers=report['performers'], sourceFile=str(source.relative_to(ROOT)), file=str(export.relative_to(ROOT)),
                         originalExport=None, originalExportSha256=None, status='Saved-source draft preview', recipeProvenance='scripts/popping/provenance.json')
            self.catalog['animations'].append(entry)
            self.entries[identifier] = entry
        bpy.ops.wm.read_factory_settings(use_empty=True)
        with bpy.data.libraries.load(str(ROOT / report['source']), link=False) as (available, loaded):
            loaded.actions = available.actions
            loaded.scenes = available.scenes
        actions = loaded.actions
        descriptor = next(scene for scene in loaded.scenes if scene.get('animation_file_template'))
        before = fingerprint(actions)
        descriptor['animation_file_template'] = '../../shared_scene_data.blend'
        source.parent.mkdir(parents=True, exist_ok=True)
        bpy.data.libraries.write(str(source), {descriptor, *actions}, path_remap='RELATIVE_ALL', compress=True)
        bpy.ops.wm.read_factory_settings(use_empty=True)
        with bpy.data.libraries.load(str(source), link=False) as (available, loaded):
            loaded.actions = available.actions
            loaded.scenes = available.scenes
        assert fingerprint(loaded.actions) == before, identifier
        descriptor = next(scene for scene in loaded.scenes if scene.get('animation_file_template'))
        assert (source.parent / descriptor['animation_file_template']).resolve() == ROOT / 'animations/shared_scene_data.blend'
        assert descriptor.render.fps / descriptor.render.fps_base == report['rate']
        shutil.copy2(ROOT / report['export'], export)
        entry.update(sourceSha256=digest(source), animationName=runtime['animation'], duration=runtime['duration'],
                     studyStatus='Procedural study; native source, bake, and runtime checked')
        if identifier in self.sources:
            record = self.sources[identifier]
            record.setdefault('originalSha256', record['sha256'])
        else:
            record = dict(id=identifier, style=report['style'], file=str(source.relative_to(ROOT)), original=None,
                          recipeProvenance='scripts/popping/provenance.json')
            self.inventory.append(record)
            self.sources[identifier] = record
        record.update(sha256=digest(source), bytes=source.stat().st_size, runtimeExport=str(export.relative_to(ROOT)))
        installation = dict(source=str(source.relative_to(ROOT)), export=str(export.relative_to(ROOT)), sourceSha256=digest(source),
                            candidateSourceSha256=report['sourceSha256'], candidateExportSha256=report['exportSha256'],
                            actionFingerprint=before, fingerprintAlgorithm='sha256-curves-v2', descriptor='../../shared_scene_data.blend', exactCurveParity=True)
        (directory / 'installation.json').write_text(json.dumps(installation, indent=2) + '\n')
        print('INSTALLED', identifier, flush=True)

    def save_catalogs(self):
        for style in self.catalog['styles']:
            style['playable'] = sum(entry['style'] == style['id'] for entry in self.catalog['animations'])
            style['sources'] = sum(entry['style'] == style['id'] for entry in self.inventory)
        self.catalog['sourceCount'] = len(self.inventory)
        self.catalog['sourceOnlyCount'] = sum(not entry.get('runtimeExport') for entry in self.inventory)
        for path, value in ((self.catalog_path, self.catalog), (self.inventory_path, self.inventory)):
            temporary = path.with_suffix('.json.motion-recovery')
            temporary.write_text(json.dumps(value, indent=2) + '\n')
            os.replace(temporary, path)


if __name__ == '__main__':
    installer = CandidateInstaller()
    for identifier in sys.argv[sys.argv.index('--') + 1:]:
        installer.install(identifier)
        installer.save_catalogs()
