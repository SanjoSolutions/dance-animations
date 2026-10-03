# Solo rumba animation work status

- Date: October 2, 2026 (Europe/Berlin; stopped at approximately 16:55 CEST).
- Chat: Solo rumba for man_and_woman3.blend (A-Game).
- Task branch: `codex/solo-rumba`.
- Starting/current commit when animation work stopped: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Author of this record and task GitHub delivery: Codex.
- State: **Stopped by user instruction; partial procedural blocking studies preserved.**

## Original scope and stopping point

Create a broad solo rumba repertoire for both Man and Woman using Blender 5.2, the
existing IK helpers, separate animation authoring files, baked deform actions and
individual Godot exports. Validate interpolated contacts, body clearance and loops;
reuse fitting existing motion; commit, rebase, document Animation guidance, merge
and push main. Files at or below 104,857,600 bytes belong directly in Git.

The working interpretation was International Latin rumba adapted for independent
solo dancers, with a 96 BPM 2, 3, 4-1 rhythm at 24 fps. The code catalog contains
52 proposed figures/positions and targets 104 independent character clips. That
catalog is a proposal, rather than evidence of completed choreography or coverage
of every rumba tradition. Eight figures reached saved files for both characters.
The latest batch stopped after reviewing Cuban rocks for Man, during its bake/export
sequence. Its newer source survived; its published GLB is from an earlier build.

## Preserved work

There are 16 per-animation `.blend` sources, each containing an editable control
rig action and a matching `.baked` deform action. Each action owns one character
slot. Man selects `PLAYER`; Woman selects `PARTNER`. Every saved clip spans frames
0–120 inclusive at 24 fps, with frame 120 as the matching loop endpoint (5 seconds).
The shared `man_and_woman3.blend`, shared scene and character geometry remain at
the original repository revisions. The combined library discovers the new sources
through the existing add-on on reopening.

There are 16 provisional GLBs and corresponding `.glb.import` files. Their extra
control-rig content makes them **partial exports, rather than approved runtime
assets**. Their additions to `models/player/animation_updates.tres` were withdrawn
on stopping so the preserved studies stay outside active game playback. An
intermediate `clip.glb` was also preserved in the evidence directory.

| Figure | Source revision at stop | Delivery state |
| --- | --- | --- |
| Basic in place | Latest interrupted batch, both roles | Authored and baked; provisional export |
| Basic forward/back | Latest interrupted batch, both roles | Authored and baked; provisional export |
| Basic side | Latest interrupted batch, both roles | Authored and baked; provisional export |
| Box | Latest interrupted batch, both roles | Authored and baked; provisional export |
| Cucaracha | Latest interrupted batch, both roles | Authored and baked; provisional export |
| Cuban rocks | Man source latest; Woman source earlier | Man GLB predates source; both exports provisional |
| Side to side | Earlier batch, both roles | Earlier elbow/finger/weight revision; provisional export |
| Spot turn left | Earlier focused test, both roles | Earlier elbow/finger/weight revision; provisional export |

Scripts preserved:

- `scripts/solo_rumba.py`: proposed vocabulary, musical events and foot trajectories.
- `scripts/create_solo_rumba.py`: Blender 5.2 authoring, sparse control keys, native
  visual bake, per-animation writer, compact scene exporter and update publisher.
  This is a work-in-progress generator; running it changes sources and registration.
- `scripts/review_solo_rumba.py`: half-frame foot plants, wrist angles, hand/torso
  proxy clearance, ankle separation, motion increments and loop diagnostics.
- `scripts/validate_solo_rumba.py`: read-only verification of saved sources, sampled
  bake agreement and GLB contents; `--existing-only` audits this stopped subset.
  During delivery only this validator was adjusted to report every preserved
  export failure instead of aborting on the first extra animation.
- `.gitattributes`: exact-path direct-Git exceptions for the measured task binaries.

`DiscoWristPoser`, `RigYogaPoser`, `YogaPoseLibrary`, `AnimationFileWriter`,
`AnimationTracks`, `AnimationClipScene`, exporter options and `AnimationUpdates`
were reused. Existing dance actions were inspected as references; their whole
routines were not relabeled as rumba. Game Rig Tools was unavailable in this cloud
installation, so the procedural studies use Blender's native visual bake. This
alternative still needs the saved-source/export parity fixes below.

