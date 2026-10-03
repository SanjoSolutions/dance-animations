# Rock 'n' roll partner animation checkpoint

Recorded 2026-10-02 (UTC). Chat title: “Rock 'n' roll partner animations for man_and_woman3.blend” (descriptive task title; UI title unavailable). Task branch: `task/rock-n-roll`. Current commit at the stop checkpoint: `3c52737c74b488501e9cfe47e7029547c6f5fe88`. Repository: SanjoSolutions/sanjo-solutions, app: `apps/a-game`.

The user instructed all active animation chats to stop authoring and preserve their present state. This checkpoint delivers **partial procedural blocking studies**, supporting tools, and evidence. It does not represent acceptance of the complete dance repertoire. Authored: 75 canonical paired clips plus 16 alternate candidate files. Baked: **0**. Exported GLB/runtime clips: **0**.

## Original scope and stopping point

The request covered coordinated Rock 'n' roll moves and positions for both characters, natural motion, planted contacts, body clearance, smooth transitions, interpolated validation, loop continuity, reuse of compatible animation work, Blender 5.2 throughout, individual animation files, repository guidance, storage checks, commits, documentation, integration, and push.

The implemented plan contains 46 named studies in both lead roles (92 sources): eight positions, eleven footwork phrases, thirteen figures, and fourteen directed transitions per leader. Grounded social choreography is the implemented scope; competition aerials and regional variations remain outside this partial plan. Reused components include disco proportion fitting and wrist posing, yoga controls, paired IK/contact solving, and the existing action/file writer. Existing choreography clips were not copied wholesale.

At the stop, the man-role batch had completed with three failures; the woman-role and recovery batches remained active. Their existing complete output files were preserved. Source scripts include changes newer than many canonical clips: neutral overhead wrist fitting, released place exchanges, shallower dips, gated heel/toe pitching, wider shadow placement, and outward shadow transition paths. These changes have only partial regeneration and validation coverage.

## Saved files and authored state

Every source and candidate is listed individually in [rock_n_roll_asset_inventory.json](rock_n_roll_asset_inventory.json), with original path, byte size, SHA-256, actual saved action frame range, key times, markers, slots, participant metadata, lead role, and authored/baked/exported state. Frame ranges and metadata were read from saved actions using Blender 5.2.2, without evaluating motion or saving animation changes after the stop. Movement labels derive from the current generator and can differ from older saved choreography.

| Canonical family | Man leads | Woman leads | Stored frames / playback |
| --- | ---: | ---: | --- |
| Position loops | 8 | 8 | 0–48 / 0–47 |
| Footwork loops | 11 | 11 | 0–72 / 0–71 or 0–96 / 0–95 |
| Figures | 10 | 9 | 0–72, once |
| Directed transitions | 14 | 4 | 0–96, once |

All clips target both `Man.rigify` and `Woman.rigify`; the suffix specifies the leader. Timing is 24 fps, 120 BPM. Canonical sources live at `animations/man_and_woman/rock_n_roll_*.blend`. The saved-file catalog at `animations/man_and_woman/rock_n_roll_catalog.json` now inventories these 75 actual sources and explicitly lists all 17 absent planned names. It replaces an obsolete single-trial catalog. `rock_n_roll_validation.json` is now a truthful checkpoint summary; the earlier report is retained in the archive.

The following task files are durable:

* `scripts/create_rock_n_roll.py`: partial authoring implementation, CLI, repertoire, synchronized sparse IK actions, contact refinement, loop closure, and split-file writing.
* `scripts/validate_rock_n_roll.py`: saved-file measurement and optional review rendering implementation; full acceptance remains pending.
* `scripts/rock_n_roll.md`: workflow and planned coverage guide, marked partial.
* `animations/man_and_woman/.gitattributes`: exact ordinary-Git exceptions for the 75 saved Rock 'n' roll sources.
* This status file, the adjacent inventory, and `rock_n_roll_partner_animations_checkpoint.zip`.

The checkpoint ZIP preserves 199 regular cache files, their manifest, 16 alternate `.blend` files, source-script snapshots, authoring/test/validation logs, historical catalogs/reports, and saved review frames/contact sheets. Original paths are retained beneath `.cache/rock_n_roll/`. Symlinks were excluded; their canonical targets remain in the repository. ZIP size: 25,950,197 bytes; SHA-256: `2312df1a8ba1efe7b8ad8506073f3a021219e2dcec2f351589b1e746c8fcb219`.

Alternate candidate groups inside the archive:

