"""Original a-game Popping vocabulary and native control authoring."""
from copy import deepcopy
import math
import bpy
from mathutils import Euler, Vector
from native_poses import ControlPoser, DiscoChoreography, DiscoWristPoser, retrieve_base_pose

class PoppingVocabulary:
    """Named movement phrases, contact schedules, and composable positions."""

    def __init__(self):
        self.clips = []
        self.base = retrieve_base_pose()
        self.base.update(
            pelvis=(0, 0.012, 0.94),
            hands=(0.32, -0.27, 1.12),
            elbows=(0.65, 0.16, 1.25),
            knees=(0.22, -0.85, 0.5),
            feet=(0.19, -0.023, 0.0815),
            bend=3,
            finger_curl=0.25,
            wrist=(0, 0, 0),
            hips=(0, 0, 0),
        )
        self.build()

    def pose(self, **changes):
        result = deepcopy(self.base)
        result.update(changes)
        return result

    def add(
        self, name, category, accents, frames=None, contacts="both", description=""
    ):
        frames = frames or [0, 6, 12, 18, 24, 30, 36, 42, 48]
        poses = [self.pose(), *accents, self.pose()]
        assert len(frames) == len(poses), name
        frames = [frames[0], 2, *frames[1:-1], 46, frames[-1]]
        poses = [poses[0], poses[0], *poses[1:-1], poses[-1], poses[-1]]
        self.clips.append(
            dict(
                name=name,
                category=category,
                frames=frames,
                poses=poses,
                contacts=contacts,
                description=description,
                loop=True,
            )
        )

    def pulse(self, name, category, strong, soft=None):
        soft = soft or self.pose()
        self.add(
            name,
            category,
            [soft, strong, soft, soft, soft, strong, soft, soft],
            frames=[0, 11, 12, 15, 24, 35, 36, 39, 44, 48],
        )

    def build(self):
        self.pulse(
            "full_body_hit",
            "Hits",
            self.pose(
                pelvis=(0, 0.008, 0.953),
                chest=-5,
                head=-2,
                hands=(0.36, -0.3, 1.16),
                finger_curl=0.45,
            ),
        )
        self.pulse("chest_pop", "Hits", self.pose(chest=-9, bend=1))
        self.pulse(
            "arm_hits",
            "Hits",
            self.pose(
                hands=(0.49, -0.28, 1.36), elbows=(0.67, 0.04, 1.34), wrist=(8, 0, 0)
            ),
            self.pose(hands=(0.46, -0.28, 1.34)),
        )
        self.pulse(
            "leg_hits",
            "Hits",
            self.pose(pelvis=(0, 0.012, 0.968)),
            self.pose(pelvis=(0, 0.02, 0.925)),
        )
        self.pulse("shoulder_hits", "Hits", self.pose(shoulder=7, chest=-3))
        self.pulse("neck_hit", "Hits", self.pose(head=-7), self.pose(head=2))
        for side, sign in [("left", 1), ("right", -1)]:
            other = "right" if side == "left" else "left"
            wave = []
            for stage in range(7):
                height = [1.2, 1.43, 1.52, 1.44, 1.33, 1.2, 1.12][stage]
                wave.append(
                    self.pose(
                        hand_targets={
                            side: (sign * 0.53, -0.22, height),
                            other: (-sign * 0.36, -0.26, 1.18),
                        },
                        wrist=([20, -15, 0, 10, 0, 0, 0][stage], 0, 0),
                        shoulder=[0, 0, 6, 0, -3, 0, 0][stage],
                        chest=[0, 0, 0, -5, 2, 0, 0][stage],
                    )
                )
            self.add("arm_wave_" + side, "Waves", wave)
        rolls = []
        disco = DiscoChoreography()
        for index in range(7):
            hands, directions = disco.retrieve_arms(2, 16 + index * 0.5)
            rolls.append(self.pose(hand_targets=hands, hand_directions=directions))
        self.add(
            "forearm_roll",
            "Boogaloo",
            rolls,
            description="Arm-roll phrase adapted from solo_disco_dance",
        )
        self.add(
            "mannequin",
            "Animation",
            [
                self.pose(head_turn=h, hands=(0.37, -0.29, z))
                for h, z in [
                    (0, 1.12),
                    (16, 1.3),
                    (16, 1.3),
                    (16, 1.3),
                    (-16, 1.4),
                    (-16, 1.4),
                    (0, 1.12),
                ]
            ],
        )
        self.add(
            "body_wave",
            "Waves",
            [
                self.pose(head=8),
                self.pose(chest=8, head=-3),
                self.pose(bend=9, chest=-5),
                self.pose(pelvis=(0, -0.045, 0.92), bend=-4),
                self.pose(pelvis=(0, 0.035, 0.91), chest=-3),
                self.pose(chest=2),
                self.pose(),
            ],
        )
        self.add(
            "cobra",
            "Waves",
            [
                self.pose(lean=v, head_turn=-v * 2, hands=(0.48, -0.26, 1.43), chest=-3)
                for v in [0, 7, 12, 0, -12, -7, 0]
            ],
        )
        for name, field, amplitude in [
            ("chest_roll", "chest", 7),
            ("hip_roll", "hips", 9),
            ("neck_roll", "head", 8),
        ]:
            poses = []
            for index in range(1, 8):
                angle = index * math.pi / 4
                changes = {field: amplitude * math.sin(angle)}
                if field == "hips":
                    changes[field] = (
                        amplitude * math.cos(angle),
                        amplitude * math.sin(angle),
                        0,
                    )
                elif field == "chest":
                    changes["lean"] = 5 * math.cos(angle)
                else:
                    changes["head_turn"] = 10 * math.cos(angle)
                poses.append(self.pose(**changes))
            self.add(name, "Boogaloo", poses)
        for name, factor in [("twist_o_flex", 1), ("neck_o_flex", 0.55)]:
            self.add(
                name,
                "Boogaloo",
                [
                    self.pose(hips=(0, 0, factor * h), head_turn=n, chest_turn=c)
                    for h, n, c in [
                        (0, 18, 0),
                        (8, 18, 0),
                        (8, 18, 12),
                        (0, 0, 12),
                        (-8, -18, 0),
                        (-8, -18, -12),
                        (0, 0, 0),
                    ]
                ],
            )
        self.add(
            "old_man",
            "Boogaloo",
            [
                self.pose(
                    bend=12,
                    head=-8,
                    pelvis=(x, 0.03, 0.91),
                    hands=(0.34, -0.34, 1.01),
                    lean=-x * 40,
                )
                for x in [0, 0.07, 0.08, 0, -0.08, -0.07, 0]
            ],
        )
        for name, category, frames in [
            ("dime_stops", "Animation", [0, 8, 10, 20, 22, 32, 34, 44, 48]),
            ("ticking", "Animation", [0, 8, 10, 18, 20, 30, 32, 44, 48]),
            ("strobing", "Animation", [0, 8, 12, 18, 22, 28, 32, 44, 48]),
            ("slow_motion", "Animation", [0, 6, 12, 18, 24, 30, 36, 42, 48]),
        ]:
            self.add(
                name,
                category,
                [
                    self.pose(
                        hand_targets={
                            "left": (0.3 + x, -0.32, 1.12 + z),
                            "right": (-0.3, -0.27, 1.12),
                        },
                        head_turn=x * 40,
                    )
                    for x, z in [
                        (0.06, 0.10),
                        (0.06, 0.10),
                        (0.14, 0.25),
                        (0.14, 0.25),
                        (0.08, 0.15),
                        (0.08, 0.15),
                        (0, 0),
                    ]
                ],
                frames,
            )
        self.add(
            "robot",
            "Animation",
            [
                self.pose(
                    hand_targets={
                        "left": (0.4, -0.3, 1.4),
                        "right": (-0.4, -0.3, 1.14),
                    },
                    head_turn=h,
                    chest_turn=c,
                    wrist=(10, 0, 0),
                    finger_curl=0.08,
                )
                for h, c in [
                    (0, 0),
                    (18, 0),
                    (18, 10),
                    (0, 10),
                    (-18, 0),
                    (-18, -10),
                    (0, 0),
                ]
            ],
        )
        self.add(
            "puppet",
            "Animation",
            [
                self.pose(hands=(0.43, -0.28, z), shoulder=s, wrist=(25, 0, 0), head=8)
                for z, s in [
                    (1.2, 0),
                    (1.4, 8),
                    (1.52, 10),
                    (1.4, 5),
                    (1.2, 0),
                    (1.08, -3),
                    (1.12, 0),
                ]
            ],
        )
        self.add(
            "scarecrow",
            "Animation",
            [
                self.pose(
                    hands=(0.53, -0.2, z), lean=l, wrist=(25, 0, 0), finger_curl=0.08
                )
                for z, l in [
                    (1.25, 0),
                    (1.38, 8),
                    (1.3, 12),
                    (1.38, 0),
                    (1.3, -12),
                    (1.38, -8),
                    (1.25, 0),
                ]
            ],
        )
        self.add(
            "tutting_box",
            "Tutting",
            [
                self.pose(
                    hand_targets={"left": (x, -0.43, z), "right": (-x, -0.43, z)},
                    finger_curl=0.05,
                    wrist=(w, 0, 0),
                )
                for x, z, w in [
                    (0.3, 1.3, 0),
                    (0.3, 1.5, -20),
                    (0.16, 1.5, -20),
                    (0.16, 1.3, 20),
                    (0.3, 1.3, 20),
                    (0.3, 1.5, 0),
                    (0.3, 1.3, 0),
                ]
            ],
        )
        self.add(
            "tutting_angles",
            "Tutting",
            [
                self.pose(
                    hand_targets={
                        "left": (0.36, -0.4, z),
                        "right": (-0.36, -0.4, 2.7 - z),
                    },
                    wrist=(w, 0, 0),
                    finger_curl=0.05,
                )
                for z, w in [
                    (1.25, 0),
                    (1.5, 20),
                    (1.5, -20),
                    (1.35, 0),
                    (1.2, 20),
                    (1.2, -20),
                    (1.25, 0),
                ]
            ],
        )
        self.add(
            "finger_tutting",
            "Tutting",
            [
                self.pose(
                    hands=(0.2, -0.46, 1.33),
                    finger_curl=v,
                    finger_pattern=i % 2,
                    wrist=(w, 0, 0),
                )
                for i, (v, w) in enumerate(
                    [
                        (0.1, 0),
                        (0.7, 10),
                        (0.15, -10),
                        (0.65, 10),
                        (0.1, -10),
                        (0.7, 0),
                        (0.25, 0),
                    ]
                )
            ],
        )
        self.add(
            "lean",
            "Positions",
            [
                self.pose(lean=v, pelvis=(-v * 0.003, 0.015, 0.93))
                for v in [3, 8, 10, 0, -10, -8, -3]
            ],
        )
        # Alternating support includes lift keys on both the outward and return steps.
        for name, axis, glide in [
            ("fresno", 0, False),
            ("walkout", 1, False),
            ("side_glide", 0, True),
            ("backslide", 1, True),
        ]:
            frames = [0, 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 48]
            poses = []
            for frame in frames:
                feet = {
                    "left": [0.19, -0.023, 0.0815],
                    "right": [-0.19, -0.023, 0.0815],
                }
                side = "left" if frame <= 22 else "right"
                sign = 1 if side == "left" else -1
                phase = frame if side == "left" else frame - 20
                displacement = {10: 0.07, 14: 0.14, 18: 0.07}.get(phase, 0)
                feet[side][axis] += sign * displacement
                feet[side][2] += (0 if glide else 0.055) if phase in (10, 18) else 0
                weight = -sign * 0.065 if 6 <= frame <= 42 else 0
                poses.append(
                    self.pose(
                        foot_targets=feet,
                        pelvis=(weight, 0.012, 0.94),
                        hands=(0.34, -0.29, 1.12 + displacement * 0.5),
                    )
                )
            self.clips.append(
                dict(
                    name=name,
                    category="Footwork",
                    frames=frames,
                    poses=poses,
                    contacts="steps",
                    description="Alternating supported " + name,
                    loop=True,
                )
            )
        self.add(
            "heel_toe",
            "Footwork",
            [
                self.pose(
                    foot_turns={"left": v, "right": -v},
                    foot_pivots={"left": -0.16, "right": 0.06},
                    pelvis=(0, 0.012, 0.93),
                )
                for v in [5, 15, 5, 0, -5, -15, -5]
            ],
            contacts="pivot",
        )
        for name, changes in {
            "ready": {},
            "wide": {"feet": (0.29, -0.023, 0.0815), "pelvis": (0, 0.012, 0.91)},
            "low": {"pelvis": (0, 0.06, 0.85), "bend": 8},
            "staggered": {
                "foot_targets": {
                    "left": (0.19, -0.16, 0.0815),
                    "right": (-0.19, 0.10, 0.0815),
                }
            },
            "t_arm": {"hands": (0.64, -0.10, 1.43), "elbows": (0.65, 0.2, 1.45)},
            "box": {"hands": (0.29, -0.4, 1.48), "finger_curl": 0.05},
            "robot": {
                "hands": (0.4, -0.32, 1.3),
                "finger_curl": 0.05,
                "wrist": (15, 0, 0),
            },
            "scarecrow": {"hands": (0.53, -0.15, 1.28), "wrist": (25, 0, 0)},
        }.items():
            position = self.pose(**changes)
            self.clips.append(
                dict(
                    name="pose_" + name,
                    category="Positions",
                    frames=[0, 48],
                    poses=[position, position],
                    contacts="both",
                    description="Held " + name + " position",
                    loop=True,
                )
            )

