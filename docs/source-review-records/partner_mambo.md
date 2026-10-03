# Partner mambo — preservation status

## Stop instruction and identity

- Date: October 2, 2026; authoring/rendering stopped at 16:55:49 Europe/Berlin (14:55:49 UTC).
- Chat title: **Create Partner mambo animations**.
- Chat ID: `01a0fce9-00bb-74c6-a3ec-3c9fde80a04c`.
- Author of this record and associated GitHub commits: **Codex**.
- Workspace: `/workspace/sanjo-solutions`, project `apps/a-game`, sanjo-solutions cloud environment.
- Task branch: `task/partner-mambo`.
- Current commit when stopped: `3c52737c74b488501e9cfe47e7029547c6f5fe88`.
- The user's stop instruction superseded further animation generation, refinement, and rendering. Delivery preserves the present state, including failed procedural studies. Further animation work requires a new user instruction.

## Original scope and actual delivery

The original request covered a broad coordinated Partner mambo repertoire for both characters in `man_and_woman3.blend`, using Blender 5.2, the repository's IK and individual-source workflow, natural movement, contacts, clearance, and smooth transitions. It also requested Git storage through 100 MiB, asset and documentation commits, integration with current main, and a verified push.

The procedural generator defines 48 planned clips. **28 individual sources were saved before stopping**: eight partner positions, sixteen footwork patterns, and four spot turns. These are editable procedural drafts; the spot turns are explicitly **blocking studies with failed contact/clearance checks**. The original repertoire remains partial.

**Authored: 28. Baked: 0. Exported runtime GLBs: 0.** Shared rigs, anatomical sources, the combined library, and existing runtime exports retain their prior contents. Individual-source composition for `partner_mambo_basic_open.blend` passed, including both rigs and matching NLA slot bindings.

All sources use 24 fps and 120 beats/minute, with on-2 landings at phrase frames 12, 24, 36, 60, 72, and 84 (2–3–4 / 6–7–8). `Man.rigify` is the leader/player and `Woman.rigify` is the follower/partner. Position and footwork sources store 0–96 and play 0–95. The four turn sources store 0–192 and play 0–191. Each source has two action slots, participant metadata, count markers, and explicit loop/range metadata.

## Exact asset inventory

All source filenames below live under `animations/man_and_woman/`, begin with `partner_mambo_`, and end with `.blend`. The adjacent [saved_assets.json](partner_mambo/saved_assets.json) lists every exact path, byte size, SHA-256, frame range, playback end, and authored/baked/exported state.

| Category | Exact filename stems after `partner_mambo_` | Saved |
| --- | --- | ---: |
| Positions | `position_open_single`, `position_open_double`, `position_closed`, `position_handshake`, `position_cross_hand`, `position_promenade`, `position_side_by_side`, `position_shadow` | 8 |
| Footwork | `basic_open`, `basic_closed`, `basic_double_hold`, `side_basic`, `back_basic`, `forward_breaks`, `cucaracha`, `progressive_basic`, `diagonal_breaks`, `fifth_position_breaks`, `open_break`, `side_by_side_basic`, `promenade_walks`, `shadow_basic`, `suzie_q`, `crossovers` | 16 |
| Blocking turn studies | `follower_spot_turn_right`, `follower_spot_turn_left`, `leader_spot_turn_right`, `leader_spot_turn_left` | 4 |

Relevant task files:

- `scripts/create_partner_mambo.py`: procedural author, foot planner, contact fitting, action writer, and planned 48-clip repertoire. It composes existing repository authoring APIs. The final script contains a traveling-contact orientation adjustment that had yet to execute when work stopped.
- `scripts/validate_partner_mambo.py`: saved-source validator and optional review renderer. Stop-state verification invokes validation only, with rendering omitted.
- `scripts/partner_mambo.md`: timing, planned coverage, individual-source editing, storage, and reproduction guide; its opening explicitly distinguishes the 28 saved drafts from planned coverage.
- `animations/man_and_woman/.gitattributes`: 28 exact-filename ordinary-Git entries added for this task's sources.
- `docs/animation_work_status/partner_mambo/saved_assets.json`: exact delivered source inventory.
- `docs/animation_work_status/partner_mambo/saved_asset_validation.json`: final read-only verification of all 28 saved binaries.
- `docs/animation_work_status/partner_mambo/review/`: 31 existing Blender review PNGs and exact-filename Git attributes. `preserved_outputs.json` lists each image and log with its hash and size.
- `docs/animation_work_status/partner_mambo/*.log`: existing generation, selected verification, source composition, fast/focused test logs, and final saved-source validation output.

