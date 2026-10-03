# Solo jazz animation work — preserved partial state

Date: October 2, 2026 (Europe/Berlin). Animation generation stopped at approximately 16:56 CEST (14:56 UTC).

Chat/task title: **Solo jazz animations for man_and_woman3.blend** (descriptive task title; the desktop UI title was unavailable).

Task branch: `codex/solo-jazz`. Commit at the stopping point: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
Repository: `SanjoSolutions/sanjo-solutions`; project: `apps/a-game` in the sanjo-solutions cloud environment.

## Governing instruction and delivery state

The user's stop-and-preserve instruction superseded repertoire completion. Authoring and rendering are stopped. This record and its adjacent evidence preserve the partial procedural blocking studies, including their failures. A later explicit resume instruction is required before further animation work.

The original request covered a broad solo-jazz repertoire for both characters, natural motion, planted contacts, body clearance, smooth transitions, interpolated and loop validation, per-animation Blender files, exports, size-based Git storage, animation commit, fetch/rebase, an `AGENTS.md` Animation update, and merge/push to main. Blender **5.2.2 LTS**, build `d13f752e3b9c`, was used for every Blender operation.

The score currently describes **88 clips per character / 176 planned clips**: 54 moving figures, 12 positions, and 22 position transitions. **18 source/bake/export families are saved: seven Man and eleven Woman.** The other **158 planned clips remain unbuilt**, including every held position and entry/exit transition. Solo jazz has an open-ended vocabulary; the score is a broad selection, rather than a claim of exhaustive cultural coverage.

These are **procedural blocking studies**. Their choreography, finger deformation, export naming, and finished natural-motion quality require further work. Their generated exports are preserved for inspection. The active `models/player/animation_updates.tres` retains its pre-task entries. The proposed registry containing the studies is preserved as `solo_jazz_evidence/proposed_animation_updates.tres.txt`.

## Exact saved animation families

Every listed file contains an editable authoring action and its matching `.baked` action. Each action family has **one participant slot**. `PLAYER` means Man, `PARTNER` means Woman. Each listed clip uses **frames 0–96 inclusive**, 24 FPS, 120 BPM, a four-second eight-count phrase; frame 96 repeats the opening pose. Godot names use `_baked`. All listed sources, baked actions, GLBs, and GLB import settings are saved, but are **blocked studies rather than production-approved animations**.

Source directory: `animations/man_and_woman/`.
Export directory: `models/player/animation_updates/`.
Each exported GLB has its adjacent `.glb.import` settings file.

