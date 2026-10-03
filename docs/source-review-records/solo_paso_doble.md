# Solo paso doble work status

Date: 2026-10-02 (Europe/Berlin). Author: Codex.
Chat title: **Create paso doble animations**.
Chat ID: `01a0fd0a-51ee-7699-b7db-c9562dafe063`.
Environment: sanjo-solutions cloud; checkout `/workspace/sanjo-solutions`; app `apps/a-game`.
Task branch: `codex/solo-paso-doble`.
Commit at the stop: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.

## Stopped state

The user stopped animation work and requested preservation, documentation, commits, and integration into main. Authoring, refinement, generation, and rendering stopped. The owned Blender processes had already exited when the stop instruction was inspected. Further animation work awaits a new user instruction.

**Partial procedural blocking studies, with an open bake-fidelity failure.** Sixteen source/baked/export families exist for eight figures and positions, with a separate Man and Woman clip for each. These assets establish editable choreography studies; production motion acceptance remains pending. The repertoire specification contains 37 entries, intended to produce 74 solo clips. The complete requested repertoire remains unfinished.

The active `models/player/animation_updates.tres` catalogue retains its pre-task contents. This task's sixteen experimental references were removed during preservation. Their exact generated catalogue snapshot is retained in `solo_paso_doble/animation_updates_draft.tres`. The per-animation Blender library can still discover the sixteen study sources in its source directory.

## Original scope and workflow

Create a broad, organized solo paso doble repertoire for both rigs from `man_and_woman3.blend`, including positions, figures, transitions, natural motion, planted contacts, clearance, interpolation and loop checks. Reuse suitable motion helpers; follow the per-animation authoring workflow; use Blender 5.2 for every Blender operation; commit assets, fetch/rebase, document animation guidance, merge main, upload required assets, and push while preserving concurrent work.

All executed Blender authoring, scripting, native visual baking, GLB export, inspection, and rendering used **Blender 5.2.2 LTS**, build `d13f752e3b9c`. The source scene was composed from `animations/man_and_woman/solo_disco_dance.blend` and the existing `shared_scene_data.blend`; the existing `DiscoCharacter`, `DiscoWristPoser`, and `RigYogaPoser` helpers supplied calibrated rig posing. The new timing and footwork came from `scripts/paso_doble/repertoire.py`.

Each saved source contains one editable action and its matching `.baked` action. Frame range **0–192**, 24 fps, 120 beats/minute, 16 musical beats, eight seconds, with frame 192 repeating the loop endpoint. Man clips use the single `Man.rigify` source slot, `Man.rigify_deform` baked slot, and `PLAYER` participant selection. Woman clips use the corresponding Woman slots and `PARTNER` selection. Each exported GLB contains only its selected character rig. The import sidecar sets looping.

The authoring pass uses sparse meaningful IK poses and a single key for constant channels. The native `bpy_extras.anim_utils` visual bake was used because Game Rig Tools was absent from the active Blender add-on set. Export used the repository's `AnimationClipScene`, glTF settings, `AnimationUpdates`, and `AnimationFileWriter`. The full animation-cache prerequisites were absent; these direct exports remain experimental pending the standard exporter/bake validation path.

## Exact saved assets

Every row has an editable source, a native visual-baked action inside that source, and a generated GLB plus the same GLB path followed by `.import`. All rows share the frame range and roles described above. “Saved” describes file presence and structure; the fidelity gate remains open for the entire set.

