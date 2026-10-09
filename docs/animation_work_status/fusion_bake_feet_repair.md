# Fusion bake and foot support repair

Written by Codex on 2026-10-09. Local authoring, source installation, numerical review, and visual sampling are complete for nine clips. Main integration follows the user's quality review. The active catalog contains the nine accepted repairs and retains their **Provisional export** and **Procedural study** labels.

## Delivered scope and measurements

The scope contains nine paired clips and six stepping variants: box basic, forward/back basic, promenade walk, shadow walk, side basic, and triple step. Compression/stretch, send-out/return, and shadow retain standing supports. All nine retain Man and Woman, `BOTH` participation, original formation metadata, four-second loops, 120 BPM, and eight beats. Original source/export provenance remains in the inventory and catalog.

The table reports maximum errors in millimeters. Baseline is the original saved bake compared with its authored source. Repaired bake and runtime columns compare the new authored motion with its deformation bake and actual-model runtime playback. Sole drift measures individual skinned vertices during declared support intervals.

| Clip | Baseline bake | Repaired bake | Runtime | Sole drift | Visual sample |
| --- | ---: | ---: | ---: | ---: | --- |
| `fusion_box_basic` | 50.860 | 0.786 | 0.787 | 0.892 | [review](fusion_bake_feet_repair/fusion_box_basic/review-contact-sheet.jpg) |
| `fusion_compression_stretch` | 15.586 | 0.081 | 0.143 | 0.297 | [review](fusion_bake_feet_repair/fusion_compression_stretch/review-contact-sheet.jpg) |
| `fusion_forward_back_basic` | 50.860 | 0.644 | 0.644 | 0.473 | [review](fusion_bake_feet_repair/fusion_forward_back_basic/review-contact-sheet.jpg) |
| `fusion_promenade_walk` | 104.038 | 0.557 | 0.557 | 0.472 | [review](fusion_bake_feet_repair/fusion_promenade_walk/review-contact-sheet.jpg) |
| `fusion_send_out_return` | 17.997 | 0.083 | 0.176 | 0.393 | [review](fusion_bake_feet_repair/fusion_send_out_return/review-contact-sheet.jpg) |
| `fusion_shadow` | 18.794 | 0.070 | 0.170 | 0.247 | [review](fusion_bake_feet_repair/fusion_shadow/review-contact-sheet.jpg) |
| `fusion_shadow_walk` | 55.038 | 0.557 | 0.557 | 0.472 | [review](fusion_bake_feet_repair/fusion_shadow_walk/review-contact-sheet.jpg) |
| `fusion_side_basic` | 50.860 | 0.797 | 0.798 | 0.870 | [review](fusion_bake_feet_repair/fusion_side_basic/review-contact-sheet.jpg) |
| `fusion_triple_step` | 50.860 | 0.196 | 0.196 | 0.656 | [review](fusion_bake_feet_repair/fusion_triple_step/review-contact-sheet.jpg) |

Every row passes the 2 mm pose and 3 mm support limits. Fresh source composition reproduces the authored matrices exactly. Loop position error is below 0.002 mm, and seam velocity is below the existing 0.12 m/s limit. See [summary.json](fusion_bake_feet_repair/summary.json) for per-file paths, sizes, SHA-256 hashes, ranges, dependency/model hashes, generator revisions, and comparison coverage. Each clip directory contains source, contacts, runtime, sole, loop, installation, and visual evidence plus `front-side.mp4`.

## Authoring choices

The native bake is rebuilt with the project's exporter and constant transform channels. A configurable rotation-repair strategy lets Fusion preserve its active quaternion finger poses while removing overlapping held Euler channels. Standard MPFB bodies, shared deformation skeletons, native wrist constraints, drivers, and rig dependencies retain their recorded revisions.

Foot controls hold world-space targets during support and use eased swings with a 45 mm peak lift. Both performers alternate an anatomical left-first swing. The selected phase convention is an original practice-study choice. The five regular stepping variants retain the recorded landing locations. Triple step has ten alternating landings with the rhythm **1, 2, 3-and-4, 5, 6, 7-and-8**; its targets follow the body's upcoming support interval. This gives triple step its own saved motion instead of the former side-basic duplicate. Stationary controls use one key where their interpolation permits it.

Sole calibration evaluates a temporary full MPFB body copy with wardrobe deletion masks disabled. The authored body and its modifiers remain intact. Native thigh IK scale corrections keep the evaluated leg lengths aligned with the shared deformation skeleton; this resolves the measured difference between stationary controls and moving foot surfaces. Recorded palm reference gaps remain about 30-31 mm, within the 35 mm study threshold. Wrist bend and hand-target reach are recorded separately.

Eight sources store frames 0-192 at 48 fps and play 0-191. Triple step stores 0-768 at 192 fps and plays 0-767. Each GLB lasts exactly four seconds and includes its repeated endpoint. The denser triple-step bake resolves the interpolation error around half-beat accents. Support plan intervals use the original 24 fps frame coordinate system; each report states its effective sampling rate.

## Validation coverage

