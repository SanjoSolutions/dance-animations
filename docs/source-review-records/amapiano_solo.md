# Amapiano solo animation work status

- Date: October 2, 2026, 16:59 Europe/Berlin (14:59 UTC).
- Chat title: Create Amapiano dance animations (`01a0fd04-bc9d-736d-9910-df6d25668060`).
- Environment: sanjo-solutions cloud environment; `/workspace/sanjo-solutions/apps/a-game`.
- Task branch at stop: `codex/amapiano-solo`.
- Starting/current pre-preservation commit: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Author: Codex. GitHub publication of this record and its commits is authored by Codex.
- State: **stopped by explicit user instruction; preservation and delivery only**.

## Original scope and stopping point

The requested work was a broad, organized Amapiano repertoire for both characters,
with reusable dance movement, positions, solo clips, natural IK motion, contact,
clearance, loop and transition validation, Blender 5.2 authoring and export,
per-animation source files, direct Git storage through 100 MiB, documentation,
rebasing onto current main, and merge/push delivery.

The implemented plan targeted 28 clips per character: 20 movement loops, four
positions, and four transitions. The user stopped the work during the Man batch.
The durable state contains **13 Man-only sources and 13 GLB exports**. Every source
contains one authored action and its matching `.baked` action. **Zero Woman clips,
zero position clips, and zero transition clips have been generated.** These are
partial procedural animation studies, rather than a completed repertoire.

The owned authoring process (PID 2163) was terminated with SIGTERM immediately
after the stop instruction. Its final log reports a passing refined control
review for `amapiano_man_forward_back`, but that revision had not reached a durable
source/export write. The saved forward/back files are the earlier study. All
owned Blender authoring and rendering processes have ended. Subsequent Blender
work only inspected existing action data; it created no animation or render.

## Exact saved assets

All clips below use Man / `PLAYER`, 24 fps, frames 0–104, eight beats at about
110.77 BPM, with frame 104 as the loop interpolation endpoint. Each linked export
has a corresponding `<export path>.import` settings file, also preserved.
`models/player/animation_updates.tres` references all 13 provisional exports and
retains its six original clip references.

**Refined** means the saved source passed the latest half-frame control review,
including evaluated deform-foot plants, reach, wrist bend, capsule clearance,
and position/rotation/velocity loop checks. **Earlier study** means the file
predates the complete saved-rotation-mode, evaluated-foot, or body-following
corrections and requires regeneration and review. None has a completed final
rendered review or a verified Godot import.

