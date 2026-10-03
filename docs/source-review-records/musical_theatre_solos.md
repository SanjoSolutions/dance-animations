# Musical-theatre solos: stopped-work checkpoint

Date: October 2, 2026 (Europe/Berlin).
Chat/task title: Musical-theatre solo animations for man_and_woman3.blend.
Repository: SanjoSolutions/sanjo-solutions, project A-Game, `apps/a-game`.
Task branch: `animation/musical-theatre-solos`.
Rebased checkpoint commit: `89ac7d9f59f3a3230f6a46f4ca60c066fee0b3cc`.
Starting/current HEAD when animation work stopped: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
Author of this record and task commits: Codex.

The user's stop instruction superseded further animation authoring, refinement,
generation, and rendering. This checkpoint preserves present outputs for later
review. **All 68 clips are procedural blocking studies with partial validation;
production animation acceptance remains outstanding.** The scripts' measured
metrics are diagnostic results, rather than a comprehensive pass/fail gate.

## Original scope and completed scope

The original request was a broad musical-theatre repertoire for both characters
from `man_and_woman3.blend`, with independent solos, natural movement, planted
contacts, clearance, transitions, interpolated-motion and loop validation,
reuse, Blender 5.2 throughout, per-animation files, Git storage through 100 MiB,
commits, rebase, Animation documentation, merge, asset publication, and main push.
Musical theatre has an open repertoire; these families represent a bounded study,
rather than an exhaustive inventory of every dance vocabulary or position.

Blender **5.2.2 LTS**, build `d13f752e3b9c`, performed authoring, native visual
baking, glTF export, rendering, and saved-source inspection. The existing
`DiscoCharacter`, `RigYogaPoser`, and forearm-relative `DiscoWristPoser` were
reused. The source scene was `animations/man_and_woman/solo_disco_dance.blend`
composed with the existing shared scene. Existing disco actions, shared rigs,
geometry, anatomical source files, and combined library were preserved.

There are **34 families × 2 independent character variants = 68 source files**:

* Positions: first, second, fourth, fifth, jazz lunge, demi-plie, jazz parallel.
* Steps: step touch, grapevine, jazz square, ball change, chasse, pas de bourree,
  mambo, Charleston, heel dig.
* Balances and kicks: passe, arabesque, attitude, front kick, side kick,
  flick kick, fan kick.
* Performance: jazz hands, port de bras, shoulder isolation, hip sway,
  body roll, bow, curtain call.
* Turns: step turn.
* Jumps: saute, star jump, echappe.

Every source contains exactly one editable authoring action and one `.baked`
action. Man clips contain the `Man.rigify` / `Man.rigify_deform` slots and
`PLAYER` participant metadata. Woman clips use the corresponding Woman slots
and `PARTNER`. Each clip uses frames **0–120 inclusive at 24 fps**, a five-second
range with matching endpoints. Common neutral opening and finish poses support
future transitions; arbitrary cross-clip blending remains a future review item.
Stationary authoring channels carry one initial key. Moving channels carry sparse
Bezier keys. Baked actions sample integer frames 0–120. Source action markers
label Neutral, Preparation, Phrase, Recovery, and Loop endpoint.

All 68 clips also have individual compact GLB exports and `.glb.import` settings.
The existing `AnimationClipScene`, glTF options, `AnimationParticipants`,
`AnimationUpdates`, `AnimationFileWriter`, and track-binding helpers were used.
The build initially registered 68 references. During delivery, the newly fetched
repository guidance required paused studies outside the active runtime registry.
The 68 GLBs and their import files were moved byte-for-byte into
`docs/animation_work_status/musical_theatre_solos/exports/`, beneath `.gdignore`.
Only this task's 68 catalog references were removed; all 19 current-main references
were retained. **These exports are preserved, provisional, and runtime-unregistered.
Godot import/playback of this new set remains unverified.**

## Files and precise inventory

[Asset inventory](musical_theatre_solos/asset_inventory.md) lists every source,
export, and retained preview. [Saved-asset audit](musical_theatre_solos/saved_asset_audit.json)
records exact source/export/import paths, sizes, SHA-256 hashes, slots, frame
ranges, channel counts, and durations for each clip.

Task scripts and reports:

* `scripts/musical_theatre/choreography.py`: sparse pose scores for 34 families.
* `scripts/musical_theatre/build.py`: character posing, sparse action writing,
  native visual baking, source-file serialization, compact export, diagnostics.
* `scripts/musical_theatre/review.py`: half-frame authoring endpoint, wrist,
  hand/torso proxy, plant, and loop measurements.