| Action | Role | Source filename | Export filename |
| --- | --- | --- | --- |
| `solo_jazz_man_pulse` | PLAYER | `solo_jazz_man_pulse.blend` | `solo_jazz_man_pulse_baked_e694f5aaa3b9.glb` |
| `solo_jazz_man_step_touch` | PLAYER | `solo_jazz_man_step_touch.blend` | `solo_jazz_man_step_touch_baked_3cdb3b04856a.glb` |
| `solo_jazz_man_jazz_walk` | PLAYER | `solo_jazz_man_jazz_walk.blend` | `solo_jazz_man_jazz_walk_baked_bd8f30b5d888.glb` |
| `solo_jazz_man_boogie_forward` | PLAYER | `solo_jazz_man_boogie_forward.blend` | `solo_jazz_man_boogie_forward_baked_458b531a8bfc.glb` |
| `solo_jazz_man_boogie_back` | PLAYER | `solo_jazz_man_boogie_back.blend` | `solo_jazz_man_boogie_back_baked_8b596ba1f9a3.glb` |
| `solo_jazz_man_boogie_drop` | PLAYER | `solo_jazz_man_boogie_drop.blend` | `solo_jazz_man_boogie_drop_baked_9509d0b97033.glb` |
| `solo_jazz_man_charleston_basic` | PLAYER | `solo_jazz_man_charleston_basic.blend` | `solo_jazz_man_charleston_basic_baked_f086fdb3740b.glb` |
| `solo_jazz_woman_pulse` | PARTNER | `solo_jazz_woman_pulse.blend` | `solo_jazz_woman_pulse_baked_a81b8270043d.glb` |
| `solo_jazz_woman_step_touch` | PARTNER | `solo_jazz_woman_step_touch.blend` | `solo_jazz_woman_step_touch_baked_79c39b8616d8.glb` |
| `solo_jazz_woman_jazz_walk` | PARTNER | `solo_jazz_woman_jazz_walk.blend` | `solo_jazz_woman_jazz_walk_baked_03e62b8590e2.glb` |
| `solo_jazz_woman_boogie_forward` | PARTNER | `solo_jazz_woman_boogie_forward.blend` | `solo_jazz_woman_boogie_forward_baked_8bf261c12836.glb` |
| `solo_jazz_woman_boogie_back` | PARTNER | `solo_jazz_woman_boogie_back.blend` | `solo_jazz_woman_boogie_back_baked_8682334c5487.glb` |
| `solo_jazz_woman_boogie_drop` | PARTNER | `solo_jazz_woman_boogie_drop.blend` | `solo_jazz_woman_boogie_drop_baked_c13a2e00ee8d.glb` |
| `solo_jazz_woman_charleston_basic` | PARTNER | `solo_jazz_woman_charleston_basic.blend` | `solo_jazz_woman_charleston_basic_baked_33ecf4d6a8a5.glb` |
| `solo_jazz_woman_charleston_kicks` | PARTNER | `solo_jazz_woman_charleston_kicks.blend` | `solo_jazz_woman_charleston_kicks_baked_719a92aacb57.glb` |
| `solo_jazz_woman_charleston_double_kick` | PARTNER | `solo_jazz_woman_charleston_double_kick.blend` | `solo_jazz_woman_charleston_double_kick_baked_9ff21be356d7.glb` |
| `solo_jazz_woman_charleston_hand_to_hand` | PARTNER | `solo_jazz_woman_charleston_hand_to_hand.blend` | `solo_jazz_woman_charleston_hand_to_hand_baked_ed24acfd01e6.glb` |
| `solo_jazz_woman_kick_ball_change_left` | PARTNER | `solo_jazz_woman_kick_ball_change_left.blend` | `solo_jazz_woman_kick_ball_change_left_baked_26a77103e610.glb` |

`scripts/solo_jazz/catalog.json` records each exact source/export/import path, actual bytes, SHA-256, role, range, in-session metrics, and fresh-load verification results. Both the source `.blend` files and the exported GLBs are retained, including the blocked finger poses and morph tracks.

## Implementation and evidence files

- `scripts/solo_jazz/repertoire.py`: counted footstep and gesture score, mirrored variants, pose definitions, and sequential foot pickup for position transitions. Most definitions have yet to produce saved assets.
- `scripts/solo_jazz/author.py`: Blender 5.2 guard; Rigify IK authoring; sparse keys; one initial key for stationary channels; per-character proportion scaling; in-session half-frame motion review; native visual deformation bake; per-animation file writer; GLB publisher; serialization of publication through a directory lock.
- The author reuses `RigYogaPoser`, `YogaPoseLibrary`, and `DiscoWristPoser` from the existing yoga/disco workflows. Existing disco motion was inspected; its calibration and posing helpers were reused rather than relabeling the disco routine as jazz.
- `scripts/solo_jazz/preview.py`: Blender Workbench contact-sheet renderer. Its sole completed image is the earlier Man Charleston prototype. Rendering is stopped.
- `scripts/solo_jazz/verify_saved.py`: reads saved action families, checks role/slot/range, evaluates source and baked poses, and checks common pose and loop endpoints. `--existing` limits it to durable current files. It deliberately reports the current fidelity failures.
- `scripts/solo_jazz/test_playback.gd`: reads the preserved catalog and checks actual Godot import, duration, loop policy, participant skeletons, and model target paths. It deliberately reports the current Man morph-path failures.
- `scripts/solo_jazz/catalog.json`: durable inventory and measurements for these 18 families.
- `.gitattributes`: exact-path regular-Git exceptions for this task's 36 `.blend`/`.glb` assets and one previously rendered PNG. The repository-wide rules and other tasks' assets retain their own attributes.
- `docs/animation_work_status/solo_jazz_evidence/`: preserved authoring logs, superseded review log, prototype render, attribute inspections, source/bake verification JSON and log, Godot playback log, Godot import log, test logs, and proposed registry snapshot. The superseded Woman review covered 81 in-memory candidates and found eight failures; it created no Woman source assets. Its results are historical evidence, separate from the final saved-file inventory.

