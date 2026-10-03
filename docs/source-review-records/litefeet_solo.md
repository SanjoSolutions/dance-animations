# Litefeet solo animation work status

Recorded October 02, 2026, 17:01 Europe/Berlin (15:01 UTC).
Chat/task title: **Litefeet solo animations for man_and_woman3.blend** (descriptive task title).
Repository: `/workspace/sanjo-solutions`, app: `apps/a-game`.
Task branch: `codex/litefeet-solo`.
HEAD at stop/recording: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
GitHub commit and integration communications for this work are authored by Codex.

## Stop instruction and delivery state

The user instructed all animation chats to stop animation work and preserve the
present state. Authoring and rendering processes were terminated. This record and
the assets preserve **partial procedural blocking studies**, suitable for later
review and refinement. The repertoire and natural-motion/style review remain
partial. Further generation requires a renewed user instruction.

There are **55 saved solo source files: 28 Man / 27 Woman**. Every
listed source contains its editable authoring action and matching `.baked` action;
every listed clip has a completed GLB and Godot import settings. All sources use
Blender **5.2.2 LTS**, 24 fps, the original shared-scene reference, one participant,
and looping playback. The final completed clip was `litefeet_man_shuffle_right`.
The Woman right-shuffle was the next work item; its in-memory work was discarded
when the process stopped. Saved source/export counts match the 55 completed
validation records. There are no committed half-written binary files.

The original request covered a broad, organized Litefeet repertoire for both
characters, existing-animation reuse, natural movement, planted contacts,
clearance, transitions and loop validation; per-animation authoring and export;
Git storage for assets at most 104,857,600 bytes, LFS above that threshold;
an animation commit, fetch/rebase, an Animation-section documentation commit,
and integration/push to main with the requested Codex trailer.

## Exact durable files

All paths below are relative to `apps/a-game` unless stated otherwise.

- `scripts/litefeet/catalog.py`: planned 62-specification/124-solo-clip procedural catalog.
- `scripts/litefeet/author_litefeet.py`: Blender 5.2 authoring, sparse keys, native
  evaluated bake, per-animation writer, GLB publisher, per-clip checkpoint report.
- `scripts/litefeet/review_litefeet.py`: half-frame control/IK, contact, comfort,
  proxy-clearance and loop checks.
- `scripts/litefeet/verify_library.py`: saved-action geometry/bake review and optional
  rendering. Its rendering run was stopped; execute again only when authorized.
- `scripts/litefeet/verify_exports.gd`: read-only Godot GLB/model track verification.
- `scripts/litefeet/README.md`: workflow, planned coverage, reuse and known limits;
  explicitly labeled partial at the stop point.
- `scripts/litefeet/reports/validation.json`: 55 successful authored/baked clip reports,
  with explicit partial-repertoire markers.
- `scripts/litefeet/reports/asset_manifest.json`: **exact path, byte size and SHA-256
  for all 110 animation binaries and four previews**, plus action, role, frames and state.
- `scripts/litefeet/reports/saved_geometry_partial.json`: five saved-geometry checks;
  the whole-library review remains incomplete.
- `scripts/litefeet/reports/authoring_stopped.txt`, `geometry_stopped.txt`,
  `related_suite_interrupted.txt`, `fast_suite.txt`, `godot_exports.txt`: preserved
  execution output and blockers.
- `scripts/litefeet/reports/attributes_before.txt`, `attributes_after.txt`:
  actual Git attribute inspections before staging.
- `scripts/litefeet/reports/previews/litefeet_man_back_tap_left.png`,
  `litefeet_man_back_tap_right.png`, `litefeet_man_bad_one.png`,
  `litefeet_man_bounce.png`: four completed Blender clay renders from the stopped run.
- `models/player/animation_updates.tres`: existing update references plus the
  55 Litefeet exports; concurrent references must be retained during integration.
- Repository-root `.gitattributes`: current main supplies the generated size policy.
  All 114 inspected task binaries use regular Git by default. The initial task’s
  exact-path exceptions were removed by policy synchronization after rebasing.

