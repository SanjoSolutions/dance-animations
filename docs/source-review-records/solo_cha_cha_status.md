# Solo cha-cha-cha animation work status

- Recorded: 2026-10-02, Europe/Berlin (stopped around 16:56 CEST).
- Chat title: Solo cha-cha-cha for man_and_woman3.blend (descriptive task title; sidebar title was unavailable).
- Task branch at stop: `codex/solo-cha-cha-cha`.
- HEAD before task commits: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Project: `apps/a-game`, sanjo-solutions cloud environment, `/workspace/sanjo-solutions`.
- State: **Paused by explicit user instruction. Partial procedural blocking studies; production motion quality remains unverified.**

## Original scope and stopping point

The original request covered a broad, organized solo cha-cha-cha repertoire for both characters in `man_and_woman3.blend`, using Blender 5.2 throughout, the existing per-animation file workflow, sparse IK keys, natural motion, planted contacts, clearance, interpolated-motion and loop checks, suitable animation reuse, direct Git storage through 100 MiB, commits/rebase, Animation guidance, merge, push, and asset-upload verification.

The authored catalogue currently describes 45 figures per character (90 intended clips): 35 moving figures, eight positions, and two entry/exit transitions. This is a practical catalogue of common movements and solo adaptations, rather than an exhaustive definition of every cha-cha variation. The user stopped work during regeneration of `in_place_basic_man`, after the updated basic Man/Woman clips had completed saving and export. The owned Blender process received SIGTERM. Its current in-memory in-place revision was discarded; its earlier saved source/export remain preserved. All owned authoring/rendering processes have stopped.

## Durable work

- `scripts/create_solo_cha_cha.py`: unfinished reusable catalogue, footwork trajectories, proportion-aware IK authoring, sparse authoring curves, native Blender visual bake, per-animation file writer, and individual GLB publisher. Uses the existing `DiscoCharacter`, `DiscoWristPoser`, and `RigYogaPoser` helpers. The existing disco action was the loaded scene/reference; its dance timing was replaced with cha-cha footwork. Existing source assets remain unchanged.
- `scripts/review_solo_cha_cha.py`: half-frame authoring-rig checks, support-phase ankle drift, endpoint reach, wrist bends, hand/torso/head proxy clearance, foot separation, loop pose and near-boundary velocity checks. These proxies cover selected landmarks; full mesh/finger collision coverage remains outstanding.
- Twelve `.blend` files contain one authoring action and its matching `.baked` action, with one character slot each. All saved clips span frames **0–96 at 24 fps**, with a four-second/eight-beat cycle at **120 BPM**. Roles are `PLAYER` for Man and `PARTNER` for Woman. Each saved source references the existing `shared_scene_data.blend` through `AnimationFileWriter`.
- Twelve individual GLBs and adjacent `.glb.import` settings have been published. Each GLB contains its matching baked action and the character's skeleton/marker skin. `models/player/animation_updates.tres` adds these twelve libraries while retaining its prior entries. Loop import mode is 1.
- `animations/man_and_woman/solo_cha_cha_review.json` contains the **last regeneration attempt's three authoring reviews only**: basic Man, basic Woman, and the in-memory in-place Man revision that had yet to be saved at cancellation. It is not a complete saved-asset validation certificate.
- `docs/animation_work_status/solo_cha_cha_assets/saved_asset_inventory.json` records exact paths, byte counts, SHA-256 hashes, slots, ranges, roles, and export channel counts for all twelve saved clips.
- Exact-file `.gitattributes` exceptions in the source, export, and preview directories store this task's small binaries directly in Git. Existing global LFS policy remains intact.

### Saved assets

All entries below are **authored + baked + exported, partial and pending export-motion repair**. Source paths use `animations/man_and_woman/`; export paths use `models/player/animation_updates/`. Each export has a tracked adjacent `.glb.import`. The inventory supplies their complete relative paths and hashes.

