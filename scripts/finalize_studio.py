"""Install the dance library and portable helper startup in the slim studio."""
from pathlib import Path
import sys
import bpy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT / 'scripts'))
import dance_tools

bpy.ops.wm.open_mainfile(filepath=str(ROOT / 'animations/shared_scene_data.blend'))
scene = bpy.context.scene
for actor in ('Man','Woman'):
    collection = bpy.data.collections.get(actor)
    if collection is None:
        collection = bpy.data.collections.new(actor)
        scene.collection.children.link(collection)
    for obj in list(scene.collection.objects):
        if obj.name.startswith(actor + '.'):
            collection.objects.link(obj)
            scene.collection.objects.unlink(obj)
shapes = bpy.data.collections.get('Rig widgets')
if shapes is None:
    shapes = bpy.data.collections.new('Rig widgets')
    scene.collection.children.link(shapes)
for obj in list(scene.collection.objects):
    if obj.name.startswith('WGT-'):
        shapes.objects.link(obj)
        scene.collection.objects.unlink(obj)
        obj.hide_render = True
        obj.hide_set(True)
if scene.objects.get('PoleDance.Pole') is None:
    original = ROOT.parent / 'sanjo-solutions/apps/a-game/man_and_woman3.blend'
    with bpy.data.libraries.load(str(original)) as (available, loaded):
        loaded.objects = ['PoleDance.Pole']
    pole = loaded.objects[0]
    scene.collection.objects.link(pole)
    pole.animation_data_clear()
    pole.hide_set(False)
    pole.hide_viewport = pole.hide_render = False
    props = bpy.data.collections.new('Dance props')
    scene.collection.children.link(props)
    props.objects.link(pole)
    scene.collection.objects.unlink(pole)
    bpy.ops.object.select_all(action='DESELECT')
    pole.select_set(True)
    bpy.context.view_layer.objects.active = pole
    bpy.ops.export_scene.gltf(filepath=str(ROOT/'models/pole.glb'),export_format='GLB',use_selection=True,
        use_active_scene=True,export_animations=False,export_materials='NONE',export_extras=False)
    import json
    catalog = json.loads((ROOT/'catalog.json').read_text())
    catalog['props'] = {'pole':{'file':'models/pole.glb','styles':['pole_dance']}}
    (ROOT/'catalog.json').write_text(json.dumps(catalog,indent=2)+'\n')
    print('Dance pole:',tuple(pole.location),tuple(pole.dimensions),flush=True)
startup = bpy.data.texts.get('dance_helpers.py') or bpy.data.texts.new('dance_helpers.py')
startup.clear()
startup.write('''import bpy
from pathlib import Path
import sys
root = next(directory for directory in Path(bpy.data.filepath).resolve().parents if (directory / "package.json").is_file())
sys.path.insert(0, str(root / "scripts"))
import dance_tools
dance_tools.register()
''')
startup.use_module = True
for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces.active.region_3d.view_distance = 4
            area.spaces.active.region_3d.view_location = (0,0,1)
            area.spaces.active.show_region_ui = True
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT / 'animations/shared_scene_data.blend'),compress=True)
scene['animation_file_directory'] = '//animations'
scene['animation_library_lazy'] = True
# Relink after switching the main path, so all library references are relative to the project root.
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT / 'main.blend'),compress=True)
dance_tools.register()
from track_chooser import TrackChooser
chooser = TrackChooser(scene)
preferred = 'hip_hop_man_bart_simpson'
chooser.apply(preferred)
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT / 'main.blend'),compress=True)
print(f'Dance studio saved: {len(chooser.retrieve_tracks())} native action tracks',flush=True)