| Clip | Saved validation state | Source | Export |
| --- | --- | --- | --- |
| `amapiano_man_basic_bounce` | Refined control checks passed | `animations/man_and_woman/amapiano_man_basic_bounce.blend` (371491 bytes) | `models/player/animation_updates/amapiano_man_basic_bounce_baked_a5609cbdab02.glb` (366948 bytes) |
| `amapiano_man_body_roll` | Refined control checks passed | `animations/man_and_woman/amapiano_man_body_roll.blend` (366416 bytes) | `models/player/animation_updates/amapiano_man_body_roll_baked_db864e14922b.glb` (363768 bytes) |
| `amapiano_man_diagonal_step` | Earlier procedural study | `animations/man_and_woman/amapiano_man_diagonal_step.blend` (400154 bytes) | `models/player/animation_updates/amapiano_man_diagonal_step_baked_2bc59c60b440.glb` (368464 bytes) |
| `amapiano_man_forward_back` | Earlier procedural study | `animations/man_and_woman/amapiano_man_forward_back.blend` (402132 bytes) | `models/player/animation_updates/amapiano_man_forward_back_baked_7ffcd15b9b48.glb` (368324 bytes) |
| `amapiano_man_heel_tap` | Earlier procedural study | `animations/man_and_woman/amapiano_man_heel_tap.blend` (376142 bytes) | `models/player/animation_updates/amapiano_man_heel_tap_baked_9055e0f324a3.glb` (368732 bytes) |
| `amapiano_man_hip_circle` | Refined control checks passed | `animations/man_and_woman/amapiano_man_hip_circle.blend` (369007 bytes) | `models/player/animation_updates/amapiano_man_hip_circle_baked_7f652e3bbc24.glb` (360384 bytes) |
| `amapiano_man_knee_lift` | Earlier procedural study | `animations/man_and_woman/amapiano_man_knee_lift.blend` (374015 bytes) | `models/player/animation_updates/amapiano_man_knee_lift_baked_961361cbc31f.glb` (363552 bytes) |
| `amapiano_man_shaku_inspired` | Earlier procedural study | `animations/man_and_woman/amapiano_man_shaku_inspired.blend` (371213 bytes) | `models/player/animation_updates/amapiano_man_shaku_inspired_baked_4bd993a9bfc6.glb` (373572 bytes) |
| `amapiano_man_shoulder_groove` | Refined control checks passed | `animations/man_and_woman/amapiano_man_shoulder_groove.blend` (362280 bytes) | `models/player/animation_updates/amapiano_man_shoulder_groove_baked_51eb24a302b2.glb` (365296 bytes) |
| `amapiano_man_side_sway` | Refined control checks passed | `animations/man_and_woman/amapiano_man_side_sway.blend` (361910 bytes) | `models/player/animation_updates/amapiano_man_side_sway_baked_72e55b29b83f.glb` (363768 bytes) |
| `amapiano_man_skater_step` | Earlier procedural study | `animations/man_and_woman/amapiano_man_skater_step.blend` (373445 bytes) | `models/player/animation_updates/amapiano_man_skater_step_baked_ea7479aca730.glb` (366940 bytes) |
| `amapiano_man_step_touch` | Refined control checks passed | `animations/man_and_woman/amapiano_man_step_touch.blend` (405293 bytes) | `models/player/animation_updates/amapiano_man_step_touch_baked_494ac1561d83.glb` (366944 bytes) |
| `amapiano_man_toe_tap` | Earlier procedural study | `animations/man_and_woman/amapiano_man_toe_tap.blend` (380743 bytes) | `models/player/animation_updates/amapiano_man_toe_tap_baked_30964967c75c.glb` (365268 bytes) |

`amapiano_solo_evidence/asset_inventory.json` lists every source, GLB, and import
file with its byte count and SHA-256. `source_inspection.json` records the action
names, channel counts, roles, frame ranges, and slots from all 13 actual Blender
files. The four early files for heel tap, toe tap, knee lift, and Shaku-inspired
motion survive from an earlier process although they are absent from the
interrupted `docs/amapiano/catalog.json`. The inventory is authoritative.

## Other durable task files

- `scripts/player_assets/amapiano_choreography.py`: the planned 28-phrase specification and foot/torso/hand trajectories. Step-touch and skater reuse the existing disco foot path with different timing and support transfer.
- `scripts/player_assets/author_amapiano.py`: Blender 5.2 authoring, sparse keys, rotation-mode preservation, evaluated-ankle correction, control checks, native visual bake, per-animation file writing, and compact GLB publication. This implementation is partially exercised, with 43 planned clips remaining to generate or regenerate as appropriate.
- `scripts/player_assets/review_amapiano.py`: saved-source/deform-bake comparison, skin-floor sampling, and optional renders/sheets. The full batch remains pending; only basic-bounce diagnostics were run.
- `scripts/player_assets/validate_amapiano_exports.py`: planned isolated Godot import and channel-target verification. It expects 56 clips and has not been executed because the repertoire stopped at 13.
- `docs/amapiano/README.md`: explicitly paused workflow and planned repertoire, with implementation and review commands.
- `docs/amapiano/catalog.json`: interrupted nine-entry generation snapshot. Six entries contain refined metrics; its earlier entries and omitted files require the preservation inventory above.
- `docs/amapiano/saved_review.json`: successful corrected basic-bounce diagnostic before the final rebuild. The final source was rebuilt afterward, so this report is evidence of the fix rather than a checksum-bound validation of every preserved file.
- `docs/animation_work_status/amapiano_solo.md`: this status record.
- `docs/animation_work_status/amapiano_solo_evidence/`: inventory, read-only source inspection, command logs, and one earlier rendered blocking study.
- `apps/a-game/.gitattributes`: 27 exact-path regular-Git exceptions for the 26 preserved source/export binaries and the earlier rendered study. Measured maximum 405,293 bytes; total 9,776,527 bytes. Existing LFS storage stays intact.

