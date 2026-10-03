# Forró partner repertoire — paused preservation record

- Date: 2026-10-02 (UTC). Recorded by Codex after the user's stop instruction.
- Chat/task title: Create Forró partner animations. Chat ID: `01a0fcea-8447-76d7-88e8-c2baa19e1047` (verified through the chat metadata).
- Project: A-Game, `apps/a-game`, sanjo-solutions cloud environment.
- Task branch at stop: `codex/forro-partner-repertoire`.
- Current commit at stop: `3c52737c74b488501e9cfe47e7029547c6f5fe88`.
- Original scope: a broad, organized coordinated Forró repertoire for both characters in `man_and_woman3.blend`, using Blender 5.2, existing paired authoring helpers and per-animation sources; natural motion, planted contacts, body clearance, smooth transitions and loop validation; then documentation, commits, rebase, main integration and push.
- Delivery state: **84 partial authored procedural blocking studies; 0 baked actions; 0 runtime exports.** The user halted production before final motion validation and visual review. These are preserved drafts, not a completed dance library.

## Saved work and stopping point

The repertoire contains 42 families with both `man_lead` and `woman_lead` variants. Each clip has synchronized `Man.rigify` and `Woman.rigify` action slots and BOTH participant metadata. The suffix identifies the leader; both characters participate in every source. The catalog covers seven positions, fourteen footwork families, six turn families, passing/travel/wrapping, and twelve directed position transitions. The [guide](../../scripts/forro.md) lists the vocabulary and workflow. This is a curated social repertoire, rather than an exhaustive claim about every regional Forró variation.

All sources use 24 fps, 120 BPM, stored frames 0–96. Loops play 0–95 with a duplicate closing pose at 96. Passing, wrapping and directed transitions play once through 96. Markers are Ready 0, Phrase A 24, Phrase B 48, Recover 72 and Loop/Finish 96. Per-file playback ends and roles appear in the inventory below and in [asset_inventory.json](forro_partner_repertoire/asset_inventory.json).

Existing `RigYogaPoser`, `DiscoWristPoser`, paired IK, `ActivityMotionAuthor` and `AnimationFileWriter` infrastructure was reused. Dance trajectories were authored procedurally with sparse control keys, planted world-space feet, native wrist constraints and calibrated palms. Existing solo disco arm phrases did not fit this coordinated choreography. Shared scenes, character geometry, existing animations, and the combined library were preserved.

Blender 5.2.2 LTS (`d13f752e3b9c`) was downloaded from the official distribution and SHA256 verified. Its path in this environment is `/workspace/tools/blender-5.2.2-linux-x64/blender`. Blender 4.3.2 was only identified during environment inspection; every Blender authoring, scripting, validation and rendering operation used 5.2.2.

At the stop request, generator PID 3130 was running the following selection:

```sh
/workspace/tools/blender-5.2.2-linux-x64/blender -t 4 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/create_forro.py -- --only position_shadow giro_follower_right giro_follower_left enrolar_desenrolar open_two_hand_to_shadow shadow_to_open_two_hand
```

It received SIGTERM and exited. Its log confirms nine completed saves: both shadow positions, both follower-right turns, both follower-left turns, both wraps, and `open_two_hand_to_shadow_man_lead`. The other three selected shadow transition files retain their previous saved versions. All 84 files are structurally readable. There are no remaining owned authoring or rendering processes. After stopping, work was limited to preservation, read-only verification, documentation and Git delivery.

The latest generator includes additional follower-turn contact samples, revised shadow spacing and grip depth, staged wrap/body rotation and staged overhead lowering. These refinements have **partial saved coverage**. The last overhead x-coordinate change has no completed motion validation. The catalog predates the final nine saves, so key-frame and pose assumptions can differ. The validator also contains a newly added transition endpoint velocity check that the historical report did not execute. Preserve these distinctions when resuming.

## Durable files and evidence

