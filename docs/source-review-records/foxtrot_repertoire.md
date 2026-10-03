# Foxtrot repertoire — preserved work status

- Date: 2026-10-02 (UTC).
- Chat/task title: Foxtrot repertoire for man_and_woman3.blend (task label).
- Checkout: `/workspace/sanjo-solutions/apps/a-game` in the sanjo-solutions cloud environment.
- Task branch at stop: `codex/foxtrot-repertoire`.
- Current commit at stop: `3c52737c74b488501e9cfe47e7029547c6f5fe88`.
- Delivery instruction: stop authoring, refining, generating, and rendering; preserve the present state and integrate it into main. Resume commands below require a later explicit instruction to resume.

## Scope and state

The original scope requested coordinated Foxtrot moves and positions for both characters, broad organized coverage, natural motion, planted contacts, body clearance, smooth transitions, interpolated and loop validation, reuse where suitable, Blender 5.2 throughout, individual animation files, commits/rebase/documentation/main push and asset delivery.

**This is a preservation checkpoint of partial procedural blocking studies, not a completed or production-validated Foxtrot repertoire.** There are 50 editable paired source files: 6 position loops, 28 International figure interpretations, 8 American social figures, and 8 directed position transitions. Every clip assigns Man.rigify as leader and Woman.rigify as follower, synchronized through two action slots and matching NLA bindings. Advanced figures use compact stepping interpretations; exact syllabus heel turns/pivots, all regional variations, physical balance, and natural presentation still require choreography review. No Foxtrot baked deform actions, exported GLBs, runtime integration, or published previews were completed.

Authored timing is 24 fps and 120 beats/minute: S = 24 frames, Q = 12 frames. Position loops store 0–96 and play 0–95; figures and transitions play once. Rig roots stay fixed while torso and world-space limb controls carry travel. The catalog contains markers, rhythm, positions, contact intervals, travel displacement, and heading changes. Shared scene and character sources remain unchanged by this task.

## Durable files

All paths in this record are relative to `apps/a-game` unless absolute.

- `scripts/create_foxtrot.py`: paired procedural IK authoring, support/swing phases, calibrated palm holds, rise/sway, quaternion finger poses, position loops and transitions; sparse sampled keys and stationary curve reduction. The latest counter-promenade adjustment is saved in code but fails before producing its first replacement source.
- `scripts/foxtrot_repertoire.py`: declarative figure/step/rhythm/turn/position definitions.
- `scripts/validate_foxtrot.py`: saved-source checks, fractional-frame sampling, contact/clearance/loop/transition checks, review and playback rendering. Its final added pre/post source-hash assertion has yet to run.
- `scripts/foxtrot.md`: authoring, timing, coverage, review, storage and runtime guide, marked with this checkpoint's partial status.
- `animations/man_and_woman/foxtrot_catalog.json`: all 50 authored clip records.
- `animations/man_and_woman/foxtrot_validation.json`: preserved **stale focused failure report**, one earlier feather-ending revision (SHA-256 `5177258ad1d57c22476ac618a868dd053e54134699583230b0a2e09bf7f62381`). This is neither a full report nor validation of the current feather-ending source.
- `animations/man_and_woman/.gitattributes`: 50 exact filename exceptions store these small Blender sources directly in Git; other assets retain their storage policy.
- `scripts/player_assets/animation_files.py`: preserves linked actions with names longer than Blender's 63-byte custom-property key limit by using deterministic short SHA-256 retention keys; full action labels remain intact. During rebase, concurrent main already supplied an equivalent numeric retention-key fix. That main implementation was retained, along with both its regression and this task’s Unicode/shared-prefix regression.
- `scripts/player_assets/test_animation_files.py`: regression through file write/link/save/reopen, including long shared-prefix ASCII and multibyte Unicode names.
- `docs/animation_work_status/foxtrot_preservation_manifest.json`: exact source byte sizes, hashes, ranges, roles, authored/baked/exported status, stopped-audit results and current-hash comparisons, plus every archived evidence filename/hash.
- `docs/animation_work_status/foxtrot_preserved_outputs.tar.gz`: complete saved Foxtrot cache evidence except Python bytecode. Contains logs, temporary diagnostic/repair scripts, regression summary, and all 234 PNG outputs. Extracted archive root is `foxtrot/`.

