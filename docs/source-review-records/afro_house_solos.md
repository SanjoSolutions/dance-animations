# Afro house animation work status

- Date: October 2, 2026 (Europe/Berlin); preservation verification completed around 17:00 CEST.
- Chat title: **Create Afro house animations**.
- Chat ID: `01a0fd04-a121-7139-8b8b-deacfea31044`.
- Workspace: `/workspace/sanjo-solutions/apps/a-game`, sanjo-solutions cloud environment.
- Task branch: `codex/afro-house-solos`.
- Current commit at the stop instruction: `fe09ef7b6a54f03909f7335d9673a27c15007d69` (task changes were still in the working tree).
- Author of this record and task commits: Codex.
- State: **Stopped at the user's instruction. Partial procedural choreography studies preserved for future review.**

## Original scope and stopping point

The original request covered a broad, organized Afro house repertoire and positions for both characters in `man_and_woman3.blend`, separate solo playback, natural IK motion, planted contacts, clearance, smooth transitions and loop checks, reusable existing motion, per-animation Blender files, Blender 5.2 for every Blender operation, Git storage through 100 MiB, commits/rebase/documentation, and main publication.

The working catalog grew to 28 families per character (56 intended clips). The woman's 28-file author/bake/export batch finished at 16:55:25 CEST before the stop was processed. The man's batch had yet to start. After the stop, work consisted of inventory, read-only motion verification, Godot import checks, records, storage attributes, and delivery. Every owned authoring/rendering process had exited; the post-stop verification processes also completed. There is no paused authoring process to resume.

These files are **procedural blocking studies**, with useful numerical checks and a preliminary rendered pose. Full visual choreography, evaluated surface collision/sole review, all-position transition coverage, and cultural/style review remain open. The catalog is a practical set of movement families, rather than an exhaustive Afro house syllabus.

## Saved asset state

- **Authored:** 28 woman actions on `Woman.rigify`, each with one participant slot, `PARTNER` metadata, asset tags, descriptive categories, and phrase markers. Moving control keys are every three frames; constant channels receive one initial key. Existing `DiscoCharacter`, `DiscoWristPoser`, and yoga posing helpers supply proportion calibration, native IK, and wrist alignment.
- **Baked:** each source also contains its matching `.baked` action on `Woman.rigify_deform`. Blender-native scripting writes rigid joint frames and carries segment stretch through child translations to avoid inherited-scale shear. This is a procedural fallback, rather than a Game Rig Tools bake; Game Rig Tools was absent in this cloud checkout.
- **Exported:** 28 compact individual GLBs through the existing `AnimationClipScene`, Blender glTF exporter, and `AnimationUpdates.publish`. Every GLB has one woman-only clip, 630 channels, an adjacent `.glb.import`, and an entry in `models/player/animation_updates.tres`. Original update references were preserved.
- **Timing:** every action spans frames **0–96 inclusive**, **24 fps**, **120 BPM**, eight beats / four seconds. Frame 96 closes each loop. `enter_groove` and `exit_groove` use non-looping imports; the other 26 clips loop. Participant role is the woman/partner only. Man authored/baked/exported count is **zero**.
- **Shared files:** `man_and_woman3.blend`, `shared_scene_data.blend`, and the anatomical source files retain their existing contents. The combined library discovers the new per-animation files on reopening with the export add-on enabled.

Each linked GLB below also has an adjacent file with `.import` appended. The linked JSON contains that clip's authoring validation. [asset_inventory.json](afro_house_evidence/asset_inventory.json) lists every preserved binary's exact app-relative path, byte size, SHA-256, and storage selection.

