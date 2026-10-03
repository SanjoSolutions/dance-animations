# Chicken Dance animation work checkpoint

- Date: October 2, 2026 (Europe/Berlin).
- Chat/task title: Chicken Dance solo animations for man_and_woman3.blend (descriptive task title).
- Project: A-Game, `apps/a-game`, sanjo-solutions cloud environment.
- Task branch: `codex/chicken-dance`.
- Starting/current commit at the stop instruction: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- State: animation work stopped immediately on the user's delegated instruction. This is a preservation checkpoint, with partial procedural blocking studies rather than finished production animations.
- GitHub communications and these checkpoint commits are authored by Codex.

## Original scope and stopping point

The original request covered the complete Chicken Dance vocabulary, positions, transitions, and solo routines for both characters in `man_and_woman3.blend`, with Blender 5.2 throughout, per-animation source files, reuse of suitable existing dance motion, planted contacts, clearance, interpolated-motion and loop validation, exports, documentation, commits, rebase, and a main push. The later stop instruction prioritizes recording and delivering the present state over further authoring or refinement.

All 32 editable sources have been generated. One source, `man_chicken_dance_claps.blend`, also contains its matching native Blender visual bake and has an individual GLB export. The remaining 31 sources contain authoring actions only. The complete routines and the individual gestures are procedural drafts. Full rendered-motion review, surface contact review, exported-motion equivalence, and Godot playback acceptance remain outstanding.

The combined library `man_and_woman3.blend`, `shared_scene_data.blend`, and the two anatomical source models retain their original Git contents. New sources use the existing `AnimationFileWriter`, shared-scene descriptor, action-slot, and source-discovery workflow. The installed Player Asset Export loader points at this checkout. Game Rig Tools is absent from the environment. The task exporter uses Blender's native `bpy_extras.anim_utils.bake_action_objects` visual bake, then the existing `AnimationClipScene`, participant metadata, and `AnimationUpdates` publisher. This path still needs comparison with the repository's usual Action Bakery export before production acceptance.

## Files and authored states

Timing is 24 fps and 120 BPM (12 frames per beat). Frame ranges below include the repeated endpoint for loops. Man actions use only the `Man.rigify` slot and `PLAYER`; Woman actions use only `Woman.rigify` and `PARTNER`. The Man clap bake uses `Man.rigify_deform`. Each row is one exact project-relative source path.

