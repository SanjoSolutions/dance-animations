# K-pop Neon Practice — stopped animation work

- Date: October 2, 2026 (Europe/Berlin). Authoring terminated around 16:55 CEST.
- Chat: Create K-pop choreography animations (`01a0fd09-6a8f-7656-9e07-c7bfafbdb04e`).
- Environment/project: sanjo-solutions cloud, A-Game, `/workspace/sanjo-solutions/apps/a-game`.
- Task branch: `codex/kpop-solo-repertoire`.
- Commit at the stopping point: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Delivery author: Codex. The preservation commit containing this record identifies the task snapshot; integration hashes are reported in chat after pushing.
- State: **partial procedural blocking studies; motion acceptance remains blocked**. The user explicitly stopped every animation chat and prioritized preservation, recording, committing, and pushing. Further authoring and rendering require a renewed instruction.

## Requested scope and chosen repertoire

The original request covered a broad, organized song-specific K-pop choreography category, separate solo animations for both characters from `man_and_woman3.blend`, natural motion, planted contacts, body clearance, interpolation and loop review, existing-animation reuse, Blender 5.2 throughout, per-animation source files, exports, documentation, and delivery to main. The user selected **Original K-pop repertoire** rather than named songs or supplied choreography references.

The working title is **Neon Practice**, an original practice arrangement at 120 BPM, with six song sections and 24 planned eight-count phrases per character. This is an original category repertoire; there is no associated audio file or claim to reproduce a released song. The planned 48 clips comprise intro, verse, pre-chorus, chorus, dance break, and ending phrases. Dance vocabulary is open-ended; this plan is a bounded repertoire.

## Exact saved state

There are **41 authored sources, 41 native-baked matching actions, 41 GLB exports, 41 import settings, and 41 live-motion JSON reports**: all 24 planned man clips and 17 woman clips. Every saved clip spans frames **0–96 inclusive**, 24 FPS, eight beats/four seconds, with an endpoint pose intended for looping. Each source contains a single authoring action and matching `.baked` action. Man uses `PLAYER` / `Man.rigify`; woman uses `PARTNER` / `Woman.rigify`. The other character contributes no action slot to that source.

`animations/man_and_woman/shared_scene_data.blend` supplies the shared rigs through the existing `AnimationFileWriter` workflow. This task leaves the shared scene, `man_and_woman3.blend`, and anatomical source assets unchanged. Library discovery occurs on reopening the combined file. `models/player/animation_updates.tres` referenced the 41 partial libraries at the stopping point. During integration, the current repository guidance required preserving failed exports behind `.gdignore`: the 41 GLBs and their import settings now live in `animations/kpop_neon_practice/exports/`, and the active runtime registry retains concurrent main entries while excluding these failed task exports. Binary bytes are unchanged; the inventory records both final and original stopping paths. Authored sources remain in the existing per-animation source directory, which already has `.gdignore`.

The first generation stopped after the woman's `arm_roll`. A later correction regenerated 17 man clips, through `arm_roll`, before the stop instruction. The remaining seven man clips and all 17 woman clips preserve the earlier generator revision. The table identifies this mixed state. **Current scripts and every saved binary are not yet a reproducible final set.**

The seven planned woman clips with no saved asset are: `knee_lift`, `toe_tap`, `wide_lunge`, `low_groove`, `diagonal_reach`, `ending_pose`, and `bow_release`.

[Exact asset inventory](kpop_neon_practice_evidence/asset_inventory.json) records every source, GLB, import file, report path, byte count, SHA-256, role, frame range, and generator revision. Paths in that inventory are repository-relative. Each table name resolves to `animations/man_and_woman/<name>.blend` and `animations/kpop_neon_practice/<name>.json`; the inventory supplies each hashed GLB filename.

