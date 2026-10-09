"""Fit planted native foot targets against evaluated MPFB sole vertices."""
import json
import bpy
from mathutils import Vector
from repair import retrieve_curves


class PlantedSoleRepair:
    def apply(self, action):
        scene=bpy.context.scene
        owner=scene.objects[action.slots[0].identifier[2:]]
        actor=owner.name.split('.')[0]
        original=scene.objects[actor+'.body']
        body=original.copy()
        body.name=actor+'.WaackingSoleReview'
        scene.collection.objects.link(body)
        for modifier in body.modifiers:
            if modifier.type=='MASK' and modifier.name.startswith('Delete.'):
                modifier.show_viewport=False
        visibility=(body.hide_viewport,body.hide_get())
        body.hide_viewport=False;body.hide_set(False)
        groups={side:{group.index for group in body.vertex_groups if group.name.startswith(('DEF-foot','DEF-toe')) and group.name.endswith('.'+side)} for side in 'LR'}
        measurements={side:float('inf') for side in 'LR'}
        counts={side:0 for side in 'LR'}
        frames=sorted({float(point.co.x) for curve in retrieve_curves(action,action.slots[0]) for point in curve.keyframe_points} | {float(value) for value in range(0,int(action.frame_range[1])+1)})
        selected=None
        try:
            for frame in frames:
                scene.frame_set(int(frame),subframe=frame%1)
                graph=bpy.context.evaluated_depsgraph_get();evaluated=body.evaluated_get(graph)
                if selected is None:
                    selected={side:[vertex.index for vertex in evaluated.data.vertices if sum(group.weight for group in vertex.groups if group.group in groups[side])>.8] for side in 'LR'}
                    assert all(selected.values()), selected
                for side in 'LR':
                    heights=[(evaluated.matrix_world @ evaluated.data.vertices[index].co).z for index in selected[side]]
                    measurements[side]=min(measurements[side],min(heights))
                    counts[side]+=len(heights)
        finally:
            bpy.data.objects.remove(body,do_unlink=True)
        assert all(counts.values()),counts
        scene.frame_set(0)
        lifts={}
        for side in 'LR':
            bone=owner.pose.bones['foot_ik.'+side]
            location=bone.location.copy();target=bone.matrix.copy()
            lift=.001-measurements[side]
            target.translation+=owner.matrix_world.inverted().to_3x3() @ Vector((0,0,lift))
            bone.matrix=target;difference=bone.location-location;bone.location=location
            for curve in retrieve_curves(action,action.slots[0]):
                if curve.data_path==bone.path_from_id('location'):
                    offset=difference[curve.array_index]
                    for point in curve.keyframe_points:
                        point.co.y+=offset;point.handle_left.y+=offset;point.handle_right.y+=offset
                    curve.update()
            lifts[side]=lift
        result=dict(minimumSole=measurements,worldLifts=lifts,frames=frames,vertexSamples=counts,units='meters',targetMinimum=.001)
        action['Waacking Sole Calibration']=json.dumps(result)
        print('SOLE_CALIBRATION',action.name,result,flush=True)
