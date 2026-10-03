# Brazilian zouk partner animation stop-state

- Date: 2026-10-02 (UTC; user delivery instruction received this date).
- Chat/task title: Brazilian zouk partner animations for man_and_woman3.blend.
- Project: A-Game, `/workspace/sanjo-solutions/apps/a-game`, sanjo-solutions cloud environment.
- Branch at stop: `work`; baseline/current pre-delivery commit: `3c52737c74b488501e9cfe47e7029547c6f5fe88`.
- User instruction: stop all animation authoring, refinement, generation, and rendering; preserve and deliver the present state. Resume animation work only after renewed authorization.
- Delivery class: **partial procedural blocking studies**, with known failures. This is not a completed or fully validated Brazilian zouk repertoire.

## Original scope and actual completion

The original request covered coordinated Brazilian zouk moves and positions for both characters, Blender 5.2 authoring, per-animation sources, natural motion, planted contacts, body clearance, smooth transitions, interpolated/loop validation, reuse, documentation, commits, main integration, and upload verification. The implementation planned 45 curated patterns across positions, foundations, turns, traveling patterns, body movements, and directed transitions. An exhaustive standard for all Brazilian zouk variations was never established.

37 individual Blender sources and their paired control actions were saved. Each source uses synchronized `Man.rigify` leader and `Woman.rigify` follower slots, BOTH participant metadata, NLA bindings, and phase markers. Every asset remains an authored blocking study. **Baked deform actions: 0. Godot runtime exports: 0.** The existing 321,820-byte MP4 is a review export of the follower right turn, rather than a runtime animation. Shared geometry, character sources, and `man_and_woman3.blend` retain their prior contents.

All Blender work used verified official Blender 5.2.2 LTS: `/workspace/tools/blender-5.2.2-linux-x64/blender`. `/workspace/tools/blender52` wraps it with a four-thread limit. The system Blender 4.3.2 belongs outside this task's toolchain. Sources reuse RigYogaPoser, DiscoChoreography easing, DiscoWristPoser, PairedAnimationAuthoring, and AnimationFileWriter; existing disco gestures were reviewed as stylistically distinct, and choreography was authored specifically for the paired studies.

## Assets, timing, and measured status

All source filenames below are relative to `animations/man_and_woman/`. All rows have both roles stated above, authoring controls saved, baking pending, and runtime export pending. Timing is 24 fps at a reference 120 BPM, 12 frames per beat. The six-step phrase lands at 24, 36, 48, 72, 84, 96. Stored loop endpoints duplicate frame 0; playback excludes that last frame. Results labeled current report have matching source SHA-256 values. Historical/log-only checks are evidence of that earlier run, rather than current full-library approval.

