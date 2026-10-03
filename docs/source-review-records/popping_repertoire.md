# Popping repertoire — stopped work record

- Date: October 2, 2026, 17:00 Europe/Berlin (15:00 UTC).
- Chat title: Popping solo animations for man_and_woman3.blend (task label; sidebar title unavailable).
- Branch at stop: `codex/popping-repertoire`.
- Current commit at stop: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Stop instruction: preserve present state, cease animation authoring/refinement/rendering, verify, commit, merge, and push.
- Delivery state: partial procedural animation studies, preserved for later review. Full repertoire completion and final artistic acceptance remain pending.

## Original scope

Create a broad organized Popping repertoire with solo motion for both characters
from `man_and_woman3.blend`, using Blender 5.2 and the repository per-animation
workflow. Reuse fitting existing motion; validate natural posture, contacts,
clearance, interpolation, transitions, and loops. Store assets at or below
104,857,600 bytes directly in Git. Commit assets, rebase onto origin/main, add
animation guidance to AGENTS.md, then merge and push while preserving concurrent work.

## Exact saved state

**67 source files and 67 corresponding GLB exports: 42 man and 25 woman clips.**
Every source has one single-participant authoring action and one `.baked` action.
Each range is **0–48 inclusive**, with a repeated loop endpoint, **24 fps**, and
**2-second** playback. Man actions use `PLAYER`; woman actions use `PARTNER`.
The builder defines 84 planned clips; 17 woman clips remain absent.

- 65 clips reached source save, native visual bake, GLB export, and authoring measurements in the final interrupted build.
- `popping_woman_finger_tutting` comes from the corrected trial. Its authoring, bake, and export are saved; it passed the trial authoring checks.
- `popping_woman_tutting_box` is an **earlier partial draft**. Its saved finger/shoulder rotation channels depend on transient rotation modes, and its Godot import settings lack the named loop entry. Preserve it as a blocking study pending a later authorized rebuild. Its older numerical report describes the in-memory trial, rather than a successful final saved-file equivalence check.
- The 65 final-build clips and corrected finger trial remain procedural studies awaiting comprehensive saved-file numerical and artistic review. The source/bake/GLB preservation audit establishes integrity and structure, rather than final choreography approval.

### Asset inventory

[asset_inventory.json](popping_repertoire/asset_inventory.json) lists **every exact
source path, GLB path, state, participant, frame range, size, SHA-256 digest, and
available authoring measurements**. The corresponding `.glb.import` file sits
beside each listed GLB. [popping_manifest.json](../../scripts/popping_manifest.json)
carries the same stopped-state index for tooling.

Source directory: `animations/man_and_woman/popping_*.blend`.
Preserved export directory: `docs/animation_work_status/popping_repertoire/exports/`.
The inventory retains each original `models/player/animation_updates/` path.
`models/player/animation_updates.tres` retains current main’s reviewed entries.
The preserved Popping exports have **runtime registration disabled**. During
integration, current AGENTS.md required stopped exports in an ignored task
directory; the GLBs and their import settings were relocated byte-for-byte into
`popping_repertoire/exports/`, under the evidence directory’s `.gdignore`. The combined Blender library discovers the
per-animation sources. `man_and_woman3.blend`, `shared_scene_data.blend`, and the
character mesh libraries retain their original bytes.

The 134 animation binaries total **41,338,071 bytes**; their largest
file is **492,366 bytes**. Exact-filename `.gitattributes` entries in the
source and preserved-export directories select direct Git storage. The evidence directory
has its own exact-filename direct-Git entries for the preserved PNG renders.
Existing unrelated LFS attributes remain intact.

### Code and supporting files

- `scripts/create_popping.py`: 42-move vocabulary, proportion-aware IK posing, sparse action writer, Blender-native visual baking, per-animation saving, and existing compact GLB/update publishing. The forearm roll adapts `DiscoChoreography` from the existing solo disco work.
- `scripts/review_popping.py`: 97 half-frame samples per clip, contacts and pivots, reach, wrist/knee angles, hand/elbow clearance proxies, loop position/orientation/velocity, and optional baked foot drift.
- `scripts/test_popping.py`: complete-repertoire saved-file and exported-channel verification. Its completeness assertion currently fails as expected for this stopped partial library.
- `scripts/test_popping_import.gd`: native Godot skeleton, track, duration, and loop-setting verification. The old woman tutting-box draft currently fails its loop-entry check.
- `scripts/popping.md`: repertoire catalog, workflow, caveats, and regeneration commands; its opening explicitly records the partial state.
- `docs/animation_work_status/popping_repertoire/verify_preserved_assets.py`: read-only integrity/structure audit of the stopped inventory.
- `docs/animation_work_status/popping_repertoire/*.log`: original build, trial, contact, bake, import, and stopped verification evidence.
- Four existing Blender 5.2 PNG renders in that evidence directory: man body wave, man heel/toe, woman arm wave, and woman finger tutting. These are saved representative pose reviews, not full motion playback validation.