| Movement family | Authored + baked source | GLB export | Validation |
| --- | --- | --- | --- |
| `alternating_arm_pump` | [afro_house_woman_alternating_arm_pump.blend](../../animations/man_and_woman/afro_house_woman_alternating_arm_pump.blend) (1578930 bytes) | [afro_house_woman_alternating_arm_pump_baked_9240e47b8729.glb](../../models/player/animation_updates/afro_house_woman_alternating_arm_pump_baked_9240e47b8729.glb) (345928 bytes) | [Report](../../scripts/afro_house/afro_house_woman_alternating_arm_pump.json) |
| `back_flick` | [afro_house_woman_back_flick.blend](../../animations/man_and_woman/afro_house_woman_back_flick.blend) (1643966 bytes) | [afro_house_woman_back_flick_baked_716c81d7879c.glb](../../models/player/animation_updates/afro_house_woman_back_flick_baked_716c81d7879c.glb) (351264 bytes) | [Report](../../scripts/afro_house/afro_house_woman_back_flick.json) |
| `chest_wave` | [afro_house_woman_chest_wave.blend](../../animations/man_and_woman/afro_house_woman_chest_wave.blend) (1622472 bytes) | [afro_house_woman_chest_wave_baked_a1a845189bf4.glb](../../models/player/animation_updates/afro_house_woman_chest_wave_baked_a1a845189bf4.glb) (350496 bytes) | [Report](../../scripts/afro_house/afro_house_woman_chest_wave.json) |
| `diagonal_step` | [afro_house_woman_diagonal_step.blend](../../animations/man_and_woman/afro_house_woman_diagonal_step.blend) (1644821 bytes) | [afro_house_woman_diagonal_step_baked_4ed9abb60e82.glb](../../models/player/animation_updates/afro_house_woman_diagonal_step_baked_4ed9abb60e82.glb) (348972 bytes) | [Report](../../scripts/afro_house/afro_house_woman_diagonal_step.json) |
| `enter_groove` | [afro_house_woman_enter_groove.blend](../../animations/man_and_woman/afro_house_woman_enter_groove.blend) (1359128 bytes) | [afro_house_woman_enter_groove_baked_b9f38d5dff43.glb](../../models/player/animation_updates/afro_house_woman_enter_groove_baked_b9f38d5dff43.glb) (348564 bytes) | [Report](../../scripts/afro_house/afro_house_woman_enter_groove.json) |
| `exit_groove` | [afro_house_woman_exit_groove.blend](../../animations/man_and_woman/afro_house_woman_exit_groove.blend) (1350453 bytes) | [afro_house_woman_exit_groove_baked_59b6cc907b14.glb](../../models/player/animation_updates/afro_house_woman_exit_groove_baked_59b6cc907b14.glb) (348292 bytes) | [Report](../../scripts/afro_house/afro_house_woman_exit_groove.json) |
| `forward_back` | [afro_house_woman_forward_back.blend](../../animations/man_and_woman/afro_house_woman_forward_back.blend) (1691299 bytes) | [afro_house_woman_forward_back_baked_2419b316730e.glb](../../models/player/animation_updates/afro_house_woman_forward_back_baked_2419b316730e.glb) (354364 bytes) | [Report](../../scripts/afro_house/afro_house_woman_forward_back.json) |
| `grounded_pulse` | [afro_house_woman_grounded_pulse.blend](../../animations/man_and_woman/afro_house_woman_grounded_pulse.blend) (1577110 bytes) | [afro_house_woman_grounded_pulse_baked_b837f393326c.glb](../../models/player/animation_updates/afro_house_woman_grounded_pulse_baked_b837f393326c.glb) (345920 bytes) | [Report](../../scripts/afro_house/afro_house_woman_grounded_pulse.json) |
| `heel_dig` | [afro_house_woman_heel_dig.blend](../../animations/man_and_woman/afro_house_woman_heel_dig.blend) (1664588 bytes) | [afro_house_woman_heel_dig_baked_ee20f60aafc2.glb](../../models/player/animation_updates/afro_house_woman_heel_dig_baked_ee20f60aafc2.glb) (348968 bytes) | [Report](../../scripts/afro_house/afro_house_woman_heel_dig.json) |
| `high_low_reach` | [afro_house_woman_high_low_reach.blend](../../animations/man_and_woman/afro_house_woman_high_low_reach.blend) (1587143 bytes) | [afro_house_woman_high_low_reach_baked_653c7f2d6ef4.glb](../../models/player/animation_updates/afro_house_woman_high_low_reach_baked_653c7f2d6ef4.glb) (348212 bytes) | [Report](../../scripts/afro_house/afro_house_woman_high_low_reach.json) |
| `hip_circle` | [afro_house_woman_hip_circle.blend](../../animations/man_and_woman/afro_house_woman_hip_circle.blend) (1581235 bytes) | [afro_house_woman_hip_circle_baked_5f53ce8e8032.glb](../../models/player/animation_updates/afro_house_woman_hip_circle_baked_5f53ce8e8032.glb) (344392 bytes) | [Report](../../scripts/afro_house/afro_house_woman_hip_circle.json) |
| `knee_lift` | [afro_house_woman_knee_lift.blend](../../animations/man_and_woman/afro_house_woman_knee_lift.blend) (1647601 bytes) | [afro_house_woman_knee_lift_baked_196ffdc4fdec.glb](../../models/player/animation_updates/afro_house_woman_knee_lift_baked_196ffdc4fdec.glb) (351260 bytes) | [Report](../../scripts/afro_house/afro_house_woman_knee_lift.json) |
| `lateral_rock` | [afro_house_woman_lateral_rock.blend](../../animations/man_and_woman/afro_house_woman_lateral_rock.blend) (1582881 bytes) | [afro_house_woman_lateral_rock_baked_1aa1d5815da9.glb](../../models/player/animation_updates/afro_house_woman_lateral_rock_baked_1aa1d5815da9.glb) (347448 bytes) | [Report](../../scripts/afro_house/afro_house_woman_lateral_rock.json) |
| `low_bounce` | [afro_house_woman_low_bounce.blend](../../animations/man_and_woman/afro_house_woman_low_bounce.blend) (1577191 bytes) | [afro_house_woman_low_bounce_baked_565e3b9a073f.glb](../../models/player/animation_updates/afro_house_woman_low_bounce_baked_565e3b9a073f.glb) (345916 bytes) | [Report](../../scripts/afro_house/afro_house_woman_low_bounce.json) |
| `open_arm_sweep` | [afro_house_woman_open_arm_sweep.blend](../../animations/man_and_woman/afro_house_woman_open_arm_sweep.blend) (1601799 bytes) | [afro_house_woman_open_arm_sweep_baked_ecfa22d22613.glb](../../models/player/animation_updates/afro_house_woman_open_arm_sweep_baked_ecfa22d22613.glb) (348212 bytes) | [Report](../../scripts/afro_house/afro_house_woman_open_arm_sweep.json) |
| `out_in` | [afro_house_woman_out_in.blend](../../animations/man_and_woman/afro_house_woman_out_in.blend) (1635324 bytes) | [afro_house_woman_out_in_baked_42dfa9ea63f3.glb](../../models/player/animation_updates/afro_house_woman_out_in_baked_42dfa9ea63f3.glb) (348968 bytes) | [Report](../../scripts/afro_house/afro_house_woman_out_in.json) |
| `quarter_turn_left` | [afro_house_woman_quarter_turn_left.blend](../../animations/man_and_woman/afro_house_woman_quarter_turn_left.blend) (1884919 bytes) | [afro_house_woman_quarter_turn_left_baked_b0dc5e7297b5.glb](../../models/player/animation_updates/afro_house_woman_quarter_turn_left_baked_b0dc5e7297b5.glb) (366956 bytes) | [Report](../../scripts/afro_house/afro_house_woman_quarter_turn_left.json) |
| `quarter_turn_right` | [afro_house_woman_quarter_turn_right.blend](../../animations/man_and_woman/afro_house_woman_quarter_turn_right.blend) (1884613 bytes) | [afro_house_woman_quarter_turn_right_baked_6701bec6d4fd.glb](../../models/player/animation_updates/afro_house_woman_quarter_turn_right_baked_6701bec6d4fd.glb) (368524 bytes) | [Report](../../scripts/afro_house/afro_house_woman_quarter_turn_right.json) |
| `ready_position` | [afro_house_woman_ready_position.blend](../../animations/man_and_woman/afro_house_woman_ready_position.blend) (1301319 bytes) | [afro_house_woman_ready_position_baked_d8d7dbec0129.glb](../../models/player/animation_updates/afro_house_woman_ready_position_baked_d8d7dbec0129.glb) (336752 bytes) | [Report](../../scripts/afro_house/afro_house_woman_ready_position.json) |
| `shoulder_roll` | [afro_house_woman_shoulder_roll.blend](../../animations/man_and_woman/afro_house_woman_shoulder_roll.blend) (1581803 bytes) | [afro_house_woman_shoulder_roll_baked_c3e835f0b620.glb](../../models/player/animation_updates/afro_house_woman_shoulder_roll_baked_c3e835f0b620.glb) (348972 bytes) | [Report](../../scripts/afro_house/afro_house_woman_shoulder_roll.json) |
| `side_step_touch` | [afro_house_woman_side_step_touch.blend](../../animations/man_and_woman/afro_house_woman_side_step_touch.blend) (1731220 bytes) | [afro_house_woman_side_step_touch_baked_bb1ba30352df.glb](../../models/player/animation_updates/afro_house_woman_side_step_touch_baked_bb1ba30352df.glb) (350504 bytes) | [Report](../../scripts/afro_house/afro_house_woman_side_step_touch.json) |
| `skate_step` | [afro_house_woman_skate_step.blend](../../animations/man_and_woman/afro_house_woman_skate_step.blend) (1637925 bytes) | [afro_house_woman_skate_step_baked_241d272deffc.glb](../../models/player/animation_updates/afro_house_woman_skate_step_baked_241d272deffc.glb) (348972 bytes) | [Report](../../scripts/afro_house/afro_house_woman_skate_step.json) |
| `staggered_position` | [afro_house_woman_staggered_position.blend](../../animations/man_and_woman/afro_house_woman_staggered_position.blend) (1300192 bytes) | [afro_house_woman_staggered_position_baked_4eaf41bf678f.glb](../../models/player/animation_updates/afro_house_woman_staggered_position_baked_4eaf41bf678f.glb) (337300 bytes) | [Report](../../scripts/afro_house/afro_house_woman_staggered_position.json) |
| `stomp_rebound` | [afro_house_woman_stomp_rebound.blend](../../animations/man_and_woman/afro_house_woman_stomp_rebound.blend) (1629243 bytes) | [afro_house_woman_stomp_rebound_baked_b9a4eec92be0.glb](../../models/player/animation_updates/afro_house_woman_stomp_rebound_baked_b9a4eec92be0.glb) (351264 bytes) | [Report](../../scripts/afro_house/afro_house_woman_stomp_rebound.json) |
| `syncopated_shuffle` | [afro_house_woman_syncopated_shuffle.blend](../../animations/man_and_woman/afro_house_woman_syncopated_shuffle.blend) (1688006 bytes) | [afro_house_woman_syncopated_shuffle_baked_f7afe8d62c69.glb](../../models/player/animation_updates/afro_house_woman_syncopated_shuffle_baked_f7afe8d62c69.glb) (354372 bytes) | [Report](../../scripts/afro_house/afro_house_woman_syncopated_shuffle.json) |
| `toe_tap` | [afro_house_woman_toe_tap.blend](../../animations/man_and_woman/afro_house_woman_toe_tap.blend) (1660102 bytes) | [afro_house_woman_toe_tap_baked_21009dd470d5.glb](../../models/player/animation_updates/afro_house_woman_toe_tap_baked_21009dd470d5.glb) (348968 bytes) | [Report](../../scripts/afro_house/afro_house_woman_toe_tap.json) |
| `v_step` | [afro_house_woman_v_step.blend](../../animations/man_and_woman/afro_house_woman_v_step.blend) (1668171 bytes) | [afro_house_woman_v_step_baked_127cc2c9db2f.glb](../../models/player/animation_updates/afro_house_woman_v_step_baked_127cc2c9db2f.glb) (354312 bytes) | [Report](../../scripts/afro_house/afro_house_woman_v_step.json) |
| `wide_position` | [afro_house_woman_wide_position.blend](../../animations/man_and_woman/afro_house_woman_wide_position.blend) (1310927 bytes) | [afro_house_woman_wide_position_baked_db8f5cb178cd.glb](../../models/player/animation_updates/afro_house_woman_wide_position_baked_db8f5cb178cd.glb) (337432 bytes) | [Report](../../scripts/afro_house/afro_house_woman_wide_position.json) |

