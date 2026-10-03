# Merengue work status — preservation handoff

Recorded 2026-10-02 (UTC), authored by Codex. Animation work stopped at the user's preservation instruction; subsequent work is verification, documentation, and Git delivery.

- Chat title: **Create Merengue dance animations**.
- Chat ID: `01a0fcbf-9c27-70ea-89f0-530f8feca040`.
- Project/environment: A-Game, `apps/a-game`, sanjo-solutions cloud; checkout `/workspace/sanjo-solutions`.
- Task branch: `codex/merengue-repertoire`.
- Commit at stop: `b36686e72089e92a05fdddbbb6d53f548c07c7b6` (task work was uncommitted).
- Task preservation commit: `9cb266bc84321eb8d139f0f3790f83be6da5fb0a`, based on `2d8c1c5f24f8ed6f5a363a8024e65fc0b8f4c43a`.
- Main integration base: `1e89ec851ca861c22e30d7425177db24e4251054`. The merged runtime registry retains all 191 incoming libraries and adds all 28 Merengue libraries (219 total).
- The containing preservation commit records this status and assets. Later merge commits preserve concurrent remote history; use `git log --all --oneline -- docs/animation_work_status/merengue_partner_repertoire.md` to identify them.

## Scope and stopping point

The original request was a broad, organized Merengue repertoire for both characters in `man_and_woman3.blend`, with coordinated natural motion, planted contacts, body clearance, smooth transitions, interpolated and loop validation, editable per-animation sources, and delivery to main. Merengue variations and combinations are open-ended; the authored vocabulary contains 28 named practice figures.

**Preserved state: 28 authored paired sources, 28 embedded paired bakes, 28 exported GLBs, and 28 importer sidecars. Twenty-five sources passed the saved-delivery checks. Three remain partial. All 28 exports passed Godot structural/playback checks before final catalog integration; 25 are currently active and three failed drafts are excluded.** This is a procedural choreography study with partial visual/style review, rather than an accepted exhaustive Merengue library. Authoring-session `passed` fields in the three failed clips' original reports cover contact/loop checks only; the failure record below is authoritative for saved-delivery status.

Each source owns one control action and one `.baked` action. Each action has synchronized Man and Woman slots. `player` is Man/leader and `partner` is Woman/follower; leader-turn clips rotate Man and follower-turn clips rotate Woman. Both characters continue the beat. Sources are discovered by the combined library; the combined `.blend` and shared geometry were preserved. The neutral stance and hand setup reuse `share_company.blend`; wrist fitting follows the existing disco technique.

## Durable asset inventory

All rows use 24 fps, 120 BPM, cyclic practice phrases, and both roles. Ranges show stored keys / inclusive Blender playback; the matching final key is omitted from native playback. Position-change phrases include their return to the entry frame. Promenade and side-by-side changes start in the single-hand open hold, release during repositioning, and reconnect. Other footwork and turn phrases enter their named frame; blend compatible clips at phrase boundaries.

| Suffix after `merengue_` | Stored / playback frames | Deliverables | Saved validation |
| --- | --- | --- | --- |
| `basic_in_place` | 0–48 / 0–47 | Authored, baked, GLB | Pass |
| `side_basic` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `forward_back_basic` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `diagonal_basic` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `box_basic` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `rock_step` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `open_break` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `closed_basic` | 0–48 / 0–47 | Authored, baked, GLB | Pass |
| `closed_side_basic` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `single_hand_basic` | 0–48 / 0–47 | Authored, baked, GLB | Pass |
| `reverse_single_hand_basic` | 0–48 / 0–47 | Authored, baked, GLB | Pass |
| `side_by_side_basic` | 0–48 / 0–47 | Authored, baked, GLB | Pass |
| `side_by_side_travel` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `promenade_basic` | 0–48 / 0–47 | Authored, baked, GLB | Pass |
| `counter_promenade_basic` | 0–48 / 0–47 | Authored, baked, GLB | Pass |
| `shadow_basic` | 0–48 / 0–47 | Authored, baked, GLB | Pass |
| `follower_right_turn` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `follower_left_turn` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `leader_right_turn` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `leader_left_turn` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `couple_right_turn` | 0–384 / 0–383 | Authored, baked, GLB | Partial: bake drift |
| `couple_left_turn` | 0–384 / 0–383 | Authored, baked, GLB | Partial: bake drift |
| `follower_underarm_right` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `follower_underarm_left` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `hand_change` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `open_to_closed` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `open_to_promenade` | 0–192 / 0–191 | Authored, baked, GLB | Pass |
| `open_to_side_by_side` | 0–192 / 0–191 | Authored, baked, GLB | Partial: skin overlap |

