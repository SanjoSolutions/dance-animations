## Commits

Whenever you create a Git commit, append exactly one commit trailer:

Co-authored-by: Codex <noreply@openai.com>

## GitHub

Identify Codex-authored GitHub communication as written by Codex.
Publish only to main after the user approves the local quality review.

## Assets

Use the project's strict size-based LFS policy:
files larger than 100 MiB use Git LFS; files at or below 100 MiB use regular Git.
Run `python scripts/lfs_policy.py sync` after staging and
`python scripts/lfs_policy.py check` before committing.

Keep per-clip provenance and the source's procedural-study status.
Use MPFB base character meshes for previews.

# Principles

Make sure to always follow the principle guidelines.

## Main principles

- Use OOP with composition. Strong tools of OOP are composition, encapsulation and polymorphism.
- Strongly follow the DRY principle. Generalize as similar patterns emerge.
- Strongly follow the SRP principle (single responsibility principle).
- Prefer higher abstractions
- Optimize code for readability for the user. This includes expressive names and straight forward flows. This does not include verbose comments that add redundant info.
- Follow YAGNI principle

## Other principles

- Use US English.
- Use expressive names for identifiers (variable names, function names, class names, property names etc.)
- Highly prefer to write natural language class-inclusively: every sentence states positive class membership — what something IS, what belongs, what to do — using only affirmative content words. This rules out negation particles (no, never, not), privatives (without, lacking, absent), negation morphemes (un-, in-/im-, non-, dis-, a-, -less).
- Prefer class-inclusive expressions: state membership in the intended category directly rather than excluding another category. For example, prefer is_available over not is_busy when availability is the intended condition.
  This preference concerns meaning, not syntax or vocabulary. Negation is appropriate when it expresses the intended condition accurately. For boolean checks, prefer idiomatic not condition over condition == false.
- Avoid early-skip guard chains for ordinary control flow. Prefer structuring conditions so the primary path is inside the `if` branch and fallback behavior is in `else` when that keeps the flow readable.
- Avoid early stop returns after a branch performs work. Prefer placing the remaining ordinary control flow in the `else` branch.
- For getter functions, use the verb "retrieve" instead of "get" (for example, `retrieveThing` instead of `getThing`).
- Don't include the unit (ms etc.) of the value in identifiers (variable names, parameter names, function names, class names, property names etc.). Instead document the unit with GDScript documentation comments (i.e. `## In milliseconds.`, `## Returns a value in milliseconds.`, or `## Parameter value in milliseconds.`). So instead of `durationMs`, rather `duration` with documentation comment with the unit.
- Avoid uncommon abbreviations in identifiers and prose.
- Structure projects modularily (not by type). Files that are closer related to each other should be closer to each other in the file system.
- Clean up temporary files that you have created when you no longer need them.

### Testing

Principles:

- Test fils should be next to the files that they test.
- Test what the system should do. Don't test what the system should not do.
- No test-only behavior.
- Only test things through their public API.

# UI

Use Bootstrap for new projects or when it is already used by the project.
UI should be minimalistic, to the point what functionally is required.
Avoid marketing prose. Assume users are familiar with common web patterns.

- Form buttons should be right aligned.
- First field should be auto focused when the page is one form primarily.


## Dance animation workflow

Apply this workflow to animation tasks in this checkout. Complete the requested
local authoring and validation work, then present the result for review under
the GitHub policy above. Use reasonable implementation choices within the
requested scope and state assumptions that affect choreography or acceptance.

### Start with local evidence

- Read [the Blender workflow](docs/blender.md) for studio setup and
  [local validation](docs/validation.md) for check coverage. Read the relevant
  sections of [animation authoring details](docs/animation-authoring.md) when
  changing pose solvers, action bindings, baking, or batch tooling.
- Inspect the selected clip in `catalog.json`, `source-inventory.json`, and
  `animations/<dance-style>/sources/`. Treat saved files as the checkpoint;
  catalogs and procedural recipes describe their recorded scope and revision.
- Consult the relevant style record in `docs/source-review-records/` for
  provenance, measured failures, and historical review. Translate its asset
  identifiers to this checkout's inventory. Execute commands verified against
  current local files; historical paths and scripts are archival context.
