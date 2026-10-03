# Robot dance solos — stopped work status

Recorded 2026-10-02 15:06 UTC (Europe/Berlin: UTC+02:00).

Chat/task title: Robot dancing solo animations for `man_and_woman3.blend` (working title; the UI title was unavailable).
Project: A-Game, `apps/a-game`, sanjo-solutions cloud environment.
Branch at stop: `robot-dance-solos`.
Current commit at stop: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
Agent/commit and any GitHub communication authorship: Codex.

## Stop instruction and scope

The user explicitly stopped all animation authoring, refinement, generation, and rendering. Six owned Blender processes were terminated with SIGTERM at approximately 15:01 UTC (17:01 Berlin) on October 2, 2026. Their saved files and logs are preserved. Subsequent work consists of read-only verification, documentation, storage configuration, commits, integration, and push. Further animation work requires renewed authorization.

The original request covered a broad Robot dance repertoire for both characters, reuse of suitable existing motion, natural planted contacts and clearance, smooth transitions, interpolated and loop validation, Blender 5.2 throughout, per-animation files, Git storage up to 100 MiB, commits and rebase, Animation guidance in AGENTS.md, and integration into main. The plan defines 30 movement families per character (60 clips). This is a partial procedural choreography study, with final repertoire and visual-quality approval pending.

## Frozen outputs

37 authoring sources and 37 matching GLBs are saved: **18 man / PLAYER** and **19 woman / PARTNER**. Every saved source contains its authoring action plus a matching `.baked` action. Every saved clip uses frames **0–96 at 24 fps**, with four-second solo playback. The planned 0–192 combination and all footwork phrases remain pending. Each GLB has an adjacent `.glb.import`, and all 37 appear in `models/player/animation_updates.tres`. The original six update references are preserved.

Each source path, baked action, export path, role, byte size, SHA-256, and repair/review state appears in [robot_dance_asset_inventory.json](robot_dance_asset_inventory.json). The table below lists every saved action; source names are `animations/man_and_woman/<action>.blend`, with the exact hashed export names in that inventory.

| Action | Role | Constant-channel rebake | Latest post-rebake review |
| --- | --- | --- | --- |
| `man_robot_arm_pistons` | PLAYER | pending | pending |
| `man_robot_arm_wave_left` | PLAYER | pending | pending |
| `man_robot_arm_wave_right` | PLAYER | pending | pending |
| `man_robot_body_wave` | PLAYER | pending | pending |
| `man_robot_box_frame` | PLAYER | pending | pending |
| `man_robot_chest_pop` | PLAYER | pending | pending |
| `man_robot_elbow_hinges` | PLAYER | pending | pending |
| `man_robot_head_scan` | PLAYER | completed | pending |
| `man_robot_head_ticks` | PLAYER | completed | pending |
| `man_robot_hip_gears` | PLAYER | pending | pending |
| `man_robot_lean_left` | PLAYER | pending | pending |
| `man_robot_lean_right` | PLAYER | pending | pending |
| `man_robot_reach_grab` | PLAYER | pending | pending |
| `man_robot_ready` | PLAYER | completed | passed |
| `man_robot_rib_slide` | PLAYER | pending | pending |
| `man_robot_shoulder_pistons` | PLAYER | completed | pending |
| `man_robot_tutting` | PLAYER | pending | pending |
| `man_robot_wrist_gears` | PLAYER | pending | pending |
| `woman_robot_arm_pistons` | PARTNER | pending | pending |
| `woman_robot_arm_wave_left` | PARTNER | pending | pending |
| `woman_robot_arm_wave_right` | PARTNER | pending | pending |
| `woman_robot_body_wave` | PARTNER | pending | pending |
| `woman_robot_box_frame` | PARTNER | pending | pending |
| `woman_robot_chest_pop` | PARTNER | completed | pending |
| `woman_robot_elbow_hinges` | PARTNER | pending | pending |
| `woman_robot_head_scan` | PARTNER | completed | passed |
| `woman_robot_head_ticks` | PARTNER | completed | passed |
| `woman_robot_hip_gears` | PARTNER | completed | pending |
| `woman_robot_lean_left` | PARTNER | pending | pending |
| `woman_robot_lean_right` | PARTNER | pending | pending |
| `woman_robot_reach_grab` | PARTNER | pending | pending |
| `woman_robot_ready` | PARTNER | completed | passed |
| `woman_robot_rib_slide` | PARTNER | completed | pending |
| `woman_robot_shoulder_pistons` | PARTNER | completed | pending |
| `woman_robot_tutting` | PARTNER | pending | pending |
| `woman_robot_wall_press` | PARTNER | pending | pending |
| `woman_robot_wrist_gears` | PARTNER | pending | pending |