* `adjustments/`: eight files (shadow position, open-to-shadow, shadow-to-open, heel-toe, each lead role). The transition files include a later path revision than their historical validation report.
* `recovery/`: six files: both man-led underarm directions, both man-led place exchanges, man-led low dip, and woman-led right underarm. Place exchanges store 0–144 and play once. The batch was terminated before completing all role variants or writing its catalog/validation.
* `neutral_trial/`: woman-led right underarm, individually validated against its archived hash.
* `turn_trial/`: earlier man-led right underarm, individually validated against its archived hash.

Candidate files reference a sibling `shared_scene_data.blend`; reconstruct those sibling links when reopening archived candidates. They have not been promoted into canonical sources. Original combined/shared/character geometry source files retain their saved content.

## Validation evidence and limitations

* Required fast suite: `GODOT=/tmp/a_game_godot/Godot_v4.7.2-stable_linux.x86_64 BLENDER=/tmp/blender-5.2.2-linux-x64/blender python tests/run_tests.py --suite fast` — **10/10 passed**, 6.10 seconds after stopping authoring (`stop_fast.log` in ZIP).
* `python -m py_compile scripts/create_rock_n_roll.py scripts/validate_rock_n_roll.py` — passed.
* Read-only Blender 5.2.2 audit: `blender -t 1 --background --factory-startup --disable-autoexec --python-exit-code 1 --python .cache/rock_n_roll/inspect_checkpoint.py` — passed for 75 canonical and 16 candidate actions, each with two slots and `BOTH` participants (`checkpoint_inspection.log`). This establishes saved-action structure, not motion quality.
* Earlier individual source composition through `scripts/player_assets/animation_file_startup.py` passed: `SOURCE_COMPOSITION_OK 5.2.2 LTS rock_n_roll_position_open_man_lead 2 24` (`source_open.log`). Full combined-library discovery currently encounters an IDProperty name length error in the broader suite; this is an open integration blocker.
* `neutral_trial/rock_n_roll_validation.json`: selected woman-led right-underarm candidate passed 67 sampled frames, maximum IK/plant error 0.000233 m, palm gap 0.018676 m, capsule clearance 0.147332 m, minimum floor height −0.001343 m. `turn_trial/rock_n_roll_validation.json`: earlier selected man-led right-underarm candidate passed 67 samples, palm gap 0.018623 m. Each result applies only to its recorded source hash.
* `adjustments/rock_n_roll_validation.json`: seven of eight candidates passed at that revision; woman-led shadow-to-open failed capsule clearance (0.006633 m versus 0.015 m required). Subsequent transition changes were saved; their validation remains pending.
* Earlier partial validation exposed support-foot errors, loop velocity error in boogie walks, kick clearance, and overhead wrist/reach problems. Later code addresses these, with mixed saved-file revision coverage. Historical reports can have hashes different from the preserved current candidates. Full-motion acceptance has not passed.
* Scoped suite command: `GODOT=/tmp/a_game_godot/Godot_v4.7.2-stable_linux.x86_64 BLENDER=/tmp/blender-5.2.2-linux-x64/blender PATH=/tmp/blender-5.2.2-linux-x64:$PATH python tests/run_tests.py --slow-timeout 60 --changed animations/man_and_woman/rock_n_roll_catalog.json --changed animations/man_and_woman/rock_n_roll_position_open_man_lead.blend --changed scripts/create_rock_n_roll.py --changed scripts/validate_rock_n_roll.py`. It selected ten fast and 57 slow checks and was interrupted during `scripts/test_disco_dance.py`. `suite_final.log` records preceding failures: Godot scene/assertion errors, 60-second timeouts, missing Game Rig Tools bake operator (`StopIteration`), and Blender discovery `KeyError: the length of IDProperty names is limited to 63 characters`. The suite has no complete passing result; causes require investigation before final delivery.

Implemented motion thresholds are IK reach 5 mm, planted ankles 6 mm, calibrated palm spacing 35 mm, torso/leg capsule clearance 15 mm, floor penetration tolerance 10 mm, loop pose 0.1 mm, endpoint velocity difference 8 mm/frame, and transition endpoint difference 6 mm. Samples cover saved keys, midpoints, phase boundaries, and loop-adjacent subframes. Capsule checks cover torso and legs; arms, fingers, balance, and full surface clearance require visual review. Only selected review images were inspected. These are geometric checks, not force-balance simulation. Contact refinement has an iteration cap and can exit with residual error, so a saved file alone is not a validation result.

## Processes, storage, and delivery

Owned woman authoring PID 5808, recovery authoring PID 8509, suite runner PID 7226, and its active Blender child PID 9112 received termination signals. Subsequent process inspection found no owned running Blender/Godot/test jobs. The man batch and shadow adjustment batch had already exited. No further animation generation, refinement, baking, export, or rendering occurred after the stop. Read-only action inspection and fast checks followed. Editor-generated UID bookkeeping in three unrelated `.tres` files was restored rather than included.

