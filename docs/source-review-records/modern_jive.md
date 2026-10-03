# Modern jive stopped work status

Recorded by Codex on 2026-10-02 (UTC; preservation audit completed around 15:10 UTC).
Chat: **Create Modern jive animations**, ID `01a0fce4-b6ce-70a0-8c87-5179e31d0050`.
Checkout: `/workspace/sanjo-solutions/apps/a-game`, sanjo-solutions cloud environment.
Task branch at stop: `codex/modern-jive`. Current commit before preservation commits:
`3c52737c74b488501e9cfe47e7029547c6f5fe88`. All task changes were uncommitted at stop.
This record describes the pre-integration snapshot; subsequent Git history records delivery commits.

## Instruction and scope

The original request covered coordinated Modern jive, Ceroc, and LeRoc moves and
positions for both characters in `man_and_woman3.blend`, Blender 5.2 throughout,
per-animation sources, reuse, natural motion, planted contacts, body clearance,
interpolated/loop validation, documentation, and publication to main.
The 2026-10-02 stop instruction supersedes further animation work. Authoring and
rendering ceased immediately; only read-only saved-source checks and delivery
records followed. Resume authoring only after a new user instruction.

**State: 42 partial authored procedural blocking studies; 0 baked actions; 0
exported runtime clips.** These files are preservation assets, not a completed
or exhaustive Ceroc/LeRoc syllabus. The generator plans 43 clips. The missing
travelling return has never been saved. `modern_jive_catalog.json` has never been
written because the generator requires all 43 sources first.

## Preparation and completed work

Blender **5.2.2 LTS**, build `d13f752e3b9c`, was downloaded from the official Blender
release site and verified against its published SHA-256 list. Every Blender
operation used `/tmp/modern-jive-tools/blender-5.2.2-linux-x64/blender`.
The installed Blender 4.3.2 was only queried for its version.
Real Git LFS shared scene, character, prop, existing animation and hair test
fixture objects were retrieved. Existing tracked source contents remain unchanged.

The generator reuses `RigYogaPoser`, the yoga mountain base, paired IK palm
calibration, `ActivityMotionAuthor.write_samples`, `AnimationTracks`, and
`AnimationFileWriter`. Existing disco choreography informed beat phrasing; its
independent arm choreography was not copied into partner actions. New paired paths
use alternating support/swing, raised hand targets, native wrist constraints,
soft finger curl, meaningful IK samples, quaternion continuity, simplified constant
curves, and flat endpoint tangents. Several earlier sources still predate the last
planner changes. The current generator is work in progress and is not a verified
reproduction of every preserved file.

All saved sources contain one authored action with `OBMan.rigify` and
`OBWoman.rigify` slots, participant `BOTH`, explicit ranges, and synchronized NLA
binding metadata. Roles: **Man/player leads; Woman/partner follows**. Timing:
24 fps, nominal 120 BPM, 12 frames/beat. Positions and basics store 0–96 with a
repeated endpoint and play 0–95. Turns and transitions play 0–96 once; figures and
passes play 0–144 once. Each row below shares these roles and authored-only state.

## Durable files and assets

Paths here are relative to `apps/a-game`.

- `scripts/create_modern_jive.py`: stopped procedural authoring generator.
- `scripts/validate_modern_jive.py`: saved-action checks and optional review renderer;
  the stop audit used validation only, with no render arguments.
- `scripts/modern_jive.md`: repertoire, workflow and explicit partial-state guidance.
- `animations/man_and_woman/modern_jive_validation.json`: final stop audit of all
  42 existing files, including source hashes, tolerances, failures and endpoint checks.
- `animations/man_and_woman/.gitattributes`: exact-name ordinary-Git exceptions
  for these 42 files. Shared/character storage rules remain in force.
- `docs/animation_work_status/modern_jive.md`: this status record.
- `docs/animation_work_status/modern_jive_evidence/saved_source_inventory.json`:
  each planned file, observed saved actions, byte size, SHA-256, slots, bindings,
  frame range, playback end, and authored/baked/exported state.