- Keep task tooling and dependencies inside this project. Reuse
  `scripts/dance_tools.py` and `scripts/player_assets/` for source composition,
  saving, participant selection, and native baking. Verify a helper's current
  public API before using it.

### Studio and source contract

- Use Blender 5.2 and confirm the executable and source versions. Open
  `main.blend` through `./open-studio.ps1`; the launcher registers the bundled
  helpers and Game Rig Tools. Restart through the launcher after helper changes.
- Author on native `Man.rigify` and `Woman.rigify` IK controls. Keep standard
  MPFB base bodies, shared deformation rigs, drivers, rest skeletons, native
  wrist constraints, and saved control rotation modes. The skeleton contract
  lives in `assets/characters/rig-schema.json`.
- Store editable sources in `animations/<dance-style>/sources/` and individual
  GLBs in `animations/<dance-style>/`. Use `animations/shared_scene_data.blend`
  as the portable rig template. Keep character and wardrobe dependencies
  project-relative; confirm each linked library resolves before saving.
- Use **Helpers > Animation** to select, create, copy, edit, rename, and save
  animations. **Edit animation file** composes action-only sources with the
  local studio. Choose the scene containing the rigs before evaluating poses.
- Hydrate required Git LFS objects with a targeted pull before opening assets.
  A text file beginning with `version https://git-lfs.github.com/spec/v1` is a
  pointer. Follow linked-library dependencies and compare resolved binary hashes.
- Keep review scenes, cameras, mats, and temporary materials in a task-specific
  review directory. Preserve the studio's selected action and frame across
  scripted authoring. Scope shared-template changes to the task's needs.

### Choreography and contacts

- Define the requested vocabulary, roles, tempo, beat subdivisions, effective
  frame rate, support intervals, entry/exit formations, and loop or travel
  behavior before generating a repertoire. Record planned and saved coverage
  separately. Original practice choreography carries its own song/phrase provenance.
- Author sparse keys at meaningful approach, contact, hold, release, and weight
  transfer poses. Keep stationary controls to one initial key after checking
  interpolation. Add corrective keys at failing samples and repeat checks after
  simplification. Sample fast accents at a spacing that captures their peaks.
- Calibrate each character against evaluated MPFB sole geometry and forearm
  references. Fit relaxed fingers, natural wrists, hips, head, and feet. Measure
  evaluated limb reach before capturing contact references.
- Plan paired support targets and performer spacing in world space. Choose
  left/right foot phases for the formation and role. Fit raised or shadow holds
  through partner spacing, shoulders, torso, elbow poles, wrist alignment, and
  calibrated palm contact. Preserve held-hand targets while styling free arms.
- Check control targets, evaluated deform joints, and skinned surfaces through
  contact intervals. Measure foot plants, intentional slides, heel/forefoot
  pivots, and swings according to their intended contact type. Record support
  transfers for standing, kneeling, seated, and floor choreography.
- Review both performers' own-limb and partner clearance, forearm/torso gaps,
  hand reconnections, wrist orientation, fingers, and physical balance through
  the complete motion. Validate static holds and moving variants independently.
- Check loop position, orientation, and velocity near the seam. Preserve duplicate
  stored endpoints and exclusive playback ends: a stored 0–96 loop plays 0–95.
  Record traveling-cycle displacement and verify its playback handling. Directed
  transitions play once and match the actual saved entry/exit position clips.

### Saved actions and runtime exports

- Keep explicit owner slots, `player_asset_participants`, prop selections,
  shared NLA track names, action/strip ranges, strip influence, serialized
  `animation_file_tracks`, and loop metadata synchronized. Use `PLAYER` for
  Man solos, `PARTNER` for Woman solos, and `BOTH` for paired clips.
- Verify effective `render.fps / render.fps_base` after source composition and
  reopening. Derive duration from the stored frame interval and effective rate;
  compare it with the intended beat count and actual GLB sample times.
- Use **Bake and export animation GLB** for native deformation baking and source
  saving. For scripted trials, give `dance_tools.export_action` a task-specific
  destination and `update_catalog=False`, then validate the saved outputs before
  updating the active catalog. Keep provisional candidates in task evidence.
