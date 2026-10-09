"""Review sampled own-arm clearance on a full native MPFB body copy."""
import json,sys
from pathlib import Path
import bpy
from mathutils.bvhtree import BVHTree
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts/motion_recovery'))
from repair import digest
import dance_tools
from track_chooser import TrackChooser


def main():
    identifier=sys.argv[sys.argv.index('--')+1];directory=ROOT/'.cache/motion-recovery'/identifier
    report=json.loads((directory/'checkpoint.json').read_text());bpy.ops.wm.open_mainfile(filepath=str(ROOT/report['source']));dance_tools.register()
    scene=bpy.context.scene;TrackChooser(scene).apply(identifier);actor=report['performers'][0].capitalize()
    for suffix in ('.rigify','.rigify_deform'):
        rig=scene.objects[actor+suffix];rig.hide_viewport=False;rig.hide_set(False)
    original=scene.objects[actor+'.body'];body=original.copy();scene.collection.objects.link(body);body.hide_viewport=False;body.hide_set(False)
    for modifier in body.modifiers:
        if modifier.type=='MASK' and modifier.name.startswith('Delete.'):modifier.show_viewport=False
    groups={group.index:group.name for group in body.vertex_groups}
    def classify(vertex):
        totals={'torso':0,'head':0,'legs':0,'L':0,'R':0}
        for weight in vertex.groups:
            name=groups[weight.group]
            if name in ('DEF-spine','DEF-spine.001','DEF-spine.002','DEF-spine.003','DEF-spine.004'):totals['torso']+=weight.weight
            if name in ('DEF-spine.005','DEF-spine.006'):totals['head']+=weight.weight
            if name.startswith(('DEF-thigh','DEF-shin','DEF-foot','DEF-toe')):totals['legs']+=weight.weight
            for side in 'LR':
                belongs=name.endswith('.'+side) or ('.'+side+'.') in name
                limb=name.startswith(('DEF-forearm','DEF-hand','DEF-f_','DEF-thumb','DEF-palm')) or name=='DEF-upper_arm.'+side+'.001'
                if belongs and limb:totals[side]+=weight.weight
        return {key for key,value in totals.items() if value>.65}
    frames=[index*report['rate']/48 for index in range(193)]
    regions=None;events=[];maximum={};coverage={}
    pairs=[('L','torso'),('R','torso'),('L','head'),('R','head'),('L','legs'),('R','legs'),('L','R')]
    try:
        for frame in frames:
            scene.frame_set(int(frame),subframe=frame%1);evaluated=body.evaluated_get(bpy.context.evaluated_depsgraph_get());mesh=evaluated.data
            if regions is None:
                membership=[classify(vertex) for vertex in mesh.vertices]
                regions={name:[tuple(polygon.vertices) for polygon in mesh.polygons if all(name in membership[index] for index in polygon.vertices)] for name in ('torso','head','legs','L','R')}
                coverage={name:len(polygons) for name,polygons in regions.items()}
            points=[evaluated.matrix_world @ vertex.co for vertex in mesh.vertices]
            trees={name:BVHTree.FromPolygons(points,polygons) for name,polygons in regions.items() if polygons}
            for first,second in pairs:
                if first in trees and second in trees:
                    overlaps=trees[first].overlap(trees[second]);key=first+'-'+second;maximum[key]=max(maximum.get(key,0),len(overlaps))
                    if overlaps:events.append(dict(frame=frame,pair=key,intersectingTrianglePairs=len(overlaps)))
    finally:bpy.data.objects.remove(body,do_unlink=True)
    result=dict(sourceSha256=report['sourceSha256'],exportSha256=report['exportSha256'],generatorSha256=digest(__file__),sampledFrames=frames,regionPolygons=coverage,maximumIntersectionPairs=maximum,events=events,
        coverage='Full MPFB body copy; distal upper arms, forearms, hands and fingers against torso, head, legs and opposite arm; threshold >0.65 summed skin weight. Native source masks preserved.',
        coverageStatus={name:'measured' if count else 'empty region' for name,count in coverage.items()},upperArms='Joint-adjacent upper arms require visual review',partner='Solo clips',passed=not events and all(coverage.values()))
    (directory/'clearance.json').write_text(json.dumps(result,indent=2)+'\n');print('SURFACE_CLEARANCE',identifier,json.dumps(dict(regions=coverage,maximum=maximum,events=len(events))),flush=True)


if __name__=='__main__':main()
