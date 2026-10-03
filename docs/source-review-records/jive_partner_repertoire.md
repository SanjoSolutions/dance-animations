# Jive partner repertoire — stopped work record

- Recorded: 2026-10-02 UTC; saved-state inventory at 15:07:33 UTC.
- Chat/task title: Jive partner repertoire for man_and_woman3.blend (descriptive task title; desktop title unavailable).
- Project/environment: A-Game, sanjo-solutions cloud environment, `/workspace/sanjo-solutions/apps/a-game`.
- Task branch at stop: `codex/jive-partner-repertoire`.
- Current commit at stop: `3c52737c74b488501e9cfe47e7029547c6f5fe88`; the task changes were then uncommitted.
- Stop instruction: delegated from chat `01a0fd1a-3673-7683-ae29-577f2ee1a927`. Preserve present state, stop animation work, commit and deliver through main.
- State: **52 authored partial procedural blocking studies; 0 baked; 0 exported.** These are development assets, not an accepted complete Jive repertoire.

## Original scope and stopping point

The original request covered coordinated Man/Woman Jive positions and moves in `man_and_woman3.blend`, broad organized coverage, natural motion, planted feet, contact and body clearance, smooth transitions, interpolated and loop validation, and reuse where appropriate. Blender 5.2 was required for every Blender operation, with per-animation files, Git size inspection, task commits, rebase onto origin/main, Animation guidance, and main delivery.

Preparation finished: read repository and app guidance and paired authoring/motion-review workflows; inspected rigs and existing animation tools; retrieved app LFS dependencies; installed and checksum-verified Blender **5.2.2 LTS, d13f752e3b9c** at `/workspace/tools/blender-5.2.2-linux-x64/blender`. The system Blender is 4.3.2 and belongs outside this task's commands. Existing solo disco motion had different rhythm and partner contacts; this task reused authoring infrastructure rather than copying its movement. Godot verification used 4.6.3.

The intended generator repertoire has 56 clips: 10 positions, 18 directed position transitions, and 28 figures. Present files cover 10 positions, all 18 transition names, and 24 figure names. Four figures have no saved source: `double_cross_whip`, `spanish_arms`, `rolling_off_the_arm`, and `windmill`. Generation errors also left older `promenade_walks_slow` and `promenade_walks_quick` files in place. Saved sources span multiple generator revisions.

The stop arrived during verification and the tail of partitioned authoring. By process inspection, authoring had finished: the transition job saved all 18 clips; repair saved `basic_in_place`, `chasse_right`, and `change_of_hands_behind_back`, then failed `double_cross_whip`. Those three repaired sources have no current-hash motion validation. Further authoring, pose refinement, generation, rendering, baking, and export were stopped. Only preservation, read-only structure checks, and the fast suite continued.

## Completed work and asset organization