Existing paired IK/Acro Yoga authoring APIs and the disco finger-posing pattern were reused; the solo disco clip's rhythm/arm motion was unsuitable as paired Foxtrot choreography. Linked dependencies are `animations/man_and_woman/shared_scene_data.blend`, `man_anatomical_study.blend`, `woman_anatomical_study_speculum.blend`, and `dildo.blend`. `man_and_woman3.blend` remains the combined discovery entry point.

## Asset inventory

All rows are authored procedural studies; **baked: no; exported: no**. All use both roles stated above. A passing row below means the stopped numerical screening passed for the matching bytes; it does not certify choreography or complete visual/physical review. Exact SHA-256 hashes are in the preservation manifest.

| Source under animations/man_and_woman/ | Category | Stored frames | Playback | Bytes | Latest stopped audit |
| --- | --- | --- | --- | ---: | --- |
| `foxtrot_position_closed.blend` | Position | 0–96 | Loop 0–95 | 124,079 | Pass in stopped audit |
| `foxtrot_position_outside_partner.blend` | Position | 0–96 | Loop 0–95 | 124,712 | Pass in stopped audit |
| `foxtrot_position_counter_promenade.blend` | Position | 0–96 | Loop 0–95 | 124,613 | Pass in stopped audit |
| `foxtrot_position_open_facing.blend` | Position | 0–96 | Loop 0–95 | 123,712 | Pass in stopped audit |
| `foxtrot_position_side_by_side.blend` | Position | 0–96 | Loop 0–95 | 123,788 | Pass in stopped audit |
| `foxtrot_feather_step.blend` | Figure | 0–48 | Once | 129,193 | Pass in stopped audit |
| `foxtrot_three_step.blend` | Figure | 0–48 | Once | 128,059 | Pass in stopped audit |
| `foxtrot_reverse_turn.blend` | Figure | 0–96 | Once | 164,567 | Pass in stopped audit |
| `foxtrot_natural_turn.blend` | Figure | 0–96 | Once | 164,464 | Pass in stopped audit |
| `foxtrot_closed_impetus.blend` | Figure | 0–48 | Once | 142,924 | Pass in stopped audit |
| `foxtrot_basic_weave.blend` | Figure | 0–72 | Once | 158,016 | Pass in stopped audit |
| `foxtrot_change_of_direction.blend` | Figure | 0–72 | Once | 144,126 | Pass in stopped audit |
| `foxtrot_reverse_wave.blend` | Figure | 0–96 | Once | 163,466 | Pass in stopped audit |
| `foxtrot_hover_feather.blend` | Figure | 0–72 | Once | 131,956 | Pass in stopped audit |
| `foxtrot_closed_telemark.blend` | Figure | 0–48 | Once | 143,681 | Pass in stopped audit |
| `foxtrot_natural_weave.blend` | Figure | 0–84 | Once | 158,498 | Pass in stopped audit |
| `foxtrot_curved_feather.blend` | Figure | 0–48 | Once | 143,435 | Pass in stopped audit |
| `foxtrot_back_feather.blend` | Figure | 0–48 | Once | 127,664 | Pass in stopped audit |
| `foxtrot_natural_zigzag.blend` | Figure | 0–96 | Once | 159,856 | Pass in stopped audit |
| `foxtrot_natural_hover_cross.blend` | Figure | 0–96 | Once | 166,807 | Pass in stopped audit |
| `foxtrot_top_spin.blend` | Figure | 0–48 | Once | 148,130 | Current revision pending |
| `foxtrot_reverse_pivot.blend` | Figure | 0–24 | Once | 136,438 | Current revision pending |
| `foxtrot_natural_pivot.blend` | Figure | 0–48 | Once | 135,416 | Current revision pending |
| `foxtrot_running_weave.blend` | Figure | 0–84 | Once | 158,054 | Current revision pending |
| `foxtrot_social_basic.blend` | Figure | 0–72 | Once | 130,716 | Current revision pending |
| `foxtrot_social_reverse_basic.blend` | Figure | 0–72 | Once | 131,065 | Current revision pending |
| `foxtrot_social_box.blend` | Figure | 0–96 | Once | 134,001 | Current revision pending |
| `foxtrot_social_left_turning_box.blend` | Figure | 0–96 | Once | 164,107 | Current revision pending |
| `foxtrot_social_sway_step.blend` | Figure | 0–72 | Once | 128,308 | Current revision pending |
| `foxtrot_social_rock_turn.blend` | Figure | 0–72 | Once | 144,359 | Current revision pending |
| `foxtrot_social_side_by_side_walks.blend` | Figure | 0–72 | Once | 129,720 | Current revision pending |
| `foxtrot_closed_to_counter_promenade.blend` | Transition | 0–96 | Once | 130,573 | Current revision pending |
| `foxtrot_counter_promenade_to_closed.blend` | Transition | 0–96 | Once | 131,063 | Current revision pending |
| `foxtrot_closed_to_open_facing.blend` | Transition | 0–96 | Once | 125,344 | Current revision pending |
| `foxtrot_open_facing_to_closed.blend` | Transition | 0–96 | Once | 126,385 | Current revision pending |
| `foxtrot_feather_finish.blend` | Figure | 0–48 | Once | 144,131 | Current revision pending |
| `foxtrot_position_promenade.blend` | Position | 0–96 | Loop 0–95 | 125,140 | Current revision pending |
| `foxtrot_open_impetus.blend` | Figure | 0–48 | Once | 144,192 | Current revision pending |
| `foxtrot_weave_from_promenade.blend` | Figure | 0–72 | Once | 157,688 | Current revision pending |
| `foxtrot_hover_telemark.blend` | Figure | 0–72 | Once | 147,243 | Current revision pending |
| `foxtrot_open_telemark.blend` | Figure | 0–48 | Once | 143,180 | Current revision pending |
| `foxtrot_outside_swivel.blend` | Figure | 0–72 | Once | 144,894 | Current revision pending |
| `foxtrot_fallaway_reverse_slip_pivot.blend` | Figure | 0–60 | Once | 147,219 | Current revision pending |
| `foxtrot_bounce_fallaway.blend` | Figure | 0–72 | Once | 157,245 | Current revision pending |
| `foxtrot_social_promenade_walks.blend` | Figure | 0–72 | Once | 136,545 | Current revision pending |
| `foxtrot_feather_ending.blend` | Figure | 0–48 | Once | 133,310 | Current revision pending |
| `foxtrot_closed_to_outside_partner.blend` | Transition | 0–96 | Once | 130,557 | Current revision pending |
| `foxtrot_outside_partner_to_closed.blend` | Transition | 0–96 | Once | 130,792 | Current revision pending |
| `foxtrot_closed_to_promenade.blend` | Transition | 0–96 | Once | 139,090 | Current revision pending |
| `foxtrot_promenade_to_closed.blend` | Transition | 0–96 | Once | 137,660 | Current revision pending |

