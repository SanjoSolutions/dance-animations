"""House target solving on the studio's native controls and saved neutral pose."""
import json
from pathlib import Path

import bpy

from ik_pose import CONTROLS, PoseSolver, PoseTarget, RigControls
from mathutils import Matrix


class HouseRig:
    def __init__(self):
        self.rigs = {role: bpy.context.scene.objects[actor + '.rigify']
                     for role, actor in (('player', 'Man'), ('partner', 'Woman'))}
        self.controls = RigControls(bpy.context, self.rigs)
        self.solver = PoseSolver(self.controls, tolerance=0.0005)
        self.reference = json.loads(Path(__file__).with_name('reference.json').read_text())
        self.base = {role: values['targets'] for role, values in self.reference['actors'].items()}
        self.restore()

    def restore(self):
        for role, rig in self.rigs.items():
            deform = bpy.context.scene.objects[rig.name + '_deform']
            deform.hide_viewport = False
            deform.hide_set(False)
            deform.animation_data_create()
            deform.animation_data.action = None
            deform.animation_data.use_nla = False
            for bone in deform.pose.bones:
                bone.matrix_basis = Matrix.Identity(4)
                for constraint in bone.constraints:
                    constraint.mute = False
            rig.hide_viewport = False
            rig.hide_set(False)
            animation = rig.animation_data_create()
            animation.action = None
            animation.use_nla = False
            for name, values in self.reference['actors'][role]['bones'].items():
                bone = rig.pose.bones[name]
                for prop in ('location', 'rotation_quaternion', 'rotation_euler', 'scale'):
                    setattr(bone, prop, values[prop])
                # The studio's saved rotation modes define action playback.
                if bone.rotation_mode != values['rotation_mode']:
                    raise ValueError(f'Neutral pose rotation mode differs: {rig.name}/{name}')
                for key, value in values['properties'].items():
                    bone[key] = value
        self.controls.rigs = self.rigs
        self.controls.update()

    def solve(self, actor, specifications):
        targets = [PoseTarget(self.controls, actor, name, specifications[name])
                   for name in CONTROLS if name in specifications
                   and not name.endswith(('hand', 'foot', 'palm'))]
        targets.extend(PoseTarget(self.controls, actor, name, specifications[name])
                       for name in CONTROLS if name in specifications
                       and name.endswith(('hand', 'foot', 'palm')))
        return self.solver.solve(targets)