| Figure | Role | Source file | GLB file | Source bytes | GLB bytes |
| --- | --- | --- | --- | ---: | ---: |
| basic_man | PLAYER | `solo_cha_cha_basic_man.blend` | `solo_cha_cha_basic_man_baked_6c98bf32e354.glb` | 1818807 | 321780 |
| basic_woman | PARTNER | `solo_cha_cha_basic_woman.blend` | `solo_cha_cha_basic_woman_baked_d7a16dc3f3d5.glb` | 1812765 | 316344 |
| compact_basic_man | PLAYER | `solo_cha_cha_compact_basic_man.blend` | `solo_cha_cha_compact_basic_man_baked_750a32dea62b.glb` | 404172 | 310716 |
| compact_basic_woman | PARTNER | `solo_cha_cha_compact_basic_woman.blend` | `solo_cha_cha_compact_basic_woman_baked_1d8b52bf874b.glb` | 398050 | 311004 |
| forward_back_locks_man | PLAYER | `solo_cha_cha_forward_back_locks_man.blend` | `solo_cha_cha_forward_back_locks_man_baked_75cf4f6f6491.glb` | 408934 | 307624 |
| forward_back_locks_woman | PARTNER | `solo_cha_cha_forward_back_locks_woman.blend` | `solo_cha_cha_forward_back_locks_woman_baked_4444120ef47d.glb` | 399393 | 311008 |
| in_place_basic_man | PLAYER | `solo_cha_cha_in_place_basic_man.blend` | `solo_cha_cha_in_place_basic_man_baked_c388f17d2baf.glb` | 400335 | 306096 |
| in_place_basic_woman | PARTNER | `solo_cha_cha_in_place_basic_woman.blend` | `solo_cha_cha_in_place_basic_woman_baked_89010f7ae23a.glb` | 393757 | 301416 |
| side_chasse_man | PLAYER | `solo_cha_cha_side_chasse_man.blend` | `solo_cha_cha_side_chasse_man_baked_ede7daddd82b.glb` | 407734 | 309184 |
| side_chasse_woman | PARTNER | `solo_cha_cha_side_chasse_woman.blend` | `solo_cha_cha_side_chasse_woman_baked_49bf05337d17.glb` | 395345 | 306000 |
| time_steps_man | PLAYER | `solo_cha_cha_time_steps_man.blend` | `solo_cha_cha_time_steps_man_baked_75b430ccbc77.glb` | 410720 | 310712 |
| time_steps_woman | PARTNER | `solo_cha_cha_time_steps_woman.blend` | `solo_cha_cha_time_steps_woman_baked_b8ab3ca39e73.glb` | 400251 | 308328 |

The basic pair was regenerated with native bake cleanup disabled. The other ten files retain the earlier bake with cleanup enabled. The saved generator's latest changes therefore do not describe one uniform generation revision for every preserved file. Future work should repair the bake discrepancy and deliberately regenerate/revalidate the catalogue before treating these exports as final.

### Recorded evidence and previews

`solo_cha_cha_assets/` holds:

- `cha-full.log`: final interrupted authoring run; confirms two basic exports completed and the next in-place authoring review completed.
- `cha-turns.log`: earlier procedural probes of New York, spot turn, spiral turn, crossover position, and entry. These were in-memory studies; corresponding `.blend`/GLB outputs were never saved. An earlier entry study failed its hand/body proxy clearance check.
- `cha-bake.log`, `cha-bake-core.log`, `bake_core_at_stop.log`: bake comparison evidence. `cha-bake-core.log` captures an unsuccessful diagnostic rebake with hidden target evaluation, which produced a 0.27 m discrepancy; that temporary output was subsequently replaced by the completed basic Woman regeneration. `bake_core_at_stop.log` records the current saved basic Woman result.
- `cha-render.log` and eight `previews/solo_cha_cha_basic_woman_{0,12,30,42,60,78,90,96}.png` images: completed Blender Workbench renders of an **earlier basic Woman revision before the hip-placement correction**. They are historical visual evidence, not previews of every current saved clip. Frame 12 was inspected. EGL warnings appeared, and all eight renders completed.
- `check_bake.py`, `check_bake_core.py`, `render_cha.py`: exact diagnostic/review scripts captured from `/tmp`. They contain this checkout's absolute path; change that path when resuming in another checkout. Rendering is a future authoring action and requires renewed authorization after this stop.
- `audit_saved_assets.py`, `saved_asset_audit.log`: read-only Blender structural verification.
- `cha-fast.log`, `fast_at_stop.log`, `selected_checks_at_stop.log`: project-check results.

## Verification at stop

All Blender operations used **Blender 5.2.2 LTS**, build `d13f752e3b9c`. The cloud lacks the Game Rig Tools add-on. Authoring used native Rigify controls, the repository's file writer and compact clip exporter, and Blender's native `bpy_extras.anim_utils.bake_action_objects` fallback. The normal Helpers/Action Bakery cache-based export path has yet to be verified in this environment.

| Command/check | Result |
| --- | --- |
| `python tests/run_tests.py --suite fast` | **9/9 passed**, 4.43 s at stop. An earlier setup run failed because three hair `.res` files were LFS pointers; retrieving those existing assets resolved it. |
| `python tests/run_tests.py --changed scripts/create_solo_cha_cha.py --changed scripts/review_solo_cha_cha.py` | **9/9 passed**, 4.44 s. Selection includes zero slow checks for these new scripts; this is not dance integration certification. |
| `python -m py_compile scripts/create_solo_cha_cha.py scripts/review_solo_cha_cha.py` | Passed. |
| `blender -t 2 -b --factory-startup --python docs/animation_work_status/solo_cha_cha_assets/audit_saved_assets.py` | **12/12 saved source/export pairs passed** structural, slot, participant, frame-range, and GLB checks. |
| Authoring half-frame sampling | The six saved figures passed the authoring checks during their build attempts. The final log covers only the latest three reviews. Final basic Woman: support drift 0.000092 m, foot-target error 0.000197 m, wrist bend 6.76 degrees, proxy hand clearance 0.189 m, exact endpoint pose match, near-boundary velocity difference 0.00409 m/s. |
| Saved basic Woman bake comparison | **Outstanding discrepancy:** up to 0.008127 m position difference (DEF-foot.R at frame 36.5) and 0.004200 rad core-bone orientation difference. Integer-frame position error reaches 0.007557 m. This prevents a claim of planted-contact fidelity in the final export. Earlier all-bone diagnostics also found roughly 0.0093 m / 0.1813 rad differences in toe/finger chains. |
| Godot runtime playback / combined-library discovery | Pending. Individual GLB structure was checked; complete imported playback and composed model behavior remain unverified. |

