"""World-space targets for the scene's existing Rigify controls and IK solvers."""

import math
import json
from dataclasses import dataclass

from mathutils import Matrix, Quaternion, Vector


@dataclass(frozen=True)
class Control:
    bone: str
    endpoint: str
    parent: str = ""


CONTROLS = {name: Control(name, name) for name in ("root", "torso", "hips", "chest", "neck", "head")}
for side, suffix in (("left", "L"), ("right", "R")):
    for limb, parent in (("hand", "upper_arm"), ("foot", "thigh")):
        CONTROLS[f"{side}_{limb}"] = Control(f"{limb}_ik.{suffix}", f"DEF-{limb}.{suffix}", f"{parent}_parent.{suffix}")
    CONTROLS[f"{side}_palm"] = CONTROLS[f"{side}_hand"]
    for joint, parent in (("elbow", "upper_arm"), ("knee", "thigh")):
        name = f"{parent}_ik_target.{suffix}"
        CONTROLS[f"{side}_{joint}"] = Control(name, name, f"{parent}_parent.{suffix}")


def vector(value, length, label):
    if (not isinstance(value, (list, tuple)) or len(value) != length
            or any(isinstance(item, bool) or not isinstance(item, (float, int)) or not math.isfinite(item)
                   for item in value)):
        raise ValueError(f"{label} requires {length} finite numbers")
    return Vector(value)


class RigControls:
    def __init__(self, context, rigs):
        self.context = context
        self.rigs = rigs

    def retrieve(self, actor, name):
        if actor not in self.rigs or name not in CONTROLS:
            raise ValueError(f"Choose a listed actor and control: {actor}.{name}")
        rig, control = self.rigs[actor], CONTROLS[name]
        for bone in (control.bone, control.endpoint, control.parent):
            if bone and bone not in rig.pose.bones:
                raise ValueError(f"Configure {rig.name}: {bone}")
        if name.endswith("palm") and "Snap Hand Calibration" not in rig.pose.bones[control.bone]:
            raise ValueError(f"Configure Snap Hand calibration for {actor}.{name}")
        return rig, control

    def retrieve_matrix(self, actor, name):
        rig, control = self.retrieve(actor, name)
        endpoint_rig = self.context.scene.objects[rig.name + '_deform'] if name.endswith(('foot', 'hand', 'palm')) else rig
        evaluated = endpoint_rig.evaluated_get(self.context.evaluated_depsgraph_get())
        matrix = evaluated.matrix_world @ evaluated.pose.bones[control.endpoint].matrix
        if name.endswith("palm"):
            values = json.loads(rig.pose.bones[control.bone]["Snap Hand Calibration"])["wrist"]
            wrist = Matrix([values[index:index + 4] for index in range(0, 16, 4)])
            matrix = matrix @ wrist.inverted()
        return matrix

    def update(self):
        for rig in self.rigs.values():
            rig.update_tag()
            self.context.scene.objects[rig.name + '_deform'].update_tag()
        self.context.view_layer.update()


class PoseTarget:
    """Positions use world units; rotations use world-space (w, x, y, z)."""

    def __init__(self, controls, actor, name, specification):
        self.controls, self.actor, self.name = controls, actor, name
        self.rig, self.control = controls.retrieve(actor, name)
        if not isinstance(specification, dict) or not specification or set(specification) - {"position", "rotation"}:
            raise ValueError(f"{actor}.{name} accepts position and rotation")
        self.position = specification.get("position")
        self.reference = None
        if isinstance(self.position, dict):
            if set(self.position) - {"actor", "control", "offset"} or not {"actor", "control"} <= self.position.keys():
                raise ValueError("Relative positions require actor, control, and an optional local offset")
            self.reference = (self.position["actor"], self.position["control"])
            controls.retrieve(*self.reference)
            self.position = vector(self.position.get("offset", [0, 0, 0]), 3, "Offset")
        elif self.position is not None:
            self.position = vector(self.position, 3, "Position")
        self.rotation = specification.get("rotation")
        if self.rotation is not None:
            values = vector(self.rotation, 4, "Rotation")
            if values.length < 1e-8:
                raise ValueError("Rotation requires a quaternion with positive length")
            self.rotation = Quaternion(values).normalized()
        if self.position is None and self.rotation is None:
            raise ValueError("Supply a position or rotation")
        bone = self.rig.pose.bones[self.control.bone]
        if self.position is not None and (bone.bone.use_connect or any(bone.lock_location)):
            raise ValueError(f"Choose a movable control for {actor}.{name}")
        if self.rotation is not None and (any(bone.lock_rotation) or
                (bone.rotation_mode in {"QUATERNION", "AXIS_ANGLE"} and bone.lock_rotations_4d and bone.lock_rotation_w)):
            raise ValueError(f"Choose a rotatable control for {actor}.{name}")

    def retrieve_position(self):
        return (self.controls.retrieve_matrix(*self.reference) @ self.position
                if self.reference else self.position)

    def measure(self):
        matrix = self.controls.retrieve_matrix(self.actor, self.name)
        position = self.retrieve_position()
        angle = matrix.to_quaternion().rotation_difference(self.rotation).angle if self.rotation else 0.0
        return {
            "actor": self.actor, "control": self.name,
            "distance": (matrix.translation - position).length if position is not None else 0.0,
            "angle": min(angle, abs(math.tau - angle)),
        }

    def move(self):
        current = self.controls.retrieve_matrix(self.actor, self.name)
        destination = current.copy()
        if self.rotation is not None:
            destination = Matrix.LocRotScale(current.translation, self.rotation, current.to_scale())
        position = self.retrieve_position()
        if position is not None:
            destination.translation = position
        bone = self.rig.pose.bones[self.control.bone]
        evaluated = self.rig.evaluated_get(self.controls.context.evaluated_depsgraph_get())
        control_world = evaluated.matrix_world @ evaluated.pose.bones[bone.name].matrix
        desired = destination @ current.inverted() @ control_world
        bone.matrix = self.rig.matrix_world.inverted() @ desired


