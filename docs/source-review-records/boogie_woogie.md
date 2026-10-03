# Boogie-woogie preservation status

Recorded 2026-10-02 (UTC). Task/chat description: “Boogie-woogie partner animations for A-Game”; the desktop chat title is unavailable to this checkout. Branch at stop: `codex/boogie-woogie`. Starting/current pre-delivery commit: `3c52737c74b488501e9cfe47e7029547c6f5fe88`. Delivery commits follow this snapshot; consult this file’s Git history for their identities.

## Stop instruction and scope

The user instructed all active animation chats to stop production and preserve their present state. The owned authoring and validation processes were terminated with SIGTERM. Further choreography, refinement, generation, and rendering are paused. Verification and repository delivery continued.

The original request covered a broad organized Boogie-woogie repertoire for both characters in `man_and_woman3.blend`, using Blender 5.2 and the existing per-animation workflow, with natural motion, planted contacts, body clearance, transitions, interpolated checks, and loop continuity. It also requested ordinary Git for assets through 104,857,600 bytes, scoped storage exceptions, documentation, commits, integration with concurrent main, and push. Dance vocabulary varies by school; the current catalog is a bounded common-social-dance selection.

## Saved state

**48 authored procedural blocking studies; 0 baked actions delivered; 0 Godot/GLB runtime exports.** All 48 files finished an initial save before the stop. Five refinements were saved immediately before termination. These are partial choreography assets with known and pending quality findings, rather than a completed, fully validated repertoire.

Each source has one coordinated action for `Man.rigify` (Man, lead/player) and `Woman.rigify` (Woman, follow/partner), synchronized slots and NLA metadata. Timing is 24 fps / 120 BPM. Eight position loops, twelve footwork clips, fourteen directed transitions, and fourteen figures are cataloged. Stored closing poses are excluded from cyclic playback; directed clips play once. Shared scenes, original characters, and the combined library were read rather than resaved.

Files relative to `apps/a-game`:

- `animations/man_and_woman/boogie_woogie_*.blend`: the 48 sources listed below, 123,803–202,241 bytes each.
- `animations/man_and_woman/boogie_woogie_catalog.json`: all 48 names, roles, formations, frames, markers, footfalls, and playback ranges.
- `animations/man_and_woman/boogie_woogie_validation.json`: last completed report, covering 32 sources under the earlier checks. It reports four failures; five report hashes now refer to earlier source versions. Preserve this historical evidence alongside the current inventory.
- `animations/man_and_woman/previews/boogie_woogie_basic_six_count.gif` (887,885 bytes) and `boogie_woogie_charleston.gif` (1,103,067 bytes): two Blender 5.2 playback previews, sampled every third source frame and packaged at 8 fps. These are review media, rather than runtime exports.
- `scripts/create_boogie_woogie.py`: repeatable paired authoring, sparse world-space plants, calibrated palms, timing/formation catalog, and loop playback metadata. Reuses the existing Rigify yoga pose capture, disco wrist helper, paired solver, and animation writer. Existing choreography files retain their contents.
- `scripts/validate_boogie_woogie.py`: reload, slots, NLA, finite keys, native wrist/finger controls, IK/plant/contact/floor checks, mesh overlap sampling, loop checks, source/input hashes, and canonical transition joins. Its latest angular-velocity and join checks have only partially run.
- `scripts/player_assets/animation_files.py` and `test_animation_files.py`: preserve action Asset Browser description, author, catalog, and tags through split-file copying, with a reopening regression check.
- `scripts/boogie_woogie.md` and `animations/man_and_woman/README.md`: coverage/workflow and explicit paused-state links.
- `animations/man_and_woman/.gitattributes` and `previews/.gitattributes`: exact-filename ordinary-Git exceptions for these 48 sources and two GIFs. Existing other-asset settings remain applicable.
- `docs/animation_work_status/boogie_woogie_evidence/asset_inventory.json`: exact saved asset sizes and SHA-256 values, frame ranges, roles, and applicable validation state.
- `docs/animation_work_status/boogie_woogie_evidence/`: preserved build, interrupted validation, diagnostic, source-opening, and delivery test logs; `interrupted_validation_results.json` extracts the eight completed checks from the interrupted process, explicitly marking the run incomplete.

## Validation and concrete blockers

The last completed 32-source report contains 28 passing entries and four overlap failures. Five source hashes changed during the last refinement, so their old results are stale. Its remaining 27 entries match their saved source hashes. The interrupted newer run completed eight additional source checks: five passed sampled checks and three failed. These completed entries are preserved separately, rather than presented as a completed full-library report.

Known findings:

