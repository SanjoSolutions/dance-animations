# Cha Cha Slide — stopped work record

Recorded by Codex on October 2, 2026, at 16:58 Europe/Berlin (CEST).
Chat title: **Create Cha Cha Slide animations**.
Chat ID: `01a0fd0b-2451-706e-95ed-277b887eb071`.
Environment: `sanjo-solutions`; checkout `/workspace/sanjo-solutions`;
app `apps/a-game`; task branch `codex/cha-cha-slide`.
Starting/current pre-preservation commit: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
The commit containing this record identifies the preservation revision through Git history.

## Stop instruction and scope

The original request covered the complete Cha Cha Slide move/position vocabulary,
independent solo motion for Man and Woman, Blender 5.2 authoring/render/export,
per-animation sources, natural motion/contact/clearance/loop checks, existing
animation reuse, Git storage through 100 MiB, commits, rebase onto origin/main,
Animation guidance, integration into main, and push.

The user's coordinated stop instruction superseded further animation work.
This is a **partial procedural blocking study**, with one saved groove source and
an earlier pending export. It is **not a completed Cha Cha Slide repertoire**.
Authoring, refining, generation, and rendering stopped. Further animation commands
below require a later instruction to resume.

## Durable files and asset state

All paths below are relative to `apps/a-game`.

| File | State |
| --- | --- |
| `scripts/cha_cha_slide/catalog.py` | Procedural definitions for 42 cue/position/practice clips; revisions to travel and knee-reaching poses await a new full review. |
| `scripts/cha_cha_slide/author.py` | Blender 5.2 authoring, sparse curves, native visual bake, per-file writer, review, and experimental compact export orchestration. Incomplete production workflow; inspect blockers before running export. |
| `scripts/cha_cha_slide/review.py` | Evaluated half-frame authoring checks for plants, reach, ankle height, foot separation, forearm/trunk proxies, and loop positions/rotations/linear velocities. Surface collision and complete joint/wrist checks remain outstanding. |
| `scripts/cha_cha_slide/render.py` | Blender 5.2 Cycles clay preview script; explicitly unmutes the baked NLA tracks for playback. |
| `animations/man_and_woman/cha_cha_slide_groove.blend` | **Partial saved source**, 2,020,710 bytes. Contains `cha_cha_slide_groove` and `cha_cha_slide_groove.baked`, both with independent Man and Woman slots; frames 0–48 at 24 fps, 120 BPM, 4 beats, 2 seconds. Frame 48 is the duplicate loop endpoint. Composes `shared_scene_data.blend` using the existing `AnimationFileWriter`. |
| `output/cha_cha_slide/review_groove.json` | Latest saved groove authoring and baked measurements, from before the stop. |
| `output/cha_cha_slide/review_all.json` | Earlier in-memory 42-clip blocking study: 24 passing, 18 failing. This study used earlier code loaded at process start and does **not** validate subsequent catalog/handle changes. The other 41 clips exist as procedural definitions, not saved blend sources or baked exports. |
| `output/cha_cha_slide/groove_partial_preview.png` | Preserved pre-stop clay preview, 421,933 bytes. A review image, not final visual approval. |
| `output/cha_cha_slide/pending_export/cha_cha_slide_groove_baked_5d9fe098050f.glb` | Earlier **pending export**, 659,572 bytes, one `cha_cha_slide_groove.baked` animation, 1,269 channels, both deform-rig roles, frames 0–48. It predates the latest groove source/curve revision. |
| `output/cha_cha_slide/pending_export/cha_cha_slide_groove_baked_5d9fe098050f.glb.import` | Preserved earlier import settings containing stray closing braces; invalid syntax is an explicit blocker. |
| `output/cha_cha_slide/.gdignore` | Keeps pending exports and review material out of Godot import. |
| `output/cha_cha_slide/preservation_manifest.json` | Per-file byte counts and SHA-256 digests for scripts, saved asset, pending export, reports, preview, and captured logs. |
| `output/cha_cha_slide/stopped_logs/cha_review.log` | Complete earlier 42-clip study log. |
| `output/cha_cha_slide/stopped_logs/cha_build.log` | Earlier successful groove export run. |
| `output/cha_cha_slide/stopped_logs/cha_bakecheck.log` | Latest groove source/bake review and save. |
| `output/cha_cha_slide/stopped_logs/cha_render.log` | Last completed pre-stop render log. |
| `output/cha_cha_slide/stopped_logs/cha_saved.log` | Read-only saved-source discovery: authoring/baked actions, slots, NLA bindings, and preview state. |
| `output/cha_cha_slide/stopped_logs/cha_fast.log` | Passing fast-suite rerun after restoring prerequisite LFS assets. |
| `output/cha_cha_slide/stopped_logs/fast_suite_after_stop.log` | Required fast suite after the stop: 9/9 passed. |

