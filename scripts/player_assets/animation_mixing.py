"""Author partial-body export masks and carry them into Godot clip metadata."""

import json
from fnmatch import fnmatchcase
from pathlib import Path

import bpy


REGIONS = json.loads(Path(__file__).with_name('animation_regions.json').read_text())
PROPERTY = "player_asset_mixable"
COMPATIBILITY = "player_asset_mixable_with"


def retrieve_regions(action, role):
    flags = action.get("player_asset_mix_" + role.lower(), 0) if action else 0
    return [region for index, region in enumerate(REGIONS) if flags & (1 << index)]


def retrieve_profile(action):
    enabled = bool(action and action.get(PROPERTY, False))
    return {
        "mixable": enabled,
        "compatible_activities": [name.strip().removesuffix("_baked") for name in
                                  (action.get(COMPATIBILITY, "") if action else "").split(",") if name.strip()],
        "regions": {role: retrieve_regions(action, role) for role in ("PLAYER", "PARTNER")},
    }


def includes(bone, regions):
    return any(fnmatchcase(bone, prefix) or (not prefix.startswith("DEF-spine") and fnmatchcase(bone, prefix + ".*"))
               for region in regions for prefix in REGIONS[region])


def filter_clip(asset, clip, action, rigs):
    profile = retrieve_profile(action)
    if profile["mixable"]:
        if not any(profile["regions"].values()):
            raise RuntimeError(f"Choose body regions for mixable animation {clip['name']}")
        paths = asset.retrieve_node_paths()
        channels = []
        for channel in clip["channels"]:
            path = paths[channel["target"]["node"]]
            role = next((role for role, rig in rigs.items() if rig and rig in path), None)
            bone = asset.document["nodes"][channel["target"]["node"]].get("name", "")
            if role and channel["target"]["path"] in {"translation", "rotation", "scale"} \
                    and includes(bone, profile["regions"][role]):
                channels.append(channel)
        if not channels:
            raise RuntimeError(f"Bake the chosen body regions for {clip['name']}")
        clip["channels"] = channels
        clip.setdefault("extras", {}).setdefault("activity_mixing", {}).update(profile)
    return profile["mixable"]


def create_region_property(property_name, label, items):
    return bpy.props.EnumProperty(
        name=label + " regions", items=items, options={"ENUM_FLAG"}, default=set(),
        get=lambda action: action.get(property_name, 0),
        set=lambda action, flags: action.__setitem__(property_name, flags))


def register():
    bpy.types.Action.player_asset_mixable = bpy.props.BoolProperty(
        name="Mixable activity", description="Export selected body regions for layered activity playback",
        get=lambda action: bool(action.get(PROPERTY, False)),
        set=lambda action, enabled: action.__setitem__(PROPERTY, enabled))
    bpy.types.Action.player_asset_mixable_with = bpy.props.StringProperty(
        name="Compatible activities", description="Comma-separated base activity IDs; leave empty for automatic compatibility",
        get=lambda action: action.get(COMPATIBILITY, ""),
        set=lambda action, names: action.__setitem__(COMPATIBILITY, names))
    items = [(name, name.replace("_", " ").title(), "Include this region and its finger bones", 1 << index)
             for index, name in enumerate(REGIONS)]
    for role, label in (("player", "Man"), ("partner", "Woman")):
        property_name = "player_asset_mix_" + role
        setattr(bpy.types.Action, property_name, create_region_property(property_name, label, items))


def unregister():
    for name in (PROPERTY, COMPATIBILITY, "player_asset_mix_player", "player_asset_mix_partner"):
        if hasattr(bpy.types.Action, name):
            delattr(bpy.types.Action, name)


def draw(layout, action):
    layout.prop(action, PROPERTY)
    if action.player_asset_mixable:
        layout.prop(action, COMPATIBILITY)
        for role in ("player", "partner"):
            if getattr(action, "player_asset_" + role):
                layout.prop(action, "player_asset_mix_" + role)
