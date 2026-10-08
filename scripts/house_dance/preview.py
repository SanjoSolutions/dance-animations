"""Render saved House motion on the project's MPFB bodies and street wardrobe."""
import json
import math
from pathlib import Path
import sys

import bpy
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
import dance_tools
from track_chooser import TrackChooser


def main():
    arguments = sys.argv[sys.argv.index('--') + 1:]
    source = Path(arguments[0]).resolve()
    destination = Path(arguments[1]).resolve()
    frames = [float(value) for value in arguments[2:]] or [0, 6, 12, 30, 48, 72]
    destination.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(source))
    dance_tools.register()
    scene = bpy.context.scene
    TrackChooser(scene).apply(source.stem)
    actor = 'Man' if source.stem.startswith('house_man_') else 'Woman'
    rig = scene.objects[actor + '.rigify_deform']
    control = scene.objects[actor + '.rigify']
    for obj in (rig, control):
        obj.hide_viewport = False
        obj.hide_set(False)
    visible = [obj for obj in scene.objects if obj.type == 'MESH' and not obj.hide_render
               and (obj.name.startswith(actor + '.') or obj.parent in (rig, control)
                    or any(mod.type == 'ARMATURE' and mod.object in (rig, control) for mod in obj.modifiers))]
    for obj in scene.objects:
        if obj.type == 'MESH':
            obj.hide_render = obj not in visible
    for name in ('Camera', 'Camera.001'):
        camera = bpy.data.objects.get(name)
        if camera: camera.hide_render = True
    bpy.ops.mesh.primitive_plane_add(size=8, location=(0, 0, -0.003))
    plane = bpy.context.object
    material = bpy.data.materials.new('House review floor')
    material.diffuse_color = (.15, .18, .22, 1)
    plane.data.materials.append(material)
    bpy.ops.object.camera_add(location=(3.0, -4.5, 2.35))
    scene.camera = bpy.context.object
    scene.camera.rotation_euler = (Vector((0, 0, .85)) - scene.camera.location).to_track_quat('-Z', 'Y').to_euler()
    scene.camera.data.type = 'ORTHO'
    scene.camera.data.ortho_scale = 2.5
    for position, power, size in [((2,-3,4),700,4),((-3,-1,2),500,3),((0,3,4),800,3)]:
        bpy.ops.object.light_add(type='AREA', location=position)
        light = bpy.context.object
        light.data.energy, light.data.shape, light.data.size = power, 'DISK', size
        light.rotation_euler = (Vector((0,0,.8)) - light.location).to_track_quat('-Z','Y').to_euler()
    scene.render.engine = 'CYCLES'
    scene.cycles.samples = 8
    scene.cycles.use_denoising = True
    scene.render.resolution_x, scene.render.resolution_y = 400, 440
    scene.render.resolution_percentage = 100
    scene.world.color = (.3,.3,.3)
    scene.render.image_settings.file_format = 'PNG'
    scene.frame_set(0)
    for frame in frames:
        scene.frame_set(math.floor(frame), subframe=frame % 1)
        scene.render.filepath = str(destination / (f'{source.stem}-{frame:g}.png'))
        bpy.ops.render.render(write_still=True)


if __name__ == '__main__':
    main()
