# Kizomba repertoire — preserved work status

Recorded 2026-10-02, 15:12 UTC (17:12 Europe/Berlin).
Chat/task title: Kizomba partner animations for man_and_woman3.blend.
Task branch: `codex/kizomba-repertoire`.
Pre-delivery HEAD: `3c52737c74b488501e9cfe47e7029547c6f5fe88`.
App checkout: `/workspace/sanjo-solutions/apps/a-game` in the sanjo-solutions cloud environment.

## Stop state and original scope

The user originally requested a broad organized Kizomba repertoire for both characters,
including positions and coordinated partner movements, reuse of fitting animation work,
Blender 5.2 throughout, planted contacts, natural motion, clearance, smooth transitions,
interpolated and loop validation, per-animation source files, documentation, and delivery to main.
The subsequent stop instruction prioritizes preserving the present state. Authoring and
rendering are stopped. These 72 source files are **partial procedural blocking studies**,
with final choreography quality and complete validation still pending. They represent
36 movement/position specifications in both lead roles, rather than exhaustive regional Kizomba.
**Authored sources: 72; baked actions: 0; runtime exports: 0.**

## Completed work and source provenance

- `scripts/create_kizomba.py`: reproducible paired IK builder, using the existing yoga
  standing poser, paired palm solver, activity channel writer, and AnimationFileWriter.
  All Blender operations used verified Blender 5.2.2 LTS, hash `d13f752e3b9c`.
- `scripts/validate_kizomba.py`: saved-action validator with half-frame and phase-boundary
  sampling, reach, planted translation/rotation, calibrated palm, mesh-floor and body-proxy
  checks, loop pose/velocity checks, transition endpoint checks, and optional review rendering.
- `scripts/kizomba.md`: repertoire, timing, source workflow, and explicit partial status.
- `animations/man_and_woman/kizomba_catalog.json`: all 72 specifications, roles, markers,
  stored ranges, and intended playback ends. Some saved loop bindings still differ from
  their intended catalog playback end, as listed in the inventory.
- `animations/man_and_woman/kizomba_validation.json`: passing report for eight clips only.
  All eight source SHA-256 values match the preserved files. Its `passed: true` applies
  solely to that selected scope. Transition comparison results are empty.
- `animations/man_and_woman/.gitattributes`: exact-filename ordinary-Git exceptions for
  these 72 sources. Shared scene and anatomical character sources retain their prior storage.
- `docs/animation_work_status/kizomba_repertoire/`: preserved logs, diagnostic/resume helpers,
  source audit, asset inventory, and 56 historical front/side PNG previews. Every supporting
  file is listed with size and SHA-256 in `evidence_inventory.json`. Previews precede the final
  refinements and provide historical evidence only. `contact_sheets.py` was prepared but never run.

The first full build saved 70 sources and rejected two man-lead promenade transitions for
palm reach (0.00676 m and 0.00583 m). The last already-running focused repair completed
all eight saves and exited before shutdown: promenade position, forward/back balance,
closed-to-promenade, and promenade-to-closed, each in both roles. It updated the catalog to72
and `build_failures.json` to an empty list. This authoring-time success is separate from
saved-file motion validation.

Finger rotation-mode correction and loop cropping were applied to the initial ten-clip
probe (closed, open, promenade, basic two side, quarter turn left, both roles), and the
latest eight repair sources use these corrections. Their union covers 16 sources.
The remaining 56 sources precede that refinement. The read-only audit finds **42 loops
with duplicate-endpoint playback still pending correction**. The checked-in builder is
therefore ahead of much of the saved batch. Rebuilding may produce different files.

## Timing and roles

All sources bind `Man.rigify` and `Woman.rigify` to one synchronized action at 24 fps.
Standard clips store frames 0–120 (96 BPM, 15 frames/beat); slow side stores 0–240.
Loop playback is intended to end at119 or239; directed turns and transitions include120.
Lead/follower roles, actual saved NLA ends, ranges, categories, byte counts, and hashes
for every source are in `asset_inventory.json` and the table below. Bodies use fixed roots
and world-space foot plants. No baked/deform action or runtime GLB was produced.