| Stage | Coverage and result |
| --- | --- |
| Authored controls | Native IK/deform foot drift, sole calibration, support boundaries, four palm pairings, wrist bend, hand-target reach, and repeated endpoints measured. All declared support/contact gates pass. |
| Saved source | Fresh-process composition and chooser evaluation match authored matrices; linked libraries resolve. Installed descriptors, owner slots, participation, NLA serialization, rate, stored ranges, exclusive playback end, and exact action-curve fingerprint pass. All four tracks share the stored range; control tracks use native defaults and deform tracks preserve the exporter's zero serialized influence with animated influence disabled. |
| Deformation bake | All 420 deform bones across both performers, including fingers and toes, sampled with live follow constraints muted. Integer matrix and fractional-frame position gates pass. |
| Runtime export | Single named animation, 1,260 tracks, finite transforms, four-second duration, sample coverage, bindings, authored joint positions/rotations, sole surfaces, and seam checked with the actual MPFB models through Three.js. Candidate and installed GLBs share their verified hashes. |
| Visual review | 97 consecutive samples at 24 fps captured from front at 15 degrees and side views. Twelve samples per clip inspected for formations, swings, visible body clearance, hand shapes, and endpoints. Video includes the repeated endpoint. Human motion-quality approval remains the publication gate. |

Eight clips have 385 numerical samples and triple step has 1,537, including integer and half frames, authored keys, support boundaries, and near-seam points. The 11 comparison clips retain matching source/export hashes; their original bake errors range from 0.106 to 0.324 mm. [Baseline reports](fusion_bake_feet_repair/baseline) preserve the original 20-clip audit.

Geometric whole-body intersection measurement and comprehensive ergonomic acceptance remain future coverage. Side-view occlusion occurs in the side-by-side formations. The current visual evidence supports the focused bake/foot repair; procedural-study labels continue to apply to the complete choreography. Historical style review identifiers are translated to the active Fusion inventory; original history remains in [the source review](../source-review-records/fusion_partner_dance.md).

## Verification and checkpoints

`npm run check`, `npm test` (46/46), and `npm run build` pass. The build packages all 3,677 runtime clips. Logs and their hashes are recorded in `fusion_bake_feet_repair/tests`. The public FootPhrase tests, native bake helper tests, timing tests, and fresh source opening/save/reopen tests pass. The cross-style source-opening test reads 5.2.2 files with Blender 5.2.1 and emits the version warning; all three cases pass and their original hashes remain intact. The isolated profile is `.cache/fusion-repair/profile`.

Blender is `C:\Program Files\Blender Foundation\Blender 5.2\blender.exe`, version 5.2.1 LTS, build `9e2066aef7ef`. Fusion source headers report 5.2.44. Task Blender writers ran serially and exited. The task review server has stopped. Shared scene, character dependencies, and the primary checkout retain their original contents.

Raw authored matrices, runtime reference binaries, logs, original backups, and rejected trials remain under this worktree's `.cache/fusion-repair` and `.cache/motion-recovery`. Earlier triple-step trials measured 11.2 mm bake interpolation error and 51.6 mm sole drift; their revisions are retained as diagnostics. The accepted triple-step checkpoint supersedes them. Eight accepted clips use [the preserved first generator](fusion_bake_feet_repair/generators/repair_supports_initial.py); triple step uses the current `scripts/fusion_repair/repair_supports.py`. The readable generator files trim a trailing empty line; [authored-generators.zip](fusion_bake_feet_repair/generators/authored-generators.zip) preserves their exact executed bytes and [manifest.json](fusion_bake_feet_repair/generators/manifest.json) maps both hashes. Generated evidence retains its Windows line endings, verified with Git's `cr-at-eol` whitespace setting. `batch-initial.json` identifies its reconstructed provenance explicitly, and `batch.json` records the final triple-step process.

Resume validation from the existing durable checkpoint with PowerShell:

```powershell
Set-Location 'C:\Users\jonas\.codex\worktrees\fusion-bake-feet-repair\dance-animations'
$clips = (Get-Content docs/animation_work_status/fusion_bake_feet_repair/summary.json -Raw | ConvertFrom-Json).clips.id
./scripts/fusion_repair/run.ps1 -Script scripts/motion_recovery/validate.py -Clips $clips
./scripts/fusion_repair/run.ps1 -Script scripts/fusion_repair/review.py -Clips $clips
./scripts/fusion_repair/run.ps1 -Script scripts/motion_recovery/audit_installed.py -Clips $clips
node scripts/motion_recovery/runtime.mjs --installed @clips
node scripts/fusion_repair/surfaces.mjs @clips
node scripts/motion_recovery/loop_review.mjs @clips
npm run check
npm test
npm run build
python scripts/fusion_repair/report.py
```

Authoring reproduction starts from the baseline assets at `039e2626b490e07a1c95192c265e5635cc77f07c` in a separate worktree, with these task scripts and the relevant generator revision. `batch.ps1` expects the original 0-96 / 24 fps sources. Its transformation and the candidate installer each apply once per baseline. Reusing the installed sources as generation inputs requires a new explicit authoring plan. The local checkpoint commands above perform validation only.

Visual capture uses project-local Playwright Core 1.64.0, Edge, Pillow, and FFmpeg. With the saved candidate cache present, start the review server in a dedicated terminal:

```powershell
npm install --prefix .cache/fusion-repair/browser --no-save --package-lock=false playwright-core@1.64.0
node node_modules/vite/bin/vite.js --host 127.0.0.1 --port 5187 --strictPort
```

Run `node scripts/fusion_repair/capture.mjs @clips` and `python scripts/fusion_repair/review_sheets.py` from a second terminal in the same worktree. Stop the task review server after capture. Review sheets use the forward playback JPEG sequence that also produces the video.
