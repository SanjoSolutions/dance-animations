# Solo Charleston work status — preserved partial studies

- Date: October 2, 2026 (Europe/Berlin).
- Chat title: Create Solo Charleston animations.
- Chat ID: `01a0fd05-38d5-705c-93a0-3aa1d6bd6053`.
- Environment: sanjo-solutions cloud; checkout `/workspace/sanjo-solutions`; app `apps/a-game`.
- Task branch at stop: `codex/solo-charleston`.
- Current/base commit at stop: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Delivery state: preservation checkpoint, with authoring stopped by the user's coordination instruction. The complete requested repertoire remains unfinished. Task and integration commit IDs appear in the Git history containing this record and the chat's delivery response.

## Original scope and stopping point

Create a broad Solo Charleston repertoire for both characters from `man_and_woman3.blend`, using Blender 5.2 and the repository's individual-animation workflow; reuse appropriate motion helpers, validate contacts, clearance and loops, export, commit, rebase, update `AGENTS.md`, merge and push. The stop instruction takes priority over further animation work.

All Blender authoring, baking, inspection, export and rendering used **Blender 5.2.2 LTS**, build `d13f752e3b9c`. The Player Asset Export add-on was installed from this checkout. Game Rig Tools was absent in this environment at the stopping point. A native Blender visual-bake study was developed using the existing per-animation writer, compact clip scene and update publisher. This remains a procedural blocking study, especially its temporary rigid-joint bake adaptation; it needs comparison with the standard Game Rig Tools workflow before production approval.

**62 `.blend` source studies are saved (58 Woman, 4 Man), each containing one editable authoring action and one `.baked` action: 124 actions total. Two GLBs are saved and referenced by `models/player/animation_updates.tres`.** Their existence establishes authored/baked/exported state, rather than final dance-quality approval. Existing combined/shared/model sources were read and retained unchanged by this task.

The latest `repertoire.py` describes 61 phrases per character (37 movement variations and 24 position hold/entry/exit clips), hence 122 intended solo clips. The saved 58 Woman files precede the three right-lead additions and the latest transition and turn refinements. The four Man files cover only the basic, heel-dig and turn probes. The current scripts are newer than most assets.

## Durable implementation and evidence

Paths in this record are relative to `apps/a-game`.

| Path | Preserved state |
| --- | --- |
| `scripts/solo_charleston/repertoire.py` | Counted choreography and pose targets: basics, kicks, swivels, travel, jazz variations, styling, breaks, turns, and eight positions with hold/entry/exit. Latest three right-lead definitions remain ungenerated. |
| `scripts/solo_charleston/author.py` | IK authoring with reused `RigYogaPoser` and `DiscoWristPoser`, sparse half-beat keys, one initial key for constant channels, participant metadata, per-file persistence, native visual bake and individual GLB publication. Latest half-frame bake/export path was exercised only for Man basic 1930s. |
| `scripts/solo_charleston/review.py` | Half-frame IK/contact/clearance/loop checks, quarter-frame baked comparisons and evaluated skin-floor checks. Final turn/ball-pivot contact-check edit was syntax-checked only after the stop; it has no motion-run result yet. |
| `models/player/animation_updates.tres` | Adds the two saved basic-step GLBs to the existing resource list. The Woman export is an earlier prototype and differs from the later saved Woman source. |
| `docs/animation_work_status/solo_charleston_evidence/saved_asset_inventory.json` | Read-only Blender inventory: every source path, SHA-256, byte size, action names, participant roles, slots, ranges, curve counts and key times. |
| `docs/animation_work_status/solo_charleston_evidence/export_inventory.json` | GLB SHA-256, sizes, animation names, channel counts and durations. |
| `docs/animation_work_status/solo_charleston_evidence/manifest_Woman.json` | Historical full 58-clip Woman prototype run, including two failed full-turn clearance checks. |
| `docs/animation_work_status/solo_charleston_evidence/manifest_Man.json` | Latest one-clip Man basic 1930s author/bake/surface validation result. Earlier Man probes are in logs. |
| `docs/animation_work_status/solo_charleston_evidence/front_*.png`, `side_*.png` | Twelve already-rendered Woman basic views: frames 0, 10, 30, 50, 60 and 70, in front and side views. These show the first prototype's actual surfaces; they are not renders of the final script revision. |
| `docs/animation_work_status/solo_charleston_evidence/*.log` | Preserved discovery, rendering, authoring, failed and improved bake probes, test-selection and fast-suite evidence. See the log list below. |
| `docs/animation_work_status/solo_charleston_evidence/inventory.py` | Read-only Blender inventory command used at stop; its checkout path is explicit. |
| `docs/animation_work_status/solo_charleston_evidence/verification_at_stop.txt` | Final preservation verification results. |

