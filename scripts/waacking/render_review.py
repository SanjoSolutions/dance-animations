"""Render native MPFB playback from three views in an isolated review scene."""
import json,math,sys
from pathlib import Path
import bpy
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts/motion_recovery'))
from repair import digest
import dance_tools
from track_chooser import TrackChooser


def main():
    identifier=sys.argv[sys.argv.index('--')+1]
    directory=ROOT/'.cache/motion-recovery'/identifier
    report=json.loads((directory/'checkpoint.json').read_text())
    bpy.ops.wm.open_mainfile(filepath=str(ROOT/report['source']));dance_tools.register()
    scene=bpy.context.scene;TrackChooser(scene).apply(identifier)
    actor=report['performers'][0].capitalize();rigs=[scene.objects[actor+suffix] for suffix in ('.rigify','.rigify_deform')]
    for rig in rigs:rig.hide_viewport=False;rig.hide_set(False)
    for obj in scene.objects:
        if obj.type=='MESH':
            obj.hide_render=not (obj.name.startswith(actor+'.') and not obj.hide_render)
    bpy.ops.mesh.primitive_plane_add(size=6,location=(0,0,-.002));floor=bpy.context.object;floor.color=(.15,.18,.22,1)
    bpy.ops.object.camera_add();scene.camera=bpy.context.object;scene.camera.data.type='ORTHO';scene.camera.data.ortho_scale=2.35
    scene.render.engine='BLENDER_WORKBENCH';scene.display.shading.light='STUDIO';scene.display.shading.color_type='MATERIAL'
    scene.display.shading.show_shadows=True;scene.display.shading.show_cavity=True;scene.display.shading.background_type='WORLD';scene.world.color=(.18,.20,.24)
    scene.render.resolution_x=240;scene.render.resolution_y=320;scene.render.resolution_percentage=100
    scene.render.image_settings.file_format='PNG';scene.render.film_transparent=False
    output=directory/'views';output.mkdir(exist_ok=True)
    samples=[]
    frames=[index*8 for index in range(12)]
    for view,position in [('front',(0,-4,1.1)),('side',(4,0,1.1)),('back',(0,4,1.1))]:
        scene.camera.location=position;scene.camera.rotation_euler=(Vector((0,0,.96))-scene.camera.location).to_track_quat('-Z','Y').to_euler()
        for original in frames:
            frame=original*report['rate']/24
            scene.frame_set(-1);scene.frame_set(int(frame),subframe=frame%1)
            path=output/f'{view}-{original:03}.png';scene.render.filepath=str(path);bpy.ops.render.render(write_still=True)
            samples.append(dict(view=view,frame=frame,file=path.relative_to(ROOT).as_posix(),sha256=digest(path)))
    (directory/'visual-capture.json').write_text(json.dumps(dict(sourceSha256=report['sourceSha256'],exportSha256=report['exportSha256'],generatorSha256=digest(__file__),frames=samples,coverage='Native MPFB surfaces; 12 poses and three views; visual inspection recorded separately'),indent=2)+'\n')


if __name__=='__main__':main()