## Verification and known failures

Commands were run from the app with:

```sh
export BLENDER=/workspace/.cloud-onboarding/3d-tools/blender-5.2.2/blender
export GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot
```

Blender work used Blender 5.2.2 LTS, build `d13f752e3b9c`. The system Blender 4.3.2 was only version-inspected.

- `python tests/run_tests.py --suite fast`: **10/10 passed**, rerun after stopping (6.32 seconds); evidence `preservation_fast.log`.
- `python tests/run_tests.py --suite changed --changed scripts/player_assets/test_animation_files.py`: **11/11 passed**, including all 10 fast checks and the file workflow regression (9.19 seconds); `preservation_verification.log`. Temporary test fixtures are the only Blender work during preservation verification.
- Earlier `python tests/run_tests.py --slow-timeout 120`: **47/67 passed** in 1631.79 seconds. Twenty failures include missing GRT_Action_Bakery, interactable_fast_mode and Quick Finger Collision properties/operators, Godot resource/UID/RID diagnostics and runtime assertions, and timeouts. This broad run predates the final retention-key fix; results are not a clean current baseline and are not all attributed to Foxtrot. `suite.log` and `regression_summary.json` preserve exact failures.
- `"$BLENDER" -t 2 -b man_and_woman3.blend --disable-autoexec --python-exit-code 1 --python .cache/foxtrot/check_discovery.py`: **FOXTROT_DISCOVERY_PASS 50**, with both rig NLA slots, after fixing long retention keys (`discovery_final.log`). Single-source scene composition also passed (`composition.log`). The temporary discovery script was not retained; equivalent reproduction requires reconstructing that diagnostic from the public AnimationFileLibrary API or using the combined chooser.
- Saved-motion command: `"$BLENDER" -t 2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_foxtrot.py`. The stopped latest full run emitted **20 passing records, then was terminated**; `final_validation.log` and the manifest retain those records. The full 50-clip report was never completed. Current-hash matching is recorded individually.
- Numerical screening uses 1.5-frame spacing plus half-frame/end/phase samples, IK tolerance 0.006 m, palm gap 0.022 m, planted drift 0.004 m, floor penetration 0.012 m, loop endpoint 0.0001 m, loop velocity 0.06 m/s, torso capsule separation and leg penetration tolerance 0.01 m. Full mesh floor is sampled at start/mid/end; sole landmarks at every sample. These proxies do not prove complete surface collision or balance.
- An earlier full audit passed 40/50 and failed weave_from_promenade, hover_telemark, fallaway_reverse_slip_pivot, bounce_fallaway, social_promenade_walks, closed_to_outside_partner, promenade_to_closed, closed_to_counter_promenade, counter_promenade_to_closed, and feather_ending. The earlier full log was overwritten by the restarted audit; this is historical context, not current certification. Wider promenade spacing later passed a focused weave check (`wider_weave_validation.log`, minimum leg clearance +0.02573 m).
- Wider feather-ending focused validation still failed IK 0.021788 m and planted drift 0.021928 m at frame 36, Woman.rigify foot.L; leg clearance improved to +0.02473 m (`wider_ending_validation.log`). A shortened second quick was saved afterward and awaits validation.
- The last partially successful generator run (`transition_refinement.log`) saved feather_ending, closed_to_outside_partner, outside_partner_to_closed, closed_to_promenade, and promenade_to_closed. It then failed closed_to_counter_promenade at follower.right_palm distance 0.00442 m versus the solver's 0.002 m limit. These five sources include the latest applicable shorter-step/lower-lift/denser-transition refinements.
- The latest run (`counter_refinement.log`) saved **zero** sources: follower.right_palm distance 0.00370 m still exceeded 0.002 m on closed_to_counter_promenade. Counter/open transition files retain earlier authored versions. Latest generator code therefore cannot regenerate the complete set successfully.
- Finger curve repair/alignment was saved before stopping, matching the shared rigs' quaternion finger modes while retaining native Euler modes on other controls (`finger_repair.log`, `finger_alignment.log`, `finger_modes.log`). Existing checks cover only the audited subset after the final changes.

