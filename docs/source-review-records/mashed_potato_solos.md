# Mashed Potato solo animations — paused work status

Recorded October 2, 2026 (Europe/Berlin), following the explicit instruction to
stop all animation authoring and preserve the current state.

- Chat/task: **Mashed Potato solo animations for man_and_woman3.blend** (descriptive task title; the UI title was unavailable).
- Project: A-Game, `apps/a-game`, sanjo-solutions cloud environment.
- Task branch: `codex/mashed-potato-solos`.
- Current commit at the stop instruction: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Original scope: a broad Mashed Potato repertoire and positions for both solo characters; Blender 5.2 throughout; individual animation files; natural motion, contacts, clearance, interpolation and loop validation; commit/rebase, animation guidance, integration and push.
- Current outcome: **partial animation studies, with baked/exported assets saved and runtime acceptance blocked**. The complete repertoire remains outstanding.

## Saved work

**20 individual sources, 20 baked actions, and 20 individual GLB exports** exist.
There are **17 Man clips** (`PLAYER`) and **3 Woman clips** (`PARTNER`). Each source
contains one authoring action and its matching `.baked` action. Each action has a
single character slot. All were authored, scripted, baked, and exported with
**Blender 5.2.2 LTS**, build `d13f752e3b9c`.

The exact file paths, actual byte counts, SHA-256 hashes, roles, ranges, recipe
versions, and draft state are recorded in
[`mashed_potato_solos/asset_inventory.json`](mashed_potato_solos/asset_inventory.json).
That inventory is authoritative for the saved subset; the choreography's planned
52-clip list is broader than the completed files.

| Character | Saved suffixes | Frames | Intended playback |
| --- | --- | --- | --- |
| Man | `position_ready`, `position_heels_in`, `position_heels_out`, `position_weight_left`, `position_weight_right`, `position_low` | 0–24 | Static loop/hold |
| Man | `basic`, `double_time`, `low_bounce`, `narrow`, `wide`, `arm_swing`, `arm_pumps`, `arm_roll`, `forward_back`, `side_left` | 0–96 | Loop |
| Man | `quarter_turn_left` | 0–96 | Once, 90° left step turn |
| Woman | `basic`, `side_left` | 0–96 | Loop |
| Woman | `quarter_turn_left` | 0–96 | Once, 90° left step turn |

Timing is 24 fps at 120 beats/minute. Frame 0 is the opening pose and the terminal
frame is the interpolation endpoint. Sources are
`animations/man_and_woman/mashed_potato_<man|woman>_<suffix>.blend`.
Exports are `models/player/animation_updates/mashed_potato_<man|woman>_<suffix>_baked_<hash>.glb`,
with adjacent `.glb.import` settings. `models/player/animation_updates.tres`
contains their references, retaining the previously existing references. These
are draft libraries, with the fidelity limitations below; activity integration
and final playback approval remain outstanding.

### Authoring and supporting files

- `scripts/mashed_potato/choreography.py`: planned 26-move vocabulary per character, body/foot trajectories, positions, turn headings, and phrase envelopes. Many planned clips have yet to be generated.
- `scripts/mashed_potato/author.py`: character calibration, sparse control keys, native visual bake, per-animation writer, GLB publishing, and incremental manifest. It reuses existing disco and yoga posing/wrist/proportion helpers. **Procedural study: its bake path has an unresolved fidelity failure.**
- `scripts/mashed_potato/review.py`: half-frame target, joint-angle, clearance-proxy, and loop checks. These establish authoring motion, separately from saved bake fidelity.
- `scripts/mashed_potato/manifest.json`: recipe version 2 results for the six corrected clips (`basic`, `side_left`, `quarter_turn_left` for both characters). It intentionally reflects the latest recipe run, rather than the full 20-file inventory.
- `scripts/mashed_potato/verify_saved.py`: reopened-source/baked comparison and base skin checks. **Currently fails the fidelity assertion**. A completed `saved_validation.json` remains outstanding.
- `scripts/mashed_potato/verify_runtime.py` and `verify_runtime.gd`: isolated Godot import, shipped-model track resolution, duration, and loop checks.
- `scripts/mashed_potato/render_review.py`: Blender Workbench motion-sheet procedure; further rendering stopped at the user's instruction.
- `scripts/mashed_potato/README.md`: intended vocabulary, current partial state, workflow and resumption procedures.
- `docs/animation_work_status/mashed_potato_solos/`: preserved run logs, inspection scripts, inventory, storage-attribute audit, and the rendered Man basic motion sheet.
- `.gitattributes`: current main's generated 100 MiB policy is preserved; task binaries remain ordinary Git blobs.