- `scripts/create_jive.py`: partial choreography generator using `RigYogaPoser`, `PairedAnimationAuthoring`, calibrated palm targets, sparse step/launch/apex/landing keys, action/NLA binding metadata, and `AnimationFileWriter`. World foot targets, support timing, knee pulse, partner spacing, grip release, and turn paths were iterated. Latest palm and right-chasse changes remain incompletely validated.
- `scripts/validate_jive.py`: saved-source/subframe checks for slots, timing, finite keys, IK reach, planted ankles, palms, support, floor, torso proxies, sampled body surface intersections, loop pose/velocity, and transition joins; existing native contact-sheet rendering support. The latest joint-speed check has yet to run across the preserved library.
- `scripts/jive.md`: intended design, usage, and rebuild notes, now explicitly labeled partial and stopped.
- `animations/man_and_woman/jive_*.blend`: 52 separate editable sources; existing shared source references retained. Both control rigs participate in synchronized layered actions: `Man.rigify` leads, `Woman.rigify` follows. Native wrist constraints remain active. All clips use 24 fps and 120 BPM. Stored final loop poses duplicate the start; playback ends one frame earlier. Directed transitions play once.
- `animations/man_and_woman/jive_catalog.json`: preserved incomplete 12-entry generation receipt. It is not a complete inventory. Partition receipts in this record's `catalogs/` directory contain additional plant/phase data, with older receipts retained as evidence.
- `animations/man_and_woman/jive_validation.json`: historical failed 33-clip report; **zero hashes match current sources**.
- `animations/man_and_woman/jive_validation_subset.json`: passing 10-position report; **all 10 hashes match current sources**.
- `animations/man_and_woman/.gitattributes`: exact filename exceptions for the 52 small Jive sources, preserving existing exceptions and shared-asset LFS settings.
- This record's `previews/`: 41 pre-existing Blender-rendered images, including 14 contact sheets and 27 earlier individual frames. These capture historical revisions; `basic_in_place` images predate the final repair. They provide evidence, not blanket visual approval.
- This record's `catalogs/`, `logs/`, and `diagnostics/`: generation receipts, prior validation reports, raw logs, and historical diagnostic/source snapshots. Diagnostic `.py.txt` files are evidence, not active tooling. No credential helper is included.
- `saved_source_structure.json`: read-only Blender reload results for all 52 actions, including exact frame ranges, slots, bindings, key counts, markers, binary size and SHA-256.
- `preservation_manifest.json`: exact source inventory and validation reports whose SHA-256 matches each current asset.
- `artifact_inventory.json`: size and SHA-256 inventory of the other task artifacts and evidence (excluding itself and this narrative record).
- `related_suite_outcomes.json`: each attempted broad-suite check and its outcome.
- `verify_preserved_sources.py`: read-only action-structure verifier; it loads actions and writes a report, with no posing, rendering, baking, or source saves.

This task made no edits to the shared scene, combined character library, anatomical source files, or runtime assets. Concurrent main updates are retained during integration. Godot import/test UID rewrites in four existing resources were inspected and restored. No Jive runtime bake/export outputs were created.

## Saved sources, frames, roles, and validation

Every row is authored-only, with Man as leader and Woman as follower. “Motion pass” means the existing report matches the preserved file hash; it is bounded by that report's sampling and tolerances. “Pending” means structure passes while current motion acceptance remains pending. None of these rows constitutes a final natural-motion review.

| Source (`animations/man_and_woman/`) | Category | Stored frames | Playback | Current-hash motion evidence |
| --- | --- | --- | --- | --- |
| `jive_american_spin.blend` | Figure | 0–144 | 0–144 once | Pending |
| `jive_apart_to_open.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_basic_in_place.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_change_of_hands_behind_back.blend` | Figure | 0–144 | 0–144 once | Pending |
| `jive_change_of_places_left_to_right.blend` | Figure | 0–144 | 0–144 once | Pending |
| `jive_change_of_places_right_to_left.blend` | Figure | 0–144 | 0–144 once | Pending |
| `jive_chasse_left.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_chasse_right.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_chicken_walks.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_closed_to_open.blend` | Transition | 0–144 | 0–144 once | Motion pass |
| `jive_compact_basic.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_counter_promenade_to_open.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_double_hand_to_open.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_fallaway_basic.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_flick_cross.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_flicks_into_break.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_handshake_to_open.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_kick_ball_change.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_link.blend` | Figure | 0–72 | 0–72 once | Motion pass |
| `jive_mooch.blend` | Figure | 0–288 | 0–287 loop | Pending |
| `jive_open_to_apart.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_open_to_closed.blend` | Transition | 0–144 | 0–144 once | Motion pass |
| `jive_open_to_counter_promenade.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_open_to_double_hand.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_open_to_handshake.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_open_to_promenade.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_open_to_shadow.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_open_to_side_by_side.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_open_to_tandem.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_position_apart.blend` | Position | 0–72 | 0–71 loop | Motion pass |
| `jive_position_closed.blend` | Position | 0–72 | 0–71 loop | Motion pass |
| `jive_position_counter_promenade.blend` | Position | 0–72 | 0–71 loop | Motion pass |
| `jive_position_double_hand.blend` | Position | 0–72 | 0–71 loop | Motion pass |
| `jive_position_handshake.blend` | Position | 0–72 | 0–71 loop | Motion pass |
| `jive_position_open.blend` | Position | 0–72 | 0–71 loop | Motion pass |
| `jive_position_promenade.blend` | Position | 0–72 | 0–71 loop | Motion pass |
| `jive_position_shadow.blend` | Position | 0–72 | 0–71 loop | Motion pass |
| `jive_position_side_by_side.blend` | Position | 0–72 | 0–71 loop | Motion pass |
| `jive_position_tandem.blend` | Position | 0–72 | 0–71 loop | Motion pass |
| `jive_promenade_to_open.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_promenade_walks_quick.blend` | Figure | 0–144 | 0–143 loop | Pending; older generation |
| `jive_promenade_walks_slow.blend` | Figure | 0–144 | 0–143 loop | Pending; older generation |
| `jive_rock_recover.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_shadow_to_open.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_side_breaks.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_side_by_side_to_open.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_simple_spin.blend` | Figure | 0–144 | 0–144 once | Pending |
| `jive_stop_and_go.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_sugar_push.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_tandem_to_open.blend` | Transition | 0–144 | 0–144 once | Pending |
| `jive_toe_heel_swivels.blend` | Figure | 0–144 | 0–143 loop | Pending |
| `jive_whip.blend` | Figure | 0–144 | 0–144 once | Pending |