[merengue_asset_manifest.json](merengue_asset_manifest.json) enumerates every exact source, GLB, import-settings, and report path, size, SHA-256, frame range, role, and authored/baked/exported state. Sources are under `animations/man_and_woman/merengue_*.blend`; runtime updates are under `models/player/animation_updates/merengue_*_baked_<name-hash>.glb`. The filename hash identifies the clip name; the manifest supplies the content hash. Runtime registration is in `models/player/animation_updates.tres`. Existing runtime library entries were retained during integration.

## Partial assets and concrete blockers

1. `merengue_open_to_side_by_side`: saved evaluated skins intersect outside the allowed hand-contact regions at frames 48 and 144 (70 triangle pairs at each frame). Source contact, foot, wrist, and loop metrics passed. Body-clearance acceptance failed. The source, bake, and GLB are preserved unchanged.
2. `merengue_couple_right_turn`: the saved bake's sampled contact-joint error reaches **0.008229227676751785 m**, above the **0.008 m** tolerance. Source contact, loop, and sampled skin checks passed before the bake comparison failed.
3. `merengue_couple_left_turn`: equivalent bake comparison reaches **0.008229880096972704 m**, above **0.008 m**. Source contact, loop, and sampled skin checks passed before this failure.

[merengue_validation_failures.json](merengue_validation_failures.json) records the failed source hashes and raw surface/bake evidence. Refinement stopped at the user's instruction. The general full-catalog Blender test remains expected to fail until these three assets are repaired. Runtime structural success does not supersede these failures.

## Code and workflow changes

Task modules in `scripts/player_assets/`:

- `merengue.py`: named repertoire, staged partner footwork, positions, contacts, arm poles, hip/chest counterbalance, and per-clip authoring entry point.
- `merengue_curves.py`: quaternion hemisphere continuity and constant-channel compaction.
- `merengue_delivery.py`: half-frame numerical review, native Blender visual baking, saved family bindings, standard clip export, and serialized runtime update publication. The publication lock uses POSIX `fcntl`; the documented cloud workflow is supported, while Windows CLI portability remains a follow-up.
- `merengue_finalize.py`: saved-file metadata/curve normalization and conditional rebaking. This mutates sources; run only after animation work is reauthorized.
- `merengue_surface_review.py`: evaluated replacement-skin floor/support and inter-character triangle intersection checks.
- `merengue_render_review.py`: isolated clay previews; current outputs are preserved below.
- `merengue.md`: repertoire and reproduction guide.
- `test_merengue.py`: reopen sources, check slots, asset tags, shared bindings, playback, finite keys, interpolated contacts, surfaces, bake agreement, GLB structure/duration, and hashes.
- `test_merengue.gd`: the 25 active runtime clips (historically all 28), bone paths, both moving skeletons, and loop flags. Its probe uses a half-beat offset, avoiding the initial test's false failure from sampling a full repeated weight-transfer cycle in 32-beat clips.

Existing files changed:

- `scripts/player_assets/paired_animation_authoring.py` and its test: explicit fractional keyframe insertion and contact-peak regression.
- `scripts/player_assets/animation_files.py` and its test: retain Asset Browser metadata/tags when copying per-animation sources; serialize exclusive loop playback endpoints.
- `scripts/track_chooser.py` and its test: omit the duplicated endpoint from marked loop playback while retaining the full stored action.
- `tests/test_run_tests.py`: allow asynchronous process-tree socket teardown, retaining the incoming Windows timeout tolerance.
- `AGENTS.md`: update the incoming fractional-key guidance to reflect the tested explicit-frame helper fix.

## Verification and limits

All Blender authoring, baking, export, diagnostics, and rendering used **Blender 5.2.2 LTS** at `/workspace/.cloud-onboarding/bin/blender`. Godot is **4.7.2** at `/workspace/.cloud-onboarding/bin/godot`. The original cloud checkout lacked Game Rig Tools, so these preserved exports use Blender's native visual-bake primitive and existing `AnimationClipScene`, GLTF options, and `AnimationUpdates` helpers. Incoming main now bundles Game Rig Tools; its installer succeeded in the isolated `.cache/blender` profile after integration. The preserved animations were not rebaked after the stop instruction.

