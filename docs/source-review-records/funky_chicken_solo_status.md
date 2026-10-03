# Funky Chicken solo animation preservation status

## Stop record

- Date: October 2, 2026, approximately 16:57 CEST (14:57 UTC).
- Chat title: **Create Funky Chicken animations**.
- Chat ID: `01a0fd06-c928-72df-ad7b-0a44a8816062`.
- Project: A-Game, `/workspace/sanjo-solutions/apps/a-game`, sanjo-solutions cloud environment.
- Branch at stop: `work`; preservation branch: `codex/funky-chicken-snapshot`.
- Commit at stop: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Current instruction: preserve the present state, verify it, commit it, integrate current main, and push. Further animation authoring requires renewed user direction.
- Owned generator PID 3966 received SIGTERM. Its final logged operation was `BAKED 15.36` for Man `scratch_right`; that action existed in process memory only. The previous Man `scratch_left` source and export had completed publication. The preserved disk inventory contains 22 source/export pairs. All owned Blender authoring/rendering processes have stopped; subsequent Blender processes performed read-only verification and exited.

## Original scope and achieved state

The request covered a broad Funky Chicken solo repertoire for both characters in
`man_and_woman3.blend`, Blender 5.2 throughout, the repository's per-animation
source workflow, natural IK motion and contacts, interpolation and loop validation,
reuse of fitting animation work, commits, rebase onto origin/main, animation
workflow guidance, integration into main, asset upload, and remote verification.

The procedural catalog plans 25 clips per character (50 total): 16 movement loops,
four positions, entry/exit, left/right quarter turns, and a 64-beat routine. The
preserved output comprises **8 Man clips and 14 Woman clips**. Each has an editable
source action, a matching `.baked` deform action, and an individual GLB. Every
saved clip spans **frames 0–96 at 24 fps**, with a repeated endpoint, four-second
loop duration, and 120 BPM. Each action has one character slot. Man clips select
`PLAYER`; Woman clips select `PARTNER`.

**Readiness:** eight Man clips and the Woman wing-flap clip pass the saved-source
numerical checks. The remaining thirteen Woman clips are **partial procedural
blocking studies**, retaining earlier bake and finger-rotation behavior. They are
preserved for recovery and further work. The full planned repertoire and broad
visual approval remain outstanding. Their original update-resource proposal is preserved as evidence; final integration
keeps these task clips outside the active gameplay registry pending complete
saved-motion and actual-composed-model validation.

The generator composes the existing disco proportion calibration, IK poser,
forearm-relative wrist helper, and eight-beat side-step vocabulary. New choreography
covers wings, head pecks, torso accents, scratches, footwork, positions, turns, and
routine arrangement. Stationary control channels have one initial key; moving
controls use clamped Bezier keys every three frames. Per-animation sources use
`AnimationFileWriter` and the existing shared scene. Individual exports compose
`AnimationClipScene`, `AnimationParticipants`, and `AnimationUpdates`.

## Exact saved animation inventory

Paths below are relative to `apps/a-game`. Each GLB has an adjacent `.glb.import`
file with solo-loop import settings. Every source contains its matching authoring
and baked action. The JSON reports include source/export SHA-256 hashes.

