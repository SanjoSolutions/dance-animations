# Breaking animation preservation checkpoint

Date: 2026-10-02. Chat: **Create Breaking dance animations** (`01a0fd02-c0bd-75cd-bc30-b041269f6050`). Project: A-Game, `apps/a-game`, sanjo-solutions cloud environment. Branch at stop: `codex/breaking-repertoire`. Current commit at stop: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.

The user stopped all animation work and prioritized preserving the present state. Authoring, refinement, generation, baking, export, and rendering stopped. Subsequent work comprises recording, read-only asset inspection, repository verification, commits, and delivery. **Every saved Breaking clip is a partial procedural blocking study.** Production motion quality and bake fidelity remain open. This checkpoint does not claim a completed Breaking repertoire.

## Original scope and completed preparation

Create a broad organized Breaking repertoire for both solo characters in `man_and_woman3.blend`, reuse suitable existing work, use Blender 5.2 throughout, validate planted contacts, interpolated clearance and loops, follow per-animation authoring/baked source workflow, commit/rebase, document findings, merge and push. Breaking has an open-ended vocabulary; the procedural catalog covers 38 named studies rather than every possible variation.

Read repository instructions and the player asset authoring workflow. Verified actual Blender **5.2.2 LTS**, selected `/home/agent/.local/bin/blender`, and hydrated existing shared scenes, linked anatomical sources, player models, existing animation updates, and hair physics resources through Git LFS. The standard Game Rig Tools addon was unavailable during authoring; an experimental native Blender bake path was attempted. Godot verification uses `/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot` (the default command resolves to 4.6.3).

`scripts/breaking/catalog.py` defines the 38 studies from the existing yoga pose vocabulary. `scripts/breaking/author.py` reuses `WorkoutPoser`, `YogaPoseLibrary`, `DiscoWristPoser`, `AnimationFileWriter`, `AnimationClipScene`, and `AnimationUpdates`. Reuse concerns existing calibrated pose/IK/export infrastructure; existing dance actions were not relabeled wholesale. `scripts/breaking/preview.py` is the interrupted preview helper. All three scripts are preserved at their stopping point.

## Saved versus evaluated state

* Man: **37 authored sources, 37 baked actions, 37 exported GLBs**. Each source contains its authoring action and matching `.baked` action. Slots target `OBMan.rigify` and `OBMan.rigify_deform`; role is `PLAYER`. Native bake fidelity remains uncertified.
* Woman: **zero saved sources, zero saved baked actions, zero exports**. All 38 procedural poses were created and evaluated in memory during an earlier review; 37 passed that review's limited checks. The process exited, so those actions survive only as procedural code and reports.
* Two-step: neither character has a saved source or export. The earlier full reviews failed its ankle clearance check. The latest isolated Man review passed after a procedural adjustment, but it was review-only and saved no animation asset. Woman's corresponding adjustment remains unverified.
* The current authoring script includes changes made after the 37 Man assets were saved. These assets represent an earlier build and must not be treated as regenerated from the final script.
* Before preservation, `models/player/animation_updates.tres` contained 37 published study references. After rebasing, updated repository guidance required isolating stopped exports: their byte-identical GLBs and import settings now live in `docs/animation_work_status/breaking_repertoire/exports/`, under `.gdignore`, and only their 37 provisional registry references were removed. All concurrent runtime references are preserved. Editable Blender sources retain the required per-animation workflow location.
* Shared scene data, the combined Blender scene, and anatomical character source geometry remain unchanged by this task.

Catalog: Toprock — basic rock, Indian step, salsa step, cross step, side step, kick step. Footwork — six-step, three-step, two-step, CC, kick-out, left/right coffee grinder, knee rock. Freezes — turtle, left/right baby, left/right chair, handstand, headstand, L-sit. Power — backspin, headspin, handglide, windmill, flare, swipe. Transitions — stand-to-squat, squat-to-support, support-to-baby, baby-to-support, support-to-squat, squat-to-stand, support-to-crab, crab-to-support. Drops — left/right hook drop.

## Exact assets and ranges

All frames use 24 fps and solo `PLAYER`. The table links each saved source and export; each export also has the adjacent `.glb.import` settings file. [saved_assets.json](breaking_repertoire/saved_assets.json) records every exact source/export/import path, byte size, SHA-256, action family, entry/exit, authored key frames, curve/channel counts, and loop flag.

