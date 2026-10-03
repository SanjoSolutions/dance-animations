# Flamenco solo animation work status

Recorded October 2, 2026, after the stop instruction at approximately 16:56 Europe/Berlin (14:56 UTC).

- Chat/task title: **Flamenco solo repertoire for man_and_woman3.blend** (working title; desktop title unavailable).
- Environment/project: sanjo-solutions cloud environment, A-Game, `/workspace/sanjo-solutions/apps/a-game`.
- Task branch: `codex/flamenco-solo-repertoire`.
- Commit at the stopping point: `fe09ef7b6a54f03909f7335d9673a27c15007d69`. The checkpoint commit adds this record and the files listed below; integration hashes are reported in the chat delivery.
- Author of this checkpoint and GitHub delivery: **Codex**.
- State: **paused by explicit user instruction; partial procedural blocking studies**. The original animation request remains incomplete. Further authoring, refinement, generation, and rendering require a subsequent instruction to resume.

**Final acceptance finding:** all 20 preserved GLBs contain constant channels. The ten moving studies fail exported-motion acceptance. The ten static poses also need an independent pose-match check. The generated bake-comparison reports are insufficient evidence: stale evaluated deform matrices can agree with a stale reference. The sources remain editable studies; **all bakes/exports are provisional and quarantined**. No runtime-ready Flamenco clip is claimed.

## Original scope and current coverage

The request was to build a broad, organized Flamenco repertoire for both characters in `man_and_woman3.blend`, use Blender 5.2 for all Blender work, reuse fitting motion, follow sparse IK/per-animation authoring, validate interpolated contacts, body clearance and loops, export, commit, rebase onto current main, document useful findings in AGENTS.md, then merge and push with required asset uploads. Files through 104,857,600 bytes belong directly in Git.

The procedural catalog defines 47 entries per character (94 intended clips): ten positions, three braceo sequences, two floreo sequences, two palmas, ten isolated footwork entries, three footwork phrases, five marking steps, four turns, and eight compas practice motifs. These are a practice vocabulary rather than an exhaustive claim about all Flamenco schools/palos. Full musical choreography and accessory work are outside the authored checkpoint.

**20 man-only source/bake/export triplets exist. Zero woman clips exist.** All 20 have the `PLAYER` participant role and only the `Man.rigify` authoring slot plus `Man.rigify_deform` baked slot. Each `.blend` contains its named authoring action and matching `.baked` action. Godot exports contain a single animation. They were initially published during authoring. At integration, newly fetched repository guidance required quarantine of stopped studies: the 20 GLBs and their import settings now reside unchanged in `docs/animation_work_status/flamenco_solo/exports/`, beneath `.gdignore`, and their 20 Flamenco references were removed from `models/player/animation_updates.tres` while preserving all other entries. The combined `man_and_woman3.blend` and shared scene were retained as existing inputs.

The action data is editable and the GLBs are structurally readable. Treat the assets as **procedural blocking studies**, not finished motion-capture-quality or production-approved Flamenco. Two final clay render snapshots were reviewed (recogida frame 0 and claras frame 12). Full playback and surface review remain outstanding.

## Durable implementation and evidence

