# Lambada repertoire: paused work status

Date: 2026-10-02 (UTC). Chat/task title: Lambada coordinated partner animations for man_and_woman3.blend.
Project: A-Game, sanjo-solutions cloud environment, `/workspace/sanjo-solutions/apps/a-game`.
Task branch at stop: `codex/lambada-repertoire`.
Current commit at stop: `3c52737c74b488501e9cfe47e7029547c6f5fe88`.
Record and delivery authored by Codex. The preservation commit is discoverable with
`git log --follow -- docs/animation_work_status/lambada_repertoire.md`.

## Scope and stopping point

The original request covered a broad organized Lambada repertoire for both characters,
including positions, moves, smooth transitions, natural motion, planted contacts,
body clearance, interpolated validation, and loop continuity. It specified Blender
5.2 for every Blender operation, the existing per-animation workflow, ordinary Git
for files at or below 104,857,600 bytes, separate workflow documentation, and delivery
to main while preserving concurrent work.

The later user instruction explicitly stopped animation authoring, refinement,
generation, and rendering. This record preserves the present state. **27 of 41
planned clips are saved authored procedural blocking studies; baked actions: 0;
Godot exports: 0. The repertoire is partial and requires further animation work.**
Numeric passes describe limited checks, not final production approval or a claim to
cover every regional Lambada move. The original completion request is superseded by
the preservation instruction.

Preparation completed: repository instructions and paired authoring workflow read;
existing yoga/disco pose and wrist utilities reused; A-Game LFS dependencies hydrated;
Blender 5.2.2 LTS downloaded and checksum-verified; executable build hash
`d13f752e3b9c`. All authoring, review renders, and Blender verification used
`/workspace/tools/blender-5.2.2-linux-x64/blender`. The system Blender 4.3.2 was
version-inspected only. Godot version: 4.6.3.

## Files and outputs

All paths below are relative to `apps/a-game`.

- `scripts/create_lambada.py`: preserved development generator for the planned 41-clip
  catalog. Uses `RigYogaPoser`, `DiscoWristPoser`, paired palm fitting, sparse channel
  writing, and `AnimationFileWriter`. Checkpoints the catalog after each successful
  save. Supports `--only`, `--start-at`, and the currently failing `--refine-saved`.
  Latest adaptive contact refinement and reversed right-turn reuse are development
  code; the saved assets predate those incomplete code paths.
- `scripts/validate_lambada.py`: saved-source metadata, interpolation, planted-contact,
  clearance-proxy, and loop checks; also contains the earlier review-render utility.
  The preservation run uses validation only. Default full-catalog validation expects
  41 clips; explicit `--only` selects the 27 saved clips.
- `scripts/lambada.md`: usage, planned vocabulary, timing, source workflow, storage,
  and explicit paused/partial state.
- `animations/man_and_woman/lambada_catalog.json`: 27 checkpointed source records with
  formations, roles, keyframes, phase markers, support intervals, and displacement.
- `animations/man_and_woman/lambada_validation.json`: final preservation verification
  of the current 27 saved files; asset hashes tie measurements to exact binaries.
- `animations/man_and_woman/lambada_*.blend`: the 27 files listed below. Each is a
  split source action with synchronized `Man.rigify` and `Woman.rigify` slots,
  participant `BOTH`, matching NLA bindings, and shared-scene metadata. They reference
  `shared_scene_data.blend`; shared scenes and character sources remain unchanged.
- `animations/man_and_woman/.gitattributes`: exact-filename ordinary-Git exceptions
  for these 27 measured small binary files; existing storage settings preserved.
- `docs/animation_work_status/lambada_repertoire/inventory.json`: per-asset byte counts,
  SHA-256 hashes, timing, role and authored/baked/exported state, and validation result.
- `docs/animation_work_status/lambada_repertoire/preservation_evidence.tar.gz`: all
  existing `.cache/lambada` logs and review PNGs, the previous two-clip validation
  report, preservation commands/results, plus two inspection scripts. The archive
  manifest records every member's size and SHA-256. Review images span earlier
  revisions and are historical evidence, not certification of the current assets.
- `docs/animation_work_status/lambada_repertoire/evidence_manifest.json`: archive
  member inventory and archive hash. No credentials are included.