## Processes and saved visual outputs

At the stop request, owned Blender validator PID 6115 and playback renderer PID 6118 were terminated with SIGTERM. The overview renderer had already stopped; the counter-promenade authoring process had exited with failure. A subsequent process scan found no owned Blender authoring/validation/render process. Verification test processes completed normally. No authoring or rendering continued after the stop request.

The archive preserves all output frames, including older revisions: first_review 6 PNGs, feather_review 3, review 18, review_final 45, overview 82, playback 79, and one position_review.png montage. Overview contains one frame for each position/figure and five per transition, but some cached images represent earlier revisions; they are review evidence, not final validation. Playback contains feather_step frames 0–48 (17 images), reverse_turn 0–96 (33), and **partial** closed_to_promenade 0–84 (29), all every three frames for playback at 8 fps. No video was assembled. The manifest identifies every retained file and checksum; provenance to exact source revisions is incomplete for older renders.

## Remaining work and blockers

1. Wait for explicit authorization to resume animation work.
2. Resolve counter-promenade follower hand reach while preserving ergonomic wrists, support, and clearance; update the latest failing generator only after authorization.
3. Complete generation of affected counter/open transitions; reconcile all saved sources with the generator revision and catalog.
4. Revalidate all 50 saved files in a fresh Blender 5.2 process, retaining a complete report with hashes. Recheck feather ending, widened promenade figures, leg clearance, floor contacts, transitions and loop velocity.
5. Complete visual playback review of every figure and both roles; refine advanced choreography, body clearance, natural motion and inter-figure alignment. Some clips are compact procedural interpretations rather than complete named-syllabus mechanics.
6. Resolve environment/add-on/runtime test failures before claiming full suite success. Baking/export requires the existing add-on workflow and remains outstanding.
7. Check linked dependency hashes after integrating concurrent main changes; numerical results here describe the task's pre-integration dependencies.

