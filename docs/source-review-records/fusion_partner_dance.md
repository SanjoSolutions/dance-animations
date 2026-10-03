# Fusion partner dance preservation checkpoint

Date: 2026-10-02 (Europe/Berlin). Stopped on the user’s coordinated preservation instruction.
Chat/task title: Fusion partner dancing for man_and_woman3.blend (descriptive task title; the UI title was unavailable).
Checkout: `/workspace/sanjo-solutions`, app `apps/a-game`, sanjo-solutions cloud environment.
Branch at stop: `codex/fusion-partner-dance`.
Base/current commit before preservation: `fe09ef7b6a54f03909f7335d9673a27c15007d69`. The commit containing this record is the task checkpoint.

## Scope and delivery state

The original request was a broad coordinated Fusion partner-dance repertoire for both characters, authored, baked, rendered, and exported with Blender 5.2, following the individual animation-file workflow, with natural motion, contacts, clearance, transitions, reuse, validation, commits, rebase, documentation, and publication.

**Preserved work is partial and constitutes procedural blocking studies, not a completed or comprehensively validated Fusion dance library.** Twenty individual source files and twenty paired GLB exports exist. Each source includes an authoring action and matching `.baked` action, with separate Man and Woman slots. All saved clips span frames 0–96, at 24 fps (4 seconds, eight beats at the intended 120 BPM). Frame 96 is the repeated endpoint; loop playback should use 0–95. Names identify intended figures and require further choreographic review.

Eleven saved sources pass the final read-only reopened-source versus baked-pose comparison. Nine fail it. Six saved stepping/travel clips have approximately 11.4–11.7 mm of sampled plant drift, above the subsequently tightened 3 mm gate. Their older reports say `passed: true` under the earlier 12 mm gate; that field does not establish readiness under the latest criteria. All twenty GLBs are retained byte-for-byte in the checkpoint evidence `exports/` directory with their import settings. A `.gdignore` keeps these paused studies outside runtime import. Their Fusion entries have been removed from the active animation update catalog; existing and concurrent entries remain present.

`triple_step` currently shares the side-basic trajectory and still needs syncopated step timing. `counterbalance` and `compression_stretch` share the same principal placement profile. Closed, shadow, promenade, and sweetheart names describe preliminary placement studies; proper frame/grip details and complete dance technique remain review work. Turns, transitions, dips, and comprehensive wrap/underarm vocabulary are incomplete. Fusion has an open-ended vocabulary; the 45-entry planned catalog was a practical starting scope rather than an exhaustive syllabus.

## Durable files and exact inventory

- `scripts/create_fusion_dance.py`: procedural authoring, 45 planned clip specifications, sparse IK controls, contact checks, native bake fallback, per-animation saving and GLB publishing. The latest source has a stationary-root interpolation experiment that had not completed a build when stopped. Its current output is therefore not a reproducible byte-for-byte description of all saved assets.
- `scripts/review_fusion_dance.py`: read-only saved-source versus baked-deformation check and optional Blender Workbench rendering. Use it without `--render` for verification.
- `scripts/finalize_fusion_dance.py`: reopen/rebake/verify/save/export helper. This mutates assets; reserve it for a newly authorized resumption.
- `models/player/animation_updates.tres`: preserves existing and concurrent references. Fusion studies remain archived pending completed review.
- `animations/man_and_woman/.gitattributes`, the evidence directory’s `.gitattributes`, and `exports/.gitattributes`: exact-file regular-Git exceptions for inspected task binaries.
- [Evidence and exact sizes/hashes](fusion_partner_dance_evidence/asset_inventory.json): every source, export, import-settings file, SHA-256, roles, range, and validation record.
- `fusion_partner_dance_evidence/`: copied authoring logs, twenty original per-clip reports, final read-only review logs/results, two already-rendered diagnostic PNGs, initial diagnostic Python studies, fast/related test results, and test-selection output. No additional animation or render was produced after the stop instruction.