All clips run at 24 fps and 120 BPM. Man leads; Woman follows. Stored loops include
a duplicate endpoint; playback excludes that last frame. Eight-beat loops store
0–96/play 0–95; sixteen-beat loops store 0–192/play 0–191. Travel is a one-shot:
left/right travel uses 0–96 with world X displacement +0.6/-0.6; the left traveling
turn uses 0–192 with +0.6 X. The catalog contains exact authored frames and plants.

| Source filename | Stored / playback frames | Bytes | Saved-file checks |
| --- | --- | ---: | --- |
| `lambada_basic_diagonal.blend` | 0–96 / 0–95 loop | 146263 | PASS (limited checks) |
| `lambada_basic_forward_back.blend` | 0–96 / 0–95 loop | 146009 | PASS (limited checks) |
| `lambada_basic_side.blend` | 0–96 / 0–95 loop | 144991 | PASS (limited checks) |
| `lambada_body_wave.blend` | 0–96 / 0–95 loop | 144693 | PASS (limited checks) |
| `lambada_closed_balance.blend` | 0–96 / 0–95 loop | 142324 | PASS (limited checks) |
| `lambada_couple_turn_left.blend` | 0–192 / 0–191 loop | 186743 | FAIL: paired_palm |
| `lambada_cross_step.blend` | 0–96 / 0–95 loop | 146447 | PASS (limited checks) |
| `lambada_follower_underarm_left.blend` | 0–192 / 0–191 loop | 179323 | PASS (limited checks) |
| `lambada_head_sway.blend` | 0–96 / 0–95 loop | 143797 | PASS (limited checks) |
| `lambada_lateral_opening.blend` | 0–96 / 0–95 loop | 153495 | PASS (limited checks) |
| `lambada_leader_turn_left.blend` | 0–192 / 0–191 loop | 175093 | FAIL: paired_palm |
| `lambada_open_balance.blend` | 0–96 / 0–95 loop | 142323 | PASS (limited checks) |
| `lambada_open_basic.blend` | 0–96 / 0–95 loop | 144668 | PASS (limited checks) |
| `lambada_open_break.blend` | 0–96 / 0–95 loop | 144988 | PASS (limited checks) |
| `lambada_promenade_balance.blend` | 0–96 / 0–95 loop | 144909 | PASS (limited checks) |
| `lambada_promenade_basic.blend` | 0–96 / 0–95 loop | 145992 | PASS (limited checks) |
| `lambada_rock_step.blend` | 0–96 / 0–95 loop | 146567 | PASS (limited checks) |
| `lambada_shadow_balance.blend` | 0–96 / 0–95 loop | 142015 | PASS (limited checks) |
| `lambada_shadow_basic.blend` | 0–96 / 0–95 loop | 143203 | PASS (limited checks) |
| `lambada_single_hand_balance.blend` | 0–96 / 0–95 loop | 142520 | PASS (limited checks) |
| `lambada_single_hand_basic.blend` | 0–96 / 0–95 loop | 144720 | PASS (limited checks) |
| `lambada_supported_cambre.blend` | 0–96 / 0–95 loop | 146253 | PASS (limited checks) |
| `lambada_travel_left.blend` | 0–96 / 0–96 once | 144674 | PASS (limited checks) |
| `lambada_travel_right.blend` | 0–96 / 0–96 once | 144784 | PASS (limited checks) |
| `lambada_traveling_turn_left.blend` | 0–192 / 0–192 once | 186793 | FAIL: paired_palm |
| `lambada_wrap_balance.blend` | 0–96 / 0–95 loop | 140962 | PASS (limited checks) |
| `lambada_wrap_basic.blend` | 0–96 / 0–95 loop | 143448 | PASS (limited checks) |

## Validation and limits

Preservation validation completed for all 27 current saved sources: **24/27 pass; 3/27 fail**. The validator exits 1 because of the preserved failures.

- `lambada_couple_turn_left`: paired_palm; maximum palm gap 0.038212927 m at frame 110.5 (limit 0.025 m).
- `lambada_leader_turn_left`: paired_palm; maximum palm gap 0.031203756 m at frame 114.0 (limit 0.025 m).
- `lambada_traveling_turn_left`: paired_palm; maximum palm gap 0.033139149 m at frame 110.5 (limit 0.025 m).

All recorded hashes match the current assets. No animation changes were made in response to these results.