The complete-library `partner_mambo_catalog.json` and `partner_mambo_validation.json` were never produced; full generation had yet to finish. The preservation inventory and selected saved-source validation are the authoritative delivered evidence.

## Validation and limits

Final read-only saved-source validation: **24/28 pass; 4/28 fail**. Blender exited with status 1 as intended for failed checks. The precise metrics, sample frames, tolerances, and source hashes appear in [saved_asset_validation.json](partner_mambo/saved_asset_validation.json).

| Source | Failed checks | Maximum palm gap | Minimum leg-proxy clearance |
| --- | --- | ---: | ---: |
| `partner_mambo_follower_spot_turn_right` | Palm gap, Leg clearance | 0.035522 m | -0.023327 m |
| `partner_mambo_follower_spot_turn_left` | Palm gap, Leg clearance | 0.064569 m | -0.052172 m |
| `partner_mambo_leader_spot_turn_right` | Palm gap, Leg clearance | 0.067150 m | -0.052733 m |
| `partner_mambo_leader_spot_turn_left` | Palm gap, Leg clearance | 0.036737 m | -0.015765 m |


Verification commands, from `apps/a-game`:

```sh
python tests/run_tests.py --suite fast
python tests/run_tests.py --suite changed \
  --changed scripts/player_assets/test_animation_files.py \
  --changed scripts/player_assets/test_paired_animation_authoring.py \
  --changed scripts/player_assets/test_motion_review.py \
  --blender /workspace/tools/blender-5.2.2-linux-x64/blender
```

The fast suite passed **10/10** after the stop instruction. The focused runner passed **14/14**, including the fast set and four selected Blender checks. The initial fast attempt failed because three hair mesh resources were Git LFS pointers; retrieving their actual objects resolved that environmental failure. Python syntax compilation and `git diff --check` passed.

Individual-source composition passed with:

```sh
/workspace/tools/blender-5.2.2-linux-x64/blender -t 2 \
  --background animations/man_and_woman/partner_mambo_basic_open.blend \
  --disable-autoexec --python-exit-code 1 \
  --python scripts/player_assets/animation_file_startup.py \
  --python /workspace/task-tools/check_mambo_source.py
```

The temporary check asserted a runtime working scene, a local source action, two correct rig/NLA/slot bindings, and 24 fps. Its preserved log is `partner_mambo/mambo-compose.log`.

Final saved-source verification used the following read-only command. It writes a report and leaves the source files unchanged. Its failure exit is expected for the four preserved turn studies:

```sh
python - <<'PY'
from pathlib import Path
import subprocess
names = [path.stem.removeprefix('partner_mambo_')
         for path in sorted(Path('animations/man_and_woman').glob('partner_mambo_*.blend'))]
subprocess.run([
    '/workspace/tools/blender-5.2.2-linux-x64/blender', '-t', '3', '--background',
    'animations/man_and_woman/shared_scene_data.blend', '--disable-autoexec',
    '--python-exit-code', '1', '--python', 'scripts/validate_partner_mambo.py',
    '--', '--only', *names], check=True)
PY
```

Checks include saved action structure, finite keys and handles, actual movement, evaluated IK reach, planted ankle positions and orientation, calibrated palm gaps during defined holds, mesh floor samples, torso/leg clearance proxies, and loop position/orientation/velocity. Samples include meaningful keys and half frames every three frames. Floor mesh checks use start, midpoint, and end; the ankle checks cover all samples. These are geometric checks, with physical balance, comprehensive mesh collision, and full visual playback review still pending.

Existing rendered frames were inspected for the basic open, closed, promenade, and side-by-side formations. The first basic-open render sequence predates a forward/back direction correction and serves as prototype evidence; it is not a visual receipt for the final binary hash. Existing follower-turn review renders were preserved when the render process stopped. Headless EGL warnings accompanied successful image saves and were not export failures. The 31 PNGs are existing still-frame review output; a complete playback review remains pending.

## Processes and environment at stop

Owned authoring PID `3048` and combined validation/render PID `3223` received SIGTERM on the stop instruction. Both terminated; their already-saved files were preserved. The generator had saved all four spot turns and was approaching the first underarm-turn task; neither underarm source exists. The renderer saved four right-turn images and three left-turn images; the left-turn frame-168 image was pending. No authoring/rendering process was restarted. A read-only verification process then inspected all saved files and exited after writing its report.

Blender executable: `/workspace/tools/blender-5.2.2-linux-x64/blender`, verified **5.2.2 LTS**, build `d13f752e3b9c`. The system `/usr/bin/blender` is 4.3.2 and was used only for a version query. All asset authoring, loading, validation, and rendering used 5.2.2.

