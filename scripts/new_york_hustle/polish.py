"""Author Hustle hand contacts on native controls, then bake their saved sources.

Blender 5.2 --background --factory-startup --python-exit-code 1
--python scripts/new_york_hustle/polish.py -- CLIP_ID ...
An empty clip list selects the New York Hustle repertoire.
"""

import hashlib
import json
from pathlib import Path
import sys

import bpy
from mathutils import Euler, Matrix, Vector

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import dance_tools
from snap_hand import HandSnap, retrieve_matrix


class BoneKeys:
    def __init__(self, frame, rotations):
        self.frame = frame
        self.rotations = rotations
        self.current_rotations = {}

    def store(self, bone, properties=None):
        rotation = "rotation_quaternion" if bone.rotation_mode == "QUATERNION" else "rotation_euler"
        if rotation == "rotation_quaternion":
            name = bone.id_data.name, bone.name
            previous = self.rotations.get(name)
            if previous and bone.rotation_quaternion.dot(previous) < 0:
                bone.rotation_quaternion.negate()
            self.current_rotations[name] = bone.rotation_quaternion.copy()
        for prop in properties or ("location", rotation, "scale"):
            bone.keyframe_insert(prop, frame=self.frame, group=bone.name)

    @staticmethod
    def evaluate(bone):
        bone.id_data.update_tag()
        bpy.context.view_layer.update()


class GripTiming:
    def __init__(self, name):
        self.move = name.removeprefix("new_york_hustle_")

    @staticmethod
    def blend(frame, start, end):
        fraction = min(1.0, max(0.0, (frame - start) / (end - start)))
        return fraction * fraction * (3 - 2 * fraction)

    def retrieve_contacts(self, frame):
        move = self.move
        if move in {"position_left_hand", "position_right_hand"}:
            side = "L" if "left" in move else "R"
            return [(side, side, 1.0, False)]
        elif move in {"position_shadow", "position_cuddle"}:
            return [("L", "L", 1.0, True), ("R", "R", 1.0, True)]
        elif move == "position_counter_promenade":
            return [("R", "L", 1.0, True)]
        elif move in {"position_side_by_side", "position_promenade"}:
            return [("L", "R", 1.0, True)]
        elif move in {"side_by_side_entry_exit", "promenade_entry_exit"}:
            facing = self.blend(frame, 24, 48) * (1 - self.blend(frame, 90, 120))
            return [("L", "R", 1.0, facing)]
        elif move in {"basic_double", "position_double", "wheel_left", "wheel_right"}:
            return [("L", "R", 1.0, False), ("R", "L", 1.0, False)]
        elif move in {"shadow_entry_exit", "cuddle_entry_exit", "counter_promenade_entry_exit"}:
            entering = self.blend(frame, 24, 48)
            leaving = self.blend(frame, 90, 120)
            weight = entering * (1 - leaving)
            pairs = [("R", "L", weight, True)] if move.startswith("counter") else [
                ("L", "L", weight, True), ("R", "R", weight, True)]
            return [("L", "R", 1 - weight, False), *pairs]
        elif ("free_spin" in move or move in {"left_side_pass", "right_side_pass", "inside_turn_pass", "outside_turn_pass"}
              or (move == "combination" and frame >= 144)):
            phase = frame - 144 if move == "combination" else frame
            weight = 1 - self.blend(phase, 18, 30) + self.blend(phase, 114, 126)
            return [("L", "R", weight, False)]
        else:
            return [("L", "R", 1.0, False)]

    def retrieve_lift(self, frame):
        turn = ("underarm" in self.move or "double_turn" in self.move
                or self.move in {"alternating_turns", "combination"})
        if turn:
            if self.move == "combination" and frame > 144:
                return 0.0
            approach, rise = (6, 18) if self.move == "alternating_turns" else (18, 36)
            return self.blend(frame, approach, rise) * (1 - self.blend(frame, 108, 126))
        else:
            return 0.0

    def retrieve_turner(self, frame):
        return "Man" if "leader_underarm" in self.move or (self.move == "alternating_turns" and frame > 72) else "Woman"

    def follows_elbow(self, actor, side):
        return actor == "Woman" and side == "R" and self.move in {"follower_double_turn", "inside_turn_pass"}


