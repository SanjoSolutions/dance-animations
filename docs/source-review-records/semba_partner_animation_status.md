# Semba partner animation preservation status

## Checkpoint

- Date: October 2, 2026; stopped-state inspection at 15:01:35 UTC.
- Chat/task title: Semba partner animations for man_and_woman3.blend.
- Checkout: `/workspace/sanjo-solutions/apps/a-game` in sanjo-solutions.
- Branch at stop: `codex/semba-animation-library`.
- Commit at stop: `3c52737c74b488501e9cfe47e7029547c6f5fe88`.
- Author: Codex. Repository commits and GitHub delivery are authored by Codex.
- Latest instruction: preserve the current animation state, record it, commit, integrate current main, and push. Authoring, refinement, generation, and rendering are stopped. All owned animation and review processes had completed before this instruction; process inspection confirmed the finished state.

The original scope requested a broad coordinated Semba repertoire for both characters, covering moves and positions, reuse of suitable rig behavior, natural motion, planted contacts, clearance, transitions, interpolated validation, per-animation Blender sources, documentation, and Git delivery. The current checkpoint contains 42 procedurally authored paired clips: 7 positions, 15 footwork phrases, 8 turns, and 12 directed formation transitions. These are procedural choreography/blocking studies with measured IK and contact checks and rendered visual review. Regional Semba completeness, teaching certification, whole-body force balance, and exhaustive mesh collision assessment remain future review work. The original all-moves scope remains partial.

## Authored, baked, and exported state

**Authored: 42. Baked: 0. Godot runtime exported: 0. Review videos: 2.** All 42 editable sources are saved and included in this checkpoint. Man.rigify leads and Woman.rigify follows in each file, using synchronized action slots and NLA bindings. Role reversal remains future choreography work.

All Blender authoring, scripting, validation, rendering, and preview encoding used `/tmp/semba-tools/blender-5.2.2-linux-x64/blender` (5.2.2 LTS). Sources use 24 fps and 120 beats per minute. Stored ranges are 0–96. Loops play 0–95, with frame 96 duplicating the opening pose. Quarter turns and directed transitions play 0–96 once. Markers: Ready 0, Lead 12, Phrase 48, Recover 84, Loop/Arrive 96. The catalog records exact authored keys and timing. Stationary channels retain one initial key; moving controls use meaningful poses and additional passing/turn poses.

All files in the following table belong to `animations/man_and_woman/`. Every row has authored state complete for this procedural checkpoint, baked state pending, exported state pending, stored frames 0–96, and the leader/follower roles described above.

