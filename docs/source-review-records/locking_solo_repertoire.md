# Locking solo repertoire — preserved partial work

Date: 2026-10-02T17:06:57+02:00 (Europe/Berlin).
Task/chat title: Locking solo animations for man_and_woman3.blend (descriptive task title; the sidebar title is unavailable to this executor).
Task branch: `codex/locking-solo-repertoire`.
Commit at stop: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
Coordinating chat: `01a0fd1a-3673-7683-ae29-577f2ee1a927`.

The user explicitly stopped animation work across the running animation chats. The owned full-generation process (PID 2274) received SIGTERM. Its outputs are preserved. All later Blender calls read existing assets for verification. This snapshot contains **15 authored/baked sources and 14 exports**, from a **90-clip procedural catalog (45 per character)**. The repertoire is partial. Treat these as procedural blocking studies pending choreography, surface-clearance, and playback review, rather than a finished Locking library.

## Original scope and stopping point

Create broad Locking moves, positions, transitions, and solo animations for both characters in A-Game, using Blender 5.2 and the existing individual-animation source workflow. Reuse compatible animation helpers; check natural motion, contacts, clearance, interpolated poses and loops; store binaries through 104,857,600 bytes directly in Git; commit assets, fetch/rebase, document animation lessons in AGENTS.md, merge main, upload assets, push, and verify the remote.

Blender **5.2.2 LTS**, build `d13f752e3b9c`, performed all authoring, scripting, baking, rendering and GLB export. The existing `DiscoCharacter`, `DiscoWristPoser`, `RigYogaPoser`, calibrated palm IK solver, `AnimationFileWriter`, `AnimationClipScene`, and `AnimationUpdates` are reused. The combined `man_and_woman3.blend`, shared scene, anatomy libraries and existing animations retain their saved contents. Per-animation descriptors point to `shared_scene_data.blend` for scene composition.

The last full run stopped after saving `locking_man_high_point_left.blend`, including its authoring and baked actions, and before publishing its GLB. Its half-frame source check passed in the interrupted log. Its bake/export fidelity gate and export remain pending. The prior six-clip pilot produced the man and woman lock, clap and jazz-split sources and exports. The full run then published nine man clips; one overlaps that pilot, for fourteen unique exports. No owned authoring/render process remains running.

## Saved assets

Every source below contains its named authoring action and matching `.baked` action, one character slot per action, explicit solo participant metadata, a shared-scene descriptor and loop endpoints. All saved clips use **24 fps** and loop. PLAYER means the man; PARTNER means the woman. The end frame duplicates the starting pose. The adjacent `.glb.import` of every listed export configures the animation-library importer and loop flag.