Shared source files (`man_and_woman3.blend`, `shared_scene_data.blend`, and both anatomical source files) retain their saved pre-task contents. The combined library discovers new per-animation sources through the existing helper workflow. There is no newly saved combined library, shared-rig change, or complete repertoire export.

## Verification results and concrete blockers

1. **Fast suite: 9/9 passed**, after downloading three pre-existing Git LFS hair mesh prerequisites and using the installed Godot 4.7.2 executable. Command: `GODOT=/workspace/.cloud-onboarding/bin/godot BLENDER=/home/agent/.local/bin/blender python tests/run_tests.py --suite fast`.
   After rebase, the updated fast suite passed **10/10 checks** in 6.24 seconds; its added Godot test harness check is included in `solo_jazz_evidence/rebased_fast_suite.log`. The repository-wide `python scripts/lfs_policy.py check` passed for 23,517 staged files.
2. **Per-animation file workflow fixture passed** under Blender 5.2.2: `blender -t 2 -b --factory-startup --python-exit-code 1 --python scripts/player_assets/test_animation_files.py`.
3. **In-session motion checks passed for the 18 saved studies**: 195 samples per clip, including half frames, foot-plant and reach errors, wrist bend, hand/torso proxy clearance, toe height, foot separation, and loop endpoint/velocity checks. These establish the recorded proxy measurements, rather than complete mesh clearance or finished dance quality. The prototype log supplies the Man Charleston record; stopped authoring logs and the catalog supply the other 17.
4. **Fresh-load verification failed for all 18 baked/source comparisons.** The saved families are readable and correctly bind one actor each. Source loop endpoints and shared ready seams passed (Man maximum ready-seam displacement approximately 0.000000963 m; Woman zero). Source/bake disagreement reaches **0.057486704 m and 2.043296099 radians**, concentrated in finger deform bones such as `DEF-f_middle.03.L`. The author changes finger control rotation modes in the working rig; persistence of those modes against the shared scene is a concrete item to investigate. The definitive mechanism remains to be confirmed. The in-session bake check had passed, making fresh-load evaluation essential. Command: `blender -t 2 -b animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/solo_jazz/verify_saved.py -- --existing`.
5. **Godot import completed**, with existing UID warnings. **Playback target verification failed:** 574 unresolved morph target checks, 82 in each of the seven Man GLBs. Examples include `Man_rigify_deform/Skeleton3D/Man_Man_Male_Gen-Heal12:!ex-eyeBlinkRight`. The eleven Woman clips produced no failures in that target/duration/loop test. Character skeleton tracks, durations, and loop policies produced no failures. Command: `/workspace/.cloud-onboarding/bin/godot --headless --path . --script scripts/solo_jazz/test_playback.gd`.
6. **Related-suite attempt:** the default selected suite was invoked with `GODOT=/workspace/.cloud-onboarding/bin/godot BLENDER=/home/agent/.local/bin/blender python tests/run_tests.py --slow-timeout 60`. The broad selection was interrupted for stop-and-deliver after 40 passing checks, 0 failing checks, and 41 started checks. It has no overall passing result. Its remaining checks are outstanding; the focused serialized-asset and Godot checks above are the relevant completed failure evidence. See `solo_jazz_evidence/interrupted_related_suite.log`.
7. **Environment prerequisites:** Game Rig Tools is absent from Blender 5.2 preferences, and the full-library `.animation_cache` was initially absent. This prototype therefore used Blender's native visual bake and the existing `AnimationClipScene`, `AnimationFileWriter`, and `AnimationUpdates` publication pieces. The subsequent rebase brought in the bundled Game Rig Tools setup at `scripts/blender/install_animation_tools.py`; use that setup with Blender 5.2 after a later resume instruction. Reconcile this prototype with the normal Action Bakery/export-cache workflow before production use. Every animation source and model prerequisite used here was downloaded through the existing Git LFS authentication path. Credential values are omitted from all evidence.