| Source file | Family | Formation | Playback |
| --- | --- | --- | --- |
| `semba_basic_back_forward.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_basic_forward_back.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_basic_in_place.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_circle_left.blend` | Turn | closed → closed | 0–95 loop |
| `semba_circle_right.blend` | Turn | closed → closed | 0–95 loop |
| `semba_closed_to_counterpromenade.blend` | Transition | closed → counterpromenade | 0–96 once |
| `semba_closed_to_open_one_hand.blend` | Transition | closed → open_one_hand | 0–96 once |
| `semba_closed_to_open_two_hand.blend` | Transition | closed → open_two_hand | 0–96 once |
| `semba_closed_to_promenade.blend` | Transition | closed → promenade | 0–96 once |
| `semba_closed_to_shadow.blend` | Transition | closed → shadow | 0–96 once |
| `semba_closed_to_side_by_side.blend` | Transition | closed → side_by_side | 0–96 once |
| `semba_counterpromenade_to_closed.blend` | Transition | counterpromenade → closed | 0–96 once |
| `semba_diagonal_basic_left.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_diagonal_basic_right.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_follower_turn_left.blend` | Turn | open_one_hand → open_one_hand | 0–95 loop |
| `semba_follower_turn_right.blend` | Turn | open_one_hand → open_one_hand | 0–95 loop |
| `semba_open_one_hand_to_closed.blend` | Transition | open_one_hand → closed | 0–96 once |
| `semba_open_two_hand_to_closed.blend` | Transition | open_two_hand → closed | 0–96 once |
| `semba_position_closed.blend` | Position | closed → closed | 0–95 loop |
| `semba_position_counterpromenade.blend` | Position | counterpromenade → counterpromenade | 0–95 loop |
| `semba_position_open_one_hand.blend` | Position | open_one_hand → open_one_hand | 0–95 loop |
| `semba_position_open_two_hand.blend` | Position | open_two_hand → open_two_hand | 0–95 loop |
| `semba_position_promenade.blend` | Position | promenade → promenade | 0–95 loop |
| `semba_position_shadow.blend` | Position | shadow → shadow | 0–95 loop |
| `semba_position_side_by_side.blend` | Position | side_by_side → side_by_side | 0–95 loop |
| `semba_promenade_to_closed.blend` | Transition | promenade → closed | 0–96 once |
| `semba_quarter_turn_left.blend` | Turn | closed → closed | 0–96 once |
| `semba_quarter_turn_right.blend` | Turn | closed → closed | 0–96 once |
| `semba_retrocesso.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_rock_step.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_saida_follower.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_saida_leader.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_shadow_to_closed.blend` | Transition | shadow → closed | 0–96 once |
| `semba_side_basic_left.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_side_basic_right.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_side_by_side_to_closed.blend` | Transition | side_by_side → closed | 0–96 once |
| `semba_step_touch.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_syncopated_step.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_traveling_left.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_traveling_right.blend` | Footwork | closed → closed | 0–95 loop |
| `semba_underarm_turn_left.blend` | Turn | open_one_hand → open_one_hand | 0–95 loop |
| `semba_underarm_turn_right.blend` | Turn | open_one_hand → open_one_hand | 0–95 loop |

## Durable files and existing dependencies

- `scripts/create_semba.py`: paired IK authoring, stance composition, calibrated palm fitting, sparse keys, and individual source writer.
- `scripts/semba/choreography.py`: repertoire, formation, and foot scheduling data.
- `scripts/validate_semba.py`: reloaded-source checks, measured tolerances, transition checks, and Blender review rendering.
- `scripts/semba.md`: coverage, roles, timing, reuse, validation, chooser, and delivery guide.
- `animations/man_and_woman/semba_catalog.json`: all 42 sources, exact keys, markers, timing, and delivery state.
- `animations/man_and_woman/semba_validation.json`: passing checks for all sources, 2,814 sampled frames, 24 transition endpoint connections, source hashes, sizes, and tolerances.
- `animations/man_and_woman/semba_review.json`: visual review scope, hashes, source discovery/composition, and delivery counts.
- `animations/man_and_woman/semba_preview_underarm_turn_left.mp4` and `semba_preview_underarm_turn_right.mp4`: Blender review media, each 384 × 384, 32 frames, eight fps, four seconds. These are preview videos; runtime exports remain pending.
- `animations/man_and_woman/.gitattributes`: exact-filename ordinary-Git exceptions for the 42 sources and two videos. Actual total binary size: 6,028,905 bytes; largest file: 176,587 bytes. All are within 104,857,600 bytes. Their `filter` attribute is unset; shared scenes retain LFS.
- `scripts/player_assets/animation_files.py`: compact numeric internal reference-cache keys preserve action names beyond Blender's 63-character custom-property key limit. Existing long Acro names exposed this chooser blocker.
- `scripts/player_assets/test_animation_files.py`: public save/reload regression with long action names and a shared prefix.

Existing paired authoring, yoga stance, disco wrist fitting, and animation writer APIs supply reused rig behavior. Existing combined library, shared scene, character sources, and props retain their saved bytes. SHA-256 checks matched the tracked LFS objects for combined/shared/anatomical sources. Hydrated dependencies include `man_and_woman3.blend`, `animations/man_and_woman/shared_scene_data.blend`, `man_anatomical_study.blend`, `woman_anatomical_study_speculum.blend`, `dildo.blend`, existing split sources, hair meshes, player models, and character textures. Player Asset Export was installed in the Blender 5.2 user configuration. Game Rig Tools/runtime export setup remains a future prerequisite.