The combined `man_and_woman3.blend`, shared scene, source anatomy models, existing
animations and original exported models retain their committed content. The
combined library discovers new per-animation sources when reopened with Player
Asset Export enabled. Existing disco IK/scale/wrist posing helpers were reused;
the disco animation itself was preserved.

### Completed clip inventory

Every row has `animations/man_and_woman/<name>.blend`, the `<name>` authoring action,
and `<name>.baked` companion. Exact hashed GLB filenames and checksums are in the
asset manifest. PLAYER means Man; PARTNER means Woman. These are independent solos.
All rows are **authored + baked + exported procedural blocking studies**.

| Name | Role | Inclusive frames |
| --- | --- | --- |
| `litefeet_man_bounce` | PLAYER | 0–24 |
| `litefeet_woman_bounce` | PARTNER | 0–24 |
| `litefeet_man_tone_wop` | PLAYER | 0–48 |
| `litefeet_woman_tone_wop` | PARTNER | 0–48 |
| `litefeet_man_rev_up` | PLAYER | 0–36 |
| `litefeet_woman_rev_up` | PARTNER | 0–36 |
| `litefeet_man_bad_one` | PLAYER | 0–48 |
| `litefeet_woman_bad_one` | PARTNER | 0–48 |
| `litefeet_man_chicken_noodle` | PLAYER | 0–24 |
| `litefeet_woman_chicken_noodle` | PARTNER | 0–24 |
| `litefeet_man_lock_in` | PLAYER | 0–24 |
| `litefeet_woman_lock_in` | PARTNER | 0–24 |
| `litefeet_man_lock_out` | PLAYER | 0–24 |
| `litefeet_woman_lock_out` | PARTNER | 0–24 |
| `litefeet_man_shoulder_rock` | PLAYER | 0–24 |
| `litefeet_woman_shoulder_rock` | PARTNER | 0–24 |
| `litefeet_man_side_tap_left` | PLAYER | 0–24 |
| `litefeet_woman_side_tap_left` | PARTNER | 0–24 |
| `litefeet_man_forward_tap_left` | PLAYER | 0–24 |
| `litefeet_woman_forward_tap_left` | PARTNER | 0–24 |
| `litefeet_man_back_tap_left` | PLAYER | 0–24 |
| `litefeet_woman_back_tap_left` | PARTNER | 0–24 |
| `litefeet_man_heel_dig_left` | PLAYER | 0–24 |
| `litefeet_woman_heel_dig_left` | PARTNER | 0–24 |
| `litefeet_man_toe_point_left` | PLAYER | 0–24 |
| `litefeet_woman_toe_point_left` | PARTNER | 0–24 |
| `litefeet_man_kick_left` | PLAYER | 0–24 |
| `litefeet_woman_kick_left` | PARTNER | 0–24 |
| `litefeet_man_knee_lift_left` | PLAYER | 0–24 |
| `litefeet_woman_knee_lift_left` | PARTNER | 0–24 |
| `litefeet_man_out_step_left` | PLAYER | 0–24 |
| `litefeet_woman_out_step_left` | PARTNER | 0–24 |
| `litefeet_man_shuffle_left` | PLAYER | 0–36 |
| `litefeet_woman_shuffle_left` | PARTNER | 0–36 |
| `litefeet_man_heel_toe_left` | PLAYER | 0–36 |
| `litefeet_woman_heel_toe_left` | PARTNER | 0–36 |
| `litefeet_man_stomp_lock_left` | PLAYER | 0–24 |
| `litefeet_woman_stomp_lock_left` | PARTNER | 0–24 |
| `litefeet_man_side_tap_right` | PLAYER | 0–24 |
| `litefeet_woman_side_tap_right` | PARTNER | 0–24 |
| `litefeet_man_forward_tap_right` | PLAYER | 0–24 |
| `litefeet_woman_forward_tap_right` | PARTNER | 0–24 |
| `litefeet_man_back_tap_right` | PLAYER | 0–24 |
| `litefeet_woman_back_tap_right` | PARTNER | 0–24 |
| `litefeet_man_heel_dig_right` | PLAYER | 0–24 |
| `litefeet_woman_heel_dig_right` | PARTNER | 0–24 |
| `litefeet_man_toe_point_right` | PLAYER | 0–24 |
| `litefeet_woman_toe_point_right` | PARTNER | 0–24 |
| `litefeet_man_kick_right` | PLAYER | 0–24 |
| `litefeet_woman_kick_right` | PARTNER | 0–24 |
| `litefeet_man_knee_lift_right` | PLAYER | 0–24 |
| `litefeet_woman_knee_lift_right` | PARTNER | 0–24 |
| `litefeet_man_out_step_right` | PLAYER | 0–24 |
| `litefeet_woman_out_step_right` | PARTNER | 0–24 |
| `litefeet_man_shuffle_right` | PLAYER | 0–36 |