The six recipe-2 clips preserve the shared rig's bone rotation modes. The other
14 sources retain recipe-1 Euler finger channels even though the shared rig uses
quaternion finger controls. Their reopened authoring finger poses therefore
require correction during future work. All 20 bakes/exports are provisional.
The combined library, shared scene, and anatomical source models retain their
existing binary contents. Source-file discovery exposes the new clips on reopen.

## Validation evidence and blockers

1. **Authoring interpolation:** each published source passed its then-current
   half-frame checks. Initial 3-frame keys produced approximately 3.3 mm ball
   errors; 1.5-frame keys reduced Man/Woman basic errors below 0.8 mm. Extra
   0.75-frame samples corrected double-time/lateral/turn arc failures. Recipe-2
   measurements for all six latest clips are in `manifest.json`. Loop endpoint
   poses match for the checked loops. These checks use rig landmarks and local
   clearance proxies.
2. **Rotation-mode persistence:** the first reopened Man basic comparison found
   a **55.80 mm finger joint mismatch**. Finger Euler channels were ignored by
   the shared rig's quaternion mode after reopening. Recipe 2 converts captured
   rotations back to the shared rig's existing modes. This correction was
   applied to the six listed recipe-2 clips.
3. **Remaining bake fidelity blocker:** the corrected Man basic still shows a
   **9.084 mm maximum joint difference**, worst at `DEF-toe.L`, frame 51.
   The native visual bake is therefore **unaccepted**. Inspection shows
   nonuniform source deform matrices and `STRETCH_TO` constraints with volume
   preservation; decomposition/inheritance is an investigation lead, rather
   than an established complete diagnosis. The cloud image has Blender 5.2.2
   and repository export helpers, while Game Rig Tools is unavailable.
4. **Sampled skin checks:** corrected Man basic, 18 sampled frames, reports
   **zero arm–torso triangle intersections** and minimum base foot-skin height
   **−3.175 mm** relative to Z=0. Ground placement needs further review; this
   measurement is a limitation, rather than final planted-contact acceptance.
   The checker evaluates the base body with its armature modifier and omits
   topology-changing display modifiers to keep vertex-region correspondence.
5. **Visual review:** the preserved
   `mashed_potato_solos/mashed_potato_man_basic.png` shows frames
   0, 27, 30, 33, 36, 42, 48, rendered in Blender 5.2.2. It is an earlier recipe-1
   preview, with the corresponding finger-mode limitation. Hand/body spacing
   and the alternating footwork were inspected. Full repertoire playback and
   final rendered approval remain outstanding.
6. **Fast suite:** `python tests/run_tests.py --suite fast` passed **9/9** after
   fetching the existing hair mesh LFS assets. The first attempt was 8/9 due to
   three unhydrated hair resources. A final fast rerun is recorded below.
7. **Broad related suite:** `python tests/run_tests.py` selected 186 slow checks.
   It encountered unrelated Godot/LFS resource-loading errors and stalled in
   the editor import for `addons/toy_grip/test_finger_pose_gizmo.gd`. The owned
   runner and child process were terminated. This suite is **incomplete**, not
   passing. Its generated changes to 59 existing `.import` files were restored
   to the initially clean checkout state. The evidence log is preserved.
8. **Runtime import:** an earlier isolated run passed 12 Man libraries,
   **8,580 tracks**, shipped-model node/bone resolution, durations and repeat
   modes. A final run against the six recipe-2 manifest entries is recorded
   below. This checks import/layout, rather than visual bake fidelity.

All verification, including failed checks, is preserved under the evidence
directory. `mashed_bake_inspect.txt`, `mashed_rig_inspect.txt`, and
`mashed_modes.txt` contain the measured matrices, rig constraint properties, and
rotation-channel evidence. Their adjacent snake_case Python scripts preserve
the exact inspection procedures.

## Processes, storage, and delivery

At the stop instruction, the corrected authoring run had already exited normally
at **14:55:00 UTC** after exporting Woman's quarter-turn-left clip. A process
inspection found **zero owned Blender, authoring, rendering, or test-runner
processes still active**. Subsequent activity is limited to recording, verification,
committing, and integration. Further authoring and rendering remain paused.

The final saved subset contains **41 binary files** (20 sources, 20 GLBs, one
preview), **16,380,619 bytes** total; the largest is **1,160,226 bytes**. Every
binary is below **104,857,600 bytes** and is stored directly in Git. The first checkpoint used exact-path exceptions; rebasing preserved main's newer generated size policy, under which these files use regular Git by default. `storage_attributes.txt` records the original pre-rebase audit; `integration_attributes.txt` records the final policy.
This task introduces **zero new LFS uploads**. Existing prerequisite LFS assets
were downloaded for inspection and verification and retain their tracked contents.
Temporary `.cache/mashed_potato/clip.glb` duplicates the last published clip;
the durable named export is included in the inventory.

