# Monkey solo animations — stopped work checkpoint

- Date: 2026-10-02 (Europe/Berlin).
- Chat title/task label: Monkey solo animations for man_and_woman3.blend. The UI title is unavailable in this execution context.
- Task branch: `codex/monkey-solo-animations`.
- Starting/current commit before checkpoint commit: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Environment: sanjo-solutions cloud; checkout `/workspace/sanjo-solutions`, app `apps/a-game`.
- State: **Stopped by explicit user instruction. Partial procedural animation study; production validation remains open.**
- GitHub delivery and commit communications are authored by Codex.

## Scope and stopping point

The original request was a broad solo Monkey repertoire for both characters in
`man_and_woman3.blend`, following the repository's per-animation Blender workflow,
with natural motion, contacts, body clearance, smooth transitions, reuse, full
validation, asset delivery, two-stage animation/documentation commits, rebase,
merge into main, and push. The user explicitly confirmed the classic 1960s Monkey
dance. All Blender work used verified Blender 5.2.2 LTS, build `d13f752e3b9c`.

The latest instruction prioritizes recording and preserving the present state over
further authoring, refining, generating, or rendering. This checkpoint includes
**34 separate source files with authored and baked actions, 33 provisional GLBs,
33 Godot import settings, experimental scripts, logs, and one initial preview**.
The intended repertoire is 18 clips per character, totaling 36. Woman `exit` and
`routine` sources remain outstanding; Woman `enter` has a saved source and baked
action, with its GLB outstanding. Every saved source is a partial study.

The full batch was terminated while debugging the bake. Its manifest is an older
single-clip result (`solo_monkey_woman_basic`), **not a complete inventory or current
validation certificate**. The precise read-only inventories beside this status file
record each saved source's actions, slots, roles, and ranges, and each GLB's actual
clip name, duration, and channel count. `binary_inventory.json` records exact sizes
and SHA-256 hashes for all 68 binary outputs.

## Durable files

- `scripts/create_monkey_dance.py`: experimental builder, IK choreography, sparse key writer, half-frame diagnostics, native bake, per-file writer, and compact GLB publisher. The final rotation-mode preservation change is present, but only the Man basic source was rebuilt with it.
- `scripts/render_monkey_dance.py`: drafted contact-sheet renderer. Its complete run was never executed; contact sheets remain outstanding.
- `scripts/player_assets/test_monkey_repertoire.py`: saved-source/bake/export/seam/discovery verification. Currently fails at catalog completeness.
- `scripts/monkey_dance.md`: intended repertoire and workflow, headed with the partial-checkpoint warning.
- `animations/monkey_repertoire.json`: stale single-clip report from an earlier successful publish; preserve as evidence.
- `animations/man_and_woman/solo_monkey_*.blend`: the 34 files enumerated below. Each stores its named source action and `.baked` action and uses existing `shared_scene_data.blend`.
- `models/player/animation_updates/solo_monkey_*.glb` and adjacent `.glb.import`: the 33 provisional exports. Exact hashed filenames are in `monkey_solo_checkpoint/export_inventory.json`.
- `docs/animation_work_status/monkey_solo_checkpoint/partial_animation_updates.tres`: the interrupted batch's update-list snapshot. The live `models/player/animation_updates.tres` has its prior references restored, so these partial exports stay outside active game playback.
- `docs/animation_work_status/monkey_solo_checkpoint/initial_woman_basic_preview.png`: Blender Workbench pose preview from the early run. This preview revealed multiple body layers and serves as an initial pose study, not final surface approval.
- The checkpoint folder also contains `source_inventory.json`, `export_inventory.json`, `binary_inventory.json`, `inventory.log`, `final_verification.log`, `monkey_full.log`, `monkey_fixed.log`, `monkey_bake_test.log`, `monkey_bake_diagnosis.log`, `monkey_modes.log`, `monkey_live.log`, `monkey_inherit.log`, `monkey_render.log`, and `monkey_fast_tests.log`.
- Diagnostic studies `check_monkey_bake.py`, `diagnose_monkey_bake.py`, `monkey_live.py`, and `monkey_inherit.py` preserve the exact bake investigation with portable checkpoint-relative imports.
- Root `.gitattributes`: upstream’s generated size-based policy remains authoritative. The initial task-specific exceptions became redundant during rebase and were dropped while retaining every binary as a full Git blob.