- `scripts/flamenco/catalog.py`: 47 choreography definitions, named keys, contact/strike/recovery timing and categories. Several planned footwork variants still share overly similar trajectories; technique differentiation remains outstanding.
- `scripts/flamenco/build.py`: Blender 5.2 guard, reused `DiscoCharacter`/`RigYogaPoser` neutral pose and proportion/wrist helpers, restrained finger/wrist animation, calibrated palmas through the paired IK solver, sparse curves, native evaluated visual baking, `AnimationFileWriter`, `AnimationClipScene`, and `AnimationUpdates` publishing. Game Rig Tools is absent in this environment, so this checkpoint used a native visual-bake implementation. It has 18 recorded per-frame comparisons; this is a task-specific fallback, not a replacement for the repository's normal Action Bakery workflow.
- `scripts/flamenco/preview.py`: Blender 5.2 Cycles CPU clay preview helper. Workbench initially encountered EGL_BAD_MATCH; Cycles rendered successfully. Preview files are saved separately, retaining the authoring sources.
- `scripts/flamenco/inspect_saved.py`: read-only Blender audit of all saved source action pairs, slots, roles, ranges, GLB counts/durations, publication references and SHA-256 digests.
- `scripts/flamenco/reports/<clip>.json`: one half-frame motion report per saved clip. Reports reflect the respective generation pass and differ in clearance/bake coverage, as detailed below.
- `docs/animation_work_status/flamenco_solo/saved_asset_audit.json`: exact source/export paths, binary sizes and digests, action slots/ranges, export channels, loop-settings/marker presence and embedded motion reports for every asset.
- `docs/animation_work_status/flamenco_solo/storage_audit.json`: exact paths and actual sizes for all 42 new binaries (20 BLEND, 20 GLB, two PNG). Largest binary: 396,153 bytes. All belong directly in Git.
- `apps/a-game/.gitattributes`: exact-file exceptions for those 42 binaries, using `-filter -diff -merge -text`; repository-wide LFS patterns remain in effect for other files.
- `docs/animation_work_status/flamenco_solo/flamenco_man_position_recogida_0.png` and `flamenco_man_palmas_claras_12.png`: saved full-body clay review snapshots.
- Evidence logs in the same directory: `build.log`, `build_man.log`, `build_all.log`, `palmas.log`, `turn.log`, `footwork.log`, `palmas_probe.log`, `palmas_search.log`, `preview_cycles.log`, `palmas_render.log`, `fast_tests.log`, `saved_asset_audit.log`, `animation_files_test.log`, `single_animation_export_test.log`, and `selected_tests.txt`. Earlier logs include deliberately retained failed intermediate checks; current saved-asset audit identifies the final files.

## Saved asset inventory

All ranges are inclusive at 24 fps. The final pose supplies a loop endpoint. Each source path is relative to `apps/a-game`; each GLB has an adjacent `.glb.import` file. Each clip also has a matching `scripts/flamenco/reports/<clip>.json`.

| Clip | Frames | Source | Export | Explicit Godot loop / exported markers | Recorded visual-bake comparison |
| --- | --- | --- | --- | --- | --- |
| `flamenco_man_braceo_alternating` | 0–96 | `animations/man_and_woman/flamenco_man_braceo_alternating.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_braceo_alternating_baked_bb75bf6acfda.glb` | yes / yes | yes |
| `flamenco_man_braceo_ascend_descend` | 0–96 | `animations/man_and_woman/flamenco_man_braceo_ascend_descend.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_braceo_ascend_descend_baked_5a66aff1b007.glb` | yes / yes | yes |
| `flamenco_man_floreo_inward` | 0–48 | `animations/man_and_woman/flamenco_man_floreo_inward.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_floreo_inward_baked_6bd32a7d021a.glb` | yes / yes | yes |
| `flamenco_man_floreo_outward` | 0–48 | `animations/man_and_woman/flamenco_man_floreo_outward.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_floreo_outward_baked_e37a9942096e.glb` | yes / yes | yes |
| `flamenco_man_golpe_left` | 0–48 | `animations/man_and_woman/flamenco_man_golpe_left.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_golpe_left_baked_a65c9a67888d.glb` | pending / pending | pending |
| `flamenco_man_golpe_right` | 0–48 | `animations/man_and_woman/flamenco_man_golpe_right.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_golpe_right_baked_557712572275.glb` | pending / pending | pending |
| `flamenco_man_palmas_claras` | 0–48 | `animations/man_and_woman/flamenco_man_palmas_claras.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_palmas_claras_baked_ecc0036d3c2e.glb` | yes / yes | yes |
| `flamenco_man_palmas_sordas` | 0–48 | `animations/man_and_woman/flamenco_man_palmas_sordas.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_palmas_sordas_baked_99e1d2793dd4.glb` | yes / yes | yes |
| `flamenco_man_port_de_bras` | 0–96 | `animations/man_and_woman/flamenco_man_port_de_bras.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_port_de_bras_baked_17aa96a07a2c.glb` | yes / yes | yes |
| `flamenco_man_position_desplante_left` | 0–48 | `animations/man_and_woman/flamenco_man_position_desplante_left.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_position_desplante_left_baked_e24f31ebe89f.glb` | yes / yes | yes |
| `flamenco_man_position_desplante_right` | 0–48 | `animations/man_and_woman/flamenco_man_position_desplante_right.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_position_desplante_right_baked_895681ff1188.glb` | yes / yes | yes |
| `flamenco_man_position_preparacion` | 0–48 | `animations/man_and_woman/flamenco_man_position_preparacion.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_position_preparacion_baked_c95004a7fd7a.glb` | yes / yes | yes |
| `flamenco_man_position_quiebro_left` | 0–48 | `animations/man_and_woman/flamenco_man_position_quiebro_left.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_position_quiebro_left_baked_735f42c9f4fa.glb` | yes / yes | yes |
| `flamenco_man_position_quiebro_right` | 0–48 | `animations/man_and_woman/flamenco_man_position_quiebro_right.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_position_quiebro_right_baked_377557032f36.glb` | yes / yes | yes |
| `flamenco_man_position_quinta` | 0–48 | `animations/man_and_woman/flamenco_man_position_quinta.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_position_quinta_baked_410b96878504.glb` | yes / yes | yes |
| `flamenco_man_position_recogida` | 0–48 | `animations/man_and_woman/flamenco_man_position_recogida.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_position_recogida_baked_c2c52005a5bc.glb` | yes / yes | yes |
| `flamenco_man_position_segunda` | 0–48 | `animations/man_and_woman/flamenco_man_position_segunda.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_position_segunda_baked_54e20321ab94.glb` | yes / yes | yes |
| `flamenco_man_position_tercera_left` | 0–48 | `animations/man_and_woman/flamenco_man_position_tercera_left.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_position_tercera_left_baked_5a7fc8add91e.glb` | yes / yes | yes |
| `flamenco_man_position_tercera_right` | 0–48 | `animations/man_and_woman/flamenco_man_position_tercera_right.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_position_tercera_right_baked_09a268a74e17.glb` | yes / yes | yes |
| `flamenco_man_vuelta_paseo_left` | 0–204 | `animations/man_and_woman/flamenco_man_vuelta_paseo_left.blend` | `docs/animation_work_status/flamenco_solo/exports/flamenco_man_vuelta_paseo_left_baked_3daca96bfa3b.glb` | pending / pending | yes |