| Clip | Role | Authored / baked / exported | Saved-source check | Source | GLB |
| --- | --- | --- | --- | --- | --- |
| `funky_chicken_man_alternating_wings` | PLAYER | Saved / saved / saved | Pass; numerical review | `animations/man_and_woman/funky_chicken_man_alternating_wings.blend` | `models/player/animation_updates/funky_chicken_man_alternating_wings_baked_4972fd2e373c.glb` |
| `funky_chicken_man_groove` | PLAYER | Saved / saved / saved | Pass; numerical review | `animations/man_and_woman/funky_chicken_man_groove.blend` | `models/player/animation_updates/funky_chicken_man_groove_baked_9babb46d9ec4.glb` |
| `funky_chicken_man_head_pecks` | PLAYER | Saved / saved / saved | Pass; numerical review | `animations/man_and_woman/funky_chicken_man_head_pecks.blend` | `models/player/animation_updates/funky_chicken_man_head_pecks_baked_696919901a81.glb` |
| `funky_chicken_man_knee_pulses` | PLAYER | Saved / saved / saved | Pass; numerical review | `animations/man_and_woman/funky_chicken_man_knee_pulses.blend` | `models/player/animation_updates/funky_chicken_man_knee_pulses_baked_9e4de0e52a1f.glb` |
| `funky_chicken_man_neck_bob` | PLAYER | Saved / saved / saved | Pass; numerical review | `animations/man_and_woman/funky_chicken_man_neck_bob.blend` | `models/player/animation_updates/funky_chicken_man_neck_bob_baked_5f33ea933dea.glb` |
| `funky_chicken_man_scratch_left` | PLAYER | Saved / saved / saved | Pass; numerical review | `animations/man_and_woman/funky_chicken_man_scratch_left.blend` | `models/player/animation_updates/funky_chicken_man_scratch_left_baked_31d5a0909351.glb` |
| `funky_chicken_man_tail_shake` | PLAYER | Saved / saved / saved | Pass; numerical review | `animations/man_and_woman/funky_chicken_man_tail_shake.blend` | `models/player/animation_updates/funky_chicken_man_tail_shake_baked_4efba7dddfc0.glb` |
| `funky_chicken_man_wing_flaps` | PLAYER | Saved / saved / saved | Pass; numerical review | `animations/man_and_woman/funky_chicken_man_wing_flaps.blend` | `models/player/animation_updates/funky_chicken_man_wing_flaps_baked_4884b1fdf05e.glb` |
| `funky_chicken_woman_alternating_wings` | PARTNER | Saved / saved / saved | Partial blocking study; bake/finger mismatch | `animations/man_and_woman/funky_chicken_woman_alternating_wings.blend` | `models/player/animation_updates/funky_chicken_woman_alternating_wings_baked_1bcc7c0191d8.glb` |
| `funky_chicken_woman_groove` | PARTNER | Saved / saved / saved | Partial blocking study; bake/finger mismatch | `animations/man_and_woman/funky_chicken_woman_groove.blend` | `models/player/animation_updates/funky_chicken_woman_groove_baked_dd4a4daa2eda.glb` |
| `funky_chicken_woman_head_pecks` | PARTNER | Saved / saved / saved | Partial blocking study; bake/finger mismatch | `animations/man_and_woman/funky_chicken_woman_head_pecks.blend` | `models/player/animation_updates/funky_chicken_woman_head_pecks_baked_2d9353ac35d8.glb` |
| `funky_chicken_woman_knee_pulses` | PARTNER | Saved / saved / saved | Partial blocking study; bake/finger mismatch | `animations/man_and_woman/funky_chicken_woman_knee_pulses.blend` | `models/player/animation_updates/funky_chicken_woman_knee_pulses_baked_07c3af8dcd35.glb` |
| `funky_chicken_woman_neck_bob` | PARTNER | Saved / saved / saved | Partial blocking study; bake/finger mismatch | `animations/man_and_woman/funky_chicken_woman_neck_bob.blend` | `models/player/animation_updates/funky_chicken_woman_neck_bob_baked_e7710b81d9f1.glb` |
| `funky_chicken_woman_scratch_left` | PARTNER | Saved / saved / saved | Partial blocking study; bake/finger mismatch | `animations/man_and_woman/funky_chicken_woman_scratch_left.blend` | `models/player/animation_updates/funky_chicken_woman_scratch_left_baked_9de7d313cf1b.glb` |
| `funky_chicken_woman_scratch_right` | PARTNER | Saved / saved / saved | Partial blocking study; bake/finger mismatch | `animations/man_and_woman/funky_chicken_woman_scratch_right.blend` | `models/player/animation_updates/funky_chicken_woman_scratch_right_baked_db7eae7a0f19.glb` |
| `funky_chicken_woman_side_step_left` | PARTNER | Saved / saved / saved | Partial blocking study; bake/finger mismatch | `animations/man_and_woman/funky_chicken_woman_side_step_left.blend` | `models/player/animation_updates/funky_chicken_woman_side_step_left_baked_3b62f075d264.glb` |
| `funky_chicken_woman_side_step_right` | PARTNER | Saved / saved / saved | Partial blocking study; bake/finger mismatch | `animations/man_and_woman/funky_chicken_woman_side_step_right.blend` | `models/player/animation_updates/funky_chicken_woman_side_step_right_baked_17f8d3bb3ef0.glb` |
| `funky_chicken_woman_strut_backward` | PARTNER | Saved / saved / saved | Partial blocking study; bake/finger mismatch | `animations/man_and_woman/funky_chicken_woman_strut_backward.blend` | `models/player/animation_updates/funky_chicken_woman_strut_backward_baked_726b28d61d12.glb` |
| `funky_chicken_woman_strut_forward` | PARTNER | Saved / saved / saved | Partial blocking study; bake/finger mismatch | `animations/man_and_woman/funky_chicken_woman_strut_forward.blend` | `models/player/animation_updates/funky_chicken_woman_strut_forward_baked_757033a781d7.glb` |
| `funky_chicken_woman_tail_shake` | PARTNER | Saved / saved / saved | Partial blocking study; bake/finger mismatch | `animations/man_and_woman/funky_chicken_woman_tail_shake.blend` | `models/player/animation_updates/funky_chicken_woman_tail_shake_baked_8e195ac0eb08.glb` |
| `funky_chicken_woman_wing_flaps` | PARTNER | Saved / saved / saved | Pass; numerical review | `animations/man_and_woman/funky_chicken_woman_wing_flaps.blend` | `models/player/animation_updates/funky_chicken_woman_wing_flaps_baked_4f925e115dfa.glb` |
| `funky_chicken_woman_wing_shimmy` | PARTNER | Saved / saved / saved | Partial blocking study; bake/finger mismatch | `animations/man_and_woman/funky_chicken_woman_wing_shimmy.blend` | `models/player/animation_updates/funky_chicken_woman_wing_shimmy_baked_38f0215595a3.glb` |