The combined `man_and_woman3.blend`, shared scene, anatomical studies, existing
disco source, and existing model GLBs retain their committed contents. The combined
library's ordinary add-on discovery will make the new partial sources selectable;
this checkpoint does not claim that combined discovery has passed its final test.

## Saved source and export inventory

All ranges start at frame 0, at 24 fps. Dance phrases use 0–96, position holds
0–48, entry/exit 0–24, and the Man routine 0–480. PLAYER means Man; PARTNER means
Woman. Loops include the closing endpoint; entry/exit are intended one-shot clips.
Each listed source contains one authored action and one baked action. File paths
are `animations/man_and_woman/<name>.blend`; export paths are fully enumerated in
the adjacent export inventory.

| Source name | Role | Frames | Saved source | GLB state |
| --- | --- | --- | --- | --- |
| `solo_monkey_man_basic` | PLAYER | 0–96 | 2 actions; 810400 bytes | provisional; 359676 bytes |
| `solo_monkey_man_double_pump` | PLAYER | 0–96 | 2 actions; 785316 bytes | provisional; 355208 bytes |
| `solo_monkey_man_enter` | PLAYER | 0–24 | 2 actions; 284022 bytes | provisional; 263780 bytes |
| `solo_monkey_man_exit` | PLAYER | 0–24 | 2 actions; 285271 bytes | provisional; 263780 bytes |
| `solo_monkey_man_forward_back` | PLAYER | 0–96 | 2 actions; 822513 bytes | provisional; 361484 bytes |
| `solo_monkey_man_high_reach` | PLAYER | 0–96 | 2 actions; 815112 bytes | provisional; 359816 bytes |
| `solo_monkey_man_low_bounce` | PLAYER | 0–96 | 2 actions; 817475 bytes | provisional; 355728 bytes |
| `solo_monkey_man_position_high` | PLAYER | 0–48 | 2 actions; 280047 bytes | provisional; 243544 bytes |
| `solo_monkey_man_position_left_up` | PLAYER | 0–48 | 2 actions; 280653 bytes | provisional; 243684 bytes |
| `solo_monkey_man_position_low` | PLAYER | 0–48 | 2 actions; 277477 bytes | provisional; 243272 bytes |
| `solo_monkey_man_position_ready` | PLAYER | 0–48 | 2 actions; 282055 bytes | provisional; 243680 bytes |
| `solo_monkey_man_position_right_up` | PLAYER | 0–48 | 2 actions; 277321 bytes | provisional; 243548 bytes |
| `solo_monkey_man_routine` | PLAYER | 0–480 | 2 actions; 3121415 bytes | provisional; 899008 bytes |
| `solo_monkey_man_shoulder_shimmy` | PLAYER | 0–96 | 2 actions; 813234 bytes | provisional; 363256 bytes |
| `solo_monkey_man_side_step` | PLAYER | 0–96 | 2 actions; 823336 bytes | provisional; 361480 bytes |
| `solo_monkey_man_side_swing` | PLAYER | 0–96 | 2 actions; 815618 bytes | provisional; 359816 bytes |
| `solo_monkey_man_stomp` | PLAYER | 0–96 | 2 actions; 821891 bytes | provisional; 361476 bytes |
| `solo_monkey_man_torso_twist` | PLAYER | 0–96 | 2 actions; 815479 bytes | provisional; 364400 bytes |
| `solo_monkey_woman_basic` | PARTNER | 0–96 | 2 actions; 811841 bytes | provisional; 354760 bytes |
| `solo_monkey_woman_double_pump` | PARTNER | 0–96 | 2 actions; 788154 bytes | provisional; 353604 bytes |
| `solo_monkey_woman_enter` | PARTNER | 0–24 | 2 actions; 287490 bytes | outstanding |
| `solo_monkey_woman_forward_back` | PARTNER | 0–96 | 2 actions; 818815 bytes | provisional; 358644 bytes |
| `solo_monkey_woman_high_reach` | PARTNER | 0–96 | 2 actions; 815248 bytes | provisional; 355912 bytes |
| `solo_monkey_woman_low_bounce` | PARTNER | 0–96 | 2 actions; 817939 bytes | provisional; 360192 bytes |
| `solo_monkey_woman_position_high` | PARTNER | 0–48 | 2 actions; 278965 bytes | provisional; 247904 bytes |
| `solo_monkey_woman_position_left_up` | PARTNER | 0–48 | 2 actions; 280730 bytes | provisional; 247908 bytes |
| `solo_monkey_woman_position_low` | PARTNER | 0–48 | 2 actions; 282731 bytes | provisional; 248040 bytes |
| `solo_monkey_woman_position_ready` | PARTNER | 0–48 | 2 actions; 282150 bytes | provisional; 247768 bytes |
| `solo_monkey_woman_position_right_up` | PARTNER | 0–48 | 2 actions; 281348 bytes | provisional; 247908 bytes |
| `solo_monkey_woman_shoulder_shimmy` | PARTNER | 0–96 | 2 actions; 815334 bytes | provisional; 375228 bytes |
| `solo_monkey_woman_side_step` | PARTNER | 0–96 | 2 actions; 815717 bytes | provisional; 358640 bytes |
| `solo_monkey_woman_side_swing` | PARTNER | 0–96 | 2 actions; 813937 bytes | provisional; 354764 bytes |
| `solo_monkey_woman_stomp` | PARTNER | 0–96 | 2 actions; 813824 bytes | provisional; 358636 bytes |
| `solo_monkey_woman_torso_twist` | PARTNER | 0–96 | 2 actions; 815070 bytes | BLOCKED: contains solo_monkey_man_basic.baked |