## Verification and blockers

- Blender: **5.2.2 LTS**, build `d13f752e3b9c`. All Blender authoring, baking,
  validation, export and the three saved preview renders used this executable.
- Final required fast suite: **9/9 passed**, 3.25 seconds, with Godot 4.7.2.
- Saved asset audit: **16/16 reported publication failure**. All GLBs contain both
  the intended `.baked` animation and an extra authoring animation, with control
  rigs included. The compact export scene's referenced dependencies require
  investigation before publication. The validator deliberately exits 1.
- Saved-source half-frame audit: 241 samples per clip. Maximum planted-ankle error
  across this subset is below 0.000231 meters. The proxy and loop measurements are
  preserved per clip; these checks describe landmarks, rather than full skin
  intersection or verified choreography. Earlier visually reviewed poses showed
  elbows too high; the latest subset includes lower elbow guides.
- Saved bake agreement: worst sampled deform-position difference is approximately
  0.005582 meters, above the chosen 0.002-meter acceptance threshold. Eleven latest
  sources exceed that threshold. Earlier clips with smaller errors still fail
  export-content checks. Fix fractional-frame bake fidelity before calling these
  complete. The partial assets were preserved as requested, with failures intact.
- Earlier finger posing used Euler channels while the shared rig uses quaternion
  controls. The latest generator uses quaternion finger keys. Earlier side-to-side,
  Woman Cuban-rocks and spot-turn files need regeneration after resumption.
- Broad repository selection was started with `python tests/run_tests.py`. It
  encountered existing resource/import failures and long-running editor checks.
  It was terminated during the stop request. It has **no complete passing result**.
  The saved log includes missing/binary-resource failures from LFS-pointer inputs
  and generated-import mismatches. Additional game binaries were downloaded;
  a complete clean import and broad rerun remain outstanding.
- Godot checks generated edits to unrelated imported resources. Those edits were
  backed up locally in `/workspace/scratch/rumba/incidental_test_changes.patch`
  and restored to their tracked revisions. Task sources and exports were retained.
- Rendering produced three still previews before the stop. They document earlier
  iterations, with source mesh artifacts visible; they are evidence, not final
  animation approval. Review full deformed surfaces and animated playback later.

## Processes and saved evidence

Owned authoring Blender PID 3793 and broad-test runner PID 1973 were terminated.
The broad runner's active Godot child was also terminated. Earlier authoring PIDs
1788 and 3650 had been stopped during iteration. Delivery used a separate read-only
Blender validation process and the final fast suite, both completed. Animation
creation and rendering remain stopped. Temporary workspace logs and helper scripts
remain under `/workspace/scratch/rumba/`; they are optional local context.

Durable evidence under `docs/animation_work_status/solo_rumba_evidence/`:

- `asset_inventory.json`: each binary's actual byte count, SHA-256 and storage.
- `saved_asset_validation.json`: per-source, bake and GLB results.
- `interrupted_build.log`: latest batch, ending at the stop point.
- `earlier_turn_build.log`: original focused spot-turn study.
- `initial_saved_validation.log`: first discovery of the export-content failure.
- `final_saved_validation.log`: complete preserved-subset audit, exit 1.
- `final_fast.log`: final nine passing fast checks.
- `related.log`: interrupted broader repository run.
- `fast.log`, `render.log`, `render_man.log`: earlier checks/render diagnostics.
- `earlier_build_report.json`: earlier focused run; it does not describe the latest
  interrupted subset.
- Three `solo_rumba_*.png` stills and `interrupted_clip.glb`: outputs produced before
  stopping. Their exact paths and hashes appear in the inventory.

## Exact saved source and export inventory

Paths below are relative to `apps/a-game`. Each GLB also has its adjacent
`.glb.import` file. All listed binaries are below 100 MiB and stored directly in
Git; this task creates zero new LFS upload obligations.