class HandPose:
    def __init__(self, rig, side, keys):
        self.rig, self.side, self.keys = rig, side, keys
        self.snap = HandSnap(bpy.context, rig, side)

    def prepare(self, previous):
        hand = self.rig.pose.bones["hand_ik." + self.side]
        hand.matrix = previous
        self.keys.store(hand)
        tweak = self.rig.pose.bones["hand_tweak." + self.side]
        tweak.matrix_basis = Matrix.Identity(4)
        self.keys.store(tweak)
        for finger in ("f_index", "f_middle", "f_ring", "f_pinky", "thumb"):
            master = self.rig.pose.bones[f"{finger}.01_master.{self.side}"]
            master.matrix_basis = Matrix.Identity(4)
            self.keys.store(master)
        self.keys.evaluate(hand)

    def retrieve_palm(self):
        return self.snap.retrieve_hand_pose() @ self.snap.wrist.inverted()

    def place_elbow(self, lift):
        spine = self.rig.pose.bones["ORG-spine"]
        heading = spine.matrix.to_3x3() @ spine.bone.matrix_local.to_3x3().inverted()
        shoulder = self.rig.pose.bones["ORG-upper_arm." + self.side].head
        lateral = 0.45 if self.side == "L" else -0.45
        offset = heading @ Vector((lateral, 0.3, -0.15 + 0.3 * lift))
        pole = self.rig.pose.bones["upper_arm_ik_target." + self.side]
        pose = pole.matrix.copy()
        pose.translation = shoulder + offset
        pole.matrix = pose
        self.keys.store(pole, ("location",))
        self.keys.evaluate(pole)

    def place(self, center, weight):
        previous = self.retrieve_palm()
        position = previous.translation.lerp(center, weight)
        target = previous.to_quaternion().to_matrix().to_4x4()
        target.translation = position
        self.snap.hand.matrix = self.rig.matrix_world.inverted() @ target @ self.snap.wrist
        self.keys.store(self.snap.hand)
        self.keys.evaluate(self.snap.hand)
        self.place_position(position)

    def place_position(self, position):
        # Translation remains available as the native wrist limit resolves rotation.
        for _iteration in range(24):
            offset = position - self.retrieve_palm().translation
            if offset.length < 0.00001:
                break
            control = self.snap.hand.matrix.copy()
            control.translation += self.rig.matrix_world.to_3x3().inverted() @ offset
            self.snap.hand.matrix = control
            self.keys.store(self.snap.hand, ("location",))
            self.keys.evaluate(self.snap.hand)

    def follow_forearm(self):
        position = self.retrieve_palm().translation
        wrist = self.rig.pose.bones["hand_tweak." + self.side]
        reference = wrist.constraints["Natural Wrist Rotation"].space_object
        for _iteration in range(12):
            graph = bpy.context.evaluated_depsgraph_get()
            orientation = reference.evaluated_get(graph).matrix_world.to_quaternion()
            control = (self.rig.matrix_world.inverted().to_quaternion() @ orientation).to_matrix().to_4x4()
            control.translation = self.snap.hand.matrix.translation
            self.snap.hand.matrix = control
            self.keys.store(self.snap.hand)
            self.keys.evaluate(self.snap.hand)
            self.place_position(position)

    def curl(self, contact):
        joints = self.snap.calibration["fingers"]
        for segment in range(3):
            for name, calibration in joints.items():
                if calibration["segment"] == segment + 1:
                    self.curl_joint(name, calibration, segment, contact)
            self.keys.evaluate(self.snap.hand)

    def curl_joint(self, name, calibration, segment, contact):
        thumb = calibration["finger"] == "thumb"
        relaxed = (0.12, 0.22, 0.15)
        cupped = (0.30, 0.65, 0.32)
        angle = (0.12, 0.25, 0.17)[segment] if thumb else relaxed[segment] + contact * (cupped[segment] - relaxed[segment])
        opposition = (0.18 if self.side == "R" else -0.18) if thumb and segment == 0 else 0.0
        rotation = Euler((angle, opposition, 0.0), "XYZ")
        for axis, (minimum, maximum) in enumerate(calibration["bounds"]):
            rotation[axis] = min(maximum, max(minimum, rotation[axis]))
        parent = self.rig.pose.bones[calibration["parent"]]
        self.rig.pose.bones[name].matrix = (parent.matrix @ retrieve_matrix(calibration["rest"])
                                           @ rotation.to_matrix().to_4x4())
        self.keys.store(self.rig.pose.bones[name])