### Exact source inventory

Every row below is an individual file under `animations/man_and_woman/`; the action name is the file stem, and the second action appends `.baked`. Man uses role `PLAYER` and `Man.rigify` / `Man.rigify_deform` slots; Woman uses `PARTNER` and the corresponding Woman slots. Timing is 24 fps, 144 BPM, ten frames per beat. Moving studies use frames 0–80 (3⅓ seconds); position studies use 0–40 (1⅔ seconds). The final frame is the repeated endpoint for loop clips. Quarter turns and position entry/exit clips are one-shot; holds and other movement studies are cyclic.

| File | Role | Frames | State and review |
| --- | --- | --- | --- |
| `solo_charleston_man_basic_1930s.blend` | PLAYER | 0–80 | Authored + half-frame baked + matching 48 Hz GLB; latest local numeric checks passed; game playback pending. |
| `solo_charleston_man_full_turn_left.blend` | PLAYER | 0–80 | Authored + rigid-joint integer-frame bake; earlier 6 mm bake tolerance passed (3.848 mm maximum); latest 3 mm policy remains unverified. |
| `solo_charleston_man_full_turn_right.blend` | PLAYER | 0–80 | Authored + earlier integer-frame bake; bake comparison failed (see validation_probe.log); export pending. |
| `solo_charleston_man_heel_digs.blend` | PLAYER | 0–80 | Authored + earlier integer-frame bake; bake comparison failed (see validation_probe.log); export pending. |
| `solo_charleston_woman_apple_jacks.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_arm_swing.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_back_flicks.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_basic_1920s.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_basic_1930s.blend` | PARTNER | 0–80 | Authored + baked; prototype IK checks passed; saved GLB is from an earlier source revision; final bake/surface checks pending. |
| `solo_charleston_woman_boogie_walk.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_cross_kicks.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_double_kicks.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_fall_off_the_log.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_forward_and_back.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_front_kicks.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_full_break.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_full_turn_left.blend` | PARTNER | 0–80 | Authored + baked blocking study; ankle-clearance FAILED; corrected procedural turn remains ungenerated for Woman. |
| `solo_charleston_woman_full_turn_right.blend` | PARTNER | 0–80 | Authored + baked blocking study; ankle-clearance FAILED; corrected procedural turn remains ungenerated for Woman. |
| `solo_charleston_woman_half_break.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_heel_digs.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_heel_toe_swivels.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_kick_ball_change.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_kick_through.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_knee_lifts.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_pecking.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_pigeon_toes.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_position_left_back_flick_enter.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_left_back_flick_exit.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_left_back_flick_hold.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_left_kick_enter.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_left_kick_exit.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_left_kick_hold.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_low_enter.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_low_exit.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_low_hold.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_ready_enter.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_ready_exit.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_ready_hold.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_right_back_flick_enter.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_right_back_flick_exit.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_right_back_flick_hold.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_right_kick_enter.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_right_kick_exit.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_right_kick_hold.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_scarecrow_enter.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_scarecrow_exit.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_scarecrow_hold.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_upright_enter.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_upright_exit.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_position_upright_hold.blend` | PARTNER | 0–40 | Authored + baked position study; early numeric checks passed; latest entry/exit refinements and transition matching pending. |
| `solo_charleston_woman_quarter_turn_left.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_quarter_turn_right.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_reverse_basic.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_rock_step.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_scarecrow.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_scissor_steps.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_shorty_george.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_side_kicks.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_side_to_side.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_suzie_q.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_tackie_annie.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |
| `solo_charleston_woman_toe_taps.blend` | PARTNER | 0–80 | Authored + baked blocking study; early numeric checks passed; final bake/surface and visual approval pending. |

### Exact exports

- `models/player/animation_updates/solo_charleston_man_basic_1930s_baked_b02170844dca.glb` (414,400 bytes), plus its adjacent `.glb.import`: 636 channels, 3.333333 seconds.
- `models/player/animation_updates/solo_charleston_woman_basic_1930s_baked_b1647ff0729b.glb` (348,616 bytes), plus its adjacent `.glb.import`: 630 channels, 3.333333 seconds.

Both GLBs are single-participant clips. Native Godot import, loop flags and playback against the composed runtime model remain unverified. The two `.import` files configure the existing animation-library post-import script and cyclic playback.

## Validation and known failures

- Required fast suite: `python tests/run_tests.py --suite fast` passed **9/9** at preservation (2.91 seconds). An earlier run passed 8/9 because three hair mesh resources were LFS pointers; fetching `apps/a-game/playground/hair/physics/*_mesh.res` fixed the environment and subsequent runs passed.
- Explicit changed-script selection: `python tests/run_tests.py --changed scripts/solo_charleston/author.py --changed scripts/solo_charleston/repertoire.py --changed scripts/solo_charleston/review.py` passed **9/9** (2.84 seconds); it selected zero slow checks.
- Full automatic change selection was listed, not executed: **9 fast + 186 slow** checks, triggered transitively by the animation directory and shared update resource. Full Godot imports, unrelated hydrated assets and Game Rig Tools remain prerequisites for portions of that selection. This record makes no full-suite claim.
- After rebase onto `18e528c73`, the updated required fast suite passed **10/10** in 6.04 seconds; see `fast_after_rebase.log`.
- Python syntax check of all three task scripts passed after the final contact-check edit.
- Blender 5.2.2 read-only saved-file inventory succeeded for all **62 sources / 124 actions** after authoring stopped. Sources contain action data and descriptor scenes, with zero saved objects or meshes.
- Structural GLB inspection passed for both exports: one named clip each and the expected 3⅓-second duration. This is not a game-playback test.
- First Woman basic: maximum foot-target error 0.179 mm, plant drift 0.104 mm, wrist bend 12.134°, coincident loop endpoints. Front/side inspection covered frames 0, 10, 30, 50, 60, 70 of this early prototype. Complete mesh-clearance certification, fingers, and continuous playback remain pending.
- The full Woman prototype run passed its early proxy checks for 56 clips; **both full turns failed ankle clearance**. The revised eight-step turns exist in the script and Man probes only. The Woman files preserve their failed studies intentionally.
- Early native bakes with full transform constraints produced about 9–14 mm endpoint differences. `validation_probe.log` and `bake_probe.log` preserve those failures. Temporary connected-joint changes alone did not fix them (`bake_fix.log`).
- A disposable bake rig with independent joint translations and copied positions/rotations gave better rigid-transform comparisons (`bake_rigid.log`). This adaptation preserves shared source files and rest matrices, but its effect on deformation still warrants production review.
- Latest **Man basic 1930s** (`half_bake.log`): editable IK error 0.202 mm, plant drift 0.117 mm, maximum wrist bend 11.805°, zero endpoint mismatch; loop velocity mismatch 0.120903 m/s; **321 quarter-frame bake samples** yielded maximum position error **1.484 mm** and rotation error **0.014681 rad**; **33 evaluated-surface samples** yielded minimum floor height **−0.058 mm**, zero measured support gap. The corresponding source stores half-frame baked keys and its GLB samples at 48 Hz with the source duration preserved.
- Review limits: spherical ankle and hand/torso proxies are partial clearance diagnostics. Full self-intersection checks, finger contact, whole-repertoire visual review, transition endpoint matching, baked loop velocity, and runtime playback remain outstanding. “Passed” fields in historical manifests apply only to the checks and code revision used for that run.
- The final turn and swivel contact-check edit in `review.py` was made just before the stop and has **syntax validation only**. The generator currently publishes local files even for a failed report; add an explicit acceptance gate before future production publication.

Preserved log files:

- `bake_diagnosis.log`
- `bake_fix.log`
- `bake_probe.log`
- `bake_rigid.log`
- `fast.log`
- `first.log`
- `fixes.log`
- `half_bake.log`
- `inspect.log`
- `install.log`
- `inventory.log`
- `mesh_probe.log`
- `probe.log`
- `render.log`
- `repertoire_probe.log`
- `repertoire_probe2.log`
- `test_selection.log`
- `validation_probe.log`

## Processes, storage and environment

At the stop, process inspection showed **zero active Blender or task authoring processes**. The first broad prototype process (PID 1407) had been terminated earlier during iteration; its current outputs were subsequently superseded by the completed second prototype run. The completed render, probe, export and inventory runs are represented by saved outputs and logs. There is no paused computation to resume.

`/tmp/charleston/` retains temporary diagnostic scripts/logs and an environment-backed Git askpass helper; credentials were never printed or committed. Durable logs and the twelve existing renders have been copied into the evidence directory. `.cache/solo_charleston/` holds duplicate exports and the two historical manifests; the manifests are preserved here, and each distinct exported GLB is committed in its normal asset path. Installed Blender preferences and downloaded pre-existing LFS dependencies are environment setup, not task source changes.

All task binary files were measured before staging. Each is at most 104,857,600 bytes and is stored directly in Git. The initial task commit used exact-path exceptions for its 62 sources, two exports and twelve PNGs. Rebase onto `18e528c73` brought the concurrent repository-wide generated 100 MiB policy. The conflict was resolved by retaining that upstream policy; the task requires zero extra exceptions, and all 76 binaries remain regular Git blobs. `python scripts/lfs_policy.py check` passed for 23,463 staged files. `storage_audit.json` records each path, actual size and effective Git attributes. Existing shared assets were hydrated using the configured `SANJO_GITHUB_LFS_TOKEN` through the sanctioned proxy with the `codex.sanjo.solutions@gmail.com` identity. Those dependency assets remain unchanged in Git.

## Integration dependency changes

The preserved task commits are `220c124afaa189ff9227d7cd762ebdc266f36a5b` (assets and status) and `75cdf5801e10a3458597e06c6a5d82ec668f19a2` (workflow documentation and post-rebase evidence). Integration began from freshly fetched main `074c6a02e32d1d0c6960425218e8abec83e3c9b0`. Merge resolution retained both AGENTS additions and the union of all 21 animation-update library references. The integrated fast suite passed **10/10** in 6.05 seconds (`fast_integrated.log`); the storage policy passed for 24,209 staged files before adding that log.

Rebase onto `18e528c73` also brought concurrent updates to `animations/man_and_woman/shared_scene_data.blend`, `man_and_woman3.blend`, `man_anatomical_study.blend`, and `woman_anatomical_study_speculum.blend`. Those upstream binaries are preserved. The motion reports describe the pre-integration dependencies at the stopping point; compatibility and playback against the newer shared sources remain pending under the stop instruction. The updated repository also supplies the previously absent bundled Game Rig Tools installer. Read its current setup instructions before resuming.

## Remaining work and blockers

1. The current user instruction blocks further authoring, generation, refinement and rendering. Resume only when the user authorizes animation work again.
2. Review the current scripts against the preserved versions and reports. Validate the final contact-check edit and add an explicit publish-on-success gate.
3. Reconcile the native rigid-joint baking study with Game Rig Tools, which was absent in this environment during authoring. The integrated main now provides bundled tools through `scripts/blender/install_animation_tools.py`; installation and use are deferred until renewed animation authorization. Verify saved baked playback and runtime skeleton/mesh fidelity.
4. Complete the Man repertoire and the missing three right-lead Woman phrases. Regenerate only after reviewing the latest code changes. The script's current default regenerates all selected outputs in place.
5. Replace the two failed Woman full-turn studies; regenerate and check position entry/exit clips against their held endpoints. Review heel-dig foot pitch, swiveled ball contacts, hopping support and all transitions.
6. Run the latest interpolated checks for all files, including actual mesh clearance, finger comfort, foot soles, loop velocities, baked playback and Godot import. Historical proxy checks provide preliminary evidence only.
7. Refresh the stale Woman basic export and export the rest only after acceptance. Keep existing update-library entries belonging to other animation tasks during publication and integration.
8. The generator temporarily changes finger controls to XYZ Euler rotation, while the integrated shared-rig guidance specifies quaternion controls. Saved-source finger channel compatibility needs verification and likely correction; the current assets remain preserved studies.
9. Complete full-repertoire visual review and ordinary playback. The preserved twelve images cover only the first Woman basic prototype.

## Exact resume commands

Read this record and the latest repository `AGENTS.md` first. The following verification is read-only with respect to authored assets:

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender --version
python tests/run_tests.py --suite fast
python -m py_compile scripts/solo_charleston/author.py scripts/solo_charleston/repertoire.py scripts/solo_charleston/review.py
blender --background --factory-startup --threads 4 --python-exit-code 1 --python docs/animation_work_status/solo_charleston_evidence/inventory.py
python tests/run_tests.py --list
```

After renewed authorization and the review/fix steps above, the precise narrow authoring command is:

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender --background --threads 4 animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/solo_charleston/author.py -- --only basic_1930s --character Man --export
```

That command overwrites the selected source and export. `--character Woman` selects the other character; comma-separated `--only` names limit the phrase set. Omitting `--export` saves authored/baked sources only. A future full regeneration command, after the blockers are resolved, is:

```bash
blender --background --threads 4 animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/solo_charleston/author.py -- --character both --export
```

The script writes `manifest_both.json` under `.cache/solo_charleston/`; archive validated reports with source hashes. Recheck sizes and effective attributes before staging any regenerated files. Preserve the existing combined library, shared scene and other tasks' actions. For integration, fetch immediately before rebasing/merging and use ordinary pushes; integrate newer remote main after a push rejection. GitHub commit messages and communications for this checkpoint are authored by Codex.