## Validation results and limits

1. `python tests/run_tests.py --suite fast`: **9/9 passed**, final checkpoint run 5.01 seconds. The first run was 8/9 because three hair `.res` inputs were LFS pointers. Downloading `playground/hair/physics/{ponytail01,braid01,long01}_mesh.res` resolved that prerequisite. These existing resources were hydrated locally, not changed in Git. Godot version: 4.6.3.
2. `blender -b --factory-startup --python-exit-code 1 --python scripts/flamenco/inspect_saved.py`: **STRUCTURE PASS; final MOTION FAIL (exit 1)**, 20 readable source/baked pairs, expected solo slots/roles, one GLB clip each, matching durations, publication/preservation state, and recorded passing motion reports. The later expanded audit additionally checks actual channel variation and exits with failure for ten moving exports; structural success alone is insufficient. This audit checks structure and recorded results; it does not rerun the entire procedural authoring pipeline.
3. `blender -b --factory-startup --python-exit-code 1 --python scripts/player_assets/test_animation_files.py`: **PASS**, one source isolation/composition test, 2.965 seconds. Temporary test fixtures were used; task animation files were retained.
4. `blender -b --factory-startup --python-exit-code 1 --python scripts/player_assets/test_single_animation_export.py`: **PASS**, existing compact-export fixture scenarios including shapes/drivers/NLA. This verifies shared export machinery, not a full Godot playback review of these studies.
5. The generation passes sampled each saved clip every half frame, measuring foot landmarks, ankle holds, IK endpoints, wrist bend, loop position/orientation and finite-difference loop velocity. All saved per-clip reports say `passed`. Flat static positions have identical endpoints. The two golpe exports predate the visual-bake comparison and explicit loop/marker publication; the full vuelta export predates explicit loop/marker publication.
6. The latest completed full-generation pass includes the stronger sampled arm-segment/torso-cylinder clearance check for the ten positions and two braceo sequences. The separately corrected palmas pass also used that check. Older floreo, port-de-bras, golpe and vuelta reports used the earlier wrist-only torso proxy. The existing JSON field `minimum_wrist_torso_proxy_gap` retains its historical name even in the stronger pass. A null gap means that the chosen height-band proxy had zero coverage, not proof of whole-body clearance.
7. The first rendered clap exposed arm/torso overlap despite passing wrist checks. The saved clap was corrected to wider, lower elbow poles. The corrected frame-12 render shows separated arms. Finger/skin intersections, full-mesh collision checks, angular loop velocity, and full motion playback remain outstanding. The native bake comparison covers integer samples; authored contact checks cover half frames.
8. Broad test selection for the source/registry paths selects **9 fast + 186 slow** checks (`selected_tests.txt`). That entire suite was not executed: it spans unrelated existing character assets, specialized manual prerequisites, GPU checks, the full combined library/cache, and Game Rig Tools. The targeted source/export fixtures and task audit above were executed. This checkpoint does not claim full-suite or Godot runtime/import acceptance.

