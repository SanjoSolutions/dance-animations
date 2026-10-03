# Boot Scootin' Boogie preservation status

- Recorded: 2026-10-02, UTC; preservation audit started at 15:33 UTC.
- Chat/task title: Create Boot Scootin' Boogie animations (descriptive title from the task; the sidebar title was unavailable in the retrieved recent-chat list).
- Environment: sanjo-solutions cloud, project A-Game, `/workspace/sanjo-solutions/apps/a-game`.
- Task branch: `codex/boot-scootin-boogie`.
- Current commit at preservation start: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Author of this status and GitHub delivery: Codex.
- Governing instruction: stop animation work immediately, preserve current state, verify, commit, integrate current main, and push. Further authoring, repair, baking, export, and rendering require renewed authorization.

## Original scope and exact stopping point

The original request was a broad, organized Boot Scootin' Boogie repertoire of solo
animations and positions for both characters in `man_and_woman3.blend`, authored,
scripted, rendered, and exported with Blender 5.2; reuse fitting animation tools,
validate natural motion, planted contacts, clearance, interpolation, and loops;
use the established per-animation workflow; commit assets, rebase onto current
main, add animation guidance, then merge/push and upload required assets.

The implemented choreography is an explicitly documented 32-count **house variant**,
not a verified reproduction of a particular published choreographer's dance.
The plan contains 36 phrases per actor (72 total). There are **67 saved source /
baked-action / GLB / import-setting families: 31 Man and 36 Woman**. They are
**partial procedural animation studies**, with blocking compatibility and review
work described below. Saved/baked/exported status does not establish production
readiness. Five planned Man families remain unsaved.

At the final process check, the owned batch shell PID 2814 and Blender PID 3377
had already exited; a best-effort SIGTERM found no remaining owned animation
process. The Woman batch log ends with `Blender quit` at 15:31 UTC and its report
contains all 36 outputs, including the four-wall routine and six positions.
The earlier in-memory checkpoint was stale: these final outputs **were saved**
before the preservation check, and are included here. No new authoring, bake,
export, or render was launched in preservation mode. A read-only Blender 5.2
action/rotation-mode inventory was run. The earlier aborted Godot process PID
2759 remained a zero-memory zombie owned by PID 1; it performs no work.

## Files and saved state

[Inventory](boot_scootin_boogie/inventory.json) is the exact asset manifest: all
72 planned names, role, frame range, loop mode, authored/baked/exported state,
every saved source/GLB/import path, actual bytes, SHA-256, and export verification.
[Saved-source audit](boot_scootin_boogie/evidence/saved_source_audit.json) records
both persisted actions, action slots, metadata, actual key ranges, and mismatched
finger channel paths for each of the 67 sources. Each saved family has one
editable action and its matching `.baked` action. Source role is `PLAYER` for
Man, `PARTNER` for Woman; each export contains only that actor's deform tracks.

Source files are `animations/man_and_woman/boot_scootin_<actor>_<phrase>.blend`.
Exports and `.glb.import` companions are preserved under
`docs/animation_work_status/boot_scootin_boogie/exports/`, beneath `.gdignore`.
The manifest records their current and original runtime paths and unchanged hashes.
The 67 original registrations were archived in `evidence/animation_updates_activation_draft.tres`
and removed from the active registry in accordance with the updated main-branch
AGENTS instructions for partial exports. All other tasks’ registry entries are preserved. The original combined file and shared rig/geometry
remain reference inputs and received no task modifications.

Source timing is 24 FPS, ten frames per beat (144 BPM). Bakes have half-frame
samples. Export copies use 48 FPS with doubled frame numbers, preserving duration.
Position sources hold one pose; the table shows intended playback ranges, while
the audit records actual key ranges (a constant source can have only frame 0 keyed).