## Validation commands and results

All commands below ran from `apps/a-game` unless stated otherwise. Full evidence is preserved beside this record.

1. `python tests/run_tests.py --suite fast` after stopping processes: **10/10 passed in 6.23 seconds**, `logs/jive_stop_fast.log`. Python AST parsing passed for both new author/validator scripts and the preservation verifier (`logs/source_syntax.txt`).
2. Read-only structural verification: **52/52 saved actions passed** with Blender 5.2.2. Checked loadability, both named action slots, two NLA binding descriptors, participant metadata, timing, and finite keys. Command:

   ```sh
   /workspace/tools/blender-5.2.2-linux-x64/blender -t 2 --background --factory-startup \
     --disable-autoexec --python-exit-code 1 \
     --python docs/animation_work_status/jive_partner_repertoire/verify_preserved_sources.py
   ```

3. Before the stop, `scripts/validate_jive.py -- --only position_open position_closed position_double_hand position_handshake position_promenade position_counter_promenade position_side_by_side position_shadow position_tandem position_apart --render .cache/jive/review`, using the explicit Blender executable and shared-scene command below: **10 positions passed**, and hashes remain current. See `logs/jive_positions_final_validate.log` and the subset report. All ten have zero sampled body surface overlap pairs and zero loop pose error. Maximum planted/IK error is approximately 0.000235 m; minimum sampled mesh floor is approximately +0.00337 m. The closed, promenade, side-by-side, shadow, and earlier open arrangements were visually inspected. Other renders remain evidence for further review.
4. Before the stop, validator with `--catalog /tmp/jive_transitions_catalog.json --only open_to_closed closed_to_open`: **2 passed and hashes remain current** (`catalogs/jive_transitions_catalog_validation.json`, `logs/jive_transition_final_validate.log`). Endpoint deviations were approximately 0.000001 m; sampled surface overlaps zero.
5. Before the stop, validator with `--catalog /tmp/jive_figures_a_catalog.json --only basic_in_place link`: **link passed with current hash**; earlier basic failed palm gap at 0.529371 m. Basic was subsequently overwritten by the repair job and requires another motion check. See `catalogs/jive_figures_a_catalog_validation.json` and `logs/jive_basic_final_validate.log`.
6. Broader command, interrupted on the stop instruction:

   ```sh
   PATH=/workspace/tools/blender-5.2.2-linux-x64:$PATH \
   BLENDER=/workspace/tools/blender-5.2.2-linux-x64/blender \
   python tests/run_tests.py --slow-timeout 120 \
     --changed scripts/create_jive.py --changed scripts/validate_jive.py \
     --changed animations/man_and_woman/jive_basic_in_place.blend
   ```

   **19 checks passed, 24 failed, 1 was interrupted; remaining selected checks were not reached.** This includes 9 fast passes and one intermittent descendant-resource cleanup test failure; the fresh fast run passed all ten. Godot errors included unsupported `PopupMenu.search_bar_enabled`, missing runtime nodes/bindings, renderer restrictions, resource/RID leaks, one native failure, and eight 120-second timeouts. Blender export/cache tests raised `StopIteration` looking for the `game_rig_tools` add-on. These failures are recorded rather than attributed to a proven clean baseline. Existing app LFS objects were fetched and generated import caches refreshed during diagnosis. The stop precluded further environment or export work. Full output: `logs/jive_related_tests.log`.