## Validation and concrete blockers

1. In-memory authoring diagnostics sampled every half frame, including planted feet,
   knee bend, torso clearance proxies, and loop pose/linear/angular seam errors.
   The completed samples in `monkey_full.log` passed. These runs preceded the
   discovered saved-source rotation-mode defect and do not validate reopened files.
2. The reused disco poser changed finger controls to Euler mode while the shared
   scene reloads their quaternion modes. Initial reopened Man basic bake comparisons
   differed by approximately **81.6 mm** at a finger endpoint. The builder now
   restores the shared rotation mode and converts its channels before capture.
   Only `solo_monkey_man_basic.blend` contains that attempted correction.
3. The corrected Man basic source still fails the saved-bake comparison:
   **7.872 mm** at frame 0 and about **8.543 mm** at frame 6 around the toes.
   The allowed positional tolerance is 3 mm. Temporary live copy-transform
   constraints align the same endpoints within about 1.6 micrometers; the persistent
   visual bake does not. The final investigation observed connected foot/toe bones,
   nonuniform evaluated segment scale, and FULL scale inheritance on both rigs.
   The cause and fix remain open. The Man basic GLB predates its corrected source.
4. A shared temporary export path collided while an earlier batch continued after
   SIGINT. SIGTERM terminated that owned process. The final script uses a per-action
   temporary filename, but the full build with that change was never run.
   `solo_monkey_woman_torso_twist_baked_c5f92b0ff091.glb` actually contains
   **`solo_monkey_man_basic.baked`**, as recorded in the export inventory.
5. Game Rig Tools is absent from this environment. The builder used Blender 5.2's
   native visual bake plus the existing file writer, compact clip scene, export
   options, and update publisher. That fallback remains blocked by item 3.
6. The final required fast suite passed **9/9**. Initially its activity JSON test
   encountered three hair LFS pointers; fetching those assets resolved the setup
   failure. The final scoped run passed 9 fast checks and failed the repertoire
   test: **9/10**, with failure at the expected 36-item catalog assertion.
7. A read-only Blender inventory successfully loaded **34** source files and
   recorded all authored/baked slots, roles, and frame ranges. Plain Python parsed
   all **33** GLBs and detected the mismatched export in item 4. Godot import/playback,
   full saved-source comparison, final surface review, and transition seam validation
   remain outstanding. Python syntax compilation passed for the three new scripts.

Final verification command (run from `apps/a-game`):

```sh
BLENDER=/workspace/.local/blender52/blender GODOT=/workspace/.cloud-onboarding/bin/godot \
  python tests/run_tests.py --changed scripts/player_assets/test_monkey_repertoire.py
```

This includes the mandatory fast set. The earlier explicit
`python tests/run_tests.py --suite fast` also passed 9/9 after the asset fetch.

## Process state and storage