| Phrase | Playback frames at 24 FPS | Mode | Man | Woman |
| --- | --- | --- | --- | --- |
| `grapevine_r` | 0–60 | once | authored / baked / exported | authored / baked / exported |
| `heel_dig_r` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `toe_touch_r` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `kick_r` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `hitch_r` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `scuff_r` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `stomp_r` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `grapevine_l` | 0–60 | once | authored / baked / exported | authored / baked / exported |
| `heel_dig_l` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `toe_touch_l` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `kick_l` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `hitch_l` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `scuff_l` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `stomp_l` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `step_touch` | 0–60 | loop | authored / baked / exported | authored / baked / exported |
| `shuffle` | 0–60 | once | authored / baked / exported | authored / baked / exported |
| `rock_step` | 0–60 | loop | authored / baked / exported | authored / baked / exported |
| `hip_bumps` | 0–80 | loop | authored / baked / exported | authored / baked / exported |
| `clap_groove` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `heel_toe_swivels` | 0–40 | loop | authored / baked / exported | authored / baked / exported |
| `step_turn_quarter` | 0–40 | once | unsaved | authored / baked / exported |
| `step_turn_half` | 0–40 | once | authored / baked / exported | authored / baked / exported |
| `pivot_turn_quarter` | 0–40 | once | unsaved | authored / baked / exported |
| `pivot_turn_half` | 0–40 | once | unsaved | authored / baked / exported |
| `jazz_box` | 0–60 | once | authored / baked / exported | authored / baked / exported |
| `walk_forward_back` | 0–100 | loop | authored / baked / exported | authored / baked / exported |
| `entry` | 0–40 | once | authored / baked / exported | authored / baked / exported |
| `exit` | 0–40 | once | authored / baked / exported | authored / baked / exported |
| `routine_32` | 0–320 | once | unsaved | authored / baked / exported |
| `routine_four_walls` | 0–1280 | loop | unsaved | authored / baked / exported |
| `position_ready` | 0–20 | loop | authored / baked / exported | authored / baked / exported |
| `position_heel_forward` | 0–20 | loop | authored / baked / exported | authored / baked / exported |
| `position_toe_back` | 0–20 | loop | authored / baked / exported | authored / baked / exported |
| `position_kick_low` | 0–20 | loop | authored / baked / exported | authored / baked / exported |
| `position_knee_hitch` | 0–20 | loop | authored / baked / exported | authored / baked / exported |
| `position_cross_behind` | 0–20 | loop | authored / baked / exported | authored / baked / exported |

### Task scripts, documentation, and review evidence

- `scripts/boot_scootin_choreography.py`: all 36 planned phrases, positions, 32-count and four-wall sequences; sparse pose schedule and foot-contact declarations.
- `scripts/author_boot_scootin.py`: Blender 5.2 generator, IK placement, review, native visual bake/hierarchy reconstruction, solo export and per-animation writer. Latest code contains improvements ahead of most saved binaries. Re-running it changes assets and is outside the stop instruction.
- `scripts/render_boot_scootin.py`: Blender Cycles CPU pose-review helper; preserved, stopped.
- `scripts/verify_boot_scootin.py`: complete-library GLB verifier; expects all 72 and therefore cannot pass this partial delivery.
- `scripts/verify_boot_scootin_sources.py`: complete-library fresh-source sampler; full successful run outstanding, and known mode mismatches block it.
- `scripts/verify_boot_scootin_import.gd`: raw Godot GLB import/track/seek check; preserved but not run.
- `scripts/boot_scootin.md`: house-variant count sheet, planned vocabulary, implementation and review instructions, with an explicit partial-state banner.
- `docs/animation_work_status/boot_scootin_boogie/verify_preserved.py`: read-only delivery verifier for the saved subset and exact hashes.
- `docs/animation_work_status/boot_scootin_boogie/audit_saved_sources.py`: read-only Blender 5.2 action inventory, including shared-rig rotation-mode compatibility.
- `docs/animation_work_status/boot_scootin_boogie/reopen_grapevine.py`: preserved diagnostic that evaluates the saved Man right grapevine without saving it.
- `docs/animation_work_status/boot_scootin_boogie/unapplied_rotation_mode_migration.py`: **unapplied, unvalidated repair proposal** copied from `/tmp`; it writes source files if executed. Preserve as a proposal only. Review/regeneration and fresh validation are required before any future use.
- Exact-file `.gitattributes` in the source, export, evidence, and evidence actor directories preserve the intended small binaries in regular Git.
- `apps/a-game/AGENTS.md`, `# Animation`: delivery documentation commit records reusable lessons about source rotation modes, world-space IK targets, fresh-source validation, and explicit partial-state preservation.

The entire pre-existing `.cache/boot_scootin/` evidence set was copied into
`docs/animation_work_status/boot_scootin_boogie/evidence/`: batch and diagnostic
logs, numerical JSON reports, test logs, 24 rendered pose PNGs (12 per actor),
and `man_sheet.jpg` / `woman_sheet.jpg`. These are **existing pose studies**, not
an animation video or exhaustive render validation of the saved library. The Man
views use later pose logic; Woman views predate the final heading/mode changes.
Render files cover grapes, heel/toe contacts, kick, hitch, hip bump, clap, turns,
jazz box, and ready stance. Preview scripts can show planned unsaved Man turns;
a preview does not establish a saved animation family.

`man_all.json` is historical: six source-review failures include the subsequently
rebuilt `step_turn_half`. The later `man_step_turn_half.json` supersedes that
entry, and `man_grapevine_r.json` / `reopen_fixed.log` supersede the earlier right
vine review. `woman_all.json` contains all 36 successful in-process source/bake
reports. The actual manifest and fresh audit are authoritative for saved state.
Other probe logs preserve failed experiments as well as successful measurements.

## Concrete blockers and remaining work

