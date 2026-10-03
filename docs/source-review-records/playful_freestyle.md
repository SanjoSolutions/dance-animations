# Playful freestyle animation preservation status

- Date: 2026-10-02 (UTC).
- Chat task/title: Create playful freestyle dance animations for man_and_woman3.blend. This is the task label; the exact desktop sidebar title was unavailable.
- Branch at stop: `work`.
- Commit at stop: `9ecd10e252a927153aeb3164e4a76bc293bf06d0` (`Add playful freestyle dance animation library`). It was rebased onto `57843e609` from `origin/main` before the stop instruction.
- Subsequent guidance commit: `ee036285d` (`Document reusable freestyle animation authoring guidance`).
- Instruction: stop animation authoring, refinement, generation, and rendering; preserve the present state and deliver it to main. This snapshot intentionally retains a failing saved-asset regression instead of continuing animation repair.

## Scope and delivery state

The original request was playful freestyle dance moves and positions for the existing Man and Woman rigs in `man_and_woman3.blend`. The saved repertoire contains 16 movement loops, six held positions, and one assembled routine. Freestyle is open-ended; this is a finite repertoire, not exhaustive coverage of every possible move.

**Partial procedural animation library / blocking study:** editable IK actions and per-frame deform bakes exist in all 23 sources. Saved finger channels use Euler curves while the current shared rig loads those controls in quaternion mode. The correction is incomplete. The assets require further saved-file and visual validation before final animation acceptance. There are no Godot runtime exports or published GLB payloads from this task.

The combined `man_and_woman3.blend` discovers these individual sources through the existing chooser. This task did not rewrite the combined library or shared scene. Both roles participate: `player` = `Man.rigify`, `partner` = `Woman.rigify`; matching baked slots target their `*.rigify_deform` rigs. Root X offsets are -0.9 and +0.9 meters. Each file contains the named editable action and its `.baked` action.

## Saved assets and timing

All filenames below are under `apps/a-game/animations/man_and_woman/`. Every row is authored and baked, with export state **none** and partial status as described above. The frame rate is 24 FPS and the choreography tempo is 120 BPM.

| File | Stored frames | Playback / role |
| --- | --- | --- |
| `playful_freestyle_bounce.blend` | 0–96 | 0–95; paired knee bounce |
| `playful_freestyle_step_touch.blend` | 0–96 | 0–95; paired side steps |
| `playful_freestyle_double_step.blend` | 0–96 | 0–95; two side steps and return |
| `playful_freestyle_forward_back.blend` | 0–96 | 0–95; forward/back steps |
| `playful_freestyle_v_step.blend` | 0–96 | 0–95; wide/narrow steps |
| `playful_freestyle_side_taps.blend` | 0–96 | 0–95; outward taps |
| `playful_freestyle_heel_digs.blend` | 0–96 | 0–95; heel accents |
| `playful_freestyle_knee_lifts.blend` | 0–96 | 0–95; alternating knees |
| `playful_freestyle_shuffle.blend` | 0–96 | 0–95; forward shuffles |
| `playful_freestyle_hip_sway.blend` | 0–96 | 0–95; lateral weight shifts |
| `playful_freestyle_shoulder_shimmy.blend` | 0–96 | 0–95; shoulder accents |
| `playful_freestyle_body_wave.blend` | 0–96 | 0–95; torso articulation |
| `playful_freestyle_arm_waves.blend` | 0–96 | 0–95; alternating arm arcs |
| `playful_freestyle_disco_points.blend` | 0–96 | 0–95; diagonal reaches |
| `playful_freestyle_step_turn.blend` | 0–96 | 0–95; 60-degree turn and return |
| `playful_freestyle_small_hops.blend` | 0–96 | 0–95; low hops |
| `playful_freestyle_pose_ready.blend` | 0–24 | held ready stance, both roles |
| `playful_freestyle_pose_wide.blend` | 0–24 | held wide stance, both roles |
| `playful_freestyle_pose_low.blend` | 0–24 | held low stance, both roles |
| `playful_freestyle_pose_diagonal_left.blend` | 0–24 | held left reach, both roles |
| `playful_freestyle_pose_diagonal_right.blend` | 0–24 | held right reach, both roles |
| `playful_freestyle_pose_celebration.blend` | 0–24 | held raised arms, both roles |
| `playful_freestyle_routine.blend` | 0–1536 | 0–1535; 64 seconds, 16 marked phrases in table order |

The last stored frame of each moving clip repeats its first pose. Held positions need authored entry/exit transitions. Phrase handles preserve individual clip interpolation across routine boundaries.

All 23 binaries match animation commit `9ecd10e25` byte-for-byte at stop. Their total size is 112,895,865 bytes; the largest individual file is 56,006,373 bytes. Each is below 100 MiB and stored as a full regular Git blob. No task asset requires an LFS upload. [The manifest](playful_freestyle_evidence/asset_manifest.json) records every asset's SHA-256, byte count, frames, and state, plus the shared/combined source hashes used at stop.

## Code, documentation, and evidence

Paths in this section are relative to `apps/a-game/`.