## Other durable task files

- `scripts/funky_chicken/choreography.py`: planned 25-clip movement/pose catalog and routine specification. Positions, transitions, turns, routine, and remaining moves are procedural specifications awaiting successful generation and review.
- `scripts/funky_chicken/author.py`: Blender 5.2 authoring, sparse key writing, deform bake, and per-clip publication. The connected-bone bake correction is present in this code and in the eight saved Man clips. The latest finger-quaternion correction is present in those clips and Woman wing flaps. Other Woman files predate these corrections.
- `scripts/funky_chicken/review.py`: half-frame contact, wrist, clearance-proxy, bake, and loop measurements.
- `scripts/funky_chicken/verify.py`: reopens saved sources and verifies independent deform playback and GLB participant ownership. It can target a character and explicit phrases. The default expects the complete planned catalog.
- `scripts/funky_chicken/verify_exports.gd`: native Godot GLB import, skeleton-track resolution, participant, and duration checks. The preservation check uses `--expected-count 22`; the default expects 50.
- `scripts/funky_chicken/README.md`: planned catalog, workflow, rebuild commands, and explicit paused-snapshot notice.
- `models/player/animation_updates.tres`: concurrent active references retained. This task's 22 proposed registrations are archived in `docs/animation_work_status/funky_chicken_snapshot/proposed_animation_updates.tres` (the exact task-branch resource, including six pre-existing entries). Runtime activation remains pending.
- `.gitattributes`: exact-path regular-Git exceptions for this task's 44 animation binaries and six preview PNGs.
- `docs/animation_work_status/funky_chicken_snapshot/asset_inventory.json`: all 50 durable binary paths, actual byte sizes, hashes, and inspected filter/diff/merge attributes.
- `docs/animation_work_status/funky_chicken_snapshot/man_saved_validation.json` and `woman_saved_validation.json`: authoritative post-stop, reopened-source measurements and hashes.
- Adjacent `man_saved_validation.log`, `woman_saved_validation.log`, and `godot_exports.log`: post-stop verification output.
- Adjacent `fast_at_stop.log`: required post-stop fast suite. `fast.log` and `related_tests.log` preserve earlier successful checks.
- Adjacent `build.log` and `woman_build.log`: interrupted final build and earlier Woman build histories. `man_report.json` and `woman_report.json` are historical per-run reports; the saved-validation reports above describe the final preserved binaries.
- Six adjacent `funky_chicken_woman_wing_flaps_{front|side}_{0000|0006|0012}.png` files: Blender 5.2.2 clay render diagnostics generated before the stop. These show the bent-elbow wing shape and apparent body clearance at three poses. They precede the latest bake revision and serve as visual studies.

