# Bhangra solo animation work status

Recorded: 2026-10-02 (Europe/Berlin). Author: Codex.
Chat/task title: Bhangra solo animations for man_and_woman3.blend.
Project: A-Game, `apps/a-game`, sanjo-solutions cloud environment.
Task branch: `codex/bhangra-solo`.
Commit at stop: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.

## Stop instruction and delivery state

The user explicitly stopped ongoing animation work and requested recording,
commit, integration, and delivery of the present state. Authoring and rendering
stopped. The final in-flight authoring command had already failed before this
instruction; its subsequent read-only verification was allowed to finish.
All task Blender processes have exited. The broad related-test runner and its
Godot editor child were terminated after unrelated missing-asset/import failures.

**These 48 clips are partial procedural blocking studies, not a completed or
production-validated Bhangra library.** Each character has 24 saved editable
sources, 24 baked actions inside those sources, and 24 individual GLBs. The
saved sources predate the last finger-mode and joint-translation code changes.
The latest generator is a preserved failing investigation state. Rebuilding
requires resolving the concrete blockers below and renewed authoring authority.

The task added 48 references to `models/player/animation_updates.tres`; the
existing entries are preserved. These references currently expose partial
exports. Successful Godot import/playback of the complete update catalog has
not been established. No gameplay activity was created for these clips.

## Original scope

Create a broad organized Bhangra repertoire for both characters from
`man_and_woman3.blend`, with reusable solo clips, natural motion, planted
contacts, clearance, smooth transitions, interpolation and loop validation.
Use Blender 5.2 for authoring, scripting, baking, rendering, and export. Follow
the existing shared-scene/per-animation source workflow, reuse suitable dance
helpers, commit assets, fetch and rebase onto origin/main, document learnings
under `# Animation` in AGENTS.md, commit that documentation, merge and push.
The user's 100 MiB threshold assigns smaller assets to ordinary Git and larger
assets to Git LFS. The stop instruction supersedes further animation completion.

## Saved repertoire and timing

Each row has separate `bhangra_man_<move>` and `bhangra_woman_<move>` actions.
Man uses participant `PLAYER`; Woman uses `PARTNER`. Each source has one
character control-rig slot and a matching `<name>.baked` deform-rig action.
All clips use frames 0–96 at 24 fps (4 seconds / eight beats at 120 BPM).
Entry and exit are one-shot transitions. The remaining 44 clips are intended
loops, with frame 96 repeating the endpoint. Source poses use 33 quarter-beat
samples before constant channels reduce to one initial key. Native visual
bakes sample every integer frame. A common ready pose supports clip sequencing;
the final generated loops settle over frames 0–3 and 93–96.

| Group | Move suffixes (each saved for Man and Woman) |
| --- | --- |
| Positions | ready, high_v, open_arms, low_stance |
| Foundations | shoulder_bounce, basic_step, double_bounce |
| Footwork | side_step, heel_dig, knee_lift, front_kick |
| Named phrase studies | chaal, jhummar, luddi, dhamaal, sammi, phumman, jugni |
| Arm gestures | overhead_pump, alternating_reach, wrist_roll |
| Level change | squat_bounce |
| Transitions | entry, exit |

The named phrases are Bhangra-inspired blocking, with regional variation and
cultural/style review still required. This set is not an exhaustive inventory
of Bhangra. Turns, airborne hops, calibrated claps, prop dances, and a complete
regional movement catalog were not authored. Heel dig currently presents the
heel through a raised-foot trajectory; a true planted-heel contact remains work.

## Exact files and artifacts

[asset_inventory.json](../../output/bhangra/asset_inventory.json) lists every
one of the 48 source files, GLBs, import settings, role, frame range, loop flag,
actual binary size, and source/export SHA-256. It is the exact asset manifest.

* `animations/man_and_woman/bhangra_{man,woman}_<move>.blend`: 48 compact source
  files with editable and baked actions. Total source bytes: 20,063,195.
* `models/player/animation_updates/bhangra_{man,woman}_<move>_baked_<hash>.glb`:
  48 generated single-clip exports. Total GLB bytes: 17,795,448. Each file has
  exactly its expected `.baked` clip; JSON channel counts are in the inventory.
* Adjacent `.glb.import` files use the existing player-animation import script
  and explicit loop mode. The stopped broad test also touched these new import
  settings while attempting project import; their current state is preserved.
* `models/player/animation_updates.tres`: added references to the 48 partial clips.
* `scripts/bhangra_repertoire.py`: procedural library, IK posing, sparse channel
  authoring, native baking, source writing, and compact export. Its final
  joint-disconnection attempt raises `AttributeError` (see blockers).
* `scripts/bhangra_review.py`: 193 half-frame samples per clip; contact, reach,
  wrist, proxy clearance, foot separation, hand-step and loop diagnostics.
