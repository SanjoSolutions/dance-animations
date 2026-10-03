"""Move fitted garment data into portable, editable Blender asset libraries."""
import json
from pathlib import Path
import bpy

ROOT = Path(__file__).resolve().parents[1]


class ClothingLibraries:
    def __init__(self, root=ROOT):
        self.root = root
        self.directory = root / 'assets/wardrobe'
        self.manifest = self.directory / 'libraries.json'

    @staticmethod
    def retrieve_garments():
        return [obj for obj in bpy.context.scene.objects if obj.type == 'MESH'
                and obj.get('dance_wardrobe_asset')]

    def write(self):
        self.directory.mkdir(parents=True, exist_ok=True)
        groups = {}
        for obj in self.retrieve_garments():
            if obj.data.library:
                previous = obj.data
                obj.data = previous.copy()
                if previous.users == 0:
                    bpy.data.meshes.remove(previous)
            for index, material in enumerate(obj.data.materials):
                if material.library:
                    material = material.copy()
                    obj.data.materials[index] = material
                for node in material.node_tree.nodes:
                    if node.type == 'TEX_IMAGE' and node.image and node.image.library:
                        node.image = node.image.copy()
            groups.setdefault(obj['dance_wardrobe_asset'], []).append(obj)
        manifest = {}
        for identifier, garments in sorted(groups.items()):
            path = self.directory / (identifier + '.blend')
            collection = bpy.data.collections.new(identifier)
            meshes = {}
            copies = []
            try:
                for obj in garments:
                    actor = obj.name.split('.', 1)[0]
                    obj.data.name = actor + '.' + identifier + '.mesh'
                    meshes[actor] = obj.data.name
                    source = obj.copy()
                    source.name = actor + '.' + identifier + '.asset'
                    source.parent = None
                    source.matrix_world = obj.matrix_world
                    source.animation_data_clear()
                    for modifier in list(source.modifiers):
                        if modifier.type == 'ARMATURE':
                            source.modifiers.remove(modifier)
                    for constraint in list(source.constraints):
                        source.constraints.remove(constraint)
                    source.hide_viewport = source.hide_render = False
                    collection.objects.link(source)
                    copies.append(source)
                collection['dance_wardrobe_asset'] = identifier
                bpy.data.libraries.write(str(path), {collection}, path_remap='RELATIVE_ALL', compress=True)
                if path.stat().st_size >= 100_000_000:
                    raise ValueError(f'Split the garment library to keep it below 100 MB: {identifier}')
                manifest[identifier] = dict(file=path.relative_to(self.root).as_posix(), meshes=meshes)
                print('Clothing library:', identifier, path.stat().st_size, flush=True)
            finally:
                bpy.data.collections.remove(collection)
                for obj in copies:
                    bpy.data.objects.remove(obj, do_unlink=True)
        self.manifest.write_text(json.dumps(manifest, indent=2) + '\n', newline='\n')

    def link(self):
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        manifest = json.loads(self.manifest.read_text())
        for identifier, entry in manifest.items():
            garments = [obj for obj in self.retrieve_garments() if obj['dance_wardrobe_asset'] == identifier]
            path = self.root / entry['file']
            with bpy.data.libraries.load(str(path), link=True) as (available, loaded):
                loaded.meshes = list(entry['meshes'].values())
            meshes = {mesh.name: mesh for mesh in loaded.meshes}
            for obj in garments:
                actor = obj.name.split('.', 1)[0]
                mesh = meshes[entry['meshes'][actor]]
                obj.data = mesh
                mesh.library.filepath = bpy.path.relpath(str(path))
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=False, do_recursive=True)


def retrieve_samples():
    bpy.context.view_layer.update()
    graph = bpy.context.evaluated_depsgraph_get()
    samples = {}
    for obj in ClothingLibraries.retrieve_garments():
        evaluated = obj.evaluated_get(graph)
        mesh = evaluated.to_mesh()
        samples[obj.name] = [evaluated.matrix_world @ mesh.vertices[index].co
                             for index in (0, len(mesh.vertices) // 2, len(mesh.vertices) - 1)]
        evaluated.to_mesh_clear()
    return samples


def main():
    for index, path in enumerate((ROOT / 'animations/shared_scene_data.blend', ROOT / 'main.blend')):
        bpy.ops.wm.open_mainfile(filepath=str(path))
        before = retrieve_samples()
        libraries = ClothingLibraries()
        if index == 0:
            libraries.write()
        libraries.link()
        after = retrieve_samples()
        difference = max((original - actual).length for name, points in before.items()
                         for original, actual in zip(points, after[name]))
        if difference > 1e-6:
            raise ValueError(f'Linked clothing changes the evaluated fit: {difference}')
        bpy.ops.wm.save_as_mainfile(filepath=str(path), compress=True)
        if path.stat().st_size >= 100_000_000:
            raise ValueError(f'Keep the studio below 100 MB: {path.name}')
        print('Linked wardrobe:', path.name, path.stat().st_size, 'maximum fit difference', difference, flush=True)


if __name__ == '__main__':
    main()
