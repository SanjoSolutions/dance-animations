# Solo Macarena animation work status

- Recorded: October 2, 2026 (Europe/Berlin).
- Chat/task: Create solo Macarena animations for `man_and_woman3.blend` (descriptive title; product title was unavailable).
- Stop instruction: user-directed animation stop received through coordination chat `01a0fd1a-3673-7683-ae29-577f2ee1a927`. Work switched immediately to preservation, verification, and delivery.
- Working branch: `codex/macarena-solo-preservation`; initial branch: `work`.
- Commit at stop: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Author: Codex. GitHub commit identity: `Codex <codex.sanjo.solutions@gmail.com>`.

## Scope and stopping point

The original request covered a broad, organized solo Macarena repertoire for both characters, existing per-animation Blender sources, natural movement, planted contacts, clearance, smooth transitions, sampled interpolation, loop checks, exports, documentation, and publication to main. Blender 5.2 was required throughout.

**This is a partial procedural blocking study.** One woman-only in-place routine reached authored, native-baked, and exported states. Its clearance review failed. The man repertoire and the other 31 woman clips exist only as generator specifications. Production-quality approval remains pending. The stop instruction takes precedence over further animation generation or correction.

The generator describes 32 clips per character: 13 positions (ready plus twelve count positions), 12 individual gesture transitions, hip sway, left and right quarter turns, in-place routine, four-wall routine, entry, and exit. The choreography is right-leading: palms down, palms up, opposite shoulders, behind head, opposite waist, own hips, sway, and the turn finish. The in-place variant keeps its heading; the four-wall specification includes quarter-turn jumps.

## Preserved files and asset states

All paths below are relative to `apps/a-game`.

| File | State and purpose |
| --- | --- |
| `scripts/create_macarena.py` | Partial procedural authoring tool. Composes the existing `RigYogaPoser` also used by disco, calibrated palm frames, native Rigify IK, sparse gesture and clearance keys, native Blender visual baking, `AnimationFileWriter`, `AnimationClipScene`, and `AnimationUpdates`. Further tuning is required. |
| `scripts/review_macarena.py` | Half-frame reach, wrist, foot-plant, forearm-separation, loop-pose and loop-velocity checks. The current source fails the forearm check. `compare_bake` exists but its validation remains pending. |
| `animations/man_and_woman/macarena_woman_routine_in_place.blend` | Canonical partial authoring source; 1,132,468 bytes. Contains `macarena_woman_routine_in_place` and its `.baked` family. Reconstructs the editable scene from `shared_scene_data.blend` through Player Asset Export. |
| `animations/man_and_woman/macarena_catalog_woman.json` | Actual generated inventory: one clip, Blender 5.2.2 LTS, 24 fps, 120 BPM, loop flag and source/export paths. |
| `models/player/animation_updates/macarena_woman_routine_in_place_baked_d5d89fe627ef.glb` | Partial native bake exported by Blender 5.2.2; 388,288 bytes; one animation, 630 channels, eight seconds. Godot playback and source/bake equivalence remain pending. |
| `models/player/animation_updates/macarena_woman_routine_in_place_baked_d5d89fe627ef.glb.import` | Animation-library import settings, named skins, repository import script, loop mode. |
| `models/player/animation_updates.tres` | Existing update libraries plus the partial Macarena export. Its presence records export publication, rather than a quality approval. |
| `.gitattributes` | Exact-path regular-Git exceptions for this task's binary assets, all at or below 104,857,600 bytes. |
| `docs/animation_work_status/macarena_solo_artifacts/storage_inventory.json` | Actual byte sizes and SHA-256 digests for each preserved binary. |
| `docs/animation_work_status/macarena_solo_artifacts/preview.blend` | Raw author-only checkpoint, 13,216,738 bytes, copied from `.cache/macarena/preview.blend`. Experimental snapshot; reopening and relative library resolution were not verified. Prefer the canonical per-animation source above. |
| `docs/animation_work_status/macarena_solo_artifacts/preview.py` | Earlier render/probe script, preserved as diagnostic procedure. References the original `.cache/macarena` output directory. |
| `docs/animation_work_status/macarena_solo_artifacts/pose_000.png` through `pose_144.png`, every 12 frames | Thirteen Blender 5.2.2 Workbench renders from an earlier iteration. These show the gesture positions before the final clearance-path changes; they are diagnostic evidence, not final renders. |
| `docs/animation_work_status/macarena_solo_artifacts/*.log` | Original fast-test attempts, final fast check, trial export, wrist probe, saved-source review, related-test selection and related verification. |
| `docs/animation_work_status/macarena_solo_artifacts/.gdignore` | Keeps diagnostic Blender assets and images outside Godot's import scan. |

The combined `man_and_woman3.blend`, shared scene, anatomy sources, existing disco source, and full animation GLB received asset hydration only. Their tracked contents remain unchanged. The combined library discovers new per-animation sources through the existing add-on workflow.

