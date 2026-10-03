"""Select the bundled Game Rig Tools module or its installed extension copy."""
import importlib
import bpy


def retrieve_game_rig_tools():
    for addon in bpy.context.preferences.addons:
        if addon.module == 'game_rig_tools' or addon.module.endswith('.game_rig_tools'):
            module = importlib.import_module(addon.module)
            if hasattr(bpy.types.Scene, 'GRT_Action_Bakery') and not hasattr(bpy.types.Scene, 'GRT_Action_Bakery_Rig_Pairs'):
                raise RuntimeError('Install the Dance animations Game Rig Tools ZIP for native paired-rig baking.')
            return module
    return importlib.import_module('game_rig_tools')
