# Priority animation recovery

The local priority pass delivers **170 reviewed source/export pairs**: 76 Hip-hop, 40 New York Hustle, 35 Salsa, and 19 Popping. This follows the user's preference for Hip-hop, New York Hustle, and Salsa. The original interruption records remain in `docs/source-review-records/`.

All 170 clips are installed in the active catalog with fresh-source, native-bake, actual-model playback, and targeted motion checks. Seventeen Popping clips are additions; the other 153 clips refine existing studies. The library now contains 3,599 selectable variants from 3,517 source/export pairs across 92 styles. Publication follows local review under [AGENTS.md](../../AGENTS.md).

## Delivered changes

| Style | Changed clips | Result |
| --- | ---: | --- |
| Hip-hop | 76 | Held fingers use the shared quaternion control modes. Higher sampling resolves the recorded kick-step interpolation failure while preserving tempo. Four wide-stance transitions now meet the actual saved poses; all eight directed transitions pass endpoint checks. |
| New York Hustle | 40 | Loops meet their closing poses with eased boundaries and a 21 ms held endpoint. Man's soles align with the floor. Fast hand arcs retain their polished contacts. The inside-turn pass gains native foot pivots; the shadow transition gains a stable follower elbow arc. |
| Salsa | 35 | All authored clips have refreshed native bakes, held finger rotations, calibrated soles, and verified contacts. Turning feet follow body heading while retaining footfall positions and pitch. The leader left turn distributes continuous arm twist through native upper-arm controls. |
| Popping | 19 | Recover 17 Woman clips and rebuild the preserved `finger_tutting` and `tutting_box` drafts from the original a-game vocabulary. The complete saved repertoire now has 42 moves for each character, or 84 clips. The 65 retained clips keep their historical motion-review status. |

The 17 recovered Woman moves are `backslide`, `fresno`, `heel_toe`, `lean`, `pose_box`, `pose_low`, `pose_ready`, `pose_robot`, `pose_scarecrow`, `pose_staggered`, `pose_t_arm`, `pose_wide`, `puppet`, `scarecrow`, `side_glide`, `tutting_angles`, and `walkout`. [Popping coverage](priority_recovery/popping-coverage.json) reconciles the full finite recipe. Original Git blob provenance accompanies the adapted [Popping](../../scripts/popping/provenance.json) and [Salsa](../../scripts/salsa/provenance.json) recipes.

Shared skeletons, MPFB bodies, native wrist constraints, and deformation-rig definitions retain their existing revisions. Saved action clocks now survive source composition, normal saves, and chooser selection. Denser 48/96/192 FPS sources preserve the original durations by scaling key times with the frame rate. Recipe resume checks preserve already-corrected poses, key counts, and clocks.

## Local review

Playback previews use the project's MPFB models and wardrobe profiles. Each MP4 includes the closing pose as an extra display frame. [Preview revisions](priority_recovery/previews.json) record candidate, installed-source, installed-export, model, and video hashes.

| Preview | Pose sheet |
| --- | --- |
| [Hip-hop kick step](priority_recovery/hip_hop_man_kick_step.mp4) | [Front and side](priority_recovery/hip_hop_man_kick_step.png) |
| [Popping finger tutting](priority_recovery/popping_woman_finger_tutting.mp4) | [Front and side](priority_recovery/popping_woman_finger_tutting.png) |
| [Hustle closed basic](priority_recovery/new_york_hustle_basic_closed.mp4) | [Front and side](priority_recovery/new_york_hustle_basic_closed.png) |
| [Hustle alternating turns](priority_recovery/new_york_hustle_alternating_turns.mp4) | [Front and side](priority_recovery/new_york_hustle_alternating_turns.png) |
| [Hustle shadow entry/exit](priority_recovery/new_york_hustle_shadow_entry_exit.mp4) | [Front and side](priority_recovery/new_york_hustle_shadow_entry_exit.png) |
| [Salsa around the world](priority_recovery/salsa_around_the_world.mp4) | [Front and side](priority_recovery/salsa_around_the_world.png) |
| [Salsa leader left turn](priority_recovery/salsa_leader_left_turn.mp4) | [Front and side](priority_recovery/salsa_leader_left_turn.png) |

Visual review covers representative front/side phases, fast accents, hand configurations, turn silhouettes, and playback highlights. Additional sheets include the Hustle inside-turn pass, Salsa cross-body outside turn, leader right turn, and dile que no, plus Popping backslide and tutting angles. Full mesh collision, detailed balance, expert dance accuracy, and continuous visual review of every clip remain separate coverage. Every asset retains its procedural-study status.

## Verification

[Per-clip evidence](priority_recovery/evidence.json) records exact installed file paths, sizes, SHA-256 hashes, original revisions, participant roles, action slots, ranges, clocks, dependency hashes, generator hashes, sampling, tolerances, and measurements. The installation stage proves exact authored/baked curve parity while repacking portable descriptors. Installed sources resolve `../../shared_scene_data.blend` and the local character dependencies.