| Source | Category | Stored frames | Playback | Validation at stop |
| --- | --- | --- | --- | --- |
| `brazilian_zouk_basic_forward_back.blend` | Foundations | 0–96 | loop 0–95 | Current report: sample checks passed |
| `brazilian_zouk_body_wave.blend` | Body movements | 0–96 | loop 0–95 | Current report: sample checks passed |
| `brazilian_zouk_bonus.blend` | Traveling patterns | 0–192 | loop 0–191 | Current report: sample checks passed |
| `brazilian_zouk_cambre_shallow.blend` | Body movements | 0–96 | loop 0–95 | Current report: sample checks passed |
| `brazilian_zouk_chest_isolation.blend` | Body movements | 0–96 | loop 0–95 | Current report: sample checks passed |
| `brazilian_zouk_circular_basic.blend` | Traveling patterns | 0–192 | loop 0–191 | Current report: IK reach, Foot plant FAILED |
| `brazilian_zouk_closed_to_open.blend` | Transitions | 0–96 | play once | Current report: sample checks passed |
| `brazilian_zouk_couple_turn.blend` | Turns | 0–192 | loop 0–191 | Current report: IK reach, Foot plant FAILED |
| `brazilian_zouk_diagonal_basic.blend` | Foundations | 0–96 | loop 0–95 | Current report: sample checks passed |
| `brazilian_zouk_double_hand_to_open.blend` | Transitions | 0–96 | play once | Current report: sample checks passed |
| `brazilian_zouk_elastic.blend` | Foundations | 0–96 | loop 0–95 | Current report: sample checks passed |
| `brazilian_zouk_head_circle.blend` | Body movements | 0–96 | loop 0–95 | Current report: sample checks passed |
| `brazilian_zouk_head_sway.blend` | Body movements | 0–96 | loop 0–95 | Current report: sample checks passed |
| `brazilian_zouk_hip_sway.blend` | Body movements | 0–96 | loop 0–95 | Current report: sample checks passed |
| `brazilian_zouk_in_place_weight_transfer.blend` | Foundations | 0–96 | loop 0–95 | Current report: sample checks passed |
| `brazilian_zouk_lateral.blend` | Foundations | 0–96 | loop 0–95 | Current report: sample checks passed |
| `brazilian_zouk_lateral_tilt.blend` | Body movements | 0–96 | loop 0–95 | Current report: sample checks passed |
| `brazilian_zouk_lateral_travel_return.blend` | Traveling patterns | 0–192 | loop 0–191 | Current report: sample checks passed |
| `brazilian_zouk_leader_turn_right.blend` | Turns | 0–192 | loop 0–191 | Historical/log-only validate_turns.log: Palm contact FAILED; current full check pending |
| `brazilian_zouk_lencol.blend` | Traveling patterns | 0–192 | loop 0–191 | Current report: sample checks passed |
| `brazilian_zouk_lunge_recovery.blend` | Foundations | 0–96 | loop 0–95 | Current report: sample checks passed |
| `brazilian_zouk_open_to_closed.blend` | Transitions | 0–96 | play once | Historical/log-only validate_batch2.log: sample checks passed; current full check pending |
| `brazilian_zouk_open_to_double_hand.blend` | Transitions | 0–96 | play once | Saved; full motion check pending |
| `brazilian_zouk_opening_break.blend` | Foundations | 0–96 | loop 0–95 | Saved; full motion check pending |
| `brazilian_zouk_position_closed.blend` | Positions | 0–96 | loop 0–95 | Historical/log-only validate_batch.log: sample checks passed; current full check pending |
| `brazilian_zouk_position_double_hand.blend` | Positions | 0–96 | loop 0–95 | Historical/log-only validate_batch.log: sample checks passed; current full check pending |
| `brazilian_zouk_position_open.blend` | Positions | 0–96 | loop 0–95 | Historical/log-only validate_batch.log: sample checks passed; current full check pending |
| `brazilian_zouk_position_promenade.blend` | Positions | 0–96 | loop 0–95 | Historical/log-only validate_batch.log: sample checks passed; current full check pending |
| `brazilian_zouk_position_shadow.blend` | Positions | 0–96 | loop 0–95 | Historical/log-only validate_turns.log: Wrist comfort FAILED; current full check pending |
| `brazilian_zouk_position_side_by_side.blend` | Positions | 0–96 | loop 0–95 | Historical/log-only validate_batch.log: sample checks passed; current full check pending |
| `brazilian_zouk_reverse_body_wave.blend` | Body movements | 0–96 | loop 0–95 | Saved; full motion check pending |
| `brazilian_zouk_rotisserie_preparation.blend` | Body movements | 0–96 | loop 0–95 | Saved; full motion check pending |
| `brazilian_zouk_simple_turn_left.blend` | Turns | 0–192 | loop 0–191 | Historical/log-only validate_turns.log: sample checks passed; current full check pending |
| `brazilian_zouk_simple_turn_right.blend` | Turns | 0–192 | loop 0–191 | Historical/log-only validate_turns.log: sample checks passed; current full check pending |
| `brazilian_zouk_soltinho.blend` | Traveling patterns | 0–192 | loop 0–191 | Saved; full motion check pending |
| `brazilian_zouk_spot_turn_exchange.blend` | Turns | 0–192 | loop 0–191 | Saved; full motion check pending |
| `brazilian_zouk_viradinha.blend` | Foundations | 0–96 | loop 0–95 | Saved; full motion check pending |

Eight planned files remain unsaved after authoring failures (prefix `brazilian_zouk_`, extension `.blend`):

| Planned clip | Failing frame | Partner right-palm error |
| --- | ---: | ---: |
| preparation_rebound | 86.4 | 0.00233 |
| io_io | 86.4 | 0.00213 |
| open_to_promenade | 72 | 0.10847 |
| promenade_to_open | 24 | 0.13264 |
| open_to_shadow | 72 | 0.10858 |
| shadow_to_open | 14.4 | 0.10472 |
| open_to_side_by_side | 72 | 0.12782 |
| side_by_side_to_open | 24 | 0.09802 |

## Relevant files and saved outputs

