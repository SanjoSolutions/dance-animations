"""Pose a selected Rigify hand against a mesh surface on request."""

import json
import math

import bpy
from mathutils import Euler, Matrix, Vector
from mathutils.bvhtree import BVHTree


def retrieve_matrix(values):
    return Matrix([values[index:index + 4] for index in range(0, 16, 4)])


class HandSurface:
    """Snapshot the evaluated target so a snap has a stable surface."""

    def __init__(self, target, graph, rig, side):
        evaluated = target.evaluated_get(graph)
        mesh = evaluated.data
        omitted = set()
        own_body = any(modifier.type == "ARMATURE" and modifier.object
                       and modifier.object.name.startswith(rig.name.split(".")[0] + ".")
                       for modifier in target.modifiers)
        if own_body:
            groups = {group.index for group in target.vertex_groups
                      if group.name.endswith("." + side)
                      and group.name.startswith(("DEF-hand", "DEF-palm", "DEF-f_", "DEF-thumb"))}
            omitted = {vertex.index for vertex in mesh.vertices
                       if sum(weight.weight for weight in vertex.groups if weight.group in groups) > 0.25}
        polygons = [tuple(polygon.vertices) for polygon in mesh.polygons
                    if all(index not in omitted for index in polygon.vertices)]
        if not polygons:
            raise ValueError("Choose a mesh with a surface outside the selected hand")
        self.tree = BVHTree.FromPolygons(
            [evaluated.matrix_world @ vertex.co for vertex in mesh.vertices], polygons,
        )

    def retrieve_nearest(self, point):
        location, normal, _index, _distance = self.tree.find_nearest(point)
        if location is None:
            raise ValueError("Choose a mesh with polygon geometry")
        return location, normal


class PalmPlacement:
    """Fit the palm's support area before resolving the finger joints."""

    # In meters.
    clearance = 0.001

    def __init__(self, surface, previous, samples):
        self.surface = surface
        self.samples = [Vector(sample) for sample in samples]
        location, normal = surface.retrieve_nearest(previous.translation)
        heading = previous.to_3x3().col[1]
        tangent = heading - normal * heading.dot(normal)
        if tangent.length < 1e-6:
            tangent = normal.orthogonal()
        tangent.normalize()
        self.frame = Matrix((tangent.cross(normal), tangent, normal)).transposed().to_4x4()
        self.frame.translation = location + normal * self.clearance

    def retrieve_contacts(self, palm):
        contacts = []
        for sample in self.samples:
            point = palm @ sample
            nearest, normal = self.surface.retrieve_nearest(point)
            contacts.append((point - nearest, normal))
        return contacts

    def retrieve_candidate(self, rotation):
        palm = self.frame @ rotation.to_matrix().to_4x4()
        direction = palm.to_3x3().col[2]
        for _iteration in range(12):
            distances = [(offset.dot(normal) - self.clearance) / max(0.25, direction.dot(normal))
                         for offset, normal in self.retrieve_contacts(palm)]
            correction = min(distances)
            palm.translation -= direction * correction
            if abs(correction) < 0.000001:
                break
        return palm

    def retrieve_cost(self, palm):
        contacts = self.retrieve_contacts(palm)
        penetration = max(0.0, self.clearance - min(offset.dot(normal) for offset, normal in contacts))
        gaps = [max(0.0, offset.length - self.clearance) for offset, _normal in contacts]
        # Every support region contributes, including the heel and both palm edges.
        return 30.0 * penetration + sum(gaps) / len(gaps) + 0.25 * max(gaps)

    def retrieve_pose(self):
        rotation = Euler((0.0, 0.0, 0.0), "XYZ")
        palm = self.retrieve_candidate(rotation)
        cost = self.retrieve_cost(palm)
        for step in (15, 8, 4, 2, 1, 0.5, 0.25):
            for _iteration in range(8):
                improved = False
                for axis in (0, 1):
                    for sign in (-1, 1):
                        candidate_rotation = rotation.copy()
                        candidate_rotation[axis] = min(max(
                            rotation[axis] + sign * math.radians(step), -math.pi / 3), math.pi / 3)
                        candidate = self.retrieve_candidate(candidate_rotation)
                        candidate_cost = self.retrieve_cost(candidate)
                        if candidate_cost < cost - 1e-8:
                            rotation, palm, cost = candidate_rotation, candidate, candidate_cost
                            improved = True
                if not improved:
                    break
        return palm


