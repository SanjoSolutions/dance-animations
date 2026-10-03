"""Select fitted MPFB clothing and its matching body coverage masks."""
import json
from pathlib import Path
import bpy

ROOT = Path(__file__).resolve().parents[1]


def retrieve_profile(style):
    wardrobe = json.loads((ROOT / 'wardrobe.json').read_text())
    return next((name for name, profile in wardrobe['profiles'].items()
                 if style in profile['styles']), wardrobe['default'])


def apply_profile(profile):
    for obj in bpy.context.scene.objects:
        profiles = json.loads(obj.get('dance_wardrobe_profiles', '[]'))
        if profiles:
            visible = profile in profiles
            obj.hide_set(not visible)
            obj.hide_render = not visible
        if obj.name in ('Man.body', 'Woman.body'):
            masks = json.loads(obj.get('dance_wardrobe_masks', '{}'))
            for modifier in obj.modifiers:
                if modifier.name in masks:
                    enabled = profile in masks[modifier.name]
                    modifier.show_viewport = enabled
                    modifier.show_render = enabled
    bpy.context.scene['dance_wardrobe_profile'] = profile or 'base'


def apply_animation(name):
    from import_assets import style_for
    apply_profile(retrieve_profile(style_for(name)))