- Earlier saved promenade/side-by-side transition pairs crossed body surfaces at frames 66–78. The widened-path probe reported zero overlaps at frames 66, 72, and 78, and all four refined sources were saved. Complete interpolated validation of those current files is pending.
- `open_to_shadow` was saved with the new endpoint wrist fade; validation is pending. `shadow_to_open` retains its previous saved source because termination occurred after its `BOOGIE_BEGIN` and before `BOOGIE_SAVED`. The current generator therefore contains a change that is still pending for that file.
- Earlier shadow endpoint comparisons found up to 0.120718 m / 1.416813 rad mismatch against canonical position poses. The current shadow pair requires saved-file endpoint verification; generator reach probes alone establish a narrower result.
- The interrupted newer check found `partner_surface_overlap` in `open_to_cuddle` (21 body triangle pairs at frame 72), `cuddle_to_open` (50 at frame 72), and `tuck_turn` (5 at frame 66). These are current saved-source failures.
- Heel/toe plant orientation and floor issues were corrected and its saved-file earlier check passed. Its newer run reused the matching source result; full newer angular-loop verification across the library remains pending.
- Contact-region intersections within 14 cm of calibrated palm centers are reported separately and allowed by the sampled body test. Fingers/wrists still require visual assessment. Surface sampling every six frames plus phase points does not prove continuous clearance or physical balance.
- All-48 visual review, combined-library chooser review, complete current-source interpolated validation, and full angular loop/join review remain pending. Existing previews cover two clips and selected still-image diagnostics only.

The validator samples rig/contact/foot-floor behavior every half frame and at keys. Earlier tolerances: IK reach 0.005 m, planted drift 0.004 m, planted angle 0.005 rad, palm gap 0.025 m, skin floor −0.01 m, torso spacing 0.4 m, loop position 0.0001 m, loop angle 0.001 rad, linear seam velocity 0.15 m/s. The latest script adds angular seam velocity 0.30 rad/s and canonical join checks at 0.0001 m / 0.001 rad. Newer checks require a complete run before claiming those thresholds across all sources.

## Processes and environment

At stop, owned author PID 5174 was generating the six transition refinements; PID 5192 was validating the other 42 requested clips. Both received SIGTERM and exited. Five refinement save messages were preserved (promenade pair, side-by-side pair, open-to-shadow); shadow-to-open had only begun. The interrupted validator produced eight complete JSON results before termination. There are no remaining owned Boogie-woogie Blender processes.

Official SHA-verified Blender executable: `/workspace/tools/blender52/blender`, version 5.2.2 LTS, build `d13f752e3b9c`. All Blender authoring, inspection, rendering, and Blender tests used this release. Godot is 4.6.3. The system Blender 4.3.2 was only queried for its version.

Linked Git LFS prerequisites retrieved: `man_and_woman3.blend`, `animations/man_and_woman/shared_scene_data.blend`, `man_anatomical_study.blend`, `woman_anatomical_study_speculum.blend`, and linked `dildo.blend`; existing split sources were also retrieved for discovery. Their existing storage/content remain intact. An earlier fast-suite failure came from three hair mesh LFS pointers; restoring their cached objects resolved it. Initial Git authentication failed, then a retry with the configured environment credential succeeded. These were preparation issues, rather than current choreography blockers.

Additional temporary diagnostics remain in `.cache/boogie_woogie/{review,positions,final_review,playback}` and `/tmp/boogie_*.log` in this workspace. They include earlier pose versions and are temporary review material. Durable review outputs are the two GIFs and copied evidence logs. The committed inventory identifies the authoritative saved source bytes.

## Verification at preservation

Commands executed from `apps/a-game` after stopping production:

```sh
BLENDER=/workspace/tools/blender52/blender python tests/run_tests.py --suite fast
BLENDER=/workspace/tools/blender52/blender python tests/run_tests.py --suite changed \
  --changed scripts/player_assets/test_paired_animation_authoring.py \
  --changed scripts/player_assets/test_animation_management.py \
  --changed scripts/player_assets/test_animation_files.py
python -m py_compile scripts/create_boogie_woogie.py scripts/validate_boogie_woogie.py
git diff --check
```

Results: fast **10/10 passed** (6.18 s); focused suite including fast **14/14 passed** (11.48 s); Python compilation and whitespace checks passed. Evidence logs are `stop_fast.log` and `stop_related.log`. These fixture/tooling tests establish tooling health; the choreography failures above remain open.

Earlier actual source composition through `scripts/player_assets/animation_file_startup.py` passed for `boogie_woogie_basic_six_count`, with both participant slots and native playback 0–71; preserved output is `source_open.log`. No all-library runtime bake or export was attempted.

## Per-source inventory

