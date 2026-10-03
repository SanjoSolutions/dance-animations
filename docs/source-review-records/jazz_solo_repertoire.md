# Jazz solo repertoire — stopped work preservation

Recorded October 2, 2026, 16:58 Europe/Berlin (14:58 UTC).

- Chat title/task label: Jazz solo repertoire for man_and_woman3.blend. The desktop chat's literal title was unavailable to this session.
- Project: A-Game, `/workspace/sanjo-solutions/apps/a-game`, sanjo-solutions cloud environment.
- Task branch: `codex/jazz-solo-repertoire`.
- Current commit at preservation: `fe09ef7b6a54f03909f7335d9673a27c15007d69` (the starting commit; task work was still local).
- Disposition: user-directed stop. This is a preserved procedural blocking study, with partial editable and baked assets. Production-ready Jazz animation delivery remains pending.
- The user subsequently instructed all animation chats to stop production, record exact state, commit, integrate concurrent main changes, and push. Resume authoring only after a subsequent user instruction.

## Original scope and stopping point

Create a broad, organized Jazz repertoire for independent Man and Woman solos using Blender 5.2, the repository's IK helpers, and one source file per animation. Reuse suitable existing motion; validate interpolation, foot plants, body clearance, and loops. Store binaries up to 104,857,600 bytes directly in Git. Commit animation work, fetch/rebase, update the Animation section of AGENTS.md in a separate commit, and merge/push main with the requested Codex trailers.

Preparation completed: root/app AGENTS.md and paired IK/per-animation workflow were read; Blender 5.2.2 LTS (`d13f752e3b9c`) verified; checkout-backed Player Asset Export installed; shared scene, character source files, all existing per-animation sources, and the referenced prop source downloaded through Git LFS. Existing binary sources remain unchanged. The fast-suite hair fixtures were also downloaded. Game Rig Tools was absent from this environment during authoring. Runtime GitHub credentials were used through a temporary askpass script; credential values are excluded from this record.

A 62-clip procedural catalog exists, covering positions, isolations, foundations, steps, kicks, balances, turns, jumps/leaps, and combinations. Only the 18 source files below were saved. The other 44 catalog entries are code definitions, with authoring and validation pending. `catalog_inventory.json` records every planned name, frame range, category, loop flag, and saved state. Vocabulary coverage is broad and finite; it is not an exhaustive definition of Jazz dance. The flat-foot passe turn is a preparation variant, and the chasse is a grounded practice phrase.

All 18 files contain an editable action and a matching `.baked` action, each with independent Man/Woman slots. Roles are `Man.rigify`/PLAYER and `Woman.rigify`/PARTNER; baked slots target the corresponding `.rigify_deform` objects. All saved clips are marked as loops. Timing is 24 fps; the final frame is the repeated interpolation endpoint. Solo rigs share the source origin and are intended for separate character playback. There are no paired contact requirements.

## Saved assets — all partial

The paths below are relative to `apps/a-game`. Each remains in the existing per-animation directory and references `shared_scene_data.blend`. Opening the combined library can discover these source files. Their presence and `.baked` suffix identify preserved work, not production approval.

