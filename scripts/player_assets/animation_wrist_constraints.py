"""Per-animation control of the character rigs' natural wrist rotation limits."""

import bpy


PROPERTY = "animation_wrist_constraint"


def retrieve_enabled(action):
    return bool(action.get(PROPERTY, True)) if action else True


def store_enabled(action, enabled):
    action[PROPERTY] = enabled


class AnimationWristConstraints:
    def __init__(self, scene):
        self.scene = scene

    def apply(self, action):
        from animation_creation import AnimationCreator
        enabled = retrieve_enabled(action)
        for name in AnimationCreator.RIGS.values():
            rig = self.scene.objects.get(name)
            if rig and rig.is_editable and rig.pose:
                for bone in rig.pose.bones:
                    constraint = bone.constraints.get("Natural Wrist Rotation")
                    if constraint and constraint.type == "LIMIT_ROTATION" and constraint.mute == enabled:
                        constraint.mute = not enabled


def update_choice(action, context):
    from animation_participants import update_preview
    update_preview(action, context)


def register():
    bpy.types.Action.animation_wrist_constraint = bpy.props.BoolProperty(
        name="Wrist constraint", default=True, options=set(), update=update_choice,
        get=retrieve_enabled, set=store_enabled,
        description="Apply natural wrist rotation limits to the character rigs for this animation",
    )


def unregister():
    del bpy.types.Action.animation_wrist_constraint
