"""Fit local MPFB assets to the studio and export textured clothing variants.

Run with the configured Blender 5.2 MPFB extension enabled:
blender --background --python-exit-code 1 --python scripts/build_wardrobe.py
Pass -- <MPFB data directory> to select another installed asset library.
"""
import argparse
import importlib
import json
from pathlib import Path
import shutil
import sys
import bpy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from wardrobe import apply_profile
from suit_clothing import remove_tie
from link_wardrobe import ClothingLibraries
from clothing_coverage import apply_full_length_coverage, separate_waist_layers
from character_library import CharacterLibrary
from rig_schema import retain_dance_bones
from character_hair import CharacterHair


class AssetLibrary:
    def __init__(self, source):
        self.source = source
        self.destination = ROOT / 'assets/mpfb'
        self.records = {}

    def copy(self, category, identifier):
        relative = Path(category) / identifier
        destination = self.destination / relative
        if not destination.exists():
            shutil.copytree(self.source / relative, destination)
        headers = list(destination.glob('*.mhclo')) or list(destination.glob('*.mhmat'))
        header = headers[0].read_text(errors='replace')
        author = next((line.removeprefix('# author ').strip() for line in header.splitlines() if line.startswith('# author ')), 'MakeHuman system assets: Data Collection AB, Joel Palmius, Jonas Hauquier')
        license = next((line.removeprefix('# license ').strip() for line in header.splitlines() if line.startswith('# license ')), 'CC0 (September 2020 release)')
        self.records[relative.as_posix()] = dict(author=author, license=license, source='https://static.makehumancommunity.org/assets/assetpacks.html', changes='Fitted to standard MPFB characters, PBR material conversion, skinned GLB export. Original asset files retained.')
        if identifier == 'toigo_male_suit_3':
            self.records[relative.as_posix()]['changes'] += ' Tie geometry removed for the plain-shirt outfit.'
        if identifier in ('toigo_fisherman_sweater', 'toigo_wool_pants'):
            self.records[relative.as_posix()]['changes'] += ' Body coverage masks added for the full-length women\'s outfits.'
        return destination


class MaterialLibrary:
    def __init__(self):
        self.materials = {}

    def retrieve(self, path):
        if path not in self.materials:
            fields = {}
            for line in path.read_text(errors='replace').splitlines():
                words = line.split()
                if words and words[0] != '#':
                    fields[words[0]] = words[1:]
            material = bpy.data.materials.new(path.parent.name + ' texture')
            material.use_nodes = True
            shader = material.node_tree.nodes.get('Principled BSDF')
            shader.inputs['Roughness'].default_value = .7
            color = fields.get('diffuseColor', ['1', '1', '1'])
            shader.inputs['Base Color'].default_value = (*map(float, color), 1)
            links = material.node_tree.links
            for key, socket in [('diffuseTexture', 'Base Color'), ('normalmapTexture', 'Normal')]:
                if key in fields:
                    image_path = path.parent / ' '.join(fields[key])
                    if image_path.is_file():
                        node = material.node_tree.nodes.new('ShaderNodeTexImage')
                        node.image = bpy.data.images.load(str(image_path), check_existing=True)
                        if node.image.library:
                            node.image = node.image.copy()
                        node.image.pack()
                        if key == 'normalmapTexture':
                            node.image.colorspace_settings.name = 'Non-Color'
                            normal = material.node_tree.nodes.new('ShaderNodeNormalMap')
                            links.new(node.outputs['Color'], normal.inputs['Color'])
                            links.new(normal.outputs['Normal'], shader.inputs['Normal'])
                        else:
                            links.new(node.outputs['Color'], shader.inputs[socket])
                            if fields.get('transparent') == ['True'] or 'hair' in path.parts or 'eyebrows' in path.parts or 'eyelashes' in path.parts:
                                links.new(node.outputs['Alpha'], shader.inputs['Alpha'])
                                material.surface_render_method = 'DITHERED'
            material.use_backface_culling = False
            self.materials[path] = material
        return self.materials[path]

    def assign(self, obj, path):
        obj.data.materials.clear()
        obj.data.materials.append(self.retrieve(path))
        for polygon in obj.data.polygons:
            polygon.material_index = 0