class PoppingCharacter:
    def __init__(self, rig):
        self.rig = rig
        self.poser = ControlPoser(rig)
        self.wrists = DiscoWristPoser(rig)
        self.proportion = rig.data.bones["torso"].head_local.z / 1.0033524

    def apply(self, specification):
        pose = deepcopy(specification)
        for field in ("pelvis", "elbows", "knees", "hands", "feet"):
            pose[field] = tuple(value * self.proportion for value in pose[field])
        for field in ("hand_targets", "foot_targets"):
            if field in pose:
                pose[field] = {
                    side: tuple(value * self.proportion for value in target)
                    for side, target in pose[field].items()
                }
        if "foot_targets" not in pose:
            pose["foot_targets"] = {
                side: (sign * pose["feet"][0], *pose["feet"][1:])
                for side, sign in [("left", 1), ("right", -1)]
            }
        for side, suffix in [("left", "L"), ("right", "R")]:
            target = list(pose["foot_targets"][side])
            target[2] += (
                self.rig.data.bones["foot_ik." + suffix].head_local.z
                - 0.0815 * self.proportion
            )
            if "foot_pivots" in pose:
                pivot = Vector((0, pose["foot_pivots"][side] * self.proportion, 0))
                rotation = Euler(
                    (0, 0, math.radians(pose["foot_turns"][side]))
                ).to_matrix()
                target = Vector(target) + pivot - rotation @ pivot
            pose["foot_targets"][side] = target
        self.poser.apply(pose)
        for name, angles in [
            ("hips", pose["hips"]),
            ("chest", (pose["chest"], 0, pose.get("chest_turn", 0))),
        ]:
            bone = self.rig.pose.bones[name]
            bone.rotation_mode = "QUATERNION"
            bone.rotation_quaternion = Euler(
                tuple(math.radians(v) for v in angles)
            ).to_quaternion()
        for side, sign in [("L", 1), ("R", -1)]:
            shoulder = self.rig.pose.bones["shoulder." + side]
            shoulder.rotation_euler.y = math.radians(sign * pose.get("shoulder", 0))
            for finger in ("index", "middle", "ring", "pinky"):
                amount = pose["finger_curl"]
                if pose.get("finger_pattern") and finger in ("index", "ring"):
                    amount = 0.08
                for segment in (1, 2, 3):
                    bone = self.rig.pose.bones[f"f_{finger}.{segment:02d}.{side}"]
                    bone.rotation_quaternion = Euler((amount, 0, 0)).to_quaternion()
        self.poser.update()
        self.wrists.apply(0)
        for side in ("L", "R"):
            hand = self.rig.pose.bones["hand_ik." + side]
            hand.rotation_quaternion @= Euler(
                tuple(math.radians(v) for v in pose["wrist"])
            ).to_quaternion()
        self.poser.update()
        return self.poser.capture("pose")