All inspected animation binaries are 123,432–244,027 bytes (the upper value is an archived candidate). Each ordinary-Git source and the checkpoint archive is below 104,857,600 bytes. Exact source exceptions unset `filter/diff/merge/text`; ZIP has no LFS filter. Shared and character source LFS attributes remain unchanged. All task uploads therefore travel as ordinary Git blobs; this task introduces no LFS objects.

The status records the pre-commit stopping point; final task/documentation/integration hashes are supplied in the delivery response and Git history. Concurrent remote work is preserved by fetching and integrating current `origin/main` with ordinary pushes.

## Remaining work and exact resume commands

The current user instruction is to preserve and deliver this checkpoint. Run authoring/rendering commands only after a later instruction resumes animation work. First review saved hashes, choose candidate revisions, diagnose combined-library discovery, install the required Game Rig Tools version for baking, and reconcile all missing roles. Then regenerate a consistent catalog, validate all saved clips and transitions, inspect complete playback for each role, and bake/export if requested. Rendering and successful metadata checks alone do not close the known motion failures.

Commands below run from `apps/a-game`. Temporary executable paths identify the verified session tools; on a new machine provision the same Blender 5.2 version and verify it before use.

```sh
cd /workspace/sanjo-solutions/apps/a-game
/tmp/blender-5.2.2-linux-x64/blender --version
python -m zipfile -e docs/animation_work_status/rock_n_roll_partner_animations_checkpoint.zip .
# Reconstruct excluded shared-scene links for each candidate directory.
python - <<'PY'
from pathlib import Path
shared = Path('animations/man_and_woman/shared_scene_data.blend').resolve()
for name in ('adjustments', 'recovery', 'neutral_trial', 'turn_trial'):
    target = Path('.cache/rock_n_roll') / name / 'shared_scene_data.blend'
    if not target.exists():
        target.symlink_to(shared)
PY
# Read-only metadata inventory; writes JSON records, never animation files.
/tmp/blender-5.2.2-linux-x64/blender -t 1 --background --factory-startup \
  --disable-autoexec --python-exit-code 1 --python .cache/rock_n_roll/inspect_checkpoint.py
# After renewed authorization and fixes: regenerate a consistent full source set.
/tmp/blender-5.2.2-linux-x64/blender -t 2 --background animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/create_rock_n_roll.py
/tmp/blender-5.2.2-linux-x64/blender -t 2 --background animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/validate_rock_n_roll.py
/tmp/blender-5.2.2-linux-x64/blender -t 2 --background animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/validate_rock_n_roll.py \
  -- --render .cache/rock_n_roll/resumed_review --render-only --playback
GODOT=/tmp/a_game_godot/Godot_v4.7.2-stable_linux.x86_64 \
BLENDER=/tmp/blender-5.2.2-linux-x64/blender python tests/run_tests.py --suite fast
```

The archived candidate inventory is preservation evidence; generator and validator defaults operate on canonical sources. Recheck exact-file Git attributes and actual binary sizes for every resumed output before staging. Re-run the scoped suite above through the runner after resolving its blockers, and use the established Player Asset Export workflow for runtime baking/export.

## Integration verification (2026-10-02)

The checkpoint commit was rebased onto concurrent `origin/main` at `de89cfea0`; its rebased hash is `343bb8cfc58b3123165aac59c277a7308d0a2b54`. The `.gitattributes` conflict retained both tasks' complete filename entries. Concurrent main changed repository storage policy and converted shared sources to ordinary Git; the pre-integration storage observations above describe the stopping baseline. This task preserves the incoming policy and shared assets. `git check-attr filter` now reports `unspecified` for `shared_scene_data.blend`.

The new main includes `scripts/blender/install_animation_tools.py` and bundled Game Rig Tools; use the current `scripts/blender/README.md` when resuming instead of treating the earlier missing-tool diagnosis as a current repository limitation. Installing or exercising bake tools remains future work under the stop instruction. All archived motion results remain tied to their historical source/helper revisions.

After integration, `python scripts/lfs_policy.py check` passed for 24,511 staged files. The required fast command recorded above passed again: **10/10 checks in 6.43 seconds**, with the full output in `rock_n_roll_integration_fast.log`. The animation sources and checkpoint archive retained their recorded SHA-256 hashes. `AGENTS.md` gained guidance to reconstruct interrupted batch inventories from actual saved actions and preserve historical catalogs separately.