## Remaining work and exact resume commands

Resume authoring only after a new user instruction. Start by investigating the
saved bake fidelity failure. Preserve the partial binaries as checkpoints and
use a new recipe version when a corrected authoring/export method is ready.
`author.py -- resume` currently skips recipe-2 manifest entries even though their
bakes need correction, so explicitly rebuild them or advance the recipe version.

From `apps/a-game`:

```sh
# Read-only reproduction of the known blocker (expected assertion failure).
blender -b -t 2 --python scripts/mashed_potato/verify_saved.py -- basic

# Inspect the affected saved matrices and rig constraints.
blender -b -t 2 animations/man_and_woman/mashed_potato_man_basic.blend \
  --python scripts/player_assets/animation_file_startup.py \
  --python docs/animation_work_status/mashed_potato_solos/mashed_bake_inspect.py
blender -b -t 2 animations/man_and_woman/mashed_potato_man_basic.blend \
  --python scripts/player_assets/animation_file_startup.py \
  --python docs/animation_work_status/mashed_potato_solos/mashed_rig_inspect.py

# Existing verification; the runtime command reads the six-entry latest manifest.
python tests/run_tests.py --suite fast
python scripts/mashed_potato/verify_runtime.py

# Future authoring only after approval and resolution of the documented blocker.
blender -b -t 4 animations/man_and_woman/solo_disco_dance.blend \
  --python scripts/player_assets/animation_file_startup.py \
  --python scripts/mashed_potato/author.py -- basic side_left quarter_turn_left
blender -b -t 4 animations/man_and_woman/solo_disco_dance.blend \
  --python scripts/player_assets/animation_file_startup.py \
  --python scripts/mashed_potato/author.py -- resume
```

Outstanding repertoire: the Man's right side/back steps/kicks/right turn,
entry/exit/routine; the Woman's remaining 23 planned clips; complete regenerated
bakes, foot-skin placement, smooth stance/heading transitions, full surface and
playback review, complete saved validation, and full runtime verification.
Runtime loop settings for older draft exports also require a final full-inventory
check; the corrected writer uses Godot's normalized `_baked` animation name.

## Final delivery verification

- Final fast rerun: **8/9 passed**. The activity JSON check encountered existing
  hair GLB import failures (`bob01`, `bob02`, `short01`–`short04`, `afro01`) after
  the broad editor scan. The earlier hydrated run passed 9/9. This is an
  environment/import blocker, recorded in `mashed_potato_solos/final_fast.txt`.
- Final focused runtime check: **6/6 recipe-2 libraries passed**, **4,035 tracks**
  resolve on the shipped Man/Woman models; duration and loop settings match.
  See `mashed_potato_solos/final_runtime.txt`.
- Saved-bake fidelity remains a known failed check; further animation work was
  stopped rather than continued after the user's instruction.
- `git diff --check` passed before staging. Binary hashes and direct-Git attributes
  were inspected before staging. No task asset requires a new LFS upload.

GitHub commits and the integration commit are authored by Codex and each carry
exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer. The delivery
response supplies the final task/integration hashes and remote verification.

## Integration discoveries

The task checkpoint was rebased onto `18e528c73` from current `origin/main`.
The sole conflict was `.gitattributes`: main had migrated to the generated
100 MiB policy. That policy was preserved, and all task binaries remain raw Git
objects. Concurrent animation libraries and documentation were retained.

Main now bundles Game Rig Tools (`scripts/blender/install_animation_tools.py`),
which was unavailable in the authoring checkout at the stop point. Main also
contains `scripts/player_assets/bachata_motion.py` and its connected-joint
regression fixture for longitudinal-axis-preserving bake decomposition. These
are useful resume leads; this stopped task performed zero further authoring
or bake refinements after fetching them. Future authorized work should follow
`scripts/blender/README.md`, enable the bundled tools in the same isolated
profile, and investigate the saved fidelity failure before regenerating clips.

Added two Animation guidance bullets covering calibrated heel-swivel pivots and
complete paused-delivery inventories. The original task checkpoint is
`cd224ec7f`; the documentation and merge hashes are reported in the delivery
response.

Post-rebase verification: the updated fast catalog passed **9/10** checks in
5.57 seconds; the activity JSON check remains blocked by existing hair import
errors. See `mashed_potato_solos/post_rebase_fast.txt`. The generated Git/LFS
policy check passed for all **23,447** staged repository files.
