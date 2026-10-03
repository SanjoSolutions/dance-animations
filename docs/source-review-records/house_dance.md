# House dance animation work status

- Date: 2026-10-02 (Europe/Berlin).
- Chat/task title: House dance animations for man_and_woman3.blend. The exact UI title was unavailable in the app's most-recent-50-chat listing; this is the task label.
- Task branch: `codex/house-dance`.
- Commit when authoring stopped: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Repository: `SanjoSolutions/sanjo-solutions`, app `apps/a-game`, sanjo-solutions cloud environment.
- Author and GitHub identity: Codex, `codex.sanjo.solutions@gmail.com`.
- Delivery state: preservation requested by the user through the coordinating chat `01a0fd1a-3673-7683-ae29-577f2ee1a927`. Animation authoring, refinement, generation, baking, export, and rendering stopped. This record accompanies the preservation commits; the final chat response supplies their hashes and remote integration result.

## Original scope and stopping point

Create a broad House dance repertoire for both characters from `man_and_woman3.blend`, with solo clips, natural motion, planted contacts, clearance, smooth transitions, interpolated and loop validation, reuse of appropriate existing motion, one source per animation, and Blender 5.2 throughout. Commit assets, fetch/rebase current main, add reusable Animation guidance, commit that documentation, merge and push with required asset uploads. Store task binaries at or below 104,857,600 bytes directly in Git.

The planned catalog contains 45 phrase/position/transition definitions, or 90 solo clips. The preserved deliverable contains **49 authored procedural blocking studies (25 PLAYER/man, 24 PARTNER/woman), zero persisted baked actions, and one earlier trial GLB**. These are partial animation studies, not a completed or artistically accepted House repertoire. House vocabulary has community and freestyle variations; the planned catalog is broad rather than an exhaustive taxonomy.

All 49 saved studies cover frames **0–96 at 24 fps**, four seconds/eight beats at the authored 120 BPM. Each file contains one authoring action and a descriptor referencing existing `shared_scene_data.blend`. Each source is discoverable through the existing combined-library workflow. The combined source, shared rig/geometry files, and existing clips were left unchanged. The existing idle stance and hand setup were reused; `solo_disco_dance` was inspected as a reuse candidate, and its disco choreography was kept separate.

## Exact preserved source assets

All paths in this record are relative to `apps/a-game` unless stated otherwise. Each listed source has a passing recorded 195-sample review. Full hashes, sizes, action slots, descriptors, roles, frame ranges, and review metrics are in [`house_dance_evidence/preserved_sources.json`](house_dance_evidence/preserved_sources.json).

