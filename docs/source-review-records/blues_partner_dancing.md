# Blues partner dancing: stopped-work record

- Date: 2026-10-02 (Europe/Berlin).
- Chat/task title: Blues partner dancing for `man_and_woman3.blend` (descriptive task title; the UI title was not supplied).
- Branch: `codex/blues-partner-repertoire`.
- Current commit at the preservation snapshot: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- State: animation work stopped at the user’s explicit request; recording, verification, and Git delivery only.
- Author of this status and GitHub-delivered work: Codex.

## Original scope

Build a broad coordinated Blues partner-dance repertoire for both characters in A-Game, using Blender 5.2, the paired IK API, and individual animation files linked by `man_and_woman3.blend`. Reuse suitable motion, validate interpolation, contacts, clearance, transitions and loops, export clips, follow the 100 MiB Git/LFS threshold, commit/rebase, add Animation guidance, and merge/push main. The stop instruction supersedes further authoring and repertoire completion.

## Saved state

34 readable per-animation `.blend` sources are preserved: 24 movement/position loops and 10 hold transitions. All have two actor slots (`BOTH`: player = `Man.rigify`, partner = `Woman.rigify`), authored frames 0–128 inclusive at 24 fps. Movement loops use an eight-beat, 90 BPM phrase. Transitions are one-shot clips. Sixteen sources also contain matching paired `.baked` actions and have individual GLB exports. Eighteen sources remain authored-only. These are procedural choreography studies with numerical validation, pending complete visual and game playback review; they are a partial repertoire, not a claim to every Blues variation.

The initial posture, grounded ankles, finger settings, and wrist calibration were reused from `cuddle_standing_sway.blend`. Holds cover close, closed, open two-hand, open one-hand, promenade, side-by-side, shadow, and breakaway. Authored movement includes pulse, slow walking/drag, lateral weight transfer, body rhythm, lowering/recovery, pause, side basics, lateral travel/return, forward/backward walking/return, rock steps, diagonal walking, and side-by-side/shadow walking.

`blues_partner_dancing_assets.json` is the authoritative saved-file audit: exact paths, byte sizes, SHA-256, authoring/baked actions, actor bindings, frame ranges, embedded validation, and every exported GLB. The earlier `blues_repertoire.json` contains only the final one-clip refinement run; `blues_transitions.json` contains the final six-transition batch. Preserve both as partial run manifests and consolidate them on resume.

### Per-animation inventory

All source paths below are relative to `apps/a-game/animations/man_and_woman/`. “Exported” means an on-disk GLB with valid container length, a named paired clip, and two skins; full Godot playback remains pending.

| Source | Bytes | Saved state |
| --- | ---: | --- |
| `blues_body_rhythm.blend` | 5033204 | Authored + baked + exported |
| `blues_breakaway_groove.blend` | 514122 | Authored only |
| `blues_breakaway_to_open_two.blend` | 526329 | Authored only |
| `blues_close_groove.blend` | 4990975 | Authored + baked + exported |
| `blues_close_to_closed.blend` | 4367706 | Authored + baked + exported |
| `blues_closed_groove.blend` | 4996791 | Authored + baked + exported |
| `blues_closed_to_close.blend` | 4378589 | Authored + baked + exported |
| `blues_closed_to_open_two.blend` | 4814292 | Authored + baked + exported |
| `blues_closed_to_promenade.blend` | 5473017 | Authored + baked + exported |
| `blues_diagonal_walk_return.blend` | 535720 | Authored only |
| `blues_down_and_recover.blend` | 5000841 | Authored + baked + exported |
| `blues_lateral_weight_shift.blend` | 5014368 | Authored + baked + exported |
| `blues_musical_pause.blend` | 4554138 | Authored + baked + exported |
| `blues_open_one_groove.blend` | 5002201 | Authored + baked + exported |
| `blues_open_one_to_open_two.blend` | 3880026 | Authored + baked + exported |
| `blues_open_two_groove.blend` | 4978839 | Authored + baked + exported |
| `blues_open_two_to_breakaway.blend` | 4113702 | Authored + baked + exported |
| `blues_open_two_to_closed.blend` | 4839331 | Authored + baked + exported |
| `blues_open_two_to_open_one.blend` | 3992742 | Authored + baked + exported |
| `blues_promenade_groove.blend` | 523667 | Authored only; saved NLA strips still end at frame 1 |
| `blues_promenade_to_closed.blend` | 557050 | Authored only |
| `blues_pulse.blend` | 519925 | Authored only |
| `blues_rock_step.blend` | 535997 | Authored only |
| `blues_shadow_groove.blend` | 514565 | Authored only |
| `blues_shadow_walk_return.blend` | 527790 | Authored only |
| `blues_side_basic.blend` | 532922 | Authored only |
| `blues_side_basic_open.blend` | 533244 | Authored only |
| `blues_side_by_side_groove.blend` | 515518 | Authored only |
| `blues_side_by_side_walk_return.blend` | 527359 | Authored only |
| `blues_slow_drag.blend` | 537812 | Authored only |
| `blues_travel_left_return.blend` | 534140 | Authored only |
| `blues_travel_right_return.blend` | 524112 | Authored only |
| `blues_walk_backward_return.blend` | 534811 | Authored only |
| `blues_walk_forward_return.blend` | 534346 | Authored only |