- Fast suite: `GODOT=... BLENDER=... python tests/run_tests.py --suite fast` — **10/10 passed** before and after integration. The integrated scoped suite also ran all ten fast checks successfully.
- Main integration verification: explicit fast suite **10/10 passed**; scoped runtime suite **11/11 passed**, including all 28 Merengue clips. Project-wide `godot --headless --editor --import --path .`, bounded to 600 seconds through `TestRunner.execute`, exited 0 but emitted 2,182 common-ancestor node-path errors and one missing animation node 1304 error. These project-import diagnostics remain unresolved; the Merengue runtime check passed afterward. Generated import-setting changes were restored to the staged versions. Exact logs: `merengue_checks/fast_main.txt`, `runtime_main.txt`, and `import_main.txt`.
- Integrated helper/runtime suite: **22/22 checks passed** (command below), including incoming quaternion/long-name regressions plus this task's fractional timing, asset tags, loop timing, export helpers, and all 28 Godot clips.
- Saved Blender validation was split into four scoped invocations of `test_merengue.py -- --clips ...`: the 18-clip group passed 15 clips and failed on the clockwise couple bake; the 8-clip refined group passed all eight; the transition group passed promenade and failed side-by-side skin clearance; the final group passed hand change and failed the counterclockwise couple bake. **25 unique source/GLB hash pairs passed; three failed.** Each invocation was bounded by `TestRunner.execute` (600 or 900 seconds).
- Numerical reports sample every half frame; supporting-foot position tolerance is 4 mm, foot rotation 0.03 rad, palm trajectory 18 mm, wrist bend 35 degrees, loop position 4 mm, loop rotation 0.03 rad, and loop velocity 0.12 m/s. Skin review samples phase landings, mid-beat subframes, and both loop boundaries; floor tolerance is 3 mm and support-gap tolerance 6 mm. Intentional hand contact regions use a 150 mm radius. These are sampled checks, not a continuous collision proof or a full self-collision/balance simulation.
- Godot import completed successfully. Existing invalid-UID warnings fell back to resource paths. The corrected runtime test passed all 28 clips; no runtime animation-generation step was performed after the stop request.
- Batch-start generator hashes were not captured during earlier authoring iterations. The preservation commit identifies the final generator code; asset hashes identify the saved outputs. Constraint-muted bake comparison covers sampled feet, hands, and head joints; complete deform-bone comparisons, including fingers and toes, remain pending.
- Source hashes identify the exact 25 accepted numerical samples. Shared scene SHA-256 remained `18a0f6bb84cc90426444e4bf4c81d78e3b81ebd84097a7c16afc098cd9948130` through the integrated main snapshot.

Logs are preserved in [merengue_checks/](merengue_checks/). The six existing clay images are in [merengue_previews/](merengue_previews/): closed basic, side-by-side basic, and right-underarm frames 42, 78, 102.5, and 138. The closed preview predates the last elbow-height adjustment; the side-by-side preview predates final metadata normalization. The four underarm views show the current motion. These are selected views, not complete playback approval; opposite-angle and whole-repertoire visual review remain pending.

## Processes and preserved local outputs

All owned authoring, refinement, bake/export, and render processes have finished. The in-flight verification processes were allowed to finish and their failures were recorded. No animation worker or render remains running at handoff. Current verification/setup processes are also complete.

The local scratch directory `/workspace/scratch/merengue` retains authoring diagnostics, earlier failed attempts, rendered images, logs, `preservation.patch`, and `preservation_assets.tar`. The patch/archive were safety backups before updating the task branch to current main. Durable sources, exports, scripts, reports, selected previews, and verification evidence are committed by this handoff; scratch files are supplemental and environment-local.

## Remaining work and exact resume commands

Further animation work requires a new user instruction. Preserve the three failed assets as partial until then. Resume priorities: repair the two couple bakes (the incoming `BachataDeformBake` demonstrates connected-bone/shear handling), repair side-by-side transition clearance at 48/144 and nearby subframes, then perform full multi-angle playback and hand/finger/self-clearance review. Recheck hash-matched saved sources and runtime playback after every changed asset. Complete any additional Merengue vocabulary only under a renewed scope.

Verification and setup from the app directory:

```sh
cd /workspace/sanjo-solutions/apps/a-game
export BLENDER=/workspace/.cloud-onboarding/bin/blender
export GODOT=/workspace/.cloud-onboarding/bin/godot
export BLENDER_USER_CONFIG="$PWD/.cache/blender/config"
export BLENDER_USER_SCRIPTS="$PWD/.cache/blender/scripts"
export BLENDER_USER_EXTENSIONS="$PWD/.cache/blender/extensions"
"$BLENDER" --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
python tests/run_tests.py --suite fast
python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py   --changed scripts/player_assets/test_paired_animation_authoring.py   --changed scripts/player_assets/test_single_animation_export.py   --changed scripts/player_assets/test_motion_review.py   --changed scripts/test_track_chooser.py   --changed scripts/player_assets/test_merengue.gd
python tests/run_tests.py --slow-timeout 1800 --changed scripts/player_assets/test_merengue.py
```

The final command is expected to fail on the preserved couple-right bake and rewrites reports for preceding passing clips. To inspect one known partial asset:

```sh
"$BLENDER" --threads 1 --background --python-exit-code 1   --python scripts/player_assets/test_merengue.py -- --clips open_to_side_by_side
```

After renewed authorization, these commands author or mutate animation assets:

