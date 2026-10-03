"""Retain the standard dance skeleton when rebuilding imported authoring rigs."""
import json
from pathlib import Path
import bpy

ROOT = Path(__file__).resolve().parents[1]


def retrieve_bones():
    return json.loads((ROOT / 'assets/characters/rig-schema.json').read_text())


def retain_dance_bones():
    schema = retrieve_bones()
    widgets = set()
    for rig in list(bpy.context.scene.objects):
        if rig.type == 'ARMATURE' and rig.name in schema:
            allowed = set(schema[rig.name])
            removed = {bone.name for bone in rig.data.bones if bone.name not in allowed}
            if removed:
                widgets.update(bone.custom_shape for bone in rig.pose.bones if bone.name in removed and bone.custom_shape)
                if bpy.context.object and bpy.context.object.mode != 'OBJECT':
                    bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.select_all(action='DESELECT')
                rig.hide_set(False)
                rig.select_set(True)
                bpy.context.view_layer.objects.active = rig
                bpy.ops.object.mode_set(mode='EDIT')
                for bone in list(rig.data.edit_bones):
                    if bone.name in removed:
                        rig.data.edit_bones.remove(bone)
                bpy.ops.object.mode_set(mode='OBJECT')
                for bone in rig.pose.bones:
                    for constraint in list(bone.constraints):
                        if getattr(constraint, 'subtarget', '') in removed:
                            bone.constraints.remove(constraint)
    used = {bone.custom_shape for rig in bpy.data.objects if rig.type == 'ARMATURE' for bone in rig.pose.bones}
    for widget in widgets - used:
        bpy.data.objects.remove(widget, do_unlink=True)