class PoseSnapshot:
    def __init__(self, controls):
        self.controls = controls
        self.values = [(bone, bone.location.copy(), bone.rotation_quaternion.copy(),
                        bone.rotation_euler.copy(), tuple(bone.rotation_axis_angle), bone.scale.copy(),
                        {key: value for key, value in bone.items() if isinstance(value, (bool, int, float))})
                       for rig in controls.rigs.values() for bone in rig.pose.bones]

    def restore(self):
        for bone, location, quaternion, euler, axis_angle, scale, properties in self.values:
            bone.location, bone.rotation_quaternion, bone.rotation_euler = location, quaternion, euler
            bone.rotation_axis_angle, bone.scale = axis_angle, scale
            for key, value in properties.items():
                bone[key] = value
        self.controls.update()

    def align_rotations(self, bones):
        for bone, _location, quaternion, euler, _axis_angle, _scale, _properties in self.values:
            if bone in bones:
                if bone.rotation_mode == "QUATERNION":
                    # Quaternion continuity needs a hemisphere choice. Preserve
                    # the solved rotation directly, including near-identity poses.
                    if bone.rotation_quaternion.dot(quaternion) < 0:
                        bone.rotation_quaternion.negate()
                elif bone.rotation_mode != "AXIS_ANGLE":
                    bone.rotation_euler.make_compatible(euler)


class PoseSolver:
    def __init__(self, controls, tolerance=0.002, angular_tolerance=0.03, iterations=12):
        self.controls = controls
        self.tolerance, self.angular_tolerance, self.iterations = tolerance, angular_tolerance, iterations

    def solve(self, targets):
        snapshot = PoseSnapshot(self.controls)
        keyed = set()
        try:
            for target in targets:
                control = target.control
                if control.parent:
                    parent = target.rig.pose.bones[control.parent]
                    properties = {"IK_FK": 0.0, "IK_Stretch": 0.0}
                    if target.name.endswith(("elbow", "knee")):
                        properties["pole_vector"] = True
                    for name, value in properties.items():
                        if name in parent and parent[name] != value:
                            parent[name] = value
                            keyed.add((parent, '["' + name + '"]'))
            self.controls.update()
            for _ in range(self.iterations):
                # Parent controls precede limbs, and relative targets follow their anchors.
                for target in targets:
                    if not self.accepts([target.measure()]):
                        target.move()
                        self.controls.update()
                measurements = [target.measure() for target in targets]
                if self.accepts(measurements):
                    break
            if not self.accepts(measurements):
                details = "; ".join(f"{item['actor']}.{item['control']}: distance={item['distance']:.5f}, angle={item['angle']:.4f}"
                                    for item in measurements if item["distance"] > self.tolerance or item["angle"] > self.angular_tolerance)
                raise ValueError("Pose exceeds reach or constraint limits; adjust torso, target, or pole. " + details)
            for target in targets:
                bone = target.rig.pose.bones[target.control.bone]
                rotation = {"QUATERNION": "rotation_quaternion", "AXIS_ANGLE": "rotation_axis_angle"}.get(bone.rotation_mode, "rotation_euler")
                # Endpoint corrections can change both channels even for a position-only request.
                keyed.update((bone, path) for path in ("location", rotation))
            snapshot.align_rotations({bone for bone, path in keyed})
        except Exception:
            snapshot.restore()
            raise
        return keyed, measurements

    def accepts(self, measurements):
        return all(item["distance"] <= self.tolerance and item["angle"] <= self.angular_tolerance for item in measurements)