- `scripts/create_forro.py`: current procedural generator; ahead of some saved sources.
- `scripts/validate_forro.py`: saved-source motion and optional preview validator; current version includes transition velocity checks.
- `scripts/forro.md`: repertoire, timings, roles, tooling and explicit paused/draft notice.
- `animations/man_and_woman/forro_catalog.json`: 84-source catalog from the preceding completed pass; stale for the final partial refinement.
- `animations/man_and_woman/forro_validation.json`: historical 18-clip report, `passed: false`; 10 clip checks passed, eight failed, and 24 transition pose endpoint checks passed on those earlier assets. It is not a current whole-library certificate.
- `animations/man_and_woman/.gitattributes`: exact-filename ordinary-Git exceptions for these 84 small sources; existing asset rules retained.
- `docs/forro_review/.gitattributes`: exact exceptions for six existing PNG contact sheets.
- `docs/forro_review/{positions,footwork_1,footwork_2,turns,travel_and_wrap,transitions}.png`: six inspected review boards from earlier versions. The transitions board covers only the first six transition families. These are preview evidence, not final approval or current-file renders.
- `forro_partner_repertoire/asset_inventory.json`: exact paths, bytes, SHA256, roles, frame ranges, authored/baked/exported flags and association with historical measurements for all 84 files.
- `forro_partner_repertoire/baseline_results.json`: merged historical 84-clip measurements, retained as evidence. Hash equality determines whether each result still describes the saved binary.
- `forro_partner_repertoire/review_frames.tar.gz`: complete saved `.cache/forro` preview output, including `review` and `preview_fast`. Extracting restores the original cached directory contents. Mixed render revisions are preserved intentionally.
- `forro_partner_repertoire/session_diagnostics.tar.gz`: temporary Python diagnostic/preview/probe scripts from this session, retained for reproducibility. Some reference absolute paths and earlier source revisions; inspect them before future execution.
- `forro_partner_repertoire/*.log`: all saved Forró session logs, including failed runs, probes, source composition, render passes and fast-suite attempts. The final relevant logs are identified below.
- `forro_partner_repertoire/verify_saved_sources.py` and `preservation_structure.log`: read-only Blender 5.2 source-integrity verification after stopping.
- `forro_partner_repertoire/evidence_inventory.json`: exact bytes and SHA256 for preserved auxiliary files, logs, scripts, archives and boards (excluding the inventory itself).

## Verification and limitations

At preservation time, hashes associate **72 current sources with passing historical motion checks**, **three with failed historical checks**, and **nine with saved refinements awaiting motion checks**. Historical passing checks describe their measured geometric tolerances, not final aesthetic acceptance. The final partial generation did not complete a new catalog/report. The saved-source structural check cannot resolve those motion limitations.

Historical interpolation checks sampled authored keys, intervening half-frames, and near-loop boundaries. They measured finite keys, movement, IK error (6 mm), planted-foot position (6 mm) and rotation (0.035 radians), calibrated palm gap (22 mm), torso sphere clearance (35 mm), evaluated surface floor penetration (8 mm at five frames), knee bend (75 degrees), elbow bend (25 degrees), loop position (0.2 mm), rotation (0.002 radians), linear velocity (0.018 m/frame) and angular velocity (0.04 radians/frame). Torso proxies are partial clearance tests; whole-body overlap, natural motion and surface contacts need continued visual review.

Known failed historical cases include follower-turn woman-lead palm gaps of approximately 22.34 mm and wrap/shadow elbow bends below 25 degrees. Those turns and wraps now have new, unvalidated binaries. The three unchanged failing files are `forro_open_two_hand_to_shadow_woman_lead.blend` (palm and elbow), `forro_shadow_to_open_two_hand_man_lead.blend` (elbow), and `forro_shadow_to_open_two_hand_woman_lead.blend` (palm and elbow). A later shadow pose probe showed promising joint angles at selected poses, but that probe is not saved-file interpolation validation.

Commands/results:

```sh
python tests/run_tests.py --suite fast
# PASS: 10/10, 6.34 seconds after authoring stopped; forro-stop-fast.log.
python tests/run_tests.py --list --changed scripts/create_forro.py --changed scripts/validate_forro.py
# 10 fast, 0 related slow checks selected.
python -m py_compile scripts/create_forro.py scripts/validate_forro.py
# PASS.
git diff --check
# PASS before staging; the staged raw logs subsequently exposed two trailing-whitespace lines.
# Those original diagnostic lines are retained as evidence; implementation files pass.
/workspace/tools/blender-5.2.2-linux-x64/blender -t 4 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python docs/animation_work_status/forro_partner_repertoire/verify_saved_sources.py
# PASS: 84/84 with Blender 5.2.2 LTS. Read-only source/action count, two slots, BOTH metadata, 24 fps,
# 0–96 ranges, template/NLA bindings and finite keys for all 84 files.
```

