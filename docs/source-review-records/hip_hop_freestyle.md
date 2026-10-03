# Hip-hop freestyle solo animation work status

Date: 2026-10-02 (Europe/Berlin). Chat/task title: Hip-hop freestyle solos for `man_and_woman3.blend`.

## Stop checkpoint

The user directed running animation chats to stop animation work and preserve their present state. Authoring, refinement, generation, and rendering stopped immediately upon that instruction. This checkpoint contains procedural blocking studies with authored IK actions, matching baked actions, and Godot exports. **The repertoire remains a partial deliverable awaiting quality review.** The asset count describes saved artifacts rather than final animation approval.

- Environment: sanjo-solutions cloud environment; checkout `/workspace/sanjo-solutions`; project `apps/a-game`.
- Task branch: `codex/hip-hop-freestyle`.
- Current commit at the stop checkpoint: `fe09ef7b6a54f03909f7335d9673a27c15007d69` (pre-task base).
- Blender used for every authoring, sampling, baking, export, and render operation: **5.2.2 LTS**, build `d13f752e3b9c`.
- All owned Blender, render, import, and verification processes exited or were terminated. The stopped broad Godot test left PID 2237 as an exited zombie owned by PID 1; it performs zero work.
- The full generation completed before the stop instruction. The latest saved-bake verification had already failed before that instruction. Further refinement awaits a new user instruction.

## Original scope and preserved implementation

Create a broad hip-hop freestyle repertoire for both adult character rigs associated with `man_and_woman3.blend`, using solo roles, natural motion, planted contacts, clearance, smooth transitions, and loop validation. Reuse suitable existing motion. Follow the existing per-animation file workflow, store binaries of at most 104,857,600 bytes directly in Git, commit/rebase, document findings under `# Animation` in `AGENTS.md`, then merge and push main.

The preserved implementation creates **38 items per character, 76 source files and 76 GLB exports**:

- 24 movement loops per character: down bounce, up groove, side rock, forward rock, step touch, two step, box step, V step, running man, Roger Rabbit, Reebok, happy feet, heel-toe, skate, kick step, cabbage patch, Smurf, party machine, Bart Simpson, shoulder bounce, chest pop, body roll, arm wave, and arm roll.
- Eight held positions per character: neutral, wide, low, lean left, lean right, stagger left, stagger right, and open hit.
- Four transitions per character: neutral to low, low to neutral, neutral to wide, wide to neutral.
- Two 16-beat compositions per character: foundation flow and isolation flow.

Freestyle is open-ended. These named procedural studies provide a starting vocabulary; their style fidelity and final natural-motion quality still need review. Several neighboring step variants share a movement family. Breaking power moves and floorwork were outside the generated set.

Each `.blend` contains one editable action and its matching `.baked` action, with one character slot in each. Man uses `PLAYER`; Woman uses `PARTNER`. Both source and baked actions store the explicit solo role. Sources reference the existing `animations/man_and_woman/shared_scene_data.blend`; the combined library discovers them through its existing loader. This task changes zero shared source scenes or anatomy models. Rebase preserves any concurrent main versions; the recorded motion evidence belongs to the pre-task base named above.

Timing: 24 fps, 96 BPM, 15 frames per beat. Movement loops cover frames **0–60** (2.5 seconds), held positions **0–15** (0.625 seconds), transitions **0–30** (1.25 seconds), and compositions **0–240** (10 seconds). Loop clips include a repeated endpoint pose. Transitions have Godot loop mode zero; other clips use linear looping. Static channels use one initial key; moving authoring controls use quarter-beat poses with Bezier interpolation. Baked channels use integer-frame sampling and linear interpolation.

Existing `DiscoCharacter`, `DiscoWristPoser`, and `RigYogaPoser` are reused. Arm rolls reuse `DiscoChoreography.retrieve_arms`. The native per-animation writer, compact export scene, participant filtering, and animation-update publisher are reused. The compact export verifies existing rest-skeleton signatures before publishing. Every export contains only its intended character's animation channels.

The man's connected deform leg chain differs from the IK control chain. The generator iteratively adjusts foot IK targets against the mesh-driving deform ankle endpoints. This calibration belongs to the new actions; the shared rig is preserved. An initial extra full-transform constraint bridge introduced shear. The saved build uses the existing deform constraints directly.

## Files and asset states

