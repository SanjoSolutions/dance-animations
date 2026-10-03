# Voguing repertoire — paused work status

Recorded on **October 2, 2026, at 16:56 Europe/Berlin (14:56 UTC)**.

Task/chat title: **Voguing repertoire for man_and_woman3.blend** (descriptive task title).
Project: A-Game, `apps/a-game`, sanjo-solutions cloud environment.
Task branch: `codex/voguing-repertoire`.
Commit at the stopping point: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
GitHub delivery and commit communications for this checkpoint are authored by Codex.

The user directed all active animation chats to stop authoring and preserve their
present state. Authoring, refinement, baking, generation, and rendering stopped.
The latest owned Blender process had already exited on a validation failure.
The process inventory at the stopping point contained zero active task Blender,
render, test, or LFS-transfer processes. Subsequent commands performed recording,
verification, storage inspection, and Git delivery.

## Original scope and present result

The original request covered a broad organized solo voguing repertoire for both
characters in `man_and_woman3.blend`, using Blender 5.2, reusable motion, sparse
IK keys, planted contacts, body clearance, smooth transitions, interpolated
motion/loop checks, and the per-animation file workflow. Delivery included
animation commits, rebasing onto origin/main, helpful additions to the app's
Animation instructions, and merging/pushing main. Assets at or below
104,857,600 bytes belong directly in Git; larger assets use LFS.

**This checkpoint contains procedural blocking studies and one partial saved
animation. Production-ready voguing animations completed: zero.**

- Drafted 28 named phrases with Man/PLAYER and Woman/PARTNER variants: 56 intended
  solo clips. Most actions existed only in temporary Blender processes during
  review; their reproducible procedural descriptions are preserved in Python.
- Reused `RigYogaPoser`, the disco character proportion/foot calibration and
  forearm-following wrist helper, plus disco step-touch footwork. Existing
  animation sources, shared geometry, and rigs retain their original files.
- Created one per-animation source with an authoring action and matching baked
  action, plus its individual GLB/import settings. The source reopens, but its
  reopened baked pose fails comparison against the authoring pose.
- Preserved eight Blender solid-shaded contact-sheet renders from intermediate
  studies. These images show earlier revisions, including known floor/dip issues;
  they serve as review evidence, rather than approved final choreography.
- Restored the production `models/player/animation_updates.tres` to its branch
  base because its sole task edit activated the partial clip. The generated
  registry is preserved as `partial_animation_updates.tres.txt` in the evidence
  directory. The partial source remains discoverable in Blender's animation
  directory. Its GLB remains saved on disk but has no task-added active game
  library reference.

## Saved animation and export

| File relative to apps/a-game | State |
| --- | --- |
| `animations/man_and_woman/vogue_pose_box_woman.blend` | Partial source; 549,542 bytes; contains `vogue_pose_box_woman` and `vogue_pose_box_woman.baked`; one Woman slot in each action; role PARTNER; 24 fps; frames 0–48; cyclic; intended 2-second held box pose with breathing |
| `models/player/animation_updates/vogue_pose_box_woman_baked_b495ca791e61.glb` | Partial export; 325,840 bytes; one `vogue_pose_box_woman.baked` clip, 630 channels, 2-second duration; exported in Blender 5.2.2; game import/playback remains pending |
| `models/player/animation_updates/vogue_pose_box_woman_baked_b495ca791e61.glb.import` | Individual animation-library import configuration, 24 fps, forward loop setting |

The source descriptor references sibling `shared_scene_data.blend`. Keep the
source in its existing directory. The combined `man_and_woman3.blend` itself
received zero task edits. There is no saved Man voguing animation and no other
saved voguing source or export at this checkpoint.

## Procedural repertoire and timing

All names use `vogue_<phrase>_<man|woman>`. Each variant has exactly one intended
participant: Man/PLAYER or Woman/PARTNER. All timing is 24 fps, starts at frame 0,
and includes a closing interpolation endpoint for loops.

| Phrase suffixes | End frame | Intended playback |
| --- | ---: | --- |
| `pose_ready`, `pose_box`, `pose_face_frame`, `pose_high_v`, `pose_diagonal` | 48 | Loop |
| `old_way_lines`, `old_way_boxes` | 96 | Loop |
| `new_way_angles`, `new_way_arm_weave` | 96 | Loop |
| `hands_face_framing`, `hands_wrist_fans`, `hands_figure_eight` | 96 | Loop |
| `body_wave`, `step_touch_frames` | 96 | Loop |
| `catwalk_left`, `catwalk_right`, `duckwalk_left`, `duckwalk_right` | 96 | Loop, in place |
| `spin_left`, `spin_right` | 96 | Loop, one full pivot turn |
| `stand_to_duckwalk`, `duckwalk_to_stand` | 48 | Once |
| `duckwalk_to_floor`, `floor_to_duckwalk` | 96 | Once |
| `floor_seated_hands` | 48 | Loop |
| `dip_left`, `dip_right` | 80 | Loop, low dip and recovery study |
| `floor_leg_sweep` | 96 | Loop |