## Stopping point, processes and blockers

The full builder process (PID 1916) was terminated with SIGTERM in response to the user instruction. Its final log reaches `AUTHOR flamenco_man_port_de_bras`; its new in-memory port-de-bras iteration was not saved. The earlier readable saved port-de-bras source/bake/export remains preserved. The read-only audit confirms all 20 source/export pairs are complete binary files. All owned Blender authoring/rendering processes are stopped; subsequent verification processes completed.

The latest pass refreshed ten positions plus two braceo sequences; other saved files retain their respective earlier passes. No woman generation began. The catalog's remaining entries are procedural definitions only, not authored/baked/exported files.

Concrete remaining work:

- Obtain a fresh instruction to resume animation work.
- Review and distinguish planta, tacon, punta and heel/toe technique trajectories; their current procedural definitions are preliminary and too similar. Verify moving-foot sole/toe/heel contacts against evaluated mesh geometry, not only ankle/landmark proxies.
- Finish/refine the other 27 man clips and all 47 woman clips, checking each character's reach and proportions separately.
- Rerun stronger clearance and native bake comparisons for older studies. Restore explicit loop settings and exported markers for both golpe clips and the saved vuelta only through an authorized resume/export pass.
- Inspect playback, all limbs, head spotting, fingers, surface contacts and loop angular velocities, and test smooth transitions across separate clips. Individual matching loop seams alone do not establish cross-clip transitions.
- Validate the published GLBs through Godot import/playback against the composed model. Current imports have only structural audit coverage.
- Restore the usual Game Rig Tools export environment when available, or review the fallback against native Action Bakery before broader use. The combined library and many unrelated assets remain LFS pointers in this checkout; only required shared/anatomical/neutral/disco/prop assets and the three hair resources were hydrated.

## Integration-time findings

The animation checkpoint rebased cleanly onto `origin/main` at `18e528c73` and became commit `f14638df8` (full checkpoint hash is available through Git). Concurrent upstream work now supplies `scripts/blender/install_animation_tools.py` and the bundled Game Rig Tools fork. The earlier missing-add-on statement describes the authoring session at the stopping point; future resumed work can use the newly available installer. It was read, and no installation or animation rebuild was performed after the stop instruction.

A read-only fresh-source check of `flamenco_man_floreo_outward.blend` confirmed `f_index.01.L` reloads with rotation mode `QUATERNION`, while this generator authored `rotation_euler` for that finger control. **Editable finger animation requires a channel-mode compatibility repair on resume.** The full-body preview and structural action audit do not establish correct reloaded finger motion. The in-session baked action is a distinct preserved output; compare it with repaired authoring playback later. Evidence: `flamenco_solo/reloaded_finger_channels.log`. The generator's same finger-writing path is shared by the other studies, so apply this follow-up across the checkpoint.

The fast suite was rerun after the rebase: **10/10 passed in 9.09 seconds**, including the newly added Godot test-tree check (`flamenco_solo/post_rebase_fast.log`). Motion reports remain evidence from their generation passes; revalidate against the then-current shared scene during an authorized resume.

The rebased repository's `python scripts/lfs_policy.py check` passed for 23,461 staged files. Root attributes now follow the upstream size-generated policy; this task's exact-file small-binary exceptions remain narrowly scoped and compatible. The Animation section of `apps/a-game/AGENTS.md` now links this paused checkpoint and records the zero-coverage proxy and palmas arm-clearance lessons.

## Final preservation layout