| Clip | Authored / baked / exported | Reopened bake check | Plant drift, mm |
| --- | --- | --- | ---: |
| `fusion_box_basic` | Yes / yes / yes | FAIL: source/bake difference | 11.427 |
| `fusion_closed_offset` | Yes / yes / yes | PASS | 0.230 |
| `fusion_compression_stretch` | Yes / yes / yes | FAIL: source/bake difference | 0.209 |
| `fusion_counterbalance` | Yes / yes / yes | PASS | 0.209 |
| `fusion_forward_back_basic` | Yes / yes / yes | FAIL: source/bake difference | 11.622 |
| `fusion_open_double_sway` | Yes / yes / yes | PASS | 0.231 |
| `fusion_open_single_left` | Yes / yes / yes | PASS | 0.231 |
| `fusion_open_single_right` | Yes / yes / yes | PASS | 0.231 |
| `fusion_promenade_left` | Yes / yes / yes | PASS | 0.231 |
| `fusion_promenade_right` | Yes / yes / yes | PASS | 0.230 |
| `fusion_promenade_walk` | Yes / yes / yes | FAIL: source/bake difference | 11.622 |
| `fusion_pulse` | Yes / yes / yes | PASS | 0.233 |
| `fusion_send_out_return` | Yes / yes / yes | FAIL: source/bake difference | 0.180 |
| `fusion_shadow` | Yes / yes / yes | FAIL: source/bake difference | 0.231 |
| `fusion_shadow_walk` | Yes / yes / yes | FAIL: source/bake difference | 11.622 |
| `fusion_side_basic` | Yes / yes / yes | FAIL: source/bake difference | 11.619 |
| `fusion_side_by_side` | Yes / yes / yes | PASS | 0.231 |
| `fusion_sweetheart` | Yes / yes / yes | PASS | 0.231 |
| `fusion_triple_step` | Yes / yes / yes | FAIL: source/bake difference | 11.619 |
| `fusion_weight_transfer` | Yes / yes / yes | PASS | 0.232 |

Each source remains at `animations/man_and_woman/<clip>.blend` to preserve its relative shared-scene binding. GLBs and import settings are archived at `docs/animation_work_status/fusion_partner_dance_evidence/exports/`; `asset_inventory.json` records original and current paths.

## Validation and limits

- Blender: **5.2.2 LTS**, build `d13f752e3b9c`; all Blender authoring, baking, checking, rendering, and export used this binary.
- `python tests/run_tests.py --suite fast`: **9/9 passed** at preservation time. Initial execution failed on LFS pointer hair fixtures; restoring `playground/hair/physics/*.res` resolved that prerequisite.
- `python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_animation_participants.py`: **11/11 passed**, including the nine fast checks and both relevant Blender fixture checks.
- Each authored clip was sampled at 193 half-frame times for foot-target positions, connected-palm positions, torso proxy clearance, endpoint positions, and boundary linear velocities. These are diagnostic proxies, not complete mesh-intersection, angular-continuity, or anatomical comfort certification.
- `blender --background --threads 1 <source> --python-exit-code 1 --python scripts/review_fusion_dance.py -- --output <report.json>`: all twenty saved sources were checked after stopping. Eleven pass, nine fail; per-file errors and command output are in `stop_reviews/`. This checks 0, 0.5, 12, 24, 48, 72, 95.5, and 96 against both baked deform rigs, with a 6 mm maximum allowed difference.
- Read-only GLB inspection: **20/20** valid GLB v2 containers, exactly one clip each, channels for both Man and Woman. All forty source/export binaries are below 104,857,600 bytes; combined size 91,724,029 bytes before evidence. Largest binary: 4,006,338 bytes. Exact individual sizes and hashes accompany the checkpoint.
- Existing open-hold Workbench renders were inspected before stopping (`open.png`, `probe.png`). They establish an initial pose review only; the full repertoire has no completed visual playback or complete surface-clearance review.
- The broad automatic `--list` selection included 186 slow checks, many for unrelated whole-library features. That full selection was not run. The focused fixtures and actual saved-source checks above are the completed related verification. Game Rig Tools and an initialized full animation-export cache are absent from this environment; numerous unrelated authoring assets remain LFS pointers. Full Godot runtime import/playback of these new clips is unverified.

## Process stop and procedural studies