### Export inventory

| GLB in `models/player/animation_updates/` | Bytes |
| --- | ---: |
| `blues_body_rhythm_baked_87146161ab9a.glb` | 639228 |
| `blues_close_groove_baked_e5a205e5f0fd.glb` | 631076 |
| `blues_close_to_closed_baked_9da399bf0176.glb` | 661204 |
| `blues_closed_groove_baked_8cc358b0fad7.glb` | 633112 |
| `blues_closed_to_close_baked_931e8ec8b548.glb` | 661204 |
| `blues_closed_to_open_two_baked_cd1c25ab9405.glb` | 705692 |
| `blues_closed_to_promenade_baked_a5a4bcf14969.glb` | 815976 |
| `blues_down_and_recover_baked_fe0f365f9e5b.glb` | 631072 |
| `blues_lateral_weight_shift_baked_e3b48c5bb5e1.glb` | 639240 |
| `blues_musical_pause_baked_2b98517243d5.glb` | 624956 |
| `blues_open_one_groove_baked_4ba477024535.glb` | 633116 |
| `blues_open_one_to_open_two_baked_081c8b07ac1d.glb` | 650972 |
| `blues_open_two_groove_baked_273bf53a2abc.glb` | 631080 |
| `blues_open_two_to_breakaway_baked_862952def6cf.glb` | 695372 |
| `blues_open_two_to_closed_baked_8a75b96fff74.glb` | 707728 |
| `blues_open_two_to_open_one_baked_b2be142b37f0.glb` | 653020 |

Every listed GLB has its adjacent `.glb.import`. `models/player/animation_updates.tres` retains the existing clip references and adds the published Blues clips. The combined `man_and_woman3.blend` and shared rig/model files were read and retained unchanged. The combined library discovers new per-animation files on open.

### Scripts and review assets

- `scripts/player_assets/author_blues.py`: templates, a planned 29-clip movement catalog, IK authoring, 257-sample contact/plant/proxy/loop checks, quaternion normalization, and per-animation file writing. Current code is ahead of several saved studies: the fixed-control-root refinement was applied only to the latest `blues_travel_right_return` save.
- `scripts/player_assets/author_blues_transitions.py`: ten transitions exist on disk; the current script’s pair list covers the last six and includes a wrist-orientation projection fallback. The first four earlier transitions are preserved in their source files and logs.
- `scripts/player_assets/export_blues.py`: evaluated Blender 5.2 sampling, paired action slots, pose-fidelity verification, `AnimationFileWriter`, compact `AnimationClipScene`, participant filtering, and `AnimationUpdates` publishing. It uses Blender evaluation directly because Game Rig Tools was unavailable in the original authoring setup. The subsequently integrated main includes `scripts/blender/install_animation_tools.py` for bundled Game Rig Tools and Player Asset Export; evaluate that setup on an authorized resume. Existing GUI baking integration remains to be checked on resume.
- `scripts/player_assets/render_blues_review.py`: Blender-only eight-hold clay-sheet renderer; no additional rendering occurred after the stop request.
- `animations/man_and_woman/blues_holds.png`: completed 1920×960 review sheet, still awaiting full visual sign-off. Top row: close, closed, open two-hand, open one-hand. Bottom row: promenade, side-by-side, shadow, breakaway.
- `docs/animation_work_status/blues_partner_dancing_studies/prototype.blend.gz`: 41,424,228-byte lossless archive of the 139,214,956-byte early open-hold blocking snapshot. Decompression SHA-256 is `4616890844b7b047e475a2baf38fd49f7404f514ed069da757fdf9f804982028`. The original LFS upload returned HTTP 501; the lossless archive fits regular Git and preserves the exact scene bytes. It contains a whole working scene and absolute library paths from this checkout. This is a superseded procedural study, not a production per-animation source; future checkouts may need library-path relinking.
- The adjacent `prototype.png`, `prototype.py`, `render.py`, `templates.py`, `bake_debug.py`, `side_debug.py`, `failure.json`, `export_batch.py`, and `audit_saved.py` preserve initial review, diagnostics, and the read-only saved-state audit. Temporary output paths inside those diagnostic scripts are historical.
- `docs/animation_work_status/blues_partner_dancing_logs/`: exact authoring, failed attempts, export, rendering, tests, and audit logs. `incidental_godot_import_changes.patch` records incidental test/editor rewrites that were restored before committing.