| Clip name | Role | Last generation |
| --- | --- | --- |
| `man_kpop_neon_arm_roll` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_arm_wave` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_body_wave` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_bow_release` | PLAYER | Earlier blocking revision |
| `man_kpop_neon_cross_open` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_diagonal_point` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_diagonal_reach` | PLAYER | Earlier blocking revision |
| `man_kpop_neon_ending_pose` | PLAYER | Earlier blocking revision |
| `man_kpop_neon_face_frame` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_forward_rock` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_heart_frame` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_hip_sway` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_knee_lift` | PLAYER | Earlier blocking revision |
| `man_kpop_neon_low_groove` | PLAYER | Earlier blocking revision |
| `man_kpop_neon_point_hook` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_punch_reach` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_ready_groove` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_rising_v` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_shoulder_accents` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_side_reach` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_step_touch` | PLAYER | Corrected rotation modes / relaxed fingers |
| `man_kpop_neon_toe_tap` | PLAYER | Earlier blocking revision |
| `man_kpop_neon_wide_lunge` | PLAYER | Earlier blocking revision |
| `man_kpop_neon_wrist_flick` | PLAYER | Corrected rotation modes / relaxed fingers |
| `woman_kpop_neon_arm_roll` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_arm_wave` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_body_wave` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_cross_open` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_diagonal_point` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_face_frame` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_forward_rock` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_heart_frame` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_hip_sway` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_point_hook` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_punch_reach` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_ready_groove` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_rising_v` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_shoulder_accents` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_side_reach` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_step_touch` | PARTNER | Earlier blocking revision |
| `woman_kpop_neon_wrist_flick` | PARTNER | Earlier blocking revision |

## Implementation and reuse

- `scripts/player_assets/kpop_choreography.py`: organized phrase specification, section lists, timing, foot and hand targets, common transition stance. Reuses the existing `DiscoChoreography` step-touch and arm-roll mechanics.
- `scripts/player_assets/author_kpop.py`: uses `DiscoCharacter` for per-character proportion adjustment, IK posing, and the existing wrist solver. Authors meaningful half-beat keys; stationary channels retain one initial key. Native `bpy_extras.anim_utils.bake_action_objects` supplied a cloud fallback because Game Rig Tools was unavailable. Writes through existing `AnimationFileWriter`, `AnimationClipScene`, and `AnimationUpdates`. This fallback has outstanding bake-fidelity failures.
- `scripts/player_assets/review_kpop.py`: read-only saved-source motion checks, optional diagnostic renders, all-deform-bone source/bake comparisons and angular loop diagnostics. Its render option was created before the stop; subsequent verification used it with rendering disabled.
- `animations/kpop_neon_practice/*.json`: per-clip live-authoring metrics at 193 half-frame samples. Their `passed` value covers that live run only. These reports are insufficient to certify saved sources or game exports.
- Three task-scoped `.gitattributes` files enumerate the intended small binaries. Each Blender/GLB file is below 1 MiB; all 82 source/export binaries total 51,141,531 bytes. Largest source: 863,614 bytes. The preserved PNG is also below the 104,857,600-byte threshold. These task assets use ordinary Git. Existing LFS assignments stay with existing assets.

## Validation and blockers

All Blender work used **Blender 5.2.2 LTS**, build `d13f752e3b9c`. `Player Asset Export` was installed from this checkout. Godot is 4.7.2. Referenced assets were restored through Git LFS with the configured `SANJO_GITHUB_LFS_TOKEN` binding and the prescribed GitHub account; credential values were kept outside logs.

Commands run from `apps/a-game`:

```bash
python tests/run_tests.py --suite fast
BLENDER=/home/agent/.local/bin/blender GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_animation_file_export.py --changed scripts/player_assets/test_single_animation_layout.py
blender --background --python-exit-code 1 --python scripts/player_assets/review_kpop.py
```