The saved-source validator samples every half-frame, adds samples near loop
boundaries, and checks descriptor/slot/NLA metadata and finite keys. Thresholds:
IK reach 0.005 m, planted-foot error 0.004 m, palm gap 0.025 m, minimum floor
-0.005 m, torso proxy clearance 0.025 m, foot proxy clearance 0.01 m, loop pose
0.0001 m, orientation 0.001 rad, linear velocity 0.08 m/s, angular velocity
0.3 rad/s. Floor geometry is sampled at authored frames and the midpoint; other
checks use the interpolated samples. Torso/foot proxies are limited geometric
checks, not full-body collision or physical-balance validation. Full moving visual
review, transitions, and all finger/wrist/body interactions remain outstanding.

Commands and recorded results (logs are preserved in the evidence archive):

```sh
python tests/run_tests.py --suite fast
# preservation_fast.log: 10/10 passed in 7.01 seconds.
python -m py_compile scripts/create_lambada.py scripts/validate_lambada.py
# Passed after the final development edits and again during preservation.
PATH=/workspace/tools/blender-5.2.2-linux-x64:$PATH \
BLENDER=/workspace/tools/blender-5.2.2-linux-x64/blender \
python tests/run_tests.py \
  --changed scripts/player_assets/test_animation_files.py \
  --changed scripts/player_assets/test_animation_file_export.py \
  --changed scripts/player_assets/test_paired_animation_authoring.py \
  --changed scripts/player_assets/test_motion_review.py
# workflow_tests.log: 14/15 passed. Export fixture failed: Game Rig Tools add-on
# is absent; test_bake_cache.py raises StopIteration looking up game_rig_tools.
```

The focused source-file, motion-landmark, motion-review, and paired-authoring checks
passed. Native source composition through `animation_file_startup.py` passed for
`lambada_basic_side`, binding both rigs to the action (`source_open.log`). A broader
suite selected by the changed asset path was incomplete and failed with Godot
resource/parse assertions, renderer/RID cleanup errors, and 120-second timeouts;
it was terminated before completion (`related_tests.log`). One earlier runner
cleanup test also failed intermittently; the final required fast suite passed.
Some early runs preceded full asset hydration. These broad failures were not
independently established as baseline failures. Incidental tracked import/cache
changes were restored before delivery. Baking/export verification remains blocked
by the absent add-on; there are no new runtime artifacts to upload.

## Processes and concrete blockers

The last authoring command was:

```sh
/workspace/tools/blender-5.2.2-linux-x64/blender -b \
  animations/man_and_woman/shared_scene_data.blend -t 2 \
  --disable-autoexec --python-exit-code 1 --python scripts/create_lambada.py \
  -- --refine-saved --only couple_turn_left traveling_turn_left
```

It failed with `KeyError: 'pose.bones["f_index.01.L"].rotation_quaternion'` in
`ActivityMotionAuthor.write_samples` while mixing captured saved poses with newly
refined poses. It reached refinement candidates 53.5, 65.5, 102, 110.5, and 114
for `lambada_couple_turn_left`, then exited before `LAMBADA_SAVED`. Its PID was
6664, parent shell 6659, tool session 59370. On receipt of the stop instruction,
TERM was attempted for both; process inspection showed both had already exited.
The chained generation from `couple_turn_right` did not start. No source was saved
by this refinement attempt. `refine_turns.log` preserves the traceback. No owned
authoring, render, or test process remains after preservation verification.

Earlier direct generation of `couple_turn_right` failed a palm-reach fit at frame
68 (approximately 0.109 m). The newly added reverse-left-action path has not run.
It reverses quick/quick/slow phrasing and requires rhythm, marker, contact, loop,
and direction review before use. Correcting the refinement sample schema is a
prerequisite for that intended resume path. Saved generator reproducibility for
the whole catalog is therefore unresolved.

Four planned right-turn clips remain absent: `couple_turn_right`,
`follower_underarm_right`, `leader_turn_right`, and `traveling_turn_right`.
Ten directed transitions remain absent: `closed_to_open`, `open_to_closed`,
`closed_to_single_hand`, `single_hand_to_closed`, `closed_to_promenade`,
`promenade_to_closed`, `closed_to_shadow`, `shadow_to_closed`, `closed_to_wrap`,
and `wrap_to_closed` (all filenames would have the `lambada_` prefix).

Remaining work upon an explicit future resumption: fix refinement schema and current
contact failures; assess movement quality and all body clearance visually; finish
four right-turn and ten transition clips; validate every saved revision and directed
endpoint; review rhythm and role/hand exchanges. Baking/runtime export would require
Game Rig Tools and a separately requested runtime delivery scope.

## Exact resume and verification commands