| Source | Role | Frames | Playback | Saved state | Current landmark result |
| --- | --- | --- | --- | --- | --- |
| `animations/man_and_woman/man_chicken_dance_beaks.blend` | PLAYER | 0–48 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/man_chicken_dance_beaks_to_wings.blend` | PLAYER | 0–24 | Transition | Authored draft | Proxy checks pass |
| `animations/man_and_woman/man_chicken_dance_chorus.blend` | PLAYER | 0–192 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/man_chicken_dance_circle_left.blend` | PLAYER | 0–96 | Loop | Authored draft | loop continuity |
| `animations/man_and_woman/man_chicken_dance_circle_right.blend` | PLAYER | 0–96 | Loop | Authored draft | loop continuity |
| `animations/man_and_woman/man_chicken_dance_claps.blend` | PLAYER | 0–48 | Loop | Authored + baked + GLB | Proxy checks pass |
| `animations/man_and_woman/man_chicken_dance_claps_to_beaks.blend` | PLAYER | 0–24 | Transition | Authored draft | Proxy checks pass |
| `animations/man_and_woman/man_chicken_dance_entry.blend` | PLAYER | 0–24 | Transition | Authored draft | Proxy checks pass |
| `animations/man_and_woman/man_chicken_dance_exit.blend` | PLAYER | 0–24 | Transition | Authored draft | Proxy checks pass |
| `animations/man_and_woman/man_chicken_dance_full_routine.blend` | PLAYER | 0–384 | Loop | Authored draft | loop continuity |
| `animations/man_and_woman/man_chicken_dance_ready.blend` | PLAYER | 0–48 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/man_chicken_dance_step_touch.blend` | PLAYER | 0–96 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/man_chicken_dance_wiggle.blend` | PLAYER | 0–48 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/man_chicken_dance_wiggle_to_claps.blend` | PLAYER | 0–24 | Transition | Authored draft | Proxy checks pass |
| `animations/man_and_woman/man_chicken_dance_wings.blend` | PLAYER | 0–48 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/man_chicken_dance_wings_to_wiggle.blend` | PLAYER | 0–24 | Transition | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_beaks.blend` | PARTNER | 0–48 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_beaks_to_wings.blend` | PARTNER | 0–24 | Transition | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_chorus.blend` | PARTNER | 0–192 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_circle_left.blend` | PARTNER | 0–96 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_circle_right.blend` | PARTNER | 0–96 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_claps.blend` | PARTNER | 0–48 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_claps_to_beaks.blend` | PARTNER | 0–24 | Transition | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_entry.blend` | PARTNER | 0–24 | Transition | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_exit.blend` | PARTNER | 0–24 | Transition | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_full_routine.blend` | PARTNER | 0–384 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_ready.blend` | PARTNER | 0–48 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_step_touch.blend` | PARTNER | 0–96 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_wiggle.blend` | PARTNER | 0–48 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_wiggle_to_claps.blend` | PARTNER | 0–24 | Transition | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_wings.blend` | PARTNER | 0–48 | Loop | Authored draft | Proxy checks pass |
| `animations/man_and_woman/woman_chicken_dance_wings_to_wiggle.blend` | PARTNER | 0–24 | Transition | Authored draft | Proxy checks pass |

The ready stance, beak opening/closing, wing up/down positions, squat/wiggle positions, and clap opening/contact positions belong to the gesture clips. The 16-beat chorus orders beaks, wings, wiggle, claps. The 32-beat routine appends clockwise/counterclockwise solo turning phrases. `step_touch` reuses the existing `DiscoChoreography.retrieve_feet` mechanics; posing/proportion setup composes `DiscoCharacter` and `RigYogaPoser`. Standalone two-beat transitions connect the four gestures and provide entry/exit.

Other durable files:

- `scripts/create_chicken_dance.py`: current procedural authoring implementation; partial draft with known turn-loop issues. Rebuilding sources overwrites their saved bakes, so preserve the checkpoint before a future rebuild.
- `scripts/player_assets/export_chicken_dance.py`: half-frame landmark review, native visual baking, per-source saving, and individual export. `-- --review-only` runs verification and writes reports; ordinary invocation also bakes/exports. The process raises on reported motion failures.
- `docs/chicken_dance_validation/*.json`: 32 per-action review reports, one for every source listed above. These contain measured values, sample counts, Blender version, and error lists. Some reports include the later per-bone velocity diagnostic; all use the final 0.01-frame boundary derivative estimate. Only the Man clap report carries an export path.
- `models/player/animation_updates/man_chicken_dance_claps_baked_e80ad0a2a7d0.glb`: sole exported task clip, `man_chicken_dance_claps.baked`, 639 channels, 2 seconds, one Man deform-rig hierarchy. Static inspection confirms the export contains only this clip.
- The adjacent `.glb.import`: animation-library importer, explicit loop mode 1, existing player animation import script.
- `models/player/animation_updates.tres`: integration preserves the concurrent main registry. The clap export remains a checkpoint asset pending runtime track and morph-target acceptance. Its original proposed registry is preserved in `docs/animation_work_status/chicken_dance_evidence/proposed_animation_updates.tres`; activation is deferred under the newer repository guidance.
- Storage integration: the original checkpoint used exact-path exceptions for 34 task binaries. Rebase encountered the newer generated size-based `.gitattributes` policy on main; its canonical contents were preserved and the superseded task exceptions were dropped. All task binaries remain full ordinary Git blobs. `python scripts/lfs_policy.py check` passed after conflict resolution.
- `docs/animation_work_status/chicken_dance_evidence/source_inventory.json`: Blender 5.2.2 read-only inventory of source action names, slots, roles, ranges, and file sizes.
- `docs/animation_work_status/chicken_dance_evidence/storage_inventory.json`: exact binary paths, actual byte counts, SHA-256 checksums, and Git attributes before/after the original scoped exceptions, plus `integration_attributes` under the newer main policy. There are 34 binary artifacts totaling 4,075,630 bytes; the largest is 329,392 bytes.
- `docs/animation_work_status/chicken_dance_evidence/export_inventory.json`: static GLB clip/channel/duration/rig summary.
- `docs/animation_work_status/chicken_dance_evidence/early_clap_review.png`: preserved early Blender Workbench image, before calibrated-palm refinement. This is evidence of an earlier blocking pose and does not represent the final saved clap geometry.
- The evidence directory also preserves `author-man.log`, `author-woman.log`, `batch-review.log`, `export-test.log`, `fast.log`, `fast_final.log`, `related-tests.log`, and `selected-tests.log`.

## Validation and limitations

All Blender work used **Blender 5.2.2 LTS**, build `d13f752e3b9c`. The installed Godot executable is **4.6.3**, while repository workflow documentation discusses 4.7.2.

- Authoring completed for all 32 sources; see both author logs.
- Half-frame deform-landmark sampling completed for all 32 actions: 29 pass the implemented checks; three Man clips fail loop continuity: `circle_left` (0.2141402 m/s boundary velocity difference), `circle_right` (0.2131113 m/s), and `full_routine` (0.2140427 m/s). The left-circle diagnostic locates the remaining mismatch in both feet. Endpoint poses match; foot velocity needs refinement. The Woman counterparts pass the current numeric test.
- Stationary-foot checks and control-to-deform IK checks are implemented. The torso check uses a labeled ellipsoid proxy. These checks do not establish complete mesh clearance, finger separation, wrist comfort, actual palm contact, or natural rendered motion. Moving-foot support intervals are not yet independently measured: their report field `maximum_plant_drift=0` is a placeholder associated with `stationary_feet=false`, rather than proof of planted turning/stepping contacts. Loop angular velocity, intra-phrase speed continuity, and baked/source equivalence remain pending.
- The initial half-frame loop derivative check overestimated curvature-related discontinuity; final reports use additional 0.01-frame boundary samples. Authored endpoint handles were adjusted before the stop instruction.
- The single Man clap export completed. `use_active_scene=True` was required to prevent glTF from including authoring actions from other scenes; the final static GLB check confirms a single baked clip. The obsolete temporary diagnostic GLB is excluded from the checkpoint.
- `python tests/run_tests.py --suite fast`: an earlier run passed **9/9** (`fast.log`). The required rerun after stopping passed **8/9** (`fast_final.log`): `playground/activity_import/test_activity_json.gd` reports missing existing imported hair GLBs (`bob01`, `bob02`, `short01`–`short04`, `afro01`) and dependent class compilation errors. A related editor test refreshed import state in this partially hydrated checkout. This final fast result is recorded as an environmental failure, not a pass.
- `python tests/run_tests.py --list`: selected 9 fast and 57 related slow checks (`selected-tests.log`).
- `python tests/run_tests.py --slow-timeout 90`: started before the stop instruction and terminated during `playground/test_animation_metadata_saving.gd`. Earlier results included an exit-0-but-engine-error failure for `models/player/test_model_animation_player.gd`, passes for activity configuration and endpoint audio, and a 90-second timeout for activity methods. Errors concern existing LFS/import prerequisites, including prior animation `.res` assets and `models/player/animations.glb` import state. The related suite is incomplete; see its full saved log. The temporary 90-second cap belongs to this attempted run; normal resume uses repository defaults.
- Read-only source inspection loaded only action datablocks with Blender 5.2.2; all 32 source files are readable. It confirmed exactly one author action per source, plus the sole clap bake.

## Processes and preserved state

Both authoring processes, the 32-clip review batch, and the single-clip export had finished when the stop instruction was processed. The owned related-test runner (PID 1883, process group 1880) and its Godot editor child (PID/process group 2380) were terminated with SIGTERM. No task animation authoring, baking, rendering, or export process remains running. A post-stop read-only inventory and the required fast rerun completed. No additional animations were generated after the stop instruction.

Transient session logs and the credential helper were under `/tmp/chicken-dance`; durable outputs are copied into the evidence directory. Credential values are excluded. Existing LFS assets were hydrated for inspection, with no intended content changes. Godot-generated changes to unrelated import settings and `playground/eyes/player_eyes.res` were restored to their original Git content.

## Remaining work and concrete resume commands

Resume authoring only after a new user instruction. First restore the repository's required Godot import prerequisites. The fetched main now bundles Game Rig Tools; follow `scripts/blender/README.md` and run `blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py` with the chosen Blender 5.2 profile before resuming. Reopen each source with Player Asset Export enabled, using Blender 5.2. Confirm the editable action and sole participant before changing it.

From the repository root:

```bash
cd apps/a-game
blender --version
python tests/run_tests.py --suite fast
# Inspect current review results before any regeneration.
cat docs/chicken_dance_validation/man_chicken_dance_circle_left.json
# Read-only motion verification of a saved source; writes its diagnostic JSON.
blender -b animations/man_and_woman/man_chicken_dance_circle_left.blend --python-exit-code 1 --python scripts/player_assets/export_chicken_dance.py -- --review-only
```

After correcting the Man foot-loop tangents and independently checking support intervals, wrists, fingers, calibrated claps, body surfaces, full routines, and transitions in rendered playback, selectively regenerate and validate the affected files. These are destructive-to-current-source rebuild commands, so use a clean committed checkout and preserve the current bake first:

```bash
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/create_chicken_dance.py -- --actor man --clips circle_left circle_right full_routine
# The same author accepts --actor woman and an explicit --clips list.
# Once the saved clip passes review and the native-bake path is approved by comparison:
blender -b animations/man_and_woman/man_chicken_dance_claps.blend --python-exit-code 1 --python scripts/player_assets/export_chicken_dance.py
python tests/run_tests.py
```

Complete the remaining 31 bakes/exports through the established per-animation workflow, verify source/bake/GLB motion equivalence and Godot roles/loops, then inspect actual binary sizes and `git check-attr` before staging. Coordinate updates to the shared `animation_updates.tres` by preserving the union of current entries. The work is a saved draft checkpoint, with production acceptance explicitly outstanding.

## Integration findings

Rebase preserved main's generated size-based storage policy. The rebased task checkpoint is `bc02fc919971c7169b3a6e8b9a983caaa7f10566`, based on fetched main `18e528c73`. `integration_dependencies.json` records that the shared scene and all three linked model/prop dependencies have identical SHA-256 contents before and after integration. No animation was regenerated during integration.

New main guidance identifies another concrete blocker: the saved Rigify finger controls use quaternion rotation modes, while this draft author keys Euler finger channels in its temporary scene. Action-only source saving preserves the action, rather than that temporary rotation-mode change. Finger/beak playback after fresh source loading therefore needs explicit verification and likely quaternion-channel correction before acceptance. This was recorded rather than repaired because authoring is stopped.

After rebase, `python tests/run_tests.py --suite fast` selected the newer 10-check catalog and passed **9/10**. The remaining failure is the same existing hair-import prerequisite in `playground/activity_import/test_activity_json.gd`; `fast_after_rebase.log` preserves the full output. `python scripts/lfs_policy.py check`, Python syntax compilation for both task scripts, and `git diff --check` pass. The dependency fingerprints and all 34 indexed binary byte counts were also verified.

The final pre-merge main fetch used `--filter=blob:none` after a large unfiltered transfer was stopped. Git tree merging preserves incoming asset references and published history while requiring only conflict-related blob payloads. Concurrent main guidance now keeps unverified exports outside the active registry; the saved clap GLB and original proposed registry remain durable evidence, with activation deferred.

The documentation update adds active-scene GLB isolation and explicit moving-foot validation coverage to the `# Animation` section of `AGENTS.md`.

## Delivery record

This file and all durable task artifacts are committed together, followed by the requested small `AGENTS.md` animation guidance update. Main integration fetches the latest `origin/main`, preserves concurrent work, uses ordinary pushes, and verifies task-commit ancestry and the pushed main SHA. Exact resulting commit hashes and push verification are reported in the chat final response because a commit cannot include its own final hash.