| Clip | Role | Inclusive frame range | Authored and baked source, relative to app | Export, relative to app |
| --- | --- | --- | --- | --- |
| `locking_man_clap` | PLAYER | 0–78 | `animations/man_and_woman/locking_man_clap.blend` | `models/player/animation_updates/locking_man_clap_baked_9625f83c3e6e.glb` |
| `locking_man_double_lock` | PLAYER | 0–78 | `animations/man_and_woman/locking_man_double_lock.blend` | `models/player/animation_updates/locking_man_double_lock_baked_b475adb0f27c.glb` |
| `locking_man_funk_groove` | PLAYER | 0–60 | `animations/man_and_woman/locking_man_funk_groove.blend` | `models/player/animation_updates/locking_man_funk_groove_baked_c210321b9119.glb` |
| `locking_man_high_point_left` | PLAYER | 0–60 | `animations/man_and_woman/locking_man_high_point_left.blend` | **Pending export** |
| `locking_man_high_point_right` | PLAYER | 0–60 | `animations/man_and_woman/locking_man_high_point_right.blend` | `models/player/animation_updates/locking_man_high_point_right_baked_0a5e4cc806ac.glb` |
| `locking_man_jazz_split` | PLAYER | 0–96 | `animations/man_and_woman/locking_man_jazz_split.blend` | `models/player/animation_updates/locking_man_jazz_split_baked_0018b8d7573b.glb` |
| `locking_man_lock` | PLAYER | 0–60 | `animations/man_and_woman/locking_man_lock.blend` | `models/player/animation_updates/locking_man_lock_baked_ff737d62b9b0.glb` |
| `locking_man_low_point_left` | PLAYER | 0–60 | `animations/man_and_woman/locking_man_low_point_left.blend` | `models/player/animation_updates/locking_man_low_point_left_baked_ec92905b644c.glb` |
| `locking_man_low_point_right` | PLAYER | 0–60 | `animations/man_and_woman/locking_man_low_point_right.blend` | `models/player/animation_updates/locking_man_low_point_right_baked_1ebcbb03096d.glb` |
| `locking_man_point_left` | PLAYER | 0–60 | `animations/man_and_woman/locking_man_point_left.blend` | `models/player/animation_updates/locking_man_point_left_baked_d33b8e626712.glb` |
| `locking_man_point_right` | PLAYER | 0–60 | `animations/man_and_woman/locking_man_point_right.blend` | `models/player/animation_updates/locking_man_point_right_baked_57d575865fc6.glb` |
| `locking_man_up_lock` | PLAYER | 0–60 | `animations/man_and_woman/locking_man_up_lock.blend` | `models/player/animation_updates/locking_man_up_lock_baked_029722cc1810.glb` |
| `locking_woman_clap` | PARTNER | 0–78 | `animations/man_and_woman/locking_woman_clap.blend` | `models/player/animation_updates/locking_woman_clap_baked_dccdc133c466.glb` |
| `locking_woman_jazz_split` | PARTNER | 0–96 | `animations/man_and_woman/locking_woman_jazz_split.blend` | `models/player/animation_updates/locking_woman_jazz_split_baked_81d7d3c388a6.glb` |
| `locking_woman_lock` | PARTNER | 0–60 | `animations/man_and_woman/locking_woman_lock.blend` | `models/player/animation_updates/locking_woman_lock_baked_4200d52b4dad.glb` |

`models/player/animation_updates.tres` references the fourteen exports. The first rebase preserved all 18 current-main references, including concurrent cha-cha clips, and added the fourteen Locking references for 32 total. Later integration continues to preserve concurrent additions by resource path and regenerates resource IDs.

## Code and evidence inventory

* `scripts/locking_choreography.py`: 45 per-character recipes grouped into foundations, gestures, footwork, floor accents, positions, transitions and showcase. Most catalog entries have yet to produce saved assets. `locking_solo_repertoire/assets.json` lists all 75 outstanding source names.
* `scripts/create_locking.py`: sparse IK keys, single initial keys for stationary channels, proportional posing, finger settings, calf/foot lift during turns, calibrated clap targets, half-frame checks, native visual baking, individual file writing and GLB publication. It currently overwrites the validation JSON when starting a run. Interrupted runs preserve only the completed entries from that run.
* `scripts/locking_validation.json`: incremental **nine-clip** report from the interrupted full run. Each recorded clip passed; the aggregate `passed` field is absent because the run ended early. The earlier pilot's validation evidence is in its separate log.
* `scripts/player_assets/test_locking.py`: full-repertoire completion verification. Its current failure correctly identifies the incomplete catalog/report.
* `scripts/player_assets/verify_locking_snapshot.py`: read-only verification of saved source families, roles, frame ranges, source loop channels, export isolation, exported timing/loops and update-library references. It writes the preservation inventory JSON, rather than authoring or exporting animations.
* `docs/animation_work_status/locking_solo_repertoire/assets.json`: exact source/export/import paths, roles, ranges, byte sizes, SHA-256 checksums, verification results and remaining source names.
* `docs/animation_work_status/locking_solo_repertoire/interrupted_build.log`: current full-run output through the high-point-left source check.
* `docs/animation_work_status/locking_solo_repertoire/completed_pilot.log`: successful six-clip pilot, including both characters' lock, clap and jazz split.
* `docs/animation_work_status/locking_solo_repertoire/snapshot_verification.log`: saved-asset verification output.
* `docs/animation_work_status/locking_solo_repertoire/fast_tests.log` and `related_tests.log`: verification after the stop instruction.
* `docs/animation_work_status/locking_solo_repertoire/storage_audit.json`: measured sizes and effective Git attributes for all 32 new binaries.
* `docs/animation_work_status/locking_solo_repertoire/man_point_left_review.png`, `woman_clap_review.png`, and `woman_jazz_split_review.png`: existing Blender workbench review stills preserved after the stop; these show blocking poses, rather than completed motion reviews.
* Root `.gitattributes`: concurrent main introduced a generated size-based policy through `scripts/lfs_policy.py`. Rebase retained that policy; ordinary Git is its default for these 15 blends, 14 GLBs and three PNGs, so the task's earlier exact-path overrides became unnecessary. Maximum saved binary: **610,968 bytes**. The measured 32 binaries all fit ordinary Git. This task introduces zero LFS objects and requires no new LFS uploads.

