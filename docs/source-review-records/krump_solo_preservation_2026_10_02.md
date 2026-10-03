# Krump solo animation work preservation

Date: 2026-10-02, Europe/Berlin. Stop request received around 16:56 CEST.
Task/chat label: Krump solo animations for man_and_woman3.blend (the desktop UI title is unavailable to this executor).
Environment: sanjo-solutions cloud environment; checkout `/workspace/sanjo-solutions`.
Task branch: `codex/krump-repertoire`.
Commit at stopping point: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
This file and its assets are committed together; `git log --follow -- docs/animation_work_status/krump_solo_preservation_2026_10_02.md` identifies the preservation commit after integration.

## Instruction and scope

The original request covered a broad Krump repertoire for Man and Woman, separate solo clips, Blender 5.2 authoring/baking/export/rendering, per-animation source files, interpolated contact and loop checks, reuse of fitting existing motion, direct Git storage through 104,857,600 bytes, commits, rebase, animation documentation, merge, and push.
The subsequent instruction stopped animation authoring, refinement, generation, and rendering and prioritized preservation and delivery. The authoring process received SIGINT, completed its active saved outputs, and then received SIGTERM. The queued Woman authoring command stayed unstarted. Animation work remains stopped.

## Preserved state: partial procedural blocking studies

The catalog defines 34 movement/position studies and four combinations per character (76 intended solo clips). The disk contains **27 Man solo authoring files**, each with its matching baked action, **27 GLB exports**, and their `.glb.import` files. These are procedural blocking studies requiring further choreography and surface review. They represent a partial repertoire rather than finished coverage of Krump.

Each saved source has the authoring action matching its filename stem and one `<stem>.baked` action. Both actions have one character slot and role `PLAYER` (Man). Sources and exports cover frames **0–48 at 24 fps**, with frame 48 duplicating the opening pose; playback duration is **2 seconds** at 120 BPM. The source uses sparse control keys and initial keys for stationary controls. The native Blender visual bake samples every integer frame. Godot import settings select linear looping.

The 28th study, `krump_man_low_guard`, reached an in-memory authored action and a passing half-frame review report. Its action and bake stayed in the terminated process: **there is no saved source or GLB for low_guard**. The JSON report is evidence of that attempt, not a deliverable animation.

Woman assets and combination assets remain procedural definitions only. The full combined file, shared scene, shipped skeletons, and existing disco source retain their tracked contents. The existing combined-library discovery workflow can find the added per-animation sources.

## Exact saved animation assets

All paths in the following table are relative to `apps/a-game`. Each GLB has an adjacent `.glb.import` file. Each source has a matching `scripts/krump/reports/<source-stem>.json` half-frame report. All listed assets are authored, baked, and exported; `low_drop` has a known baked-contact failure.