## Scripts, reports, and supporting files

All paths in this section are relative to `apps/a-game`.

- `scripts/create_afro_house.py`: 28-family procedural authoring, native bake, per-animation saving, and GLB publishing; supports both roles, with only Woman run so far.
- `scripts/review_afro_house.py`: evaluated IK targets, planted intervals, wrist bend, chest/hand and knee proxies, loop pose and seam velocity diagnostics.
- `scripts/verify_afro_house_files.py`: fresh action loading, repeated control checks, and every-frame authored-to-baked joint position/orientation checks.
- `scripts/render_afro_house.py`: staged batch surface/contact-sheet renderer; **authored but never run**. Its planned `.cache/afro_house/review/` images and `scripts/afro_house/surface_review.json` were never generated.
- `scripts/test_afro_house_exports.py`: planned **full 56-clip completion test**. It currently fails on the 28/56 count before its full-catalog Godot branch runs. Preserve that failure as unfinished-scope evidence.
- `scripts/afro_house/afro_house_woman_*.json`: 28 per-clip authoring checks.
- `scripts/afro_house/saved_file_verification.json`: post-stop reopened verification for all 28 saved sources.
- `models/player/animation_updates.tres`: active-library references for the exports.
- `animations/man_and_woman/.gitattributes`, `models/player/animation_updates/.gitattributes`, and `docs/animation_work_status/afro_house_evidence/.gitattributes`: exact-filename Git storage overrides for these assets.
- `docs/animation_work_status/afro_house_evidence/`: final woman build log, fast/selected test logs, reopened verification log, Godot import and verification logs, preserved fixture verifier, asset inventory, and one preliminary render. `.gdignore` isolates the evidence scripts from normal Godot imports.
- `afro_house_evidence/preliminary_grounded_pulse.png`: existing Blender Workbench render at frame 15, generated before the final rotation-mode and bake corrections. It is **preliminary evidence**, not a render of every final saved clip. Its log records EGL warnings despite successful image output.

