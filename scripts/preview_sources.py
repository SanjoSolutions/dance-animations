"""Sample saved authored dance studies in Blender for browser quality review.

Run with Blender 5.2 --background --factory-startup --python-exit-code 1
--python scripts/preview_sources.py -- SOURCE_DIRECTORY JOB_JSON RESULT_JSON.
Source Blender files stay byte-identical. Preview exports carry a draft label.
"""
from __future__ import annotations

from array import array
import copy
import json
from pathlib import Path
import struct
import sys
import time

import bpy
from mathutils import Matrix

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from import_assets import read_glb, write_glb

CONVERSION = Matrix(((1,0,0,0),(0,0,1,0),(0,-1,0,0),(0,0,0,1)))


def template_for(actor):
    document, _ = read_glb(ROOT / 'models' / f'mpfb-{actor}.glb')
    for node in document['nodes']:
        for key in ('mesh','skin','weights'):
            node.pop(key, None)
    return document


def sample_clip(record, scene, rigs, baseline):
    loaded = []
    try:
        with bpy.data.libraries.load(str(ROOT / record['file'])) as (available, data):
            data.actions = available.actions
        loaded = data.actions
        action = next((action for action in loaded if action.name == record['id']), None)
        if action is None:
            action = next((action for action in loaded if not action.name.endswith(('.baked','_baked'))), None)
        if action is None:
            raise ValueError('Source has no authored action')
        performers = []
        for obj in rigs.values():
            obj.animation_data_create()
            obj.animation_data.action = None
            for bone in obj.pose.bones:
                bone.matrix_basis = baseline[obj.name][bone.name]
        for slot in action.slots:
            if slot.target_id_type == 'OBJECT':
                obj = scene.objects.get(slot.identifier[2:])
                if obj is not None and obj.name in rigs:
                    obj.animation_data.action = action
                    obj.animation_data.action_slot = slot
                    actor = 'man' if obj.name.startswith('Man.') else 'woman'
                    if actor not in performers:
                        performers.append(actor)
        if not performers:
            raise ValueError('Source slots require another rig')
        start, end = action.frame_range
        fps = scene.render.fps / scene.render.fps_base
        # Sample every source frame and retain the authored fractional key times.
        frames = {float(frame) for frame in range(int(start), int(end) + 1)} | {float(start),float(end)}
        for layer in action.layers:
            for strip in layer.strips:
                for bag in strip.channelbags:
                    for curve in bag.fcurves:
                        frames.update(float(point.co.x) for point in curve.keyframe_points if start <= point.co.x <= end)
        frames = sorted(frames)
        document = {'asset': {'version':'2.0','generator':'Codex saved-source review sampler'},
                    'scene':0,'scenes':[{'name':'Saved-source review','nodes':[]}],
                    'nodes':[], 'animations':[], 'accessors':[], 'bufferViews':[]}
        node_indices = {}
        for actor in performers:
            template = template_for(actor)
            offset = len(document['nodes'])
            document['scenes'][0]['nodes'].extend(index + offset for index in template['scenes'][0]['nodes'])
            for index,node in enumerate(template['nodes']):
                node = copy.deepcopy(node)
                if 'children' in node:
                    node['children'] = [child + offset for child in node['children']]
                document['nodes'].append(node)
                node_indices[actor,node.get('name','')] = index + offset
        tracks = {}
        for actor in performers:
            rig = rigs[actor.capitalize() + '.rigify_deform']
            for bone in rig.pose.bones:
                if (actor,bone.name) in node_indices:
                    for prop in ('translation','rotation','scale'):
                        tracks[actor,bone.name,prop] = []
            for prop in ('translation','rotation','scale'):
                tracks[actor,rig.name,prop] = []
        previous = {}
        for frame in frames:
            scene.frame_set(int(frame), subframe=frame-int(frame))
            depsgraph = bpy.context.evaluated_depsgraph_get()
            for actor in performers:
                rig = rigs[actor.capitalize() + '.rigify_deform'].evaluated_get(depsgraph)
                matrices = {bone.name: (bone.parent.matrix.inverted_safe() @ bone.matrix
                            if bone.parent else CONVERSION @ bone.matrix) for bone in rig.pose.bones
                            if (actor,bone.name) in node_indices}
                matrices[rig.name] = CONVERSION @ rig.matrix_world @ CONVERSION.inverted()
                for name,matrix in matrices.items():
                    position,rotation,scale = matrix.decompose()
                    key = actor,name
                    if key in previous and rotation.dot(previous[key]) < 0:
                        rotation.negate()
                    previous[key] = rotation.copy()
                    tracks[actor,name,'translation'].extend(position)
                    tracks[actor,name,'rotation'].extend((rotation.x,rotation.y,rotation.z,rotation.w))
                    tracks[actor,name,'scale'].extend(scale)
        packed = bytearray()
        def accessor(values, kind, width):
            values = array('f', values)
            view = len(document['bufferViews'])
            document['bufferViews'].append({'buffer':0,'byteOffset':len(packed),'byteLength':len(values)*4})
            packed.extend(values.tobytes())
            index = len(document['accessors'])
            entry = {'bufferView':view,'componentType':5126,'type':kind,'count':len(values)//width}
            if kind == 'SCALAR':
                entry.update(min=[min(values)],max=[max(values)])
            document['accessors'].append(entry)
            return index
        duration = (end-start)/fps
        times = accessor([(frame-start)/fps for frame in frames],'SCALAR',1)
        animation = {'name':record['id']+'.review','samplers':[],'channels':[]}
        for (actor,name,prop),values in tracks.items():
            width = 4 if prop == 'rotation' else 3
            # Preserve a constant transform as one key, sampled at t=0.
            if all(abs(value-values[index % width]) < 1e-7 for index,value in enumerate(values)):
                output = accessor(values[:width], 'VEC4' if width==4 else 'VEC3', width)
                input_index = accessor([0], 'SCALAR', 1)
            else:
                output = accessor(values,'VEC4' if width==4 else 'VEC3',width)
                input_index = times
            sampler = len(animation['samplers'])
            animation['samplers'].append({'input':input_index,'output':output,'interpolation':'LINEAR'})
            animation['channels'].append({'sampler':sampler,'target':{'node':node_indices[actor,name],'path':prop}})
        document['animations'] = [animation]
        destination = ROOT / 'animations' / record['style'] / (record['id']+'.glb')
        write_glb(destination,document,bytes(packed))
        return {'id':record['id'],'style':record['style'], 'label':record['id'].replace('_',' ').capitalize(),
                'performers':sorted(performers),'duration':duration,'file':destination.relative_to(ROOT).as_posix(),
                'sourceFile':record['file'],'originalExport':None,'originalExportSha256':None,
                'sourceSha256':record['sha256'],'animationName':animation['name'],'status':'Saved-source draft preview'}
    finally:
        for obj in rigs.values():
            if obj.animation_data:
                obj.animation_data.action = None
        if loaded:
            bpy.data.batch_remove(ids=loaded)


def main():
    arguments = sys.argv[sys.argv.index('--') + 1:]
    source, jobs, result = map(Path, arguments)
    bpy.ops.wm.open_mainfile(filepath=str(source / 'animations/man_and_woman/shared_scene_data.blend'))
    scene = next(scene for scene in bpy.data.scenes if scene.objects.get('Man.rigify'))
    bpy.context.window.scene = scene
    # Geometry remains in the archived sources and MPFB models. Evaluation needs
    # the rig and its native constraints, so discard unrelated render meshes.
    for obj in list(scene.objects):
        if obj.type in {'MESH','LIGHT','CAMERA'}:
            scene.collection.all_objects.get(obj.name)
            bpy.data.objects.remove(obj,do_unlink=True)
    rigs = {obj.name: obj for obj in scene.objects if obj.type == 'ARMATURE'
            and obj.name in {'Man.rigify','Woman.rigify','Man.rigify_deform','Woman.rigify_deform'}}
    for obj in rigs.values():
        obj.hide_viewport = False
        obj.hide_set(False)
        obj.data.pose_position = 'POSE'
        if obj.animation_data:
            obj.animation_data.action = None
            for track in obj.animation_data.nla_tracks:
                track.mute = True
    baseline = {name:{bone.name:bone.matrix_basis.copy() for bone in obj.pose.bones} for name,obj in rigs.items()}
    results, failures = [], []
    started = time.monotonic()
    for index,record in enumerate(json.loads(jobs.read_text()),1):
        try:
            results.append(sample_clip(record,scene,rigs,baseline))
        except Exception as error:
            failures.append({'id':record['id'],'error':str(error)})
        result.write_text(json.dumps({'animations':results,'failures':failures},indent=2))
        print(f'REVIEW {index} {record["id"]} elapsed={time.monotonic()-started:.1f}s failures={len(failures)}',flush=True)


if __name__ == '__main__':
    main()