1. **66 of 67 editable sources have finger Euler channels targeting quaternion-mode shared-rig bones.** The fresh read-only audit records exact paths. The source reopen diagnostic showed an earlier mismatch up to about 0.078 m / 2.755 rad between editable and baked finger transforms. Only the rebuilt Man `grapevine_r` is clear of this mismatch and has a passing fresh evaluated comparison. The latest generator preserves shared rotation modes and drivers; most sources were created by an earlier in-process generator. Do not treat the exported/baked result as proof that the editable source reopens equivalently.
2. **Saved heel/toe swivels need further contact work.** Historical floor-reference penetration was about 0.00397 m for Man and 0.00393 m for Woman. It passed the earlier 0.012 m threshold but exceeds the final 0.003 m target. The generator contains later quarter-beat contact keys; the saved swivel files were not regenerated. This is a concrete code/binary discrepancy.
3. **Five Man families remain missing:** `step_turn_quarter`, `pivot_turn_quarter`, `pivot_turn_half`, `routine_32`, `routine_four_walls`. Their earlier attempts failed source clearance review and did not save a source or export. A later torso-heading / parent-following IK fix exists in code and supported saved Woman turns; the missing Man clips still need authoring and verification after a resume authorization.
4. **Runtime integration remains unverified.** The broad related suite encountered missing/unimported project resources (including `animations.glb` and a newly registered update), then hung during `playground/test_activity_animation_methods.gd`. The owned runner/Godot were terminated. The raw import verifier and complete source-library certification remain outstanding. Existing GLBs have valid containers/timing and preserved import settings; that is a narrower result than Godot playback readiness.
5. **Naturalness and clearance remain partially reviewed.** Half-frame numerical checks and selected clay poses cover references and conservative arm/torso proxies, not exhaustive surface collisions or every transition. Full saved-source motion review, video playback, inter-clip blends, and final visual review remain future work.
6. Game Rig Tools is absent in the environment. A native Blender 5.2 visual bake fallback plus deform hierarchy reconstruction was used and preserved. Its in-process comparisons pass for saved clips, but source-reopening compatibility still needs the work above.
7. The documented variant needs an explicit choreography choice if a specific published Boot Scootin' Boogie version is required. The task supplied no exact count sheet or footage. Existing disco/yoga/Snap Hand calibration code was reused; complete disco action motions were not relabeled as country dancing.

## Verification and results

All Blender operations used **Blender 5.2.2 LTS**, build `d13f752e3b9c`.
Godot is 4.6.3. Commands below run from `apps/a-game`.
Updated main includes bundled Game Rig Tools; the earlier absence describes the
original authoring environment. Follow the current Blender tools setup when resuming.

| Command/check | Result |
| --- | --- |
| `python tests/run_tests.py --suite fast` | Delivery rerun: **9/9 passed**, 5.43 s; `evidence/delivery_fast.log`. Earlier missing hair-mesh LFS inputs were hydrated before passing runs. |
| `python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_single_animation_layout.py --changed scripts/player_assets/test_motion_review.py --changed scripts/player_assets/test_animation_participants.py` | Delivery rerun: **13/13 passed**, 13.56 s; `evidence/delivery_focused.log`. Includes fast suite and four relevant slow checks. |
| `python docs/animation_work_status/boot_scootin_boogie/verify_preserved.py` | **67/67 saved families passed** exact hash/size/storage, solo track ancestry, finite values, monotonic 48 Hz samples, durations, loop endpoints, import settings and archived runtime state. Original registration checks passed before archival. Five planned families are explicitly missing. |
| `blender -b --factory-startup --python-exit-code 1 --python docs/animation_work_status/boot_scootin_boogie/audit_saved_sources.py` | **67 two-action source families inspected**, 66 with mismatched shared-rig finger rotation modes; read-only inventory only. |
| Fresh Man right-grapevine diagnostic, preserved `reopen_fixed.log` | Source: 121 half-frame samples passed; baked joint position error 0.0000029086 m, rotation error 0.030556 rad, 210 deform bones. |
| In-process source and bake reports | Saved clips passed the thresholds active in their batch. Typical ankle target error <0.00023 m and plant drift <0.00009 m. Review includes wrist bend, separation, floor references, arm/torso proxies, loop position/orientation/velocity and bake comparisons. Historical and final thresholds differ; this is not fresh whole-library certification. |
| `python tests/run_tests.py --changed animations/man_and_woman/boot_scootin_man_grapevine_r.blend` | **Incomplete / blocked**: broad related selection (9 fast + 57 slow), missing Godot imported resources and later hang; terminated. Details retained in `evidence/related_tests.log` and `selected_tests.txt`. |
| `python -m py_compile` on new task Python scripts | Passed during preparation and the delivery syntax rerun. |
| Full `verify_boot_scootin.py`, `verify_boot_scootin_sources.py`, Godot import verifier | No complete passing run claimed. The first expects missing Man families; source compatibility and runtime resource state block broader certification. |