The numerical review samples **94,762 scene times**, every stored integer and half-frame, across all 209 deform bones for each participating actor. Saved-source playback runs in fresh Blender processes. Bake playback runs with live deformation follow constraints muted. Three.js playback binds the project's actual MPFB skeletons and compares positions, orientations, and durations against the native reference. Compression preserves numeric animation data and receives a separate installed-runtime check.

| Measurement | Worst measured result | Acceptance limit |
| --- | ---: | ---: |
| Reopened source matrix components | 0 | 0.0001 |
| Integer bake matrix components | 0.00001592 | 0.0001 |
| Fractional bake joint position | 1.939 mm | 2 mm |
| Installed runtime joint position | 1.938 mm | 2 mm |
| Installed runtime joint orientation | 0.950 degrees | 2.005 degrees |
| Lowest sampled base sole vertex | −0.914 mm | −2 mm |
| Loop endpoint joint position, 146 loops | 0.00133 mm | 1 mm |
| Loop seam velocity difference | 0.0991 m/s | 0.12 m/s |
| Hustle fully held palm gap | 10.14 mm | 25 mm |
| Salsa fully held palm gap | 21.79 mm | 35 mm |

Sole checks sample actual base-mesh foot/toe vertices in the lowest 18 mm rest band. Salsa additionally checks stationary footfall targets, body-center spacing, wrist bend, and wrist speed. Those targeted quantities establish their stated coverage; the visual-review coverage above describes broader physical assessment.

Project verification includes `npm run check`, the 40-test playback/application suite, and `npm run build`. Blender checks cover `dance_tools.test.py`, source composition/save/reopen, mixed-rate timing, and recipe resumption. [Integration results](priority_recovery/integration-checks.json) retain commands and results. The packaged runtime library occupies approximately 793.4 MiB. The recorded Slow dance source was hydrated from Git LFS to complete whole-library hash validation.

## Reproduce or resume

Use Blender 5.2.2 and the project Node dependencies from the repository root. Runtime-reference preparation uses the packages in `scripts/motion_recovery/requirements.txt`. Keep recipes stable for each generation batch. Complete each writer before evaluating its output and run catalog writers serially.

For a paired clip, the batch chooses its applicable refinement, checks the saved native source/bake, and checks contacts, soles, and loops. The three special turn/shadow corrections are selected automatically.

```bash
python scripts/motion_recovery/refine_batch.py CLIP_ID --workers 1
python scripts/motion_recovery/runtime_batch.py CLIP_ID
blender -b -t 1 --factory-startup --python-exit-code 1 --python scripts/motion_recovery/install.py -- CLIP_ID
node scripts/compress-clips.mjs CLIP_ID
blender -b -t 1 --factory-startup --python-exit-code 1 --python scripts/motion_recovery/audit_installed.py -- CLIP_ID
node scripts/motion_recovery/runtime.mjs --installed CLIP_ID
python scripts/motion_recovery/report.py --complete
```

Hip-hop candidates use `scripts/motion_recovery/repair.py`; its wide-stance transition corrections use `scripts/hip_hop/refine_transitions.py`. Popping candidates use `scripts/popping/complete.py`. Run those scripts through Blender with the clip identifier after `--`, followed by `validate.py`, runtime, sole, and applicable loop checks before installation. Fresh Popping generation reconstructs the original recipe; its current saved clips can also receive native rebakes through `repair.py`.

```bash
blender -b -t 1 --factory-startup --python-exit-code 1 --python scripts/popping/coverage.py
blender -b -t 1 --factory-startup --python-exit-code 1 --python scripts/motion_recovery/refinements.test.py
python scripts/motion_recovery/ready.py --runtime-pending
python scripts/motion_recovery/ready.py --runtime-checked
```

The two `ready.py` commands list paired candidates awaiting runtime review or installation. A candidate with a current failed check stays outside installation. Current source refinements retain their established correction metadata; resuming preserves their denser clocks.

Task-owned candidates, reference matrices, original-file backups, diagnostic trials, screenshots, and detailed logs remain under `.cache/motion-recovery/<clip-id>/`. Durable final reports and previews live alongside this document. Historical failed trials include dense bakes through native leg/arm twist branches and the superseded shadow elbow fit. Their diagnostics informed the installed control corrections; final per-clip hashes identify the delivered revision. The priority generation queue is complete, with each targeted source and export installed.

## Broader library

The lower-priority interruption records continue to describe additional source gaps and individual motion-review issues. This pass changes the four styles listed above.

| Style | Planned | Saved | Source gaps | Original checkpoint |
| --- | ---: | ---: | ---: | --- |
| House | 90 | 49 | 41 | [House repertoire](../source-review-records/house_dance.md) |
| Waacking | 62 | 16 | 46 | [Waacking repertoire](../source-review-records/waacking_repertoire.md) |
| Fusion | 45 | 20 | 25 | [Fusion partner dance](../source-review-records/fusion_partner_dance.md) |

These counts reconcile the finite plans with current saved sources. Saved studies across the broader library retain their recorded review status and remain candidates for subsequent style-specific work.