* `scripts/musical_theatre/render_review.py`: saved-bake Workbench render inspection.
* `scripts/musical_theatre/audit_saved.py`: read-only source and GLB structural audit.
* `scripts/musical_theatre/validation.json`: numerical results for all 68 clips.
* `docs/animation_work_status/musical_theatre_solos/`: inventory, storage audit,
  source audit, build/render/test logs, and 15 original PNG render samples.
* Root `.gitattributes`: current main's generated size-based storage policy; all task binaries remain ordinary Git blobs.
* `models/player/animation_updates.tres`: current-main references retained; task studies stay outside the active catalog.

The retained 15 renders cover first position and jazz square for both characters,
and passe for Man, each at frames 30, 48, and 84. Two images (Man jazz square at
48; Woman first position at 48) received direct visual inspection before the stop.
The render process enumerated available sources while the build was running;
Woman passe was outside that captured list. Full playback and other views remain
outstanding. These are neutral anatomical-model motion-review images.

## Validation performed

Commands ran from `/workspace/sanjo-solutions/apps/a-game`.

* `GODOT=/workspace/.cloud-onboarding/bin/godot python tests/run_tests.py --suite fast`
  — **9/9 passed**, including the final stopped-work run (9.15 seconds).
  Earlier use of the system Godot 4.6.3 with pointer-only hair assets produced
  8/9. Hydrating cached LFS assets and selecting installed Godot **4.7.2** resolved
  those environment prerequisites. Logs preserve the successful runs.
* `blender -t 2 -b --factory-startup --python scripts/musical_theatre/audit_saved.py`
  — **passed** for all 68 sources, 136 actions, and 68 solo GLBs. Verified roles,
  one slot per action, action family, 0–120 range, five-second exports, one clip
  per GLB, character rig isolation, binary headers, and file hashes.
* `blender -t 2 -b --factory-startup --python scripts/player_assets/test_animation_files.py`
  — **1 test passed**. Its deliberate linked-file rename/missing-library fixture
  emits warnings; the unittest result is OK.
* `blender -t 2 -b --factory-startup --python scripts/player_assets/test_single_animation_layout.py`
  — **passed**: inactive prop rest and animated prop publication layout.
* The original build measured each authoring action at **241 half-frame samples**.
  Maximum authoring plant drift: **0.1553 mm**. Maximum hand/foot IK reach error:
  **0.2198 mm**. All sampled loop endpoint position/orientation errors and
  boundary linear-velocity differences were zero. The minimum measured
  hand-to-torso capsule-proxy clearance was **112.9 mm**. This proxy is a local
  diagnostic, not a mesh-intersection or whole-body clearance certificate.
* Baked landmark and planted-foot samples ran at every integer frame. The maximum
  plant drift was **15.55 mm (Man step turn)** and **12.52 mm (Woman step turn)**.
  Other clips peaked at **3.37 mm**. Native bake/source landmark discrepancy
  reached **12.24 mm**. These deviations remain unresolved.
* Maximum authoring wrist bend was **20.68 degrees** in Woman step turn. A planned
  20-degree review threshold would flag both turn variants; the script records
  metrics but currently asserts neither this threshold nor foot-drift thresholds.
* Source loading was exercised for the first-position files with the repository's
  `animation_file_startup.py`. Complete combined-library rediscovery and runtime
  model track resolution remain outstanding.

The broad changed-file test selection expands through `animation_updates.tres`
to numerous gameplay systems. The stopped-work checkpoint ran the required fast
suite, two focused Blender workflow checks, and the saved-asset audit. It does
not claim the broad gameplay suite passed.

After rebasing onto `074c6a02e`, the current fast suite **passed 10/10** in
9.56 seconds, and the saved-asset audit passed again at the archived export paths.
The repository-wide `python scripts/lfs_policy.py check` passed for all 24,338
staged files. All 151 task binaries were also checked against their full Git-blob
sizes. Delivery moved only paths: source/export/import SHA-256 payloads match the
original preservation commit. Post-rebase logs are in the evidence directory.

## Concrete blockers and remaining work

1. **Deform bake plant fidelity:** resolve the turn drift and smaller plant offsets
   before production acceptance. The shared target rigs' connected-bone and
   scale-inheritance behavior differs from control-rig evaluated deformation.
   This is a suspected source of conversion error, not an established diagnosis.
2. **Game Rig Tools was absent from the authoring environment.** The checkpoint
   uses Blender's native `bpy_extras.anim_utils.bake_action_objects` with temporary
   full-transform followers, preserving the source/action-file workflow. The
   normal Action Bakery button path remains unverified here. No shared rig or
   add-on replacement was committed. The subsequent rebase onto `074c6a02e`
   brought in `scripts/blender/install_animation_tools.py`, bundled tools, and
   `scripts/player_assets/bachata_motion.py` longitudinal-axis bake guidance.
   Those arrived after the stop; installation and bake changes were deferred.