## Verification and findings

- Blender used for every authoring, baking, exporting, rendering, and Blender verification operation: **5.2.2 LTS**, build `d13f752e3b9c`.
- `GODOT=/workspace/.cloud-onboarding/bin/godot python tests/run_tests.py --suite fast`: **9/9 passed**, 3.08 seconds. The selected Godot is 4.7.2.
- `python tests/run_tests.py --slow-timeout 1800 --changed scripts/create_popping.py --changed scripts/review_popping.py --changed scripts/test_popping.py --changed scripts/test_popping_import.gd`: **9/11 passed**. The complete-set assertion failed (67 saved versus 84 planned). The import test reached the old woman tutting-box missing loop key; its owned Godot process was terminated after the script failure. This run used the default Godot 4.6.3. These are recorded task incompleteness issues, rather than environment failures.
- Repeated the native import check with Godot 4.7.2 and `--quit-after 3`: the same old tutting-box loop-key error occurred. Exit code 0 is **not** a passing result; the script error and cleanup messages are in `stopped_godot.log`.
- `blender --background --factory-startup --python-exit-code 1 --python docs/animation_work_status/popping_repertoire/verify_preserved_assets.py`: **67/67 passed** author/bake families, solo slots/roles, 0–48 ranges, GLB animation identities/channels, sizes, and SHA-256 digests.
- Before the stop, eight saved man studies (full-body hit, leg hits, Fresno, walkout, side glide, heel/toe, lean, low position) passed the enhanced saved-contact review. For example, Fresno/walkout/side-glide baked support drift was about 1.072 mm, and lean about 1.517 mm. Body-wave baked drift was separately measured at about 1.661 mm.
- Saved-file comparison identified and corrected transient finger quaternion/Euler mode mismatch in the builder. Corrected arm-wave finger poses agree closely after reopening. Connected deform-chain conversion retains a pose-dependent toe offset (about 7.35 mm in the ready stance; 9.79 mm in the low stance). The complete validation uses a 12 mm bone-position tolerance and a separate 4 mm planted-foot drift tolerance; its full run remains pending.
- Clearance measurements use local proxies. Complete mesh/finger intersection and full playback review remain pending.
- `git diff --check`: passed before staging.

## Processes, preparation, and stopping point

The final owned Blender generation process was PID **2182**. It received SIGTERM
at 15:00:38 UTC after `popping_woman_robot` had completed its output log entry.
Its next in-memory work was discarded by termination; the saved files listed in
the inventory are the durable state. All owned animation/render processes are
stopped. Read-only verification processes finished or were explicitly terminated
after their recorded script failure.

The authoring scene and all existing animation-source LFS objects were hydrated
locally (364 additional sources, approximately 148 MB) for review. Player Asset
Export's checkout-backed loader was installed in local Blender preferences.
Three hair `.res` LFS pointers were hydrated to restore the fast test setup.
These environment operations did not change tracked source assets. Cached shell
helpers and temporary diagnostic scripts are local working aids; durable logs
and renders are copied into this record's evidence directory.

The full-build manifest was only written at normal process completion. After the
stop, the manifest and inventory were reconstructed from actual saved files and
the completed log entries, with byte counts and hashes. This recording step
changed documentation/metadata only; it performed zero animation generation.

## Remaining work and concrete blockers

1. Obtain a new instruction to resume animation work. The present stop instruction is the active authoring constraint.
2. Rebuild the earlier woman tutting-box draft with preserved shared rotation modes and explicit loop import settings.
3. Generate the 17 absent woman clips listed below.
4. Run the full saved-file numerical test, native import test, combined-library discovery review, and representative surface/playback review. The current prototype tests make the incomplete state explicit.
5. Investigate the recorded connected-chain toe offset if tighter exported endpoint agreement is required. Preserve shared-rig compatibility and concurrent assets.
6. Recheck exact binary sizes/attributes and update the inventory before staging future generation.