- Stop-time required fast suite: **9/9 passed**. The first run was 8/9 because three hair `.res` assets were LFS pointers; restoring those assets resolved it.
- Focused suite: **11/12 passed** (nine fast plus two workflow checks). `test_animation_files.py` and `test_single_animation_layout.py` passed. `test_animation_file_export.py` failed at its Game Rig Tools lookup with `StopIteration`; that add-on is missing in this environment.
- GLB structural verification: **41/41 passed** for complete GLB header, single expected clip, and four-second duration. See [structural results](kpop_neon_practice_evidence/glb_structure.json). Game runtime playback and full visual acceptance remain pending.
- Live pose sampling passed each saved clip's local thresholds for foot targets, hand reach, wrist bend, torso-proxy clearance and endpoint continuity. Sparse keys were sampled at half-frame intervals. These are landmark/proxy checks, not exhaustive surface collision or choreography-quality proof.
- Stopped-snapshot saved-source validation: **0/41 accepted**. All 41 were measured at 193 half-frame samples across every deform bone. See the final saved review JSON and log. Maximum recorded position discrepancy is 0.075455 m; maximum rotation discrepancy is 2.644985 rad.
- Saved-source validation fails bake fidelity. The earlier revision changed finger rotation modes in memory while writing only animation channels; reopening a per-animation file restores the shared rig's modes. The corrected builder converts the posed matrix back into each original mode before capturing channels. Seventeen man clips include this correction and revised relaxed fingers.
- A corrected man face-frame sample still showed up to **0.00877 m** position discrepancy and **0.02184 rad** rotation discrepancy between the source and unconstrained native bake. Earlier woman face-frame showed **0.03891 m** and **1.26190 rad**, especially fingers. These figures are intermediate diagnostics; the stopped-snapshot report records each current asset's result.
- The diagnostic experiment disconnecting deform joints did **not** resolve the remaining approximately 7.5 mm toe discrepancy. Its transient edit existed only in a separate Blender process; shared rigs and saved assets remain unchanged by that experiment. Treat the cause as unresolved.
- Loop endpoints matched in sampled checks, but endpoint agreement alone does not accept the bake, finger shapes, contacts, surface clearance, or visual motion.
- The default broad change selector listed nine fast and 186 slow checks. The focused suite above covered the per-animation file/layout work; the full 186-check suite was not run. Full-library tests additionally require installed Game Rig Tools and the complete configured scene.

## Processes, outputs, and evidence

Owned authoring process PID 2278 received SIGTERM immediately after the stop instruction. Its last fully published/saved clip was `man_kpop_neon_arm_roll`. Earlier generation PID 1415 was terminated during refinement. No further animation authoring, refinement, export, or rendering occurred after the stop instruction. The post-stop Blender process only reopened and measured existing sources. All owned Blender processes have completed or been terminated by delivery.

Evidence lives in `docs/animation_work_status/kpop_neon_practice_evidence/`:

- `build_all.log`, `build_final.log`: initial and partial corrected build provenance.
- `saved_review.log`: intermediate two-clip reopen failure.
- `stop_saved_review.log`, `saved_review.json`: final read-only check of the 41 stopped assets.
- `bake_debug.py`, `bake_debug.log`, `bake_disconnect.py`, `bake_disconnect.log`: diagnostic scripts and outputs, including the unsuccessful disconnected-joint experiment.
- `stop_fast.log`, `stop_verification.log`: required and focused verification results.
- `render.log`, `initial_blocking_study.png`: **one initial procedural blocking render**, produced before the stop. It includes overlapping preview/body surfaces and was used to diagnose viewport selection; it is not a final choreography preview. No contact sheet or playback movie was completed.
- `asset_inventory.json`, `glb_structure.json`: precise file provenance and structural results.

Temporary runtime scripts/logs originally lived under `/workspace/scratch/kpop`. The durable evidence above preserves the useful outputs. The temporary Git askpass helper reads the configured credential variable and contains no credential value; it is outside Git. Downloaded existing assets and Blender preferences are environment setup, not task changes.