## Validation and concrete limits

- Blender authoring invocation: `blender -t 2 --background
  animations/man_and_woman/shared_scene_data.blend --python-exit-code 1
  --python scripts/litefeet/author_litefeet.py -- --resume --replace`.
  Stopped after 55 saved, checked source/export pairs. Half-frame checks passed
  for these clips; the bake compares every integer frame with evaluated source
  deform bones. Maximum bake-position difference:
  0.000000894 m.
- Maximum measured control/loop metrics across the 55 records:
  foot-plant drift 0.000152679 m; IK error 0.000228831 m;
  wrist bend 9.1424 degrees;
  loop-position mismatch 0.000000000 m;
  loop-angle mismatch 0.000000000 radians;
  boundary velocity mismatch 0.012913 m/s.
  Velocity uses 0.01-frame boundary probes. Clearance uses local proxies,
  rather than a comprehensive mesh-intersection proof.
- `blender -t 2 --background animations/man_and_woman/shared_scene_data.blend
  --python-exit-code 1 --python scripts/litefeet/verify_library.py -- --render`:
  interrupted by the stop instruction. Five Man clips passed sampled saved-mesh
  floor, knee-separation and bake checks: back-tap left/right, Bad One, bounce,
  Chicken Noodle. Four renders finished; the Chicken Noodle render did not finish.
  A separate earlier Woman bounce check found sole height about 0.000055 m and
  endpoint difference below 0.000001 m. Full saved-geometry and visual review remain open.
- Direct Godot **4.7.2** export check, run after stopping:
  `/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot --headless
  --path /tmp/litefeet/godot_validation --script verify_exports.gd --
  /workspace/sanjo-solutions/apps/a-game`:
  **PASS: 55 solo GLBs; 17,691 finite tracks resolve on the existing models.**
- Required final fast suite:
  `GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot python
  tests/run_tests.py --suite fast`: **8/9 passed**. `test_activity_json.gd`
  encountered missing imported hair-model resources (`bob01`, `bob02`,
  `short01`–`short04`, `afro01`), cascading into the `Character.STYLES` dependency.
  Hair source GLBs were hydrated, but their full-project imports remain incomplete.
  An earlier run with the default Godot 4.6.3 passed 9/9 before the project import attempt.
- Related suite: `GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot
  python tests/run_tests.py --changed scripts/litefeet/author_litefeet.py
  --changed animations/man_and_woman/litefeet_man_bounce.blend --slow-timeout 40`.
  Stopped by user instruction with 14 completed passing checks and 14
  completed failures/timeouts across fast and slow selections. Whole-playground
  checks encountered existing asset/import errors; the 40-second per-check bound
  also expired on dependent editor/scene checks. No complete-suite success is claimed.
  Exact check names and diagnostics are in `related_suite_interrupted.txt`.
- `git diff --check`: passed before recording. Storage is regular Git for every
  task binary (114 files, 55,096,906 bytes total, largest 1,236,754 bytes).
  No new LFS uploads are needed for these assets. Existing LFS source downloads
  used the environment credential through a temporary credential helper; its
  secret is outside all committed files.

## Processes and saved runtime state

