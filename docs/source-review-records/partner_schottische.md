# Partner schottische: preserved partial animation work

Recorded October 2, 2026. Stop instruction received at approximately 17:01 Europe/Berlin (15:01 UTC).
Task/chat label: **Partner schottische for man_and_woman3.blend**. The sidebar title is unavailable in this executor.
Project: `sanjo-solutions/apps/a-game`, checkout `/workspace/sanjo-solutions`.
Task branch: `codex/partner-schottische`.
Commit at recording start: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
Author of this record and the associated GitHub push: **Codex**.

The user's stop instruction takes priority over the original completion request. This delivery preserves **partial procedural blocking studies**, scripts, diagnostics, and existing exports. It represents 11 saved paired authoring sources, one saved paired bake, and two GLB exports from different authoring iterations. Full repertoire completion and production acceptance remain pending.

## Original scope

Create a broad coordinated Partner schottische repertoire for both characters in `man_and_woman3.blend`, using Blender 5.2 and the existing paired IK and per-animation source workflow. Include moves, positions, transitions, natural motion, planted contacts, clearance, interpolated checks, and loop checks. Reuse suitable motion; use ordinary Git for actual binaries up to 104,857,600 bytes, and LFS above that boundary. Commit animation work, fetch/rebase onto `origin/main`, update the app's Animation guidance in a separate commit, then integrate into main, push, and verify remote inclusion.

## Saved sources and exact state

All rows use prefix `partner_schottische_` and live at `animations/man_and_woman/<prefix><suffix>.blend`. Both character slots participate: `OBMan.rigify` / player and `OBWoman.rigify` / partner. The tempo is 120 beats/minute, at 24 frames/second. Position clips span 48 frames (2 seconds); basic loops span 192 frames (8 seconds). The combined library discovers these individual sources on reopening through Player Asset Export. Its binary and the shared rig/geometry files retain their original contents.

| Suffix | Frames | Baked action in current source | GLB state | Final read-only source review |
| --- | --- | --- | --- | --- |
| `basic_closed` | 0–192 | Pending | Pending | PASS |
| `basic_double_hand` | 0–192 | Pending | Pending | PASS |
| `basic_open` | 0–192 | Saved | Current saved bake exported | PASS |
| `basic_promenade` | 0–192 | Pending | Pending | FAIL: wrist bend 2.5765 rad |
| `basic_sweetheart` | 0–192 | Pending | Pending | PASS |
| `position_closed` | 0–48 | Pending | Pending | PASS |
| `position_double_hand` | 0–48 | Pending | Earlier iteration exported; current source is authoring-only | PASS |
| `position_open` | 0–48 | Pending | Pending | PASS |
| `position_promenade` | 0–48 | Pending | Pending | PASS |
| `position_shadow` | 0–48 | Pending | Pending | PASS |
| `position_sweetheart` | 0–48 | Pending | Pending | PASS |

`basic_open` includes `partner_schottische_basic_open.baked`, with slots `OBMan.rigify_deform` and `OBWoman.rigify_deform`. The other ten current sources contain their authoring action only. The earlier two-hand export predates the current source's hand fitting; treat source/export synchronization as pending.

Exact source action names, ranges, slots, participant properties, byte sizes, and SHA-256 hashes are in `partner_schottische_evidence/source_inventory.json` beside this record. The eleven corresponding JSON files in `animations/man_and_woman/schottische_review/` are the final preservation reviews; each includes the reviewed source hash.

## Exported assets and integration metadata

- `models/player/animation_updates/partner_schottische_basic_open_baked_cf291225a62c.glb`: 835,752 bytes, one paired 8-second animation, 1,269 channels.
- `models/player/animation_updates/partner_schottische_position_double_hand_baked_fd5fce6b310f.glb`: 583,472 bytes, one paired 2-second animation, 1,269 channels; earlier authoring iteration.
- Each export has its matching `.glb.import` descriptor. Both parse successfully with Godot's `ConfigFile`. The two-hand descriptor originally inherited a malformed partial `_subresources` replacement; its original text is preserved as `partner_schottische_evidence/position_double_hand_import_before_metadata_repair.txt`. Recording repaired only that descriptor's text structure and retained the GLB bytes.
- `models/player/animation_updates.tres` contains the two new update-library references while retaining the prior entries.
- `partner_schottische_evidence/export_inventory.json` records clip names, target counts, durations, skin names, sizes, and hashes. Full Godot character playback, comprehensive mesh clearance, and final choreography review remain pending.

## Authoring and export scripts

- `scripts/player_assets/partner_schottische.py`: experimental choreography builder. It reuses the saved `idle` stance, the existing paired IK helper, calibrated palm targets, and `AnimationFileWriter`. It plans 37 figures: six positions, six basics, four travel directions, step-hop, heel-toe, rock/recover, three coupled turns/circles, two underarm turns, separate turns, ten formation transitions, join, and release. Saved output covers the eleven table rows. Remaining planned clips have yet to reach saved source output.
- `scripts/player_assets/export_partner_schottische.py`: half-frame reviewer, Blender native visual bake, paired-slot verification, compact clip export, and the existing `AnimationUpdates` publisher. `-- --review-only` runs the read-only motion evaluation and writes its JSON report. Its default invocation also bakes, exports, and rewrites the selected source.