## Verification at preservation

Run commands from `apps/a-game`.

1. `python tests/run_tests.py --suite fast` — **9/9 passed**. The initial run had 8/9 because three hair `.res` files were LFS pointers. Hydrating those existing assets resolved the failure. Preserved output: [fast_tests.txt](afro_house_evidence/fast_tests.txt).
2. `python tests/run_tests.py --changed scripts/test_afro_house_exports.py` — **9/10 passed**. The intended complete-catalog check fails with `28 != 56`; the stop left every man clip pending. [selected_tests.txt](afro_house_evidence/selected_tests.txt).
3. `blender --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/verify_afro_house_files.py` — **28/28 saved sources passed** under Blender **5.2.2 LTS** (`d13f752e3b9c`). Each clip receives 193 half-frame samples plus near-seam samples at 0.01 and 95.99, then baked joints are checked at all 97 integer frames. Maximum bake joint-position error: **0.0000053594 m**; reported rotation error: **0 radians**. [saved_file_verification.txt](afro_house_evidence/saved_file_verification.txt).
4. Preserved GLBs were copied into `/tmp/afro-godot/clips`, alongside their import settings and the existing import hook. `godot --headless --editor --path /tmp/afro-godot --import`, followed by `godot --headless --path /tmp/afro-godot --script res://verify.gd` — **passed for all 28** with Godot **4.6.3**. Verified one AnimationLibrary clip per file, four-second duration, more than 500 tracks, and correct loop modes. [godot_verification.txt](afro_house_evidence/godot_verification.txt). The preserved fixture script is `afro_house_evidence/verify_preserved_exports.gd`.