Absent clips:

- `popping_woman_backslide`
- `popping_woman_fresno`
- `popping_woman_heel_toe`
- `popping_woman_lean`
- `popping_woman_pose_box`
- `popping_woman_pose_low`
- `popping_woman_pose_ready`
- `popping_woman_pose_robot`
- `popping_woman_pose_scarecrow`
- `popping_woman_pose_staggered`
- `popping_woman_pose_t_arm`
- `popping_woman_pose_wide`
- `popping_woman_puppet`
- `popping_woman_scarecrow`
- `popping_woman_side_glide`
- `popping_woman_tutting_angles`
- `popping_woman_walkout`

## Exact resume commands (after renewed authoring authorization)

Run from `/workspace/sanjo-solutions/apps/a-game` in this environment:

```sh
export BLENDER=/home/agent/.local/bin/blender
export GODOT=/workspace/.cloud-onboarding/bin/godot
blender --version
blender --background --python scripts/player_assets/install_blender_addon.py
# Rebuild the complete repertoire after authorization; this writes source and export assets.
blender --background animations/man_and_woman/idle.blend --python-exit-code 1 \
  --python scripts/create_popping.py
python tests/run_tests.py --suite fast
python tests/run_tests.py --slow-timeout 1800 \
  --changed scripts/create_popping.py --changed scripts/review_popping.py \
  --changed scripts/test_popping.py --changed scripts/test_popping_import.gd
```

For the partial state, the read-only integrity command remains:

```sh
blender --background --factory-startup --python-exit-code 1 \
  --python docs/animation_work_status/popping_repertoire/verify_preserved_assets.py
```

The full generator merges clip entries into the stopped manifest; update its
status/planned fields and the preservation inventory explicitly when completing a
future generation. Add exact storage exceptions for newly generated filenames
only after measuring their sizes. Future reproduction requires the hydrated idle,
shared-scene, and linked character source files.

## Integration

- Subsequent ordinary-push retry integrated `1844d41b28afdae87be26733d1e91e11b7968c08`; fast checks passed (`retry_fast_1844d41b2.log`). Incoming history and other task assets were retained.
- Subsequent ordinary-push retry integrated `74503a8d600bb4aaae663bd22dfdad572e3af539`; fast checks passed (`retry_fast_74503a8d6.log`). Incoming history and other task assets were retained.
- Subsequent ordinary-push retry integrated `617c065350834292cd464354741acb1effc3b98c`; fast checks passed (`retry_fast_617c06535.log`). Incoming history and other task assets were retained.
- An ordinary push encountered a concurrent main update. Fetched `e971ed83b`, retained its complete guidance/storage rules, and reapplied only the two Popping notes and 67 source-storage entries. The retry fast suite passed 10/10 (`retry_fast.log`). `storage_audit.json` records the exact direct-Git binary inventory.
- Final integration base fetched immediately before merge: `764e18133`. Shared AGENTS.md guidance and source-storage rules retain concurrent task additions. Post-merge fast checks passed **10/10** in 6.14 seconds (`merge_fast.log`); all 138 preserved binary blobs matched their indexed bytes after conflict resolution.
- Rebase completed onto `e12670ea9` from origin/main, preserving concurrent source-storage entries. Preservation commit: `0cf27a26e533518e387b6e875101386fa22d6d86`.
- The current main fast suite passed **10/10** in 5.93 seconds with Godot 4.7.2 (`integration_fast.log`).
- Relocated-export integrity verification passed **67/67** again in Blender 5.2.2 (`integration_integrity.log`).
- `python scripts/lfs_policy.py check` passed after conflict resolution; all task binaries remain direct-Git blobs.
- `apps/a-game/AGENTS.md` gains animation guidance for incremental batch receipts and separate editable/baked support-drift checks.

Delivery commits include this status record, task-owned sources/exports, scripts,
import settings, evidence, and scoped storage attributes. The source attributes
were merged by retaining both tasks’ exact-file entries; the active runtime index
and its storage rules retain current main’s contents. Fetch origin/main
immediately before integration, preserve concurrent animation-index entries,
merge with ordinary history-preserving Git operations, and verify the pushed
remote main includes the task commits. Final delivery reports provide the actual
task and merge commit hashes and the verified push result. All commit trailers
identify Codex; GitHub communications for this task are authored by Codex.