## Verification and results

1. `python tests/run_tests.py --suite fast`: latest run **10/10 passed** in 6.34 seconds (`.cache/semba/fast_final.log`). Initial hair-mesh LFS pointer failures were resolved by retrieving their real objects. Earlier concurrent workload exposed intermittent process-tree socket cleanup test timing failures; the latest quiet run passed.
2. `BLENDER=/tmp/semba-tools/blender-5.2.2-linux-x64/blender python tests/run_tests.py --suite changed --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_paired_animation_authoring.py --changed scripts/player_assets/test_motion_review.py --changed scripts/test_track_chooser.py`: **15/15 passed** in 13.65 seconds, comprising ten fast and five focused slow checks (`.cache/semba/slow_final.log`).
3. Saved-source validation command below passed all 42 clips and all 24 transition endpoint connections. Checks cover slots, NLA metadata, timing, finite keys, visible movement, evaluated IK reach, planted ankle position/rotation, calibrated palm targets, interpolated grip spacing, wrist deviation, sampled surfaces above the floor, torso clearance proxies, and loop position/rotation/linear/angular velocity. Detailed tolerances and measurements belong to `semba_validation.json`.
4. Maximum IK reach error: 0.0002268 m; planted ankle error: 0.0002247 m; shared-hand gap error: 0.0049461 m; authored palm-target error: 0.0000029 m. Sampled floor penetration: 0 m. Minimum torso sphere clearance: 0.0498521 m. Loop position and rotation errors: 0. Maximum boundary linear velocity difference: 0.00244 m/frame; angular velocity difference: 0.0052393 radians/frame. These quantify the implemented checks; physical balance and complete surface collision analysis have separate scopes.
5. Reviewed six-pose strips at frames 0, 6, 30, 54, 78, 96 for every clip and native Blender playback for both connected underarm turns. Source pre-roll fixed stale evaluated geometry in initial review frames. Final strips and two videos completed before the stop instruction.
6. Combined-library smoke check: all 42 Semba sources discovered through TrackChooser; opening `semba_underarm_turn_left.blend` composes both synchronized editable rigs (`.cache/semba/delivery.log`).
7. `git diff --check`, Python compilation, and Black checks for the three new Python scripts passed.
8. A broader asset-triggered Godot runtime suite selected 57 slow checks. Its first model animation player check encountered stale/missing imported animation update/cache resources; the activity animation check stalled and its owned runner was explicitly terminated with child-process cleanup. That broad runtime run remains incomplete. Hydrated assets alone do not supply the complete Godot import and runtime export prerequisites. The focused authoring/tooling checks above completed successfully.

## Saved local outputs and processes

The ignored `.cache/semba/` directory retains build, validation, review, smoke, and test outputs. Useful paths: `build_final.log`, `partition_0.log`, `partition_1.log`, `partition_*_records.json`, `catalog.log`, `final_validation.log`, `render_review.log`, `final_review/*.png`, `atlas_0.png` through `atlas_6.png`, `playback/`, `playback.log`, `fast_final.log`, `slow_final.log`, `delivery.log`, and `related_tests.log`. It also retains diagnostic scripts, including `verify_delivery.py` and `assemble_catalog.py`. These local caches are supplementary; committed catalogs, reports, sources, and videos form the durable checkpoint. Process state at handoff: all owned Blender, render, and test processes finished or terminated. Further animation execution is paused.

## Remaining work and resume commands

Remaining work after renewed animation authorization: expert Semba review and additional regional variations, role variants, further collision/balance assessment, runtime export prerequisites, baking each requested source, saving its baked action, export receipts, and Godot runtime checks. Current delivery proceeds with the authored checkpoint. Runtime integration checks remain blocked by the incomplete imported/exported resource setup described above.

