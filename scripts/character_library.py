"""Keep editable MPFB body data in a portable Blender character library."""
from pathlib import Path
import bpy

ROOT = Path(__file__).resolve().parents[1]


class CharacterLibrary:
    def __init__(self, root=ROOT):
        self.path = root / 'assets/characters/mpfb-characters.blend'

    @staticmethod
    def localize():
        for actor in ('Man', 'Woman'):
            body = bpy.data.objects[actor + '.body']
            if body.data.library:
                body.data = body.data.copy()

    def write(self):
        # Mesh copies can retain linked shape-key and material dependencies.
        # Localize the character library's remaining IDs before replacing it.
        for owner in list(bpy.data.user_map()):
            if owner.library and Path(bpy.path.abspath(owner.library.filepath)).resolve() == self.path:
                owner.make_local()
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        for library in list(bpy.data.libraries):
            if Path(bpy.path.abspath(library.filepath)).resolve() == self.path:
                if any(owner.library == library for owner in bpy.data.user_map()):
                    raise ValueError('Localize the remaining character dependencies before saving.')
                bpy.data.libraries.remove(library)
        for actor in ('Man', 'Woman'):
            body = bpy.data.objects[actor + '.body']
            if body.data.library or body.data.shape_keys is None:
                raise ValueError('Use local, editable MPFB targets to build the character library.')
            body.data.name = actor + '.body.MPFB.mesh'
        self.path.parent.mkdir(parents=True, exist_ok=True)
        bpy.ops.wm.save_as_mainfile(filepath=str(self.path), compress=True, copy=True, relative_remap=True)
        if self.path.stat().st_size >= 100_000_000:
            raise ValueError('Keep the MPFB character library below 100 MB.')

    def link(self):
        names = [actor + '.body.MPFB.mesh' for actor in ('Man', 'Woman')]
        with bpy.data.libraries.load(str(self.path), link=True) as (available, loaded):
            loaded.meshes = names
        for actor, mesh in zip(('Man', 'Woman'), loaded.meshes):
            if mesh is None:
                raise ValueError('Missing MPFB character mesh for ' + actor)
            bpy.data.objects[actor + '.body'].data = mesh
            mesh.library.filepath = bpy.path.relpath(str(self.path))
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=False, do_recursive=True)