- Preserve constant transform channels in bakes. Reopen sources in a fresh
  Blender process, compare every deform bone including fingers and toes, and
  evaluate baked playback with live deform follow constraints muted. Measure
  absolute pose differences and contact drift as separate quantities.
- Verify each GLB's single embedded animation name, duration, finite transforms,
  sample times, and intended performer/node targets. Check skeleton and morph
  target bindings against the project's actual MPFB models through Three.js
  playback. Preserve per-clip source hashes, original hashes, and study status
  in `catalog.json` and `source-inventory.json`.

### Validation and completion

Record these stages separately for each delivered clip:

| Stage | Required evidence |
| --- | --- |
| Authored controls | Evaluated IK reach, contacts, clearance, timing, and loop/transition behavior. |
| Saved source playback | Fresh-process composition, chooser selection, owner slots, native NLA bindings, ranges, rotation modes, and matching evaluated poses. |
| Deformation bake | Every deform bone compared with authored playback, with live follow constraints muted; contact and seam measurements repeated. |
| Runtime export | GLB identity, duration, sample coverage, participant bindings, and playback with the actual project models. |
| Visual review | Viewport or rendered playback from useful angles for recognizable choreography, ergonomic poses, surfaces, and transitions. |

- Associate reports with source/export SHA-256 hashes, shared-scene and character
  dependency hashes, generator revision, sampled frames, units, tolerances,
  coverage, and measured failures. Give skipped or empty checks an explicit
  coverage status. Carry forward results for matching asset and dependency revisions.
- Use authored keys, integer frames, fractional frames, contact phase boundaries,
  and near-seam samples. Numerical acceptance, visual review, and publication
  each establish their own completion state. Keep procedural-study labels until
  the required stages pass; structural checks establish structural coverage.
- For asset or playback changes, run `npm run check`, `npm test`, and
  `npm run build`. For Blender helper changes, run the relevant local Blender
  tests from [the authoring details](docs/animation-authoring.md#local-checks).
  For documentation edits, verify referenced paths and commands and review the diff.
- Report delivered clip names/counts, source/bake/export/review states, validation
  coverage, and remaining measured issues concisely. Scale checks to the changed
  behavior and acceptance scope; repeat or broaden checks for concrete failures,
  changed dependencies, or gaps in required coverage.

### Batch work and interruption

- Keep recipes stable during a running Blender batch and record their content
  hashes at startup. Later script edits belong to the next process. Give each
  worker a distinct temporary directory, result file, and log file.
- Run shared catalog writers serially or coordinate writes. Run full-scene
  reviews and renders sequentially when memory capacity requires it. Finish each
  source writer before sampling and record the evaluated revision.
- Persist a per-clip checkpoint after each source save, bake, and export. Reconcile
  actual saved files and completed log entries with manifests before reporting
  whole-repertoire coverage. A focused report describes its selected subset.
- When the user stops work, terminate task-owned generation/render processes and
  preserve durable outputs and diagnostics. Record the stopping point under
  `docs/animation_work_status/<task>.md`, creating the directory as needed.
- Include per-file paths, sizes, SHA-256 hashes, roles, slots, frame ranges,
  authored/baked/exported/reviewed states, dependency/generator revisions,
  validation coverage, known failures, active-catalog state, process state, and
  exact resume commands using local paths. Identify newer in-memory attempts and
  historical renders by revision. Resume within the user's current authorization.

### Blender extension installation tests

- Use a dedicated temporary profile. Create its resource root, config, scripts,
  and extensions directories before launching Blender; set
  `BLENDER_USER_RESOURCES`, `BLENDER_USER_CONFIG`, `BLENDER_USER_SCRIPTS`, and
  `BLENDER_USER_EXTENSIONS` to those existing directories.
- Before extension repository changes, installation, or preference saving,
  verify `bpy.utils.user_resource('CONFIG')` resolves to the intended temporary
  config directory. Record the regular `userpref.blend` SHA-256 before and after
  the test and compare it; record file presence when the regular profile is fresh.
  Factory startup selects factory settings while preference writes still use
  the configured profile path.
- Keep the same isolated profile environment for installation, authoring,
  validation, export, and their subprocesses. Follow the bundled extension
  packaging and validation commands in [the Blender workflow](docs/blender.md).