These scripts are **procedural blocking work in progress**. The final generator revision includes wider elbow poles and damped forearm-aligned palm orientation fitting. It has been applied only to the final static shadow/promenade studies. Earlier saved clips reflect earlier script revisions. Byte-for-byte regeneration of all saved sources from the final script remains unverified. Dance actions opt out of the idle wrist clamp and instead use explicit wrist frames plus the measured bend check; inspect twist, fingers, and skin contact before approving this approach.

## Validation and evidence

All Blender execution used **Blender 5.2.2 LTS**, hash `d13f752e3b9c`. Game Rig Tools was absent during authoring. The native visual-bake fallback preserves the paired action/slot naming and per-animation source/export structure. No Game Rig Tools installation was completed. The subsequently integrated main now includes the bundled add-on and `scripts/blender/install_animation_tools.py`; use that setup before resuming.

- `python tests/run_tests.py --suite fast`: **9/9 passed** after restoring required existing hair mesh LFS prerequisites. Earlier runs failed because those files were pointer stubs. `partner_schottische_evidence/fast_suite.log` captures the preservation run.
- `python tests/run_tests.py --changed scripts/player_assets/partner_schottische.py --changed scripts/player_assets/export_partner_schottische.py`: **9/9 passed**; the selector chose the fast set and zero additional slow fixtures. `related_suite.log` records the result.
- `python -m py_compile scripts/player_assets/partner_schottische.py scripts/player_assets/export_partner_schottische.py`: passed.
- Blender 5.2 action inventory: eleven source files read successfully; their bytes remained unchanged. See `source_inventory.log` and `source_inventory.json`.
- Final half-frame review: **10/11 sources passed** the implemented checks. `basic_promenade` fails the 0.65-radian wrist-bend limit with 2.5765 radians (about 148 degrees). Its source remains a blocking study. The later static `position_promenade` passes after pole/hand fitting.
- Review limits: foot target error 0.008 m, paired palm separation 0.012 m, torso sphere-proxy gap above 0.06 m, wrist bend below 0.65 rad, loop endpoint position below 0.008 m, angle below 0.10 rad, and estimated seam velocity difference below 0.18 m/s. Samples include every half frame, including interpolation and loop boundaries. Moving basics have about 0.004 m maximum target error and 0.1375 m/s seam-velocity difference. Passing these local diagnostics supplies measured blocking evidence; full mesh, finger, balance, and visual motion acceptance remain separate.
- Native bake checks compared all deform-bone matrices at five sampled frames. The initial cleaned bake failed the 0.0002 matrix-component tolerance (0.0003568 observed); disabling bake key cleanup allowed the basic-open bake/export to complete. The earlier two-hand bake/export also completed. Saved logs preserve both paths.
- Both GLBs have valid binary headers and a single paired clip. Both import descriptors parse in Godot 4.6.3. See `import_descriptors.log` and `export_inventory.json`.
- Historical Blender renders: `schottische_closed.png`, `schottische_sweetheart.png`, and `schottische_promenade.png` in the evidence directory. These show earlier blocking iterations, including the problematic earlier promenade hand. They serve as historical diagnostics rather than final visual acceptance.
- Earlier source reviews are retained under `partner_schottische_evidence/historical_review/`. Final verification logs use `review_<suffix>.log`, with `preservation_review_summary.log` listing process outcomes. Historical authoring, export, wrist diagnostics, and the Blender crash report are also preserved there.

## Stopping point, processes, and blockers

An authoring process for static shadow/promenade was already running when the stop instruction arrived. Shadow had saved successfully. The termination attempt found that the promenade process and its parent shell had already completed; that final saved output is preserved too. No additional authoring, refinement, generation, or rendering was started after the stop instruction. Subsequent Blender invocations were inventories and read-only source reviews. All owned Blender processes have exited.

Concrete outstanding work:

1. Re-author and validate the moving promenade study; its excessive wrist bend is reproducible. The latest static hold passes and supplies a candidate starting point.
2. Inspect whole-body/finger mesh contacts and playback. Current clearance evidence uses torso proxies and historical still renders. The current repertoire has yet to receive complete natural-motion review.
3. Resolve occasional IK NaNs and the background Blender crash observed while authoring `basic_shadow`. Its attempted animation remained in process memory; a completed `basic_shadow.blend` is absent. `idle.crash.txt` and `schottische_author.log` preserve the available diagnostics. Wider poles improved the final static shadow, with residual wrist bend about 0.294 rad; applying this to the moving figure is pending.
4. Finish the remaining 26 catalog figures and validate their counts, support phases, turn grips, transitions, root displacement, and loops. The planned catalog is finite and covers common schottische figures; regional variations require an explicit scope decision.
5. Bake/export the ten authoring-only sources after acceptance; synchronize the two-hand source/export pair. Verify final imported tracks and playback on the composed Godot models.
6. Review the native-bake fallback against the installed Game Rig Tools workflow when that add-on is available. Retain Blender 5.2 and per-animation source isolation.