No repository Blender source, shared rig geometry, base model export, or preexisting animation file was rewritten. Existing LFS assets were fetched solely to materialize scene/test prerequisites.

## Remaining work and blockers

1. Resolve the native visual bake/source discrepancy, including ankle positions and toe/finger chains; recheck baked and exported support intervals, loop poses, and velocities. Check target visibility, rest hierarchy, parent scale/shear, constraints, and native bake conversion. Disabling cleanup alone left the current core discrepancy.
2. Finish and validate the other 39 figures per character. The catalogue describes them; saved animation assets exist only for basic, in-place basic, compact basic, side chasse, time steps, and forward/back locks.
3. Revalidate later generator changes: differentiated progressive/walk paths, distinct spiral/three-step trajectories, opposite Cuban-break lead, revised entry clearance, and near-boundary derivative checks. A progressive study previously failed the coarser half-frame seam velocity check; its revised result remains pending.
4. Render and inspect current saved motion, both characters, crossing steps, turns, hips, head, wrists, fingers, and complete mesh clearance. The historical basic preview alone supplies limited evidence.
5. Verify normal helper-driven baking/export (Game Rig Tools is currently absent), action discovery on reopening `man_and_woman3.blend`, Godot import/loop metadata, solo participant visibility, and smooth transitions between figures.
6. Keep the saved partial state intact until the user explicitly resumes animation work.

## Exact resume and verification commands

Run from `/workspace/sanjo-solutions/apps/a-game`. Resume authoring only after renewed user authorization. Confirm `blender --version` reports 5.2. These scripts regenerate destination assets; make a commit/checkpoint first.

```sh
# Read-only structural review and project checks.
blender -t 2 -b --factory-startup --python docs/animation_work_status/solo_cha_cha_assets/audit_saved_assets.py
python tests/run_tests.py --suite fast
blender -t 2 -b animations/man_and_woman/solo_cha_cha_basic_woman.blend --python docs/animation_work_status/solo_cha_cha_assets/check_bake_core.py

# Future authoring: reproduce one figure for diagnosis after the bake fix.
blender -t 2 -b animations/man_and_woman/solo_disco_dance.blend --python scripts/create_solo_cha_cha.py -- --only basic --character Woman

# Future authoring: rebuild the complete catalogue after validation improvements.
blender -t 2 -b animations/man_and_woman/solo_disco_dance.blend --python scripts/create_solo_cha_cha.py

# Future authoring: resume catalogue traversal at the first unsaved figure.
blender -t 2 -b animations/man_and_woman/solo_disco_dance.blend --python scripts/create_solo_cha_cha.py -- --from-figure progressive_basic
```

The generator writes its review JSON anew on each invocation and appends individual export references through `AnimationUpdates`. Preserve earlier reports when comparing runs. It asserts authoring checks before saving each clip; a failing figure remains an in-memory study. The first two basic files and the other ten saved files currently use different bake-cleanup settings.

## Delivery and storage

The task's 12 sources total 7,650,263 bytes, its 12 GLBs total 3,720,212 bytes, and its eight historical PNGs total 2,151,870 bytes. Every new binary is below 104,857,600 bytes and is committed directly to Git using exact-filename attributes. There are no new LFS objects to upload for this task; the ordinary Git push transports all new binary payloads. Existing repository assets retain their existing storage settings.

The task preservation commit, subsequent Animation-guidance commit, and main integration are reported in the delivery message. This record identifies its pre-commit snapshot above; Git history provides the final immutable commit IDs. Integration must fetch current origin/main, retain concurrent animation-update references and documentation, use an ordinary push, and verify task-commit ancestry in remote main. Git commits and any GitHub communications for this delivery are authored by Codex.

### Integration checkpoint

The preservation commit rebased onto `18e528c73e6d5be8a86b1a21ff6cc2f7cfeca1f2` as `bf43af633f2a3b661dcfa0e974638fc5bba874de`. The source-directory `.gitattributes` add/add conflict was resolved by retaining both the concurrent entries and this task's twelve exact-file entries. The refreshed repository now supplies the bundled Game Rig Tools installer in `scripts/blender/install_animation_tools.py` and inherited-scale bake guidance in `scripts/player_assets/bachata_motion.py`. These are newly available starting points for a future authorized repair; animation work remained stopped. The refreshed AGENTS.md also explains saved finger rotation-mode compatibility, which merits review for this study's reused disco posing helper.

Post-rebase verification: the refreshed fast suite passed **10/10** in 8.25 s (`solo_cha_cha_assets/fast_after_rebase.log`); `python scripts/lfs_policy.py check` passed for the staged repository. These delivery checks preserve the animation-quality blockers above.