class WardrobeBuilder:
    def __init__(self, library, configuration):
        self.library = library
        self.configuration = configuration
        self.services = importlib.import_module('bl_ext.blender_org.mpfb.services')
        self.materials = MaterialLibrary()

    @staticmethod
    def organize_characters():
        for actor in ('Man', 'Woman'):
            parent = bpy.data.collections.get(actor)
            if parent is None:
                parent = bpy.data.collections.new(actor)
                bpy.context.scene.collection.children.link(parent)
            wardrobe = bpy.data.collections.get(actor + '.Wardrobe')
            if wardrobe and wardrobe.name in bpy.context.scene.collection.children:
                bpy.context.scene.collection.children.unlink(wardrobe)
                parent.children.link(wardrobe)
            for obj in list(bpy.context.scene.collection.objects):
                if obj.name.startswith(actor + '.'):
                    parent.objects.link(obj)
                    bpy.context.scene.collection.objects.unlink(obj)

    def texture_characters(self):
        for actor in ('Man', 'Woman'):
            skin = 'young_caucasian_' + ('male' if actor == 'Man' else 'female')
            self.materials.assign(bpy.data.objects[actor + '.body'], self.library.copy('skins', skin) / (skin + '.mhmat'))
            bpy.data.objects[actor + '.body'].MPFB_HUM_material_source = f'{skin}/{skin}.mhmat'
            parts = {'high-poly': ('eyes', 'materials', 'brown.mhmat'), 'bob01': ('hair', 'bob01', 'bob01.mhmat'), 'eyebrow007': ('eyebrows', 'eyebrow007', 'eyebrow007.mhmat'), 'eyelashes01': ('eyelashes', 'eyelashes01', 'eyelashes01.mhmat'), 'teeth_base': ('teeth', 'teeth_base', 'teeth_base.mhmat'), 'tongue01': ('tongue', 'tongue01', 'tongue01.mhmat')}
            for name, (category, identifier, filename) in parts.items():
                obj = bpy.data.objects.get(actor + '.' + name)
                if obj:
                    path = self.library.copy(category, identifier) / filename
                    if path.is_file():
                        self.materials.assign(obj, path)
        CharacterHair(self.library, self.materials, self.services).apply()

    def fit_clothes(self):
        for actor in ('Man', 'Woman'):
            body = bpy.data.objects[actor + '.body']
            masks = {}
            identifiers = sorted({identifier for profile in self.configuration['profiles'].values() for identifier in profile[actor.lower()]})
            for group in list(body.vertex_groups):
                if group.name.startswith('Delete.') and group.name.removeprefix('Delete.') not in identifiers:
                    body.vertex_groups.remove(group)
            for obj in list(bpy.context.scene.objects):
                identifier = obj.get('dance_wardrobe_asset')
                if obj.name.startswith(actor + '.') and identifier and identifier not in identifiers:
                    for modifier in list(body.modifiers):
                        if modifier.name == 'Delete.' + identifier:
                            body.modifiers.remove(modifier)
                    bpy.data.objects.remove(obj, do_unlink=True)
            for identifier in identifiers:
                profiles = [name for name, profile in self.configuration['profiles'].items() if identifier in profile[actor.lower()]]
                path = self.library.copy('clothes', identifier) / (identifier + '.mhclo')
                obj = next((obj for obj in bpy.context.scene.objects if obj.name.startswith(actor + '.') and obj.get('dance_wardrobe_asset') == identifier), None)
                if obj is None:
                    obj = self.services.HumanService.add_mhclo_asset(str(path), body, subdiv_levels=0, material_type='MAKESKIN', set_up_rigging=True, interpolate_weights=True, import_subrig=False, import_weights=False)
                obj['dance_wardrobe_asset'] = identifier
                obj['dance_wardrobe_profiles'] = json.dumps(profiles)
                if obj.data.library:
                    previous = obj.data
                    obj.data = previous.copy()
                    if previous.users == 0:
                        bpy.data.meshes.remove(previous)
                remove_tie(obj)
                material_name = next(line.split(maxsplit=1)[1] for line in path.read_text().splitlines() if line.startswith('material '))
                self.materials.assign(obj, path.parent / material_name)
                if actor == 'Woman':
                    apply_full_length_coverage(body, obj)
                # MPFB's garment masks retain the actual asset name in the modifier.
                for modifier in body.modifiers:
                    if modifier.type == 'MASK' and modifier.name == 'Delete.' + identifier:
                        masks[modifier.name] = profiles
                collection = bpy.data.collections.get(actor + '.Wardrobe')
                if collection is None:
                    collection = bpy.data.collections.new(actor + '.Wardrobe')
                    parent = bpy.data.collections.get(actor) or bpy.context.scene.collection
                    parent.children.link(collection)
                for previous in list(obj.users_collection):
                    previous.objects.unlink(obj)
                collection.objects.link(obj)
                print('Fitted', actor, identifier, len(obj.data.vertices), flush=True)
            body['dance_wardrobe_masks'] = json.dumps(masks)
            if actor == 'Woman':
                garments = {obj['dance_wardrobe_asset']: obj for obj in bpy.context.scene.objects
                            if obj.name.startswith(actor + '.') and obj.get('dance_wardrobe_asset')}
                separate_waist_layers(garments['toigo_fisherman_sweater'], garments['toigo_wool_pants'])

    def export(self, profile, actor):
        apply_profile(profile)
        bpy.ops.object.select_all(action='DESELECT')
        rig = bpy.data.objects[actor + '.rigify_deform']
        rig.hide_set(False)
        rig.select_set(True)
        muted = [(constraint, constraint.mute) for bone in rig.pose.bones for constraint in bone.constraints]
        for constraint, previous in muted:
            constraint.mute = True
        rig.data.pose_position = 'REST'
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH' and obj.name.startswith(actor + '.') and not obj.hide_render:
                obj.hide_set(False)
                obj.select_set(True)
        bpy.context.view_layer.objects.active = rig
        destination = ROOT / 'models' / ('wardrobe/' + profile + '/mpfb-' + actor.lower() + '.glb' if profile else 'mpfb-' + actor.lower() + '.glb')
        destination.parent.mkdir(parents=True, exist_ok=True)
        bpy.ops.export_scene.gltf(filepath=str(destination), export_format='GLB', use_selection=True, export_animations=False, export_skins=True, export_def_bones=True, export_morph=False, export_apply=True, export_extras=False, export_cameras=False, export_lights=False)
        rig.data.pose_position = 'POSE'
        for constraint, previous in muted:
            constraint.mute = previous