The complete machine-readable inventory is [hip_hop_freestyle_inventory.json](hip_hop_freestyle_inventory.json). It names **every source, export, import sidecar, and retained render**, with actual byte size and SHA-256. Per-clip authoring measurements, category, description, roles, timing, and paths are in [`../../scripts/hip_hop/validation.json`](../../scripts/hip_hop/validation.json).

| File | Preserved purpose/state |
| --- | --- |
| `scripts/hip_hop/choreography.py` | Procedural 38-item vocabulary and phase/contact definitions. |
| `scripts/hip_hop/build.py` | Blender 5.2 generator, deform-foot solve, sparse action writer, bake, exporter, and publisher. |
| `scripts/hip_hop/review.py` | Half-frame evaluated contact, reach, wrist, proxy clearance, and loop diagnostics. |
| `scripts/hip_hop/preview.py` | Blender Cycles CPU geometry-sheet renderer; two completed renders retained. |
| `scripts/hip_hop/validate_saved.py` | Saved-bake comparison; currently fails as recorded below. |
| `scripts/hip_hop/validate_import.gd` | Native Godot library role, track, duration, and loop verification. |
| `scripts/hip_hop/validation.json` | Completed build measurements for all 76 clips. |
| `models/player/animation_updates.tres` | Adds all 76 libraries while retaining existing references. Concurrent integration must preserve the union of references. |
| Repository `.gitattributes` | Current main's generated size-based policy is retained. Historical exact-file audits are preserved in evidence. |
| `docs/animation_work_status/hip_hop_freestyle_evidence/` | Render sheets, build/reopen/validation logs, fast results, and before/after storage attributes. |

All 76 source files have authored and baked actions; all 76 GLBs are exported and imported successfully by the isolated Godot test. **Saved-bake subframe approval is partial**. These artifacts need further review.

## Verification and limitations

1. `blender -b --factory-startup animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/hip_hop/build.py`: all 76 generated clips passed the builder's **8,716 half-frame authoring samples**. Maximum measured planted ankle error: **0.0013322316 m**. Maximum integer-frame bake discrepancy: **0.0000054806 m**. Loop endpoint and finite-difference velocity checks passed. Clearance uses limb/torso proxies; complete mesh collision coverage remains pending.
2. Source reopen through `scripts/player_assets/animation_file_startup.py`: the Man down-bounce source composed a runtime authoring scene and exposed exactly its source/baked action pair, each with one slot. See `source_reopen.log`.
3. `blender ... --python scripts/hip_hop/validate_saved.py`: stopped on **`hip_hop_man_kick_step`**, with **0.002447941453115392 m** maximum subframe deviation against a **0.002 m** threshold. Earlier clips passed as listed below. Subsequent clips remain unchecked by this stricter comparison. The script writes JSON after full success, so `saved_validation.json` does not exist; `saved_validation.log` preserves partial results.
4. Isolated native Godot **4.7.2** editor import and `validate_import.gd`: **PASS, 76 solo libraries, 47,994 tracks**, exact clip lengths and loop modes. See `godot_validation.log`. The fixture lives under `.cache/hip_hop/godot_validation` and is reproducible below.
5. Blender 5.2 Cycles CPU rendered `down_bounce_preview.png` and `foundation_flow_preview.png`; both were visually inspected. The eight uniformly spaced composition samples land on some neutral phrase beats and give limited coverage of lifted-foot extremes. Complete playback and mesh clearance for every move still need visual review.
6. Required `python tests/run_tests.py --suite fast`: **9/9 PASS before the stop instruction**, retained in `fast_tests_before_stop.log`. The post-stop rerun was **8/9** (`fast_tests.log`): the activity JSON check encountered missing existing hair-model GLB imports after the broad editor run. Earlier missing hair `.res` assets had been hydrated. A separate post-rebase fast result is recorded below.
7. `BLENDER=/home/agent/.local/bin/blender python tests/run_tests.py`: broader dependency selection reached unrelated existing libraries with LFS-pointer resources, including `animations/player/crouch.res` and existing `playground/animations/*.res`. The first slow grip-preset test printed passes but failed the runner's error scan. The following Godot editor test `addons/toy_grip/test_finger_pose_gizmo.gd` stalled; its owned process and the broad runner were terminated. **The broad slow suite remains incomplete.** Game Rig Tools was absent from factory Blender preferences at the original checkpoint, affecting bakery-dependent fixtures. Concurrent main now supplies `scripts/blender/install_animation_tools.py`; consult its setup guide when resuming. Unrelated importer side effects from that run were restored to their initially clean tracked contents; task import settings retain explicit loop metadata.