- `scripts/create_brazilian_zouk.py`: reproducible 45-pattern generator, with later refinements that have yet to be applied to all saved sources.
- `scripts/validate_brazilian_zouk.py`: saved-action validation, half-frame interpolation sampling, source/dependency fingerprints, incremental report, transition comparisons, optional still rendering.
- `scripts/render_brazilian_zouk.py`: Blender native H.264 review export helper.
- `scripts/brazilian_zouk.md` and `animations/man_and_woman/README.md`: chooser, timing, authoring, validation, and explicit suspended-work guidance.
- `animations/man_and_woman/brazilian_zouk_catalog.json`: 37 saved sources with ranges, keys, roles, and sole offsets; delivery status records 45 planned / 37 saved.
- `animations/man_and_woman/brazilian_zouk_validation.json`: interrupted report, `passed: false`, 20 persisted clip results (18 sample passes, two failures). Final transition and catalog checks remain pending. `open_to_closed` also produced a passing per-clip measurement in `validate_batch2.log` before shutdown, but its result had yet to be persisted in the JSON.
- `animations/man_and_woman/brazilian_zouk_preview.mp4`: completed 360×360, eight-second follower-right-turn review, every second source frame encoded at 12 fps. It predates the stop instruction.
- `animations/man_and_woman/.gitattributes`: exact-filename ordinary-Git exceptions for the 37 saved sources. Existing source-library storage settings remain intact.
- [Preservation manifest](brazilian_zouk_preservation_manifest.json): exact task asset sizes/hashes, all archived paths/sizes/hashes, historical per-clip log measurements, syntax and count verification.
- [Preserved outputs archive](brazilian_zouk_preserved_outputs.tar.gz): complete task cache snapshot, including diagnostics and their scripts, logs, render receipts, existing still images, contact sheets, test outputs, and original JSON snapshots. Archive member paths correspond to `.cache/brazilian_zouk/`. Historical stills/receipts can depict earlier asset revisions; inspect their fingerprints before reuse. The cache also remains in place locally.

## Stopping point, processes, and blockers

Owned Blender PID 3449 was executing validation with optional renders when the stop instruction arrived. SIGTERM stopped it; its wrapper session completed with code 241 (subprocess signal exit mapped by the shell). Process inspection confirmed the Blender process ended. The last logged per-clip result was `open_to_closed`; the last completed still series was `lunge_recovery`. All existing outputs were preserved. Earlier authoring and preview processes had already exited. There are no continuing task animation jobs.

Concrete blockers:

1. `couple_turn` fails evaluated IK reach (0.04208564) and planted-foot error (0.03879519); `circular_basic` fails reach (0.03988549) and plant (0.03569625). Limits are 0.005 and 0.006. Lowering the pelvis was only considered; that change was neither implemented nor validated.
2. Saved `leader_turn_right` has a 0.03148156 palm gap, above the 0.02 tolerance. Extra swing keys exist in current generator code but the saved asset awaits regeneration and validation.
3. Saved `position_shadow` has a 1.394308-radian wrist angle, above the 0.8 tolerance. Current generator formation and palm-target changes passed selected pose diagnostics, but the source file awaits regeneration and interpolated checks. Older shadow logs show a different revision passing; the later failure takes precedence.
4. Six changing-facing transitions encounter arm/palm constraint limits. Automatic arm pole mode passed four isolated failure-pose diagnostics, while alternate explicit pole positions failed. Continuous pole behavior and exact named-position endpoints remain unresolved. Those diagnostics are procedural studies, not completed animations.
5. Current generator code increases palm solver iterations from 12 to 24 and reduces preparation-rebound yaw from 0.7 to 0.55. Selected rebound/io-io poses passed diagnostic checks; complete files have yet to be generated. Source code and saved clips therefore intentionally represent different refinement stages.
6. Full saved-file validation, all transition boundaries, complete visual playback review, bake/export, and runtime integration remain pending. Numerical torso proxies do not establish full mesh clearance or natural dancing.

## Verification commands and results

Executed from `apps/a-game`:

```sh
BLENDER=/workspace/tools/blender52 python tests/run_tests.py --suite fast
```

Preservation-time result: **10/10 passed in 9.37 seconds**, recorded in archived `preservation_fast_tests.log`. Earlier first attempt passed 9/10 while hair mesh LFS pointers still needed hydration; after fetching those dependencies the earlier fast run also passed 10/10.

```sh
BLENDER=/workspace/tools/blender52 python tests/run_tests.py --suite changed \
  --changed scripts/player_assets/test_paired_animation_authoring.py \
  --changed scripts/player_assets/test_animation_files.py \
  --changed scripts/player_assets/test_motion_review.py \
  --changed scripts/player_assets/test_motion_landmarks.py
```

Earlier relevant authoring-tool verification: **14/14 passed in 18.05 seconds**, including the ten fast checks and four focused slow checks; `authoring_tests.log`. Source composition through `scripts/player_assets/animation_file_startup.py` also passed with both rigs and two action slots (`source_composition.log`).

```sh
BLENDER=/workspace/tools/blender52 python tests/run_tests.py
```

Earlier broad selection included ten fast and 57 slow checks. Runtime `test_model_animation_player.gd` failed on imported resource availability. `test_activity_animation_configuration.gd` passed; `test_activity_animation_methods.gd` stalled and its owned runner/process tree was terminated. The broad suite remains incomplete, not passing (`related_tests.log`, `selected_tests.log`). Environment Godot is 4.6.3 while workflow examples name 4.7.2; imported checkout resources require investigation before attributing this solely to engine version.