## Validation and findings

All Blender work used Blender **5.2.2 LTS**, hash `d13f752e3b9c`. The final fast
and focused checks used the available Godot **4.7.2** executable.

| Verification | Result |
| --- | --- |
| `python tests/run_tests.py --suite fast` after stopping | **9/9 passed**, 2.91 seconds. `fast_tests.txt`. |
| `python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_single_animation_layout.py --changed scripts/player_assets/test_animation_updates.py` | **11/11 passed**, 5.69 seconds, including two related slow fixtures. `focused_tests.txt`. |
| Read-only Blender source inspection after stopping | **13/13 files** have exactly one Man authoring action and one matching baked action, each with one slot and PLAYER participant. `source_inspection.json` and `.txt`. |
| GLB structural inspection after stopping | **13/13** have one animation, 0–104-frame duration (4.333 seconds), and complete readable GLB data. Inventory records channel counts and names. |
| Source startup through `animation_file_startup.py` | Basic-bounce source composes the runtime shared scene, 430 objects, and selects its source name. `source_open.txt`. |
| Six refined control-motion checks | Passed at 211 samples per clip, including half frames and 0.05-frame seam samples. `refined_build.txt`, `interrupted_build.txt`, and catalog metrics. |
| Corrected basic-bounce saved/baked comparison | Passed across 210 deform bones and 209 samples: maximum position difference 0.00133193 m, rotation difference 0.00384474 rad, minimum visible-skin height 0.00051812 m. `saved_basic_bounce_review.txt`. This is the diagnostic version before final regeneration. |
| Final whole-repertoire render, bake, and Godot checks | Pending at user stop. |

Early validation identified finger rotation-mode loss after source reopening and
an offset between the man's IK ankle and visible deform foot. The implementation
now preserves shared-rig rotation modes and compensates the evaluated deform
ankle. An early native-bake comparison failed with a 52.9 mm fingertip discrepancy
and 1.7446 rad rotational difference; the corrected diagnostic above passed.
The step-touch torso capsule test also found a hand/body overlap during lateral
travel; moving the hands with the torso passed its refined review.

`earlier_basic_bounce_study.png` is a **procedural blocking/diagnostic render from
before the saved-mode and ground corrections**. It supplies visual context only.
It is not an approved final animation preview. No further renders were produced
after the user's stop instruction.

## Remaining work and blockers

1. The user stop is the active blocker. Resume animation work only after fresh authorization.
2. Regenerate the seven earlier Man studies and finish the remaining Man and all Woman moves, positions, and transitions. Reconcile the partial catalog against the inventory.
3. Re-run read-only saved-source/bake comparisons against the final generated bytes, inspect actual skin contact/clearance and complete visual playback/render review.
4. Verify transition endpoints and inter-clip blends; the implemented transitions have yet to be authored and reviewed on either rig.
5. Earlier generated `.glb.import` files omit the full-library `gltf/*` naming settings after replacing `_subresources`; the latest exporter preserves them. Regeneration/import review is pending. Preserve current files as studies until that review completes.
6. Execute the isolated Godot validator after the complete 56-entry catalog exists, and confirm all target paths on the composed model.
7. Game Rig Tools was absent from this environment when authoring began; native Blender visual baking was used. Rebased main now includes the bundled installer from `18e528c73`. Follow `scripts/blender/README.md` and enable the tools in a consistent profile before future work; the preserved assets remain the native-bake studies described above.