Retrieved linked assets include `shared_scene_data.blend`, `man_and_woman3.blend`, `man_anatomical_study.blend`, `woman_anatomical_study_speculum.blend`, and `dildo.blend`; their binary contents remain unchanged by this task. Concurrent main work converted their storage to the repository's size-based Git policy. Existing `idle.blend` and `solo_disco_dance.blend` were retrieved for reuse assessment. The new choreography reuses the existing posing/contact/file-writing APIs; it does not copy the disco movement into mambo.

Local logs and temporary probes remain in `/workspace/task-tools/` for this environment. Durable evidence is copied into the task's documentation directory. The configured `SANJO_GITHUB_LFS_TOKEN` supported GitHub asset retrieval through the existing proxy; credential values are absent from the task files.

## Remaining work and concrete blockers

1. Obtain renewed authorization before any further animation work.
2. Repair all four spot-turn studies. Inspect the failed palm-reconnection intervals and crossed-leg trajectories, then rerun saved-file validation and visual playback review.
3. Author the remaining 20 planned sources: two underarm turns; cross-body lead, cross-body inside/outside turn, and walkaround; fourteen directed transitions between open-single and the seven other formations.
4. Exercise the untested traveling-contact orientation code and transition end-pose comparisons. A generator definition is planning code, not an authored asset.
5. Complete visual motion, wrist/finger surface-fit, balance, and body-overlap review for every delivered and future clip. Passing proxies alone do not establish production readiness.
6. Produce the complete catalog and full validation report only after the entire intended set exists and passes.
7. Bake/export through Player Asset Export only when runtime output is authorized; retain baked actions in their individual sources and validate runtime imports.

Current technical blockers are the recorded contact/leg-clearance failures and pending choreography/review. GitHub LFS authentication was resolved during preparation. Every new task binary is below 100 MiB and uses ordinary Git, so this task adds zero LFS uploads.

## Exact resume commands after renewed authorization

```sh
cd /workspace/sanjo-solutions/apps/a-game
/workspace/tools/blender-5.2.2-linux-x64/blender --version
```

Inspect this status, `saved_asset_validation.json`, and the turn review images first. After repairing the turn planner/contact schedule, regenerate only those studies:

```sh
/workspace/tools/blender-5.2.2-linux-x64/blender --background \
  animations/man_and_woman/shared_scene_data.blend --disable-autoexec \
  --python-exit-code 1 --python scripts/create_partner_mambo.py -- --only \
  follower_spot_turn_right follower_spot_turn_left \
  leader_spot_turn_right leader_spot_turn_left
```

After those repairs, continue the pending repertoire and run the complete review:

```sh
/workspace/tools/blender-5.2.2-linux-x64/blender --background \
  animations/man_and_woman/shared_scene_data.blend --disable-autoexec \
  --python-exit-code 1 --python scripts/create_partner_mambo.py -- --resume
/workspace/tools/blender-5.2.2-linux-x64/blender --background \
  animations/man_and_woman/shared_scene_data.blend --disable-autoexec \
  --python-exit-code 1 --python scripts/validate_partner_mambo.py -- \
  --render .cache/partner_mambo/review
```

`--resume` trusts existing sources. Use a full regeneration after changes affecting existing clips, and refresh binary hashes after each validation. Inspect actual sizes and attributes before staging new files.

## Storage and integration

The 28 source binaries total **3,916,399 bytes**; the largest is **161,109 bytes**. The 31 preserved review PNGs total **4,879,739 bytes**. Exact-filename `.gitattributes` entries keep these intended binaries in ordinary Git; the integrated repository policy controls shared-asset storage. Staged blobs are checked against their recorded hashes.

The preservation commit is followed by a fetch/rebase onto current `origin/main` and a separate `AGENTS.md` documentation commit, then main integration. Concurrent work is preserved through ordinary fetch, rebase/merge, and push operations. Final integration hashes and remote verification are reported in the chat; identify this task's preservation commit with `git log -- docs/animation_work_status/partner_mambo.md`.


Integration verification: the first rebase used `origin/main` at `18e528c73` and
preserved both sides of concurrent filename additions in the animation
`.gitattributes`. The shared scene, both anatomical sources, and the linked prop
match their pre-rebase binary SHA-256 values; their apparent Git changes are
storage conversion. The preserved mambo source hashes also match. The repository's
new `python scripts/lfs_policy.py check` passes with these task files staged.

Post-rebase verification also passed: fast suite **10/10** (5.96 seconds), focused runner **14/14** (11.49 seconds). The integrated verification logs are preserved beside the earlier stop-state logs.