Temporary exploratory scripts and historical logs remain under `/tmp/locking/`; they are session-local scratch work. Current useful evidence and render outputs are copied into the committed status directory. `.cache/player_assets/locking_review.json` is an exploratory partial report. The durable incremental report and the two authoring logs above establish the saved snapshot. No pending temporary export was present at the stop inventory.

## Verification and limits

Commands run from `apps/a-game` after stopping:

```sh
python tests/run_tests.py --suite fast
# 9/9 passed, 2.95 seconds.

python tests/run_tests.py --changed scripts/create_locking.py --changed scripts/locking_choreography.py --changed scripts/player_assets/test_locking.py
# 9/10 passed, 3.55 seconds. The full-repertoire test fails at the expected-name assertion.

blender --background --factory-startup --python-exit-code 1 --python scripts/player_assets/verify_locking_snapshot.py
# PASS: 15 readable authored/baked sources, 14 isolated solo exports;
# saved roles, ranges, GLB timing, loop endpoints and references verified.
```

The required fast suite initially encountered three LFS pointer resources under `playground/hair/physics/`. Hydrating those resources resolved the environment prerequisite; the final fast suite passes. The broad default selector lists 186 slow checks because shared update-library references reach many app scenes. The commands above use the runner's explicit task-source scope, selecting the new asset verification plus the fast set. The complete 186-check integration set remains outstanding.

The nine incremental entries passed actual evaluated half-frame checks: IK hand and foot reach, planted-foot drift, wrist bend, hand separation, a torso-capsule clearance proxy, toe height, maximum sampled endpoint displacement, loop position/orientation/velocity and applicable palm contacts. Their maximum bake skeleton position errors are below 0.000004 meters. The successful pilot asserts the same 0.002-meter bake-fidelity limit, with sampled source checks recorded in its log. These are skeletal/proxy checks, rather than a complete mesh self-intersection test. Export loop verification compares actual GLB sampler endpoints, with quaternion sign equivalence.

A native-bake discrepancy was corrected in the pilot: connected deform joints and copied nonuniform scale caused toe offsets. The task-specific baker uses a temporary copied deform armature with free joint translations and native COPY_LOCATION/COPY_ROTATION sampling, preserving rest matrices and parent names. It writes only action files and exports; it saves the original shared rig file contents intact. Game Rig Tools was absent from the initial authoring environment, so the script uses Blender 5.2's native `bpy_extras.anim_utils.bake_action` through the same individual-source/publication helpers. Future re-export must retain this tested bake behavior or establish equivalent fidelity through Action Bakery.

## Remaining work and concrete blockers

1. The user stop instruction is the active authorization boundary for further animation authoring, refinement, generation or rendering. Resume animation work after an explicit user request.
2. Author/bake/export the 75 catalog entries listed in `assets.json`; export the existing man high-point-left source after its bake comparison succeeds. Reconcile retained pilot entries into a complete final validation report.
3. Review these procedural studies as choreography. The point review shows the head turning away from the pointing side: inspect the `head_turn` signs in point/high-point recipes and their mirrors. The split is a moderate seated/folded-leg blocking pose that needs dance-form review. Footwork recipes share broad motion structures and require move-specific refinement and musical playback review. The catalog represents broad coverage, rather than an exhaustive enumeration of all Locking traditions and variations.
4. Finish evaluated surface and finger clearance checks, biomechanical weight-transfer review, floor support and knee contacts, then inspect full motion and transitions in Blender. Three stills and skeletal proxies cover only part of that work. In particular, the arm/torso proxy describes wrists and a torso capsule, rather than every limb surface.
5. Test Godot import, actual playback track binding and loop settings for each published GLB. The preservation check establishes valid GLB content and intended `.import` settings; it does not establish the completed Godot integration or gameplay activation.
6. Newly fetched guidance identifies additional saved-playback concerns: Rigify finger controls use quaternion rotation modes, while this generator sets temporary finger controls to Euler mode; source actions alone retain channels rather than that rig setting. The generator also clears control-rig animation data between clips, which can remove drivers. Native NLA playback showed a stationary reference during bake investigation; direct action assignment bypassed that reference for the numerical comparison. Fresh-process native NLA movement, finger-mode compatibility, and driver retention therefore require investigation after renewed authoring authorization. The current snapshot verifier checks stored data and GLB content, rather than proving those playback behaviors. Current main now bundles Game Rig Tools; read `scripts/blender/README.md` before resuming.
7. The full-catalog verification remains red until all 90 clips and the aggregate validation report are complete. Preserve this expected distinction while delivering the requested partial snapshot.