## Storage and delivery

Every task binary was inspected by actual file size before staging. The **154 binaries total 62,416,296 bytes**; the largest is **2,218,892 bytes**. Every new `.blend`, `.glb`, and retained PNG is at or below 104,857,600 bytes and uses ordinary Git. Before rebasing, exact-file exceptions set `-filter -diff -merge -text`; those historical audits remain in evidence. Concurrent main introduced a generated size-based policy through `scripts/lfs_policy.py`. Integration retained that current policy instead of adding redundant exceptions. `storage_after_rebase.txt` confirms ordinary Git attributes for all task binaries, and the repository-wide staged policy check passed for 25,039 files. This task creates zero new LFS objects. Hydrated existing LFS files retain their storage configuration and are outside the changed-file set.

Durable evidence preserves the build, source reopen, partial saved validation, Godot validation, fast-test logs, and both completed render sheets. Local `.cache/hip_hop/godot_validation` is a reproducible verification fixture. No owned animation process remains active.

Delivery commits these artifacts and this record first, then fetches current `origin/main` and rebases. Scoped `# Animation` guidance is committed separately. Integration fetches again immediately before merging and pushing main, retaining concurrent exact-file attributes, documentation, and library references. Ordinary push rejection is resolved by incorporating the newer remote main. Task and integration commit hashes and remote verification are reported in chat; a commit cannot embed its own hash.

## Remaining work and blockers

- Resume authoring, refinement, or rendering only after a new user instruction.
- Investigate Man kick-step's 2.45 mm saved-bake subframe discrepancy against the 2 mm threshold, then finish the saved-bake sweep. Preserve the threshold until the discrepancy is understood.
- Review every move's full motion and silhouette from front/side perspectives, including lifted-foot extremes, body clearance, support and weight shifts, wrists, fingers, dance identity, and transitions. Current clearance checks are proxy studies.
- Audit finger rotation-mode parity: the reused Disco poser sets finger controls to Euler mode in its authoring session, while current shared Rigify guidance records quaternion defaults. The present saved-bake validator covers nine landmarks and omits finger bones. Preserve this potential mismatch as a known quality gap.
- Review source/deform NLA grouping: the current builder uses distinct authoring and `.baked` track labels; current repository guidance prefers a shared clip label.
- Run a complete saved-source reopen/selection sweep. One source was tested through the full startup helper; the stricter validator appends actions directly.
- Hydrate the broad suite's existing LFS prerequisites, use the intended Godot/add-on setup, and rerun related checks. The isolated import pass establishes library structure rather than complete gameplay integration.
- Static positions are held pose assets. Related step variants may need more differentiated choreography. The set makes no claim to exhaust every freestyle move.

## Exact resume commands

Run from the app checkout. Read this status and fetch main before resuming concurrent work. Authoring and rendering commands require a fresh user instruction.

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender --version
python tests/run_tests.py --suite fast

# Verification only; currently reproduces the kick-step failure.
blender -b --factory-startup animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/hip_hop/validate_saved.py

# Verification of the native source startup helper.
blender -b --factory-startup animations/man_and_woman/hip_hop_man_down_bounce.blend --python-exit-code 1 --python scripts/player_assets/animation_file_startup.py

# After fresh authorization: rebuild only kick_step for both roles.
blender -b --factory-startup animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/hip_hop/build.py -- kick_step

# After fresh authorization: render samples from that source.
blender -b --factory-startup animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/hip_hop/preview.py -- kick_step
```

Recreate the isolated Godot verification fixture:

```bash
cd /workspace/sanjo-solutions/apps/a-game
python - <<'PYCODE'
from pathlib import Path
import shutil
root = Path('.cache/hip_hop/godot_validation')
(root / 'scripts/player_assets').mkdir(parents=True, exist_ok=True)
(root / 'models/player/animation_updates').mkdir(parents=True, exist_ok=True)
(root / 'project.godot').write_text('config_version=5\n[application]\nconfig/name="Hip-hop asset validation"\n[rendering]\nrenderer/rendering_method="gl_compatibility"\n')
shutil.copyfile('scripts/player_assets/import_player_animations.gd', root / 'scripts/player_assets/import_player_animations.gd')
shutil.copyfile('scripts/hip_hop/validation.json', root / 'catalog.json')
shutil.copyfile('scripts/hip_hop/validate_import.gd', root / 'validate_import.gd')
for source in Path('models/player/animation_updates').glob('hip_hop_*.glb*'):
    shutil.copyfile(source, root / 'models/player/animation_updates' / source.name)