## Remaining work and exact resume commands

Resume authoring only after a renewed user instruction. First install/enable the project's Game Rig Tools version when available, then resolve native bake fidelity or return to the standard Action Bakery path. Reconcile the 17 corrected sources with the older 24 sources, generate the seven missing woman sources, and rerun all saved-file checks. Complete actual surface/body clearance review, grounded sole checks, interpolated fingers and wrist review, visual playback, and transition acceptance. The earlier `step_touch` and `side_reach` were identical; the current builder distinguishes them, but only corrected man files include that refinement. The widened-lunge specification was added to code, while the saved wide-lunge file still reflects the earlier revision. Full song arrangement playback and audio binding remain future work.

Read-only reproduction:

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender --version
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
blender --background --python-exit-code 1 --python scripts/player_assets/review_kpop.py
blender --background animations/man_and_woman/man_kpop_neon_face_frame.blend --python-exit-code 1 --python docs/animation_work_status/kpop_neon_practice_evidence/bake_debug.py
python tests/run_tests.py --suite fast
```

The saved-source review is expected to fail at the current state and writes measurements to `.cache/player_assets/kpop_review/saved_review.json`. Opening a source with the add-on composes the shared editable scene.

Future authoring commands, **only after the renewed instruction and resolving blockers**:

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/player_assets/author_kpop.py -- --character man --move face_frame
blender --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/player_assets/author_kpop.py
blender --background --python-exit-code 1 --python scripts/player_assets/review_kpop.py -- --render
```

These authoring commands overwrite matching task files and update `animation_updates.tres`. Use an isolated branch, inspect the task's existing files, and preserve concurrent catalog entries. Review actual binary sizes and path-scoped Git attributes before staging. Commit with exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer, fetch and integrate current `origin/main`, use an ordinary history-preserving push, and verify remote containment.

## Integration verification update

The preservation snapshot rebased onto `origin/main` at `18e528c73` (the concurrent Game Rig Tools bundle), becoming task commit `bcaa4d4c0`. The sole add/add conflict in `animations/man_and_woman/.gitattributes` was resolved by retaining both task scopes. Concurrent main changes include a native bake reference in `scripts/player_assets/bachata_motion.py`; examine that existing implementation during a future authorized resume rather than inferring that the disconnected-joint experiment fixed this task.

The newly bundled Game Rig Tools and Player Asset Export were enabled with `blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py`. The focused verification command above then passed **13/13 checks**: the current main's ten fast checks plus all three selected Blender workflow fixtures, including `test_animation_file_export.py`. Evidence: `integration_setup.log` and `integration_verification.log`. This resolves the environment setup blocker recorded at the stopping point. It does **not** resolve or supersede the 41 saved-motion acceptance failures; the choreography sources and exports remain exactly the stopped snapshot.

`python scripts/lfs_policy.py check` passed for the integrated index. All task binaries remain ordinary Git blobs with byte counts matching the asset inventory. The separate documentation commit adds two guidance bullets to `# Animation` in `apps/a-game/AGENTS.md`, covering original song-category scope and all-deform-bone validation. Final merge and remote verification are reported in chat after the ordinary push.

### Final preservation layout

Integration against `e12670ea9` introduced newer repository guidance to archive failed exports behind `.gdignore`. The merge therefore relocated all 41 task GLBs and 41 import settings, byte for byte, to `animations/kpop_neon_practice/exports/`. This is preservation and runtime isolation, not animation refinement or generation. `animations/kpop_neon_practice/.gdignore` protects that archive. Concurrent main's `animation_updates.tres` was retained in full, and this task's failed exports have no active runtime registration. Source `.blend` files remain at their authored paths so their shared-scene descriptors keep resolving. The original stopping paths remain recorded in `asset_inventory.json` and task history. Future authoring commands still target the original runtime export directory and require reviewed motion before publication.