The interrupted saved-motion command used Blender 5.2.2 with `-b --threads 2 animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_brazilian_zouk.py -- --render .cache/brazilian_zouk/review_final --only ...`; the selected subset omitted pending shadow/leader-turn refinements. `validate_batch2.log` retains all measurements. Half-frame and key samples check IK, plants, palms, floor, support, wrists, torso proxies, movement, loop endpoint and velocity tolerances. Floor geometry is sampled at keys and 12-frame boundaries. This stopped run supplies partial evidence only.

Preservation-only checks parsed all three Python scripts, matched all 37 catalog entries to saved source files, and verified the 20 persisted measurement source hashes. The manifest records every preserved binary size and SHA-256. Ordinary Git is used for every new task file (all are below 104,857,600 bytes); shared LFS files were fetched and remain unchanged. No new LFS asset upload is required for these sources, review MP4, or archive. Delivery uses ordinary Git blob uploads.

## Exact resume commands and remaining work

These are future commands, **not instructions to resume while the stop request remains active**. First read this record and reconcile the known source/save differences. Restore diagnostic outputs from the archive if the cache has been removed:

```sh
cd /workspace/sanjo-solutions/apps/a-game
mkdir -p .cache/brazilian_zouk
tar -xzf docs/animation_work_status/brazilian_zouk_preserved_outputs.tar.gz -C .cache/brazilian_zouk
/workspace/tools/blender-5.2.2-linux-x64/blender --version
```

Confirm actual shared/linked LFS source objects and Blender 5.2 before continuing. After renewed authorization, the pending-source subset can be generated serially as follows (known transition failures require a designed fix first):

```sh
/workspace/tools/blender-5.2.2-linux-x64/blender -b --threads 2 \
  animations/man_and_woman/shared_scene_data.blend --disable-autoexec \
  --python-exit-code 1 --python scripts/create_brazilian_zouk.py -- \
  --only position_shadow leader_turn_right preparation_rebound io_io
```

Each authoring process reads the catalog once and writes its merged result. Run one generator at a time to preserve concurrent subset records. Finish leg-reach and six transition solutions; regenerate affected clips only after reviewing their intended changes. Then validate all saved clips and the complete catalog:

```sh
/workspace/tools/blender-5.2.2-linux-x64/blender -b --threads 2 \
  animations/man_and_woman/shared_scene_data.blend --disable-autoexec \
  --python-exit-code 1 --python scripts/validate_brazilian_zouk.py
```

Only after animation work is authorized, request stills with `-- --render .cache/brazilian_zouk/review` or recreate the review movie using:

```sh
/workspace/tools/blender-5.2.2-linux-x64/blender -b --threads 2 \
  animations/man_and_woman/shared_scene_data.blend --disable-autoexec \
  --python-exit-code 1 --python scripts/render_brazilian_zouk.py -- \
  --output animations/man_and_woman/brazilian_zouk_preview.mp4
```

Review natural motion, fingers, support, whole-body clearance, and transitions. Use the existing chooser and **Bake & Export Active Animation** only when ready; save each source to retain its baked action, then record actual runtime outputs and receipts. Repeat the required fast and relevant checks, inspect actual binary sizes/attributes before staging, and preserve all concurrent main changes during ordinary push integration.

## Delivery provenance

This record captures the pre-commit stop state. Task and integration commit identifiers are reported in the delivery response; assigning this file its own commit hash would be circular. Each new commit carries exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer. GitHub repository delivery is authored by Codex. The requested follow-up AGENTS Animation guidance is committed separately after the preservation commit and task-branch rebase.

## Integration verification

The preservation commit rebased onto `8648f10ee` as `9a88d70cf`. Concurrent Tango, New York Hustle, Swing, and solo cha-cha README/storage additions were retained when resolving the two additive conflicts. The new root storage policy check, `python scripts/lfs_policy.py check`, passed for 24,187 staged files. Post-rebase dependencies can differ from the captured validation fingerprint; the preserved measurements remain historical evidence for the stopped task state.

Current main's Animation guidance also calls out fractional-key insertion in `key_poses`: inspect actual saved key coordinates against intended fractional poses before resuming this generator. This discovery is recorded for later investigation; animation work remained stopped. The separate guidance commit adds shared-catalog serialization and Blender 5.2 movie configuration notes.

Post-rebase fast suite: **10/10 passed in 8.22 seconds**, using `BLENDER=/workspace/tools/blender52 python tests/run_tests.py --suite fast`. The committed `brazilian_zouk_post_rebase_fast_tests.txt` preserves its output.