Voguing includes improvisation and dancer-specific vocabulary. This is a scoped
repertoire study covering Old Way, New Way, and Vogue Fem elements, rather than
an exhaustive catalog of every possible move or position.

## Durable implementation files

- `scripts/voguing/catalog.py`: pose descriptions, named phrases, mirrored sides,
  timing, reusable disco footwork, floor entries and recoveries.
- `scripts/voguing/author.py`: proportion-aware sparse IK authoring, stationary
  channel compaction, native visual bake, experimental hierarchical correction
  of baked transforms, per-animation source writer, compact GLB publishing.
  This draft currently stops on the Man ready-pose bake check. It is a blocking
  study, not a successful full-library build pipeline.
- `scripts/voguing/review.py`: half-frame endpoint reach, inferred foot-hold drift,
  wrist bend, hand separation, chest sphere proxy, loop pose and near-boundary
  linear velocity measurements. These are scoped geometric checks; they do not
  establish full-body collision freedom or artistic approval.
- `scripts/voguing/surface_review.py`: evaluated body mesh floor bounds at every
  third frame plus contact-sheet frames; Blender Workbench contact sheets.
- `scripts/voguing/verify.py`: reopen source files, compare constrained authoring
  and saved baked deform joints, inspect solo roles, file families, GLB channels,
  duration, and loop import settings. It currently fails on the saved partial
  source before reaching the GLB assertions. GLB structure was separately
  inspected directly during preservation.

## Validation results and evidence

Evidence directory: `docs/animation_work_status/voguing_repertoire_evidence/`.
Its `.gdignore` keeps review artifacts outside Godot asset import.

| Command/run | Result |
| --- | --- |
| `python tests/run_tests.py --suite fast` at stop | **9/9 passed**, 3.07 seconds; `fast_stop_verification.log` |
| `python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_single_animation_layout.py --changed scripts/player_assets/test_animation_export_evaluation.py` | **12/12 passed**, 7.49 seconds, including fast set; `related_stop_verification.log` |
| Same focused checks plus `--changed scripts/player_assets/test_character_single_animation_export.py`, earlier | **12/13 passed**; character integration blocked by missing `.animation_cache/manifest.json`, with then-missing linked source assets also logged; `related_tests.log` |
| `blender -b --python-exit-code 1 --python scripts/voguing/verify.py` at stop | **Failed**, reopened `vogue_pose_box_woman` maximum deform-position difference **0.8507388934866976**; `reopen_stop_verification.log` |
| Full 52-variant motion/surface review before final refinements | 52 reviewed, **46 passed / 6 failed**; `final_review.log`. Issues: man's two lowering/recovery clips and four dip variants |
| Targeted lowering/recovery and dip refinement review | **8/8 passed** at that procedural revision; `refinement.log` |
| Added floor entry/recovery review | **4/4 passed** at the latest procedural revision; `transition_review.log` and `last_transition_validation.json` |
| Woman box bake/export trial | Native bake with experimental compensation completed and source/GLB saved; `bake_trial.log`. This in-process success was superseded by the reopened-source failure |
| Latest `author.py --export --surface` full build | Ready-Man motion review passed, then bake failed before writing that source: **0.005487211885431509** difference at `DEF-toe2-3.L`, frame 0; `build.log` |

Half-frame review and every-third-frame floor sampling are different coverage
sets. The logs span several procedural revisions. There is **no complete final
56-clip saved, baked, exported, reopened, and game-imported validation pass**.
The floor bounds permit 8 mm penetration and up to 25 mm minimum-surface height;
additional contact, balance, body clearance, and visual review remain warranted.

Additional preserved logs: `all_review.log`, `bake_debug.log`, `verify_trial.log`,
`reopen.log`, `modes.log`, `visual.log`, and `floor_review.log`. They record earlier
failures, local-transform diagnostics, loaded action families, and render states.

Preserved PNGs: `vogue_pose_box_woman.png`, `vogue_hands_face_framing_woman.png`,
`vogue_duckwalk_left_woman.png`, `vogue_spin_left_woman.png`,
`vogue_dip_left_woman.png`, `vogue_dip_left_man.png`,
`vogue_floor_leg_sweep_woman.png`, and `vogue_floor_leg_sweep_man.png`.

## Environment and concrete blockers

1. Blender is **5.2.2 LTS**, build `d13f752e3b9c`. The `blender` command resolves
   through `/home/agent/.local/bin/blender` into the provisioned cloud install.
   All task Blender authoring, scripting, baking, rendering, and export used it.
2. Player Asset Export was installed with the repository loader. **Game Rig Tools
   was absent** from this cloud Blender configuration at the stopping point.
   The rebased main now includes `scripts/blender/install_animation_tools.py`;
   use that bundled setup when a future instruction authorizes resumption.
   The draft uses Blender's
   native visual bake and existing repository file/export helpers as a fallback.