| Action / role | Source | Provisional export |
| --- | --- | --- |
| `solo_rumba_basic_in_place_man` / PLAYER | `animations/man_and_woman/solo_rumba_basic_in_place_man.blend` | `output/solo_rumba/partial_exports/solo_rumba_basic_in_place_man_baked_7024c5f0d9e8.glb` |
| `solo_rumba_basic_in_place_woman` / PARTNER | `animations/man_and_woman/solo_rumba_basic_in_place_woman.blend` | `output/solo_rumba/partial_exports/solo_rumba_basic_in_place_woman_baked_eceaf124f00b.glb` |
| `solo_rumba_basic_forward_back_man` / PLAYER | `animations/man_and_woman/solo_rumba_basic_forward_back_man.blend` | `output/solo_rumba/partial_exports/solo_rumba_basic_forward_back_man_baked_9306c5dc4fc9.glb` |
| `solo_rumba_basic_forward_back_woman` / PARTNER | `animations/man_and_woman/solo_rumba_basic_forward_back_woman.blend` | `output/solo_rumba/partial_exports/solo_rumba_basic_forward_back_woman_baked_651eb532c468.glb` |
| `solo_rumba_basic_side_man` / PLAYER | `animations/man_and_woman/solo_rumba_basic_side_man.blend` | `output/solo_rumba/partial_exports/solo_rumba_basic_side_man_baked_11c5a8f17bf6.glb` |
| `solo_rumba_basic_side_woman` / PARTNER | `animations/man_and_woman/solo_rumba_basic_side_woman.blend` | `output/solo_rumba/partial_exports/solo_rumba_basic_side_woman_baked_8c16d45758ce.glb` |
| `solo_rumba_box_man` / PLAYER | `animations/man_and_woman/solo_rumba_box_man.blend` | `output/solo_rumba/partial_exports/solo_rumba_box_man_baked_bafe4a769195.glb` |
| `solo_rumba_box_woman` / PARTNER | `animations/man_and_woman/solo_rumba_box_woman.blend` | `output/solo_rumba/partial_exports/solo_rumba_box_woman_baked_b2c104e923be.glb` |
| `solo_rumba_cucaracha_man` / PLAYER | `animations/man_and_woman/solo_rumba_cucaracha_man.blend` | `output/solo_rumba/partial_exports/solo_rumba_cucaracha_man_baked_36ea97d45f8f.glb` |
| `solo_rumba_cucaracha_woman` / PARTNER | `animations/man_and_woman/solo_rumba_cucaracha_woman.blend` | `output/solo_rumba/partial_exports/solo_rumba_cucaracha_woman_baked_070c6e422c8a.glb` |
| `solo_rumba_cuban_rocks_man` / PLAYER | `animations/man_and_woman/solo_rumba_cuban_rocks_man.blend` | `output/solo_rumba/partial_exports/solo_rumba_cuban_rocks_man_baked_ead6d0c3fff1.glb` |
| `solo_rumba_cuban_rocks_woman` / PARTNER | `animations/man_and_woman/solo_rumba_cuban_rocks_woman.blend` | `output/solo_rumba/partial_exports/solo_rumba_cuban_rocks_woman_baked_049cb87bd345.glb` |
| `solo_rumba_side_to_side_man` / PLAYER | `animations/man_and_woman/solo_rumba_side_to_side_man.blend` | `output/solo_rumba/partial_exports/solo_rumba_side_to_side_man_baked_7620ef191ccb.glb` |
| `solo_rumba_side_to_side_woman` / PARTNER | `animations/man_and_woman/solo_rumba_side_to_side_woman.blend` | `output/solo_rumba/partial_exports/solo_rumba_side_to_side_woman_baked_218c383aead8.glb` |
| `solo_rumba_spot_turn_left_man` / PLAYER | `animations/man_and_woman/solo_rumba_spot_turn_left_man.blend` | `output/solo_rumba/partial_exports/solo_rumba_spot_turn_left_man_baked_94b81c92fdbb.glb` |
| `solo_rumba_spot_turn_left_woman` / PARTNER | `animations/man_and_woman/solo_rumba_spot_turn_left_woman.blend` | `output/solo_rumba/partial_exports/solo_rumba_spot_turn_left_woman_baked_32fb821171d4.glb` |

## Remaining work and exact resume commands