7. Storage audit before staging: 52 Blender binaries total **7,864,953 bytes**, individual sizes **121,592–202,592 bytes**. All 41 preserved PNGs also fit the 104,857,600-byte threshold. `git check-attr filter diff merge text -- <each exact binary path>` reports every attribute unset for all 93 new binary files; see `logs/storage_attributes.txt`. All new binaries use ordinary Git; this task adds zero LFS objects needing separate upload.

Motion checks use half frames plus phase keys and quarter-frame loop derivatives; tolerances are IK/plant 0.005 m, palms 0.025 m, floor penetration 0.012 m, torso gap 0.015 m, loop pose 0.0002 m, and loop velocity 0.015 m/frame. Mesh floor and body overlap are sampled sparsely at 12-frame spacing; hand/shoulder contact neighborhoods are excluded from surface overlap checks. These checks do not establish full collision freedom, balance, finger fit, or professional Jive accuracy.

## Processes and preserved outputs

At shutdown, authoring PIDs 7264 (transitions) and 7736 (repair), and both figure partition jobs, had exited. The repair log ends with `double_cross_whip` reach failure and Blender exit. Test runner PID 6472 and its current Blender export-test child PID 7924 received SIGTERM; the runner recorded `KeyboardInterrupt`. Subsequent process inspection found no active owned Blender, Godot, or suite processes. Read-only verification and the fresh fast run then completed normally.

Saved Blender files were retained exactly as found. Existing `.cache/jive/review` renders and `/tmp/jive*` logs/catalogs were copied into this task's evidence directory. Temporary credentials, downloaded Blender archives, generated Godot caches, and unrelated LFS source downloads are environment preparation rather than new task assets. Asset hashes in the manifest make mixed revisions explicit.

## Remaining work and concrete blockers

- User stop instruction is the active constraint; animation work requires a later instruction to resume.
- Four intended source files remain absent. Latest generation failures: `double_cross_whip` frame 33 partner left palm error 0.00644 m (repair attempt); `spanish_arms` frame 21 player left palm 0.09085 m; `rolling_off_the_arm` frame 18 partner right palm 0.06920 m; `windmill` frame 39 partner left palm 0.05473 m.
- Latest promenade builds failed reach: slow frame 21 partner right palm 0.01777 m; quick frame 9 partner right palm 0.01538 m. Older saved versions are preserved and require deliberate regeneration/review.
- Basic/right-chasse/behind-back repair outputs require validation. Kick closing changes in the current source are newer than several saved kick studies. The damped contact solver and handhold changes have not been verified across all figures.
- Consolidate generation receipts only after rebuilding or deliberately reconciling revisions; a filename alone proves neither matching plant metadata nor validation freshness. The current 12-entry catalog cannot drive validation of all saved files.
- Finish natural motion, exact dance semantics, wrist/finger fit, whole-body clearance, support/balance, heading transitions, and every loop/transition review. Thirteen current files have passing sampled motion reports; 39 have pending current-hash motion acceptance.
- No baked/exported clips exist. Blender `game_rig_tools` setup and Godot runtime compatibility need resolution before the broad export/runtime suite can pass. Continue authored-source work only after the user resumes it; runtime delivery needs its established bake/export workflow.