| Clip | Source `.blend` | Export `.glb` | Source bytes | Export bytes |
| --- | --- | --- | ---: | ---: |
| `solo_paso_doble_appel_man` | `animations/man_and_woman/solo_paso_doble_appel_man.blend` | `models/player/animation_updates/solo_paso_doble_appel_man_baked_d4cca325e5b4.glb` | 1513056 | 483948 |
| `solo_paso_doble_appel_woman` | `animations/man_and_woman/solo_paso_doble_appel_woman.blend` | `models/player/animation_updates/solo_paso_doble_appel_woman_baked_ada0b01056fb.glb` | 1510217 | 486032 |
| `solo_paso_doble_attack_man` | `animations/man_and_woman/solo_paso_doble_attack_man.blend` | `models/player/animation_updates/solo_paso_doble_attack_man_baked_a6389fb0c9c9.glb` | 1607741 | 507560 |
| `solo_paso_doble_attack_woman` | `animations/man_and_woman/solo_paso_doble_attack_woman.blend` | `models/player/animation_updates/solo_paso_doble_attack_woman_baked_5ac0fa362676.glb` | 1605717 | 530452 |
| `solo_paso_doble_basic_forward_man` | `animations/man_and_woman/solo_paso_doble_basic_forward_man.blend` | `models/player/animation_updates/solo_paso_doble_basic_forward_man_baked_9c0abc686436.glb` | 1540877 | 479228 |
| `solo_paso_doble_basic_forward_woman` | `animations/man_and_woman/solo_paso_doble_basic_forward_woman.blend` | `models/player/animation_updates/solo_paso_doble_basic_forward_woman_baked_62e4e1c6688b.glb` | 1535230 | 494324 |
| `solo_paso_doble_flamenco_taps_man` | `animations/man_and_woman/solo_paso_doble_flamenco_taps_man.blend` | `models/player/animation_updates/solo_paso_doble_flamenco_taps_man_baked_dd42a95f3e0e.glb` | 1545125 | 499008 |
| `solo_paso_doble_flamenco_taps_woman` | `animations/man_and_woman/solo_paso_doble_flamenco_taps_woman.blend` | `models/player/animation_updates/solo_paso_doble_flamenco_taps_woman_baked_aeb0c3cac872.glb` | 1542068 | 496496 |
| `solo_paso_doble_position_high_cape_man` | `animations/man_and_woman/solo_paso_doble_position_high_cape_man.blend` | `models/player/animation_updates/solo_paso_doble_position_high_cape_man_baked_353e82856200.glb` | 1216822 | 396904 |
| `solo_paso_doble_position_high_cape_woman` | `animations/man_and_woman/solo_paso_doble_position_high_cape_woman.blend` | `models/player/animation_updates/solo_paso_doble_position_high_cape_woman_baked_55b07b60a608.glb` | 1233238 | 399908 |
| `solo_paso_doble_position_spanish_line_left_man` | `animations/man_and_woman/solo_paso_doble_position_spanish_line_left_man.blend` | `models/player/animation_updates/solo_paso_doble_position_spanish_line_left_man_baked_75127a8ba9b1.glb` | 1266465 | 394188 |
| `solo_paso_doble_position_spanish_line_left_woman` | `animations/man_and_woman/solo_paso_doble_position_spanish_line_left_woman.blend` | `models/player/animation_updates/solo_paso_doble_position_spanish_line_left_woman_baked_470112a31259.glb` | 1265856 | 382192 |
| `solo_paso_doble_spanish_lines_man` | `animations/man_and_woman/solo_paso_doble_spanish_lines_man.blend` | `models/player/animation_updates/solo_paso_doble_spanish_lines_man_baked_a9736cf23434.glb` | 1605579 | 517520 |
| `solo_paso_doble_spanish_lines_woman` | `animations/man_and_woman/solo_paso_doble_spanish_lines_woman.blend` | `models/player/animation_updates/solo_paso_doble_spanish_lines_woman_baked_75a9ce558679.glb` | 1614039 | 518212 |
| `solo_paso_doble_twist_turn_man` | `animations/man_and_woman/solo_paso_doble_twist_turn_man.blend` | `models/player/animation_updates/solo_paso_doble_twist_turn_man_baked_8edf392ff1c1.glb` | 1582819 | 502204 |
| `solo_paso_doble_twist_turn_woman` | `animations/man_and_woman/solo_paso_doble_twist_turn_woman.blend` | `models/player/animation_updates/solo_paso_doble_twist_turn_woman_baked_945879b11716.glb` | 1588123 | 507352 |

Paths in the table are relative to `apps/a-game`. `solo_paso_doble/asset_inventory.json` contains the exact role, frame range, duration, channel count, size, and source/export path for every family. `solo_paso_doble/asset_sizes.json` also includes the two retained render images.

## Supporting files and evidence