## Exact resume commands

The following commands describe future work; authoring/rendering commands were stopped on the user's instruction. Start in this checkout with Blender 5.2.2 on PATH and the listed shared LFS assets hydrated.

```sh
cd /workspace/sanjo-solutions/apps/a-game
blender --version
# Expect Blender 5.2.x.

# Read-only snapshot verification:
blender --background --factory-startup --python-exit-code 1 --python scripts/player_assets/verify_locking_snapshot.py

# After renewed authoring authorization, isolate the unfinished exported clip:
blender -b -t 2 animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/create_locking.py -- --moves high_point_left --characters man
# This overwrites its source/export and starts a fresh incremental report.

# Rebuild the catalog after choreography review and necessary refinements:
blender -b -t 2 animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/create_locking.py

# Validate the complete report and persisted assets:
python tests/run_tests.py --suite fast
python tests/run_tests.py --changed scripts/create_locking.py --changed scripts/locking_choreography.py --changed scripts/player_assets/test_locking.py
```

Shared prerequisites: `animations/man_and_woman/shared_scene_data.blend`, `man_anatomical_study.blend`, `woman_anatomical_study_speculum.blend`, and `dildo.blend` (a shared scene dependency). The hydrated combined library, idle and disco sources were inspected as references. Maintain the per-animation file workflow and measured-size storage rules during resumption.

## Integration notes

The task snapshot was committed as `abdb748fd` and rebased onto `origin/main` at `e12670ea9`, producing task commit `d78c4d030`. Conflicts in the generated storage policy and animation-update registry were resolved by retaining current-main policy and all current-main clip references plus this task's fourteen exports. `python scripts/lfs_policy.py check` passed for 23,989 staged files. The original logs above remain the pre-integration record; `integration_fast_tests.log` and `snapshot_after_rebase.log` record fresh verification: the updated fast suite passed **10/10 in 5.90 seconds**, and snapshot verification again passed for all fifteen sources and fourteen exports. Animation work remained stopped throughout integration.

Final integration fetched `origin/main` at `391093e0a` immediately before merging. It preserved all 288 current-main animation references and added fourteen Locking exports for 302 references. Both sides' animation-guidance additions remain present. The final fast suite passed **10/10 in 6.12 seconds**; the saved snapshot verification passed again. See `final_fast_tests.log` and `final_snapshot_verification.log`. The full-repertoire completion gate remains intentionally outstanding for the stopped work.

The first ordinary push encountered concurrent main advancement. The retry integrated `origin/main` at `4adaa35c0`, preserving its 517 animation references plus the fourteen Locking exports (531 total). `retry_fast_tests.log` and `retry_snapshot_verification.log` record verification of that integration.

A further concurrent integration preserved `origin/main` at `ffda2f90801565c97278c80fecf5bd6dd54b7231`. `delivery_fast_tests.log` and `delivery_snapshot_verification.log` record passing fast and saved-snapshot verification. Authoring remained stopped.

A further concurrent integration preserved `origin/main` at `58d450833f7cb8dd7d13e84313ae24baaa6fb512`. `delivery_fast_tests.log` and `delivery_snapshot_verification.log` record passing fast and saved-snapshot verification. Authoring remained stopped.

## Delivery record

This status is committed with the task's durable assets and code. Subsequent integration uses a fresh `origin/main`, preserves concurrent clip references and exact-path attributes, and uses ordinary history-preserving pushes. The final chat response records the task/documentation/merge hashes and verified remote main, which become known after this file's recording commit. Every task-created commit carries exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer. GitHub task communication is authored by Codex.