### Verification after rebase and export archival

- `python tests/run_tests.py --suite fast`: **10/10 passed in 7.71 s** on the integrated tree; main added a fast check. See `evidence/integrated_fast.log`.
- The same four focused `--changed` paths: **14/14 passed in 15.02 s** including the integrated fast suite. See `evidence/integrated_focused.log`.
- `verify_preserved.py`: **67/67 passed**, including unchanged hashes after relocation and exclusion from the active registry.
- `python scripts/lfs_policy.py check` from the repository root: passed after rebase (32,596 indexed files); the final staged preservation layout is checked again before commit.
- `evidence/dependency_baseline.json` compares original and integrated content hashes: shared scene, Man/Woman anatomical sources, and the dildo prop match; the combined `man_and_woman3.blend` changed concurrently and was preserved. The earlier numerical source results retain their original baseline and coverage.
- Current `AGENTS.md` supplies bundled Game Rig Tools setup and bounded Godot test guidance for a future authorized resume. No animation was reauthored during integration.

## Storage and delivery

The 67 source `.blend` files and 67 `.glb` files were inspected as actual binaries,
before staging. The largest is Woman `routine_four_walls.blend`, **65,596,630 bytes**,
below 104,857,600 bytes. Every new binary, including preserved preview images and archived GLBs,
uses regular Git via **exact-filename** attribute exceptions. Actual sizes and
SHA-256 hashes are recorded in the manifest. Before/after `git check-attr` evidence
is preserved. This task introduces no new Git LFS objects; regular pushes upload
these assets as Git blobs. Existing LFS inputs were hydrated using the configured
Codex account credential, whose value is never stored in this record.

The preservation commit contains sources, baked actions, exports/import settings,
original registration draft, scripts, evidence, manifest, and this status. A separate
animation-guidance and preservation-layout commit follows fetch/rebase as originally
requested. The rebase completed onto `26ac8e049` and preserved both sides of
registry/attribute conflicts. New main guidance requires partial runtime assets to
remain under `.gdignore`; this task’s 67 GLBs/import files were relocated byte-for-byte
and their active registrations removed. Shared dependency changes make earlier
evaluated results historical until fresh validation covers the integrated baseline. Integration fetches current `origin/main`, preserves concurrent changes,
and uses ordinary history-preserving pushes with retries if main advances.
Final task/integration hashes and remote verification are reported by Codex in the
chat; this record's starting commit is intentionally the pre-delivery snapshot.

## Exact resume commands

Read-only checks are safe under the present stop instruction:

```sh
cd /workspace/sanjo-solutions/apps/a-game
blender --version
python tests/run_tests.py --suite fast
python docs/animation_work_status/boot_scootin_boogie/verify_preserved.py
blender -b --factory-startup --python-exit-code 1 --python docs/animation_work_status/boot_scootin_boogie/audit_saved_sources.py
blender -b --factory-startup --python-exit-code 1 animations/man_and_woman/boot_scootin_man_grapevine_r.blend --python docs/animation_work_status/boot_scootin_boogie/reopen_grapevine.py
```

After renewed authorization, first review the saved source mismatch and latest
code; use a task branch. The following commands **author/bake/export assets** and
must remain paused under the current instruction. A single-clip first pass makes
source/bake agreement reviewable before the rest of the batch:

```sh
cd /workspace/sanjo-solutions/apps/a-game
git switch -c codex/boot-scootin-resume
blender -b --factory-startup --python-exit-code 1 animations/man_and_woman/shared_scene_data.blend --python scripts/author_boot_scootin.py -- --character Man --clip heel_dig_r
# Follow current scripts/blender/README.md and install_animation_tools.py first.
# After inspecting that reopened source, regenerate each actor sequentially:
blender -b --factory-startup --python-exit-code 1 animations/man_and_woman/shared_scene_data.blend --python scripts/author_boot_scootin.py -- --character Man
blender -b --factory-startup --python-exit-code 1 animations/man_and_woman/shared_scene_data.blend --python scripts/author_boot_scootin.py -- --character Woman
python scripts/verify_boot_scootin.py
blender -b --factory-startup --python-exit-code 1 --python scripts/verify_boot_scootin_sources.py
# Finish Godot import initialization, then runtime checks:
godot --headless --editor --path . --import
godot --headless --path . --script res://scripts/verify_boot_scootin_import.gd
python tests/run_tests.py --changed models/player/animation_updates.tres
```

Inspect actual sizes and update exact-file attributes for newly created assets
before staging. Refresh the preservation manifest only as a new authorized task
record, keeping this snapshot's hashes as historical evidence. Review clips and
transition playback before declaring completion. The unapplied migration proposal
is not a certified substitute for regeneration and validation.