All 37 authoring receipts passed half-frame control sampling (193 samples per clip), supporting-foot position, wrist separation, and position/orientation/velocity loop checks during generation. These receipts describe that generation pass; they are separate from saved-file and bake verification.

11 clips completed a fresh constant-channel rebake: the first four man phrases and first seven woman phrases in generation order. Four completed the repeated independent saved-file review before termination: man ready; woman ready, head ticks, and head scan. The latest `man_review.json` and `woman_review.json` contain those four passing records. Other saved clips remain at the earlier bake state.

## Files and saved process outputs

* `scripts/player_assets/author_robot_dance.py`: planned 30-family procedural authoring script; sparse IK, flat Bezier stops, measured sole-height adjustment, calibrated wrist targets, native visual baking, and per-clip publishing. The saved script includes the later constant-channel and finger rotation-mode fixes; interrupted running generators had loaded its earlier revision.
* `scripts/player_assets/rebake_robot_dance.py`: saved-source rebake and export repair pass. Partially executed as listed above.
* `scripts/player_assets/review_robot_dance.py`: saved-source comparison of all deform bones, fractional-frame bake checks, loop and ready-pose comparisons, six evaluated-surface samples, and Blender pose-sheet rendering. Rendering was stopped; only read-only inventory verification ran afterward.
* `scripts/player_assets/validate_robot_dance.gd`: future full 60-clip import validator. Its frozen 37-clip verification copy is `robot_dance_logs/frozen_godot_validate.gd`.
* `scripts/player_assets/robot_dance/README.md`: planned vocabulary and workflow, labeled as partial.
* `scripts/player_assets/robot_dance/<action>.json`: 37 per-clip dense control-review receipts.
* `scripts/player_assets/robot_dance/man_review.json` and `woman_review.json`: interrupted latest post-rebake reports, one and three clips respectively.
* `scripts/player_assets/robot_dance/man_poses.png` and its `.import`: earlier two-pose ready-stance inspection sheet; this is a partial inspection image, not a completed repertoire contact sheet.
* `.gitattributes` in the app: exact-path regular-Git overrides for the 37 sources, 37 GLBs, and saved PNG.
* `docs/animation_work_status/robot_dance_logs/`: preserved authoring, rebake, review, test, import, inventory, storage, and diagnostic outputs.
* `docs/animation_work_status/robot_dance_asset_inventory.json`: complete frozen asset manifest with hashes.
* `docs/animation_work_status/robot_dance_solos.md`: this status record.

Owned processes at stop: authoring PIDs 2401 (man) and 2413 (woman); rebaking 3461 (man) and 3444 (woman); review/render-capable processes 3562 (man) and 3574 (woman). All terminated. The man generator had saved reach_grab and was entering wall_press; the woman generator had saved wall_press and was entering marionette. The man rebaker had saved shoulder_pistons and opened chest_pop; the woman rebaker had saved hip_gears and opened arm_pistons. In-memory poses and incomplete next operations remain unsaved. No owned authoring/render process remains active.

## Verification and blockers