| Study | Authoring source | Export | Bytes: source / GLB |
| --- | --- | --- | --- |
| `arm_circle` | `animations/man_and_woman/krump_man_arm_circle.blend` | `models/player/animation_updates/krump_man_arm_circle_baked_b817889db90b.glb` | 414,037 / 237,384 |
| `arm_swing_in` | `animations/man_and_woman/krump_man_arm_swing_in.blend` | `models/player/animation_updates/krump_man_arm_swing_in_baked_f4d140e51511.glb` | 432,081 / 239,604 |
| `arm_swing_out` | `animations/man_and_woman/krump_man_arm_swing_out.blend` | `models/player/animation_updates/krump_man_arm_swing_out_baked_cf7db9b9d450.glb` | 426,610 / 238,096 |
| `back_step` | `animations/man_and_woman/krump_man_back_step.blend` | `models/player/animation_updates/krump_man_back_step_baked_3a592b8a4874.glb` | 428,258 / 256,896 |
| `buck` | `animations/man_and_woman/krump_man_buck.blend` | `models/player/animation_updates/krump_man_buck_baked_3ae5da76e2d8.glb` | 443,068 / 262,424 |
| `chest_pop` | `animations/man_and_woman/krump_man_chest_pop.blend` | `models/player/animation_updates/krump_man_chest_pop_baked_1c0ba293222b.glb` | 437,999 / 265,640 |
| `chest_roll` | `animations/man_and_woman/krump_man_chest_roll.blend` | `models/player/animation_updates/krump_man_chest_roll_baked_010cbe3c354f.glb` | 504,791 / 270,960 |
| `diagonal_jab` | `animations/man_and_woman/krump_man_diagonal_jab.blend` | `models/player/animation_updates/krump_man_diagonal_jab_baked_7b77d8e42a89.glb` | 482,958 / 262,676 |
| `double_chest_pop` | `animations/man_and_woman/krump_man_double_chest_pop.blend` | `models/player/animation_updates/krump_man_double_chest_pop_baked_4b3b76d16932.glb` | 437,095 / 257,144 |
| `double_jab` | `animations/man_and_woman/krump_man_double_jab.blend` | `models/player/animation_updates/krump_man_double_jab_baked_18f7818308cb.glb` | 430,382 / 239,092 |
| `forward_step` | `animations/man_and_woman/krump_man_forward_step.blend` | `models/player/animation_updates/krump_man_forward_step_baked_5918a4821ea1.glb` | 428,056 / 256,332 |
| `hammer` | `animations/man_and_woman/krump_man_hammer.blend` | `models/player/animation_updates/krump_man_hammer_baked_9a6a22442759.glb` | 448,411 / 255,856 |
| `jab_left` | `animations/man_and_woman/krump_man_jab_left.blend` | `models/player/animation_updates/krump_man_jab_left_baked_ee73dd7f5eba.glb` | 495,570 / 267,860 |
| `jab_right` | `animations/man_and_woman/krump_man_jab_right.blend` | `models/player/animation_updates/krump_man_jab_right_baked_21eb20723677.glb` | 497,414 / 269,268 |
| `knee_lift_left` | `animations/man_and_woman/krump_man_knee_lift_left.blend` | `models/player/animation_updates/krump_man_knee_lift_left_baked_bb8bbce3218c.glb` | 430,882 / 256,008 |
| `knee_lift_right` | `animations/man_and_woman/krump_man_knee_lift_right.blend` | `models/player/animation_updates/krump_man_knee_lift_right_baked_d89f59c0d9b2.glb` | 428,621 / 256,012 |
| `low_drop` | `animations/man_and_woman/krump_man_low_drop.blend` | `models/player/animation_updates/krump_man_low_drop_baked_0d0136330747.glb` | 457,418 / 258,840 |
| `overhead_swing` | `animations/man_and_woman/krump_man_overhead_swing.blend` | `models/player/animation_updates/krump_man_overhead_swing_baked_39c227e2c449.glb` | 449,156 / 254,732 |
| `reach_pull` | `animations/man_and_woman/krump_man_reach_pull.blend` | `models/player/animation_updates/krump_man_reach_pull_baked_f284d4011dbc.glb` | 398,934 / 239,604 |
| `ready_bounce` | `animations/man_and_woman/krump_man_ready_bounce.blend` | `models/player/animation_updates/krump_man_ready_bounce_baked_2eccff83c099.glb` | 437,467 / 262,572 |
| `shoulder_hits` | `animations/man_and_woman/krump_man_shoulder_hits.blend` | `models/player/animation_updates/krump_man_shoulder_hits_baked_145607cc2967.glb` | 480,737 / 265,784 |
| `side_step_left` | `animations/man_and_woman/krump_man_side_step_left.blend` | `models/player/animation_updates/krump_man_side_step_left_baked_844f0c316e7c.glb` | 433,279 / 258,412 |
| `side_step_right` | `animations/man_and_woman/krump_man_side_step_right.blend` | `models/player/animation_updates/krump_man_side_step_right_baked_0dd3f85df446.glb` | 434,758 / 258,416 |
| `stomp_left` | `animations/man_and_woman/krump_man_stomp_left.blend` | `models/player/animation_updates/krump_man_stomp_left_baked_80dd063fcccb.glb` | 445,320 / 262,996 |
| `stomp_right` | `animations/man_and_woman/krump_man_stomp_right.blend` | `models/player/animation_updates/krump_man_stomp_right_baked_ca90c6398a72.glb` | 442,856 / 263,136 |
| `toe_jab` | `animations/man_and_woman/krump_man_toe_jab.blend` | `models/player/animation_updates/krump_man_toe_jab_baked_507b033bc132.glb` | 428,348 / 255,868 |
| `uppercut` | `animations/man_and_woman/krump_man_uppercut.blend` | `models/player/animation_updates/krump_man_uppercut_baked_e36040f4057e.glb` | 443,135 / 255,996 |