```sh
"$BLENDER" --threads 2 --background animations/man_and_woman/share_company.blend   --python-exit-code 1 --python scripts/player_assets/merengue.py -- --clip open_to_side_by_side
"$BLENDER" --threads 1 --background animations/man_and_woman/merengue_couple_right_turn.blend   --python-exit-code 1 --python scripts/player_assets/merengue_finalize.py
```

Changing the builder is required before reauthoring the failed transition; rerunning its current recipe reproduces the preserved issue. `merengue_finalize.py` only rebakes when it detects changed foot calibration or quaternion signs; an unchanged couple source requires an explicit bake-code repair and re-export. A fresh full authoring invocation rebakes the named clip. Keep the Blender 5.2 executable and profile consistent across workers.

## Storage and Git delivery

Every new source and export is below 100 MiB and belongs in ordinary Git under the current generated root attributes. Required original LFS assets were hydrated during setup. No new task asset requires LFS upload. The manifest permits staged-blob checksum verification; run `python scripts/lfs_policy.py check` from the repository root after staging.

The task branch was fast-forwarded to current origin/main after a local patch/archive backup, then the pending task patch was applied with a three-way merge. The socket-test conflict was resolved by preserving both the task's asynchronous teardown handling and the incoming Windows tolerance. Incoming animation assets, helper fixes, shared geometry, and runtime entries were preserved. Publication uses ordinary merge/push operations and the exact Codex co-author trailer on every new commit. GitHub delivery and this status record are authored by Codex.

## Concurrent publication integration

The first preservation merge is `f6a73a1b479f54958616f42fa708fa7293520b66`. An ordinary push encountered newer remote history; the retry integrates `51c1b5ef6` and retains concurrent assets and registry entries. Incoming Asset Browser metadata copying overlapped this task’s implementation; the merged helper uses the complete field copy with duplicate-tag protection.

Incoming repository guidance requires failed exports to remain outside the active runtime catalog. The three known partial Merengue exports remain byte-for-byte preserved at their recorded paths, with proposed activation paths in `merengue_activation_draft.json`; they are excluded from the active registry. Twenty-five Merengue clips remain active. The earlier 28-clip runtime result covers the previous complete registration; the current runtime check expects the 25 active clips. This catalog-only change performs no animation authoring, baking, export, or rendering.

Retry integration checks: fast **10/10 passed**; related Blender/helper checks **21/21 passed**; runtime suite **11/11 passed**, covering all **25 active** Merengue clips. The 515-entry registry preserves all 490 incoming libraries plus 25 active Merengue libraries. Project import exited 0 with the same 2,183 error diagnostics recorded above. The 112 source/export/import/report blobs match the asset manifest. Storage-policy verification passed. Task changes pass whitespace checks; incoming historical country-swing logs retain their original trailing whitespace. Logs are saved under `merengue_checks/{fast,helpers,runtime,import}_retry.txt`.

A further ordinary-push retry integrates remote `2d0db14bd`, retaining all 566 incoming registry entries plus the 25 active Merengue entries (591 total). The task helper implementations and shared scene are unchanged from the preceding verified merge. Fast verification passed **10/10** again (`merengue_checks/fast_last.txt`); broader runtime verification remains the preceding 25-clip result.

The next retry integrates `80a3c16f7`, preserving 610 active registry entries (25 Merengue). Incoming long-action-name regressions plus all ten fast checks passed **11/11**. The earlier explicit fast invocation and broader helper/runtime results remain recorded above. See `merengue_checks/final_integration.txt`.

Publication retry integrates `d826684ea`, retaining 626 registry entries including 25 active Merengue clips. The explicit fast suite passed **10/10** (`merengue_checks/publish_retry.txt`); Merengue assets and task helpers retain their checked revisions.

Latest integration base: `58d450833`. The final registry contains 626 entries: the exact current remote catalog plus 25 active Merengue entries. This retains concurrent additions and removals, including other tasks’ quarantines. Fast checks passed **10/10** (`merengue_checks/publish_final.txt`). Merengue assets retain their checked hashes.

Latest publication retry integrates `6ac18e100`, preserving the current remote registry plus 25 active Merengue clips (640 total). Fast suite: **10/10 passed**; the final fast log is `merengue_checks/publish_final.txt`.

Final documentation/asset integration base: `db18988b4`. Task helpers, shared scene, and runtime registry retain the previously checked revisions; the registry equals remote main plus the 25 active Merengue entries. The preceding fast/helper/runtime results apply to the task changes.

The upload reached the remote but encountered a reference-lock race; ordinary retry integrates `d960a803b` and preserves its exact runtime catalog plus 25 Merengue entries (676 total). Task helper and shared-scene revisions remain unchanged. The repeated stop instruction was received; only preservation and Git delivery continued.
