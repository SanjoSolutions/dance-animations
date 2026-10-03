"""Fit Melissa's saved MPFB braid and color to the standard Woman character."""
from pathlib import Path
import bpy
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


class CharacterHair:
    STYLE = 'braid01'
    COLOR = (54 / 255, 36 / 255, 26 / 255)

    def __init__(self, library, materials, services):
        self.library = library
        self.materials = materials
        self.services = services

    def apply(self):
        body = bpy.data.objects['Woman.body']
        folder = self.library.copy('hair', self.STYLE)
        hair = bpy.data.objects.get('Woman.' + self.STYLE)
        if hair is None:
            hair = self.services.HumanService.add_mhclo_asset(
                str(folder / (self.STYLE + '.mhclo')), body, asset_type='Hair',
                subdiv_levels=0, set_up_rigging=False)
            hair.name = 'Woman.' + self.STYLE
            hair.parent = bpy.data.objects['Woman.rigify_deform']
            hair.matrix_parent_inverse = hair.parent.matrix_world.inverted()
            for group in list(hair.vertex_groups):
                hair.vertex_groups.remove(group)
            group = hair.vertex_groups.new(name='DEF-spine.006')
            group.add(list(range(len(hair.data.vertices))), 1, 'REPLACE')
            modifier = hair.modifiers.new('Hair deformation', 'ARMATURE')
            modifier.object = hair.parent
            collection = bpy.data.collections['Woman']
            for previous in list(hair.users_collection):
                previous.objects.unlink(hair)
            collection.objects.link(hair)
        previous = bpy.data.objects.get('Woman.bob01')
        if previous:
            bpy.data.objects.remove(previous, do_unlink=True)
        self.materials.assign(hair, folder / (self.STYLE + '.mhmat'))
        material = hair.data.materials[0]
        shader = material.node_tree.nodes.get('Principled BSDF')
        texture = next(node for node in material.node_tree.nodes if node.type == 'TEX_IMAGE')
        source = texture.image.copy()
        source.colorspace_settings.name = 'Non-Color'
        pixels = np.empty(len(source.pixels), dtype=np.float32)
        source.pixels.foreach_get(pixels)
        pixels = pixels.reshape((-1, 4))
        # Match a-game's hair shader: tinted luminance with retained strand alpha.
        brightness = pixels[:, :3] @ np.array((.2126, .7152, .0722), dtype=np.float32)
        tint = np.array(self.COLOR, dtype=np.float32)
        tinted = (.35 + .65 * np.sqrt(brightness))[:, None] * tint
        pixels[:, :3] = np.where(tinted <= .04045, tinted / 12.92, ((tinted + .055) / 1.055) ** 2.4)
        image = bpy.data.images.new('Melissa braid - dark brown', width=source.size[0], height=source.size[1], alpha=True)
        image.pixels.foreach_set(pixels.reshape(-1))
        image.filepath_raw = str(ROOT / 'assets/characters/melissa-braid.png')
        image.file_format = 'PNG'
        image.save()
        image.pack()
        texture.image = image
        shader.inputs['Roughness'].default_value = .75
        hair['dance_hair_style'] = self.STYLE
        hair['dance_hair_color'] = '#36241a'
        self.library.records['hair/' + self.STYLE]['changes'] += ' Melissa braid and #36241a color from a-game/playground/playground.tscn, fitted to the standard Woman; head-bone skinning and shader tint baked into the texture.'
        bpy.data.images.remove(source)