At the stop checkpoint, `ps -o pid,etime,args -C blender` reported zero Blender
processes. The original batch PID 1494 had already been terminated with SIGTERM;
the subsequent read-only inventory and verification completed. All useful outputs
from `/tmp/monkey-*` were copied into this checkpoint. Download archives, unpacked
Blender, credentials/helper scripts, and fetched pre-existing LFS objects remain
environment setup, outside the commit. Temporary export leftovers retain no unique
animation state beyond the preserved source and GLB files.

All 68 preserved binary outputs are at or below **104,857,600 bytes** and use regular
Git. Their exact sizes and hashes are in `binary_inventory.json`. Before rebase,
file-specific exceptions cleared the older inherited LFS filters. The fetched main
had already migrated to a generated size-based policy, so rebase preserved its
attributes unchanged. `python scripts/lfs_policy.py check` passed for 23,482 staged
files, and the checkpoint binaries retained their full contents and hashes. New LFS asset
uploads are therefore unnecessary; an ordinary Git push carries these binaries.

## Resume only after renewed animation authorization

Read this status and its failed-check logs first. Diagnose the saved visual bake
before rebuilding. These exact commands assume the current cloud checkout;
substitute a verified Blender 5.2 path when resuming elsewhere.

```sh
cd /workspace/sanjo-solutions/apps/a-game
/workspace/.local/blender52/blender -t 4 --background \
  animations/man_and_woman/solo_monkey_man_basic.blend --python-exit-code 1 \
  --python docs/animation_work_status/monkey_solo_checkpoint/diagnose_monkey_bake.py
/workspace/.local/blender52/blender -t 4 --background \
  animations/man_and_woman/solo_monkey_man_basic.blend --python-exit-code 1 \
  --python docs/animation_work_status/monkey_solo_checkpoint/monkey_inherit.py
```

After correcting the saved-source and bake problems, rebuild a single clip and
require its reopened comparison to pass before the complete batch:

```sh
/workspace/.local/blender52/blender -t 4 --background \
  animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 \
  --python scripts/create_monkey_dance.py -- --moves basic --characters Man
/workspace/.local/blender52/blender -t 4 --background \
  animations/man_and_woman/solo_monkey_man_basic.blend --python-exit-code 1 \
  --python docs/animation_work_status/monkey_solo_checkpoint/check_monkey_bake.py
/workspace/.local/blender52/blender -t 4 --background \
  animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 \
  --python scripts/create_monkey_dance.py
BLENDER=/workspace/.local/blender52/blender GODOT=/workspace/.cloud-onboarding/bin/godot \
  python tests/run_tests.py --changed scripts/player_assets/test_monkey_repertoire.py
/workspace/.local/blender52/blender -t 4 --background --factory-startup \
  --python-exit-code 1 --python scripts/render_monkey_dance.py
```

Then inspect rendered geometry and playback, run Godot import/target checks, verify
all 36 sources/exports and the catalog, inspect actual binary sizes/attributes,
and publish only validated update references. The renderer currently follows the
manifest, so running it against this checkpoint's stale one-item manifest would
produce an incomplete review. Preserve concurrent animation files and settings
when integrating subsequent work.

## Integration checkpoint

The animation checkpoint rebased onto `origin/main` at
`18e528c73` as commit `d482f1a5579c06221ebc88c6afcb44d9bee20211`.
The attributes conflict was resolved by retaining upstream's generated storage
policy. Concurrent animation sources, tooling, and documentation remain preserved.

The fetched main now supplies bundled Game Rig Tools setup and the connected-joint
bake regression in `scripts/player_assets/bachata_motion.py` and
`test_bachata_motion.py`. These arrived after animation work stopped. On an authorized
resume, read the current `AGENTS.md` and `scripts/blender/README.md`, install the
bundled tools with the documented profile, and assess that existing bake approach
before further development of this checkpoint's native-bake fallback.

A separate documentation commit adds an Animation-section rule about unique worker
export paths, completed process termination, and checking embedded GLB identity.
The final chat delivery reports the documentation and merge hashes and the verified
remote-main push, since a commit cannot record its own hash in its contents.

Post-rebase verification: the current fast suite passed **10/10** in 6.18 seconds;
its output is `monkey_solo_checkpoint/post_rebase_fast.log`. The earlier scoped
repertoire failure remains recorded and unresolved. This documentation-only pass
performed zero animation generation or rendering.