class FingerComfort:
    """Favor relaxed curl, centered spread, and coordinated fingertip flexion."""

    def __init__(self, calibration, parent_flexion=None):
        self.bounds = calibration["bounds"]
        segment = calibration["segment"]
        rest = retrieve_matrix(calibration["rest"]).to_euler("XYZ").x
        flexion = 0.0
        if segment > 1:
            if calibration["finger"] == "thumb":
                flexion = math.radians(10) - rest
            else:
                preferred = (0.65 * max(0.0, parent_flexion)
                             if segment == 3 and parent_flexion is not None else math.radians(20))
                flexion = preferred - rest
        self.preferred = self.clamp((flexion, 0.0, 0.0))

    def clamp(self, angles):
        return Euler(tuple(min(max(angle, lower), upper)
                           for angle, (lower, upper) in zip(angles, self.bounds)), "XYZ")

    def retrieve_cost(self, angles):
        cost = 0.0
        for angle, preferred, (lower, upper), weight in zip(
                angles, self.preferred, self.bounds, (1.0, 2.0, 6.0)):
            if upper > lower:
                cost += weight * (angle - preferred) ** 2
                extent = upper - preferred if angle >= preferred else preferred - lower
                if extent > 1e-8:
                    effort = abs(angle - preferred) / extent
                    cost += 20.0 * max(0.0, effort - 0.75) ** 2
        return cost


class JointRotationSearch:
    """Refine bounded rotations with individual and coordinated joint steps."""

    def __init__(self, comforts, retrieve_cost, directions=None):
        self.comforts = comforts
        self.retrieve_cost = retrieve_cost
        self.directions = [[(joint, axis, 1)] for joint, comfort in enumerate(comforts)
                           for axis, (lower, upper) in enumerate(comfort.bounds) if upper > lower]
        self.directions.extend(directions or [])

    def refine(self, rotations):
        rotations = [comfort.clamp(rotation) for comfort, rotation in zip(self.comforts, rotations)]
        cost = self.retrieve_cost(rotations)
        for step in (10, 5, 2, 1, 0.5, 0.25):
            for _iteration in range(8):
                improved = False
                for direction in self.directions:
                    for sign in (-1, 1):
                        candidate = [rotation.copy() for rotation in rotations]
                        for joint, axis, factor in direction:
                            candidate[joint][axis] += sign * factor * math.radians(step)
                            candidate[joint] = self.comforts[joint].clamp(candidate[joint])
                        candidate_cost = self.retrieve_cost(candidate)
                        if candidate_cost < cost - 1e-10:
                            rotations, cost = candidate, candidate_cost
                            improved = True
                if not improved:
                    break
        return rotations


