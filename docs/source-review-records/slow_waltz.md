# Slow Waltz preservation checkpoint

- Date: 2026-10-02; recording and delivery began at approximately 15:06 UTC.
- Chat title (descriptive task title): Slow Waltz animations for man_and_woman3.blend.
- Project/environment: A-Game, sanjo-solutions cloud, `/workspace/sanjo-solutions/apps/a-game`.
- Stopped branch: `feat/slow-waltz`.
- Current commit at the stopping point: `3c52737c74b488501e9cfe47e7029547c6f5fe88`.
- Author of this record: Codex. The task commit containing this record and subsequent integration commits are reported in the delivery response; this hash is the pre-checkpoint base.

## Scope and stop instruction

The original request was a broad, coordinated Slow Waltz repertoire for both characters in `man_and_woman3.blend`, including positions, moves, planted contacts, body clearance, smooth transitions, interpolated validation and loop continuity, with reusable existing animation work, per-animation sources, Blender 5.2 throughout, documentation, commits and delivery to main.

The user subsequently instructed all animation chats to stop authoring, refining, generating and rendering, preserve the present state, record exact progress, run delivery checks, commit and push. That instruction controls this checkpoint. These assets are **partial procedural blocking studies**, rather than a completed or approved dance library. The named figure families include compact game adaptations and additional half-beat transfers for large turns. They do not certify competition syllabus accuracy or complete coverage of every Slow Waltz variation.

## Completed work and asset state

60 individual `.blend` sources were authored with synchronized actions for `Man.rigify` (leader/player) and `Woman.rigify` (follower/partner), matching participant slots/NLA bindings, timing and metadata. They use the existing linked shared scene and character geometry. The source catalog defines 24 fps, 30 measures/minute, 3/4 meter, 16 frames/beat and 48 frames/measure.

Coverage: 7 positions, 10 foundation figures, 8 turning figures, 15 advanced figures, 6 lines, 2 practice loops and 12 directed transitions. Seven position loops and two box-step practice loops have duplicate final poses; playback excludes the duplicate endpoint. The inventory below records every source, frame range, playback end and role. Detailed counts, markers, support intervals, entry/exit frames and feature flags are in the catalog.

**Authored: 60 partial studies. Baked: 0. Exported: 0.** Runtime GLB publication, Godot clip export and gameplay integration have yet to begin. Saved combined/shared/character source assets remain unchanged. Existing disco actions were inspected and judged stylistically unsuitable; the neutral yoga posing helper, paired IK/palm calibration API and established split-file writer were reused.

Files belonging to this task (all paths relative to `apps/a-game`):

- `animations/man_and_woman/slow_waltz_*.blend`: the 60 exact filenames in the inventory and asset manifest, with real authored actions. Each is 121,028–155,933 bytes; total 7,990,452 bytes.
- `animations/man_and_woman/slow_waltz_catalog.json`: complete 60-source timing, figure and support catalog, including the final double reverse spin generation.
- `animations/man_and_woman/slow_waltz_validation.json`: preserved last full scan, 59 passes and one failure. Its double reverse spin hash is stale; its other 59 hashes match current assets.
- `animations/man_and_woman/.gitattributes`: 60 exact-filename ordinary-Git exceptions after size/filter inspection. Existing storage rules remain present.
- `animations/man_and_woman/README.md`: discovery and partial-status links.
- `scripts/create_slow_waltz.py`: reproducible procedural source authoring, figure definitions, paired posing, foot contacts and split-file output. Final double reverse spin refinement is saved but awaits validation.
- `scripts/slow_waltz_support.py`: bounded partner-leg clearance fitting helper.
- `scripts/validate_slow_waltz.py`: saved-source validation and optional review renderer. Latest edit adds every authored key to the fractional/phase samples; this strengthened full scan has yet to execute.
- `scripts/slow_waltz.md`: repertoire, workflow, limitations and explicit paused status.
- `scripts/player_assets/animation_files.py`: initial task repair used a 63-character SHA-256 prefix for long-name chooser references. During rebase, current main already supplied an equivalent indexed-reference repair; that implementation was retained. Both tasks' save/reopen regressions were preserved.
- `scripts/player_assets/test_animation_files.py`: public-API save/reopen regression for distinct long action names.
- This status file and `docs/animation_work_status/slow_waltz_evidence/asset_manifest.json`: per-file current hashes, sizes, roles, ranges and prior validation applicability.
- `docs/animation_work_status/slow_waltz_evidence/archive_manifest.json` and `saved_review_and_logs.tar.gz`: 179 existing diagnostic scripts, logs and PNGs preserved from `/tmp/slow_waltz_tools`. The archive is 27,573,000 bytes and uses ordinary Git. It excludes the downloaded Blender distribution and authentication helper.