Across the authoring reports: maximum planted-foot sample drift **0.000082213 m**; maximum wrist bend **13.5844 degrees**; maximum planned-foot-path error **0.003556645 m** (moving toe accent); loop endpoint position and angle errors **zero**; maximum near-seam velocity difference **0.0040518 m/s**. Limits are recorded per clip. Foot-path tolerance is 8 mm; planted-interval drift tolerance is 2 mm. Clearance checks are local spherical proxies. These measurements establish sampled joint/contact behavior, not whole-body surface clearance or final aesthetic approval.

## Remaining work and concrete blockers

- The user stopped animation authoring. Resume generation, refinement, or rendering only after a new instruction authorizes it.
- All 28 man clips remain pending.
- `ready_position` has a precise source/binary mismatch: the saved woman's action was generated by the already-running batch with pelvis height 0.943 m and groove-style hands. The current generator was edited before the stop to use height 0.975 m and relaxed hands, matching `enter_groove`'s opening pose. That edit was **never regenerated for Woman**. All other preserved outputs correspond to the final batch's script state. Review this discrepancy before any future regeneration.
- The preserved authorer and saved-action verifier call `animation_data_clear()` when isolating a rig. This also clears that rig's animation-data drivers in the temporary process. The passing reports therefore establish isolated action/bake parity. Validate the composed chooser with the shared Rigify drivers retained before treating these studies as production-ready; current main guidance explicitly calls for preserving those drivers.
- Full saved-bake surface renders, sole-height checks, mesh intersections, fingers, support balance, and review of every phrase remain pending. The staged renderer's three sample frames are a starting point; complete review should include contact boundaries and in-between motion.
- Position clips (`ready_position`, `wide_position`, `staggered_position`) have separate stance boundaries. A full transition network across those stances is still pending. Entry and exit clips only connect standing rest with the common groove boundary.
- The 56-clip completion test remains red until the missing role is authored and reviewed. The original scope therefore remains partial.
- Game Rig Tools was unavailable when work began. The project add-on may become available through concurrent work; inspect the latest checkout before choosing a future bake path. The preserved native rigid-joint bake is verified for joint positions and orientations; surface fidelity under segment scaling still warrants review.
- Repository documentation may evolve concurrently. Re-read root and app `AGENTS.md` and current authoring docs before resuming.

## Exact resume commands