class FingerPlacement:
    """Balance surface support and comfortable rotation within joint limits."""

    def __init__(self, surface, frame, palm, calibration, parent_flexion=None):
        self.surface = surface
        self.frame = frame
        self.input = frame.copy()
        self.samples = [Vector(sample) for sample in calibration["samples"]]
        self.bounds = calibration["bounds"]
        self.comfort = FingerComfort(calibration, parent_flexion)
        self.clearance = 0.001
        if calibration["segment"] == 1:
            nearest, _normal = surface.retrieve_nearest(frame @ self.samples[0])
            relative = frame.inverted() @ nearest
            spread = min(max(math.atan2(-relative.x, relative.y), -math.pi / 4), math.pi / 4)
            self.input = frame @ Matrix.Rotation(spread, 4, "Z")
            if calibration["finger"] == "thumb":
                normal = self.input.to_3x3().inverted() @ -palm.to_3x3().col[2]
                self.input = self.input @ Matrix.Rotation(math.atan2(normal.x, normal.z), 4, "Y")
        self.inverse = self.input.inverted()

    def retrieve_projection(self, sample):
        point = sample.copy()
        for _iteration in range(16):
            nearest, normal = self.surface.retrieve_nearest(self.input @ point)
            projected = self.inverse @ (nearest + normal * self.clearance)
            projected.x = sample.x
            if projected.length > 1e-10:
                projected *= sample.length / projected.length
            change = (projected - point).length
            point = projected
            if change < 0.000001:
                break
        return point

    def retrieve_candidate(self, sample):
        point = self.retrieve_projection(sample)
        angle = math.atan2(point.z, point.y) - math.atan2(sample.z, sample.y)
        rotation = (self.frame.inverted() @ self.input @ Matrix.Rotation(angle, 4, "X")).to_euler("XYZ")
        return self.comfort.clamp(rotation)

    def retrieve_cost(self, rotation):
        candidate = self.frame @ rotation.to_matrix().to_4x4()
        distances = []
        for pad in self.samples:
            point = candidate @ pad
            nearest, normal = self.surface.retrieve_nearest(point)
            distances.append((point - nearest).dot(normal) - self.clearance)
        penetration = max(0.0, -min(distances))
        gap = max(0.0, min(distances[:4]) - 0.0005)
        # Contact inside this small tolerance allows the joints to relax.
        return 30.0 * penetration + gap + 0.0005 * self.comfort.retrieve_cost(rotation)

    def retrieve_pose(self):
        candidates = [self.retrieve_candidate(sample) for sample in self.samples]
        candidates.append(self.comfort.preferred)
        seeds = sorted(candidates, key=self.retrieve_cost)[:3]
        search = JointRotationSearch([self.comfort], lambda rotations: self.retrieve_cost(rotations[0]))
        rotations = [search.refine([seed])[0] for seed in seeds]
        rotation = min(rotations, key=self.retrieve_cost)
        return self.frame @ rotation.to_matrix().to_4x4()


class FingerChainPlacement:
    """Relax all three joints together while preserving their surface support."""

    def __init__(self, surface, frame, calibrations, rotations):
        self.surface = surface
        self.frame = frame
        self.calibrations = calibrations
        self.rests = [retrieve_matrix(calibration["rest"]) for calibration in calibrations]
        self.rotations = rotations
        self.samples = []
        for calibration in calibrations:
            pads = [Vector(sample) for sample in calibration["samples"][:4]]
            self.samples.append([first.lerp(second, fraction / 4)
                                 for first, second in zip(pads, pads[1:]) for fraction in range(4)] + pads[-1:])

    def retrieve_poses(self, rotations):
        poses = []
        for index, rotation in enumerate(rotations):
            frame = poses[-1] @ self.rests[index] if poses else self.frame
            poses.append(frame @ rotation.to_matrix().to_4x4())
        return poses

    def retrieve_cost(self, rotations):
        cost = 0.0
        parent_flexion = None
        for index, (pose, rotation, calibration) in enumerate(zip(
                self.retrieve_poses(rotations), rotations, self.calibrations)):
            distances = []
            for sample in self.samples[index]:
                point = pose @ sample
                nearest, normal = self.surface.retrieve_nearest(point)
                distances.append((point - nearest).dot(normal) - 0.001)
            cost += 30.0 * max(0.0, -min(distances)) + 3.0 * max(0.0, min(distances) - 0.0005)
            comfort = FingerComfort(calibration, parent_flexion)
            cost += 0.001 * comfort.retrieve_cost(rotation)
            parent_flexion = (self.rests[index].to_3x3() @ rotation.to_matrix()).to_euler("XYZ").x
        return cost

    def retrieve_pose(self):
        comforts = [FingerComfort(calibration) for calibration in self.calibrations]
        # Paired bends let contact move between joints along a curved surface.
        directions = [[(joint, 0, 1), (joint + 1, 0, -ratio)]
                      for joint in (0, 1) for ratio in (1, 2)]
        search = JointRotationSearch(comforts, self.retrieve_cost, directions)
        candidates = [search.refine(seed) for seed in (
            self.rotations, [comfort.preferred for comfort in comforts])]
        rotations = min(candidates, key=self.retrieve_cost)
        return self.retrieve_poses(rotations)