class HustlePolish:
    def __init__(self, action):
        self.action = action
        self.scene = bpy.context.scene
        self.rigs = {actor: self.scene.objects[actor + ".rigify"] for actor in ("Man", "Woman")}
        self.timing = GripTiming(action.name)
        for rig in self.rigs.values():
            rig.animation_data.action = action
            rig.animation_data.action_slot = next(slot for slot in action.slots if slot.identifier == "OB" + rig.name)
            rig.animation_data.use_nla = False

    def retrieve_samples(self):
        saved = self.action.get("Hustle Original Hand Samples")
        if saved:
            return [(sample["frame"], {
                actor: {side: retrieve_matrix(values) for side, values in sides.items()}
                for actor, sides in sample["hands"].items()}) for sample in json.loads(saved)]
        frames = sorted({float(key.co.x) for layer in self.action.layers for strip in layer.strips
                         for bag in strip.channelbags for curve in bag.fcurves
                         if "hand_ik." in curve.data_path for key in curve.keyframe_points})
        samples = []
        for frame in frames:
            self.scene.frame_set(int(frame), subframe=frame % 1)
            samples.append((frame, {
                actor: {side: rig.pose.bones["hand_ik." + side].matrix.copy() for side in "LR"}
                for actor, rig in self.rigs.items()}))
        return samples

    def author(self):
        samples = self.retrieve_samples()
        self.action["Hustle Original Hand Samples"] = json.dumps([
            {"frame": frame, "hands": {actor: {side: [value for row in pose for value in row]
                for side, pose in sides.items()} for actor, sides in previous.items()}}
            for frame, previous in samples])
        samples = self.refine_samples(samples)
        for layer in self.action.layers:
            for strip in layer.strips:
                for bag in strip.channelbags:
                    for curve in list(bag.fcurves):
                        if (curve.data_path.startswith(tuple('pose.bones["' + finger for finger in
                                ("f_index.", "f_middle.", "f_ring.", "f_pinky.", "thumb.")))
                                and curve.data_path.endswith("rotation_euler")
                                and "master" not in curve.data_path):
                            bag.fcurves.remove(curve)
        contact_errors = []
        rotations = {}
        for frame, previous in samples:
            self.scene.frame_set(int(frame), subframe=frame % 1)
            keys = BoneKeys(frame, rotations)
            poses = {(actor, side): HandPose(rig, side, keys) for actor, rig in self.rigs.items() for side in "LR"}
            for (actor, side), pose in poses.items():
                pose.prepare(previous[actor][side])
                if self.timing.follows_elbow(actor, side):
                    pose.place_elbow(self.timing.retrieve_lift(frame))
            curls = {pair: 0.0 for pair in poses}
            lift = self.timing.retrieve_lift(frame)
            for leader_side, follower_side, weight, same_heading in self.timing.retrieve_contacts(frame):
                if weight > 0:
                    leader, follower = poses["Man", leader_side], poses["Woman", follower_side]
                    man_wrist = self.rigs["Man"].matrix_world @ previous["Man"][leader_side].translation
                    woman_wrist = self.rigs["Woman"].matrix_world @ previous["Woman"][follower_side].translation
                    center = (man_wrist + woman_wrist) / 2
                    if same_heading:
                        palms = (leader.retrieve_palm().translation + follower.retrieve_palm().translation) / 2
                        center = center.lerp(palms, float(same_heading))
                    if lift > 0:
                        turner = self.rigs[self.timing.retrieve_turner(frame)]
                        head = turner.matrix_world @ turner.pose.bones["head"].matrix.translation
                        partner = self.rigs["Woman" if turner == self.rigs["Man"] else "Man"]
                        partner_head = partner.matrix_world @ partner.pose.bones["head"].matrix.translation
                        head = head.lerp(partner_head, 0.22)
                        head.z = max(rig.pose.bones["head"].head.z for rig in self.rigs.values()) + 0.22
                        center = center.lerp(head, lift)
                    normal = Vector((0, 0, -1))
                    for pose, sign in ((leader, 1), (follower, -1)):
                        pose.place(center + normal * (0.002 * sign), weight)
                        curls[pose.rig.name.split(".")[0], pose.side] = max(curls[pose.rig.name.split(".")[0], pose.side], weight)
                    if weight == 1:
                        for _iteration in range(8):
                            gap = (leader.retrieve_palm().translation - follower.retrieve_palm().translation).length
                            if gap < 0.008:
                                break
                            reachable = (leader.retrieve_palm().translation + follower.retrieve_palm().translation) / 2
                            leader.place_position(reachable + normal * 0.002)
                            follower.place_position(reachable - normal * 0.002)
                        contact_errors.append((leader.retrieve_palm().translation - follower.retrieve_palm().translation).length)
            for pair, pose in poses.items():
                if self.timing.follows_elbow(*pair):
                    pose.follow_forearm()
                pose.curl(curls[pair])
            rotations.update(keys.current_rotations)
        self.action["Contact Style"] = "Calibrated cupped grips; relaxed releases; native wrist and finger limits"
        self.action["Hustle Hand Polish"] = 4
        self.action["Hustle Study Status"] = "Procedural study; local hand-contact review"
        self.action["Hustle Grip Timing"] = json.dumps([
            {"frame": frame, "contacts": self.timing.retrieve_contacts(frame), "lift": self.timing.retrieve_lift(frame)}
            for frame, _previous in samples])
        controls = tuple('pose.bones["' + prefix for prefix in
                         ("hand_ik.", "hand_tweak.", "upper_arm_ik_target.", "f_index.", "f_middle.", "f_ring.", "f_pinky.", "thumb."))
        for layer in self.action.layers:
            for strip in layer.strips:
                for bag in strip.channelbags:
                    for curve in bag.fcurves:
                        if curve.data_path.startswith(controls):
                            for key in curve.keyframe_points:
                                key.interpolation = "LINEAR"
                            curve.update()
        if max(contact_errors, default=0.0) > 0.012:
            raise ValueError(f"Resolve the authored hand contact for {self.action.name}: {max(contact_errors):.4f}")
        return {"id": self.action.name, "authoredFrames": len(samples),
                "handPolishVersion": 4,
                "maximumAuthoredPalmGap": max(contact_errors, default=0.0)}

    def refine_samples(self, samples):
        frames = {frame for frame, _previous in samples}
        if any(self.timing.retrieve_lift(frame) > 0 for frame in frames):
            frames.update(range(18, 37))
            frames.update(range(108, 127))
            interval = 2 if self.timing.move in {"follower_double_turn", "alternating_turns"} else 3
            frames.update(range(36, 109, interval))
            if self.timing.move == "alternating_turns":
                frames.update(range(6, 19))
        if self.timing.move == "inside_turn_pass":
            frames.update(range(18, 31))
            frames.update(range(114, 133))
        if self.timing.move in {"inside_turn_pass", "follower_double_turn"}:
            frames.update(range(int(samples[0][0]), int(samples[-1][0]) + 1))
        result = []
        for frame in sorted(frames):
            lower = max(sample for sample in samples if sample[0] <= frame)
            upper = min(sample for sample in samples if sample[0] >= frame)
            fraction = (frame - lower[0]) / (upper[0] - lower[0]) if upper[0] > lower[0] else 0
            hands = {}
            for actor, sides in lower[1].items():
                hands[actor] = {}
                for side, pose in sides.items():
                    first = pose.decompose()
                    last = upper[1][actor][side].decompose()
                    hands[actor][side] = Matrix.LocRotScale(first[0].lerp(last[0], fraction),
                        first[1].slerp(last[1], fraction), first[2].lerp(last[2], fraction))
            result.append((frame, hands))
        return result