- `docs/animation_work_status/modern_jive_evidence/audit_saved_sources.py`:
  read-only Blender 5.2 source inspection; writes only the inventory JSON.
- `docs/animation_work_status/modern_jive_evidence/source_smoke.py` and `smoke.log`:
  individual-source composition and chooser smoke check.
- `docs/animation_work_status/modern_jive_evidence/review/`: 42 existing pose PNGs;
  `sheets/`: two existing review sheets. These were rendered before the stop and
  include historical revisions. They are illustrative evidence, not final playback
  certification. `sheets.log` maps sheet cells to filenames.
- The evidence directory also preserves authoring stop/failure logs, historical
  selected validations, initial/full-run test logs, and stop-time verification logs.
  `preserved_file_inventory.json` lists every preserved evidence file with its hash.
  Historical selected checks are superseded by the full stop audit where they differ.
- Evidence `.gitattributes` lists the 44 exact PNG paths for ordinary Git storage.

The 42 source binaries total **6,282,862 bytes**; the largest is **237,043 bytes**.
All new source and preview binaries are below 104,857,600 bytes. Their actual
sizes and `git check-attr` results were checked before staging. These new assets
use ordinary Git, so their upload is part of the Git push and requires no new
LFS upload. Existing LFS objects are dependencies, not new task assets.

## Saved source inventory

All paths below are under `animations/man_and_woman/`. PASS means the current
sampled diagnostics passed; every asset remains a partial procedural blocking study.