The initial fast suite encountered three materialized-LFS prerequisites in
`playground/hair/physics/` (ponytail, braid, long hair). Downloading those existing
assets resolved the issue; the recorded final fast suite passes. Git LFS initially
needed the configured `SANJO_GITHUB_LFS_TOKEN` through an ephemeral askpass helper.
Credentials were consumed at runtime, with no secret values written to task files.

## Exact resume commands

These commands document future work; they were not run after the stop request.
Use an authorized new task and start from the integrated main branch. The default
full authoring command regenerates all outputs consistently; avoid `--resume`
against this mixed-generation catalog.

```sh
cd /workspace/sanjo-solutions/apps/a-game
export BLENDER=/home/agent/.local/bin/blender
export GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot
"$BLENDER" --version
"$BLENDER" --background --python-exit-code 1 \
  --python scripts/blender/install_animation_tools.py
"$BLENDER" -b -y animations/man_and_woman/shared_scene_data.blend \
  --python-exit-code 1 --python scripts/player_assets/author_amapiano.py
"$BLENDER" -b -y animations/man_and_woman/shared_scene_data.blend \
  --python-exit-code 1 --python scripts/player_assets/review_amapiano.py
python scripts/player_assets/validate_amapiano_exports.py
python tests/run_tests.py --suite fast
python tests/run_tests.py \
  --changed scripts/player_assets/test_animation_files.py \
  --changed scripts/player_assets/test_single_animation_layout.py \
  --changed scripts/player_assets/test_animation_updates.py
```

For focused authoring, append `-- --character Man --move basic_bounce` to the
authoring command. For read-only numerical review, append
`-- --move basic_bounce --skip-render` to the review command. Recheck actual
binary sizes and attributes before staging later regenerated assets; files over
104,857,600 bytes require a file-specific LFS rule.

## Delivery record

This record is committed together with the preserved assets. The task commit is
identified by the Git history entry adding this path; integration and push hashes
are reported in the chat delivery response. The original request's helpful
`# Animation` guidance update follows in a separate documentation commit after
rebasing the preservation commit onto freshly fetched `origin/main`. Integration
uses ordinary history-preserving pushes, with concurrent changes retained.

Preservation commit after rebasing onto `18e528c73`: `d272a978c58ede4eb711cb0b78b1052ca0407155`. The subsequent documentation commit adds the shared `# Animation` guidance and this delivery clarification.

After rebasing, the current main fast suite passed **10/10** in 5.97 seconds
(`amapiano_solo_evidence/rebased_fast_tests.txt`). `python scripts/lfs_policy.py check`
passed for 23,415 staged files. The shared scene and both anatomical sources match
the original LFS object SHA-256 values byte-for-byte; their main-branch changes
are storage conversions, preserving the rig content used by these studies.

Integration onto `629cffdc1` retained both branches' exact-path storage rules and
animation guidance. The runtime-update registry is the union of 55 main references
and 19 task references, yielding 68 distinct libraries. All preserved task-asset
hashes still match the inventory. The integrated fast suite passed **10/10** in
6.11 seconds (`amapiano_solo_evidence/merged_fast_tests.txt`); the staged LFS policy
check passed for 24,454 files before adding this final test log.

The first ordinary push met concurrent main changes and was rejected. Integration
with `1e89ec851` retains all 191 current-main runtime references plus the 13
Amapiano references (204 total), every current-main guidance line, and both
Amapiano guidance additions. The fast suite passed **10/10** in 6.07 seconds
(`amapiano_solo_evidence/retry_fast_tests.txt`). The final integration preserves
the original task commits and uses an ordinary history-preserving push.

## Latest integration attempt

Integrated remote `b0b1ea4cda471e017f4b5f79b4f096fe96b51fa5` with the preserved task commits. Retained all remote guidance and 585 runtime-library references including the 13 Amapiano studies. Preserved asset SHA-256 checks passed. Most recent recorded fast result (before this integration retry when checks are reused): **10/10 checks passed in 6.50s**; see `amapiano_solo_evidence/latest_integration_fast_tests.txt`. Ordinary push retries retain remote history.