## Verification and limitations

Commands were run from the app checkout:

- `python tests/run_tests.py --suite fast`: **10/10 passed**, final stop-delivery run in
  `kizomba_repertoire/fast_tests.log` (6.42 seconds).
- `python -m py_compile scripts/create_kizomba.py scripts/validate_kizomba.py`: passed.
- `/workspace/tools/blender-5.2 -b --factory-startup --disable-autoexec --python-exit-code 1 --python docs/animation_work_status/kizomba_repertoire/audit_saved_sources.py`:
  passed;72 paired actions,8 matching passing report hashes,42 pending loop corrections.
  This audits saved metadata and provenance, rather than evaluating full motion.
- `/workspace/tools/blender-5.2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_kizomba.py -- --only position_closed position_open basic_two_side quarter_turn_left`:
  earlier completed8-clip motion check,259 samples per clip; `validate_probe.log`.
  Source hashes were checked again during stop delivery. The earlier ten-clip report was
  superseded; preserve its `validate.log` as historical evidence.
- `/workspace/tools/blender-5.2 -b animations/man_and_woman/kizomba_position_closed_man_lead.blend --disable-autoexec --python-exit-code 1 --python scripts/player_assets/animation_file_startup.py --python .cache/kizomba/source_smoke.py`:
  earlier passed source composition, two slots, both rig NLA bindings, and24fps;
  preserved `source_smoke.py` and `source_smoke.log`.
- `BLENDER=/workspace/tools/blender-5.2 python tests/run_tests.py --changed animations/man_and_woman/kizomba_position_closed_man_lead.blend --changed scripts/create_kizomba.py --changed scripts/validate_kizomba.py --slow-timeout 60`:
  **interrupted** by stop instruction;17 PASS entries (including10 fast),15 FAIL entries,
  then stopped during `test_paired_animation_loop_input.gd`. Resource loading/null nodes,
  editor API errors and60-second timeouts appear in `integration_tests_scoped.log`.
  Earlier integration/import attempts are retained as setup history, not completed checks.
- Actual engine: Godot4.6.3. Missing/unimported game fixtures and an unavailable
  `EditorInterface.get_resource_filesystem` call blocked related integration checks.
  Game Rig Tools is absent from Blender5.2, so bake/export prerequisites also remain.

Full72-clip interpolation, transitions, all role variants, complete loop continuity,
and final visual review remain outstanding. Proxy clearance does not establish full
mesh clearance or physical balance. No claim of production-ready dance quality is made.

## Processes and storage

Generator PID6016 had already completed its eight pending saves and exited when inspected.
Suite PID5327 received SIGTERM; the runner cleaned up its owned Godot process tree.
No owned Blender or test process remained after shutdown. No further authoring or rendering
was started after the stop instruction. Read-only audit and required fast checks then completed.
Godot import side effects in eight existing unrelated tracked resources were restored to HEAD.
Original saved output/cache logs remain under `.cache/kizomba`; durable copies are committed here.
The Blender installation remains `/workspace/tools/blender-5.2.2-linux-x64/blender`, with a
`/workspace/tools/blender-5.2` wrapper that supplies `-t 2`.

The72 source binaries total10,754,838 bytes; largest173,857 bytes. All56 preserved PNGs
are at most189,160 bytes. Actual `git check-attr filter` results for every binary are in
`storage_attributes.log`; all intended binaries have filter unset and are ordinary Git.
Exact preview exceptions live in the companion `.gitattributes`. These new assets require
ordinary Git transfer only; existing LFS assets retain their storage and are unchanged.

## Remaining work and exact resume commands

Resume authoring only after renewed user authorization. First review the source inventory,
repertoire suitability, and historical images. Then, from the app directory:

