# Lyrical dance solo animation checkpoint

## Identity and stop instruction

- Date: October 2, 2026 (Europe/Berlin).
- Chat/task title: Lyrical dance solo animations for man_and_woman3.blend (descriptive task title).
- Project: A-Game, `/workspace/sanjo-solutions/apps/a-game`, sanjo-solutions cloud environment.
- Task branch: `codex/lyrical-dance`.
- Starting/pre-checkpoint commit: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Author of this checkpoint and GitHub delivery: Codex.
- Latest user instruction: stop animation authoring, refinement, generation, and rendering; preserve the current state, record it, commit it, integrate current main, and push. This instruction supersedes completion of the repertoire. Resume animation work only after a new user instruction.

## Integration update

The checkpoint was committed as `893c978dfbd98bc531d2ece4d73cc86335dd6bcd`, then rebased onto `origin/main` at `18e528c73`. Its rebased task commit is `99ec12f26a2648e1507ede6bf5b6bdd1a6608e75`. The sole conflict was `.gitattributes`: concurrent main had replaced broad extension-based LFS rules with the generated 100 MiB policy. That newer policy was preserved in full. Every task binary remains a real regular-Git blob; exact-file exceptions became unnecessary. `storage_audit.json` preserves the historical pre-rebase checks; `integration_storage_audit.json` records final attributes and hashes. The original unrebased commit remains only a local recovery reference.

Concurrent main also supplies bundled Game Rig Tools setup and additional authoring guidance. The initial environment limitation below describes the stopped authoring run; future work should follow `scripts/blender/README.md` and `scripts/blender/install_animation_tools.py`. This integration does not regenerate or revalidate motion against changed shared dependencies.

## Original scope

Create a broad organized lyrical dance repertoire for separate Man and Woman solos, using Blender 5.2, repository native IK and one-file-per-animation workflow, reusing suitable existing motion, validating interpolated contacts/clearance/loops, baking and exporting, recording animation guidance, and committing/rebasing/merging/pushing. Lyrical dance has an open vocabulary; the procedural catalog proposes 72 named clips per character, rather than an exhaustive world catalog.

## Preserved completion and limitations

126 Blender source files are saved and independently readable: **72 Woman, 54 Man**. Each contains a solo authoring action. The source family covers standing and arm positions, plié, contraction/release and breath phrases, side/diagonal reaches, arabesque/passé/attitude balances, tendus, développés, ronds de jambe, pivot turns, steps, jumps/leaps, and seated/kneeling phrases. The Woman sources also include battements, fan kicks, half pivots, and experimental kneel/seat transitions. The table below is authoritative for the saved subset.

**These are partial procedural blocking studies, not a finished or approved animation library.** The saved numeric reports contain 111 provisional proxy passes and 15 failures. Validation currently measures control-rig ORG endpoints for reach/contact and evaluated skin for the floor. Diagnostic work found that the Man's deform foot shifts despite stable ORG endpoints. The current proxy passes therefore do not establish planted final skinned contacts. Hand/body clearance uses spherical proxies, not full mesh self-intersection detection. Loop position/orientation and finite-difference linear velocity are sampled; angular-velocity continuity still needs its own check. Wrist/finger comfort and full animated visual review remain outstanding.

One source, `lyrical_woman_position_parallel.blend`, additionally contains its native Blender visual bake, `lyrical_woman_position_parallel.baked`, and has one published compact GLB. All other sources are **authoring only**. The export prototype uses Blender 5.2 native `bpy_extras.anim_utils.bake_action`, the repository's `AnimationClipScene`, and `AnimationUpdates`. Game Rig Tools is absent from the environment; its normal Action Bakery path has not been exercised. The one clip's sampled bake deviation is 0.0000027593 m. Its GLB has 630 channels, 259,412 bytes, and 49 sampled frames (0–48 at 24 fps). Godot reads the sole imported clip with a two-second duration, linear looping, and animation tracks; end-to-end character playback remains unverified.

The combined `man_and_woman3.blend`, shared scene, anatomical sources, existing animation sources, and shared rig definitions retain their repository contents. Player Asset Export discovers the new source filenames on reopening the combined library. `models/player/animation_updates.tres` adds only the one lyrical GLB to its previous references.

## Relevant files