The pending GLB and import file were moved byte-for-byte out of
`models/player/animation_updates/` during preservation. The task's temporary entry
in `models/player/animation_updates.tres` was removed by restoring its pre-task
contents; that file had only this task's edits. This retains existing runtime
libraries and avoids activating a stale partial export with invalid import syntax.
The combined `man_and_woman3.blend`, shared scene, original disco action, and
anatomical sources were read only. The combined file discovers new source files
on reopening with Player Asset Export enabled; groove remains explicitly partial.

## Earlier study inventory

Every entry targets independent Man and Woman slots, using Blender 24 fps and
120 BPM. Only **groove** has a saved authored/baked `.blend` and an earlier GLB.
All other entries below are **procedural blocking definitions / in-memory studies**.
Travel and turn cues retain displacement/facing changes; their sequencing/root
placement still needs integration review. Pass results describe the sampled checks,
not final choreography or surface approval.

| Cue | Frames | Earlier study |
| --- | --- | --- |
| position_ready | 0–48 | Passed sampled checks |
| position_freeze | 0–48 | Passed sampled checks |
| position_low | 0–48 | Passed sampled checks |
| position_hands_on_knees | 0–48 | maximum_reach_error |
| position_hands_up | 0–48 | Passed sampled checks |
| position_wide | 0–48 | Passed sampled checks |
| groove | 0–48 | Passed sampled checks |
| step_left | 0–30 | maximum_reach_error; minimum_forearm_torso_gap |
| slide_left | 0–30 | maximum_reach_error; minimum_forearm_torso_gap |
| step_right | 0–30 | maximum_reach_error; minimum_forearm_torso_gap |
| slide_right | 0–30 | maximum_reach_error; minimum_forearm_torso_gap |
| take_it_back | 0–60 | Passed sampled checks |
| take_it_forward | 0–60 | Passed sampled checks |
| hop_1 | 0–24 | Passed sampled checks |
| hop_2 | 0–48 | Passed sampled checks |
| hop_3 | 0–72 | Passed sampled checks |
| hop_4 | 0–96 | Passed sampled checks |
| hop_5 | 0–120 | Passed sampled checks |
| hop_6 | 0–144 | Passed sampled checks |
| stomp_left_1 | 0–24 | loop_velocity_error |
| stomp_left_2 | 0–48 | loop_velocity_error |
| stomp_right_1 | 0–24 | loop_velocity_error |
| stomp_right_2 | 0–48 | loop_velocity_error |
| cha_cha | 0–108 | Passed sampled checks |
| cha_cha_forward | 0–108 | Passed sampled checks |
| cha_cha_back | 0–108 | Passed sampled checks |
| criss_cross_left | 0–24 | Passed sampled checks |
| criss_cross_right | 0–24 | Passed sampled checks |
| reverse | 0–48 | Passed sampled checks |
| turn_left | 0–36 | Passed sampled checks |
| turn_right | 0–36 | Passed sampled checks |
| turn_around | 0–60 | Passed sampled checks |
| hands_on_knees | 0–72 | maximum_reach_error; loop_velocity_error |
| hands_up | 0–72 | loop_velocity_error |
| get_low | 0–72 | loop_velocity_error |
| bring_it_up | 0–48 | maximum_reach_error |
| clap | 0–60 | loop_velocity_error |
| freeze | 0–48 | loop_velocity_error |
| limbo | 0–72 | loop_velocity_error |
| charlie_brown | 0–60 | Passed sampled checks |
| get_funky | 0–120 | loop_velocity_error |
| practice_sequence | 0–828 | maximum_reach_error; loop_velocity_error |