Integration with concurrent `main` at `3f2039a5a` preserved the Solo Jive and Cha Cha Slide Animation notes alongside this task's notes. That upstream guidance requires stopped studies and stale exports to live beneath a task-specific `.gdignore`. Therefore the final delivery moves all 20 GLBs and their matching import settings into `flamenco_solo/exports/` and removes only their active runtime references. Their binary contents remain unchanged, and the source files stay in the existing ignored per-animation authoring directory. The saved-asset and storage audits use these final paths. Resumed publication requires completing the documented motion repairs and reviews before re-exporting through the normal workflow.

Final preservation verification passed: the read-only saved-asset audit still reads all 20 source/bake/export triplets, and the runtime registry matches the integrated upstream registry after removing this task's entries. The first post-integration fast run passed 9/10: `test_timeout_releases_resources_owned_by_descendants` raised `ConnectionResetError` while reconnecting to its local fixture socket. A complete retry passed **10/10 in 7.90 seconds**. Both outputs are retained in `flamenco_solo/post_integration_fast.log` and `flamenco_solo/post_integration_fast_retry.log`; test implementation was retained.

## Final exported-motion failure

`flamenco_solo/export_motion_audit.json` decodes every GLB animation sampler: all 20 files have zero varying output samplers and zero component change. Constant channels are an explicit failure for the ten moving clips (three braceo/port-de-bras, two floreo, two golpe, two palmas, one vuelta). Static position clips need a fresh control-versus-bake pose comparison before acceptance. The expanded `scripts/flamenco/inspect_saved.py` now also records varying source/baked curve counts and returns exit status 1 for the dynamic-export failures; its final JSON/log retain structural success separately from motion failure.

The saved-action inspection confirms the ten moving sources contain 2–37 varying curves each, while every corresponding baked action has zero varying curves. Thus the motion loss is already present in the saved bake, before GLB export.

Likely investigation lead, supplied by concurrent Animation guidance: reveal both participating rigs with `hide_viewport=False` and `hide_set(False)` before sampling, and compare the standalone saved bake to live control-rig motion with deform constraints muted. The task fallback did not explicitly reveal the deform rig. Its zero-error self-comparison therefore does not prove a correct moving bake. This is a diagnosed failure condition and a hypothesis for the cause, not an implemented repair. Use the now-bundled native Action Bakery workflow on an authorized resume and require varying source, bake, and exported channels for moving clips.

## Exact resume and verification commands

Run from `/workspace/sanjo-solutions/apps/a-game`. The environment's `blender` is **5.2.2 LTS**, build `d13f752e3b9c`; verify the version again in a new environment. The following authoring/export/render commands are documented for a future authorized resume only:

```bash
blender --version
# Future resumed setup, using the newly bundled tools:
blender -b --python-exit-code 1 --python scripts/blender/install_animation_tools.py
# Read-only saved-state audit and always-required tests:
blender -b --factory-startup --python-exit-code 1 --python scripts/flamenco/inspect_saved.py
python tests/run_tests.py --suite fast
# Focused resumed authoring; this overwrites only the selected task clip and publishes it:
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/flamenco/build.py -- --match port_de_bras --character man
# Woman generation after choreography/validation review:
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/flamenco/build.py -- --character woman
# Full task rebuild after reviewing the preliminary footwork definitions:
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/flamenco/build.py
# Preview an existing saved clip in Cycles CPU; edits are kept out of the source:
blender -b animations/man_and_woman/flamenco_man_palmas_claras.blend --python-exit-code 1 --python scripts/flamenco/preview.py -- 0 12 24 36 48
```

Open a source with `--python scripts/player_assets/animation_file_startup.py` to compose the shared editable scene. Hydrate its declared linked dependencies through the configured Git LFS identity before opening it. At this checkpoint `/tmp/a-game-git-credentials` was a temporary helper using the configured `SANJO_GITHUB_LFS_TOKEN`; recreate an equivalent helper without printing credentials if the environment requires it. Use only the `codex.sanjo.solutions@gmail.com` GitHub identity.

Before staging a regenerated binary, inspect its actual size and `git check-attr filter diff merge text -- <path>`. The exact exceptions here apply to this checkpoint's existing files; add exact exceptions for new files through 100 MiB and retain LFS for larger files. This checkpoint adds zero LFS objects; ordinary Git push uploads all new asset content. Integration fetches current origin/main, preserves concurrent updates and uses an ordinary history-preserving push. The chat delivery records the verified pushed commit. Git history retains the initial publication checkpoint; the final tree quarantines these stopped-study GLBs.