All rows are authored procedural blocking studies, with baked/exported states both false and Man lead / Woman follow. Range is stored start–end followed by native playback end. “PASS sampled checks” applies only to the named saved hash and corresponding report scope, rather than full production readiness.

| Source in `animations/man_and_woman/` | Stored / playback end | Playback | Bytes | Recorded validation |
| --- | --- | --- | ---: | --- |
| `boogie_woogie_basic_eight_count.blend` | 0–96 / 95 | Loop | 146656 | Earlier report: PASS sampled checks |
| `boogie_woogie_basic_six_count.blend` | 0–72 / 71 | Loop | 141926 | Earlier report: PASS sampled checks |
| `boogie_woogie_boogie_walks.blend` | 0–96 / 95 | Loop | 146845 | Earlier report: PASS sampled checks |
| `boogie_woogie_break_freeze.blend` | 0–72 / 72 | Once | 140936 | Earlier report: PASS sampled checks |
| `boogie_woogie_change_places.blend` | 0–144 / 144 | Once | 199542 | Pending validation |
| `boogie_woogie_charleston.blend` | 0–96 / 95 | Loop | 140662 | Earlier report: PASS sampled checks |
| `boogie_woogie_circle_left.blend` | 0–144 / 144 | Once | 199954 | Pending validation |
| `boogie_woogie_circle_right.blend` | 0–144 / 144 | Once | 201421 | Pending validation |
| `boogie_woogie_closed_basic.blend` | 0–72 / 71 | Loop | 147835 | Earlier report: PASS sampled checks |
| `boogie_woogie_closed_to_open.blend` | 0–144 / 144 | Once | 199787 | Earlier report: PASS sampled checks |
| `boogie_woogie_cuddle_to_open.blend` | 0–144 / 144 | Once | 181298 | Interrupted run: FAIL partner_surface_overlap |
| `boogie_woogie_double_hand_basic.blend` | 0–72 / 71 | Loop | 144435 | Earlier report: PASS sampled checks |
| `boogie_woogie_follower_free_spin.blend` | 0–144 / 144 | Once | 173871 | Interrupted run: PASS sampled checks |
| `boogie_woogie_follower_underarm_left.blend` | 0–144 / 144 | Once | 177309 | Interrupted run: PASS sampled checks |
| `boogie_woogie_follower_underarm_right.blend` | 0–144 / 144 | Once | 175901 | Interrupted run: PASS sampled checks |
| `boogie_woogie_handshake_to_open.blend` | 0–144 / 144 | Once | 157510 | Earlier report: PASS sampled checks |
| `boogie_woogie_heel_toe.blend` | 0–96 / 95 | Loop | 142754 | Earlier report: PASS sampled checks |
| `boogie_woogie_kick_ball_change.blend` | 0–72 / 71 | Loop | 141424 | Earlier report: PASS sampled checks |
| `boogie_woogie_kick_step.blend` | 0–96 / 95 | Loop | 139370 | Earlier report: PASS sampled checks |
| `boogie_woogie_leader_turn_left.blend` | 0–144 / 144 | Once | 185936 | Interrupted run: PASS sampled checks |
| `boogie_woogie_leader_turn_right.blend` | 0–144 / 144 | Once | 185390 | Interrupted run: PASS sampled checks |
| `boogie_woogie_left_side_pass.blend` | 0–144 / 144 | Once | 199363 | Pending validation |
| `boogie_woogie_low_dip_recover.blend` | 0–144 / 144 | Once | 174059 | Pending validation |
| `boogie_woogie_open_double_to_open.blend` | 0–144 / 144 | Once | 159398 | Earlier report: PASS sampled checks |
| `boogie_woogie_open_to_closed.blend` | 0–144 / 144 | Once | 199076 | Earlier report: PASS sampled checks |
| `boogie_woogie_open_to_cuddle.blend` | 0–144 / 144 | Once | 180848 | Interrupted run: FAIL partner_surface_overlap |
| `boogie_woogie_open_to_handshake.blend` | 0–144 / 144 | Once | 157887 | Earlier report: PASS sampled checks |
| `boogie_woogie_open_to_open_double.blend` | 0–144 / 144 | Once | 159655 | Earlier report: PASS sampled checks |
| `boogie_woogie_open_to_promenade.blend` | 0–144 / 144 | Once | 200842 | STALE report; current refinement pending validation |
| `boogie_woogie_open_to_shadow.blend` | 0–144 / 144 | Once | 180604 | STALE report; current refinement pending validation |
| `boogie_woogie_open_to_side_by_side.blend` | 0–144 / 144 | Once | 181525 | STALE report; current refinement pending validation |
| `boogie_woogie_position_closed.blend` | 0–48 / 47 | Loop | 125939 | Earlier report: PASS sampled checks |
| `boogie_woogie_position_cuddle.blend` | 0–48 / 47 | Loop | 123803 | Earlier report: PASS sampled checks |
| `boogie_woogie_position_handshake.blend` | 0–48 / 47 | Loop | 125141 | Earlier report: PASS sampled checks |
| `boogie_woogie_position_open_double.blend` | 0–48 / 47 | Loop | 125666 | Earlier report: PASS sampled checks |
| `boogie_woogie_position_open_single.blend` | 0–48 / 47 | Loop | 125546 | Earlier report: PASS sampled checks |
| `boogie_woogie_position_promenade.blend` | 0–48 / 47 | Loop | 124832 | Earlier report: PASS sampled checks |
| `boogie_woogie_position_shadow.blend` | 0–48 / 47 | Loop | 124841 | Earlier report: PASS sampled checks |
| `boogie_woogie_position_side_by_side.blend` | 0–48 / 47 | Loop | 124631 | Earlier report: PASS sampled checks |
| `boogie_woogie_promenade_to_open.blend` | 0–144 / 144 | Once | 202241 | STALE report; current refinement pending validation |
| `boogie_woogie_right_side_pass.blend` | 0–144 / 144 | Once | 199357 | Pending validation |
| `boogie_woogie_send_out_return.blend` | 0–144 / 144 | Once | 166582 | Pending validation |
| `boogie_woogie_shadow_to_open.blend` | 0–144 / 144 | Once | 180139 | Earlier report: PASS sampled checks |
| `boogie_woogie_side_by_side_to_open.blend` | 0–144 / 144 | Once | 181197 | STALE report; current refinement pending validation |
| `boogie_woogie_sugar_push.blend` | 0–144 / 144 | Once | 166865 | Pending validation |
| `boogie_woogie_swivels.blend` | 0–72 / 71 | Loop | 148255 | Earlier report: PASS sampled checks |
| `boogie_woogie_traveling_triples.blend` | 0–144 / 143 | Loop | 161445 | Earlier report: PASS sampled checks |
| `boogie_woogie_tuck_turn.blend` | 0–144 / 144 | Once | 175597 | Interrupted run: FAIL partner_surface_overlap |