## Measurements and concrete blockers

Latest saved groove: 99 authoring samples, 424 contact samples; maximum planted
ankle drift 0.000100966 m; maximum endpoint reach error 0.000190542 m; loop position
and rotation differences zero; boundary linear-velocity difference 0.00959255 m/s.
Native baked replay: 49 integer frames; planted-foot drift 0.00124679 m;
maximum bone-head discrepancy 0.00855357 m at Man `DEF-toe.L`, frame 42.

The cloud image has Blender **5.2.2 LTS**, hash `d13f752e3b9c`. Game Rig Tools and
`models/player/.animation_cache` were absent. The checkout-backed Player Asset
Export add-on was installed locally. The experiment used Blender's native
`bpy_extras.anim_utils.bake_action_objects` with temporary COPY_TRANSFORMS
constraints, plus the existing `AnimationFileWriter`, `AnimationClipScene`,
`AnimationParticipants`, and `AnimationUpdates` helpers. Native visual bake showed
an approximately 8.55 mm toe/head discrepancy. Its cause was not conclusively
resolved; transform decomposition/inherited scaling is a lead for investigation.
The temporary bake threshold was relaxed from 2 mm to 12 mm during investigation;
this is a **study threshold**, not production-quality acceptance. Review the
existing Action Bakery path when its add-on becomes available.

Additional blockers and outstanding work:

- Full-study failures include hand reach, lateral-step forearm/trunk clearance,
  and loop boundary velocity. The report lists every failure and metric.
- Travel targets, hands-on-knees targets, and horizontal endpoint-handle widths
  were revised before stopping. Only groove received a subsequent saved review;
  the remaining revisions are unverified.
- The exporter edits `_subresources` by string slicing and leaves unmatched
  closing braces. Repair metadata handling before publication.
- The pending export is from the earlier groove revision. Re-export from the
  reviewed final source after resumed work; complete actual Godot import and
  animation-track resolution checks then.
- The authoring review uses forearm/trunk proxies and ankle landmarks. Whole-mesh
  clearance, shoe/sole support, calibrated palm clap contact, hands-on-knees
  surface contact, finger/wrist comfort, joint angles, angular loop velocity,
  every source's reopening, and practical sequencing remain incomplete.
- The current `--review-only` loop creates transient in-memory actions but writes
  only JSON reports. It exits successfully even when a report has failed checks;
  inspect `clips[].passed` and `issues`, not just the process exit status.
- Blender Python failures can still produce a successful process exit unless
  `--python-exit-code 1` is supplied. Use that flag on resume.
- The preview's first attempt used muted baked tracks and displayed the shared
  scene's old pose; its overwritten successor enables the new baked tracks.
  Final visual acceptance was not performed after the corrected render.

## Validation and process state at stop

`blender --version` confirmed 5.2.2 before any Blender operations.

The first `python tests/run_tests.py --suite fast` run passed 8/9; the activity JSON
fixture encountered LFS pointer files for `playground/hair/physics/*_mesh.res`.
Those existing assets were hydrated through the configured GitHub identity.
The rerun passed 9/9 in 3.25 seconds. The required post-stop run passed 9/9 in
3.14 seconds; see `fast_suite_after_stop.log`.

`python tests/run_tests.py --suite changed --changed scripts/cha_cha_slide/catalog.py
--changed scripts/cha_cha_slide/author.py --changed scripts/cha_cha_slide/review.py
--changed scripts/cha_cha_slide/render.py --list` selected 9 fast and 0 slow checks.

`python -m py_compile` passed for all four task scripts. A read-only binary GLB
header/length/JSON inspection confirmed GLB 2.0, one named animation and 1,269
channels. These checks do not establish Godot import or final animation quality.