| File | Frames | Actual bytes | State |
| --- | --- | ---: | --- |
| `animations/man_and_woman/jazz_isolation_head.blend` | 0–60 | 1,065,396 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_kick_front_left.blend` | 0–42 | 1,872,582 | Quaternion source; saved bake verification failed |
| `animations/man_and_woman/jazz_passe_turn_left.blend` | 0–120 | 4,137,148 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_contraction.blend` | 0–48 | 222,017 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_high_v.blend` | 0–48 | 222,799 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_jazz_fourth_left.blend` | 0–48 | 222,890 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_jazz_fourth_right.blend` | 0–48 | 223,088 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_jazz_l_left.blend` | 0–48 | 223,129 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_jazz_l_right.blend` | 0–48 | 221,462 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_low_v.blend` | 0–48 | 223,113 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_parallel_first.blend` | 0–48 | 221,736 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_parallel_second.blend` | 0–48 | 222,336 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_release.blend` | 0–48 | 223,547 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_rounded_first.blend` | 0–48 | 222,353 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_t_arms.blend` | 0–48 | 221,836 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_turned_out_first.blend` | 0–48 | 221,358 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_position_turned_out_second.blend` | 0–48 | 223,208 | Earlier Euler root/finger study; reauthoring required |
| `animations/man_and_woman/jazz_step_touch.blend` | 0–54 | 1,953,708 | Earlier Euler root/finger study; reauthoring required |

`jazz_solo_repertoire_evidence/asset_inventory.json` records SHA-256, exact byte count, action names, slots, key counts, ranges, loop flags, and root rotation channels for every file. Read-only loading with Blender 5.2.2 succeeded for all 18 sources. Total binary size is 12,143,706 bytes; the largest file is 4,137,148 bytes. The initial preservation commit used exact-path `.gitattributes` exceptions. During rebase, concurrent main introduced a generated size-based policy with ordinary Git as the default. That policy was retained; the Jazz-specific exceptions became unnecessary. The original before/after reports and a post-rebase attribute report are retained. There are no new LFS objects to upload for this task.

## Scripts and evidence

- `scripts/jazz_choreography.py`: 62 procedural clip specifications, sparse poses and timing. Reuses YogaPoseLibrary and GymnasticsCatalog shapes; front-kick knee poles were refined.
- `scripts/create_jazz_dance.py`: both-character proportion adjustment, RigYogaPoser IK, DiscoWristPoser wrist alignment, sparse editable channels, native deform-matrix baking, and AnimationFileWriter output. Its final version preserves quaternion control modes and orthogonalizes bake matrices around the bone Y axis. That final bake change is experimental and was interrupted during its first pilot.
- `scripts/review_jazz_dance.py`: half-frame IK reach, stationary-foot interval drift, ankle-based floor proxy, hand/torso capsule proxy, endpoint loop matching, finite-difference seam velocity, and a newly added deform-bone rotation-step check. It is a numerical screening tool; evaluated skin clearance, ergonomic review, and rendered motion review remain pending.
- `scripts/export_jazz_dance.py`: saved-file comparison of native bakes against control-rig deform bones, then rest-skeleton validation and the existing AnimationClipScene/AnimationParticipants/AnimationUpdates publication path. Export attempts stopped at the bake-verification gate. The publication path is unverified.
- `docs/animation_work_status/jazz_solo_repertoire_evidence/`: asset/catalog inventories, per-clip in-memory measurements, failed bake report, pilot/group logs, fast-suite results, partial broad-suite log, per-animation workflow regression output, and Git attribute audit. These files preserve evidence previously held in `.cache/jazz` and `/tmp/jazz-task`.

There are zero exported Jazz GLBs, zero published Jazz animation-update references, zero renders, and zero approved complete solo animations. `man_and_woman3.blend`, `shared_scene_data.blend`, character geometry, existing animation sources, skeleton signatures, and gameplay catalogs were kept intact.

## Validation results and concrete blockers

Commands ran from `apps/a-game` unless noted:

1. `python tests/run_tests.py --suite fast`: initial run 8/9 due to LFS pointer hair resources. After downloading `playground/hair/physics/*_mesh.res`, 9/9 passed. Final preservation run: **9/9 passed in 4.51 seconds**, retained as `fast_final.log`.
2. `python -m py_compile scripts/create_jazz_dance.py scripts/export_jazz_dance.py scripts/jazz_choreography.py scripts/review_jazz_dance.py`: passed after stopping production.
3. `blender --threads 1 --background --factory-startup --python-exit-code 1 --python scripts/player_assets/test_animation_files.py`: **1 test passed** in 2.425 seconds. This validates independent source saves and combined-library discovery on its temporary fixture, rather than the artistic quality of these Jazz clips.
4. All 18 saved sources were opened read-only via `bpy.data.libraries.load` using Blender 5.2.2 and inventoried successfully. These files each contain exactly the expected source/baked family and two character slots.
5. `blender --threads 1 --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/create_jazz_dance.py -- --only jazz_kick_front_left` (successive pilots) and `--group 0`, `--group 1`, `--group 2`, `--group 3`: authored partial assets. Eighteen per-clip in-memory reports passed their then-current numerical thresholds. Most reports predate the new joint-rotation continuity check. Passing in-memory results do not establish saved-file correctness. Representative step-touch results were approximately 0.216 mm maximum IK error and 0.150 mm maximum planted-foot drift, with matching endpoint poses.
6. `blender --threads 1 --background --python-exit-code 1 --python scripts/export_jazz_dance.py -- --only jazz_kick_front_left`: **failed saved-bake validation**. A first error was caused by Euler-mode authoring on shared rigs whose root and finger controls reload in quaternion mode. Seventeen preserved sources still carry that earlier Euler-mode study. The front-kick source has the quaternion correction. The next pilot exposed a front-kick knee-pole flip; the current catalog corrects its knee target. The last completed saved-bake test still measured **0.0165462176 m** maximum bone-position error at Man `DEF-foot.L`, frame **20.5**, and **0.0282952804 rad** maximum orientation error. The 0.005 m position gate failed; publication never started. The baked file remains the third pilot. The last Y-axis-preserving bake algorithm change had begun its fourth pilot when stopped; its completion and saved-bake validation are pending.
7. `python tests/run_tests.py --list` selected 9 fast and 57 slow checks, with broad Blender-source dependency triggers. `python tests/run_tests.py --slow-timeout 120` was started and then terminated during preservation. It is **incomplete**, not a passing suite. Failures included unavailable imported Godot model/animation libraries and a 120-second timeout in `test_activity_animation_methods.gd`; execution had reached `test_animation_metadata_saving.gd`. The installed Godot reports 4.6.3, while project workflow references 4.7.2. Its editor import attempt rewrote 59 `.import` files with failed-import state; those task-generated side effects were restored exactly to HEAD. See `related_tests_incomplete.log`.

The native bake implementation remains experimental because connected deform bones, inherited nonuniform scale, and shear decomposition affect the reconstructed joint positions. Game Rig Tools/Action Bakery was absent during authoring; the customary bake workflow was therefore not validated here. The latest source code and older partial binary results intentionally differ. Full evaluated-surface clearance, foot-sole geometry, wrist/finger comfort, transition choreography, render review, and successful game export remain outstanding.

## Processes and saved outputs at stop

The four authoring groups were terminated during bake debugging; their completed files and logs are preserved. At the stop instruction the owned fourth-pilot shell (PID 2209) and Blender authoring process (PID 2213) were terminated with SIGTERM. Its chained export command never began. Its `pilot4.log` and latest in-memory front-kick measurements are preserved, but its experimental bake was not saved. The broad test runner (PID 2016) and its current Godot child (PID 2300) were also terminated, preserving their partial log. Defunct exited process entries may remain until their parent reaps them. No active task-owned animation, export, rendering, or broad test process remained after preservation. The read-only inventory and focused regression checks subsequently exited successfully.

## Concurrent changes observed during integration

Fetched main `18e528c73` includes `scripts/blender/install_animation_tools.py`, the bundled Game Rig Tools fork, and the size-based `scripts/lfs_policy.py` workflow. Preserve these concurrent changes. The historical missing-add-on blocker now has a repository-provided setup path; setup and animation production were left for an authorized resumption. Main also includes `scripts/player_assets/bachata_motion.py` and its connected-joint regression, which may provide a reusable replacement for this task's experimental native baker. The `.gitattributes` conflict was resolved by retaining main's generated policy. `python scripts/lfs_policy.py check` passed for 23,417 staged files. Repeating the fast suite against the rebased tree produced **9/10 passing** in 6.73 seconds; the activity JSON check is blocked by missing Godot imports for seven newly referenced hair GLBs (`bob01`, `bob02`, `short01`–`short04`, `afro01`). See `fast_after_rebase.log`. These are integration-environment prerequisites; animation production remains stopped. Repeating `test_animation_files.py` on the rebased tree passed **2 tests in 2.813 seconds**, recorded in `animation_files_after_rebase.log`.

## Remaining work and exact resume commands

A new user instruction to resume is required. Begin by reading this status and comparing the asset hashes. Resolve saved-bake accuracy and shared rotation modes before regenerating the catalog. Retain other chats' sources and regenerate only named Jazz files. The combined/shared scene and rest-skeleton files are coordinated assets.

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender --version
# After authorization to resume, enable the tools added by concurrent main.
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
python tests/run_tests.py --suite fast
python -m py_compile scripts/create_jazz_dance.py scripts/export_jazz_dance.py scripts/jazz_choreography.py scripts/review_jazz_dance.py
blender --threads 1 --background --factory-startup --python-exit-code 1 --python scripts/player_assets/test_animation_files.py
# Inspect the existing saved front-kick bake; currently expected to fail its gate.
blender --threads 1 --background --python-exit-code 1 --python scripts/export_jazz_dance.py -- --only jazz_kick_front_left --verify-only
# After authorization and bake-code review, rerun the interrupted fourth pilot.
blender --threads 1 --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/create_jazz_dance.py -- --only jazz_kick_front_left
blender --threads 1 --background --python-exit-code 1 --python scripts/export_jazz_dance.py -- --only jazz_kick_front_left --verify-only
# After the pilot passes saved-source, baked-motion, surface, and visual review:
blender --threads 1 --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/create_jazz_dance.py
# Publishing updates is a separate step after review:
blender --threads 1 --background --python-exit-code 1 --python scripts/export_jazz_dance.py
```

`create_jazz_dance.py` writes per-animation sources and `.cache/jazz` reports and overwrites matching Jazz destinations. `--review-only` skips baking/source-file writes but still computes new motion in memory. `--group 0` through `--group 3` partition the current catalog modulo four; these are Blender processes, not delegated agents. `export_jazz_dance.py` publishes GLBs and updates `models/player/animation_updates.tres` unless `--verify-only` is supplied. Enable the newly bundled Game Rig Tools and prepare the complete imported Godot prerequisites before repeating the broader related suite; keep Blender at 5.2 for all Blender operations.

## Delivery record

This status, scripts, evidence, and measured partial assets are committed as preservation work. A separate Animation-section documentation commit follows the task commit and fetch/rebase. Integration uses freshly fetched origin/main and an ordinary history-preserving push; later chats may advance main. The final chat response records the task, documentation, and merge commit hashes and remote verification. Commit messages identify Codex authorship with exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer. GitHub interactions in this task are authored by Codex; no issue, PR, or review comment was posted.