Dependencies retrieved through LFS include `man_and_woman3.blend`, `animations/man_and_woman/shared_scene_data.blend`, `man_anatomical_study.blend`, `woman_anatomical_study_speculum.blend`, `dildo.blend`, existing individual animation sources and hair physics mesh resources used by tests. These are existing repository dependencies, rather than task edits or new upload requirements.

## Exact stopping point and saved processes

The final owned authoring process was a focused double reverse spin regeneration. It completed naturally before the process inventory: `double_spin.log` contains `WALTZ_SAVED slow_waltz_double_reverse_spin 49` followed by `Blender quit`. Its current source SHA-256 is `37e41a3f4ed0d64d6472c95451405bf0a731799066773de26964f181f72df1ef`. The previous failing report references `77f4faaec3e2e1b0b525dbd898428fc195a7e32b65eecd696773b706eca5da2f`. The final change uses one-frame samples and opposed swing lanes for this clip. Its effect has not been validated.

At the stop inventory, no owned Blender or suite-runner process remained. No additional animation generation, motion refinement or rendering was started after the stop. Delivery tests completed and their logs are archived. The earlier full overview render was intentionally terminated after 32 midpoint images during prior refinement; these are partial and some predate changed assets.

All Blender authoring, scripting, rendering and Blender test work used official Blender **5.2.2 LTS**, build `d13f752e3b9c`, at `/tmp/slow_waltz_tools/blender-5.2.2-linux-x64/blender`; the download checksum was verified. System `/usr/bin/blender` is 4.3.2 and is unsuitable for resuming this task. The `/tmp` executable and original logs are environment-local; durable evidence is in the archive.

## Validation and review evidence

Run these commands from the app directory. `BLENDER` below refers to the explicit 5.2.2 executable above.

| Command/check | Recorded result |
| --- | --- |
| `python tests/run_tests.py --suite fast` | Stop-time run: 10/10 passed; `stop_fast.log`. An earlier run failed on hair mesh LFS pointers; fetching the real dependencies resolved it. |
| `BLENDER=/tmp/slow_waltz_tools/blender-5.2.2-linux-x64/blender python tests/run_tests.py --suite changed --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_paired_animation_authoring.py --changed scripts/player_assets/test_motion_review.py` | Stop-time run: 14/14 passed (10 fast + 4 Blender entries); `stop_focused.log`. Includes the new long-name regression. |
| `python -m py_compile scripts/create_slow_waltz.py scripts/validate_slow_waltz.py scripts/slow_waltz_support.py` | Passed after stopping. |
| `git diff --check` | Passed after stopping. |
| `LP_NUM_THREADS=4 "$BLENDER" --threads 4 --background animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_slow_waltz.py` | Last pre-stop full run: 59/60 passed; `delivery_validation.log`. Double reverse spin failed leg-proxy clearance (minimum gap -0.0102074 m; allowed overlap 0.005 m). The current source and every-authored-key validator revision postdate this run. |
| `LP_NUM_THREADS=4 "$BLENDER" --threads 4 --background animations/man_and_woman/slow_waltz_position_closed.blend --disable-autoexec --python-exit-code 1 --python /tmp/slow_waltz_tools/check_delivery.py` | Pre-stop pass: individual source composes editable Man/Woman rigs; `source_delivery.log`. |
| `LP_NUM_THREADS=4 "$BLENDER" --threads 4 --background man_and_woman3.blend --disable-autoexec --python-exit-code 1 --python /tmp/slow_waltz_tools/check_delivery.py` | Pre-stop pass: 60 chooser clips and 120 participant bindings; `combined_delivery.log`. The diagnostic script is archived. |
| SHA-256 comparison of all 60 current sources with the preserved report | 59 matching prior passes; double reverse spin changed and awaits validation. Exact hashes in `asset_manifest.json`. |