- `scripts/create_playful_freestyle.py`: reproducible procedural authoring, sparse keys, IK evaluation, baking, and routine composition. At stop, the finger setter was changed to quaternion mode. **That correction has not generated any replacement asset and remains unverified.**
- `scripts/player_assets/test_playful_freestyle.py`: saved-source, slot, motion, loop, bake, and combined-library checks. New Euler/mode compatibility assertions and finger deform comparisons expose the saved-source failure. The failure occurs before the remaining clip checks can run.
- `scripts/playful_freestyle.md`: catalog, playback, authoring, and testing commands. Its original validation description is historical; this status records the newer failed compatibility check.
- `animations/man_and_woman/README.md`: link to the freestyle guide, preserving the concurrent Tango catalog.
- `animations/man_and_woman/playful_freestyle_validation.json`: historical generation metrics for 22 individual clips; this is not evidence that the saved finger channels or assembled routine pass the new regression.
- `AGENTS.md`, Animation section: separate committed guidance on selecting the populated shared scene, sampling quick accents, and preserving Bézier handles while assembling phrases.
- `docs/animation_work_status/playful_freestyle_evidence/verification.log`: complete post-stop fast plus focused Blender test output.
- `docs/animation_work_status/playful_freestyle_evidence/stopped_conversion.log`: failed pre-stop conversion output.
- `docs/animation_work_status/playful_freestyle_evidence/stopped_conversion.py.txt`: exact abandoned temporary conversion attempt, retained as inert evidence. It assumes 48 finger channel groups but finds 64 in the first file. The assertion occurs before the write. Do not merely change its assertion or execute it as a repair; inspect all actual control modes and bake implications first.

## Verification and saved process state

Run from `apps/a-game/`:

```sh
python tests/run_tests.py --suite fast
python tests/run_tests.py --blender /tmp/blender-5.2.1-linux-x64/blender \
  --changed scripts/player_assets/test_playful_freestyle.py
```

- Post-stop explicit fast suite: **10/10 passed**, 6.18 seconds.
- Post-stop fast plus focused Blender suite: **10/11 passed**, 11.06 seconds; focused check failed with `('playful_freestyle_bounce', 'Man.rigify', 'f_index.01.L', 'saved rotation mode', 'QUATERNION')`.
- Blender: 5.2.1 LTS, build `9e2066aef7ef`. System Blender 4.3.2 is older than these sources; use the explicit executable above.
- Earlier pre-correction saved-file checks passed 11/11, but omitted finger rotation-mode compatibility. That earlier pass does not resolve the current failure.
- Historical generation report: maximum foot target error approximately 0.000235 meters; maximum wrist bend approximately 13.6 degrees; sampled loop endpoints matched. These measures do not establish skin clearance, final visual quality, or finger correctness.
- Earlier clay pose reviews covered knee lifts, arm waves, step turns, hops, heel digs, and shimmy with the visible replacement character meshes. Temporary review renders had been cleaned before the stop. No review render asset is being delivered.
- No live owned authoring, rendering, or test process remained at the preservation checkpoint. The converter failed on its first file, `playful_freestyle_arm_waves.blend`, before writing anything. Read-only hash comparison verified all 23 source binaries against their committed blobs.
- Root storage check `python scripts/lfs_policy.py check` passed for 23,297 staged files before the guidance commit. Repeat it after staging the status/evidence and during integration.
- The focused failure is a real asset compatibility issue, not an environmental blocker. The current user instruction requires preservation despite that failure.

## Remaining work and exact resume commands

Animation work is paused by explicit user instruction. Resume generation, repair, baking, export, or rendering only after the user authorizes animation work again.

1. Inspect all finger control rotation modes and channel groups in fresh loaded sources. Complete the generator correction, including any additional controls revealed by the abandoned converter's 64-group result.
2. Regenerate the affected authored actions and bakes together; check both roles and routine consistency. The present code change is ahead of the saved binaries.
3. Re-run the saved-source regression through completion, review finger poses and interpolation visually, and perform final movement/clearance review. Refine only after authorization.
4. Godot runtime export was not performed. If requested on resumption, follow `docs/player-animation-workflow.md` and record/export each validated source.

Read-only reproduction of the stopping point:

```sh
cd /workspace/sanjo-solutions/apps/a-game
python tests/run_tests.py --suite fast
python tests/run_tests.py --blender /tmp/blender-5.2.1-linux-x64/blender \
  --changed scripts/player_assets/test_playful_freestyle.py
cd /workspace/sanjo-solutions
python scripts/lfs_policy.py check
git diff --check
```

After renewed authorization and completing the generator correction, rebuild all clips and their routine with:

```sh
cd /workspace/sanjo-solutions/apps/a-game
/tmp/blender-5.2.1-linux-x64/blender --background --factory-startup \
  animations/man_and_woman/shared_scene_data.blend \
  --python-exit-code 1 --python scripts/create_playful_freestyle.py
python tests/run_tests.py --blender /tmp/blender-5.2.1-linux-x64/blender \
  --changed scripts/player_assets/test_playful_freestyle.py
```

The rebuild replaces the task's 23 sources and generation report. Compare new asset hashes and report results rather than carrying forward this snapshot's measurements. Delivery proceeds through a fresh fetch, ordinary merge into main, and ordinary push preserving concurrent animation chats. Final task and integration commit hashes and remote verification are reported in the delivery message; this file describes the preserved animation state.

## Integration verification

- Integrated fetched `origin/main` at `e12670ea9` with task preservation commit `7cb0b3520` and guidance commit `ee036285d` in merge `b8bc35ec8`. The README conflict was resolved by retaining New York Hustle, Swing, and freestyle entries.
- Re-ran the fast plus focused suite on the merged checkout: **10/11 passed in 9.44 seconds**. All 10 fast checks passed; the same saved finger rotation-mode assertion failed. See [the integrated log](playful_freestyle_evidence/integrated_verification.log).
- Storage policy passed for 23,962 staged files; whitespace verification and Python syntax compilation passed.
- All task binaries remain unchanged from the recorded asset manifest. Ordinary push and remote ancestry verification follow this record; any additional merge needed for concurrent pushes preserves remote history.