All paths in this record are relative to `apps/a-game`.

- `scripts/lyrical_dance/catalog.py`: 72 proposed motifs per actor; reuses `GymnasticsCatalog` pose dictionaries and native yoga/workout IK tools. No existing animation binaries were rewritten. Reuse here is pose/choreography vocabulary, not a wholesale copied approved dance action.
- `scripts/lyrical_dance/build.py`: partial authoring pipeline, sparse control curves, role metadata, markers, native action-file writer, half-frame checks and report output. Stationary curves have one initial key. Looping movement includes boundary settling poses.
- `scripts/lyrical_dance/export.py`: prototype visual bake, four sampled bake comparisons, compact per-clip publication, and re-saving source with matching baked action. Its guard reads provisional numeric reports; fix the validation limitations before relying on it for production export.
- `scripts/lyrical_dance/render.py`: Blender Workbench pose-sheet renderer; full final visual review remains pending.
- `scripts/lyrical_dance/verify_checkpoint.py`: read-only Blender source and GLB inventory verifier.
- `scripts/lyrical_dance/inspect_foot_deformation.py`, `inspect_foot_constraints.py`: saved diagnostic probes for the unresolved Man foot issue; run from the app directory.
- `scripts/lyrical_dance/review/checkpoint_inventory.json`: exact source paths, byte sizes, SHA-256, action names, authored/baked status, roles, frame ranges, slots, markers and channel counts; includes exported GLB identity.
- `scripts/lyrical_dance/review/man_validation.json`, `woman_validation.json`: last completed per-clip measurements. Man run is partial (54/72).
- `scripts/lyrical_dance/review/woman_exports.json`: the single completed bake/export receipt.
- `scripts/lyrical_dance/review/woman_poses_01.png`, `woman_poses_02.png`: **superseded exploratory pose sheets** from the earlier Woman build. They are preserved evidence, not final visuals; sheet framing truncates some labels. No Man sheets exist.
- `scripts/lyrical_dance/review/logs/`: initial and revised build logs, export probe, render logs, foot diagnostics, interrupted integration runs, fast-suite runs, and source-read verification.
- `scripts/lyrical_dance/review/storage_audit.json`: all 129 binary assets, measured sizes and hashes, and before/after Git attribute checks.
- `models/player/animation_updates/lyrical_woman_position_parallel_baked_07563961c366.glb` and adjacent `.glb.import`: sole generated game clip, configured as a looping AnimationLibrary with the existing import script.
- Repository `.gitattributes`: concurrent main's generated 100 MiB policy is preserved. All 126 sources, one GLB, and two PNGs use regular Git. Largest task binary is 1,356,856 bytes; every task binary is below 104,857,600 bytes. The pre-rebase exact-file exceptions are superseded by the repository policy.

The procedural scripts are ahead of the saved animation state: the catalog's final diagonal reach reduction and traveling leap offsets were edited after the last builds started. Saved source `Choreography` metadata and the inventory describe the actual assets. Re-running the current catalog changes those assets; it is not a byte-identical reproduction of this checkpoint. The final builder report-merging/assertion guard and export validation guard also postdate the running build's loaded module. Preserve this checkpoint before future regeneration.

## Validation and process state

All Blender authoring, inspection, rendering, and export used **Blender 5.2.2 LTS**, build `d13f752e3b9c`. Installed Godot is **4.6.3**, while workflow documentation references 4.7.2.