3. Native visual bake decomposes sheared transforms. Experimental parent-first
   compensation succeeds for the woman box in-process, but still fails for the
   man's ready pose. Diagnose this before treating bake output as final.
4. Saved-source playback differs greatly after reopening. One concrete
   compatibility concern remains unresolved: the draft changes the authoring
   root to Euler mode and finger controls to Euler modes, while the shared scene
   supplies quaternion modes. Per-animation files preserve actions rather than
   these runtime-only rig settings. Inspect rotation modes and other scene-state
   assumptions; the recorded 0.85-meter discrepancy has yet to receive a proven
   root-cause diagnosis or correction.
5. The existing character single-export integration fixture requires an initialized
   full-library export cache and Game Rig Tools. Its manifest is absent. No
   complete full-library export was run to establish those prerequisites.
6. Some early LFS fixture assets were pointer-only. Downloaded the needed base
   rigs/models, disco source, shared scene, all existing animation source blends,
   dildo library, animations GLB, and three hair mesh resources during setup.
   Downloads preserved tracked source content. Broader game import prerequisites
   may still require hydration. Godot available here reports 4.6.3.
7. Workbench produced EGL warnings but wrote the preserved PNGs. Those are static
   review images. No complete final motion video or game playback was verified.

## Storage, processes, and temporary outputs

`storage_audit.json` records exact sizes, SHA-256 hashes, and Git attributes before
and after task-scoped exceptions. Both generated animation binaries and all eight
PNGs are below 100 MiB and use ordinary Git. The initial commit used ten exact-path
exceptions against the then-current extension-wide rules. During rebase, main
already contained the generated 100 MiB policy from `scripts/lfs_policy.py`.
The conflict resolution retained main's generated `.gitattributes`; the old
extension-wide rules and now-redundant exceptions were omitted. The audit keeps
its historical before/after attributes and adds the final post-rebase attributes.
`python scripts/lfs_policy.py check` passed for 23,393 staged files after rebase.
This checkpoint creates zero new LFS objects requiring upload.

No authoring process remains running. Temporary copies remain in
`.cache/voguing/` and `/tmp/voguing-tools/`; durable logs, the last transition
report, generated-registry snapshot, and PNGs are copied into the evidence
directory. `.cache/voguing/clip.glb` duplicates the saved partial GLB. Python
`__pycache__` files are disposable and excluded from delivery.

The task's temporary Git askpass helper reads `SANJO_GITHUB_LFS_TOKEN` at runtime;
its contents include no credential value. It remains outside the repository.
Use the environment's configured authentication for future fetch/push commands.

## Resume steps and exact commands

Resume animation work only after a new user instruction authorizes it. Begin
with inspection and diagnosis; the generation command below currently fails.
Run from `/workspace/sanjo-solutions/apps/a-game` in this cloud checkout.

```bash
blender --version
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
blender -b animations/man_and_woman/vogue_pose_box_woman.blend
blender -b --python-exit-code 1 --python scripts/voguing/verify.py
python tests/run_tests.py --suite fast
python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_single_animation_layout.py --changed scripts/player_assets/test_animation_export_evaluation.py
```

After correcting rotation-mode persistence and bake fidelity, revalidate the
procedural studies with these exact commands. The source disco file provides the
shared rig scene; the builder authors independent voguing actions.

```bash
blender -b animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/voguing/author.py -- --names pose_box --characters Woman --review-only --surface
blender -b animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/voguing/author.py -- --review-only --surface
# Only after the failed fidelity checks are fixed and a new instruction permits generation:
blender -b animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/voguing/author.py -- --export --surface
blender -b --python-exit-code 1 --python scripts/voguing/verify.py
```

Then perform visual review of complete motion, floor support and clearance,
inspect half-frame and loop angular behavior, import/play the GLBs in Godot,
verify single-participant bindings against the production models, and publish
only validated clips into the active game catalog. Inspect every actual binary
size and its attributes before staging. Preserve concurrent animation sources,
shared data, and current main during integration.

## Integration checkpoint

The preservation commit was rebased onto `origin/main` at
`18e528c73`; its rebased hash is
`3769df2a9791accb6cf387e382dc65c783da9c63`.
The only rebase conflict was `.gitattributes`, resolved in favor of the concurrent
generated size policy while retaining the task's full binary blobs. Shared
animation data and concurrent task files retain the versions from main.
A subsequent documentation commit adds floor-support and paused-delivery guidance
to the app's `# Animation` section and records verification after integration.
The final response records the documentation and merge commits plus remote
verification, since those commit hashes become available after this record saves.

Post-rebase verification on the preserved task state:

- Fast suite: **10/10 passed**, 5.99 seconds (`fast_post_rebase.log`). Main added
  one fast check since the original stop snapshot.
- Focused file/layout/evaluation suite including fast checks: **13/13 passed**,
  9.84 seconds (`related_post_rebase.log`).
- Reopened partial source: the same **0.8507388934866976** deform-position
  mismatch (`reopen_post_rebase.log`); preserved as an explicit blocked asset.