* `scripts/verify_bhangra_exports.py`: saved-source reopen and isolated baked
  comparison, plus GLB clip/role checks. It reports known failures.
* `output/bhangra/validation_man.json` and `validation_woman.json`: final full
  build's in-memory control-rig checks, 24/24 passed for each. These are not
  evidence of saved-source/baked equivalence.
* `output/bhangra/validation.json`: earlier draft pass, 39/48 passed before the
  settled-endpoint refinement. Preserve as historical evidence.
* `output/bhangra/validation_woman_basic_step.json`: initial single-clip study.
* `output/bhangra/validation_man_basic_step.json`: latest in-memory single-clip
  check before the failed rebake. Its clip was not saved by that failed attempt.
* `output/bhangra/export_validation.json`: latest saved Man basic-step check,
  failed. Earlier two-character comparison is described below and in logs.
* `output/bhangra/woman_basic_step_frame_30.png`: one Blender Workbench render
  of the initial woman basic-step source at frame 30, visually inspected. This
  is limited pose evidence, not full repertoire playback review.
* `output/bhangra/diagnostics/`: preserved preview, finger-mode diagnosis, and
  native-bake diagnosis scripts originally run from `/tmp`. These scripts are
  historical tools; the bake diagnostic authors transient data when invoked.
* `output/bhangra/logs/`: discovery, builds, draft, render, diagnostics, failed
  correction, export comparison, fast suite, broad-suite selection and partial
  broad-suite logs. Blender exceptions can exit with shell status 0: inspect
  traceback/report results; use `--python-exit-code 1` in subsequent commands.
* Root `.gitattributes`: exact-path ordinary-Git exceptions for the 48 new
  sources, 48 GLBs, and preview PNG. No broad storage override was introduced.

`man_and_woman3.blend`, `shared_scene_data.blend`, both anatomical source models,
and existing animation source files retain their Git contents. Required existing
LFS assets were hydrated for local use, including the shared scene, disco/idle
sources, character models, linked prop dependency, and hair test fixtures.
The existing `DiscoCharacter`, `DiscoWristPoser`, `RigYogaPoser`,
`AnimationFileWriter`, `AnimationClipScene`, and `AnimationUpdates` were reused.

## Validation results and blockers

1. Blender version: **5.2.2 LTS**, build `d13f752e3b9c`, used for all Blender work.
   Game Rig Tools is absent from this environment, so a native Blender visual
   bake was attempted with the repository's source writer and compact exporter.
2. Full generated control-rig reports: **48/48 passed in memory**, each at 193
   samples spaced 0.5 frames apart. Maximum planted ankle drift 0.000101 m;
   maximum requested endpoint error 0.000191 m; maximum wrist bend 14.993 degrees.
   Final generated loop reports show zero endpoint position/rotation and sampled
   velocity mismatches. Checks use ankle landmarks and hand-to-torso proxies;
   they do not prove sole, finger, whole-body mesh clearance, or natural style.
3. **Saved-source/bake equivalence failed.** Reopened Man basic step: maximum
   positional discrepancy 0.077565 m and orientation discrepancy 129.079 degrees,
   with finger bones worst at frame 92.5. Integer-frame maxima were 0.071881 m
   and 127.017 degrees. An earlier Woman basic-step comparison failed at
   0.014156 m / 23.083 degrees; the later full Woman build remains unverified.
4. Finger root cause: the reused dance poser changes finger controls to XYZ,
   while the shared scene stores QUATERNION. Per-animation files persist actions,
   not those shared rig-mode changes. The latest generator now writes finger
   quaternion keys, but **none of the 48 saved assets has been rebuilt with this
   correction**. The failed rebake preserved the previous source and GLB.
5. Native bake diagnosis after correcting transient finger modes still showed
   connected-joint differences: Man foot about 0.006608 m, hand 0.002178 m,
   fingertip 0.003235 m at frame 0. Independent animated joint translations were
   being investigated for bake/export copies; shared rigs must remain preserved.
6. **Current generator blocker:** assigning `bone.use_connect = False` on
   `bpy.types.Bone` raises `AttributeError: ... is read-only`. The latest bake,
   export-copy and marked-action verification branches contain this unfinished
   approach. Research the correct EditBone/context API or a compatible bake
   strategy before running them. No generated action currently carries the new
   translated-joints flag. Do not interpret the latest code as a working fix.
7. Initial fast run used Godot 4.6.3 and hit LFS-pointer hair resources. After
   hydrating those resources and selecting Godot 4.7.2, fast suite passed 9/9.
   The stop-time required fast suite again passed **9/9 in 2.87 seconds**.