| File | Family | Stored range / playback | Bytes | Stop audit |
| --- | --- | --- | ---: | --- |
| `modern_jive_position_open.blend` | Position | 0–96; loop 0–95 | 123573 | PASS sampled checks |
| `modern_jive_position_double_hand.blend` | Position | 0–96; loop 0–95 | 124462 | PASS sampled checks |
| `modern_jive_position_right_hand.blend` | Position | 0–96; loop 0–95 | 123116 | PASS sampled checks |
| `modern_jive_position_closed.blend` | Position | 0–96; loop 0–95 | 124216 | FAIL: Leg capsule clearance |
| `modern_jive_position_promenade.blend` | Position | 0–96; loop 0–95 | 122911 | PASS sampled checks |
| `modern_jive_position_side_by_side.blend` | Position | 0–96; loop 0–95 | 122134 | PASS sampled checks |
| `modern_jive_position_basket.blend` | Position | 0–96; loop 0–95 | 124152 | PASS sampled checks |
| `modern_jive_position_tandem.blend` | Position | 0–96; loop 0–95 | 123886 | PASS sampled checks |
| `modern_jive_basic_rock_step.blend` | Basic | 0–96; loop 0–95 | 127261 | PASS sampled checks |
| `modern_jive_side_step.blend` | Basic | 0–96; loop 0–95 | 126602 | PASS sampled checks |
| `modern_jive_forward_back_basic.blend` | Basic | 0–96; loop 0–95 | 127016 | PASS sampled checks |
| `modern_jive_concertina.blend` | Basic | 0–96; loop 0–95 | 128104 | PASS sampled checks |
| `modern_jive_arm_jive.blend` | Basic | 0–96; loop 0–95 | 125874 | PASS sampled checks |
| `modern_jive_follower_underarm_turn.blend` | Turn | 0–96; once | 149751 | PASS sampled checks |
| `modern_jive_follower_return.blend` | Turn | 0–96; once | 149197 | PASS sampled checks |
| `modern_jive_leader_underarm_turn.blend` | Turn | 0–96; once | 171176 | PASS sampled checks |
| `modern_jive_leader_return.blend` | Turn | 0–96; once | 171216 | PASS sampled checks |
| `modern_jive_follower_free_spin.blend` | Turn | 0–96; once | 148122 | PASS sampled checks |
| `modern_jive_leader_free_spin.blend` | Turn | 0–96; once | 145116 | PASS sampled checks |
| `modern_jive_first_move.blend` | Figure | 0–144; once | 237043 | PASS sampled checks |
| `modern_jive_basket.blend` | Figure | 0–144; once | 194794 | PASS sampled checks |
| `modern_jive_in_and_out.blend` | Figure | 0–144; once | 131089 | PASS sampled checks |
| `modern_jive_side_by_side_break.blend` | Figure | 0–144; once | 187909 | PASS sampled checks |
| `modern_jive_tandem_walk.blend` | Figure | 0–144; once | 188885 | PASS sampled checks |
| `modern_jive_left_side_pass.blend` | Pass | 0–144; once | 201329 | FAIL: Leg capsule clearance |
| `modern_jive_right_side_pass.blend` | Pass | 0–144; once | 199704 | FAIL: Leg capsule clearance |
| `modern_jive_travelling_return.blend` | Pass | planned 0–144, once | — | MISSING: solver failure before save |
| `modern_jive_change_places.blend` | Pass | 0–144; once | 201639 | FAIL: Leg capsule clearance |
| `modern_jive_both_hands_turn.blend` | Turn | 0–96; once | 184059 | PASS sampled checks |
| `modern_jive_open_to_double_hand.blend` | Transition | 0–96; once | 124981 | PASS sampled checks |
| `modern_jive_double_hand_to_open.blend` | Transition | 0–96; once | 124956 | PASS sampled checks |
| `modern_jive_open_to_right_hand.blend` | Transition | 0–96; once | 124208 | PASS sampled checks |
| `modern_jive_right_hand_to_open.blend` | Transition | 0–96; once | 124194 | PASS sampled checks |
| `modern_jive_open_to_closed.blend` | Transition | 0–96; once | 131349 | FAIL: Leg capsule clearance |
| `modern_jive_closed_to_open.blend` | Transition | 0–96; once | 131468 | FAIL: Leg capsule clearance |
| `modern_jive_open_to_promenade.blend` | Transition | 0–96; once | 199581 | PASS sampled checks |
| `modern_jive_promenade_to_open.blend` | Transition | 0–96; once | 199283 | PASS sampled checks |
| `modern_jive_open_to_side_by_side.blend` | Transition | 0–96; once | 139663 | FAIL: Palm contact, Planted foot |
| `modern_jive_side_by_side_to_open.blend` | Transition | 0–96; once | 139511 | FAIL: Palm contact, Planted foot |
| `modern_jive_open_to_basket.blend` | Transition | 0–96; once | 140804 | FAIL: Palm contact, Planted foot |
| `modern_jive_basket_to_open.blend` | Transition | 0–96; once | 139713 | FAIL: Palm contact, Planted foot |
| `modern_jive_open_to_tandem.blend` | Transition | 0–96; once | 139369 | FAIL: Planted foot |
| `modern_jive_tandem_to_open.blend` | Transition | 0–96; once | 139446 | FAIL: Planted foot |

## Verification

Commands run from `apps/a-game`; `BLENDER` refers to the 5.2.2 binary above.

- `python tests/run_tests.py --suite fast`: **10/10 PASS**, stop-time rerun,
  `modern_jive_evidence/stop_fast.log`. Earlier missing hair LFS fixtures were
  retrieved; an earlier transient process-tree check also passed on rerun.
- `BLENDER="$BLENDER" python tests/run_tests.py --suite changed --changed scripts/player_assets/test_paired_animation_authoring.py --changed scripts/player_assets/test_animation_files.py`:
  **13/13 PASS**, including fast suite and three workflow checks;
  `modern_jive_evidence/stop_workflow_tests.log` (also earlier `workflow_tests.log`).