The current checkout already contains hydrated shared scene/anatomical libraries and Blender 5.2.2. On another checkout, hydrate `shared_scene_data.blend`, `man_anatomical_study.blend`, `woman_anatomical_study_speculum.blend`, and the linked `dildo.blend` through the configured Git LFS credentials. The preservation commit keeps new task binaries directly in Git.

Read-only verification, valid while generation stays stopped:

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender --version
python tests/run_tests.py --suite fast
blender --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/verify_afro_house_files.py
python tests/run_tests.py --changed scripts/test_afro_house_exports.py
```

After an explicit future instruction to resume animation work, inspect the ready-position discrepancy and the current repository workflow, then use:

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/create_afro_house.py -- --character Woman --moves ready_position
blender --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/create_afro_house.py -- --character Man
blender --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/verify_afro_house_files.py
blender --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/render_afro_house.py
python tests/run_tests.py --changed scripts/test_afro_house_exports.py
```

The first two commands overwrite/publish animation assets; they are future work, not part of this stop-and-preserve delivery. Measure new binary sizes and set exact-file Git/LFS attributes before staging. Current overrides cover the preserved woman assets only; future man files need their own size-based decisions.

## Storage and delivery

All **57** preserved binaries (28 `.blend`, 28 `.glb`, one preliminary PNG) were inspected as actual binary bytes before staging. Total: **54,714,692 bytes**; largest: **1,884,919 bytes**. Every file is below 104,857,600 bytes and uses ordinary Git through exact-filename overrides. Existing LFS assets retain their original policy. Task publication needs ordinary Git binary uploads; this task adds zero new LFS pointers.

This record is committed with the durable assets. The delivery sequence then fetches/rebases against concurrent `origin/main`, records concise lessons under the app's `# Animation` guidance in a separate commit, and merges through an ordinary history-preserving main push. Final task and integration hashes are reported in the chat and discoverable with `git log --all -- docs/animation_work_status/afro_house_solos.md`.

### Integration checkpoint

The preservation commit rebased to `1f438c656ef96a7e91cc035d9adf4c683ef981c2` on fetched `origin/main` commit `18e528c73`. An add/add conflict in the per-animation `.gitattributes` was resolved by retaining both complete exact-file rule sets. The repository's new `python scripts/lfs_policy.py check` passed for 23,488 staged files. The updated fast suite passed **10/10** in 6.52 seconds; see [after_rebase_fast_tests.txt](afro_house_evidence/after_rebase_fast_tests.txt).

Shared-scene and linked-geometry SHA-256 values match the dependencies used for the preserved verification:

| Dependency | SHA-256 |
| --- | --- |
| `animations/man_and_woman/shared_scene_data.blend` | `18a0f6bb84cc90426444e4bf4c81d78e3b81ebd84097a7c16afc098cd9948130` |
| `man_anatomical_study.blend` | `6144ac70e971bff82f432f0930eb0fe8e5c18e16ba99f8193aa8738af6b67c55` |
| `woman_anatomical_study_speculum.blend` | `d9b123f681bd8c343ed861ec8d9c8b512bede54ae0b93c8cefb33acfafda96e9` |
| `dildo.blend` | `3ac962bf36627fd886d0661036412d4efb37d388dcf5e4aa5650b3f3dab10ce8` |

The reused disco/yoga posing helpers and animation-evaluation helper also match their validation versions. Concurrent main now includes `scripts/blender/install_animation_tools.py` and bundled Game Rig Tools setup guidance; follow that workflow upon a future authorized resumption. The updated testing guidance requires the suite runner and timed temporary Godot diagnostics. The preserved isolated Godot verification predates this rebase; adapt its temporary fixture to the current runner before future execution.

### Published preservation checkpoint

The first successful ordinary push published merge `1e89ec851ca861c22e30d7425177db24e4251054`; `git ls-remote origin refs/heads/main` returned that exact commit immediately afterward. Both task commits (`1f438c656ef96a7e91cc035d9adf4c683ef981c2`, `1532d073eb6addd406990565f2840d6047f45d1c`) were verified as ancestors of remote main. Every one of the 57 binary SHA-256 values still matched the inventory after integration. The final integrated fast suite passed **10/10**; its output is in [integrated_fast_tests.txt](afro_house_evidence/integrated_fast_tests.txt). A documentation follow-up records the rig-driver isolation limit of the preserved verifier. All asset uploads used ordinary Git; this task introduced zero LFS uploads. Additional concurrent merge commits may advance main while preserving these task commits.