## Exact resume commands

Run these only after a new instruction resumes animation work, from `/workspace/sanjo-solutions/apps/a-game`, with a clean task branch based on current main. Preserve the saved studies before regenerating; the generator overwrites its selected source path.

```sh
blender --version
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py

# Read-only diagnosis of the known failing saved source:
blender -t 2 -b animations/man_and_woman/partner_schottische_basic_promenade.blend --python-exit-code 1 --python scripts/player_assets/export_partner_schottische.py -- --review-only

# Regenerate that selected study from the idle source after reviewing the solver:
blender -t 2 -b animations/man_and_woman/idle.blend --python-exit-code 1 --python scripts/player_assets/partner_schottische.py -- --clip basic_promenade

# Continue catalog entries whose source paths are absent:
blender -t 2 -b animations/man_and_woman/idle.blend --python-exit-code 1 --python scripts/player_assets/partner_schottische.py -- --resume

# After motion acceptance, bake and publish one current source:
blender -t 2 -b animations/man_and_woman/partner_schottische_basic_promenade.blend --python-exit-code 1 --python scripts/player_assets/export_partner_schottische.py

python tests/run_tests.py --suite fast
python tests/run_tests.py --changed scripts/player_assets/partner_schottische.py --changed scripts/player_assets/export_partner_schottische.py
```

Existing source prerequisites are `idle.blend`, `shared_scene_data.blend`, the two anatomical source libraries, and their referenced assets. They were hydrated through the environment's configured GitHub/LFS credential binding. The export add-on loader points into this checkout. A new worktree needs its own loader installation. The shell's `blender` resolves to the installed 5.2.2 executable under `/workspace/.cloud-onboarding/3d-tools/`.

## Storage and delivery

All sixteen task binaries (eleven sources, two GLBs, three historical PNGs) are at or below 104,857,600 bytes. The largest is 6,939,656 bytes. Exact paths, sizes, hashes, and storage choices are in `partner_schottische_evidence/binary_inventory.json`. Before rebase, exact-path `.gitattributes` overrides selected these files for regular Git; `storage_before.txt` and `storage_after.txt` preserve those historical observations. Concurrent main migrated storage to the generated size policy in `scripts/lfs_policy.py`. Rebase retained that current policy, which stores these files directly in Git without per-task exceptions. This task adds zero LFS objects; ordinary Git push uploads its binaries.

Preservation commit: `a8a0155dba8bbe7983b6285b4da1dfbb25693499`, rebased onto `43b08e48560a18a90ad2d20c193274d51827aef9`. Rebase retained main's generated storage policy and combined all 19 incoming animation-library entries with this task's two entries. Source binaries and the shared `idle.blend` / `shared_scene_data.blend` payload hashes remain unchanged; the latter two changed only their Git storage representation. Main also revised shared Python authoring helpers, so resumed motion work should revalidate against that code revision.

Post-rebase `python tests/run_tests.py --suite fast`: **10/10 passed**, recorded in `partner_schottische_evidence/post_rebase_fast_suite.log`. The incoming main added a fast check. The repeated task-scoped suite also passed **10/10**, with zero additional slow fixtures selected; see `post_rebase_related_suite.log`. `python scripts/lfs_policy.py check` passed for the integrated index. The separate Animation guidance commit documents independent static/moving hold validation and per-clip generator revisions. The final chat delivery reports its hash, integration commit, push outcome, and remote inclusion verification.

Final integration fetched `391093e0a12796f1ff91eb7a68170cb5fb2d447c` immediately before merging. The merged registry retains all 288 incoming references plus the two schottische references (290 total). The integrated fast suite passed **10/10**; see `partner_schottische_evidence/integration_fast_suite.log`. Documentation commit: `e39d81a83305ff186e18aa221a2bf7e4837c7858`.

The first ordinary push encountered a concurrent update. Delivery integrated newer `origin/main` at `51c03e3053207b9831af5ee44ed36020b0dd9fb5`, retaining all 352 incoming registry references plus this task's two (354 total). The repeated integrated fast suite passed **10/10**; see `partner_schottische_evidence/integration_retry_fast_suite.log`.

A further concurrent push retry integrated `ee594a5f0c983ca213d133b4867976337526980a` with all registry paths preserved; the integrated fast suite passed **10/10** (`partner_schottische_evidence/latest_integration_fast_suite.log`).

A further concurrent push retry integrated `569fc01b86a21650a10a6839b6ce56d8e2225ec4` with all registry paths preserved; the integrated fast suite passed **10/10** (`partner_schottische_evidence/latest_integration_fast_suite.log`).

A further concurrent push retry integrated `9ccbeadfb16ef3847f5e1bc0a0728fae30be23c5` with all registry paths preserved; the integrated fast suite passed **10/10** (`partner_schottische_evidence/latest_integration_fast_suite.log`).