Read and inspect first:

```sh
cd /workspace/sanjo-solutions/apps/a-game
export BLENDER=/tmp/semba-tools/blender-5.2.2-linux-x64/blender
"$BLENDER" --version
python tests/run_tests.py --suite fast
BLENDER="$BLENDER" python tests/run_tests.py --suite changed \
  --changed scripts/player_assets/test_animation_files.py \
  --changed scripts/player_assets/test_paired_animation_authoring.py \
  --changed scripts/player_assets/test_motion_review.py \
  --changed scripts/test_track_chooser.py
git check-attr filter -- animations/man_and_woman/semba_*.blend animations/man_and_woman/semba_*.mp4
```

After renewed authorization to resume animation work, the reproducible authoring and validation commands are:

```sh
"$BLENDER" --factory-startup -t 4 --background \
  animations/man_and_woman/shared_scene_data.blend --disable-autoexec \
  --python-exit-code 1 --python scripts/create_semba.py
"$BLENDER" --factory-startup -t 4 --background \
  animations/man_and_woman/shared_scene_data.blend --disable-autoexec \
  --python-exit-code 1 --python scripts/validate_semba.py \
  -- --render .cache/semba/resumed_review
```

For one source, append `-- --only underarm_turn_left` to the authoring command. For runtime work, configure the documented Game Rig Tools/Player Asset Export prerequisites, open the individual source, use **Bake & Export Active Animation**, and save the source to retain its baked action. Follow `docs/player-animation-workflow.md` and run related Godot checks through `tests/run_tests.py` after imports complete. A recreated environment needs the Blender 5.2 executable and hydrated linked dependencies again.

## Git delivery record

At status creation, durable changes were awaiting the preservation commit. Integration follows the requested order: commit assets/status, fetch and rebase onto current origin/main, commit learned animation guidance, fetch immediately before integration, merge main, ordinary push, and verify task ancestry and remote tip. Each new commit carries exactly one Codex co-author trailer. Exact delivered commit hashes are reported in the chat completion record; the status file records the stopped-state base above. All 44 new binary assets use real ordinary-Git blobs, so this task introduces zero LFS upload objects.


### Integration checkpoint

The preservation commit was rebased onto `origin/main` at `e12670ea9`. Its rebased identifier is `6e181113f76ceb92495dd983bbc722040359c9a3`. Conflict resolution preserved every concurrent asset storage entry, retained main's equivalent compact reference-cache implementation, and retained both long-action-name regression tests. The subsequent documentation update adds Semba guidance, review pre-roll/video configuration, and action-reference key guidance to `AGENTS.md` under Animation. The initial reports describe the saved authoring revision; integration verification covers the resolved tooling and byte-identical task assets. Further choreography execution remains paused.

Post-rebase verification: `python tests/run_tests.py --suite fast` passed 10/10 in 6.38 seconds (`.cache/semba/fast_integrated.log`); the same focused changed-suite command above passed 15/15 in 11.81 seconds (`.cache/semba/slow_integrated.log`). All 44 committed binary hashes, working-file hashes, sizes, and ordinary-Git attributes match the checkpoint. `python /workspace/sanjo-solutions/scripts/lfs_policy.py check` passed for all 23,982 indexed files. Main's newly available bundled tool installer is documented in `scripts/blender/README.md`; installation and animation execution remain future resume steps.

Final integration fetched `origin/main` at `b2cf8b15f` immediately before merging the two task commits. The merge preserved concurrent documentation and combined exact-filename storage entries. The merged fast suite passed 10/10 in 6.17 seconds (`.cache/semba/fast_merged.log`), and the repository LFS policy passed for all 25,571 indexed files. The documentation task commit is `75f2dd7c1`; ordinary push and remote ancestry/tip verification follow the merge commit. Final merge and push identifiers are recorded in the chat completion report.