- Saved-file validator with `--only` selecting the 42 existing suffixes: **exit 1**,
  **30 pass / 12 fail**, **4,786 evaluated samples**. Every named entry/exit endpoint
  matches its saved position clip. All 13 loop clips pass pose and velocity closure.
  Structural checks, finite keys, movement, IK reach, mesh-floor clearance and torso
  proxies pass for all 42. Six clips fail leg capsules; four older transitions fail
  both palm and planted-foot expectations; two older tandem transitions fail foot
  expectations. See table and JSON for exact values. Samples occur every 0.75
  frames for changing facings, otherwise 1.5, plus 0.1/0.5 boundary samples;
  full-mesh floor checks occur each beat. Planner-dependent contact/plant checks
  compare earlier sources against the stopped generator's current choreography.
- `"$BLENDER" -t 2 -b --factory-startup --disable-autoexec --python-exit-code 1 --python docs/animation_work_status/modern_jive_evidence/audit_saved_sources.py`:
  **exit 0**, 42 actual action inventories and one missing planned source.
  Every observed file hash matches the stop validation report.
- Individual `modern_jive_arm_jive.blend` startup/chooser smoke: **PASS** for runtime
  scene composition, chooser entry, 24 fps and both slot/NLA bindings; `smoke.log`.
  Full combined-library chooser and runtime playback verification remain pending.
- Earlier `BLENDER="$BLENDER" python tests/run_tests.py`: broader selection included
  57 slow checks. It encountered missing Godot imported/runtime animation resources
  (Nil animation libraries) and stalled in `playground/test_activity_animation_methods.gd`.
  The owned runner PID 2403 was terminated with process-tree cleanup. This broader
  suite is **incomplete / environment blocked**, not passed; `related_tests.log`.

Rendered pose review inspected representative holds, figures and passes before
stop. Complete animation playback, detailed wrist/finger/body-surface collision,
physical balance and runtime export review remain pending. Capsule/sphere proxies
provide sampled diagnostics rather than a complete mesh collision guarantee.

## Exact stopping point and processes

The last owned authoring process, PID **4008**, received SIGTERM and exited **143**.
Its `transitions_b.log` records saved `open_to_promenade` and `promenade_to_open`,
then `JIVE_AUTHOR modern_jive_open_to_side_by_side` with no subsequent save.
The prior saved `open_to_side_by_side` file remains intact. Its six-clip batch also
included `side_by_side_to_open`, `open_to_basket`, and `basket_to_open`; those retain
older sources. `transitions_a.log` records the six simple double/right/closed
transitions saved before stop. `transitions_c.log` records travelling-return failure
before either tandem transition could be regenerated.

No authoring or rendering process remains. Stop-time verification processes finished.
The ignored `.cache/modern_jive/review` and `sheets` outputs remain locally and were
copied into committed evidence. Temporary Blender installation, diagnostic scripts
and historical logs remain under `/tmp/modern-jive-tools` for immediate resumption;
that temporary directory is environment-local. Critical evidence is committed here.
No further animations or renders were created after the stop instruction.

## Remaining work and concrete blockers

1. Await user authorization before resuming animation work.
2. Resolve `modern_jive_travelling_return` authoring failure at frame **54**:
   `partner.right_palm: distance=0.00597, angle=0.0000`, beyond the solver limit.
   No durable `.blend` exists for this clip; see `transitions_c.log`.
3. Address the twelve saved-file failures without treating older sampled passes as
   completion. The exact finite-segment leg calculation revealed clearance failures
   in closed holds/transitions and the three passing studies. Reconcile six older
   side-by-side/basket/tandem transitions with the current foot/contact planner.
4. Finish natural-motion and full playback review, contact orientation, detailed
   body clearance, key economy, and smooth transitions. `change_places` shares the
   left-pass path; independent figure differentiation remains design work.
5. Complete the intended repertoire/catalog and clarify further school-specific
   names/variants. Role-reversed variants, dips, drops, aerials and lifts are outside
   the authored snapshot. Current files do not fulfill “all moves and positions.”
6. Bake, save baked actions, export through the repository addon and validate Godot
   imports/runtime only after source quality is accepted. Prepare missing imported
   runtime dependencies before retrying the broader slow suite.

## Exact resume commands