This task's animation commit preserves the original `man_and_woman3.blend`,
`shared_scene_data.blend`, anatomical source models, and existing disco animation.
Integration retains concurrent main updates to the combined library. Shared-scene
and anatomical-source actual SHA-256 content matched the pre-integration inputs;
main converted those files from LFS pointers to regular Git storage.
Temporary `.cache/funky_chicken/clip.glb` is a staging duplicate; logs and preview
artifacts with recovery value have durable copies above. The temporary credential
helper reads the environment at runtime and remains outside Git.

## Validation results and concrete blockers

1. Blender version: **5.2.2 LTS**, build `d13f752e3b9c`. All Blender authoring,
   scripting, baking, exports, rendering, and validation used this version.
2. `GODOT=/workspace/.cloud-onboarding/bin/godot python tests/run_tests.py --suite fast`:
   **9/9 pass** after the stop. The initial default Godot 4.6.3 run passed 8/9 because
   three hair meshes were LFS pointers. Hydrating those existing fixtures and using
   installed Godot **4.7.2** resolved that setup failure.
3. Focused runner invocation below: **12/12 pass** (nine fast checks plus animation
   file, participant, and motion-review checks).
4. Reopened Man sources: **8/8 pass** across 193 half-frame samples per clip.
   Reopened Woman sources: **1/14 pass**, with wing flaps passing. Thirteen earlier
   Woman sources fail independent bake agreement: maximum position discrepancy is
   about 0.02163 meters and angular discrepancy about 0.66133 radians. Earlier
   finger keys used Euler channels on runtime controls, while reopened shared
   controls use quaternion rotation. Earlier native bakes also exhibit accumulated
   scaled-joint differences. Preserve these as partial studies and regenerate only
   after renewed authoring authorization.
5. Native Godot check: **22/22 exports load**, with character ownership, skeleton
   track paths, and four-second durations verified. This demonstrates import
   structure, separate from the thirteen failed motion-bake checks.
6. Current review uses forearm/torso capsule proxies, per-sample planted-foot drift,
   and half-frame seam finite differences. Full mesh intersection review, complete
   playback review, and all planned clips remain outstanding.
7. Game Rig Tools was absent from this task's installed Blender add-ons at setup.
   Player Asset Export was installed through the repository installer. The task
   implemented a native Blender pose-conversion bake with connected-shaft
   preservation; it did not install or validate Action Bakery. Incoming main commit `18e528c73` supplies the bundled add-on and
   `scripts/blender/install_animation_tools.py`. Resume setup uses that installer.
   The preserved animation binaries retain their pre-stop bakes.
8. The full automatic change selection listed 186 slow checks. Focused animation
   workflow checks and actual saved-asset checks were run; the complete 186-check
   selection remains outstanding.
9. The Woman verification intentionally reports its failed assertions. Blender
   without `--python-exit-code` can return process exit 0 after a Python error;
   the assertion text and JSON `passed` fields determine the result. Resume commands
   below use `--python-exit-code 1`.

## Storage and integration

Actual binary inspection found **50 files totaling 33,554,142 bytes**; the largest
is **1,466,811 bytes**. All belong in regular Git under the user's 104,857,600-byte
threshold. Exact path exceptions set `-filter -diff -merge -text`; unrelated LFS
rules retain their scope. Staged blob sizes and bytes are checked against the
working files before committing. This task adds zero LFS payloads, so its asset
upload is the ordinary Git push. Existing downloaded LFS dependencies remain
unchanged.

The preservation commit is identified by this file's introducing commit. A
separate documentation commit adds the connected-bone and reopened-source lessons
to `AGENTS.md` under `# Animation`. Integration fetches current `origin/main`,
rebases the snapshot as requested, preserves concurrent additions, then merges
and pushes using ordinary history-preserving operations. The final chat report
records exact task/documentation/merge hashes and remote ancestry verification.
GitHub commits and integration messages identify **Codex** as their author.
The first rebase completed cleanly onto `18e528c73`; the rebased snapshot commit is
`3a4fad8bbf759ab6910584f3b36978323e00c66e`. The incoming repository storage-policy
check passed for 23,450 indexed files. Post-rebase verification passed **10/10 fast
checks**, **13/13 focused checks**, and **22/22 native Godot GLB checks**. Logs are
`funky_chicken_snapshot/integrated_fast.log`, `integrated_checks.log`, and
`integrated_godot_exports.log`. The Godot asset check now extends the repository
test tree and was run through `TestRunner.execute` with a 60-second timeout.
Bundled animation-tool setup also completed successfully; it changed local Blender
preferences, with the preserved animation files retaining their recorded hashes.
The final integration refreshes origin/main
again to include work published during documentation and verification.