Authoring PID 2780, geometry/render PID 3219, related-suite PID 2252, and its
Godot child PID 3277 were terminated. The earlier Godot PID 1708 and the last
Godot child may appear as defunct/reaped-pending process entries; they execute
no work. There are no continuing owned authoring/render jobs. Completed outputs
were copied from `.cache/litefeet_review` and `/tmp/litefeet` into the report paths
above. The in-memory working scene was discarded; the checkpoint is the 55 source
files plus `validation.json`. Temporary credential-helper files are local only.

The native bake initially exposed a parent-transform conversion error. The saved
55-clip set uses the corrected conversion: each child is converted relative to
its represented parent after decomposition, and the temporary export skeleton
releases connected heads. This keeps rest matrices, bone names and hierarchy
stable. Earlier faulty draft exports were overwritten before this checkpoint.

## Remaining work and resume commands

**69 of the planned 124 solo clips are unbuilt:** Woman right-shuffle; both
right heel-toe and right stomp-lock; eight hop clips; twenty held-position clips;
and thirty-six entry/exit clips. The later catalog sections and hop timing are
procedural designs awaiting rig evaluation. They are not completed assets.
The 55 saved clips also need the remaining full geometry review, motion playback,
style refinement and dancer review. Hat/removable-shoe tricks, spins and other
freestyle variants extend beyond the implemented floor-footwork catalog and remain
unfulfilled parts of the original broad scope.

Resume **only after renewed animation authorization**, from `apps/a-game`:

```sh
# Rehydrate the shared source dependencies with the authorized GitHub credential.
git lfs pull --include='apps/a-game/animations/man_and_woman/shared_scene_data.blend,apps/a-game/man_anatomical_study.blend,apps/a-game/woman_anatomical_study_speculum.blend,apps/a-game/dildo.blend'
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
# Continue from the committed per-clip checkpoint; uses Blender 5.2 only.
blender -t 2 --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/litefeet/author_litefeet.py -- --resume --replace
blender -t 2 --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/litefeet/verify_library.py -- --render
# Repair full-project resource imports, then repeat required suites.
GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot python tests/run_tests.py --suite fast
GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot python tests/run_tests.py --changed scripts/litefeet/author_litefeet.py --changed animations/man_and_woman/litefeet_man_bounce.blend
```

For direct export verification, create a temporary folder with `project.godot`
containing `config_version=5` and an application name, copy
`scripts/litefeet/verify_exports.gd` there, and use the direct Godot command above
with that folder and the current absolute checkout path.

Before staging resumed output, inspect actual sizes and Git attributes again.
Current main uses the generated size-based policy. Stage intended changes, run
`python scripts/lfs_policy.py check` from the repository root, and synchronize
when the measured sizes require it. Keep storage changes scoped to task assets.

## Integration verification after rebasing

The task preservation commit is `f9448df65c30803971506266f7c96eb92466c69b`,
rebased onto `18e528c73` (the bundled Game Rig Tools update). Current main introduced
the generated size-based LFS policy; `python scripts/lfs_policy.py sync` changed
only the attributes file, removed redundant task exceptions, and verified all
23,542 then-tracked files. Task binaries remain full Git blobs with manifest-matching
sizes. Historical before/after attribute logs describe the pre-rebase checkpoint;
`reports/attributes_integrated.txt` records the integrated state.

Read-only source inspection after stopping passed for all 55 `.blend` files:
exactly one authoring action and one baked action, one solo slot each, matching
roles and frame ranges. See `reports/source_structure.txt`.

After rebasing, the fast suite contains ten checks: **9/10 passed**. The same
hair-import/Character dependency blocks the activity JSON check. See
`reports/fast_suite_after_rebase.txt`. The isolated Godot export verification was
rerun through `TestRunner.execute` with a 60-second timeout and again passed all
55 GLBs / 17,691 tracks (`reports/godot_exports_after_rebase.txt`).

SHA-256 comparison confirmed that the shared scene and both anatomy source payloads
match the payloads used for authoring despite storage migration on main. Game Rig
Tools is now bundled by concurrent work; future sessions should run the current
`scripts/blender/install_animation_tools.py` setup rather than treating that tool
as an unavailable dependency. This integration performs documentation and storage
updates only; animation generation and rendering stay stopped.