These first commands only inspect/validate saved files. They perform no authoring
or rendering. The validator's exit 1 is expected for the preserved partial snapshot.

```sh
cd /workspace/sanjo-solutions/apps/a-game
export BLENDER=/tmp/modern-jive-tools/blender-5.2.2-linux-x64/blender
"$BLENDER" --version
python tests/run_tests.py --suite fast
BLENDER="$BLENDER" python tests/run_tests.py --suite changed \
  --changed scripts/player_assets/test_paired_animation_authoring.py \
  --changed scripts/player_assets/test_animation_files.py
"$BLENDER" -t 2 -b --factory-startup --disable-autoexec --python-exit-code 1 \
  --python docs/animation_work_status/modern_jive_evidence/audit_saved_sources.py
python - <<'CHECK'
from pathlib import Path
import os, subprocess
root = Path('animations/man_and_woman')
names = [p.stem.removeprefix('modern_jive_') for p in sorted(root.glob('modern_jive_*.blend'))]
raise SystemExit(subprocess.call([os.environ['BLENDER'], '-t', '2', '-b',
    str(root / 'shared_scene_data.blend'), '--disable-autoexec', '--python-exit-code', '1',
    '--python', 'scripts/validate_modern_jive.py', '--', '--only', *names]))
CHECK
"$BLENDER" -t 2 -b animations/man_and_woman/modern_jive_arm_jive.blend \
  --disable-autoexec --python-exit-code 1 \
  --python docs/animation_work_status/modern_jive_evidence/source_smoke.py
```

On a replacement environment, install an official Blender 5.2 release, verify its
published checksum, set `BLENDER` accordingly, and retrieve real linked Git LFS
objects before opening sources. The current environment's authorized read command is:

```sh
GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=http.https://github.com/.extraheader \
GIT_CONFIG_VALUE_0="Authorization: Bearer ${SANJO_GITHUB_LFS_TOKEN:?}" \
git lfs pull --include='apps/a-game/man_and_woman3.blend,apps/a-game/animations/man_and_woman/*.blend,apps/a-game/man_anatomical_study.blend,apps/a-game/woman_anatomical_study_speculum.blend,apps/a-game/dildo.blend,apps/a-game/playground/hair/physics/*_mesh.res' --exclude=''
```

After explicit authorization and a solver fix, the missing-clip repro command is:

```sh
"$BLENDER" -t 2 -b animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/create_modern_jive.py \
  -- --only travelling_return
```

It currently fails at frame 54. For a resumed stopped batch, select
`open_to_side_by_side side_by_side_to_open open_to_basket basket_to_open open_to_tandem tandem_to_open`
with the same `--only` option, then validate the actual saved files. Preserve the
snapshot before authoring: the generator overwrites selected source files. Use
**Bake & Export Active Animation** from accepted individual sources to create runtime
assets; that step has not been performed for this task.

## Integration verification

The preservation commit was rebased onto fetched `origin/main` at
`de89cfea0` on 2026-10-02. The `.gitattributes` conflict was resolved by retaining
every concurrent exact-file rule and the Modern jive rules. The three shared/character
binary SHA-256 values still match the stop validation report after main's concurrent
storage conversion. Modern jive source/preview contents remain unchanged.
`python scripts/lfs_policy.py check` from the repository root passed for all 24,540
staged files after rebase. The focused workflow suite was rerun after integration
and passed **13/13**, including the required fast checks.

Concurrent main added the bundled Blender tools setup and changed quaternion sign
handling in `PoseSnapshot` and the combined-library reference property layout.
The report remains evidence of the stopped saved assets, not a claim that a future
regeneration under the newer helpers produces identical files. Before future source
work, follow `scripts/blender/README.md` and run
`"$BLENDER" --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py`
with the same profile used by later authoring/validation/export subprocesses.

The subsequent documentation commit adds this integration note and two Modern jive
lessons to the `# Animation` section of `AGENTS.md`: preserve planner/report provenance,
and use exact finite-segment distances for planted-leg capsule checks.