## Resume after a new instruction to continue

From `/workspace/sanjo-solutions/apps/a-game`, first inspect this record and compare hashes with `boogie_woogie_evidence/asset_inventory.json`. Restore linked source objects using the repository’s established LFS workflow if needed. Recheck Blender’s version. The following are future resume commands, rather than steps performed after the stop:

```sh
BLENDER=/workspace/tools/blender52/blender
"$BLENDER" --version
"$BLENDER" --background --threads 4 animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/create_boogie_woogie.py -- \
  --only open_to_promenade promenade_to_open open_to_side_by_side side_by_side_to_open open_to_shadow shadow_to_open
"$BLENDER" --background --threads 4 animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/validate_boogie_woogie.py -- --reuse-reviewed
```

Review complete results, including all 14 canonical transition joins and loop angular continuity. Resolve the three current overlap findings through future authoring, then regenerate only affected sources and repeat saved-file verification. Review all 48 in playback, body support, palms/fingers, and musical phrasing; verify combined-library selection. Use the existing **Bake & Export Active Animation** workflow only when runtime delivery is resumed/requested. Preserve authored/baked/exported distinctions. Reinspect byte sizes, exact-file attributes, and staged raw blob hashes before committing any regenerated sources. Ordinary Git covers assets through 104,857,600 bytes; larger assets require LFS and completed uploads.

## Integration verification

The preservation commit was rebased onto fetched `origin/main` at `e12670ea9`. The resulting task commit is `bb259d0bb`. Append conflicts in the source README and `.gitattributes` were combined to preserve each chat’s additions. The current shared-scene and both anatomical-source hashes still match the recorded review dependencies. All 50 task binary hashes and exact-file storage attributes match the inventory after rebase.

Post-rebase verification passed: fast 10/10 (6.08 s), focused animation-tooling suite 14/14 (11.50 s), and `python scripts/lfs_policy.py check` for all 23,999 staged files. Logs are `boogie_woogie_evidence/integrated_fast.log` and `integrated_related.log`. The source-copy implementation and reopening regression test retain the concurrent main changes. These checks performed verification only; production authoring/rendering stayed paused.

The `# Animation` section of `AGENTS.md` now links this status and documents dependency-aware report reuse, canonical transition joins, and explicit Asset Browser metadata preservation. The 48 source studies and two GIFs total 9,837,048 bytes; all are ordinary Git blobs, so their publication uses the ordinary Git push and requires zero new LFS uploads. Final merge/push identities are reported in the delivery response and Git history.
