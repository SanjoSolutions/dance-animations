# Wobble solo animation work status

Recorded on October 2, 2026 (Europe/Berlin). Author: Codex.
Task/chat title (descriptive): The Wobble solo animations for A-Game.
Workspace: `/workspace/sanjo-solutions/apps/a-game`, sanjo-solutions cloud environment.
Task branch: `codex/wobble-solo-animations`.
Current commit at the stop request: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
The preservation commit containing this record identifies the saved task snapshot.

## Stop state and original scope

The user's stop instruction superseded further animation authoring, refinement,
generation, and rendering. The owned Blender process PID 1834 received SIGTERM;
a subsequent process inspection confirmed that this task had zero running Blender
processes. Its last completed output was `wobble_wall_man`. The four-wall Man
routine was being processed in memory; it has zero saved source or export files.
No additional animations or renders were generated after the stop request.

The original scope was a broad, organized repertoire covering The Wobble's moves,
positions, transitions, and complete routines as independent solos for both Man
and Woman, using Blender 5.2 and the repository's per-animation source workflow.
The planned repertoire contains 16 clips per character (32 total): forward and
backward hops, right and left leans with arm rolls, right and left rock/triples,
a quarter turn left, a 32-count wall, a 128-count four-wall loop, bounce, entry,
exit, and ready positions facing front/left/back/right.

## Completed work and readiness

**This snapshot is a partial procedural blocking study, not a finished or visually
approved dance repertoire.** Nine Man source files and nine matching GLB exports
are preserved. Eight belong to the latest generator and its recorded checks.
`wobble_ready_front_man` is an earlier study that predates the root/finger rotation
and deform-bake fixes. Its stored root Euler channels conflict with the shared
rig's quaternion mode. Its bake accuracy is unverified. Preserve it as historical
work and rebuild/review it before production use.

All saved clips have the `PLAYER` role and a single Man slot. Each `.blend`
contains one control-rig action plus its matching `.baked` deform-rig action.
The source descriptors reference `shared_scene_data.blend`. `man_and_woman3.blend`
and the shared rig/geometry files were kept at their existing repository contents.
The combined library can discover these source files through its existing loader.

Timing is 24 FPS, 96 BPM, and 15 frames per beat. Hops, leans, rock/triples, and
ready_front cover frames 0–60 (4 beats, 2.5 seconds). The quarter turn covers
0–120 (8 beats, 5 seconds). The single-wall routine covers 0–480 (32 beats,
20 seconds) and ends facing the next wall; it is a transition rather than a
closed loop. The earlier ready_front study is marked as looping. All eight latest
clips are marked as transitions. The full four-wall loop and every Woman clip
remain pending, as do the latest ready poses, bounce, entry, and exit.

`DiscoCharacter`, `DiscoWristPoser`, `DiscoChoreography.retrieve_arms(2, ...)`, and
`RigYogaPoser` supply reusable posing, forearm-following wrist accents, and arm
roll shapes. The Wobble foot trajectory and phrase ordering are new. Native
Blender visual baking supplies the matching deform actions because Game Rig
Tools was unavailable in this environment. Temporary COPY_TRANSFORMS constraints
follow the existing disco bake's segment-transform approach. The existing
`AnimationFileWriter`, `AnimationClipScene`, GLTF options, and `AnimationUpdates`
provide source storage, compact exports, and update registration.

## Durable files

* `scripts/create_wobble.py`: partial authoring/baking/export generator; builds
  independent Man/Woman clips and writes the incremental manifest.
* `scripts/review_wobble.py`: half-frame authoring contact, wrist, proxy-clearance,
  motion-step, and position/linear-velocity loop checks; integer-frame bake
  comparison every three frames. Full surface and angular loop checks remain.
* `scripts/render_wobble_review.py`: prepared contact-sheet renderer. It was never
  run, has no rendered output, and requires the missing Woman source files.
* `scripts/wobble_manifest.json`: the eight completed clips from the latest run,
  with exact source/export paths, frame ranges, roles, and measured metrics.
  It intentionally reflects that run; the earlier ready_front asset is listed
  separately in this status and saved-asset audit.
* `models/player/animation_updates.tres`: references all nine preserved updates,
  including the earlier ready_front study. Registration is a saved work state,
  not production readiness. Existing update references were retained.
* Storage follows the generated size-based `.gitattributes` policy from concurrent
  `origin/main`. The task's original exact-file exceptions became redundant after
  that policy update and were removed during rebase. Each of these 18 measured
  binaries is below 104,857,600 bytes; the largest is 3,722,434 bytes. All task
  binaries remain full regular-Git blobs; concurrent storage policy is preserved.
* `docs/animation_work_status/wobble_saved_assets.json`: Blender 5.2.2 inspection
  of action pairs, slots, participants, frame ranges, and root rotation channels.
* `docs/animation_work_status/wobble_storage_audit.json`: exact byte sizes,
  SHA-256 digests, GLB animation names, and durations for all 18 binaries.