### Authored/baked/exported timing and roles

- Authored action: `macarena_woman_routine_in_place`, participant `PARTNER` (Woman), one character's control-rig slot plus its object channels.
- Baked action: `macarena_woman_routine_in_place.baked`, Woman deform rig, native visual samples for frames 0–192 inclusive.
- Export: eight seconds at 24 fps, loop endpoint at 192. Twelve gestures occupy counts 1–12 (frames 12–144); the final four counts cover the in-place groove and return. Frame 0 is the ready/own-hips pose.
- Planned position clips: 0–24; gesture clips: 0–12; hip sway: 0–48; quarter turns: 0–12; entry/exit: 0–24; in-place routine: 0–192; four-wall routine: 0–768.
- The remaining specifications have **zero authored source files, baked actions, or exports**.

## Verification and blockers

Blender reports `5.2.2 LTS`, build `d13f752e3b9c`. All Blender authoring, native baking, rendering, export, and review used that binary.

`python -m py_compile scripts/create_macarena.py scripts/review_macarena.py` passed.

`python tests/run_tests.py --suite fast --godot /workspace/.cloud-onboarding/bin/godot` passed **9/9 in 3.01 seconds** after loading the required hair `.res` assets. The initial default-engine attempt passed 8/9 and reported LFS pointer files for hair resources; the working environment's explicit Godot is 4.7.2. See `fast.log`, `fast2.log`, and `fast_final.log`.

Saved-source validation completed before preservation:

```bash
blender -b animations/man_and_woman/macarena_woman_routine_in_place.blend \
  --python-exit-code 1 --python scripts/review_macarena.py
```

Result: **failed clearance**, exit 1. The 385 samples cover every half frame from 0 through 192:

| Measurement | Result |
| --- | ---: |
| Maximum IK reach error | 0.000209849 m |
| Maximum planted-foot drift | 0.000062471 m |
| Maximum wrist bend | 67.309711 degrees |
| Maximum half-frame hand displacement | 0.068056377 m |
| Minimum sampled forearm centerline separation | **0.005225692 m**, below the 0.065 m review threshold |
| Loop endpoint position error | 0 m |
| Loop endpoint rotation error | 0 radians |
| Loop boundary velocity difference | 0.173999133 m/s |

The forearm measurement is a sampled segment proxy. Full skin, fingers, shoulders, waist, and breast clearance still require evaluated-surface review and updated renders. Endpoint equality alone establishes only part of loop quality. Existing renders caught wrist/arm issues in earlier iterations, and the latest half-frame check demonstrates a remaining arm-crossing problem.

The GLB header, declared length, animation count, name, channel count, and duration passed a read-only structural check. Playback, imported track binding, baked-versus-authored equivalence, source re-save behavior, all other clips, the man rig, and quarter-turn/four-wall foot contacts remain pending.

Game Rig Tools was absent from the active Blender profile during authoring. Player Asset Export was installed through its repository loader. The trial used Blender's `bpy_extras.anim_utils.bake_action_objects` and the repository's compact clip-scene/export publication primitives. This route produced the saved trial; its complete equivalence to the normal Action Bakery workflow remains a review item.

Related repository checks are recorded in `macarena_solo_artifacts/related_checks.log`; their final outcome is appended below.

## Processes and local outputs at stop

The process inventory at stop contained zero Blender processes. The authored-source review had finished with exit 1. Existing authoring and rendering processes had completed; additional animation work stopped immediately.

The original `.cache/macarena/` directory contained disposable probe scripts, incremental metrics logs, duplicate export, and a prior `preview.blend1`. The latest checkpoint, all existing position renders, important logs, and render procedure were copied into the tracked artifact directory. The canonical authored and exported assets remain at their normal project paths. Cache-only intermediate probes and duplicate save backups were removed during final delivery cleanup.

Preservation verification runs use transient fixture processes owned by the test runner. Their results belong to the delivery record and introduce zero new Macarena motion.

## Remaining work

1. Resume only under a new instruction authorizing animation work.
2. Resolve the forearm crossing through gesture-specific elbow paths, contact heights, and travel clearance; preserve stationary-arm contacts while the other hand travels.
3. Recheck evaluated surface clearance and natural wrist/finger poses. Re-render the final choreography after correction.
4. Verify native bake equivalence and Godot imported track binding against the shared model and existing animation pipeline.
5. Validate quarter-turn takeoff/landing and four-wall loop velocity, including interpolated foot positions and heading.
6. Generate and validate the remaining 63 clips, including all man sources, with one authored/baked family per file.
7. Review hold-key reduction, transition compatibility, intended Macarena positions, metadata and all export settings.
8. Inspect actual new binary sizes, scope Git attributes to those files, then perform the requested asset publication workflow.

## Exact resume commands

