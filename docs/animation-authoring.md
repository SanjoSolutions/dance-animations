# Animation authoring details

Use these sections for the corresponding Blender task. The root
[agent instructions](../AGENTS.md#dance-animation-workflow) define the workflow
and acceptance stages; [the Blender guide](blender.md) defines studio setup.
All paths below are relative to the dance-animations checkout.

## Pose solving and interpolation

- Evaluate the intended frame before fitting a pose. Capture each fitted wrist
  rotation and calibrated palm position in the saved pose data so subsequent
  frame evaluation restores the fit. Align the wrist to the evaluated forearm,
  then refit the palm origin; wrist rotation changes its offset from the IK control.
- Use the local Snap Hand helper and its calibration for hand placement and
  finger fitting. Measure hand-to-hand separation and body-local surface contacts
  directly; a natural Bézier grip path can depart from a linear world-space target.
- Preserve native wrist constraints. Resolve reach through performer spacing,
  torso placement, and elbow poles. Record per-action wrist-constraint exceptions
  explicitly and review deform hand rotations, angular steps, and wrist alignment
  throughout the motion, including saved-source and bake comparisons.
- Check the elbow pole against the shoulder-to-wrist axis during connected turns.
  Near alignment can produce an elbow flip and a wrist spike between keyed poses.
- Snapshot affected controls' world matrices before group turns or parent
  transforms. Apply transformed snapshots parent-first, update the dependency
  graph, then restore world-space hand/foot targets and elbow/knee poles. For solo
  travel, move hand targets with the torso before adding arm accents.
- Normalize quaternion keys and align successive signs with a dot-product check.
  Repeat alignment across all four rotation curves after custom matrix posing
  and before simplification. Match loop-ending controls to the opening values
  with compatible signs; check finite values after repeated small rotations.
- Unwrap successive foot headings to their nearest equivalent angle before
  interpolation. Include the rest-space IK-to-deform rotation offset when
  comparing planted-foot orientations. Use shortest equivalent quaternion angles
  for angular seam measurements and compare several sample spacings near extrema.
- Keep fractional rhythm times in F-curves and catalogs. Pass the fractional
  `frame` explicitly to `keyframe_insert`; `scene.frame_set(..., subframe=...)`
  alone can produce integer-time keys. Pose-marker labels use integer frames.
- Insert scalar custom properties with `keyframe_insert(path)`; supply a component
  index for array channels. Preserve underlying numeric values for keyed Rigify
  parent-space enum properties, even when RNA exposes a label.
- Preserve Bézier handles and interpolation when joining phrases. A boundary
  key retains the preceding incoming handle and following outgoing handle.
  Expand one-key constants with flat handles at their held value. Validate both
  the component phrases and assembled routine against baked playback.
- For prop-axis turns, place the root pivot on that axis and use stable local
  grip offsets. Compose palm targets with the calibrated wrist matrix and fit
  fingers to the prop. Preserve grip metadata and pose-specific overrides when
  deriving or mirroring poses.

## Evaluated support and clearance

- Capture grounded contacts after the full rig evaluates. Calibrate soles,
  knees, heel pivots, and forefoot pivots against each character's skin geometry.
  Preserve a stable target through each support interval and check toe/heel pitch
  transitions between keys. Mesh-driving deform joints can differ from IK joints.
- Measure control endpoint reach before storing a contact reference. Review
  control, deform, and skin contact results separately, including stationary
  tweak controls and inherited scale. An accurate ankle target establishes only
  that target's placement.
- Sample complete swing paths, integer key times, fractional frames, toe-off,
  landing, and support-transfer boundaries. Check shins, thighs, feet, each
  dancer's own limbs, partner clearance, forearms, upper arms, and torso surfaces.
- For capsule diagnostics, use exact closest points on finite limb segments.
  Record radii, actor pair, failing frame, measured gap, and sample coverage;
  review actual skin surfaces alongside the proxy measurements.
- Preserve mesh modifier enablement, body masks, and visibility during surface
  checks. Evaluate standard `Man.body` and `Woman.body` MPFB meshes. Keep
  preview-only material, shape-key, and visibility changes in isolated review scenes.
- For floor and seated poses, report the lowest evaluated surface and the maximum
  of that minimum height across samples. Measure penetration, floating supports,
  support transfer, and drift with explicit tolerances and units.
- Validate held-hand recovery intervals and transitions against both performers'
  saved endpoint clips. Include relative grip error, orientation, limb reach,
  body clearance, and support velocity as separate measurements.
- For traveling cycles, compare closing poses after removing the recorded root
  displacement and verify displacement accumulation for both performers. Select
  cyclic playback when the runtime handles that travel as intended.

## Action ownership and saved playback

- Reuse `AnimationFileWriter` and `AnimationAuthoringScene` in
  `scripts/player_assets/animation_files.py`. Source descriptors retain the
  relative shared-template reference, timing, and selected source action.
- Assign a layered action to each owner before
  `action.fcurve_ensure_for_datablock(owner, ...)`. Bind NLA strips to slots for
  the owner's ID type: rigs use `OBJECT`; shape-key datablocks use `KEY`.
- Finalize action and NLA strip ranges after adding all keys. Synchronize owner
  slots, shared track names, intended influence, and serialized
  `animation_file_tracks`. Growing a one-pose action requires updating its strips.
- Use `TrackChooser` in `scripts/track_chooser.py` for source discovery and
  selection. Test reopened composed NLA playback through
  `AnimationAuthoringScene.prepare()` and chooser selection; direct action
  assignment exercises a different binding path.
- Register included props through `animation_objects` and preserve participant
  metadata. Keep Asset Browser authors, descriptions, catalogs, licenses, and
  tags when splitting sources, and verify those fields after reopening.
- Preserve saved rotation modes, including quaternion finger controls, across
  posing and reload. Actions store channels; the owning rig supplies rotation
  modes. Capture the initial values of stationary tweak controls when using a
  poser that resets the full rig.
- Retain animation-data drivers when switching actions or NLA tracks. Store
  action references under compact custom-property keys while keeping descriptive
  action names; property dictionary keys have a shorter length limit.
- Resolve appended actions by exact datablock identity. Repeated appends can add
  numeric name suffixes while a name lookup selects a previously loaded action.
  A fresh process per source provides an independent reload check.
- Before editing shared studio data, preserve a backup and fingerprint existing
  action curves. After saving and reopening, compare keys, handles, slots,
  ranges, and dependency resolution. Integrate concurrent binary edits in Blender
  with both action sets and their dependencies preserved.

## Native bake and export diagnostics

- Reuse `SingleActionBake` in `scripts/player_assets/single_action_bake.py` and
  `AnimationClipScene` in `scripts/player_assets/single_animation_export.py`
  through `dance_tools.export_action`. Preserve parents and constraints in the
  shared Action Bakery setup; use a distinct baked action name.
- Reveal participating control and deform rigs for headless evaluation with
  `hide_viewport = False` and `hide_set(False)`, then update their pose state.
  Hidden rigs can retain earlier matrices, especially while mesh evaluation pauses.
- Establish the authored reference with neutral deform-bone basis transforms
  and live follow constraints. Then evaluate the saved baked action with those
  constraints muted. Clearing an action retains pose values, so prepare each
  reference explicitly. Compare every deform bone at matching sampled times.
- Keep constant transform channels explicit in the bake. Measure bone position,
  orientation, planted-contact drift, and seam velocity separately. A saved
  `.baked` action identifies an output whose fidelity still requires validation.
- For scale/shear diagnostics, account for the bone's longitudinal Y axis,
  rest length, connected children, and inherited scale. Scope connectivity
  experiments to temporary armature data using the editable-armature API;
  `bpy.types.Bone.use_connect` is read-only. Preserve the shared rest skeleton.
- Export isolated clip scenes with `use_active_scene=True`. Inspect the saved
  animation names and participant rig inventory to catch channels introduced
  by another scene or dependency. Validate target bindings with the actual
  project models, including applicable morph paths and node identity.
- Inspect GLB channel times: fractional source keys can be sampled at integer
  frames during export. Preserve intended duration when changing sample spacing
  and compare authored, saved-source, baked, and exported motion independently.
- For frozen geometry previews, activate the source scene, evaluate a pre-roll
  frame, then evaluate the requested frame before copying meshes. Use a fresh
  render directory for each revised source. Blender movie output requires
  `scene.render.image_settings.media_type = "VIDEO"` before `file_format = "FFMPEG"`.

## Local checks

Run commands from the repository root with the verified Blender 5.2 executable.
Use `--python-exit-code 1` for background scripts so failures reach the caller.
The root instructions define isolated profiles for extension installation tests.

For studio selection, source editing, saving, baking, and export helpers:

```powershell
$blenderExecutable = 'C:\Program Files\Blender Foundation\Blender 5.2\blender.exe'
& $blenderExecutable --factory-startup --background --python-exit-code 1 --python scripts/dance_tools.test.py
```

For fresh startup, editing, and save/reopen of supported source formats:

```powershell
& $blenderExecutable --factory-startup --background --python-exit-code 1 --python scripts/player_assets/animation_files.test.py
```

For character or wardrobe changes, select the relevant tests and prerequisites
in [local validation](validation.md). For assets or playback, run:

```powershell
npm run check
npm test
npm run build
```

Record numerical motion review alongside these structural checks with explicit
asset hashes, tolerances, and sampling coverage. Inspect report results as well
as process exit status; a completed review can contain measured failures.