```sh
cd /workspace/sanjo-solutions/apps/a-game
/workspace/tools/blender-5.2 --version
# Apply the saved corrective helper across the existing72-source catalog.
/workspace/tools/blender-5.2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python docs/animation_work_status/kizomba_repertoire/refine_fingers.py
# Validate the complete saved batch; this replaces the eight-clip report.
/workspace/tools/blender-5.2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_kizomba.py
# Render current sources only after resolving numerical validation findings.
/workspace/tools/blender-5.2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_kizomba.py -- --render-only --render .cache/kizomba/review
# Optional diagnostic repair/rebuild; latest generator differs from older saved sources.
/workspace/tools/blender-5.2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/create_kizomba.py -- --only position_promenade balance_forward_back closed_to_promenade promenade_to_closed --role both
python tests/run_tests.py --suite fast
BLENDER=/workspace/tools/blender-5.2 python tests/run_tests.py --changed animations/man_and_woman/kizomba_position_closed_man_lead.blend --changed scripts/create_kizomba.py --changed scripts/validate_kizomba.py --slow-timeout 60
```

After any saved edit, rerun full validation and review both lead roles. Resolve Godot fixture
imports/editor test setup and install the project-supported Game Rig Tools before baking.
Use the existing Bake & Export Active Animation workflow if runtime exports are requested.
Record authored/baked/exported outputs separately. Integration hashes are reported in the
chat delivery; this snapshot records the pre-delivery commit to avoid self-referential hashes.

## Delivery integration update

The preservation commit rebased onto `de89cfea0` as `00759028d`.
The additive animation `.gitattributes` conflict was resolved by retaining all entries
from both histories. Concurrent main updates converted shared source storage; SHA-256
comparison confirms identical shared scene, Man, and Woman payloads against the original
validation baseline (`dependency_revision_audit.json`). All Kizomba source and evidence
hashes were rechecked after preservation. Raw historical logs retain their original
whitespace; code and documentation pass `git diff --check` with those logs excluded.

The fast suite after rebase passed **10/10** in6.26 seconds, recorded in
`fast_tests_after_rebase.log`. The repository storage policy check passed for24,591
indexed files. Concurrent main now bundles Game Rig Tools and an installer; the task's
Blender profile still needs setup before resuming. Run the following before opening
sources for renewed authoring, using the same profile for subsequent commands:

```sh
/workspace/tools/blender-5.2 --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
```

This delivery adds Kizomba provenance and shared-pair motion guidance to the app's
`# Animation` instructions, preserves prior documentation, and places `.gdignore` in
the historical evidence directory. No new animation generation, baking, export, or
rendering occurred during integration. Final merge/push hashes are reported in chat.

## Per-source inventory

Every source is authored-only, partial, with zero baked/exported output. Paths below are
relative to `animations/man_and_woman/`. `Pass` means the current eight-clip report matches;
`Pending` means full saved-motion validation remains. Saved NLA end lists both rig bindings.

