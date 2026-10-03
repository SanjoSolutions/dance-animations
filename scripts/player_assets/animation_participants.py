"""Per-action character selection shared by Blender controls and animation exports."""

import importlib
from pathlib import Path
import sys

import bpy

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from animation_export_cache import AnimationDocument
from animation_phase_markers import AnimationPhaseMarkers
import animation_interactables
import animation_objects
import animation_wrist_constraints
import animation_mixing
from animation_viewport import AnimationViewport


PROPERTY = "player_asset_participants"


def retrieve_actions():
    actions = {action.name: action for action in bpy.data.actions}
    for name in list(actions):
        base = name.removesuffix(".baked").removesuffix("_baked")
        if base != name and base in actions:
            actions[name] = actions[base]
    items = getattr(bpy.context.scene, "GRT_Action_Bakery", [])
    addon = next((name for name in bpy.context.preferences.addons.keys()
                  if name.endswith("game_rig_tools")), None)
    if items and addon:
        bakery = importlib.import_module(addon + ".GRT_Action_Bakery")
        for item in items:
            if item.Action:
                actions[bakery.Change_to_Baked_Name(bpy.context, item)] = item.Action
    return actions


def retrieve_selection(action):
    return action.get(PROPERTY, "BOTH") if action else "BOTH"


def retrieve_active_action(context):
    from track_chooser import TrackChooser
    name = TrackChooser(context.scene).retrieve_active_name()
    obj = getattr(context, 'object', None)
    animation = obj.animation_data if obj else None
    action = animation.action if animation else None
    selected = name or (action.name if action else context.scene.get("Track Chooser Selection", ""))
    return retrieve_actions().get(selected)


def includes(action, role):
    return retrieve_selection(action) in {"BOTH", role}


def store_participant(action, role, enabled):
    roles = {participant for participant in ("PLAYER", "PARTNER") if includes(action, participant)}
    if enabled:
        roles.add(role)
    else:
        roles.discard(role)
    action[PROPERTY] = "BOTH" if len(roles) == 2 else next(iter(roles), "NONE")


def update_preview(action, context):
    if action and not AnimationViewport.suspended and action == retrieve_active_action(context):
        animation_wrist_constraints.AnimationWristConstraints(context.scene).apply(action)
        AnimationViewport(context.view_layer).apply(
            {role for role in ("PLAYER", "PARTNER") if includes(action, role)},
            animation_objects.retrieve_selection(action))
        animation_interactables.apply_selection(action, context.scene)


def register():
    animation_mixing.register()
    animation_wrist_constraints.register()
    bpy.types.Action.player_asset_player = bpy.props.BoolProperty(
        name="Man", description="Include the man's channels in this animation's export",
        get=lambda action: includes(action, "PLAYER"),
        set=lambda action, enabled: store_participant(action, "PLAYER", enabled),
        update=update_preview,
    )
    bpy.types.Action.player_asset_partner = bpy.props.BoolProperty(
        name="Woman", description="Include the woman's channels in this animation's export",
        get=lambda action: includes(action, "PARTNER"),
        set=lambda action, enabled: store_participant(action, "PARTNER", enabled),
        update=update_preview,
    )
    animation_objects.register()
    animation_interactables.register()


def unregister():
    animation_mixing.unregister()
    animation_interactables.unregister()
    animation_objects.unregister()
    animation_wrist_constraints.unregister()
    del bpy.types.Action.player_asset_partner
    del bpy.types.Action.player_asset_player


class AnimationParticipants:
    def __init__(self, rig_names):
        animation_objects.register_properties()
        animation_interactables.register_properties()
        self.rigs = {"PLAYER": rig_names.get("man"), "PARTNER": rig_names.get("woman")}
        self.actions = retrieve_actions()

    def retrieve(self, name):
        return retrieve_selection(self.actions.get(name))

    def retrieve_signature(self, name):
        choices = animation_objects.retrieve_selection(self.actions.get(name))
        interactables = animation_interactables.retrieve_signature(self.actions.get(name))
        return [self.retrieve(name), [(obj.name, included) for obj, included in choices.items()], list(interactables),
                animation_mixing.retrieve_profile(self.actions.get(name)),
                AnimationPhaseMarkers(self.actions[name]).retrieve() if name in self.actions else {}]

    def apply(self, contents):
        asset = AnimationDocument(contents)
        paths = asset.retrieve_node_paths()
        changed = False
        for clip in asset.document.get("animations", []):
            action = self.actions.get(clip["name"])
            if action:
                scene = bpy.context.scene
                changed = AnimationPhaseMarkers(action).apply(clip, scene.render.fps / scene.render.fps_base) or changed
            selection = self.retrieve(clip["name"])
            excluded = {obj.name for obj, included in animation_objects.retrieve_selection(
                self.actions.get(clip["name"])).items() if not included}
            if selection != "BOTH":
                if selection == "NONE":
                    raise RuntimeError(f"Select Man or Woman in Participants for {clip['name']}")
                rig = self.rigs.get(selection)
                if rig is None:
                    raise RuntimeError(f"Configure the {selection.lower()} rig before exporting {clip['name']}")
                if not any(rig in paths[channel["target"]["node"]] for channel in clip["channels"]):
                    raise RuntimeError(f"Bake channels for the selected {selection.lower()} in {clip['name']}")
                excluded.update(name for role, name in self.rigs.items() if role != selection and name)
            mixed = animation_mixing.filter_clip(asset, clip, self.actions.get(clip["name"]), self.rigs)
            if excluded or mixed:
                clip["channels"] = [channel for channel in clip["channels"]
                                    if excluded.isdisjoint(paths[channel["target"]["node"]])]
                if mixed and not clip["channels"]:
                    raise RuntimeError(f"Choose body regions for an included participant in {clip['name']}")
                indices = sorted({channel["sampler"] for channel in clip["channels"]})
                mapping = {original: index for index, original in enumerate(indices)}
                clip["samplers"] = [clip["samplers"][index] for index in indices]
                for channel in clip["channels"]:
                    channel["sampler"] = mapping[channel["sampler"]]
                changed = True
        return asset.retrieve_bytes() if changed else contents