- `scripts/paso_doble/repertoire.py`: 37-entry draft catalogue, contact-event footwork, arm shapes, and loop timing. Contains several preliminary solo adaptations rather than a certified dance syllabus.
- `scripts/paso_doble/create.py`: original procedural study author, sparse keys, native bake, individual source writer, and experimental export. Treat this as a stopped work-in-progress builder. It overwrites matching destination sources; resume on a fresh branch after addressing the blockers.
- `scripts/paso_doble/validate.py`: half-frame evaluated control-rig contact, reach, wrist, torso-proxy clearance, knee-angle, continuity, and loop checks.
- `scripts/paso_doble/review.json`: all 17 recorded motion reviews: 16 passing saved studies and the failed travelling-spins Man attempt.
- `scripts/paso_doble/verify_saved.py`: persisted source/bake comparison; fails on the first clip and leaves the full report unwritten.
- `scripts/paso_doble/inspect_saved.py`: read-only structural inventory of all sixteen source/baked/export families; passes.
- `scripts/paso_doble/render_review.py`: pre-stop studio-render script. The render initially selected masked `Man.body`/`Woman.body` helpers. Its current source selects the visible anatomical surface objects.
- `docs/animation_work_status/solo_paso_doble/initial_build.log`, `turns_build.log`, and `steps_build.log`: original build output and measured motion results.
- `solo_paso_doble/saved_bake_verification.log` and `saved_bake_verification_after_stop.log`: original and repeated saved-bake failure.
- `solo_paso_doble/fast_tests_before_stop.log` and `fast_tests_after_stop.log`: fast-suite runs.
- `solo_paso_doble/asset_inventory.log`, `asset_inventory.json`, and `asset_sizes.json`: structural and storage evidence.
- `solo_paso_doble/selected_checks.txt`: repository test-runner selection, including nine fast and 57 broader slow checks.
- `solo_paso_doble/high_cape_woman_frame_48.png`: the one usable pre-stop surface render, visually inspected for the high-cape position. This single still provides limited pose evidence rather than full motion approval.
- `solo_paso_doble/initial_render_missing_body.png`: preserved diagnostic from the first render; only the eyes were visible because the base-body helper meshes evaluate to zero vertices.
- `solo_paso_doble/render_review.log`: usable render execution log.
- `solo_paso_doble/animation_updates_draft.tres`: generated activation snapshot, retained solely as review evidence.
- Root `.gitattributes`: the initial exact-file exceptions were superseded during rebase by upstream’s generated size-based policy. The final task preserves upstream attributes; all thirty-four binary assets remain full regular Git blobs. `python scripts/lfs_policy.py check` passes.

## Validation results and blockers

1. `python tests/run_tests.py --suite fast`: **9/9 pass** after the stop (3.46 seconds). An earlier preparation run passed 8/9 because three existing hair mesh files were Git LFS pointers. Scoped `git lfs pull` fetched `playground/hair/physics/*_mesh.res`; the next run and the post-stop run passed all nine.
2. Build-time `MotionValidator.sample`: **385 half-frame samples per saved clip**, 6,160 total samples across sixteen saved clips. Planted-foot, wrist, reach, local clearance-proxy, knee-angle, positional loop, rotational loop, and finite-difference loop-velocity checks passed for these source actions. These checks cover supplied landmarks/proxies; complete mesh-intersection and plantar-surface validation remain pending.
3. `blender -t 1 --background --factory-startup --python-exit-code 1 --python scripts/paso_doble/inspect_saved.py`: **passes all sixteen families**. Each has two correctly named actions, one role/slot each, frames 0–192, one eight-second GLB animation, the intended exported rig, and binary sizes below 100 MiB.
4. `blender -t 1 --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/paso_doble/verify_saved.py`: **fails** on `solo_paso_doble_appel_man`, maximum saved-bake position difference **0.06406096591617307 m**, against a 0.002 m bound. This failure reproduces after the stop. Root cause remains undiagnosed; the comparison covers matching bones, including potential helper bones. Later clips remain unverified for persisted bake fidelity. The `saved_review.json` success report was never created.
5. `travelling_spins` Man attempt: **fails before bake/save/export**, maximum hand reach error **0.119139895695854 m** and minimum elbow-to-torso proxy gap **-0.05674767985743988 m**. The source specification and failure log preserve this attempt; a travelling-spins `.blend` or GLB was never written. The Woman attempt was never reached.
6. `python tests/run_tests.py --list`: selects nine fast and 57 slow checks. The broad slow set remains outstanding. Several checks require Game Rig Tools, full animation-cache initialization, and additional hydrated source/game assets. The task-specific saved-asset inspection and failed fidelity verification were run; they establish explicit acceptance limits rather than a passing full integration result. Godot playback import and runtime character-track resolution remain pending.
7. The high-cape still was rendered and inspected before the stop. Full motion playback, all-angle surface clearance, style review, choreography accuracy, transition blending, and all-figure visual review remain pending.

## Processes and local outputs

Owned build processes exited naturally: the appel and steps batches completed; the turns batch exited with the travelling-spins validation error. The render and structural inventory processes completed. The bake verifier exited with the saved-bake mismatch. Process inspection at the stop found zero owned Blender processes. There are no queued authoring jobs.