- Sent SIGTERM to owned Blender PIDs **2466** (remaining repertoire batch) and **3146** (stationary-root diagonal experiment). Confirmed authoring/rendering processes ended. Their completed files remain present; in-memory poses were lost when those processes terminated.
- The remaining batch had logged failed follower/leader turn checks and reached `leader_turn_right`; no turn source/export was saved. The stationary-root diagonal experiment had only startup output in `refine2.log` and no durable clip.
- Earlier `diagonal_basic`, `lateral_travel`, and circle tests failed the plant gate. A three-frame-key diagonal trial still measured 7.47 mm plant drift. The subsequent stationary-root hypothesis is stored in the script and is unverified.
- A native bake initially differed by about 55 mm at fingers because changing rotation modes was absent from the action-only save. Quaternion finger keys fixed that issue. Preparing the bake dependency graph and reopening/rebaking corrected a separate ~15.7 mm arm discrepancy for eleven clips; nine saved clips still fail the final comparison.
- Game Rig Tools is unavailable. Native `bpy_extras.anim_utils` visual baking was composed with the existing action-slot/NLA convention, animation file writer, clip scene, participant filter, and update publisher. This fallback still requires the remaining per-asset verification/repair.
- Reused the existing idle starting stance and the solo-disco forearm-following `DiscoWristPoser`; no claim is made that the original solo disco choreography itself became partner dancing. The source library and shared rig/geometry files were kept intact.

## Resume commands and outstanding work

Continue only following a new authorization to resume animation work. Commands run from `apps/a-game`. Restore evidence reports to the ignored working cache before using the finalizer:

```bash
blender --version
mkdir -p .cache/fusion
cp docs/animation_work_status/fusion_partner_dance_evidence/fusion_*.json .cache/fusion/
# Read-only verification of an existing source:
blender --background --threads 1 animations/man_and_woman/fusion_open_double_sway.blend --python-exit-code 1 --python scripts/review_fusion_dance.py -- --output .cache/fusion/recheck_open.json
# Authoring experiment, only after renewed authorization:
blender --background --threads 1 animations/man_and_woman/idle.blend --python-exit-code 1 --python scripts/create_fusion_dance.py -- --clips diagonal_basic
# Reopen/rebake/export a specific checkpoint, only after renewed authorization:
blender --background --threads 1 animations/man_and_woman/fusion_box_basic.blend --python-exit-code 1 --python scripts/finalize_fusion_dance.py
python tests/run_tests.py --suite fast
```

First inspect the final nine bake failures, then establish planted feet under the tighter gate and audit the latest stationary-root change. Compare complete pose and velocity/rotation continuity between clips. Correct the repeated/placeholder choreography, complete unsaved turns and transitions, author remaining connections/wraps/underarm figures as appropriate, inspect fingers/wrists/full surfaces and support transfer in actual playback, and verify Godot import/playback and loop settings. Reinspect sizes/attributes before staging any resumed binaries.

## Storage and integration

All preserved task binaries use ordinary Git with exact-filename attribute exceptions because their actual sizes are at or below 100 MiB. Existing unrelated LFS assets retain their storage policy. No new task binary requires LFS upload. Commits identify Codex and carry exactly one requested co-author trailer. Fetch/rebase and final integration use ordinary history-preserving pushes; the final chat response records the resulting hashes and remote verification.

## Concurrent integration context

The task checkpoint was rebased onto fetched `origin/main` at `e12670ea9`. The resulting task commit is `688d5a66abf10a6b2a377e0ac57bfc32b5304850`. Conflicts in the two per-directory attribute files and animation update catalog were resolved by retaining both branches' entries; the merged catalog contained 38 animation-library references at that point.

Fetched main supplies `scripts/blender/install_animation_tools.py` and its setup guide. Game Rig Tools was absent from the active Blender profile during this task's authoring; a resumed task should follow that newly available installation workflow before choosing the native fallback. The newly available repository storage-policy check passed after rebase. The original diagnostics remain historical evidence from their recorded source hashes and environment.

Post-rebase fast verification: `python tests/run_tests.py --suite fast` passed **10/10** checks under the updated main test catalog. The output is saved in `fusion_partner_dance_evidence/post_rebase_fast_tests.log`. All forty task asset hashes were rechecked after conflict resolution.

The fetched animation-delivery instructions require paused exports to remain under a task-specific ignored directory. A preservation-only packaging commit archives the twenty existing GLBs/import settings under the evidence directory, retaining their exact hashes and removing their active runtime references. Blender sources remain at their original paths to retain saved relative shared-scene bindings. No animation was authored, rebaked, exported, or rendered during this packaging step. Historical logs retain their original output paths.

Delivery packaging verification: the fast suite passed **10/10** again after archiving the paused exports. `delivery_fast_tests.log` records this run. The repository LFS policy check passed for the staged checkpoint.