After rebasing the task commits onto `origin/main` at `074c6a02e32d1d0c6960425218e8abec83e3c9b0`, the fast suite passed again: **10/10 in 6.16 seconds**, recorded in `integrated_fast.log`. `python scripts/lfs_policy.py check` from the repository root passed for all 24,229 staged files. Concurrent attributes and animation guidance were retained during conflict resolution.

Earlier fast-suite attempts failed because LFS hair mesh dependencies were still pointers, then because a process-cleanup timeout test failed while the machine was busy. Required mesh objects were retrieved; the final quiet run passed. Source composition also passed for `forro_position_closed_man_lead` through `animation_file_startup.py` (`forro-compose.log`). No final full motion validation or further rendering was performed after the stop request.

Storage inspection found all 84 Blend files between 126,036 and 175,416 bytes, totaling 11,849,516 bytes. The preview archive is 33,787,529 bytes. Every new binary is below 104,857,600 bytes and is committed as an ordinary Git blob. Existing shared-scene/anatomical/prop LFS assets retain their original rules. New assets travel in the ordinary Git push; this task introduces zero LFS uploads.

The `# Animation` section of `AGENTS.md` now records preservation/hash provenance, partial-generator catalog reconciliation, rest-bone foot rotation offsets, and native-wrist palm-solving lessons.

## Remaining work and resume commands

The immediate blocker is the user's explicit pause. Further animation production requires a future request to resume. Technical work remaining: reconcile all affected saved clips with the current generator; refresh the catalog; fix palm and elbow failures; validate all saved sources, subframes, transitions and loops; inspect every role variant and entire motion, including whole-body clearance and hand paths; then bake/export only if runtime assets are requested. The system has usable Blender 5.2 and retrieved source dependencies. Authentication uses the configured environment credential helper; tokens belong outside the repository.

From `/workspace/sanjo-solutions/apps/a-game`, after a future authorized resumption:

```sh
# Inspect current preservation hashes and logs before modifying sources.
cat docs/animation_work_status/forro_partner_repertoire/asset_inventory.json
# Restore preserved previews, if needed; this only extracts existing files.
mkdir -p .cache
# The archive has a top-level forro/ directory.
tar -xzf docs/animation_work_status/forro_partner_repertoire/review_frames.tar.gz -C .cache

# Resume the interrupted selection only after reviewing the outstanding issues.
/workspace/tools/blender-5.2.2-linux-x64/blender -t 4 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/create_forro.py -- --only position_shadow giro_follower_right giro_follower_left enrolar_desenrolar open_two_hand_to_shadow shadow_to_open_two_hand
# Once the generator/catalog are reconciled, measure the full library.
/workspace/tools/blender-5.2.2-linux-x64/blender -t 4 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_forro.py
# Render only after motion failures have been addressed.
/workspace/tools/blender-5.2.2-linux-x64/blender -t 4 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_forro.py -- --render-only --render .cache/forro/review
python tests/run_tests.py --suite fast
```

## Per-source inventory

All paths below are relative to `animations/man_and_woman/`. Every row is a partial procedural source, with **baked: false** and **exported: false**. Both characters participate. `pass` and `fail` refer to matching historical checks; `pending` marks a different saved hash awaiting motion validation. Full SHA256 and failure details are in `asset_inventory.json`.