## Validation and limits

- Blender: `5.2.2 LTS`, build `d13f752e3b9c`. All Blender work used this binary.
- Every saved source has an embedded passing authoring report. Movement and transition sampling used 257 times, including half-frames. Checks measure named palm origins, planted ankle origins, torso sphere proxies, and endpoint continuity. Movement reports include loop orientation and linear-velocity differences. These checks are not complete mesh/finger collision proofs or visual motion sign-off.
- The final right-travel refinement reduced maximum measured planted-ankle error from approximately 5.35 mm to 0.397 mm by keeping the control root fixed. Earlier travel clips retain their earlier results, up to approximately 5.35 mm. This refinement was not propagated after the stop request.
- Successful export logs contain `BLUES_EXPORT` with the measured pose-bake error. Initial bake failures were investigated before publication; final exported clips were published only after the script’s 2 mm bake-fidelity gate passed. Published container/skin/action checks passed in the saved-state audit.
- `blender -t 2 --background --factory-startup --python-exit-code 1 --python docs/animation_work_status/blues_partner_dancing_studies/audit_saved.py`: PASS, 34 readable sources, 16 baked, 16 exported, all participants `BOTH`, maximum source size 5,473,017 bytes, maximum exported GLB 815,976 bytes.
- `python tests/run_tests.py --suite fast`: earlier run 9/9 passed after hydrating the three hair physics meshes. Final stop-state run: 8/9 passed; activity JSON emitted missing hair-model resource/Character compilation errors (`bob01`, `bob02`, `short01`–`short04`, `afro01`). Godot 4.6.3 is installed; repository documentation references 4.7.2. The apparent test PASS marker does not override these engine errors.
- `blender -t 2 --background --factory-startup --python-exit-code 1 --python scripts/player_assets/test_paired_animation_authoring.py`: PASS, 12 tests.
- `blender -t 2 --background --factory-startup --python-exit-code 1 --python scripts/player_assets/test_motion_review.py`: PASS, 10 tests.
- `blender -t 2 --background --factory-startup --python-exit-code 1 --python scripts/player_assets/test_animation_files.py`: PASS, 1 integration test.
- `python tests/run_tests.py` and then `python tests/run_tests.py --slow-timeout 60`: incomplete. Broad dependency checks encountered missing LFS assets, incompatible/imported resources, script errors, and timeouts. The bounded run reached `adult-ai-chat/test_activity_menu.gd` before termination for the stop request. Logs preserve the executed subset; no complete slow-suite pass is claimed.

## Processes and precise stopping point

All owned authoring, refinement, rendering, and export-queue processes were stopped or had already completed. The long movement process was stopped after saving `blues_diagonal_walk_return`; subsequent promenade walking and turn studies were not saved. The side/shadow batch and ten transitions completed. The fixed-root right-travel refinement and eight-hold sheet completed before the stop. The export queue published sixteen clips before termination. The read-only audit subsequently confirmed each saved binary is readable. No animation-generating process remains running. Verification-only fixtures completed after the stop request.

## Remaining work and concrete blockers