Run from `/workspace/sanjo-solutions/apps/a-game`. Read `AGENTS.md`, `scripts/player_assets/paired_animation_authoring.md`, `scripts/player_assets/motion_review.md`, and this status first. Keep Blender at 5.2.

Read-only review of the preserved canonical source:

```bash
/workspace/.cloud-onboarding/bin/blender --version
/workspace/.cloud-onboarding/bin/blender -b \
  animations/man_and_woman/macarena_woman_routine_in_place.blend \
  --python-exit-code 1 --python scripts/review_macarena.py
python tests/run_tests.py --suite fast --godot /workspace/.cloud-onboarding/bin/godot
```

The source composes its scene through Player Asset Export. Integration fetched concurrent commit `18e528c73`, which bundles Game Rig Tools and the combined installer. A fresh profile can install both tools with:

```bash
/workspace/.cloud-onboarding/bin/blender -b \
  --python-exit-code 1 --python scripts/blender/install_animation_tools.py
```

**Future authoring, after explicit resume authorization and clearance fixes:** the following command replaces the existing partial trial and updates its export/catalog; preserve its prior Git commit first.

```bash
mkdir -p .cache/macarena
/workspace/.cloud-onboarding/bin/blender -b \
  animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 \
  --python scripts/create_macarena.py -- --character Woman --clip routine_in_place
```

A future complete build uses the same invocation with `--character Woman --clip routine_in_place` removed. It generates both roles and the 64-entry catalog. The current generator is a blocking study and requires the remaining checks above before that build.

Git fetch/push/LFS operations in this environment use its configured `SANJO_GITHUB_LFS_TOKEN` through the inherited proxy. The successful command-scoped authentication pattern is:

```bash
GIT_CONFIG_COUNT=1 \
GIT_CONFIG_KEY_0=http.https://github.com/.extraheader \
GIT_CONFIG_VALUE_0="Authorization: Bearer ${SANJO_GITHUB_LFS_TOKEN:?}" \
git fetch origin
```

Use the same environment prefix for authorized Git pushes and scoped `git lfs pull`; keep credential values in the process environment.

## Final preservation verification outcome

The following related-check command selected 9 fast and 57 slow checks:

```bash
python tests/run_tests.py \
  --godot /workspace/.cloud-onboarding/bin/godot \
  --blender /workspace/.cloud-onboarding/bin/blender --slow-timeout 60 \
  --changed scripts/create_macarena.py --changed scripts/review_macarena.py \
  --changed animations/man_and_woman/macarena_woman_routine_in_place.blend
```

It recorded 12 passes and 4 failures across 16 completed checks; a seventeenth check had started. The runner and its owned child were terminated with SIGTERM after repeated missing-resource errors and 60-second timeouts established the setup blocker. The remaining selected checks have pending results. Failures included `models/player/test_model_animation_player.gd`, `playground/test_activity_animation_methods.gd`, `playground/test_animation_metadata_saving.gd`, and `playground/test_animation_phases.gd`. Required `playground/animations/*.res` files were still LFS pointers, existing individual update imports were missing, and the new Macarena update also lacked a verified Godot import. Treat the game integration as pending. The run's 58 incidental tracked `.import` edits were restored to their pre-verification contents; task assets and existing update-library references were preserved.

All preserved task binary files passed the 104,857,600-byte storage boundary check. `git check-attr filter diff merge text` reports `unset` for their exact paths. These assets use regular Git, with zero newly introduced LFS pointers. The inventory contains source/export hashes and sizes. A final `git diff --check` passed.

The current preservation workflow commits these files, fetches and rebases onto current `origin/main`, adds verified authoring lessons to `AGENTS.md` in a separate documentation commit, and integrates through an ordinary main-branch push. The delivery response records the resulting commit hashes and remote verification; this source record deliberately anchors the original stopping commit above.

## Integration notes

The preservation commit rebased cleanly onto `18e528c73e6d5be8a86b1a21ff6cc2f7cfeca1f2`, preserving concurrent animation libraries, storage policy, tooling, and documentation. The new storage policy check passed for all 23,389 staged files. The bundled Game Rig Tools setup resolves the earlier tool-availability preparation item for a future resumed session; authoring stayed stopped. The new `AGENTS.md` rotation-mode guidance also identifies a review item: the procedural builder changes some controls to Euler mode in memory, whereas individual sources compose their rig modes from the shared scene. Verify those channels after reload before expanding the repertoire. The final task `.glb.import` includes Godot-generated settings from the attempted integration checks; existing files’ incidental import changes were restored.

After the rebase, the current fast suite expanded to ten checks. The same explicit-Godot fast command passed **9/10 in 5.32 seconds**. `playground/activity_import/test_activity_json.gd` was blocked by missing imports for newly present hair models (`bob01`, `bob02`, `short01`–`short04`, `afro01`), which prevented dependent Character scripts from compiling. See `fast_rebased.log`. The earlier 9/9 result belongs to the pre-rebase checkout. Further environment imports and animation work remain paused.