The task-owned full-review process (PID 1559) was completing its practice study
when the stop arrived. A termination attempt found it already exited; its log
ends `COMPLETE 42` and `Blender quit`. The latest groove bake check and corrected
preview render had also finished. No task-owned Blender process remains.
No further authoring or rendering was launched after the stop instruction.
Temporary logs/preview were copied to the durable paths listed above.

## Storage and delivery

Actual binary sizes were inspected before staging. The saved blend, PNG preview,
and pending GLB are all below **104,857,600 bytes** and use regular Git. Before
staging, three exact-path exceptions were applied to the original blanket LFS
rules. Rebase encountered the concurrent repository-wide size-based policy; its
generated `.gitattributes` was preserved, and the now-redundant task exceptions
were dropped. `python scripts/lfs_policy.py check` passed for 23,376 staged files. This task creates zero new LFS
objects and requires no separate new LFS asset upload; ordinary Git push carries
its three binaries. Original-source hydration changed local availability only.

Task changes and this record are committed first; fetch/rebase then preserves
current origin/main, followed by a separate Animation-guidance commit. Integration
uses an ordinary history-preserving merge/push and verifies task ancestry and the
remote main commit. Commit IDs and final remote verification are reported by Codex
in the chat's delivery message. GitHub communications/commits are authored by Codex,
with exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer per new commit.

## Integration checkpoint

The preservation commit rebased onto `18e528c73` (latest fetched main at that
checkpoint) as `325c134cd`. The only conflict was `.gitattributes`, resolved by
retaining the concurrent generated size-policy file. The worktree became clean.
Concurrent commit `18e528c73` bundles Game Rig Tools and documents
`scripts/blender/install_animation_tools.py`; this resolves availability of the
installer after the original study. It was **not installed or used by this stopped
study**, and no further animation work followed the rebase. Read
`scripts/blender/README.md` and the latest Animation guidance before resuming;
the newly available Bachata baking guidance may help investigate the measured
native-bake discrepancy. The post-rebase fast suite passed **10/10** in 5.87
seconds; its log is `output/cha_cha_slide/stopped_logs/fast_suite_after_rebase.log`.
Final merge/push hashes are reported in chat.

## Exact resume commands

Run only after the user explicitly resumes animation work. Read current
`AGENTS.md`, this record, and `scripts/player_assets/paired_animation_authoring.md`
first. Preserve concurrent files and inspect current branch status.

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender --version
python tests/run_tests.py --suite fast
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
# Inspect the saved partial source in Blender 5.2 with its shared source hydrated.
blender animations/man_and_woman/cha_cha_slide_groove.blend
# Re-evaluate the revised procedural definitions. This creates only in-memory studies
# and overwrites review_all.json; preserve the stopped report first.
blender --background --python-exit-code 1 \
  animations/man_and_woman/solo_disco_dance.blend \
  --python scripts/cha_cha_slide/author.py -- --review-only
# After fixing failures and bake discrepancies, rebuild a selected source.
# This overwrites the selected source file, so review its Git state first.
blender --background --python-exit-code 1 \
  animations/man_and_woman/solo_disco_dance.blend \
  --python scripts/cha_cha_slide/author.py -- --only groove
# After reviewing metadata handling and the bake/export workflow, publish a selected clip.
blender --background --python-exit-code 1 \
  animations/man_and_woman/solo_disco_dance.blend \
  --python scripts/cha_cha_slide/author.py -- --only groove --export
# Representative geometry preview, after source/bake review.
blender --background --python-exit-code 1 \
  --python scripts/cha_cha_slide/render.py -- groove 12 /tmp/cha_cha_slide_groove.png
```

Hydrate the combined source, `animations/man_and_woman/shared_scene_data.blend`,
`animations/man_and_woman/solo_disco_dance.blend`, `man_anatomical_study.blend`, and
`woman_anatomical_study_speculum.blend` through Git LFS if they are pointer files.
Use the configured credential helper and Codex GitHub identity; keep token values
out of logs. Re-check whether Game Rig Tools has since been installed by concurrent
work before continuing the native-bake experiment.