Resume animation work only after a fresh user instruction. First repair the
compact export dependency selection and fractional-frame bake agreement, then
reconcile earlier files with the current quaternion finger and elbow/weight
revision. Confirm meaningful figure distinctions and rumba timing through visual
playback. Continue the remaining catalog, add presentation positions and transitions,
then validate surfaces, contact phases and game imports before registering clips.
A complete repertoire and production-ready exports remain outstanding.

Read-only verification, from `/workspace/sanjo-solutions/apps/a-game`:

```bash
GODOT=/workspace/.cloud-onboarding/bin/godot python tests/run_tests.py --suite fast
blender -t 4 -b --factory-startup animations/man_and_woman/shared_scene_data.blend \
  --python-exit-code 1 --python scripts/validate_solo_rumba.py -- \
  --existing-only --output .cache/solo_rumba/resumed_validation.json
python tests/run_tests.py --list
GODOT=/workspace/.cloud-onboarding/bin/godot BLENDER=/home/agent/.local/bin/blender \
  python tests/run_tests.py
```

After renewed authorization and fixes, regenerate a focused clip first:

```bash
blender -t 4 -b --factory-startup animations/man_and_woman/shared_scene_data.blend \
  --python-exit-code 1 --python scripts/create_solo_rumba.py -- \
  --figure basic_in_place --character man
```

The same generator with no arguments attempts the full 104-clip catalog and
writes the active update registry. Review and correct the known issues first.
Install the checkout-backed Helpers loader for the editor as documented in
`docs/player-animation-workflow.md`; source files compose the shared scene on load.

Proposed figures/positions with no saved source at this stop:

`progressive_walks`, `backward_walks`, `forward_check`, `back_break`, `side_break`, `open_hip_twist`, `closed_hip_twist`, `advanced_hip_twist`, `spiral`, `rope_spinning`, `three_alemanas`, `three_threes`, `sliding_doors`, `fencing`, `syncopated_cuban_rock`, `new_york_left`, `hand_to_hand_left`, `shoulder_to_shoulder_left`, `switch_turn_left`, `alemana_left`, `aida_left`, `fan_left`, `hockey_stick_left`, `natural_top_left`, `new_york_right`, `hand_to_hand_right`, `shoulder_to_shoulder_right`, `spot_turn_right`, `switch_turn_right`, `alemana_right`, `aida_right`, `fan_right`, `hockey_stick_right`, `reverse_top_right`, `position_ready`, `position_closed_feet`, `position_wide`, `position_forward_check`, `position_back_check`, `position_side_lunge`, `position_crossover`, `position_fan`, `position_aida`, `position_presentation`.

## Integration record

The preservation commit records the above pre-integration state. Integration uses
fresh `origin/main`, retains concurrent work, and pushes with ordinary Git history.
Task and integration commit IDs are supplied in the delivery response; this file's
commit can be resolved using `git log -- docs/animation_work_status/solo_rumba_status.md`.

After the preservation commit, the task rebased onto `18e528c73` from origin/main.
That concurrent commit adds `scripts/blender/install_animation_tools.py` and bundled
Game Rig Tools; use the current `scripts/blender/README.md` for resumed setup.
The measurements above remain evidence for the source dependencies at the original
stopping revision; revalidate against updated shared scenes before reuse.
The root storage-policy check passed after rebase for all 23,427 staged files.
Post-rebase verification: the current fast suite passes **10/10**, 6.98 seconds;
see `solo_rumba_evidence/post_rebase_fast.log`. Animation generation and rendering
remain stopped. The `# Animation` section now links this status and describes the
solo-export rig/clip inventory check.

During final integration, the concurrent Animation guidance required isolating
stale exports with `.gdignore`. The 16 provisional GLBs and their saved import
metadata were moved byte-for-byte into `output/solo_rumba/partial_exports/`.
Their hashes remain identical; the inventory reflects their delivery paths.
A `.gdignore` also protects this record's media evidence from Godot import.
The saved Blender sources remain in the existing ignored per-animation directory.
The validator supports the isolated exports; the generator remains stopped.
Final integration verification: all 36 preserved binary hashes and staged sizes
match the inventory; the four task Python scripts compile. The integrated fast
suite passes **10/10**; see `solo_rumba_evidence/integrated_fast.log`.