| Source file | Role | Frames | State | Recorded review |
| --- | --- | --- | --- | --- |
| `animations/man_and_woman/house_man_body_roll.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_body_roll.json` |
| `animations/man_and_woman/house_man_box_step.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_box_step.json` |
| `animations/man_and_woman/house_man_cross_step.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_cross_step.json` |
| `animations/man_and_woman/house_man_diamond_step.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_diamond_step.json` |
| `animations/man_and_woman/house_man_farmer.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_farmer.json` |
| `animations/man_and_woman/house_man_floor_support_position.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_floor_support_position.json` |
| `animations/man_and_woman/house_man_half_turn_return.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_half_turn_return.json` |
| `animations/man_and_woman/house_man_heel_dig.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_heel_dig.json` |
| `animations/man_and_woman/house_man_jack.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_jack.json` |
| `animations/man_and_woman/house_man_kick_ball_change.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_kick_ball_change.json` |
| `animations/man_and_woman/house_man_lofting_floor_rock.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_lofting_floor_rock.json` |
| `animations/man_and_woman/house_man_loose_legs.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_loose_legs.json` |
| `animations/man_and_woman/house_man_low_sweep.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_low_sweep.json` |
| `animations/man_and_woman/house_man_pas_de_bourree.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_pas_de_bourree.json` |
| `animations/man_and_woman/house_man_running_man.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_running_man.json` |
| `animations/man_and_woman/house_man_salsa_step.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_salsa_step.json` |
| `animations/man_and_woman/house_man_scissors.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_scissors.json` |
| `animations/man_and_woman/house_man_shuffle.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_shuffle.json` |
| `animations/man_and_woman/house_man_side_jack.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_side_jack.json` |
| `animations/man_and_woman/house_man_side_step.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_side_step.json` |
| `animations/man_and_woman/house_man_skate.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_skate.json` |
| `animations/man_and_woman/house_man_stomp.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_stomp.json` |
| `animations/man_and_woman/house_man_tip_tap.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_tip_tap.json` |
| `animations/man_and_woman/house_man_toe_touch.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_toe_touch.json` |
| `animations/man_and_woman/house_man_train.blend` | PLAYER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_man_train.json` |
| `animations/man_and_woman/house_woman_body_roll.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_body_roll.json` |
| `animations/man_and_woman/house_woman_box_step.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_box_step.json` |
| `animations/man_and_woman/house_woman_cross_step.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_cross_step.json` |
| `animations/man_and_woman/house_woman_diamond_step.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_diamond_step.json` |
| `animations/man_and_woman/house_woman_farmer.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_farmer.json` |
| `animations/man_and_woman/house_woman_floor_support_position.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_floor_support_position.json` |
| `animations/man_and_woman/house_woman_half_turn_return.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_half_turn_return.json` |
| `animations/man_and_woman/house_woman_heel_dig.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_heel_dig.json` |
| `animations/man_and_woman/house_woman_jack.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_jack.json` |
| `animations/man_and_woman/house_woman_kick_ball_change.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_kick_ball_change.json` |
| `animations/man_and_woman/house_woman_lofting_floor_rock.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_lofting_floor_rock.json` |
| `animations/man_and_woman/house_woman_low_sweep.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_low_sweep.json` |
| `animations/man_and_woman/house_woman_pas_de_bourree.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_pas_de_bourree.json` |
| `animations/man_and_woman/house_woman_running_man.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_running_man.json` |
| `animations/man_and_woman/house_woman_salsa_step.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_salsa_step.json` |
| `animations/man_and_woman/house_woman_scissors.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_scissors.json` |
| `animations/man_and_woman/house_woman_shuffle.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_shuffle.json` |
| `animations/man_and_woman/house_woman_side_jack.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_side_jack.json` |
| `animations/man_and_woman/house_woman_side_step.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_side_step.json` |
| `animations/man_and_woman/house_woman_skate.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_skate.json` |
| `animations/man_and_woman/house_woman_stomp.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_stomp.json` |
| `animations/man_and_woman/house_woman_tip_tap.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_tip_tap.json` |
| `animations/man_and_woman/house_woman_toe_touch.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_toe_touch.json` |
| `animations/man_and_woman/house_woman_train.blend` | PARTNER | 0–96 | Authored study; bake absent | `scripts/player_assets/house_dance/reports/house_woman_train.json` |

## Baked and exported state

- `models/player/animation_updates/house_man_jack_baked_e20e55a226e1.glb`: **earlier trial export**, 342,480 bytes, one `house_man_jack.baked` animation and 639 channels. Blender 5.2.2 native visual baking measured maximum sampled deform-position error 0.00000253937 and zero angular error at frames 0, 12, 24, 48, 72, 96. The matching `.glb.import` file is preserved.
- The authoring source was subsequently regenerated. The preserved GLB is **stale relative to the current jack source**. Its previous bake is absent from that current source. The trial is **unregistered from `models/player/animation_updates.tres`**, which was restored to its pre-task contents, so preservation adds no active runtime clip override.
- `scripts/player_assets/house_dance/reports/house_man_jack_export.json` and `house_dance_evidence/export.log` describe that earlier trial, not a bake of the current source. `house_dance_evidence/preserved_export.json` records its hash and explicit status.
- The other 48 saved sources have zero exports from this task. No current full library export or complete Godot playback validation was produced. Reopened native NLA/chooser playback was not validated; read-only preservation inspection checked saved action ranges and bindings metadata.

## Procedural tools and other durable files

- `scripts/player_assets/house_dance/repertoire.py`: data for 35 standing phrases/positions, six supported floor phrases/positions, and four standing transitions; 90 intended solo clips.
- `scripts/player_assets/house_dance/author.py`: Blender 5.2 IK authoring, contact timing, neutral-pose reuse, sparse control keys, stationary-channel compaction, loop closure, per-animation saving, and interpolated proxy review.
- `scripts/player_assets/house_dance/floor.py`: supported floor blocking studies, calibrated palms, and relaxed fingers. Its per-action standing wrist constraint is disabled for floor support. Full skin/wrist review remains required before acceptance.
- `scripts/player_assets/house_dance/transitions.py`: **implemented but unexecuted transition generator**, relaxed↔ready and ready↔low. Its one-way motion and endpoint handling have yet to be validated in saved clips.
- `scripts/player_assets/house_dance/export.py`: native Blender visual-bake experiment plus existing `AnimationClipScene`, `AnimationFileWriter`, and `AnimationUpdates` publishing helpers. Game Rig Tools was absent during this task. The single earlier jack trial succeeded; later loop-mode handling is only syntax checked.
- `scripts/player_assets/house_dance/build.py`: isolated authoring jobs and serialized clip publication. Preservation interrupted the additional batch before its requested clips completed.
- `scripts/player_assets/house_dance/validate.py`: **unexecuted full-catalog validator**. It expects all 90 sources, review reports, and exports and cannot pass against this partial snapshot. `catalog.json` was never generated.
- `scripts/player_assets/house_dance/reports/*.json`: 49 successful procedural motion reports plus the one earlier export report.
- `docs/animation_work_status/house_dance_evidence/`: preserved logs, source/export inventories, verification output, storage audit, and two early preview images. `pose.png` and `floor.png` are early blocking previews, not current-source acceptance renders. `floor.png` predates the later finger and floor-depth adjustments.
- Storage integration: the initial task commit used exact-file regular-Git exceptions for 52 small binaries (49 sources, one GLB, two PNG previews). Fetched main introduced `scripts/lfs_policy.py` and generated size-based attributes. The rebased preservation follows that policy; these small raw Git blobs require zero additional attribute exceptions. The original pre-staging audit and post-integration attribute checks are both retained.

## Validation results and limits

- `blender --version`: Blender **5.2.2 LTS**, hash `d13f752e3b9c`. All authoring, inspection, rendering and the trial bake/export used this executable.
- Each completed authoring run sampled 195 times, including half frames and 0.1-frame loop boundaries. All 49 saved-source reports passed their implemented criteria. Maximum recorded planted-target error across them was **0.00142149 world units**. Reports include ankle separation, half-frame displacement, loop position/velocity, joint-angle ranges and hand/torso proxies where the later review implementation was used.
- These checks establish sampled target/proxy behavior. Full mesh collision coverage, finger-surface contact, balance dynamics, stylistic authenticity, exported subframe behavior, and complete visual motion review remain outstanding. Earlier saved sources predate later generator refinements, so the current script is not a frozen recipe for every saved file.
- Read-only preservation verification: `blender -t 1 -b --factory-startup --python-exit-code 1 --python /tmp/house-dance/inspect_preserved.py`. **49/49 sources opened**, each with one authoring action, correct solo role and range, and zero baked actions. Script preserved as `house_dance_evidence/inspect_preserved.py`; its embedded project path can be adjusted for another checkout. Results: `source_inspection.log`, `preserved_sources.json`, `preservation_verification.txt`.
- `GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot python tests/run_tests.py --suite fast`: **9/9 passed after stopping**, 3.78 seconds; `house_dance_evidence/fast_preservation.log`.
- `GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot BLENDER=/home/agent/.local/bin/blender python tests/run_tests.py --slow-timeout 60 --changed scripts/player_assets/house_dance/author.py --changed animations/man_and_woman/house_man_jack.blend`: selected nine fast and 57 slow checks. The latest attempt was **interrupted at the stop request**, with 13 passes and six failures recorded across completed entries; remaining entries have no final result. Existing material/texture import failures caused scene instantiation errors and timeouts. Exact test results are in `related_test_results.json`, with full output in `related-final.log`. This is not a passing related suite.
- After rebasing onto `98440a92c`, the same fast-suite command passed **10/10 checks in 6.76 seconds**; `house_dance_evidence/fast_integrated.log`. The additional check came from concurrent main changes. `python scripts/lfs_policy.py check` passed for the staged repository, and all 52 preserved binary blobs retained their recorded hashes.
- `python -m compileall -q apps/a-game/scripts/player_assets/house_dance`: passed during preservation.
- Read-only GLB structure verification passed for the earlier trial (header/length, one expected animation, channel count). Hashes and states are recorded separately from current source hashes.
- Several initial checks encountered LFS pointers instead of assets. Required source files and subsequently the remaining A-Game LFS assets were hydrated. Godot imports exposed tracked `valid=false` import metadata; removing invalid local cache markers and reimporting was an environment-repair attempt. Incidental tracked import/eye-resource changes were restored, keeping this preservation scoped to House work.

## Owned processes and saved state

The stop request terminated the task's authoring batch, additional batch, and related-test process trees, including active heel/toe, swivel, open/close, loose-legs retry, and Charleston retry workers. No owned authoring, export or render process remains running. Defunct Blender process entries are terminated zombies awaiting parent reaping; they perform no work. The final Godot import process completed during the stopping window. Durable saved sources and logs were retained; unsaved in-memory poses ended with their processes.

Original temporary investigation outputs were under `/tmp/house-dance`. Relevant logs and images were copied into the committed evidence directory. The credential helper in that temporary directory reads the configured `SANJO_GITHUB_LFS_TOKEN` at runtime; it contains no token literal and is deliberately excluded from Git. `.cache/house_dance` is local-only; the additional authoring logs were copied to the evidence directory. Environment hydration, Blender/Godot caches and downloaded pre-existing LFS assets are setup rather than new repository assets.

## Concrete blockers and remaining work

1. The user has paused animation work. Resume authoring only after a new instruction to resume.
2. Procedural blocking is incomplete: 41 intended clips have no saved source, listed below. The transition module and most floor-flow variations have no authored outputs.
3. Blender repeatedly crashed while evaluating an incompletely keyed floor-rock action near frame 93; loose-legs also produced an invalid IK foot value, and Charleston crashed. The latest authoring implementation solves each pose from a complete frame-zero reference before inserting keys at the target time. This allowed both floor-rock studies to finish. Loose-legs/Charleston retries were stopped; the general recovery remains partially validated.
4. The floor-support source uses the earlier 0.40 torso-height study while the saved floor rock uses the later 0.36 study. Their transition and full surface contact require review. Floor wrist constraints were disabled per action; natural wrist extension and finger contact need direct inspection.
5. All 49 current sources need validated bakes and exports. The single preserved GLB is stale. Game Rig Tools was absent from the task environment at authoring time; recheck current main and installation guidance on resume, since another chat may now provide it.
6. Complete mesh/foot-sole clearance, wrist/finger review, dance-style review, transitions between supported floor and standing motion, visual sampling, and Godot target/playback validation remain outstanding.
7. Finish relevant project checks after resolving existing import metadata/material dependencies. Keep environmental failures distinct from animation checks.

Missing saved clips:

- `house_woman_loose_legs`
- `house_man_charleston`
- `house_woman_charleston`
- `house_man_heel_toe`
- `house_woman_heel_toe`
- `house_man_swivel`
- `house_woman_swivel`
- `house_man_open_close`
- `house_woman_open_close`
- `house_man_quarter_turn_left`
- `house_woman_quarter_turn_left`
- `house_man_quarter_turn_right`
- `house_woman_quarter_turn_right`
- `house_man_deep_jack`
- `house_woman_deep_jack`
- `house_man_relaxed_position`
- `house_woman_relaxed_position`
- `house_man_ready_position`
- `house_woman_ready_position`
- `house_man_low_position`
- `house_woman_low_position`
- `house_man_wide_position`
- `house_woman_wide_position`
- `house_man_staggered_position`
- `house_woman_staggered_position`
- `house_man_lofting_leg_sweep_left`
- `house_woman_lofting_leg_sweep_left`
- `house_man_lofting_leg_sweep_right`
- `house_woman_lofting_leg_sweep_right`
- `house_man_lofting_knee_switch`
- `house_woman_lofting_knee_switch`
- `house_man_lofting_body_wave`
- `house_woman_lofting_body_wave`
- `house_man_relaxed_to_ready`
- `house_woman_relaxed_to_ready`
- `house_man_ready_to_relaxed`
- `house_woman_ready_to_relaxed`
- `house_man_ready_to_low`
- `house_woman_ready_to_low`
- `house_man_low_to_ready`
- `house_woman_low_to_ready`

## Exact resume commands

These commands are recorded for a future explicitly resumed task, not executed after the stop request. Start from the integrated main and read its current `AGENTS.md` and animation workflow. Use the configured GitHub credential mechanism without printing credentials.

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender --version
# Read-only preserved-source inspection; adjust the embedded checkout path if needed.
blender -t 1 -b --factory-startup --python-exit-code 1 \
  --python docs/animation_work_status/house_dance_evidence/inspect_preserved.py
# Small recovery probes after renewed authoring authorization.
python scripts/player_assets/house_dance/build.py --author --workers 1 loose_legs charleston
python scripts/player_assets/house_dance/build.py --author --workers 1 \
  floor_support_position lofting_floor_rock lofting_leg_sweep_left lofting_leg_sweep_right \
  lofting_knee_switch lofting_body_wave
python scripts/player_assets/house_dance/build.py --author --workers 1 \
  relaxed_position ready_position low_position wide_position staggered_position \
  relaxed_to_ready ready_to_relaxed ready_to_low low_to_ready
python scripts/player_assets/house_dance/build.py --author --workers 1 \
  heel_toe swivel open_close quarter_turn_left quarter_turn_right deep_jack
# Re-author the entire intended catalog only when desired; this replaces existing studies.
python scripts/player_assets/house_dance/build.py --author --workers 3
# Export only after source review; publication modifies the active update registry.
python scripts/player_assets/house_dance/build.py --export
python scripts/player_assets/house_dance/validate.py
GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot python tests/run_tests.py --suite fast
GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot \
BLENDER=/home/agent/.local/bin/blender python tests/run_tests.py \
  --changed scripts/player_assets/house_dance/author.py \
  --changed animations/man_and_woman/house_man_jack.blend
```

Before staging any regenerated asset, inspect its actual byte size and `git check-attr` output. Retain regular Git for files at or below 104,857,600 bytes; use file-scoped LFS attributes for larger outputs. Regenerate the status/catalog when its source state changes.

## Integration note

The preservation commit was rebased onto fetched `origin/main` at `98440a92c`. Its root attribute conflict was resolved by retaining main's generated 100 MiB policy; all 52 House binary hashes and raw Git blobs remain unchanged. Main now includes bundled Game Rig Tools setup instructions, which supersede the environment limitation observed during authoring. No animation authoring or baking was resumed.

Final integration merged the House task into main based on fetched `9eedcbc5e1889e55af3ea91c62ad552cfbef7ca4`, retaining every concurrent Animation guidance entry. The merged fast suite passed **10/10 in 6.36 seconds** (`house_dance_evidence/fast_merged.log`), and the size-based storage policy passed for 26,170 staged files. Task preservation commit: `6236f49ef968b74a18580e1bce1ba401e5ae72ee`; guidance commit: `bbfd0a46587eb3f9e4a8751ff2eaa2e27fef8d22`. The final chat response records the merge hash and remote verification.

The first ordinary push was rejected because concurrent main advanced. Integrated fetched `712693bd5` with a history-preserving merge; its fast suite passed **10/10 in 6.34 seconds**, and storage policy passed for 27,266 staged files. Logs: `house_dance_evidence/fast_final_merge.log` and `policy_final.log`.