The saved scan checks finite keys, paired bindings, movement, evaluated IK reach, joined palms, planted contacts, mesh floor clearance, torso/leg proxies, same-character foot separation, and loop pose/orientation/velocity. Tolerances: IK 0.005 m, palm gap 0.018 m, planted landmark drift 0.008 m, floor penetration 0.01 m, loop position 0.0001 m and velocity 0.08 m/s. Its sampling covers fractional frames, phase boundaries, quarter cycles and endpoints; the pending strengthened version also includes all authored key times. Proxy clearance is not a complete surface-collision or physical-balance proof. A diagnostic of the previous double reverse spin found worse overlap at frame 44, motivating that added key-time coverage.

Existing rendered evidence includes 76 playback PNGs at four-frame intervals for box step (0–96), natural spin turn (0–96), closed-to-promenade (0–48), and throwaway oversway (0–48), plus four inspected contact sheets. These four clips retain matching report hashes. The archive also retains 32 partial overview renders and older iteration renders/logs; their chronological filenames do not constitute approval of current asset bytes. All-clip visual review remains incomplete.

## Remaining work and concrete blockers

1. The user's stop instruction blocks further animation work until explicit resumption.
2. Validate the newly saved double reverse spin and then all 60 sources with every-key sampling. Preserve the old report before replacing it. Its previous leg-overlap failure remains an unresolved risk for the current source.
3. Review every figure and transition in playback for dance accuracy, knee/foot crossing, contact appearance, wrists/fingers, support and whole-body clearance. Compact procedural families require further choreography work before a completed repertoire claim.
4. Validate assembled figure-to-figure blends and support-foot compatibility; entry/exit labels alone do not establish a smooth continuous routine.
5. Revisit key density and natural rise/fall after clearance corrections. Expanded sampling can reveal additional failures.
6. Baking, runtime export and any requested runtime asset uploads remain separate future work. No new LFS objects belong to this checkpoint: all new binary files meet the ordinary-Git size limit.

Delivery tests have no remaining environmental blocker. Runtime tests initially required real LFS hair meshes; they now pass. A fresh environment must retrieve linked LFS dependencies and install/locate Blender 5.2 before resuming. Software rendering previously emitted EGL initialization warnings and still produced the saved images.

## Exact resume commands (future authorization required)

These commands are recorded for a future resumed task; they were not run after the stop instruction. From the same cloud checkout:

```sh
cd /workspace/sanjo-solutions/apps/a-game
export BLENDER=/tmp/slow_waltz_tools/blender-5.2.2-linux-x64/blender
"$BLENDER" --version
# Current main requires bundled animation tools; retain the same Blender profile.
"$BLENDER" --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
mkdir -p .cache/slow_waltz
cp animations/man_and_woman/slow_waltz_validation.json .cache/slow_waltz/pre_resume_validation.json
# Full saved-source validation, including the changed double reverse spin.
LP_NUM_THREADS=4 "$BLENDER" --threads 4 --background animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_slow_waltz.py
# After diagnosing and editing choreography, regenerate only the intended clip.
LP_NUM_THREADS=4 "$BLENDER" --threads 4 --background animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/create_slow_waltz.py -- --only double_reverse_spin
# Validate and render that clip; a focused run replaces the report with a subset.
LP_NUM_THREADS=4 "$BLENDER" --threads 4 --background animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_slow_waltz.py -- --only double_reverse_spin --sequence --render .cache/slow_waltz/double_reverse_spin
# Restore a complete 60-clip validation report before delivery.
LP_NUM_THREADS=4 "$BLENDER" --threads 4 --background animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_slow_waltz.py
python tests/run_tests.py --suite fast
```