3. **Godot integration:** compact exports include one selected deform rig and a
   skin marker. Verify bone track paths against the actual model, import all
   clips, configure intended Godot loop settings, and review participant behavior.
   `.glb.import` files currently inherit the full-library import settings (including
   unrelated animation entries); per-clip cleanup remains pending.
4. **Animation quality:** these are sparse procedural blocking phrases, not finished
   choreography. Verify weight transfer, support polygons, toe/sole clearance,
   body/arm/leg intersections, finger splay, spotting, jump timing, and full
   playback. Body clearance currently covers hand/torso proxies only. The foot
   turns and jumps require particular review. Hold entries do not establish every
   named ballet/theatre position's stylistic accuracy.
5. **Review coverage:** remaining rendered views, subframe baked/export checks,
   angular seam velocity, full mesh contacts, and cross-clip transitions await
   explicit authorization to resume animation work.
6. Newly fetched rig guidance identifies additional saved-playback risks: this
   generator changes finger controls to XYZ in its temporary scene while shared
   Rigify controls use quaternion rotations. Its group turn reads child matrices
   after moving parents; a parent-first snapshot review is required. These are
   concrete review targets preserved at the stop, rather than repaired clips.
7. `build.py` overwrites its selected task source/export outputs and replaces
   `validation.json` with that invocation's subset. Preserve the checkpoint report
   before any later selective regeneration. It is a batch-authoring tool, with
   diagnostic checks still awaiting production thresholds.

## Processes, saved outputs, storage, and delivery

At the stop instruction, the owned full-build and render processes had already
finished successfully; their terminal sessions were reaped. No animation,
authoring, or rendering process remained running. No further animation was
created or refined after the stop. Subsequent Blender invocations were verification
of saved assets or repository test fixtures. Temporary `/tmp/theatre_*.log` output
was copied into the durable evidence directory where relevant. Generated previews
were copied unchanged out of `.cache/musical_theatre_review/` into this checkpoint.

Before staging, actual binary sizes and effective Git attributes were inspected.
All **151 task binaries** (68 BLEND, 68 GLB, 15 PNG) are under 104,857,600 bytes;
the largest is **2,287,639 bytes**. Initial exact-path exceptions stored every task
binary directly in Git. Current main had independently converted repository
storage to `scripts/lfs_policy.py`; delivery adopted its generated attributes and
rechecked all task blobs. The task introduces **zero new LFS objects**, so ordinary
Git push uploads every new asset. Shared/anatomical/disco assets were originally
hydrated for reading; concurrent main's storage conversion is preserved.
`storage_audit.json` records final per-file sizes and effective attributes.

This status and all durable task assets are committed as a preservation checkpoint.
Integration fetches current `origin/main`, preserves concurrent additions to
`.gitattributes` and `animation_updates.tres`, and uses ordinary history-preserving
pushes. Commit and verified remote-main hashes are reported by the delivering chat;
this document records the pre-checkpoint base rather than a self-referential hash.

## Exact resume and verification commands

Verification can run while the stop remains in effect:

```bash
cd /workspace/sanjo-solutions/apps/a-game
export GODOT=/workspace/.cloud-onboarding/bin/godot
export BLENDER=/workspace/.cloud-onboarding/bin/blender
"$BLENDER" --version
python tests/run_tests.py --suite fast
"$BLENDER" -t 2 -b --factory-startup --python scripts/musical_theatre/audit_saved.py
"$BLENDER" -t 2 -b --factory-startup --python scripts/player_assets/test_animation_files.py
"$BLENDER" -t 2 -b --factory-startup --python scripts/player_assets/test_single_animation_layout.py
```

After the user explicitly resumes animation work, first preserve existing reports
and diagnose bake drift. Open a current source with the helpers:

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender animations/man_and_woman/musical_theatre_step_turn_man.blend \
  --python scripts/player_assets/animation_file_startup.py
```

The original generator still targets the runtime update directory: revise its publication
step to use an isolated pending directory before executing it on resumed work.
The original generator and renderer commands (these overwrite task outputs and
are for an authorized resumed authoring session):

```bash
blender -t 2 -b animations/man_and_woman/solo_disco_dance.blend \
  --python scripts/player_assets/animation_file_startup.py \
  --python scripts/musical_theatre/build.py -- step_turn
# Omit "-- step_turn" to regenerate all 34 families for both characters.
blender -t 2 -b animations/man_and_woman/musical_theatre_first_position_man.blend \
  --python scripts/player_assets/animation_file_startup.py \
  --python scripts/musical_theatre/render_review.py -- step_turn
```