## Other durable task files

- `scripts/krump/choreography.py`: named movement catalog, shared ready stance, sparse poses, combinations, and categories. Definitions for pending clips describe planned procedural motion.
- `scripts/krump/author.py`: Blender 5.2-only character adaptation, control key writing, native visual baking, `AnimationFileWriter` source output, compact `AnimationClipScene` export, and `AnimationUpdates` publishing. The shared rig rotation modes are preserved and stationary rig controls receive initial keys.
- `scripts/krump/review.py`: half-frame source checks for reach, feet, hand/forearm clearance proxies, wrists, and loop endpoint/linear-velocity continuity.
- `scripts/krump/validate_assets.py`: saved source/action structure, baked skeleton comparison, baked foot drift, solo export tracks, and clip-duration checks. This was named `test_krump.py` in earlier logs; it was renamed during preservation because it is a manually invoked full-asset validator and the repository test catalog requires explicit Blender recipes for discovered tests.
- `scripts/krump/verify_import.py` and `verify_import.gd`: disposable Godot fixture using shipped character GLBs, the existing imported-root helper, and animation import script. It checks role paths, bone resolution, loop mode, and playback.
- `scripts/krump/render_review.py`: saved-source Workbench contact-sheet utility. It remains a draft review tool. Further rendering stopped on instruction.
- `scripts/krump/reports/krump_man_*.json`: 28 passing source-review reports, including report-only `low_guard`.
- `scripts/krump/reports/saved_asset_validation.json`: successful saved-asset verification for the subset recorded in its `clips` array; the failed `low_drop` case is documented in the validation log.
- `models/player/animation_updates.tres`: existing update references plus task GLB references. Concurrent animation references must be retained during integration.
- `.gitattributes` at repository root: retain the concurrent generated 100 MiB policy. The initial local commit used exact-path exceptions for 54 model binaries and one preview image; the rebase removes those redundant exceptions because current main already stores these sizes directly in Git.
- `docs/animation_work_status/krump_evidence/storage_audit.json`: actual byte counts, SHA-256 digests, and Git attributes before/after the initial scoped storage exceptions and after rebase for every task binary.
- `docs/animation_work_status/krump_evidence/chest_pop_preview.png`: one existing Blender Workbench sheet of six Man chest-pop frames (0, 10, 14, 20, 36, 48). It provides limited source-geometry inspection, not full-library visual approval.
- `docs/animation_work_status/krump_evidence/*.log`: retained authoring, bake/debug, render, fast-suite, workflow, saved-asset, and Godot verification output. Earlier failures in historical logs describe superseded attempts; final preservation results appear below.

## Validation and known limits

Blender reports **5.2.2 LTS** (`d13f752e3b9c`, build 2026-09-15). Every Blender command in this task used that executable. The Godot fixture reports 4.6.3 stable; the user version restriction concerns Blender.