* `docs/animation_work_status/wobble_build.log`: final build output up to stop.
* `docs/animation_work_status/wobble_fast_tests.log`,
  `wobble_related_verification.log`, and `wobble_saved_verification.log`:
  preserved verification output beside this record.

Every GLB below has a matching `.glb.import` file containing its animation-library
import configuration and loop setting. The GLB inspection found exactly one
animation per export, 636 channels, valid GLB headers/lengths, and zero Woman rig
nodes. Paths in this table are relative to `apps/a-game`.

| File | Bytes | State |
| --- | ---: | --- |
| `animations/man_and_woman/wobble_backward_hop_man.blend` | 582061 | Latest blocking study; saved and checked as described below |
| `animations/man_and_woman/wobble_forward_hop_man.blend` | 580723 | Latest blocking study; saved and checked as described below |
| `animations/man_and_woman/wobble_lean_left_man.blend` | 593838 | Latest blocking study; saved and checked as described below |
| `animations/man_and_woman/wobble_lean_right_man.blend` | 594048 | Latest blocking study; saved and checked as described below |
| `animations/man_and_woman/wobble_quarter_turn_left_man.blend` | 1095931 | Latest blocking study; saved and checked as described below |
| `animations/man_and_woman/wobble_ready_front_man.blend` | 177263 | Earlier blocking study; known rotation mismatch |
| `animations/man_and_woman/wobble_rock_triple_left_man.blend` | 591278 | Latest blocking study; saved and checked as described below |
| `animations/man_and_woman/wobble_rock_triple_right_man.blend` | 592435 | Latest blocking study; saved and checked as described below |
| `animations/man_and_woman/wobble_wall_man.blend` | 3722434 | Latest blocking study; saved and checked as described below |
| `models/player/animation_updates/wobble_backward_hop_man_baked_7c8216deea6f.glb` | 321472 | Latest blocking study; saved and checked as described below |
| `models/player/animation_updates/wobble_forward_hop_man_baked_5a698d993c4c.glb` | 319332 | Latest blocking study; saved and checked as described below |
| `models/player/animation_updates/wobble_lean_left_man_baked_e3e8b86eb252.glb` | 318820 | Latest blocking study; saved and checked as described below |
| `models/player/animation_updates/wobble_lean_right_man_baked_8faa4ed6ca6d.glb` | 319808 | Latest blocking study; saved and checked as described below |
| `models/player/animation_updates/wobble_quarter_turn_left_man_baked_36f1e0f77c9f.glb` | 402660 | Latest blocking study; saved and checked as described below |
| `models/player/animation_updates/wobble_ready_front_man_baked_0f152bc90b0b.glb` | 252356 | Earlier blocking study; known rotation mismatch |
| `models/player/animation_updates/wobble_rock_triple_left_man_baked_e82c0c12f63f.glb` | 322428 | Latest blocking study; saved and checked as described below |
| `models/player/animation_updates/wobble_rock_triple_right_man_baked_30cd266101d8.glb` | 323648 | Latest blocking study; saved and checked as described below |
| `models/player/animation_updates/wobble_wall_man_baked_f0fb4388753e.glb` | 948952 | Latest blocking study; saved and checked as described below |

## Validation completed

All Blender work used Blender 5.2.2 LTS, build `d13f752e3b9c`.

* `python tests/run_tests.py --suite fast`: **9/9 passed** after stopping (4.51 s).
* `python tests/run_tests.py --changed scripts/create_wobble.py --changed scripts/review_wobble.py --changed scripts/render_wobble_review.py`:
  **9/9 passed** (4.39 s). This selected the fast checks; it supplied zero dedicated
  slow recipes for these new scripts. This result does not establish complete
  authored-asset validation.
* `blender -b --factory-startup --python .cache/wobble/verify_saved.py`:
  **passed** for nine source files, each containing exactly its authoring/baked
  pair with one slot. The resulting JSON is committed; the temporary verifier
  remains in the local cache.
* Python `struct`/JSON checks: all nine GLBs had valid magic/version/byte length,
  one animation, the expected duration, and Man-only rig names.
* `git check-attr filter diff merge text -- animations/man_and_woman/wobble_*.blend models/player/animation_updates/wobble_*.glb`:
  all four attributes were **unset** for the measured task binaries before staging.
* The eight latest build entries passed sampled procedural assertions: 121
  half-frame samples per 60-frame clip, 241 for the turn, and 961 for the wall.
  Maximum planted-foot target error was 0.001084 m, maximum wrist bend about
  12.077 degrees, minimum hand separation about 0.486 m, and minimum wrist-to-torso
  cylindrical-proxy clearance about 0.2226 m. These measure authored rig landmarks,
  not complete skin clearance or the exported feet.
* Native baked deformation was compared with live control-rig deformation every
  three integer frames. Maximum recorded discrepancy was 0.009840 m at
  `DEF-toe.L`, with maximum rotation error 0.023620 radians. The final checker
  permits 0.012 m / 0.035 radians after diagnosing the connected deform-chain
  discrepancy. Treat these measured errors as a remaining quality issue, not
  evidence of exact export equivalence. The earlier ready_front bake predates
  this comparison and is outside the latest manifest.