def main():
    configuration = json.loads((ROOT / 'wardrobe.json').read_text())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', nargs='?', type=Path, default=Path.home() / 'Documents/blender/mpfb/data')
    parser.add_argument('--profiles', nargs='+', choices=configuration['profiles'])
    parser.add_argument('--characters', nargs='+', choices=('man', 'woman'), default=('man', 'woman'))
    arguments = parser.parse_args(sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else [])
    library = AssetLibrary(arguments.source)
    template = ROOT / 'animations/shared_scene_data.blend'
    for path in (template, ROOT / 'main.blend'):
        bpy.ops.wm.open_mainfile(filepath=str(path))
        CharacterLibrary.localize()
        retain_dance_bones()
        builder = WardrobeBuilder(library, configuration)
        builder.organize_characters()
        builder.texture_characters()
        builder.fit_clothes()
        if path == template:
            for profile in arguments.profiles or [None, *configuration['profiles']]:
                for actor in arguments.characters:
                    builder.export(profile, actor.capitalize())
        clothing = ClothingLibraries()
        if path == template:
            clothing.write()
        clothing.link()
        apply_profile(configuration['default'])
        characters = CharacterLibrary()
        if path == template:
            characters.write()
        characters.link()
        for image in bpy.data.images:
            if image.packed_file and image.library is None:
                image.filepath = bpy.path.relpath(image.filepath, start=str(path.parent))
        for screen in bpy.data.screens:
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    area.spaces.active.shading.type = 'MATERIAL'
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=False, do_recursive=True)
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.wm.save_as_mainfile(filepath=str(path), compress=True)
        if path.stat().st_size >= 100_000_000:
            raise ValueError(f'Keep the studio below 100 MB: {path.name}')
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    for model in catalog['models'].values():
        model['description'] = 'Textured standard MPFB base body on the native DEF animation rig; clothed style variants under models/wardrobe/.'
    catalog['wardrobe'] = dict(default=configuration['default'], profiles={name: dict(label=profile['label'], styles=profile['styles'], models={actor: dict(file=f'models/wardrobe/{name}/mpfb-{actor}.glb') for actor in ('man', 'woman')}) for name, profile in configuration['profiles'].items()})
    (ROOT / 'catalog.json').write_text(json.dumps(catalog, indent=2) + '\n', newline='\n')
    (ROOT / 'assets/mpfb/attribution.json').write_text(json.dumps(library.records, indent=2) + '\n', newline='\n')
    print('Textured MPFB wardrobe and portable studios saved.', flush=True)


if __name__ == '__main__':
    main()