* Blender 5.2.2 LTS, build d13f752e3b9c, performed all Blender authoring, baking, rendering, and binary inspection.
* `GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot python tests/run_tests.py --suite fast`: **9/9 passed after stop**; see `robot_dance_logs/fast_stop.log`.
* `python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_single_animation_export.py --changed scripts/player_assets/test_paired_animation_authoring.py --changed scripts/player_assets/test_motion_review.py`: **19/19 passed** earlier in the task; see `focused_tests.log`.
* Read-only Blender inventory using the preserved `frozen_inventory.py`: **37/37 sources reopen as action libraries**, each with exactly one authoring and baked action, correct solo role, complete matching GLB, four-second duration, and update registry reference; see `frozen_inventory.log`.
* Isolated Godot 4.7.2 import and the frozen-count GDScript validator: **37/37 imported animation libraries passed** timing, loop mode, solo track ownership, and track-count assertions. The original source and export bytes were retained. Logs: `frozen_godot_import.log`, `frozen_godot_validation.log`.
* Python source syntax compilation and `git diff --check`: passed during delivery preparation.
* Broad `python tests/run_tests.py --slow-timeout 60` was interrupted after unrelated missing-resource errors and a toy-grip editor-import timeout. It used default Godot 4.6.3 and the partially hydrated application. Test-generated unrelated modifications were restored. `related_tests.log` preserves the evidence. A complete broad suite remains outstanding.
* Game Rig Tools is absent from this cloud environment. Native Blender visual baking supplies the saved `.baked` actions; the existing project file writer, clip scene exporter, participant filter, and update publisher are reused.
* The first saved-file comparison revealed female elbow differences around 10 mm, reaching roughly 32 mm in a rib slide, in earlier cleaned bakes. A fresh bake retaining constant channels passed for the reviewed repaired files. The repair is incomplete for 26 clips; 33 clips still await the repeated full saved-file review. This is a concrete validation blocker, not a claim of completed motion quality.
* Earlier skin review found the reused male stance about 16.34 mm below floor. Saved authored sources include the measured root correction (man +0.016342841; woman +0.000139899). Reopened corrected samples clear the floor. Sampled arm/body surfaces showed zero intersections in the inspected poses; full continuous surface coverage remains pending.
* Finger closure in the saved reach_grab studies requires review because the stopped generator had loaded the earlier rotation-mode handling. The saved authoring script includes the mode-preserving revision.
* The full pose sheets, movement playback review, footwork, textures, remaining mime phrases, power cycle, and combination are pending. The repertoire remains a procedural study.

## Storage and uploads

Actual binary sizes and inherited attributes were inspected before staging. All 75 task binaries are at or below 104,857,600 bytes; the largest is 5,621,783 bytes. Exact-path app attributes select ordinary Git for these files. Other assets retain their existing storage rules. `binary_sizes.json` and `storage_attributes_before.txt` / `storage_attributes_after.txt` record the audit. New task assets require ordinary Git upload; this task introduces zero LFS objects. Existing LFS prerequisites were fetched and retained unchanged.

## Resume commands — only after renewed animation authorization

Run from `apps/a-game` in the sanjo-solutions cloud environment. Install the checkout-backed Player Asset Export loader if the Blender profile changes. The current saved files are the resume boundary; use the inventory hashes to identify this state.

```sh
blender --version
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
# Finish missing vocabulary; existing JSON receipts are resume markers.
blender --background --threads 2 animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/player_assets/author_robot_dance.py -- --resume
# Recreate the two grasp studies with the saved mode-preserving finger code.
blender --background --threads 2 animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/player_assets/author_robot_dance.py -- --only reach_grab
# Reconcile every saved source and export after all planned sources exist.
blender --background --threads 2 --python-exit-code 1 --python scripts/player_assets/rebake_robot_dance.py -- --character man
blender --background --threads 2 --python-exit-code 1 --python scripts/player_assets/rebake_robot_dance.py -- --character woman
# These two commands include rendering; run only after authorization resumes.
blender --background --threads 2 --python-exit-code 1 --python scripts/player_assets/review_robot_dance.py -- --character man
blender --background --threads 2 --python-exit-code 1 --python scripts/player_assets/review_robot_dance.py -- --character woman
GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot python tests/run_tests.py --suite fast
```

After renewed work, investigate every failing review, render and inspect complete movement sequences, and repeat the isolated Godot import using the full 60-count validator. Update exact-path storage exceptions for newly generated files after measuring their real sizes. Fetch origin/main immediately before integration and merge update-library references by path union to preserve concurrent animation tasks.

## Shared dependencies captured at stop

[robot_dance_dependencies.json](robot_dance_dependencies.json) records the actual byte sizes and SHA-256 values for the shared scene, disco seed, combined library, and both character model files used from commit `fe09ef7b6a54f03909f7335d9673a27c15007d69`. These existing dependencies remain in their established storage system. Compare their hashes before resuming against a newer shared scene. The Animation section in `AGENTS.md` records the sole, wrist, constant-bake-channel, and interrupted-work lessons.

The integration rebase reached `origin/main` at `e12670ea9`. That newer revision supplies the bundled animation-tool installer referenced in the resume commands. Game Rig Tools was absent from the original active Blender profile; tool installation and further animation work remain deferred until renewed authorization. The update-library conflict was resolved by retaining the union of existing and task library paths.

After rebase, the current fast suite passed **10/10** with Godot 4.7.2 (`fast_rebased.log`), and `python scripts/lfs_policy.py check` verified all 24,109 staged repository files (`lfs_policy.log`). All 75 task binary hashes still match the frozen audit, and every upstream animation-update path remains present.