| Source | Lead | Stored / playback | Bytes | Motion check |
| --- | --- | --- | ---: | --- |
| `forro_position_closed_man_lead.blend` | man | 0–96 / 0–95 | 126036 | pass |
| `forro_position_closed_woman_lead.blend` | woman | 0–96 / 0–95 | 127043 | pass |
| `forro_position_open_two_hand_man_lead.blend` | man | 0–96 / 0–95 | 127036 | pass |
| `forro_position_open_two_hand_woman_lead.blend` | woman | 0–96 / 0–95 | 126523 | pass |
| `forro_position_open_one_hand_man_lead.blend` | man | 0–96 / 0–95 | 126889 | pass |
| `forro_position_open_one_hand_woman_lead.blend` | woman | 0–96 / 0–95 | 126333 | pass |
| `forro_position_handshake_man_lead.blend` | man | 0–96 / 0–95 | 127074 | pass |
| `forro_position_handshake_woman_lead.blend` | woman | 0–96 / 0–95 | 126434 | pass |
| `forro_position_promenade_man_lead.blend` | man | 0–96 / 0–95 | 126967 | pass |
| `forro_position_promenade_woman_lead.blend` | woman | 0–96 / 0–95 | 127360 | pass |
| `forro_position_side_by_side_man_lead.blend` | man | 0–96 / 0–95 | 126317 | pass |
| `forro_position_side_by_side_woman_lead.blend` | woman | 0–96 / 0–95 | 126363 | pass |
| `forro_position_shadow_man_lead.blend` | man | 0–96 / 0–95 | 132984 | pending |
| `forro_position_shadow_woman_lead.blend` | woman | 0–96 / 0–95 | 133918 | pending |
| `forro_basico_lateral_man_lead.blend` | man | 0–96 / 0–95 | 136891 | pass |
| `forro_basico_lateral_woman_lead.blend` | woman | 0–96 / 0–95 | 136499 | pass |
| `forro_basico_frente_tras_man_lead.blend` | man | 0–96 / 0–95 | 136130 | pass |
| `forro_basico_frente_tras_woman_lead.blend` | woman | 0–96 / 0–95 | 135803 | pass |
| `forro_dois_pra_la_dois_pra_ca_man_lead.blend` | man | 0–96 / 0–95 | 131073 | pass |
| `forro_dois_pra_la_dois_pra_ca_woman_lead.blend` | woman | 0–96 / 0–95 | 130898 | pass |
| `forro_balanco_man_lead.blend` | man | 0–96 / 0–95 | 130224 | pass |
| `forro_balanco_woman_lead.blend` | woman | 0–96 / 0–95 | 130140 | pass |
| `forro_marcacao_man_lead.blend` | man | 0–96 / 0–95 | 136168 | pass |
| `forro_marcacao_woman_lead.blend` | woman | 0–96 / 0–95 | 136357 | pass |
| `forro_arrasta_pe_man_lead.blend` | man | 0–96 / 0–95 | 140927 | pass |
| `forro_arrasta_pe_woman_lead.blend` | woman | 0–96 / 0–95 | 141448 | pass |
| `forro_caminhada_man_lead.blend` | man | 0–96 / 0–95 | 131561 | pass |
| `forro_caminhada_woman_lead.blend` | woman | 0–96 / 0–95 | 132173 | pass |
| `forro_vai_e_vem_man_lead.blend` | man | 0–96 / 0–95 | 136566 | pass |
| `forro_vai_e_vem_woman_lead.blend` | woman | 0–96 / 0–95 | 136280 | pass |
| `forro_abertura_lateral_man_lead.blend` | man | 0–96 / 0–95 | 142125 | pass |
| `forro_abertura_lateral_woman_lead.blend` | woman | 0–96 / 0–95 | 142375 | pass |
| `forro_contrapasso_man_lead.blend` | man | 0–96 / 0–95 | 139839 | pass |
| `forro_contrapasso_woman_lead.blend` | woman | 0–96 / 0–95 | 139130 | pass |
| `forro_cruzado_man_lead.blend` | man | 0–96 / 0–95 | 132529 | pass |
| `forro_cruzado_woman_lead.blend` | woman | 0–96 / 0–95 | 132861 | pass |
| `forro_triangulo_man_lead.blend` | man | 0–96 / 0–95 | 140056 | pass |
| `forro_triangulo_woman_lead.blend` | woman | 0–96 / 0–95 | 139717 | pass |
| `forro_quadrado_man_lead.blend` | man | 0–96 / 0–95 | 131522 | pass |
| `forro_quadrado_woman_lead.blend` | woman | 0–96 / 0–95 | 131457 | pass |
| `forro_pe_de_serra_man_lead.blend` | man | 0–96 / 0–95 | 139940 | pass |
| `forro_pe_de_serra_woman_lead.blend` | woman | 0–96 / 0–95 | 139073 | pass |
| `forro_giro_casal_right_man_lead.blend` | man | 0–96 / 0–95 | 175112 | pass |
| `forro_giro_casal_right_woman_lead.blend` | woman | 0–96 / 0–95 | 175147 | pass |
| `forro_giro_follower_right_man_lead.blend` | man | 0–96 / 0–95 | 168324 | pending |
| `forro_giro_follower_right_woman_lead.blend` | woman | 0–96 / 0–95 | 164132 | pending |
| `forro_giro_leader_right_man_lead.blend` | man | 0–96 / 0–95 | 156619 | pass |
| `forro_giro_leader_right_woman_lead.blend` | woman | 0–96 / 0–95 | 159518 | pass |
| `forro_giro_casal_left_man_lead.blend` | man | 0–96 / 0–95 | 175416 | pass |
| `forro_giro_casal_left_woman_lead.blend` | woman | 0–96 / 0–95 | 174999 | pass |
| `forro_giro_follower_left_man_lead.blend` | man | 0–96 / 0–95 | 168199 | pending |
| `forro_giro_follower_left_woman_lead.blend` | woman | 0–96 / 0–95 | 165664 | pending |
| `forro_giro_leader_left_man_lead.blend` | man | 0–96 / 0–95 | 157001 | pass |
| `forro_giro_leader_left_woman_lead.blend` | woman | 0–96 / 0–95 | 159057 | pass |
| `forro_troca_de_lugar_man_lead.blend` | man | 0–96 / 0–96 | 174718 | pass |
| `forro_troca_de_lugar_woman_lead.blend` | woman | 0–96 / 0–96 | 173608 | pass |
| `forro_passeio_man_lead.blend` | man | 0–96 / 0–95 | 134344 | pass |
| `forro_passeio_woman_lead.blend` | woman | 0–96 / 0–95 | 134564 | pass |
| `forro_enrolar_desenrolar_man_lead.blend` | man | 0–96 / 0–96 | 164152 | pending |
| `forro_enrolar_desenrolar_woman_lead.blend` | woman | 0–96 / 0–96 | 163522 | pending |
| `forro_open_two_hand_to_closed_man_lead.blend` | man | 0–96 / 0–96 | 132791 | pass |
| `forro_open_two_hand_to_closed_woman_lead.blend` | woman | 0–96 / 0–96 | 132963 | pass |
| `forro_closed_to_open_two_hand_man_lead.blend` | man | 0–96 / 0–96 | 132562 | pass |
| `forro_closed_to_open_two_hand_woman_lead.blend` | woman | 0–96 / 0–96 | 132962 | pass |
| `forro_open_two_hand_to_open_one_hand_man_lead.blend` | man | 0–96 / 0–96 | 127181 | pass |
| `forro_open_two_hand_to_open_one_hand_woman_lead.blend` | woman | 0–96 / 0–96 | 127651 | pass |
| `forro_open_one_hand_to_open_two_hand_man_lead.blend` | man | 0–96 / 0–96 | 127937 | pass |
| `forro_open_one_hand_to_open_two_hand_woman_lead.blend` | woman | 0–96 / 0–96 | 128006 | pass |
| `forro_open_two_hand_to_handshake_man_lead.blend` | man | 0–96 / 0–96 | 129641 | pass |
| `forro_open_two_hand_to_handshake_woman_lead.blend` | woman | 0–96 / 0–96 | 129527 | pass |
| `forro_handshake_to_open_two_hand_man_lead.blend` | man | 0–96 / 0–96 | 130615 | pass |
| `forro_handshake_to_open_two_hand_woman_lead.blend` | woman | 0–96 / 0–96 | 129356 | pass |
| `forro_open_two_hand_to_promenade_man_lead.blend` | man | 0–96 / 0–96 | 147753 | pass |
| `forro_open_two_hand_to_promenade_woman_lead.blend` | woman | 0–96 / 0–96 | 147576 | pass |
| `forro_promenade_to_open_two_hand_man_lead.blend` | man | 0–96 / 0–96 | 148539 | pass |
| `forro_promenade_to_open_two_hand_woman_lead.blend` | woman | 0–96 / 0–96 | 148085 | pass |
| `forro_open_two_hand_to_side_by_side_man_lead.blend` | man | 0–96 / 0–96 | 142594 | pass |
| `forro_open_two_hand_to_side_by_side_woman_lead.blend` | woman | 0–96 / 0–96 | 142565 | pass |
| `forro_side_by_side_to_open_two_hand_man_lead.blend` | man | 0–96 / 0–96 | 141484 | pass |
| `forro_side_by_side_to_open_two_hand_woman_lead.blend` | woman | 0–96 / 0–96 | 141709 | pass |
| `forro_open_two_hand_to_shadow_man_lead.blend` | man | 0–96 / 0–96 | 160889 | pending |
| `forro_open_two_hand_to_shadow_woman_lead.blend` | woman | 0–96 / 0–96 | 142106 | fail |
| `forro_shadow_to_open_two_hand_man_lead.blend` | man | 0–96 / 0–96 | 141371 | fail |
| `forro_shadow_to_open_two_hand_woman_lead.blend` | woman | 0–96 / 0–96 | 142518 | fail |