For a fresh checkout, retrieve dependencies with `git lfs pull --include='apps/a-game/man_and_woman3.blend,apps/a-game/animations/man_and_woman/*.blend,apps/a-game/man_anatomical_study.blend,apps/a-game/woman_anatomical_study_speculum.blend,apps/a-game/dildo.blend,apps/a-game/playground/hair/physics/*_mesh.res'` from the repository root using configured authentication. Select an installed **5.2** executable explicitly if the recorded temporary executable is absent. Extract the evidence with `tar -xzf docs/animation_work_status/slow_waltz_evidence/saved_review_and_logs.tar.gz -C DESTINATION` after creating `DESTINATION`.

## Exact per-source inventory

All files below are under `animations/man_and_woman/`; every row has Man leader/Woman follower, authored partial-study status, zero bake and zero export. Current bytes and SHA-256 values are in the linked [asset manifest](slow_waltz_evidence/asset_manifest.json).

| Source file | Group | Stored frames | Playback end | Loop | Prior report matches |
| --- | --- | --- | ---: | --- | --- |
| `slow_waltz_back_lock.blend` | Advanced | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_back_whisk.blend` | Foundation | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_backward_left_closed_change.blend` | Foundation | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_backward_right_closed_change.blend` | Foundation | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_basic_weave.blend` | Advanced | 0–96 | 96 | No | Yes; passed earlier scan |
| `slow_waltz_box_step.blend` | Practice | 0–96 | 95 | Yes | Yes; passed earlier scan |
| `slow_waltz_chasse_from_promenade.blend` | Foundation | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_closed_impetus.blend` | Turning | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_closed_telemark.blend` | Turning | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_closed_to_counter_promenade.blend` | Transition | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_closed_to_fallaway.blend` | Transition | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_closed_to_open_facing.blend` | Transition | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_closed_to_outside_partner.blend` | Transition | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_closed_to_partner_outside.blend` | Transition | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_closed_to_promenade.blend` | Transition | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_contra_check.blend` | Line | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_counter_promenade_to_closed.blend` | Transition | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_cross_hesitation.blend` | Advanced | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_curved_feather.blend` | Advanced | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_double_reverse_spin.blend` | Advanced | 0–48 | 48 | No | No; changed after failing scan |
| `slow_waltz_drag_hesitation.blend` | Advanced | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_fallaway_to_closed.blend` | Transition | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_fallaway_whisk.blend` | Advanced | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_hesitation_change.blend` | Turning | 0–96 | 96 | No | Yes; passed earlier scan |
| `slow_waltz_hover_corte.blend` | Advanced | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_left_foot_closed_change.blend` | Foundation | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_left_lunge.blend` | Line | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_left_whisk.blend` | Line | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_natural_spin_turn.blend` | Turning | 0–96 | 96 | No | Yes; passed earlier scan |
| `slow_waltz_natural_turn.blend` | Foundation | 0–96 | 96 | No | Yes; passed earlier scan |
| `slow_waltz_open_facing_to_closed.blend` | Transition | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_open_impetus.blend` | Turning | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_open_telemark.blend` | Turning | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_outside_change.blend` | Turning | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_outside_partner_to_closed.blend` | Transition | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_outside_spin.blend` | Advanced | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_oversway.blend` | Line | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_partner_outside_to_closed.blend` | Transition | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_position_closed.blend` | Position | 0–96 | 95 | Yes | Yes; passed earlier scan |
| `slow_waltz_position_counter_promenade.blend` | Position | 0–96 | 95 | Yes | Yes; passed earlier scan |
| `slow_waltz_position_fallaway.blend` | Position | 0–96 | 95 | Yes | Yes; passed earlier scan |
| `slow_waltz_position_open_facing.blend` | Position | 0–96 | 95 | Yes | Yes; passed earlier scan |
| `slow_waltz_position_outside_partner.blend` | Position | 0–96 | 95 | Yes | Yes; passed earlier scan |
| `slow_waltz_position_partner_outside.blend` | Position | 0–96 | 95 | Yes | Yes; passed earlier scan |
| `slow_waltz_position_promenade.blend` | Position | 0–96 | 95 | Yes | Yes; passed earlier scan |
| `slow_waltz_progressive_chasse_right.blend` | Foundation | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_promenade_to_closed.blend` | Transition | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_reverse_box_step.blend` | Practice | 0–96 | 95 | Yes | Yes; passed earlier scan |
| `slow_waltz_reverse_corte.blend` | Turning | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_reverse_pivot.blend` | Advanced | 0–16 | 16 | No | Yes; passed earlier scan |
| `slow_waltz_reverse_turn.blend` | Foundation | 0–96 | 96 | No | Yes; passed earlier scan |
| `slow_waltz_right_foot_closed_change.blend` | Foundation | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_right_lunge.blend` | Line | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_running_spin_turn.blend` | Advanced | 0–96 | 96 | No | Yes; passed earlier scan |
| `slow_waltz_throwaway_oversway.blend` | Line | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_turning_lock.blend` | Advanced | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_turning_lock_right.blend` | Advanced | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_weave_from_promenade.blend` | Advanced | 0–96 | 96 | No | Yes; passed earlier scan |
| `slow_waltz_whisk.blend` | Foundation | 0–48 | 48 | No | Yes; passed earlier scan |
| `slow_waltz_wing.blend` | Advanced | 0–48 | 48 | No | Yes; passed earlier scan |