class HandSnap:
    calibration_property = "Snap Hand Calibration"

    def __init__(self, context, rig, side):
        self.context = context
        self.rig = rig
        self.side = side
        self.hand = rig.pose.bones[f"hand_ik.{side}"]
        self.calibration = json.loads(self.hand[self.calibration_property])
        self.wrist = retrieve_matrix(self.calibration["wrist"])

    def retrieve_hand_pose(self):
        graph = self.context.evaluated_depsgraph_get()
        evaluated = self.rig.evaluated_get(graph)
        return evaluated.matrix_world @ evaluated.pose.bones[f"DEF-hand.{self.side}"].matrix

    def retrieve_palm_pose(self, surface):
        previous = self.retrieve_hand_pose() @ self.wrist.inverted()
        return PalmPlacement(surface, previous, self.calibration["support"]).retrieve_pose()

    def place_wrist(self, desired):
        for _iteration in range(16):
            current = self.retrieve_hand_pose()
            if ((current.translation - desired.translation).length < 0.00001
                    and current.to_quaternion().rotation_difference(desired.to_quaternion()).angle < 0.0001):
                break
            graph = self.context.evaluated_depsgraph_get()
            control = self.rig.evaluated_get(graph).pose.bones[self.hand.name]
            world = desired @ current.inverted() @ self.rig.matrix_world @ control.matrix
            self.hand.matrix = self.rig.matrix_world.inverted() @ world
            self.rig.update_tag()
            self.context.view_layer.update()

    def fit_fingers(self, surface, palm):
        flexions = {}
        fingers = sorted(self.calibration["fingers"].items(), key=lambda item: item[1]["segment"])
        for name, calibration in fingers:
            graph = self.context.evaluated_depsgraph_get()
            evaluated = self.rig.evaluated_get(graph)
            frame = (evaluated.matrix_world @ evaluated.pose.bones[calibration["parent"]].matrix
                     @ retrieve_matrix(calibration["rest"]))
            pose = FingerPlacement(surface, frame, palm, calibration,
                                   flexions.get(calibration["finger"])).retrieve_pose()
            self.rig.pose.bones[name].matrix = self.rig.matrix_world.inverted() @ pose
            self.rig.update_tag()
            self.context.view_layer.update()
            evaluated = self.rig.evaluated_get(self.context.evaluated_depsgraph_get())
            joint = evaluated.pose.bones[calibration["parent"]].matrix.inverted() @ evaluated.pose.bones[name].matrix
            flexions[calibration["finger"]] = joint.to_euler("XYZ").x
        for finger in dict.fromkeys(calibration["finger"] for _name, calibration in fingers):
            chain = [(name, calibration) for name, calibration in fingers if calibration["finger"] == finger]
            evaluated = self.rig.evaluated_get(self.context.evaluated_depsgraph_get())
            frames = [evaluated.matrix_world @ evaluated.pose.bones[calibration["parent"]].matrix
                      @ retrieve_matrix(calibration["rest"]) for _name, calibration in chain]
            rotations = [(frame.inverted() @ evaluated.matrix_world @ evaluated.pose.bones[name].matrix).to_euler("XYZ")
                         for frame, (name, _calibration) in zip(frames, chain)]
            placement = FingerChainPlacement(surface, frames[0], [calibration for _name, calibration in chain], rotations)
            for (name, _calibration), pose in zip(chain, placement.retrieve_pose()):
                self.rig.pose.bones[name].matrix = self.rig.matrix_world.inverted() @ pose
                self.rig.update_tag()
                self.context.view_layer.update()

    def snap(self, target, keyframe=False):
        if target is None or target.type != "MESH":
            raise ValueError("Choose the hand's target mesh in the Snap Hand panel")
        surface = HandSurface(target, self.context.evaluated_depsgraph_get(), self.rig, self.side)
        poses = {bone.name: bone.matrix_basis.copy() for bone in self.rig.pose.bones
                 if bone.name == self.hand.name or bone.name in self.calibration["fingers"]}
        parent = self.rig.pose.bones[f"upper_arm_parent.{self.side}"]
        previous_blend = parent["IK_FK"]
        try:
            parent["IK_FK"] = 0.0
            self.rig.update_tag()
            self.context.view_layer.update()
            palm = self.retrieve_palm_pose(surface)
            self.place_wrist(palm @ self.wrist)
            self.fit_fingers(surface, palm)
            if keyframe:
                parent.keyframe_insert('["IK_FK"]', group=parent.name)
                for name in poses:
                    bone = self.rig.pose.bones[name]
                    rotation = "rotation_quaternion" if bone.rotation_mode == "QUATERNION" else "rotation_axis_angle" if bone.rotation_mode == "AXIS_ANGLE" else "rotation_euler"
                    for path in ("location", rotation, "scale"):
                        bone.keyframe_insert(path, group=name)
        except Exception:
            for name, pose in poses.items():
                self.rig.pose.bones[name].matrix_basis = pose
            parent["IK_FK"] = previous_blend
            self.rig.update_tag()
            self.context.view_layer.update()
            raise
        return self.hand