1. Obtain renewed user authorization before resuming animation authoring, refining, rendering, or export. The current instruction is preservation only.
2. Review the preserved studies visually for natural weight transfer, arm/finger/body clearance and contact surfaces; inspect motion between keys. Torso proxies and palm-origin checks cover a limited geometric model.
3. Correct the authored-only `blues_promenade_groove` saved NLA strip range (currently 0–1 against action 0–128). The exporter contains a range correction, but that source has not been exported.
4. Reconcile the partial JSON manifests, the current generator revisions, and the saved sources. Propagate quaternion normalization and any accepted foot-plant refinement only after reviewing its effect.
5. Complete/review the planned promenade walk, quarter-turn left/right returns, and partnered full-circle left/right clips. Their recipes exist in code; their final sources do not exist. Underarm turns, tuck/send-out variations, dips, and additional regional/social Blues vocabulary remain outside the preserved authored subset.
6. Bake/export the eighteen authored-only sources, then verify their imports and paired playback. Preserve the existing animation update catalog while adding their files.
7. Hydrate the specific missing LFS dependencies and use the project-compatible Godot version before re-running the broad suite. Game Rig Tools setup and cache prerequisites remain relevant for the GUI export route.
8. This snapshot uses regular Git for new files at or below 104,857,600 bytes. The historical prototype is preserved as a smaller lossless `.blend.gz` archive after its LFS upload returned HTTP 501. All outgoing task files fit regular Git. Integration preserves main’s generated `scripts/lfs_policy.py` attributes and introduces no outgoing LFS pointer.

## Resume commands

Run read-only verification now, or authoring/export commands only after renewed authorization. Start in `/workspace/sanjo-solutions/apps/a-game` with Blender 5.2 and the Player Asset Export add-on installed.

```bash
blender --version
python tests/run_tests.py --suite fast
blender -t 2 --background --factory-startup --python-exit-code 1 --python docs/animation_work_status/blues_partner_dancing_studies/audit_saved.py
# After authorization: author a selected missing recipe, review before running another.
blender -t 2 --background animations/man_and_woman/cuddle_standing_sway.blend --python-exit-code 1 --python scripts/player_assets/author_blues.py -- --only promenade_walk_return
# After authorization and source review: bake/export one authored-only source.
blender -t 2 --background animations/man_and_woman/blues_pulse.blend --python-exit-code 1 --python scripts/player_assets/export_blues.py
# After authorization: the current transition script covers only its last six entries.
blender -t 2 --background animations/man_and_woman/cuddle_standing_sway.blend --python-exit-code 1 --python scripts/player_assets/author_blues_transitions.py
```

To restore the historical snapshot for inspection, run `gzip -dc docs/animation_work_status/blues_partner_dancing_studies/prototype.blend.gz > /tmp/blues_prototype.blend` and verify its recorded decompressed SHA-256.

Each generator can overwrite its named source files, and run manifests represent the selected batch. Review Git status, check real binary sizes/attributes before staging, and retain the status audit as the frozen inventory of this stop point. Integration commits and the verified remote-main hash are reported in the chat delivery; the snapshot commit above identifies the original base.

## Preservation integration verification

- Preservation commit: `882f9622179bc44f3bad7f5be14e69e191a3b43d`, rebased onto fetched main `3b81a0665`. The catalog conflict retained main’s 55 current entries and added only the 16 Blues exports.
- Main’s repository-wide generated size policy was retained. `python scripts/lfs_policy.py check` passed for 24,373 staged files after rebase. All 53 task binary assets use regular Git. The prototype archive restores the exact original bytes and SHA-256 above; the unsuccessful historical LFS pointer is outside the outgoing task history.
- The documentation commit adds the paused Blues inventory and measured foot-support refinement guidance to `AGENTS.md` under Animation. Animation authoring and rendering remain stopped.
- Rebased integration fast suite: `python tests/run_tests.py --suite fast`, **9/10 passed**, exit 1. The newly integrated suite adds a passing export-receipt check; the activity JSON check still fails on hair-resource loading and dependent `Character` compilation. Exact output: `blues_partner_dancing_logs/integration_fast.log`.
- Read-only preservation verification: all 34 source hashes and 16 export hashes match the frozen audit; all 53 binary sizes, staged object sizes, and Git filter attributes match regular-Git storage. Lossless prototype decompression matches 139,214,956 bytes and the recorded SHA-256. Result: `blues_partner_dancing_logs/integration_preservation.log`.
- Final integration fetched `51c1b5ef6ada636e4c89036fece7d0f0d2209de6` immediately before merging. Conflict resolution preserved all 490 current-main catalog entries and added the 16 task exports, producing 506 entries; all concurrent Animation guidance was retained. `test_animation_updates.py`: 5 tests passed. Repository storage check passed for 28,337 staged files.
- Merged-tree fast suite: **9/10 passed**, with the same activity JSON resource/Character compilation blocker; see `blues_partner_dancing_logs/merged_fast.log`. Preservation commits are authored by Codex and carry the required single co-author trailer. All task assets travel in the ordinary Git push; additional LFS asset uploads are unnecessary for this outgoing snapshot.