PYCODE
/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot --headless --editor --path .cache/hip_hop/godot_validation --import
/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot --headless --path .cache/hip_hop/godot_validation --script res://validate_import.gd
```

## Saved-bake checks completed before failure

- `hip_hop_man_arm_roll`: 0.0017428440899215911 m maximum sampled deviation.
- `hip_hop_man_arm_wave`: 0.0014252433658683025 m maximum sampled deviation.
- `hip_hop_man_bart_simpson`: 0.0011828227464273336 m maximum sampled deviation.
- `hip_hop_man_body_roll`: 0.0005989351672698186 m maximum sampled deviation.
- `hip_hop_man_box_step`: 0.0010802842737046004 m maximum sampled deviation.
- `hip_hop_man_cabbage_patch`: 0.000605230077846581 m maximum sampled deviation.
- `hip_hop_man_chest_pop`: 0.0005798499269277977 m maximum sampled deviation.
- `hip_hop_man_down_bounce`: 0.000582503133190666 m maximum sampled deviation.
- `hip_hop_man_forward_rock`: 0.0005791753981281233 m maximum sampled deviation.
- `hip_hop_man_foundation_flow`: 0.0017974918045569597 m maximum sampled deviation.
- `hip_hop_man_happy_feet`: 0.000582503133190666 m maximum sampled deviation.
- `hip_hop_man_heel_toe`: 0.000582503133190666 m maximum sampled deviation.
- `hip_hop_man_isolation_flow`: 0.0014252433658683025 m maximum sampled deviation.

## Exact clip inventory

Paths are relative to `apps/a-game`. Each source includes authored and baked actions; every export has its adjacent `.glb.import` sidecar. These remain procedural studies awaiting final approval.

| Role | Clip | Frames | Source | Export |
| --- | --- | --- | --- | --- |
| PLAYER | `hip_hop_man_arm_roll` | 0–60 | `animations/man_and_woman/hip_hop_man_arm_roll.blend` | `models/player/animation_updates/hip_hop_man_arm_roll_baked_eac652878885.glb` |
| PLAYER | `hip_hop_man_arm_wave` | 0–60 | `animations/man_and_woman/hip_hop_man_arm_wave.blend` | `models/player/animation_updates/hip_hop_man_arm_wave_baked_68d19492a3f7.glb` |
| PLAYER | `hip_hop_man_bart_simpson` | 0–60 | `animations/man_and_woman/hip_hop_man_bart_simpson.blend` | `models/player/animation_updates/hip_hop_man_bart_simpson_baked_2365b37e48fa.glb` |
| PLAYER | `hip_hop_man_body_roll` | 0–60 | `animations/man_and_woman/hip_hop_man_body_roll.blend` | `models/player/animation_updates/hip_hop_man_body_roll_baked_e348a0b5b97e.glb` |
| PLAYER | `hip_hop_man_box_step` | 0–60 | `animations/man_and_woman/hip_hop_man_box_step.blend` | `models/player/animation_updates/hip_hop_man_box_step_baked_9058d82abcea.glb` |
| PLAYER | `hip_hop_man_cabbage_patch` | 0–60 | `animations/man_and_woman/hip_hop_man_cabbage_patch.blend` | `models/player/animation_updates/hip_hop_man_cabbage_patch_baked_6e06920ef6fb.glb` |
| PLAYER | `hip_hop_man_chest_pop` | 0–60 | `animations/man_and_woman/hip_hop_man_chest_pop.blend` | `models/player/animation_updates/hip_hop_man_chest_pop_baked_ee10f2f40023.glb` |
| PLAYER | `hip_hop_man_down_bounce` | 0–60 | `animations/man_and_woman/hip_hop_man_down_bounce.blend` | `models/player/animation_updates/hip_hop_man_down_bounce_baked_953f38346568.glb` |
| PLAYER | `hip_hop_man_forward_rock` | 0–60 | `animations/man_and_woman/hip_hop_man_forward_rock.blend` | `models/player/animation_updates/hip_hop_man_forward_rock_baked_4b7e06ecc473.glb` |
| PLAYER | `hip_hop_man_foundation_flow` | 0–240 | `animations/man_and_woman/hip_hop_man_foundation_flow.blend` | `models/player/animation_updates/hip_hop_man_foundation_flow_baked_263170dfcc5b.glb` |
| PLAYER | `hip_hop_man_happy_feet` | 0–60 | `animations/man_and_woman/hip_hop_man_happy_feet.blend` | `models/player/animation_updates/hip_hop_man_happy_feet_baked_a7dba0904758.glb` |
| PLAYER | `hip_hop_man_heel_toe` | 0–60 | `animations/man_and_woman/hip_hop_man_heel_toe.blend` | `models/player/animation_updates/hip_hop_man_heel_toe_baked_7b3a8c546541.glb` |
| PLAYER | `hip_hop_man_isolation_flow` | 0–240 | `animations/man_and_woman/hip_hop_man_isolation_flow.blend` | `models/player/animation_updates/hip_hop_man_isolation_flow_baked_25e9febf7b5e.glb` |
| PLAYER | `hip_hop_man_kick_step` | 0–60 | `animations/man_and_woman/hip_hop_man_kick_step.blend` | `models/player/animation_updates/hip_hop_man_kick_step_baked_cdf3f29d827c.glb` |
| PLAYER | `hip_hop_man_low_to_neutral` | 0–30 | `animations/man_and_woman/hip_hop_man_low_to_neutral.blend` | `models/player/animation_updates/hip_hop_man_low_to_neutral_baked_64a12c1ecf30.glb` |
| PLAYER | `hip_hop_man_neutral_to_low` | 0–30 | `animations/man_and_woman/hip_hop_man_neutral_to_low.blend` | `models/player/animation_updates/hip_hop_man_neutral_to_low_baked_74aee4ac9391.glb` |
| PLAYER | `hip_hop_man_neutral_to_wide` | 0–30 | `animations/man_and_woman/hip_hop_man_neutral_to_wide.blend` | `models/player/animation_updates/hip_hop_man_neutral_to_wide_baked_f8c72ccfbdda.glb` |
| PLAYER | `hip_hop_man_party_machine` | 0–60 | `animations/man_and_woman/hip_hop_man_party_machine.blend` | `models/player/animation_updates/hip_hop_man_party_machine_baked_5514c94a1ca6.glb` |
| PLAYER | `hip_hop_man_pose_lean_left` | 0–15 | `animations/man_and_woman/hip_hop_man_pose_lean_left.blend` | `models/player/animation_updates/hip_hop_man_pose_lean_left_baked_ea6f2d0542c0.glb` |
| PLAYER | `hip_hop_man_pose_lean_right` | 0–15 | `animations/man_and_woman/hip_hop_man_pose_lean_right.blend` | `models/player/animation_updates/hip_hop_man_pose_lean_right_baked_981fcbc51d4c.glb` |
| PLAYER | `hip_hop_man_pose_low` | 0–15 | `animations/man_and_woman/hip_hop_man_pose_low.blend` | `models/player/animation_updates/hip_hop_man_pose_low_baked_4664898539d6.glb` |
| PLAYER | `hip_hop_man_pose_neutral` | 0–15 | `animations/man_and_woman/hip_hop_man_pose_neutral.blend` | `models/player/animation_updates/hip_hop_man_pose_neutral_baked_e8c5bea4267c.glb` |
| PLAYER | `hip_hop_man_pose_open_hit` | 0–15 | `animations/man_and_woman/hip_hop_man_pose_open_hit.blend` | `models/player/animation_updates/hip_hop_man_pose_open_hit_baked_2497d079b819.glb` |
| PLAYER | `hip_hop_man_pose_stagger_left` | 0–15 | `animations/man_and_woman/hip_hop_man_pose_stagger_left.blend` | `models/player/animation_updates/hip_hop_man_pose_stagger_left_baked_0db95aedc0bd.glb` |
| PLAYER | `hip_hop_man_pose_stagger_right` | 0–15 | `animations/man_and_woman/hip_hop_man_pose_stagger_right.blend` | `models/player/animation_updates/hip_hop_man_pose_stagger_right_baked_b91e43176060.glb` |
| PLAYER | `hip_hop_man_pose_wide` | 0–15 | `animations/man_and_woman/hip_hop_man_pose_wide.blend` | `models/player/animation_updates/hip_hop_man_pose_wide_baked_8e014ba4f5a3.glb` |
| PLAYER | `hip_hop_man_reebok` | 0–60 | `animations/man_and_woman/hip_hop_man_reebok.blend` | `models/player/animation_updates/hip_hop_man_reebok_baked_cc7d106efb80.glb` |
| PLAYER | `hip_hop_man_roger_rabbit` | 0–60 | `animations/man_and_woman/hip_hop_man_roger_rabbit.blend` | `models/player/animation_updates/hip_hop_man_roger_rabbit_baked_023e757226a2.glb` |
| PLAYER | `hip_hop_man_running_man` | 0–60 | `animations/man_and_woman/hip_hop_man_running_man.blend` | `models/player/animation_updates/hip_hop_man_running_man_baked_ab06c67de6bd.glb` |
| PLAYER | `hip_hop_man_shoulder_bounce` | 0–60 | `animations/man_and_woman/hip_hop_man_shoulder_bounce.blend` | `models/player/animation_updates/hip_hop_man_shoulder_bounce_baked_5d6fab932380.glb` |
| PLAYER | `hip_hop_man_side_rock` | 0–60 | `animations/man_and_woman/hip_hop_man_side_rock.blend` | `models/player/animation_updates/hip_hop_man_side_rock_baked_5e45c804b313.glb` |
| PLAYER | `hip_hop_man_skate` | 0–60 | `animations/man_and_woman/hip_hop_man_skate.blend` | `models/player/animation_updates/hip_hop_man_skate_baked_efa4672083cd.glb` |
| PLAYER | `hip_hop_man_smurf` | 0–60 | `animations/man_and_woman/hip_hop_man_smurf.blend` | `models/player/animation_updates/hip_hop_man_smurf_baked_dbb40230cd37.glb` |
| PLAYER | `hip_hop_man_step_touch` | 0–60 | `animations/man_and_woman/hip_hop_man_step_touch.blend` | `models/player/animation_updates/hip_hop_man_step_touch_baked_96ff0c1c8ec7.glb` |
| PLAYER | `hip_hop_man_two_step` | 0–60 | `animations/man_and_woman/hip_hop_man_two_step.blend` | `models/player/animation_updates/hip_hop_man_two_step_baked_2a320663d575.glb` |
| PLAYER | `hip_hop_man_up_groove` | 0–60 | `animations/man_and_woman/hip_hop_man_up_groove.blend` | `models/player/animation_updates/hip_hop_man_up_groove_baked_4b3f0a278c43.glb` |
| PLAYER | `hip_hop_man_v_step` | 0–60 | `animations/man_and_woman/hip_hop_man_v_step.blend` | `models/player/animation_updates/hip_hop_man_v_step_baked_02627c2b47da.glb` |
| PLAYER | `hip_hop_man_wide_to_neutral` | 0–30 | `animations/man_and_woman/hip_hop_man_wide_to_neutral.blend` | `models/player/animation_updates/hip_hop_man_wide_to_neutral_baked_93d5641eecf1.glb` |
| PARTNER | `hip_hop_woman_arm_roll` | 0–60 | `animations/man_and_woman/hip_hop_woman_arm_roll.blend` | `models/player/animation_updates/hip_hop_woman_arm_roll_baked_3dbfa4598720.glb` |
| PARTNER | `hip_hop_woman_arm_wave` | 0–60 | `animations/man_and_woman/hip_hop_woman_arm_wave.blend` | `models/player/animation_updates/hip_hop_woman_arm_wave_baked_99548942d54a.glb` |
| PARTNER | `hip_hop_woman_bart_simpson` | 0–60 | `animations/man_and_woman/hip_hop_woman_bart_simpson.blend` | `models/player/animation_updates/hip_hop_woman_bart_simpson_baked_e94baa195c0d.glb` |
| PARTNER | `hip_hop_woman_body_roll` | 0–60 | `animations/man_and_woman/hip_hop_woman_body_roll.blend` | `models/player/animation_updates/hip_hop_woman_body_roll_baked_4a10d5be9237.glb` |
| PARTNER | `hip_hop_woman_box_step` | 0–60 | `animations/man_and_woman/hip_hop_woman_box_step.blend` | `models/player/animation_updates/hip_hop_woman_box_step_baked_465721f8acdc.glb` |
| PARTNER | `hip_hop_woman_cabbage_patch` | 0–60 | `animations/man_and_woman/hip_hop_woman_cabbage_patch.blend` | `models/player/animation_updates/hip_hop_woman_cabbage_patch_baked_3ccee97c2a01.glb` |
| PARTNER | `hip_hop_woman_chest_pop` | 0–60 | `animations/man_and_woman/hip_hop_woman_chest_pop.blend` | `models/player/animation_updates/hip_hop_woman_chest_pop_baked_27f3b359c508.glb` |
| PARTNER | `hip_hop_woman_down_bounce` | 0–60 | `animations/man_and_woman/hip_hop_woman_down_bounce.blend` | `models/player/animation_updates/hip_hop_woman_down_bounce_baked_5a66de594176.glb` |
| PARTNER | `hip_hop_woman_forward_rock` | 0–60 | `animations/man_and_woman/hip_hop_woman_forward_rock.blend` | `models/player/animation_updates/hip_hop_woman_forward_rock_baked_43c41307cb09.glb` |
| PARTNER | `hip_hop_woman_foundation_flow` | 0–240 | `animations/man_and_woman/hip_hop_woman_foundation_flow.blend` | `models/player/animation_updates/hip_hop_woman_foundation_flow_baked_de39cbc26f09.glb` |
| PARTNER | `hip_hop_woman_happy_feet` | 0–60 | `animations/man_and_woman/hip_hop_woman_happy_feet.blend` | `models/player/animation_updates/hip_hop_woman_happy_feet_baked_aeb20c5625cc.glb` |
| PARTNER | `hip_hop_woman_heel_toe` | 0–60 | `animations/man_and_woman/hip_hop_woman_heel_toe.blend` | `models/player/animation_updates/hip_hop_woman_heel_toe_baked_620ba238b308.glb` |
| PARTNER | `hip_hop_woman_isolation_flow` | 0–240 | `animations/man_and_woman/hip_hop_woman_isolation_flow.blend` | `models/player/animation_updates/hip_hop_woman_isolation_flow_baked_d5246e979d94.glb` |
| PARTNER | `hip_hop_woman_kick_step` | 0–60 | `animations/man_and_woman/hip_hop_woman_kick_step.blend` | `models/player/animation_updates/hip_hop_woman_kick_step_baked_93b2bba88f6e.glb` |
| PARTNER | `hip_hop_woman_low_to_neutral` | 0–30 | `animations/man_and_woman/hip_hop_woman_low_to_neutral.blend` | `models/player/animation_updates/hip_hop_woman_low_to_neutral_baked_519d9a339251.glb` |
| PARTNER | `hip_hop_woman_neutral_to_low` | 0–30 | `animations/man_and_woman/hip_hop_woman_neutral_to_low.blend` | `models/player/animation_updates/hip_hop_woman_neutral_to_low_baked_4c8939a614c2.glb` |
| PARTNER | `hip_hop_woman_neutral_to_wide` | 0–30 | `animations/man_and_woman/hip_hop_woman_neutral_to_wide.blend` | `models/player/animation_updates/hip_hop_woman_neutral_to_wide_baked_7ee479780801.glb` |
| PARTNER | `hip_hop_woman_party_machine` | 0–60 | `animations/man_and_woman/hip_hop_woman_party_machine.blend` | `models/player/animation_updates/hip_hop_woman_party_machine_baked_11fc4b89f1dc.glb` |
| PARTNER | `hip_hop_woman_pose_lean_left` | 0–15 | `animations/man_and_woman/hip_hop_woman_pose_lean_left.blend` | `models/player/animation_updates/hip_hop_woman_pose_lean_left_baked_58209d27e5b6.glb` |
| PARTNER | `hip_hop_woman_pose_lean_right` | 0–15 | `animations/man_and_woman/hip_hop_woman_pose_lean_right.blend` | `models/player/animation_updates/hip_hop_woman_pose_lean_right_baked_62a06d93a575.glb` |
| PARTNER | `hip_hop_woman_pose_low` | 0–15 | `animations/man_and_woman/hip_hop_woman_pose_low.blend` | `models/player/animation_updates/hip_hop_woman_pose_low_baked_88e6bff68644.glb` |
| PARTNER | `hip_hop_woman_pose_neutral` | 0–15 | `animations/man_and_woman/hip_hop_woman_pose_neutral.blend` | `models/player/animation_updates/hip_hop_woman_pose_neutral_baked_2be64af5919f.glb` |
| PARTNER | `hip_hop_woman_pose_open_hit` | 0–15 | `animations/man_and_woman/hip_hop_woman_pose_open_hit.blend` | `models/player/animation_updates/hip_hop_woman_pose_open_hit_baked_53cc23d13df3.glb` |
| PARTNER | `hip_hop_woman_pose_stagger_left` | 0–15 | `animations/man_and_woman/hip_hop_woman_pose_stagger_left.blend` | `models/player/animation_updates/hip_hop_woman_pose_stagger_left_baked_886f964401e3.glb` |
| PARTNER | `hip_hop_woman_pose_stagger_right` | 0–15 | `animations/man_and_woman/hip_hop_woman_pose_stagger_right.blend` | `models/player/animation_updates/hip_hop_woman_pose_stagger_right_baked_e012f9605bc7.glb` |
| PARTNER | `hip_hop_woman_pose_wide` | 0–15 | `animations/man_and_woman/hip_hop_woman_pose_wide.blend` | `models/player/animation_updates/hip_hop_woman_pose_wide_baked_8c0024e193e1.glb` |
| PARTNER | `hip_hop_woman_reebok` | 0–60 | `animations/man_and_woman/hip_hop_woman_reebok.blend` | `models/player/animation_updates/hip_hop_woman_reebok_baked_c6feb2e7a9d7.glb` |
| PARTNER | `hip_hop_woman_roger_rabbit` | 0–60 | `animations/man_and_woman/hip_hop_woman_roger_rabbit.blend` | `models/player/animation_updates/hip_hop_woman_roger_rabbit_baked_7ab19742e94e.glb` |
| PARTNER | `hip_hop_woman_running_man` | 0–60 | `animations/man_and_woman/hip_hop_woman_running_man.blend` | `models/player/animation_updates/hip_hop_woman_running_man_baked_301ef8b84858.glb` |
| PARTNER | `hip_hop_woman_shoulder_bounce` | 0–60 | `animations/man_and_woman/hip_hop_woman_shoulder_bounce.blend` | `models/player/animation_updates/hip_hop_woman_shoulder_bounce_baked_8575e6ecae03.glb` |
| PARTNER | `hip_hop_woman_side_rock` | 0–60 | `animations/man_and_woman/hip_hop_woman_side_rock.blend` | `models/player/animation_updates/hip_hop_woman_side_rock_baked_92d13b10014c.glb` |
| PARTNER | `hip_hop_woman_skate` | 0–60 | `animations/man_and_woman/hip_hop_woman_skate.blend` | `models/player/animation_updates/hip_hop_woman_skate_baked_e8de54fbc1f6.glb` |
| PARTNER | `hip_hop_woman_smurf` | 0–60 | `animations/man_and_woman/hip_hop_woman_smurf.blend` | `models/player/animation_updates/hip_hop_woman_smurf_baked_0d162c45730f.glb` |
| PARTNER | `hip_hop_woman_step_touch` | 0–60 | `animations/man_and_woman/hip_hop_woman_step_touch.blend` | `models/player/animation_updates/hip_hop_woman_step_touch_baked_9dce2b616e13.glb` |
| PARTNER | `hip_hop_woman_two_step` | 0–60 | `animations/man_and_woman/hip_hop_woman_two_step.blend` | `models/player/animation_updates/hip_hop_woman_two_step_baked_103f19e9bf87.glb` |
| PARTNER | `hip_hop_woman_up_groove` | 0–60 | `animations/man_and_woman/hip_hop_woman_up_groove.blend` | `models/player/animation_updates/hip_hop_woman_up_groove_baked_3665c1249a68.glb` |
| PARTNER | `hip_hop_woman_v_step` | 0–60 | `animations/man_and_woman/hip_hop_woman_v_step.blend` | `models/player/animation_updates/hip_hop_woman_v_step_baked_7f475b1b3f21.glb` |
| PARTNER | `hip_hop_woman_wide_to_neutral` | 0–30 | `animations/man_and_woman/hip_hop_woman_wide_to_neutral.blend` | `models/player/animation_updates/hip_hop_woman_wide_to_neutral_baked_ff22cec2353d.glb` |

## Integration checkpoint

The asset/status commit was rebased onto concurrent main `3f53f0f503cea6255ee9d4162051d4101d7d7bd9`, becoming `b33559ae7`. The library conflict was resolved by preserving the union of 159 references. All 230 inventoried files retained their original hashes after rebase. Current main's generated LFS policy was retained and its staged check passed. The separate documentation commit adds the hip-hop findings under `# Animation` while preserving other animation chats' guidance.

Post-rebase required fast suite: **9/10 checks passed in 5.46 seconds**. The activity JSON check remains blocked by existing hair-model GLB imports (`bob01`, `bob02`, `short01`–`short04`, `afro01`); the error propagates through the existing `Character.STYLES` dependency. The additional current-main test-runner check passed. Full output is retained in `hip_hop_freestyle_evidence/fast_tests_after_rebase.log`. This result is the latest fast-suite checkpoint and supersedes the earlier 9/9 and 8/9 results.