- `blender --background --factory-startup --python-exit-code 1 --python scripts/lyrical_dance/verify_checkpoint.py`: **passes**, 126 readable source files and one structurally readable GLB. This is file preservation verification, not final motion approval.
- `godot --headless --path . --script scripts/lyrical_dance/verify_export.gd`: passes for the sole imported clip; see `logs/checkpoint_godot_export.log`.
- Post-rebase `python tests/run_tests.py --suite fast`: **9/10 passed**; concurrent main adds a tenth fast check. The same activity JSON check remains blocked by the seven hair model imports. See `logs/integration_fast.log`.
- `python scripts/lfs_policy.py check`: **passes**, 23,514 indexed files at the checkpoint integration; all 129 task binaries retain their original hashes and real Git blobs (`integration_storage_audit.json`).
- `python tests/run_tests.py --suite fast`: earlier run **9/9 passed** (`logs/lyrical_fast.log`). Stop-time rerun **8/9 passed** (`logs/checkpoint_fast.log`). Activity JSON reports unresolved `playground/hair/models/{bob01,bob02,short01,short02,short03,short04,afro01}.glb`, causing dependent character-class compilation errors after the broader editor checks changed local import caches.
- `python tests/run_tests.py --slow-timeout 60`: attempted broader related selection (9 fast, 186 slow); interrupted after repeated missing resource/import errors and timeout. See `logs/lyrical_related.log`.
- `python tests/run_tests.py --changed animations/man_and_woman/lyrical_woman_position_parallel.blend --slow-timeout 60`: attempted source-focused selection (9 fast, 57 slow); interrupted at the stop instruction. Some checks passed; several failed or timed out with checkout resource/engine prerequisites. See `logs/lyrical_source_tests.log`. This suite is incomplete and is not a pass.
- The authoring builder samples every 0.5 frame, recording reach, declared ankle contact drift, evaluated-body floor minimum, hand/chest and hand/pelvis spherical clearance, loop position/orientation, and finite-difference boundary velocity. Thresholds include 4 mm reach, 3 mm contact drift, floor greater than -6 mm, and 0.06 m/s loop velocity difference. These thresholds and the control/deform discrepancy require review before production acceptance.
- Woman's final run completed 72 source saves. Man process PID 1726 reached 54 source saves; it was terminated at the stop request. Initial SIGINT was ineffective; SIGTERM stopped it. Test runner PID 2605 and active Godot child were also stopped. No owned animation or test process remains active. Unsaved in-memory poses from the interrupted next Man clip are discarded; each completed source stays preserved.
- Test-created changes to previously tracked `.import` files were restored after stopping the runners. These were generated checkout churn; the task's new lyrical import file and registry addition remain saved.

### Known measured failures

- `lyrical_man_body_wave`: reach 0.000228 m; floor minimum -0.009565 m.
- `lyrical_man_hinge_recovery`: reach 0.000228 m; floor minimum -0.007977 m.
- `lyrical_man_plie_rebound`: reach 0.000224 m; floor minimum -0.009565 m.
- `lyrical_man_saute`: reach 0.000233 m; floor minimum -0.009565 m.
- `lyrical_man_split_leap_left`: reach 0.000233 m; floor minimum -0.015037 m.
- `lyrical_man_stag_leap_left`: reach 0.000233 m; floor minimum -0.015037 m.
- `lyrical_woman_diagonal_reach_left`: reach 0.005100 m; floor minimum 0.005971 m.
- `lyrical_woman_split_leap_left`: reach 0.000223 m; floor minimum -0.010755 m.
- `lyrical_woman_stag_leap_left`: reach 0.000223 m; floor minimum -0.010755 m.
- `lyrical_woman_diagonal_reach_right`: reach 0.005100 m; floor minimum 0.005971 m.
- `lyrical_woman_split_leap_right`: reach 0.000223 m; floor minimum -0.010755 m.
- `lyrical_woman_stag_leap_right`: reach 0.000223 m; floor minimum -0.010755 m.
- `lyrical_woman_seated_spiral`: reach 0.000122 m; floor minimum -0.006450 m.
- `lyrical_woman_kneel_to_seat`: reach 0.149987 m; floor minimum -0.104396 m.
- `lyrical_woman_seat_to_kneel`: reach 0.149988 m; floor minimum -0.163292 m.

### Concrete blockers and next work