def main():
    requested = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    deferred = "--defer-catalog" in requested
    requested = [name for name in requested if name != "--defer-catalog"]
    catalog_path = ROOT / "catalog.json"
    catalog = json.loads(catalog_path.read_text())
    records = [entry for entry in catalog["animations"] if entry["style"] == "new_york_hustle"
               and (entry["id"] in requested or not requested)]
    evidence = ROOT / ".cache/hustle-polish"
    evidence.mkdir(parents=True, exist_ok=True)
    for record in records:
        source = ROOT / record["sourceFile"]
        original_hash = hashlib.sha256(source.read_bytes()).hexdigest()
        bpy.ops.wm.open_mainfile(filepath=str(source))
        dance_tools.register()
        action = bpy.data.actions[record["id"]]
        from animation_export_evaluation import AnimationExportEvaluation
        evaluation = AnimationExportEvaluation(set(bpy.context.scene.objects[name + ".rigify"] for name in ("Man", "Woman")))
        evaluation.prepare()
        try:
            report = HustlePolish(action).author()
        finally:
            evaluation.restore()
        report["previousSourceSha256"] = original_hash
        destination = dance_tools.export_action(action, update_catalog=not deferred)
        report["sourceSha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
        from import_assets import read_glb
        document, _binary = read_glb(destination)
        report["animationName"] = document["animations"][0]["name"]
        report["duration"] = max(document["accessors"][sampler["input"]]["max"][0]
                                 for sampler in document["animations"][0]["samplers"])
        if not deferred:
            catalog = json.loads(catalog_path.read_text())
            updated = next(entry for entry in catalog["animations"] if entry["id"] == record["id"])
            updated["status"] = record["status"]
            updated["studyStatus"] = "Procedural study; hand-contact polish"
            catalog_path.write_text(json.dumps(catalog, indent=2) + "\n")
        (evidence / (record["id"] + ".json")).write_text(json.dumps(report, indent=2) + "\n")
        print("HUSTLE", json.dumps(report), flush=True)


if __name__ == "__main__":
    main()