## Resume commands

These verification commands perform read-only animation inspection. Run from
`/workspace/sanjo-solutions/apps/a-game`:

```sh
mkdir -p .cache/funky_chicken
GODOT=/workspace/.cloud-onboarding/bin/godot python tests/run_tests.py --suite fast
GODOT=/workspace/.cloud-onboarding/bin/godot BLENDER=/workspace/.cloud-onboarding/bin/blender \
  python tests/run_tests.py --changed scripts/funky_chicken/author.py \
  --changed scripts/funky_chicken/choreography.py --changed scripts/funky_chicken/review.py \
  --changed scripts/player_assets/test_animation_participants.py \
  --changed scripts/player_assets/test_animation_files.py \
  --changed scripts/player_assets/test_animation_updates.py \
  --changed scripts/player_assets/test_motion_review.py
blender -b -t 2 -y --python-exit-code 1 --python scripts/funky_chicken/verify.py -- \
  --character Man --clip groove --clip wing_flaps --clip alternating_wings \
  --clip head_pecks --clip neck_bob --clip tail_shake --clip knee_pulses --clip scratch_left \
  --output .cache/funky_chicken/man_recheck.json
blender -b -t 2 -y --python-exit-code 1 --python scripts/funky_chicken/verify.py -- \
  --character Woman --clip groove --clip wing_flaps --clip alternating_wings \
  --clip head_pecks --clip neck_bob --clip tail_shake --clip knee_pulses \
  --clip scratch_left --clip scratch_right --clip strut_forward --clip strut_backward \
  --clip side_step_left --clip side_step_right --clip wing_shimmy \
  --output .cache/funky_chicken/woman_recheck.json
/workspace/.cloud-onboarding/bin/godot --headless --path . --quit-after 2 \
  --script scripts/funky_chicken/verify_exports.gd -- --expected-count 22
```

The following commands resume generation **only after renewed user direction**.
The full generation command replaces this task's existing clip files. Preserve the
snapshot commit before running it. The first command targets the next stopped Man
phrase; the second builds the complete planned catalog using the saved generator.

```sh
blender -b --python-exit-code 1 --python scripts/blender/install_animation_tools.py
blender -b -t 4 -y --python-exit-code 1 animations/man_and_woman/shared_scene_data.blend \
  --python scripts/funky_chicken/author.py -- --character Man --clip scratch_right --review
blender -b -t 4 -y --python-exit-code 1 animations/man_and_woman/shared_scene_data.blend \
  --python scripts/funky_chicken/author.py -- --review
blender -b -t 4 -y --python-exit-code 1 --python scripts/funky_chicken/verify.py
/workspace/.cloud-onboarding/bin/godot --headless --path . --quit-after 2 \
  --script scripts/funky_chicken/verify_exports.gd
```

Remaining work: regenerate the thirteen Woman blocking studies with quaternion
finger channels and corrected bake conversion; generate the remaining 28 clips;
verify all saved sources and exports; review motion, surfaces, ergonomics, support
transfers, turns, and routine transitions; then approve the repertoire for use.
The user-directed stop takes precedence over those future generation commands.

## Final merge verification

The final integration started from incoming main `1e89ec851`. Shared-file conflicts
were resolved by retaining both sets of animation guidance and exact-path storage
rules, and taking the union of animation update paths. All 191 incoming update
references and all 28 task-branch references were preserved (including the six
pre-existing references shared by both branches). Every one of the 50 task binary
blobs still matches its recorded size and SHA-256. The merged fast suite passed
10/10 (`funky_chicken_snapshot/merged_fast.log`), and the repository storage policy
passed for 25,485 indexed files before this additional log was staged.


The first ordinary push was rejected because another chat advanced main. The
subsequent integration incorporated `1eb1adc14` and retained both sides of shared
file changes. That revision adds explicit guidance to retain blocked exports and
proposed registrations as evidence. Consequently, all 22 Funky Chicken entries
are archived in `funky_chicken_snapshot/proposed_animation_updates.tres` and are
excluded from the final active registry. Every incoming main registration remains
active. Source and export bytes remain identical to the preserved inventory.
Even the nine numerical passes require full visual and actual-composed-model
review before gameplay registration; the native GLB test establishes each GLB's
own hierarchy and skeleton paths rather than the complete composed-model contract.