Original temporary logs were under `/tmp/paso-*.log`; durable copies are listed above. `.cache/paso_doble/` retains duplicate per-clip export staging GLBs, per-clip JSON reports, `publish.lock`, and render PNGs. The committed source/export files, merged motion report, preserved logs, and two render images provide the durable state; duplicate cache files remain local. `/tmp/paso-git-askpass` is a local credential helper using the configured `SANJO_GITHUB_LFS_TOKEN`; it contains variable references rather than a credential value and is excluded from Git.

## Remaining repertoire

The following catalogue entries lack saved source/baked/export assets for either character:

- `position_attention`.
- `position_paso_frame`.
- `position_spanish_line_right`.
- `position_promenade`.
- `position_counter_promenade`.
- `position_low_cape`.
- `position_flamenco`.
- `position_matador_finish`.
- `sur_place`.
- `basic_backward`.
- `chasse_left`.
- `chasse_right`.
- `elevation`.
- `huit`.
- `separation`.
- `sixteen`.
- `promenade`.
- `promenade_close`.
- `grand_circle`.
- `fallaway_reverse`.
- `banderillas`.
- `travelling_spins` — failed Man motion attempt; Woman pending.
- `syncopated_separation`.
- `coup_de_pique`.
- `left_foot_variation`.
- `fregolina`.
- `farol`.
- `entry_salute`.
- `closing_salute`.

Resume work also needs qualified review of the draft footwork adaptations, a resolution of the saved-bake discrepancy, mesh and support validation, full visual review, reliable standard exporter integration, and game playback verification before production activation. Existing names describe procedural study intent rather than a claim that the complete dance syllabus has been authored.

## Exact resume commands

Read-only verification remains safe during preservation. Run from `/workspace/sanjo-solutions/apps/a-game`:

```bash
blender --version
python tests/run_tests.py --suite fast
blender -t 1 --background --factory-startup --python-exit-code 1 --python scripts/paso_doble/inspect_saved.py
blender -t 1 --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/paso_doble/verify_saved.py
python tests/run_tests.py --list
```

After a future explicit instruction to resume animation work, first diagnose the persisted bake mismatch and the travelling-spin reach/pole path, then use a new task branch. The following commands are exact examples of the stopped authoring and rendering paths; they are **resume-only**, and were not run after the stop:

```bash
blender -t 2 --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/paso_doble/create.py -- travelling_spins
blender -t 2 --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/paso_doble/create.py -- sur_place basic_backward chasse_left chasse_right
blender -t 1 --background animations/man_and_woman/solo_paso_doble_position_high_cape_woman.blend --python-exit-code 1 --python scripts/paso_doble/render_review.py -- solo_paso_doble_position_high_cape_woman 48
```

Run the full selected test set and the standard exporter prerequisites before activating clips. Compare actual binary sizes and `git check-attr` before staging regenerated assets. Files at or below 104,857,600 bytes belong in regular Git; larger files belong in Git LFS.

## Preservation and integration

This status record and every durable task asset belong to the preservation commit. The animation guidance addition is committed separately after rebasing onto current `origin/main`. Every new task or merge commit has exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer. Integration fetches current main, preserves concurrent work, and uses ordinary history-preserving pushes. Final commit and remote verification identifiers are reported in the chat delivery; the commit containing this status can be located with `git log --follow -- docs/animation_work_status/solo_paso_doble.md`.

### Rebase findings

The preservation commit was rebased onto `18e528c73` (`Bundle Game Rig Tools for cloud animation tasks`). Its post-rebase ID is `323da1561`. Upstream now includes `scripts/blender/install_animation_tools.py` and related setup documentation. Game Rig Tools was absent from the active profile during authoring; its source is available in the integrated repository for a future resume. The root size-based LFS policy supersedes this task's earlier exact-file attribute exceptions. `python scripts/lfs_policy.py check` passed for 23,427 staged files after rebase.

`solo_paso_doble/source_dependencies.json` records the original authoring dependency content hashes and the post-rebase checkout hashes. The original motion reports describe the original authoring environment; changed shared dependencies require renewed pose, skin, and bake validation before acceptance. The preserved per-animation binary payloads retain their recorded sizes and contents.

Post-rebase checks: the current fast suite passes **10/10** in 6.48 seconds (`solo_paso_doble/fast_tests_after_rebase.log`), and read-only structural inventory again passes **16/16** (`solo_paso_doble/asset_inventory_after_rebase.log`). The shared scene, disco seed, and two linked character assets retain their original content hashes; the combined library changed upstream. The original saved-bake and travelling-spins failures remain open.
