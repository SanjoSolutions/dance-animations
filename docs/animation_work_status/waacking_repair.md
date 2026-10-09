# Waacking source and bake repair

Local repair of the existing 16 clips, based on `039e2626b490e07a1c95192c265e5635cc77f07c`.
The final per-clip evidence and review disposition are collected in `waacking_repair/evidence.json`.

## Choreography and scope

The saved repertoire contains eight arm-circle movements for each solo role: alternating,
backward single left/right, double backward/forward, forward single left/right, and windmill.
Each clip retains its original four-second phrase at 120 BPM: eight beats, standing support,
a fixed formation, and a repeated loop endpoint. Man uses `PLAYER`; Woman uses `PARTNER`.
The saved hand and torso location curves retain their original trajectories. Foot target
heights receive a measured MPFB sole calibration. The support interval covers the entire loop.

The repair uses a posterior and outward elbow pole, with the wrist orientation fitted to the
evaluated forearm and native rest offset. These choices preserve the circular hand paths and
movement directions while changing elbow placement and wrist roll. Native wrist constraints,
control rotation modes, character bodies, drivers, and rest skeletons retain their shared definitions.
The source clock and all keys scale together from 24 to 192 frames per second. Stored frames
0–768 represent four seconds; cyclic playback ends at 767. Additional wrist keys are simplified
against a 0.15-degree angular tolerance. Held Euler finger poses become quaternion channels
in the shared controls' saved modes.

## Diagnosis

The current focused baseline exhibited an upper-arm twist step of approximately 125 degrees
between quarter-frame samples. The native arm mechanism blends upper-arm and forearm frames
at half influence. The original outward pole lets the forearm frame cross the blend's rotation
branch while its hand follows the circle. Local tweak compensation moved that branch crossing
into another segment. The repaired elbow plane and forearm-based wrist orientation keep the
arm chain continuous through the sampled motion. The shared mechanism remains intact.

Fresh composition and native bake playback use `dance_tools`, `TrackChooser`, and the existing
motion recovery helpers. Bake review mutes the live deform follow constraints and compares every
deform bone, including fingers and toes. Sampling includes stored integer and half frames,
with independent near-seam runtime samples. The reports distinguish authored control motion,
fresh source playback, deformation bake fidelity, runtime playback, and visual review.

## Reproduction

Run the authoring recipe on the recorded baseline source revision. Keep the saved source/export
pairs and their catalog hashes together. The scripts write candidates and checkpoints under
`.cache/motion-recovery`; installation uses the existing recovery installer after the required
candidate checks. Windows processes use the dedicated `.cache/waacking-profile` directories.
The executable is Blender 5.2.1 LTS, build `9e2066aef7ef`. Baseline source schema tuples are
`[5, 2, 44]` for Man and `[5, 2, 45]` for Woman. Every candidate receives a fresh-process
composition and evaluated-pose comparison with the executable recorded above.
The native batch runs one Blender process at a time.

```powershell
python scripts/waacking/batch.py --blender 'C:\Program Files\Blender Foundation\Blender 5.2\blender.exe'
./scripts/waacking/run_blender.ps1 -Script scripts/waacking/review.py -Clips waacking_man_forward_single_left
./scripts/waacking/run_blender.ps1 -Script scripts/waacking/surface_review.py -Clips waacking_man_forward_single_left
./scripts/waacking/run_blender.ps1 -Script scripts/waacking/render_review.py -Clips waacking_man_forward_single_left
```

Runtime reference conversion uses `scripts/motion_recovery/runtime_batch.py` with the packages
in `scripts/motion_recovery/requirements.txt`. `runtime.mjs`, `surfaces.mjs`, and `loop_review.mjs`
run against the project's actual MPFB GLBs. `contact_sheets.py` uses Pillow to assemble the
rendered front, side, and back poses. An isolated headless Edge session captures the exported
GLBs on the actual MPFB base models at eight samples per second from the same three views.
The browser capture and native renders have separate source/export hash records.

The clips retain procedural-study status. Numerical coverage, sampled surface review,
choreographic review, and main integration have separate completion states.


## Review dependencies and playback

```powershell
python -m venv .cache/waacking-venv
.cache/waacking-venv/Scripts/python.exe -m pip install -r scripts/waacking/requirements.txt
npm ci --cache .cache/npm
npm install --prefix .cache/waacking-browser --cache .cache/npm playwright@1.64.0
npm run dev -- --port 5193 --strictPort
```

With the server running, open `/scripts/waacking/preview.html` to review all 16 candidates.
The active catalog supplies the installed-clip fallback. With candidate checkpoints present, their source/export hashes select
the reviewed trial files. `node scripts/waacking/capture_runtime.mjs` captures those candidates
through the public playback controls. `.cache/waacking-venv/Scripts/python.exe
scripts/waacking/replay_media.py` creates the animated review images.


## Numerical results

All 16 candidates pass the fresh-source, native deformation-bake and actual-model runtime
comparisons. Native review samples all 209 deform bones at 1,537 times per clip, including
stored integer and half frames. The source comparison has a maximum matrix difference of zero.
The baseline scan uses 385 quarter-frame samples at the original 24 fps; the repaired scan
uses the denser clock above.