1. Respect the user stop instruction; authoring resumes only on a new request.
2. The Man's `DEF-foot`/`DEF-toe` endpoint moves during plié/contraction while ORG-foot stays fixed. Diagnostic vertex 7373 (85.15% DEF-foot.R, 14.85% DEF-toe.R) changes ground height from +0.0060 to -0.00415 m in contraction. The control-rig DEF-foot follows `foot_tweak.R` plus Stretch To; the deform rig copies its location/rotation. Investigate and calibrate the actual deform endpoint; no fix was applied before stopping.
3. Woman diagonal reach max error is about 5.10 mm. The reduction in the current catalog has yet to be generated or validated.
4. Split/stag takeoff floor minimum is about -10.75 mm for Woman and -15.04 mm for Man. Traveling offsets are only in the newer procedural catalog. Fix takeoff/landing foot clearance and verify support phases.
5. Woman seated spiral reaches -6.45 mm floor clearance. Kneel-to-seat and reverse are **blocked transition studies**: about 150 mm reach error and 104–163 mm floor penetration. They are unsuitable for playback pending substantial re-authoring.
6. Complete the missing 18 Man clips (`battement_left`, `battement_right`, `developpe_right`, `fan_kick_left`, `fan_kick_right`, `half_pivot_left`, `half_pivot_right`, `kneel_to_seat`, `kneeling_port_de_bras`, `passe_turn_right`, `rond_de_jambe_right`, `seat_to_kneel`, `seated_fold_release`, `seated_spiral`, `side_step_right`, `split_leap_right`, `stag_leap_right`, `step_through_right`) only after stabilizing the shared motions. Recheck existing provisional passes using deform contacts, angular velocity, joint/wrist comfort, skin clearance and visual playback. Expand vocabulary if requested; the present catalog remains a subset.
7. Bake/export the remaining approved files, verify Godot role binding, looping and skeleton layout, and review the one prototype export against the normal Action Bakery workflow when the add-on is available.
8. Restore the Godot project's imported-resource prerequisites and use its documented engine version before rerunning the broader integration suites.

## Exact resume/verification commands

Commands run from `/workspace/sanjo-solutions/apps/a-game`. Verification commands may run while work remains paused:

```bash
blender --version
blender --background --factory-startup --python-exit-code 1 --python scripts/lyrical_dance/verify_checkpoint.py
python tests/run_tests.py --suite fast
blender --background --factory-startup animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/lyrical_dance/inspect_foot_deformation.py
blender --background --factory-startup animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/lyrical_dance/inspect_foot_constraints.py
```

Only after a new instruction to resume, preserve the checkpoint, fix the blockers, then use these existing entry points (they replace task-owned outputs):

```bash
blender --background --factory-startup animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/lyrical_dance/build.py -- --actor woman --only diagonal_reach_left,diagonal_reach_right
blender --background --factory-startup animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/lyrical_dance/build.py -- --actor man
blender --background --factory-startup animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/lyrical_dance/render.py -- woman
blender --background --factory-startup animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/lyrical_dance/export.py -- --actor woman --only position_parallel
python tests/run_tests.py --changed animations/man_and_woman/lyrical_woman_position_parallel.blend
```

Run exports serially because `AnimationUpdates.publish()` updates the shared registry. Before staging, repeat actual byte-size and `git check-attr` checks; files at or below 100 MiB belong in regular Git. Integrate current `origin/main` immediately before pushing, union concurrent animation registry references, and preserve other tasks' sources and documentation. Use one `Co-authored-by: Codex <noreply@openai.com>` trailer for each new commit.

## Saved source inventory

All rows use 24 fps. PLAYER is the Man solo; PARTNER is the Woman solo. Every row remains a partial study even when its existing proxy measurements pass. For full hashes, action slots, markers and channel counts, use `checkpoint_inventory.json`.