## Integration preparation

Fetched `origin/main` at `074c6a02e` and rebased the checkpoint. Combined all concurrent README and exact-filename storage additions. Retained main's indexed long-name reference implementation and both regression tests. The animation binaries and their manifest hashes remain unchanged. Delivery verification is repeated after conflict resolution; its results are recorded in the follow-up documentation commit.

After conflict resolution, fast checks passed 10/10 and the focused suite passed 14/14, including both long-name regression fixtures. Logs are preserved as `slow_waltz_evidence/rebased_fast.txt` and `rebased_focused.txt`; `.gdignore` isolates this evidence directory. `python scripts/lfs_policy.py check` passed for the staged repository. All 60 committed source blobs still match their exact inventory hashes. The separate `AGENTS.md` documentation update records the paused checkpoint, every-key sampling, and evaluated turning-support landmarks. No authoring or rendering resumed.

Final integration fetched newer main at `1e89ec851` immediately before merging. Documentation and exact-file attribute conflicts were combined to retain every task's additions. The merged fast suite passed 10/10 (`slow_waltz_evidence/merged_fast.txt`), and the storage-policy check passed for 25,462 staged files before adding that log. The paired-animation tooling implementation remained the already-tested main implementation. The merge commit and final verified remote hash are reported in the delivery response.

An ordinary push was rejected because another chat advanced main. Fetched `764e18133` and merged its changes, preserving Boogie-woogie documentation and new asset-metadata handling in the shared writer. Repeated the changed suite for `test_animation_files.py`: 11/11 passed, including all ten fast checks (`slow_waltz_evidence/retry_focused.txt`). Storage policy passed. The full merge whitespace check reported two pre-existing whitespace lines in the incoming Forro diagnostic logs; those historical logs were preserved. The task-scoped whitespace check passed.