## Exact resume commands (future authorization required)

Recording and reading evidence:

```sh
cd /workspace/sanjo-solutions/apps/a-game
mkdir -p .cache/foxtrot_preserved
tar -xzf docs/animation_work_status/foxtrot_preserved_outputs.tar.gz -C .cache/foxtrot_preserved
export BLENDER=/workspace/.cloud-onboarding/3d-tools/blender-5.2.2/blender
export GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot
"$BLENDER" --version
python tests/run_tests.py --suite fast
python tests/run_tests.py --suite changed --changed scripts/player_assets/test_animation_files.py
```

The following first reproduces the known authoring blocker and writes sources only if it succeeds. Fix the solve before attempting a full rebuild; preserve this checkpoint in Git.

```sh
"$BLENDER" -t 2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/create_foxtrot.py -- --only closed_to_counter_promenade
"$BLENDER" -t 2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/create_foxtrot.py
"$BLENDER" -t 2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_foxtrot.py
"$BLENDER" -t 2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_foxtrot.py -- --render-only --playback --only foxtrot_feather_step foxtrot_reverse_turn foxtrot_closed_to_promenade --render .cache/foxtrot/resumed_playback
```

Focused validator runs overwrite the shared validation JSON with their selected subset. Use a full run for the final report. Use a fresh render directory after changes to avoid mixing cached revisions. For a requested runtime delivery, open each validated source with Player Asset Export, use **Bake & Export Active Animation**, and save the individual source to retain its bake; baking/export has not been performed here.

## Storage and integration

All 50 new Blender binaries and the evidence archive are below 104,857,600 bytes and stored directly in Git. The source exceptions are scoped to the 50 exact filenames; the archive has no LFS filter. Existing shared sources retain LFS. No new LFS objects require upload for this checkpoint. Byte sizes, source/dependency hashes, and archive checksum are in the manifest. Before staging, all 51 new binary files passed the 104,857,600-byte limit and attribute checks; shared_scene_data.blend retained filter=lfs. Python syntax parsing and git diff --check passed. The preservation commit is followed by fetch/rebase, an Animation-section guidance commit, then current-main integration and an ordinary push. Delivery hashes and remote inclusion verification belong to the final response, avoiding a self-referential commit hash in this file.

### Post-rebase verification

The checkpoint rebased onto `43b08e485` from origin/main. Conflicts retained all existing storage entries, main’s numeric action-reference keys, and both long-name regression tests. The four recorded linked dependency hashes remained unchanged. The focused suite, including all ten fast checks, passed **11/11 in 8.64 seconds** after integration; see `foxtrot_integration_verification.log`. `python scripts/lfs_policy.py check` from the repository root passed for all 24,086 staged files. The Animation section of `AGENTS.md` gained the Foxtrot status/report-subset guidance and the action-label versus retention-key distinction.

The final integration started from newer origin/main `4fb068970`; additive documentation and storage conflicts preserved both chats’ content. The merged file-workflow run passed **11/11 in 8.80 seconds**, including all fast checks (`foxtrot_merge_verification.log`). The policy check passed for 25,650 staged files before adding that final verification log.

Further ordinary push races integrated remote main through `f76f8f5bc`, retaining additional long-action-name regression coverage from both branches. The resulting focused/fast run passed **11/11 in 8.95 seconds** (`foxtrot_final_integration_verification.log`). Repository-wide storage policy passed. Raw diagnostic whitespace from concurrent country-swing/forró logs was preserved; those pre-existing remote logs produced diff-check whitespace warnings during integration.