- All 27 saved sources and the report-only low-guard attempt passed their live-source checks at 0.5-frame spacing (97 samples each). Checks include 4 mm planted-foot tolerance, 5 mm keyed-foot tolerance, 12 mm keyed-hand tolerance, 35-degree wrist bend, 32-degree half-frame hand rotation step, loop endpoints, and endpoint linear velocity. Clearance uses labeled proxies, not comprehensive mesh intersection checks.
- The first bake comparison revealed missing persisted finger rotation modes. The authoring pipeline now restores the shared rig's rotation modes before capturing channels, and all preserved files were regenerated with that correction.
- Native Rigify-to-deform baking has measurable pose differences, chiefly toes. The saved validator permits 25 mm joint-position difference and 0.06 radians rotation difference, while checking planted-foot movement separately against 4 mm. This broad pose tolerance does not establish exact Rigify deformation preservation.
- **Known failure:** `krump_man_low_drop` baked plant drift is **0.009093480540636627 m**, exceeding 0.004 m. Preserve the source and export as a blocking study requiring correction. The full validation run stopped at this failure; subsequent subset verification is recorded separately.
- A supplemental surface-ground probe failed when `Man.body` evaluated to an empty masked mesh. That probe established no ground-contact guarantee. The visible body comes from the anatomical mesh; future surface validation should select an evaluated mesh with geometry.
- Visual review covered the Man chest-pop sheet only. Side views, playback review, complete finger/body surface clearance, full ground-contact checks, angular loop-velocity checks, and transitions between every clip remain outstanding.
- Game Rig Tools was absent during authoring. The fetched `origin/main` commit `18e528c73` now bundles its installer; future work should use `scripts/blender/install_animation_tools.py`. The fallback uses Blender's native `bpy_extras.anim_utils.bake_action_objects`, with the existing source writer, compact scene builder, and update publisher. The combined-library full-cache export path was not initialized or exercised.
- Initial fast tests failed because three existing LFS hair meshes were pointers. Those dependencies were hydrated. A later catalog check identified the manually invoked asset validator's test naming; renaming it resolved that catalog failure.

Final preservation verification:

- `python tests/run_tests.py --suite fast`: **9/9 passed**, 2.88 seconds.
- `python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_single_animation_export.py --changed scripts/player_assets/test_animation_participants.py`: **16/16 passed** (nine fast and seven related slow checks), 20.77 seconds.
- Full `validate_assets.py` equivalent (named `test_krump.py` when the process started): **failed at low_drop** with the baked drift above. That failure remains open.
- Repeating `validate_assets.py` with all saved paths except `krump_man_low_drop.blend`: **26/26 passed**. Maximum baked plant drift in this subset: **0.003466520 m**. Maximum source-to-baked joint-position difference: **0.010501762 m**. The exact selected list is in `scripts/krump/reports/saved_asset_validation.json`.
- `python scripts/krump/verify_import.py`: **27/27 passed** for solo targets, skeleton bone resolution, linear looping, and playback. Playback success does not supersede the low-drop contact failure.
- Every preservation verification process exited. The fast/workflow/Godot/subset checks exited zero; the full saved-asset check exited one at its documented assertion.

Repeat the 26-clip subset by passing the source paths listed in `scripts/krump/reports/saved_asset_validation.json` after `--` to `validate_assets.py`.


## Processes and saved outputs

The owned animation-authoring process (PID 2303) was terminated. Its chain had been writing Man clips and would have launched Woman next. It saved `toe_jab` and `low_drop` during the interrupt handling window, then stopped while processing `low_guard`. There are no ongoing authoring or rendering processes. The preservation verification processes have finished; their exits appear above.

The exported binaries are durable in `models/player/animation_updates/`. Disposable duplicate GLBs remain under the ignored `.cache/krump/`; they match the published exports and require no additional commit. Exploratory scripts and logs under `/tmp/krump*` are ephemeral; the relevant review image and diagnostic logs are copied into the evidence directory. Rig/model LFS hydration changed local working-file availability, not tracked asset content.

## Remaining work and blockers