| Source file | Frames | Role | Playback | Saved state | Existing numeric review |
| --- | --- | --- | --- | --- | --- |
| `animations/man_and_woman/lyrical_man_arabesque_balance_left.blend` | 0–72 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_arabesque_balance_right.blend` | 0–72 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_attitude_balance_left.blend` | 0–72 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_attitude_balance_right.blend` | 0–72 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_body_wave.blend` | 0–96 | PLAYER | LOOP | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_man_breath_and_suspend.blend` | 0–96 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_contraction_release.blend` | 0–72 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_developpe_left.blend` | 0–96 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_diagonal_reach_left.blend` | 0–72 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_diagonal_reach_right.blend` | 0–72 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_hinge_recovery.blend` | 0–72 | PLAYER | LOOP | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_man_passe_balance_left.blend` | 0–72 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_passe_balance_right.blend` | 0–72 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_passe_turn_left.blend` | 0–90 | PLAYER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_plie_rebound.blend` | 0–72 | PLAYER | LOOP | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_man_port_de_bras.blend` | 0–120 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_arabesque_left.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_arabesque_right.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_arms_fifth.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_arms_first.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_arms_second.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_attitude_left.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_attitude_right.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_contraction.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_fifth.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_first.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_fourth.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_hinge.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_kneel.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_low_v.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_lunge_left.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_lunge_right.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_parallel.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_passe_left.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_passe_right.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_plie.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_release.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_seated.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_second.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_position_third.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_rond_de_jambe_left.blend` | 0–96 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_saute.blend` | 0–60 | PLAYER | ONCE | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_man_side_step_left.blend` | 0–64 | PLAYER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_side_tilt_left.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_side_tilt_right.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_split_leap_left.blend` | 0–60 | PLAYER | ONCE | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_man_stag_leap_left.blend` | 0–60 | PLAYER | ONCE | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_man_step_through_left.blend` | 0–64 | PLAYER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_tendu_back_left.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_tendu_back_right.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_tendu_front_left.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_tendu_front_right.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_tendu_side_left.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_man_tendu_side_right.blend` | 0–48 | PLAYER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_arabesque_balance_left.blend` | 0–72 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_arabesque_balance_right.blend` | 0–72 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_attitude_balance_left.blend` | 0–72 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_attitude_balance_right.blend` | 0–72 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_battement_left.blend` | 0–40 | PARTNER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_battement_right.blend` | 0–40 | PARTNER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_body_wave.blend` | 0–96 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_breath_and_suspend.blend` | 0–96 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_contraction_release.blend` | 0–72 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_developpe_left.blend` | 0–96 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_developpe_right.blend` | 0–96 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_diagonal_reach_left.blend` | 0–72 | PARTNER | LOOP | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_woman_diagonal_reach_right.blend` | 0–72 | PARTNER | LOOP | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_woman_fan_kick_left.blend` | 0–52 | PARTNER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_fan_kick_right.blend` | 0–52 | PARTNER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_half_pivot_left.blend` | 0–64 | PARTNER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_half_pivot_right.blend` | 0–64 | PARTNER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_hinge_recovery.blend` | 0–72 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_kneel_to_seat.blend` | 0–64 | PARTNER | ONCE | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_woman_kneeling_port_de_bras.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_passe_balance_left.blend` | 0–72 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_passe_balance_right.blend` | 0–72 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_passe_turn_left.blend` | 0–90 | PARTNER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_passe_turn_right.blend` | 0–90 | PARTNER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_plie_rebound.blend` | 0–72 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_port_de_bras.blend` | 0–120 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_arabesque_left.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_arabesque_right.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_arms_fifth.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_arms_first.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_arms_second.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_attitude_left.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_attitude_right.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_contraction.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_fifth.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_first.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_fourth.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_hinge.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_kneel.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_low_v.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_lunge_left.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_lunge_right.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_parallel.blend` | 0–48 | PARTNER | LOOP | Baked + GLB | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_passe_left.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_passe_right.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_plie.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_release.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_seated.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_second.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_position_third.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_rond_de_jambe_left.blend` | 0–96 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_rond_de_jambe_right.blend` | 0–96 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_saute.blend` | 0–60 | PARTNER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_seat_to_kneel.blend` | 0–64 | PARTNER | ONCE | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_woman_seated_fold_release.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_seated_spiral.blend` | 0–48 | PARTNER | LOOP | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_woman_side_step_left.blend` | 0–64 | PARTNER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_side_step_right.blend` | 0–64 | PARTNER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_side_tilt_left.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_side_tilt_right.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_split_leap_left.blend` | 0–60 | PARTNER | ONCE | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_woman_split_leap_right.blend` | 0–60 | PARTNER | ONCE | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_woman_stag_leap_left.blend` | 0–60 | PARTNER | ONCE | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_woman_stag_leap_right.blend` | 0–60 | PARTNER | ONCE | Authored only | Fails; see JSON |
| `animations/man_and_woman/lyrical_woman_step_through_left.blend` | 0–64 | PARTNER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_step_through_right.blend` | 0–64 | PARTNER | ONCE | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_tendu_back_left.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_tendu_back_right.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_tendu_front_left.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_tendu_front_right.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_tendu_side_left.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
| `animations/man_and_woman/lyrical_woman_tendu_side_right.blend` | 0–48 | PARTNER | LOOP | Authored only | Proxy pass; provisional |