| Measurement across 16 clips | Maximum measured value | Acceptance tolerance |
| --- | ---: | ---: |
| Native bake joint-position error | 1.491 mm | 2 mm |
| Native bake bone-tail error | 1.541 mm | 6 mm |
| Native bake orientation error | 0.595 degrees | 3 degrees |
| Integer-frame bake matrix difference | 0.000009828 | 0.0001 |
| Authored angular step per 1/384 second | 4.588 degrees | 20 degrees |
| Wrist bend | 6.968 degrees | 85 degrees |
| Hand IK reach error | 0.007751 mm | 6 mm |
| Runtime joint-position error | 1.491 mm | 2 mm |
| Runtime orientation error | 0.596 degrees | 3 degrees |
| Runtime loop position difference | 0.000820 mm | 1 mm |
| Runtime loop velocity difference | 0.004368 m/s | 0.12 m/s |

Every export has a four-second duration. The complete repertoire receives 360 held-finger
control conversions across 15 sources; the focused Man forward-left source already carried
its quaternion repair. Baseline source-to-bake errors reached 82.362 mm and 133.031 degrees.

Standing-support targets remain stationary. Evaluated deform foot joints drift by up to
2.724 mm through the inherited torso motion. Runtime sole minima range from -0.980 mm to
+1.917 mm relative to the review floor, within the 2 mm penetration tolerance. These are
contact measurements, distinct from the source-to-bake errors above.

Surface coverage samples each native MPFB body at 193 times. Weighted distal upper-arm,
forearm, hand and finger regions are compared with the torso, head, legs and opposite arm.
Joint-adjacent proximal shoulders receive visual coverage. Individual finger self-contact,
dynamic balance and full-speed expert choreography review retain study coverage.


## Delivered clip identifiers

| Movement | Man | Woman |
| --- | --- | --- |
| alternating | `waacking_man_alternating` | `waacking_woman_alternating` |
| backward single left | `waacking_man_backward_single_left` | `waacking_woman_backward_single_left` |
| backward single right | `waacking_man_backward_single_right` | `waacking_woman_backward_single_right` |
| double backward | `waacking_man_double_backward` | `waacking_woman_double_backward` |
| double forward | `waacking_man_double_forward` | `waacking_woman_double_forward` |
| forward single left | `waacking_man_forward_single_left` | `waacking_woman_forward_single_left` |
| forward single right | `waacking_man_forward_single_right` | `waacking_woman_forward_single_right` |
| windmill | `waacking_man_windmill` | `waacking_woman_windmill` |


## Installation and verification commands

Use the task worktree at
`C:\Users\jonas\.codex\worktrees\waacking-repair\dance-animations`.
The candidate checkpoints under `.cache/motion-recovery/<clip-id>/` retain the original
source/export backups, evaluated pose arrays, reports and render logs. The current recipe
is the pole/wrist repair plus sole calibration recorded in each checkpoint. The historical
source review and earlier diagnostic renders describe their own asset revisions.

After recording the sampled visual disposition for each candidate, installation writes the
portable `../../shared_scene_data.blend` descriptor and verifies exact curve parity. The
existing compressor compares every decoded accessor value after lossless Meshopt encoding.
Use these commands for a fresh reviewed candidate set:

```powershell
$clips = (Get-Content catalog.json -Raw | ConvertFrom-Json).animations |
    Where-Object style -eq 'waacking' | ForEach-Object id
./scripts/waacking/run_blender.ps1 -Script scripts/waacking/install_reviewed.py
node scripts/compress-clips.mjs @clips
./scripts/waacking/run_blender.ps1 -Script scripts/motion_recovery/audit_installed.py -Clips $clips
node scripts/motion_recovery/runtime.mjs --installed @clips
npm run check
npm test
npm run build
python scripts/waacking/collect_evidence.py
```

For installed assets, resume with `audit_installed.py`, the installed runtime check and the
project checks. `install_reviewed.py` expects the baseline source/export pair and is a
single promotion step for that candidate revision.


## Storage and review state

The 16 installed sources total 421.77 MiB, with each source below 26.42 MiB. The dense native
bakes preserve the complete deformation channels at 192 fps. The 16 compressed runtime GLBs
total 11.14 MiB. All delivered files belong to regular Git under the 100 MiB size policy.

All 16 clips have authored-control, fresh-source, deformation-bake, actual-model runtime,
sampled-surface and sampled-pose review evidence. Every tested skin-region pair has zero
triangle intersections at the 193 sampled times. The native contact sheets contain 576
reviewed captures; the runtime animations contain 32 samples per view across each four-second
loop. Runtime capture inspection covers the explicitly listed frames in `runtime-capture.json`.

The repaired pairs occupy their existing catalog entries on `codex/waacking-repair`.
Procedural-study status remains active. Main integration awaits the user's local quality
approval. The final project-check receipts and process disposition accompany the per-clip
records in `waacking_repair/`.


## Final local validation

`npm run check` passes for 3,677 runtime variants and 3,558 source hashes, including asset
provenance, GLB structure, license notices and the 816.3 MiB packaged runtime footprint.
`npm test` passes all 46 tests. `npm run build` passes and packages all 3,677 runtime variants.
The installed-source and installed-runtime audits pass for all 16 repaired clips.

Task-owned authoring, baking, rendering, browser capture, preview and validation processes
have completed. Saved candidates, baseline backups and diagnostic arrays remain available
under the task-local cache for the resume commands above.

`recipe-byte-snapshots.zip` preserves the script bytes associated with the recorded generator
hashes. `recipe-byte-normalization.json` maps those bytes to the tools' UTF-8/LF checkout
versions and verifies matching Python syntax trees. The normalization changes file endings;
the reviewed animation values and source/export hashes retain their recorded revisions.