## Exact resume commands

These are future commands, **not actions authorized by the stop instruction**. Use a new task branch from current main, inspect this record and the manifest first, and resolve the listed choreography/reach issues before a complete rebuild. `--resume` alone would keep stale entries; a coherent full rebuild is required after shared movement changes.

```sh
cd /workspace/sanjo-solutions
 git fetch origin
 git switch -c codex/resume_jive origin/main
cd apps/a-game
export BLENDER=/workspace/tools/blender-5.2.2-linux-x64/blender
"$BLENDER" --version
# Current main supplies the bundled add-on setup for future authoring/export:
"$BLENDER" --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
# Confirm 5.2.x and retrieve linked source libraries in a fresh checkout:
git lfs pull --include='apps/a-game/**'
# Read-only saved-state check:
"$BLENDER" -t 2 --background --factory-startup --disable-autoexec --python-exit-code 1 \
  --python docs/animation_work_status/jive_partner_repertoire/verify_preserved_sources.py
# After a future resume instruction and fixes, rebuild coherent source/catalog state:
"$BLENDER" -t 2 --background animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/create_jive.py
# This currently reaches the documented failures; inspect logs and fix, rather than assuming success.
"$BLENDER" -t 2 --background animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/validate_jive.py \
  -- --render .cache/jive/review
python tests/run_tests.py --suite fast
PATH="$(dirname "$BLENDER"):$PATH" python tests/run_tests.py --blender "$BLENDER" \
  --slow-timeout 120 --changed scripts/create_jive.py --changed scripts/validate_jive.py \
  --changed animations/man_and_woman/jive_basic_in_place.blend
```

Use authenticated Git configured by the environment for fetch/push/LFS; keep tokens out of files and logs. Before staging any regenerated or new source, inspect actual size and exact attributes; scope ordinary-Git exceptions to files at or below 104,857,600 bytes. Record authored, baked, and exported states separately. Preservation and documentation commits carry exactly one Codex co-author trailer. Main integration uses a fresh fetch and ordinary history-preserving push; final delivery hashes are reported by the chat after remote verification.

## Integration verification

The preservation commit rebased onto `629cffdc1` from origin/main. The single conflict was the per-animation `.gitattributes` append; both existing remote exceptions and all 52 Jive exceptions were retained. The updated repository-wide `python scripts/lfs_policy.py check` passed for 24,540 staged files. The fresh post-rebase fast suite passed **10/10 in 6.43 seconds** (`logs/jive_integration_fast.log`).

Main's shared scene and both anatomical source payloads have the same SHA-256 as the stop-time inputs; their Git storage changed upstream. Main's combined `man_and_woman3.blend` has concurrent content changes, which are retained. Shared authoring helpers also changed upstream; any future regeneration should use a fresh validation run. Existing motion reports document the recorded source revisions and stop-time tooling rather than a rerun after integration.

The follow-up documentation commit adds the Jive checkpoint, partial-catalog warning, six-count timing, and support/loop-review guidance to the app's `# Animation` section. All animation sources remain unchanged after the stop. Final integration will fetch origin/main immediately before merging and use an ordinary push, with remote commit equality and task ancestry verified in the final delivery report.

Final merge preparation used freshly fetched origin/main `f76f8f5bc`. Its concurrent attributes entries and Animation guidance were preserved. The merged tree passed the fast suite **10/10 in 6.11 seconds** (`logs/jive_final_fast.log`) and the repository LFS policy check. No animation authoring or rendering resumed during integration.

The first ordinary push was rejected because remote main advanced. The retry fetched `2d0db14bd` and retained both sides of append conflicts in AGENTS.md and per-animation attributes. Fast checks passed **10/10 in 6.13 seconds** (`logs/jive_retry_fast.log`); LFS policy passed for 30,373 staged files before adding this log. The Jive diff against the fetched main passes `git diff --cached --check origin/main`. Existing whitespace in other tasks’ raw evidence logs is preserved.