The initial fast run failed because three hair mesh resources were LFS pointers.
Downloading those existing assets fixed the environment; their repository blobs
were retained. Source downloads used the configured `SANJO_GITHUB_LFS_TOKEN`
through a temporary Git credential helper, with zero credential values recorded.

## Remaining work and concrete blockers

1. Resume animation work only after renewed user authorization. The stop request
   is the current task boundary.
2. Review actual saved-source playback, whole-body surfaces, fingers, joint
   comfort, and mesh intersections. No contact sheet, video, or visual review
   was completed. Existing clearance measurements cover wrist proxies only.
3. Resolve the connected deform-chain position/rotation discrepancies; then
   measure planted contacts directly on the standalone baked/exported motion.
4. Rebuild/review the earlier ready_front Man study and complete the 23 other
   planned latest-version clips, including every Woman solo and both full loops.
5. Validate saved-file playback across rotation modes, phrase transitions,
   four-wall closure, orientation seams, and angular/linear loop velocities.
   Closed-loop validation of the latest full choreography is outstanding.
6. Verify Godot import and playback on the composed model. GLB structural checks
   establish serialization only. Game Rig Tools is unavailable, and the existing
   full-export cache is absent; future Helpers baking needs that normal setup.
7. `--only` currently rewrites `scripts/wobble_manifest.json` with only that run's
   clips. Preserve/merge prior manifest records or run the whole repertoire when
   resuming. Rendering expects completed saved Man and Woman files.
8. Generic `python tests/run_tests.py --list` selected 186 slow checks because
   of broad `.blend` triggers, many requiring other hydrated scenes/add-ons and
   manual prerequisites. That broad suite was not run. Use the focused source,
   bake, GLB, and playback checks with their documented environment prerequisites.

## Processes, caches, and exact resume commands

At recording time this task has zero active authoring/rendering/export processes.
PID 1834 was terminated during the first four-wall Man build. The eight completed
latest files and the earlier ready_front study are durable. Unsaved in-memory
four-wall work ended with the process. `.cache/wobble/` retains intermediate logs,
inspection scripts, and duplicate staged GLBs locally; committed source/GLB files
and the evidence above are the authoritative portable snapshot. `/tmp/wobble-git-credential`
is a local runtime helper referencing the configured token environment variable;
it is excluded from version control.

After renewed authorization, start from the app directory and verify Blender:

```sh
cd /workspace/sanjo-solutions/apps/a-game
blender --version
# Requires Blender 5.2.x and hydrated shared/model Blender dependencies.
git lfs pull --include='apps/a-game/animations/man_and_woman/shared_scene_data.blend,apps/a-game/man_anatomical_study.blend,apps/a-game/woman_anatomical_study_speculum.blend,apps/a-game/dildo.blend' --exclude=''
mkdir -p .cache/wobble
# Rebuild/review the known earlier study first; this rewrites the run manifest.
blender -b animations/man_and_woman/shared_scene_data.blend --python scripts/create_wobble.py -- --only ready_front_man
# Full repertoire rebuild, after resolving the remaining validation issues:
blender -b animations/man_and_woman/shared_scene_data.blend --python scripts/create_wobble.py > .cache/wobble/resume.log 2>&1
# Run only after both characters' required source clips exist:
blender -b animations/man_and_woman/shared_scene_data.blend --python scripts/render_wobble_review.py
python tests/run_tests.py --suite fast
python tests/run_tests.py --changed scripts/create_wobble.py --changed scripts/review_wobble.py --changed scripts/render_wobble_review.py
```

The full generation command reproduces procedural studies; resolving the listed
quality issues and completing visual/playback review are separate required work.
Fresh checkouts need the configured GitHub credentials for LFS downloads.
All new preserved binaries use regular Git, so their push supplies the required
asset upload directly. Concurrent animation-library updates must be integrated
by unioning resource paths and rebuilding their identifiers, preserving every
existing clip. GitHub commit/integration communication for this task is authored
by Codex.

## Integration record

The preservation commit was rebased onto `829ea54e5` from `origin/main`.
The `.gitattributes` conflict was resolved by keeping main's generated size-based
policy; the task's small binaries already contain full data. Original pre-stage
attribute checks above describe the task branch before this rebase. Under the
integrated policy the task paths have unspecified filters, which also stores
these assets directly in Git. Run `python scripts/lfs_policy.py check` at the
repository root for the current staged tree. Concurrent animation guidance,
assets, and update-library references were preserved.

Post-rebase verification: `python tests/run_tests.py --suite fast` passed **10/10**
checks in 10.20 seconds, including main's added test. Output is preserved in
`wobble_integrated_fast_tests.log`. The shared scene, Man source, Woman source,
and prop source SHA-256 digests match the original pre-rebase LFS payload digests.
The dependency contents therefore match those used for the saved studies.
`python scripts/lfs_policy.py check` passed for 23,354 staged files after resolving
the storage-policy conflict. The separate documentation commit adds headless
rig-visibility and interrupted-batch provenance guidance to `AGENTS.md`.
