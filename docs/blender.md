# Blender authoring

Use Blender 5.2. `main.blend` is the dance studio. `open-studio.ps1` opens it
with the included helpers and Game Rig Tools version:

```powershell
./open-studio.ps1
```

On other systems:

```sh
blender --factory-startup main.blend --python scripts/open_studio.py
```

The sidebar's **Helpers > Animation** provides animation selection, editing,
creation, copying, renaming, source saving, and **Bake and export animation GLB**.
Use the native `Man.rigify` and `Woman.rigify` controls for sparse IK editing.
Sources live in `animations/<dance-style>/sources/`; runtime exports live beside
that directory. The website shows move names and available solo characters.
**Edit animation file** opens the selected source with the shared studio's
characters and native rigs, including sources that contain only actions.
Restart the studio through the launcher after updating the helper scripts.

## Editable MPFB characters

The studios link body meshes and their original MPFB shape-key target stacks
from `assets/characters/mpfb-characters.blend`. Keep this file and the linked
`assets/wardrobe/` directory alongside the studios when copying the project.

Open the character library with the MPFB add-on enabled. Select `Man.body` or
`Woman.body`, then use MPFB's existing-human controls to edit macro settings
and targets. The library includes the native rigs, fitted clothing, textures,
and body masks. Save the library and reload the character library in
`main.blend` to see body changes. Blender's linked data is edited in its source
library; the dance studio retains local rig controls and animation actions.
Review and refit rigs and clothing after proportion changes, then rebuild the
runtime character exports with `scripts/build_wardrobe.py`.

## Install Game Rig Tools in regular Blender sessions

The project launcher registers the bundled version directly. For regular
Blender sessions, install
`tools/game-rig-tools-dance-animations-4.3.0.zip`:

1. Open **Edit > Preferences > Get Extensions**.
2. Use the menu's **Install from Disk**, then choose the ZIP.
3. Enable **Game Rig Tools (Dance animations)**. Use one installed Game Rig Tools
   version per session; replace an existing extension with the same ID through
   Blender's extension controls as needed.
4. Open `main.blend` and start the project helpers with `scripts/open_studio.py`.

This version supports the studio's native paired-rig Action Bakery workflow.
Its complete source, GPL license, original changelog, and fork notice are under
`scripts/blender/extensions/game_rig_tools/` and also in the installation ZIP.
Build a fresh archive after changing that source:

```sh
python scripts/package_game_rig_tools.py
blender --command extension validate tools/game-rig-tools-dance-animations-4.3.0.zip
```

MPFB is installed separately through Blender's extension catalog. Enable it
for character editing and wardrobe reconstruction. Animation playback and
editing use the bundled project helpers and native Rigify controls.