The current stop instruction is the blocker for further animation work. Resume animation authoring only after a subsequent user instruction authorizes it.

Pending Man files: `low_guard`, `high_guard`, `open_guard`, `blade_left`, `blade_right`, `taunt`, `body_rock`, `alternating_stomps`, `jab_swing_phrase`, `stomp_buck_phrase`, `level_change_phrase`. All 38 Woman files remain pending. Position and combination definitions are present in `choreography.py`; their procedural descriptions still need motion and surface review.

Before treating this repertoire as production-ready, correct the low-drop baked foot drift, examine deform-skeleton approximation on every clip, review actual soles and body/finger surfaces, render and inspect both actors through interpolated motion, and validate transition and loop angular velocities. Verify the source-window workflow from newly opened files and the combined library after hydration of its linked assets. Broad coverage remains open-ended because Krump has evolving freestyle vocabulary.

## Exact resume and verification commands

Run from `/workspace/sanjo-solutions/apps/a-game`. The commands below are recorded for future authorized work; authoring and rendering remain stopped at preservation.

```bash
blender --version
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
python tests/run_tests.py --suite fast
python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_single_animation_export.py --changed scripts/player_assets/test_animation_participants.py
blender -b animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/krump/validate_assets.py
python scripts/krump/verify_import.py
```

After authorization to resume animation work, first diagnose `low_drop` using its source and validation log. The current authoring command reproduces the current study; correction requires a new reviewed change before rebuilding it. Then continue from the first unsaved Man study and author Woman:

```bash
blender -b animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/krump/author.py -- --character Man --start low_guard --export
blender -b animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/krump/author.py -- --character Woman --export
blender -b animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/krump/render_review.py -- --character Man --moves chest_pop --output .cache/krump/chest_pop_review.png
```

Required hydrated inputs are `animations/man_and_woman/solo_disco_dance.blend`, `animations/man_and_woman/shared_scene_data.blend`, `man_anatomical_study.blend`, and `woman_anatomical_study_speculum.blend`; the Godot fixture also needs `models/player/man.glb` and `models/player/woman.glb`. Use the configured `SANJO_GITHUB_LFS_TOKEN` through the authorized proxy for LFS operations, keeping credential values out of logs. The first plain `git lfs pull` failed for missing interactive credentials; the task's process-local Basic authorization header successfully hydrated the required inputs.

## Storage and delivery

The **55 binary files** total **20,505,468 bytes**. The largest is **1,560,219 bytes**. All belong directly in Git under the user's 104,857,600-byte rule; the storage audit records the initial exact-path exceptions and their removal in favor of the concurrent generated repository policy. There are no task-created LFS objects requiring a separate upload. The current generated LFS policy and concurrent assets stay intact.

Commit this status file and all durable task outputs together. Fetch `origin`, rebase the task branch onto current `origin/main`, add the requested workflow observations under `# Animation` in `AGENTS.md` in a separate commit, then integrate into `main`. Fetch immediately before integration, retain concurrent update-library references and other animation paths, retry ordinary push rejection by integrating newer main, and verify that both task commits are ancestors of remote main. Use exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer per new commit. GitHub-facing commit and merge messages identify Codex as the author of the communication. Final commit and remote verification hashes are delivered in chat to avoid a self-referential hash inside this commit.

Integration note: the first rebase onto `18e528c73` conflicted only in `.gitattributes`. The concurrent generated policy was retained. Task binary blob sizes and checksums remained unchanged.

Post-rebase verification: the updated fast suite passed **10/10 checks** in 6.08 seconds. SHA-256 comparisons confirmed that `shared_scene_data.blend`, `man_anatomical_study.blend`, and `woman_anatomical_study_speculum.blend` retain the exact dependency content used for the preserved checks. `python scripts/lfs_policy.py check` passed for all 23,487 staged files at rebase. Workflow observations were added under `# Animation` in `AGENTS.md` in the separate documentation commit.