## Processes and saved stopping point

Owned generation PIDs **2342 (Man)** and **2355 (Woman)** received SIGTERM at the user's stop instruction. Man had finished `boogie_drop` and was proceeding toward `charleston_basic`; the earlier complete Man Charleston prototype remains saved. Woman had finished `kick_ball_change_left` and was proceeding toward the next figure. There are no extra in-memory poses counted as saved output. Both final logs end with their last completed publish records.

Earlier experimental and review processes had already exited or been terminated. The initial broader test attempt was interrupted to hydrate/import existing dependencies. The later broad verification runner and its owned child were terminated for delivery. Focused verification and import processes have exited. No task-owned Blender authoring, rendering, or verification process remains active.

Local working logs remain in `/tmp/jazz-*.log`; durable relevant copies accompany this record. `.cache/solo_jazz/review/` contains the last per-clip session reports; `.cache/solo_jazz/saved_validation.json` contains fresh-load results. The Git-tracked catalog and evidence preserve the required results across environment deletion. Temporary Git askpass configuration reads the bound token at runtime and is excluded from the repository.

## Remaining work and exact resume commands

First inspect the catalog, saved-source failure JSON, and playback failure log. Resolve finger rotation-mode/action persistence, then resolve duplicated Man morph target names against the real composed model. Preserve all unrelated clips and shared assets during those repairs. Validate any repairs after reopening sources and through Godot. Continue choreography and actual surface/visual review only after an explicit instruction to resume. Then author the remaining figures, positions, and transitions, validate every saved result, and coordinate active-registry publication.

From the repository's `apps/a-game` directory, verification commands for the present state are:

```bash
blender --version
GODOT=/workspace/.cloud-onboarding/bin/godot BLENDER=/home/agent/.local/bin/blender python tests/run_tests.py --suite fast
blender -t 2 -b animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/solo_jazz/verify_saved.py -- --existing
/workspace/.cloud-onboarding/bin/godot --headless --editor --import
/workspace/.cloud-onboarding/bin/godot --headless --path . --script scripts/solo_jazz/test_playback.gd
```

After later authorization and the documented repairs, a targeted authoring command is:

```bash
blender -t 2 -b animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/solo_jazz/author.py -- --character Man --filter charleston_basic
```

Use `--character Woman` for the other actor; `--review-only` evaluates candidates without saving source/GLB assets. Omit `--filter` only for an intentionally authorized whole-character rebuild: the current author overwrites matching per-animation paths. Rebuild the catalog against actual saved outputs before using playback verification for a larger repertoire. `verify_saved.py` without `--existing` requires the complete planned repertoire.

## Storage and integration

All 37 task binary files are at or below **104,857,600 bytes**; their combined size is **14,974,856 bytes**, with the largest file **1,541,938 bytes** (the earlier prototype PNG). All are stored directly in Git, using exact-path overrides inspected before staging. There are **zero new LFS payloads** for this task. Existing LFS objects remain managed by the repository's configured upload hook.

The preserved asset/status commit after the first rebase is `8e2f2adcc`. The first rebase retained concurrent upstream work through `0868c8076`. Delivery uses a task commit with exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer, followed by fetch/rebase onto current `origin/main`, the concise Animation-section documentation commit, and ordinary-history-preserving integration/push. Concurrent status records, animation sources, and storage exceptions must all be retained. The final chat response reports the task/documentation/merge commit hashes and verified remote main hash; a file cannot record its own commit hash without another commit. GitHub commit communications are authored by Codex.