def retrieve_selected_hand(context):
    rig = context.object
    bone = context.active_pose_bone
    if rig and rig.type == "ARMATURE" and context.mode == "POSE" and bone:
        side = bone.name.rsplit(".", 1)[-1]
        hand = rig.pose.bones.get(f"hand_ik.{side}")
        if bone.name.startswith(("hand_", "f_index", "f_middle", "f_ring", "f_pinky", "thumb", "palm")) and hand and HandSnap.calibration_property in hand:
            return rig, side
    return None


class HAND_OT_snap(bpy.types.Operator):
    bl_idname = "hand.snap"
    bl_label = "Snap Hand"
    bl_description = "Fit the selected hand's palm and fingers to its surface and update the IK control"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return retrieve_selected_hand(context) is not None

    def execute(self, context):
        rig, side = retrieve_selected_hand(context)
        hand = rig.pose.bones[f"hand_ik.{side}"]
        try:
            HandSnap(context, rig, side).snap(hand.snap_hand_surface, context.scene.tool_settings.use_keyframe_insert_auto)
        except (ValueError, RuntimeError) as error:
            self.report({"ERROR"}, str(error))
            return {"CANCELLED"}
        self.report({"INFO"}, f"Snapped {rig.name} hand {side}")
        return {"FINISHED"}


class HAND_PT_snap(bpy.types.Panel):
    bl_label = "Snap Hand"
    bl_idname = "HAND_PT_snap"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Item"

    @classmethod
    def poll(cls, context):
        return bool(context.scene.get("Snap Hand Version", 0))

    def draw(self, context):
        selected = retrieve_selected_hand(context)
        if selected:
            rig, side = selected
            self.layout.prop(rig.pose.bones[f"hand_ik.{side}"], "snap_hand_surface", text="Surface")
            self.layout.operator("hand.snap")
        else:
            self.layout.label(text="Select a hand IK or finger control")


def register():
    if not hasattr(bpy.types.PoseBone, "snap_hand_surface"):
        bpy.types.PoseBone.snap_hand_surface = bpy.props.PointerProperty(
            name="Surface", type=bpy.types.Object, poll=lambda _bone, obj: obj.type == "MESH",
        )
    for cls in (HAND_OT_snap, HAND_PT_snap):
        previous = getattr(bpy.types, cls.__name__, None)
        if previous:
            bpy.utils.unregister_class(previous)
        bpy.utils.register_class(cls)


register()