8. `python tests/run_tests.py --list` selected **9 fast + 186 slow** due to the
   animation directory and update catalog. `python tests/run_tests.py` was
   started with Blender 5.2.2 and Godot 4.7.2. Fast checks passed; the first slow
   fixture emitted missing binary/import errors (including `crouch.res` and
   existing player libraries) and failed. The runner and next Godot editor test
   were terminated to honor the stop. The remaining slow checks are unverified.
   Test-induced edits to 59 preexisting `.import` files were restored to HEAD;
   no concurrent source changes were discarded.
9. Python syntax compilation passed for the three new task scripts. GLB JSON
   inspection confirmed 48 unique expected single clips. No comprehensive
   runtime playback, animated render review, or restored-source contact pass
   has completed. These are explicit completion blockers.

## Current processes and storage

No task authoring/rendering process remains. Saved output has been copied from
`/tmp/bhangra-*` into the task output directory. The fast suite completed; the
broad suite was deliberately stopped. The original command's shell success code
is insufficient for Blender Python failures, as the logs demonstrate.

All 97 task binary assets are between 213,282 and 441,729 bytes, below
104,857,600 bytes. Actual file sizes and `git check-attr filter diff merge text`
were inspected before staging; each exact-path override resolves to unset.
These assets upload through ordinary Git. This task introduces zero LFS objects.

## Resume commands and order

Further authoring requires the user's renewed instruction. For read-only review:

```bash
cd /workspace/sanjo-solutions/apps/a-game
export BLENDER=/workspace/.cloud-onboarding/bin/blender
export GODOT=/workspace/.cloud-onboarding/bin/godot
"$BLENDER" --version
python tests/run_tests.py --suite fast
"$BLENDER" -b --python-exit-code 1 --python scripts/verify_bhangra_exports.py -- bhangra_man_basic_step bhangra_woman_basic_step
```

The verification command is expected to fail on the preserved studies. Review
`output/bhangra/asset_inventory.json`, both final control-rig reports, and the
bake diagnostics first. Resolve quaternion persistence and the read-only Bone
API/connected-joint strategy before a new build. After fixing those blockers
and receiving renewed authoring authority, use these exact build entry points:

```bash
"$BLENDER" -b -y animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/bhangra_repertoire.py -- --character Man --move basic_step
"$BLENDER" -b --python-exit-code 1 --python scripts/verify_bhangra_exports.py -- bhangra_man_basic_step
# After single-clip and saved-source verification pass:
"$BLENDER" -b -y animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/bhangra_repertoire.py -- --character Man
"$BLENDER" -b -y animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/bhangra_repertoire.py -- --character Woman
"$BLENDER" -b --python-exit-code 1 --python scripts/verify_bhangra_exports.py
python tests/run_tests.py --list
python tests/run_tests.py
```

Rebuild every saved source/export after the finger fix; remeasure planted soles,
interpolated hand/finger/body clearance, angular and linear loop velocities, and
transitions on reopened sources and exported clips. Complete actual motion
playback and cultural/style review. Reinspect binary sizes/attributes before
staging. Preserve concurrent update-catalog references by taking the union of
resource paths when resolving a rebase conflict. Use ordinary history-preserving
pushes and verify task-commit ancestry in remote main.

## Integration record

This status is committed together with the preserved assets. The task's final
chat response records the task/documentation/merge hashes and verified remote
main hash, avoiding a self-referential commit hash in this file. GitHub commit
communications for this delivery are authored by Codex.

### Post-stop integration update

The asset/status commit rebased onto `18e528c73` as `b4dc616a9`.
Concurrent main introduced generated size-based Git storage rules and bundled
Game Rig Tools. The `.gitattributes` conflict was resolved by retaining main's
generated policy; the task's earlier exact-path ordinary-Git exceptions became
redundant and were removed during rebase. All 97 task binaries remain full
ordinary-Git blobs, with unchanged inventory hashes. The repository-wide
`python scripts/lfs_policy.py check` passed for 23,530 staged files.

Main now documents `scripts/blender/install_animation_tools.py` and
`scripts/blender/README.md`. On a future authorized resume, review that bundled
Game Rig Tools setup before continuing the preserved native-bake experiment.
No add-on installation, animation repair, or rebake was performed after the stop.
Two focused notes were added under AGENTS.md's Animation section: the read-only
Bone connectivity API and the explicit paused Bhangra study status.

The post-rebase fast suite expanded to ten checks and completed **9/10** in
5.26 seconds. `playground/activity_import/test_activity_json.gd` failed because
seven hair-model GLB imports (`bob01`, `bob02`, `short01` through `short04`, and
`afro01`) were unavailable to Godot; dependent Character scripts then failed to
compile. This is an environment/import blocker on the newly fetched main, and
is recorded in `output/bhangra/logs/bhangra-post-rebase-fast.log`. The earlier
stop-time 9/9 result applies to the pre-rebase checkout. Asset/source SHA-256
checks passed after rebase for all 96 source and export binaries. The stop
instruction prioritizes preserving this explicit partial state over repairing
additional environment or animation work.