| Study | Category | Frames | Loop | Source | Export |
| --- | --- | --- | --- | --- | --- |
| baby_to_support | Transitions | 0–40 | one-shot | [blend](../../animations/man_and_woman/breaking_man_baby_to_support.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_baby_to_support_baked_3f38e0d8d191.glb) |
| backspin | Power | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_backspin.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_backspin_baked_3721edfca667.glb) |
| basic_rock | Toprock | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_basic_rock.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_basic_rock_baked_7ac403cbf652.glb) |
| cc | Footwork | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_cc.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_cc_baked_0636781287ca.glb) |
| coffee_grinder_left | Footwork | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_coffee_grinder_left.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_coffee_grinder_left_baked_bb259e4c4278.glb) |
| coffee_grinder_right | Footwork | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_coffee_grinder_right.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_coffee_grinder_right_baked_083727c47286.glb) |
| crab_to_support | Transitions | 0–40 | one-shot | [blend](../../animations/man_and_woman/breaking_man_crab_to_support.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_crab_to_support_baked_fc0f210b5f25.glb) |
| cross_step | Toprock | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_cross_step.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_cross_step_baked_41be642c1a86.glb) |
| flare | Power | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_flare.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_flare_baked_060377b6a499.glb) |
| freeze_baby_left | Freezes | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_freeze_baby_left.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_freeze_baby_left_baked_d40c5b96bc79.glb) |
| freeze_baby_right | Freezes | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_freeze_baby_right.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_freeze_baby_right_baked_3dbee90dfc50.glb) |
| freeze_chair_left | Freezes | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_freeze_chair_left.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_freeze_chair_left_baked_3f27997b33d8.glb) |
| freeze_chair_right | Freezes | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_freeze_chair_right.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_freeze_chair_right_baked_3872d3492c21.glb) |
| freeze_handstand | Freezes | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_freeze_handstand.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_freeze_handstand_baked_e9653069d9df.glb) |
| freeze_headstand | Freezes | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_freeze_headstand.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_freeze_headstand_baked_6c0e950619e3.glb) |
| freeze_l_sit | Freezes | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_freeze_l_sit.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_freeze_l_sit_baked_ce62500944a4.glb) |
| freeze_turtle | Freezes | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_freeze_turtle.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_freeze_turtle_baked_b36cc50794fe.glb) |
| handglide | Power | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_handglide.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_handglide_baked_62b2ec912600.glb) |
| headspin | Power | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_headspin.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_headspin_baked_0b235acde6de.glb) |
| hook_drop_left | Drops | 0–40 | one-shot | [blend](../../animations/man_and_woman/breaking_man_hook_drop_left.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_hook_drop_left_baked_9d5c96b1cf96.glb) |
| hook_drop_right | Drops | 0–40 | one-shot | [blend](../../animations/man_and_woman/breaking_man_hook_drop_right.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_hook_drop_right_baked_30a3e2ac2659.glb) |
| indian_step | Toprock | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_indian_step.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_indian_step_baked_81d539d68dac.glb) |
| kick_out | Footwork | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_kick_out.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_kick_out_baked_1a7f409884fd.glb) |
| kick_step | Toprock | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_kick_step.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_kick_step_baked_09aaccb54e03.glb) |
| knee_rock | Footwork | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_knee_rock.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_knee_rock_baked_81feee6e7722.glb) |
| salsa_step | Toprock | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_salsa_step.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_salsa_step_baked_e371f211a1d0.glb) |
| side_step | Toprock | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_side_step.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_side_step_baked_5211687784da.glb) |
| six_step | Footwork | 0–72 | yes | [blend](../../animations/man_and_woman/breaking_man_six_step.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_six_step_baked_d73f77dcb267.glb) |
| squat_to_stand | Transitions | 0–40 | one-shot | [blend](../../animations/man_and_woman/breaking_man_squat_to_stand.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_squat_to_stand_baked_e6ee8a26ab38.glb) |
| squat_to_support | Transitions | 0–40 | one-shot | [blend](../../animations/man_and_woman/breaking_man_squat_to_support.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_squat_to_support_baked_3d8763b18b74.glb) |
| stand_to_squat | Transitions | 0–40 | one-shot | [blend](../../animations/man_and_woman/breaking_man_stand_to_squat.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_stand_to_squat_baked_3bf929b3be28.glb) |
| support_to_baby | Transitions | 0–40 | one-shot | [blend](../../animations/man_and_woman/breaking_man_support_to_baby.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_support_to_baby_baked_056a1b9339b8.glb) |
| support_to_crab | Transitions | 0–40 | one-shot | [blend](../../animations/man_and_woman/breaking_man_support_to_crab.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_support_to_crab_baked_bd4e1746f45d.glb) |
| support_to_squat | Transitions | 0–40 | one-shot | [blend](../../animations/man_and_woman/breaking_man_support_to_squat.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_support_to_squat_baked_a76365d26bf0.glb) |
| swipe | Power | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_swipe.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_swipe_baked_c307d1741066.glb) |
| three_step | Footwork | 0–36 | yes | [blend](../../animations/man_and_woman/breaking_man_three_step.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_three_step_baked_3000e0facc13.glb) |
| windmill | Power | 0–48 | yes | [blend](../../animations/man_and_woman/breaking_man_windmill.blend) | [GLB](../../docs/animation_work_status/breaking_repertoire/exports/breaking_man_windmill_baked_70b2959123ad.glb) |