class PoppingActionWriter:
    def create(self, rig, clip, states, character):
        action = bpy.data.actions.new("popping_" + character + "_" + clip["name"])
        action.use_fake_user = True
        action.use_frame_range = True
        action.frame_start, action.frame_end = 0, 48
        action.use_cyclic = True
        action["player_asset_participants"] = (
            "PLAYER" if character == "man" else "PARTNER"
        )
        action["Category"] = clip["category"]
        action["Tempo"] = 120
        action["Playback"] = "LOOP"
        action["Contact schedule"] = clip["contacts"]
        action["Description"] = clip["description"] or clip["name"].replace("_", " ")
        action.asset_mark()
        action.asset_data.description = (
            action["Description"] + "; independent " + character + " solo."
        )
        for tag in ("Popping", "Solo", character.title(), clip["category"]):
            action.asset_data.tags.new(tag)
        rig.animation_data.action = action
        for path, first in states[0].items():
            vectors = [list(state[path]) for state in states]
            if path.endswith("rotation_quaternion"):
                for index in range(1, len(vectors)):
                    if (
                        sum(a * b for a, b in zip(vectors[index - 1], vectors[index]))
                        < 0
                    ):
                        vectors[index] = [-v for v in vectors[index]]
            for component in range(len(first)):
                values = [vector[component] for vector in vectors]
                constant = max(values) - min(values) < 1e-6
                indices = [0] if constant else range(len(states))
                curve = action.fcurve_ensure_for_datablock(
                    rig, path, index=component, group_name=path.split('"')[1]
                )
                for index in indices:
                    point = curve.keyframe_points.insert(
                        clip["frames"][index], values[index], options={"FAST"}
                    )
                    point.interpolation = (
                        "CONSTANT" if constant or path.endswith('"]') else "BEZIER"
                    )
                    point.handle_left_type = point.handle_right_type = "AUTO_CLAMPED"
                curve.update()
        for index, frame in enumerate(clip["frames"]):
            action.pose_markers.new(
                "Loop" if index == len(clip["frames"]) - 1 else "Pose " + str(index)
            ).frame = frame
        self.track(rig, action)
        return action

    @staticmethod
    def track(rig, action):
        data = rig.animation_data
        slot = data.action_slot
        track = data.nla_tracks.new()
        track.name = action.name
        track.mute = True
        strip = track.strips.new(action.name, 0, action)
        strip.action_slot = slot
        strip.action_frame_end = strip.frame_end = 48
        strip.extrapolation = "NOTHING"