The following read-only source validation can be repeated now. It writes only its
JSON measurement report and leaves source assets unchanged; a failing exit reflects
preserved animation issues. The full argv is also archived in
`preservation_validation_command.json`.

```sh
cd /workspace/sanjo-solutions/apps/a-game
/workspace/tools/blender-5.2.2-linux-x64/blender --version
python - <<'PY'
import json, subprocess
from pathlib import Path
records = json.loads(Path('animations/man_and_woman/lambada_catalog.json').read_text())['clips']
command = ['/workspace/tools/blender-5.2.2-linux-x64/blender', '-b',
           'animations/man_and_woman/shared_scene_data.blend', '-t', '2',
           '--disable-autoexec', '--python-exit-code', '1', '--python',
           'scripts/validate_lambada.py', '--', '--only']
command += [record['name'].removeprefix('lambada_') for record in records]
raise SystemExit(subprocess.run(command, timeout=600).returncode)
PY
python tests/run_tests.py --suite fast
```

Only after the user resumes animation work and the refinement schema is repaired:

```sh
cd /workspace/sanjo-solutions/apps/a-game
/workspace/tools/blender-5.2.2-linux-x64/blender -b \
  animations/man_and_woman/shared_scene_data.blend -t 2 \
  --disable-autoexec --python-exit-code 1 --python scripts/create_lambada.py \
  -- --refine-saved --only couple_turn_left traveling_turn_left
# Validate the refined left clips before reusing their actions.
/workspace/tools/blender-5.2.2-linux-x64/blender -b \
  animations/man_and_woman/shared_scene_data.blend -t 2 \
  --disable-autoexec --python-exit-code 1 --python scripts/create_lambada.py \
  -- --start-at couple_turn_right
# Full validation becomes applicable after all 41 files have been saved.
/workspace/tools/blender-5.2.2-linux-x64/blender -b \
  animations/man_and_woman/shared_scene_data.blend -t 2 \
  --disable-autoexec --python-exit-code 1 --python scripts/validate_lambada.py
```

These are exact intended resume commands, not a promise that the preserved failing
implementation will succeed. Render review remains paused. Rehydrate shared and
linked LFS objects when resuming in a fresh checkout: `git lfs pull --include='apps/a-game/**'`
from the repository root. The Blender executable and add-on must be provisioned in
a new environment; neither is committed as part of this task.

## Storage and integration

Every task asset and evidence archive is measured below 104,857,600 bytes and stored
as an ordinary Git blob. Exact `.blend` exceptions are scoped to the listed task
files; existing LFS assets keep their attributes. Staged binary hashes are checked
against the inventory. Required task asset uploads are part of the ordinary Git
push; there are no newly introduced LFS objects.

Delivery sequence: preservation commit; fetch and rebase onto current origin/main;
separate Animation-section documentation commit; fresh fetch immediately before
main integration; ordinary merge/push retaining concurrent history; remote commit
and task ancestry verification. Git commit trailers identify Codex authorship.
Final task, documentation, merge, and remote hashes are reported in the chat because
embedding a commit's own hash in its contents would create a circular reference.

## Integration follow-up

The preservation commit was rebased onto origin/main at
`074c6a02e`. Concurrent Tango, New York Hustle, and solo cha-cha storage
entries were retained alongside all 27 Lambada entries. This newer main includes
the bundled Game Rig Tools installer and updated animation helpers. The historical
export-fixture failure above describes the pre-rebase environment. A future resume
can install the bundled tools using Blender 5.2:

```sh
cd /workspace/sanjo-solutions/apps/a-game
/workspace/tools/blender-5.2.2-linux-x64/blender --background \
  --python-exit-code 1 --python scripts/blender/install_animation_tools.py
```

Installation and bake/export fixture generation remain deferred during the user
requested stop. Asset measurements in the preservation report were produced on
the recorded pre-rebase source revision; source hashes remain unchanged after
integration. Revalidate against the newer helpers and shared scene on a future
resume. The final integration checks are recorded below.

Post-rebase `python tests/run_tests.py --suite fast`: **10/10 passed in 6.35
seconds**, preserved in `lambada_repertoire/integration_fast.log`.
`python scripts/lfs_policy.py check` from the repository root passed for 24,137
indexed files. All 27 source hashes match both the rebased commit and working
files. `git diff --check` passed. The separate `AGENTS.md` update adds formation
foot-phase guidance and a link to this paused study with its refinement blocker.