The unsaved two-step study is intended for frames 0–24. Saved six-step spans 0–72, three-step 0–36, remaining loops 0–48, and transitions/drops 0–40. These authoring labels describe intended vocabulary; power studies require specialist visual review for recognizable technique and physically credible support.

## Validation and concrete blockers

Before stopping, the procedural review sampled half frames and the loop boundary at 0.05-frame offsets. It checked evaluated body floor height (minimum −0.003 m), IK reach error (maximum 0.005 m), declared planted contact translation (0.002 m) and rotation (0.03 rad), selected hand/chest and ankle clearance proxies, loop endpoint translation (0.002 m), endpoint angle (0.03 rad), and boundary linear velocity (0.35 m/s). Wrist deltas were logged. These checks cover selected proxies, not exhaustive mesh self-intersection, angular velocity, center of mass, or every transition pairing.

Earlier full Man and Woman reports each show 37/38 passes, with two-step failing. The isolated latest Man two-step review passes with ankle proxy gap about 0.0393 m and IK error about 0.000120 m. The reports predate some later edits and are not final certification of the saved assets.

A subsequent basic-rock authoring-versus-native-bake diagnostic measured **0.008418681525469403 m position error** and **0.008679884485900402 rad angle error**, with the worst position on `DEF-toe.L` at frame 36. The attempted correction currently stops at `bone.use_connect = False` in `scripts/breaking/author.py` because `Bone.use_connect` is read-only. This unfinished change remains preserved. A future repair must use a valid edit-bone/copied-rig approach or the repository's standard baking addon, preserve the required skeleton, and verify evaluated matrix fidelity. Raising tolerances to conceal the discrepancy is not a repair.

Read-only saved-file inspection with Blender 5.2.2 passed for all 37 source/export pairs: two matching actions, solo role/slots, one matching GLB animation and expected duration, and absence of Woman nodes. This verifies structure, not motion fidelity. See [saved_assets_verification.log](breaking_repertoire/saved_assets_verification.log) and the accompanying inspector.

Fast suite: **9/9 passed in 3.17 s**. An earlier run using the default Godot and incomplete asset hydration failed; the recorded final run uses Godot 4.7.2 and hydrated hair physics resources. The related selection contained 9 fast and 57 slow checks. The run was interrupted after repeated environment failures; its exact partial counts appear in Delivery verification. Missing Godot imported resources and class dependencies are environment blockers; failures are preserved rather than represented as passes.

## Preserved diagnostics and processes

The task had no running authoring, baking, export, or rendering process when preservation began. The subsequent verification runner used a 60-second timeout per slow test and was deliberately interrupted with SIGINT after repeated prerequisite failures. It exited 130; saved diagnostic output remains intact.

Durable evidence under `docs/animation_work_status/breaking_repertoire/`:

* `man_review.json`, `woman_review.json`: earlier full 38-study numerical reviews.
* `man_build.log`: the build that saved 37 Man sources/exports and failed overall on two-step.
* `man_final.log`, `bake_diagnostic.log`, `bake_diagnostic2.log`: later bake fidelity failure and unfinished read-only-property correction.
* `two_step_pilot.log`, `woman_pilot2.log`: isolated latest Man two-step review and earlier full Woman review.
* `man_sheet_1.png`, `man_six_step_12.png`: pre-stop clay snapshots only. Limited earlier pose views; no final full-motion playback review was completed. The older Workbench preview attempt failed EGL initialization; Cycles CPU produced these saved images.
* `inspect_saved_assets.py`, `saved_assets.json`, `saved_assets_verification.log`: read-only structural verification and exact asset inventory.
* `fast_tests.log`, `related_tests.log`: repository verification output.
* `storage_inventory.json` and task-scoped `.gitattributes` files: actual sizes and before/after storage attributes.