| File | Lead / follower | Stored frames | Saved NLA ends | Motion report | Bytes |
| --- | --- | --- | --- | --- | ---: |
| `kizomba_balance_forward_back_man_lead.blend` | Man / Woman | 0–120 | [119.0, 119.0] | Pending | 143781 |
| `kizomba_balance_forward_back_woman_lead.blend` | Woman / Man | 0–120 | [119.0, 119.0] | Pending | 142449 |
| `kizomba_basic_one_weight_transfer_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 138855 |
| `kizomba_basic_one_weight_transfer_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 138919 |
| `kizomba_basic_three_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 145900 |
| `kizomba_basic_three_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 144208 |
| `kizomba_basic_two_side_man_lead.blend` | Man / Woman | 0–120 | [119, 119] | Pass | 145608 |
| `kizomba_basic_two_side_woman_lead.blend` | Woman / Man | 0–120 | [119, 119] | Pass | 143633 |
| `kizomba_box_step_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 147034 |
| `kizomba_box_step_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 146687 |
| `kizomba_closed_to_offset_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 147266 |
| `kizomba_closed_to_offset_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 146220 |
| `kizomba_closed_to_open_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 147148 |
| `kizomba_closed_to_open_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 146467 |
| `kizomba_closed_to_promenade_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 169698 |
| `kizomba_closed_to_promenade_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 169169 |
| `kizomba_diagonal_walk_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 148173 |
| `kizomba_diagonal_walk_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 147947 |
| `kizomba_ginga_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 137784 |
| `kizomba_ginga_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 139369 |
| `kizomba_half_turn_left_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 173633 |
| `kizomba_half_turn_left_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 173857 |
| `kizomba_half_turn_right_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 173403 |
| `kizomba_half_turn_right_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 173226 |
| `kizomba_lateral_left_and_return_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 144913 |
| `kizomba_lateral_left_and_return_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 144409 |
| `kizomba_lateral_right_and_return_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 146034 |
| `kizomba_lateral_right_and_return_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 144107 |
| `kizomba_marca_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 138671 |
| `kizomba_marca_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 139890 |
| `kizomba_offset_to_closed_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 147759 |
| `kizomba_offset_to_closed_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 145074 |
| `kizomba_open_to_closed_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 147807 |
| `kizomba_open_to_closed_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 146275 |
| `kizomba_pausa_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 137797 |
| `kizomba_pausa_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 138609 |
| `kizomba_position_closed_man_lead.blend` | Man / Woman | 0–120 | [119, 119] | Pass | 140339 |
| `kizomba_position_closed_woman_lead.blend` | Woman / Man | 0–120 | [119, 119] | Pass | 140416 |
| `kizomba_position_offset_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 139672 |
| `kizomba_position_offset_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 140617 |
| `kizomba_position_open_man_lead.blend` | Man / Woman | 0–120 | [119, 119] | Pass | 140783 |
| `kizomba_position_open_woman_lead.blend` | Woman / Man | 0–120 | [119, 119] | Pass | 138573 |
| `kizomba_position_promenade_man_lead.blend` | Man / Woman | 0–120 | [119.0, 119.0] | Pending | 141958 |
| `kizomba_position_promenade_woman_lead.blend` | Woman / Man | 0–120 | [119.0, 119.0] | Pending | 142017 |
| `kizomba_promenade_to_closed_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 170133 |
| `kizomba_promenade_to_closed_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 169445 |
| `kizomba_quarter_turn_left_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pass | 168540 |
| `kizomba_quarter_turn_left_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pass | 168115 |
| `kizomba_quarter_turn_right_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 169214 |
| `kizomba_quarter_turn_right_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 169680 |
| `kizomba_retrocesso_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 145286 |
| `kizomba_retrocesso_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 144217 |
| `kizomba_saida_follower_left_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 151295 |
| `kizomba_saida_follower_left_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 147779 |
| `kizomba_saida_follower_right_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 150321 |
| `kizomba_saida_follower_right_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 149747 |
| `kizomba_saida_leader_left_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 149685 |
| `kizomba_saida_leader_left_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 148894 |
| `kizomba_saida_leader_right_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 150392 |
| `kizomba_saida_leader_right_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 149057 |
| `kizomba_slow_side_man_lead.blend` | Man / Woman | 0–240 | [240.0, 240.0] | Pending | 145212 |
| `kizomba_slow_side_woman_lead.blend` | Woman / Man | 0–240 | [240.0, 240.0] | Pending | 144054 |
| `kizomba_syncopated_side_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 144629 |
| `kizomba_syncopated_side_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 143408 |
| `kizomba_tarraxinha_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 139376 |
| `kizomba_tarraxinha_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 137382 |
| `kizomba_virgula_redirect_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 171204 |
| `kizomba_virgula_redirect_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 170716 |
| `kizomba_walk_backward_and_return_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 145380 |
| `kizomba_walk_backward_and_return_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 145081 |
| `kizomba_walk_forward_and_return_man_lead.blend` | Man / Woman | 0–120 | [120.0, 120.0] | Pending | 146407 |
| `kizomba_walk_forward_and_return_woman_lead.blend` | Woman / Man | 0–120 | [120.0, 120.0] | Pending | 144035 |