The ignored `.cache/breaking/` directory retains scratch review JSON files, diagnostic scripts/logs, intermediate export and previews in this checkout. Durable evidence is copied above; scratch paths are optional convenience, not required source assets. Test-generated unrelated import/resource edits are restored to their pre-test state before committing.

All 76 new binary files (37 blend, 37 GLB, two PNG) total **20,620,215 bytes**; the largest is **2,106,703 bytes**. Each is below 104,857,600 bytes and uses ordinary Git through exact-filename attribute exceptions. Existing unrelated LFS rules remain intact. No new task asset requires a separate LFS upload; ordinary Git push delivers the preserved binaries. The staged Git blob sizes are checked against the working files before committing.

## Verification and future resume commands

Run from `/workspace/sanjo-solutions/apps/a-game`:

```sh
BLENDER=/home/agent/.local/bin/blender
GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot
export BLENDER GODOT
python tests/run_tests.py --suite fast
python tests/run_tests.py --suite changed --changed animations/man_and_woman/breaking_man_basic_rock.blend --slow-timeout 60
"$BLENDER" --background --factory-startup --python-exit-code 1 --python docs/animation_work_status/breaking_repertoire/inspect_saved_assets.py
```

**Animation work resumes only after a new user instruction.** First inspect the diagnostics, restore required standard Blender baking prerequisites, and repair the known native bake error before running the authoring/export path. Reconcile the procedural script and saved source versions explicitly. The following are the exact future review/build commands; the current build command is expected to fail on the recorded property error until repaired:

```sh
cd /workspace/sanjo-solutions/apps/a-game
BLENDER=/home/agent/.local/bin/blender
"$BLENDER" --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/breaking/author.py -- --character Man --clip basic_rock --review-only
"$BLENDER" --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/breaking/author.py -- --character Woman --review-only
# After repair and explicit animation authorization:
"$BLENDER" --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/breaking/author.py -- --character Man
"$BLENDER" --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/breaking/author.py -- --character Woman
"$BLENDER" --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/breaking/preview.py -- Man 0
```

Remaining work includes reliable bake fidelity, complete Man/Woman saved outputs, credible Breaking technique and support in power/freeze studies, exhaustive collision and contact review, smooth transition compatibility, interpolated loop/angular continuity, full visual playback review, and Godot runtime validation with complete imports. These tasks remain open; preservation delivery does not complete them.

## Delivery verification

The checkpoint commit is discoverable with `git log --format=fuller -- docs/animation_work_status/breaking_repertoire.md`. Integration preserves newer `origin/main`, unions shared animation library references by path, and uses ordinary pushes. Final delivered commit hashes are reported in the chat to avoid a self-referential commit hash in this file.

Related run: **16 passed, 13 failed, 30 started of 66 selected** before deliberate SIGINT (exit 130); remaining checks were not completed. Failures include missing imported hair/player resources, unresolved NPC dependencies, and editor-only API use in headless tests. The partial suite is not a passing result. The structural asset inspection and final 9/9 fast suite passed independently.

Integration note: fetched `origin/main` at `4fa0d077e` and rebased preservation as `e5caee13088d8d31df40c00bc3aebbd1fdce61bc`. Attribute conflicts retained concurrent entries. Later isolation follows the updated `AGENTS.md` rule for stopped exports; binary hashes remain identical. The runtime registry retains the 133 references present on that fetched main and excludes all Breaking studies pending renewed work.

After rebase, the updated fast runner selected ten checks: **9/10 passed in 5.50 s**. `playground/activity_import/test_activity_json.gd` reports missing imported hair GLBs, unresolved `Hair.STYLES`/Character/NPC dependencies, and compilation errors despite printing its success marker. The newer runner correctly treats these errors as a failure. See `breaking_repertoire/fast_tests_after_rebase.log`; the earlier 9/9 result belongs to the earlier runner/environment and does not certify the integrated tree. Importing the whole project was deferred to preserve the animation stop.

After export isolation, read-only Blender 5.2.2 inspection passed again for all 37 pairs. All 111 source/export/import SHA-256 values match the pre-isolation inventory. All 76 binary Git blob sizes match the actual files. `python scripts/lfs_policy.py check` passed for 25,212 staged files. No owned authoring, rendering, or verification process remained after these checks.
