# Watusi solo repertoire — stopped work record

- Date: October 2, 2026, Europe/Berlin; preservation verification completed at approximately 17:00 CEST.
- Chat title/task label: Watusi solo animations for man_and_woman3.blend.
- Task branch: `codex/watusi-solo-repertoire`.
- Starting/current commit before preservation commits: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Checkout: `/workspace/sanjo-solutions`, project `apps/a-game`, sanjo-solutions cloud environment.
- Recorder and GitHub commit communications: Codex.
- Current instruction: stop animation work, preserve its present state, document and verify it, commit, merge, and push. Further authoring, refinement, generation, and rendering stopped.

## Original scope and present disposition

The original request covered a broad solo Watusi repertoire for both characters,
Blender 5.2 throughout, the repository's per-animation source workflow, natural
motion and contact/loop review, reuse of suitable existing dance work, asset
storage by actual size, commits, rebase onto origin/main, Animation documentation,
and merging/pushing main.

This is **partial procedural choreography and a blocking study**, rather than an
accepted completed animation library. Thirty-seven source/export pairs are saved:
20 for Man and 17 for Woman. Each source has an editable Rigify action and a
matching `.baked` deform action. Each GLB contains one solo clip. The pre-integration candidate registry registered these draft exports. Its exact
contents are preserved as `watusi_solo_repertoire_evidence/candidate_animation_updates.tres`.
Final integration retains upstream main's active registry and keeps Watusi drafts
out of runtime registration, following the newer Animation delivery guidance.
Both low-swing clips fail the recorded IK reach tolerance. Fresh-load comparison
also fails for every Man source/bake pair. The Woman entry, exit, and routine
remain unsaved. Full-body mesh clearance, complete playback review, and runtime
playback acceptance remain open.

## Work completed

- Read root/project AGENTS.md, paired authoring, motion-review, per-animation,
  export, testing, and asset-versioning instructions.
- Confirmed Blender 5.2.2 LTS (`d13f752e3b9c`) and used it for every Blender command.
- Retrieved the shared scene, linked anatomical assets, disco source, and local
  project asset dependencies through the configured GitHub credential. Credential
  values were kept outside logs and committed files.
- Reused DiscoCharacter, DiscoWristPoser, and RigYogaPoser for proportional IK,
  wrist placement, poles, and foot targets; authored Watusi-specific movement.
- Saved one Blender file per solo action using AnimationFileWriter and shared
  scene references, then compact GLB exports with AnimationClipScene and
  AnimationUpdates. The shared scene, combined library, and model sources retain
  their prior Git contents.
- Authored sparse six-frame pose keys with one initial key for stationary
  channels. Clips run at 24 fps/120 BPM. Loop endpoints and cyclic tangents are
  authored explicitly. Position clips are static holds.
- Sampled editable motion every half-frame in the interrupted build. Thirty-five
  of 37 saved clips passed that in-memory review; both low-swing variants failed.
- Preserved 14 completed CPU Cycles review PNGs (12 Man views, two Woman basic-sway
  views). These are preliminary, partially overexposed diagnostic images. The
  final lighting changes in render_watusi.py were saved after the renderer started
  and are **not represented** by these images. No later renders were generated.

## Exact asset state

Paths below are relative to `apps/a-game`. Each source contains the base action
and its `.baked` action. Man's role is PLAYER and Woman's role is PARTNER; each
source has just its character's authoring/deform slots. All listed assets are
work in progress. The full binary inventory, actual byte counts, and SHA-256
hashes are in `watusi_solo_repertoire_evidence/asset_inventory.json` beside this
record. Every listed GLB also has a `.glb.import` settings file.

| Character / move | Frames | Source file | Export file | In-memory motion | Fresh-load bake |
| --- | --- | --- | --- | --- | --- |
| man / alternating_swing | 0–96 | `animations/man_and_woman/man_watusi_alternating_swing.blend` | `models/player/animation_updates/man_watusi_alternating_swing_baked_8fe69eb7907c.glb` | pass | FAIL: pose mismatch |
| man / basic_sway | 0–96 | `animations/man_and_woman/man_watusi_basic_sway.blend` | `models/player/animation_updates/man_watusi_basic_sway_baked_00061d173e5f.glb` | pass | FAIL: pose mismatch |
| man / double_time_sway | 0–96 | `animations/man_and_woman/man_watusi_double_time_sway.blend` | `models/player/animation_updates/man_watusi_double_time_sway_baked_0de28af169fa.glb` | pass | FAIL: pose mismatch |
| man / elbow_pump | 0–96 | `animations/man_and_woman/man_watusi_elbow_pump.blend` | `models/player/animation_updates/man_watusi_elbow_pump_baked_57719ed901a0.glb` | pass | FAIL: pose mismatch |
| man / enter | 0–48 | `animations/man_and_woman/man_watusi_enter.blend` | `models/player/animation_updates/man_watusi_enter_baked_e62a2ad4f604.glb` | pass | FAIL: pose mismatch |
| man / exit | 0–48 | `animations/man_and_woman/man_watusi_exit.blend` | `models/player/animation_updates/man_watusi_exit_baked_d24404375b41.glb` | pass | FAIL: pose mismatch |
| man / forward_back_swing | 0–96 | `animations/man_and_woman/man_watusi_forward_back_swing.blend` | `models/player/animation_updates/man_watusi_forward_back_swing_baked_3fdabe8f0668.glb` | pass | FAIL: pose mismatch |
| man / high_swing | 0–96 | `animations/man_and_woman/man_watusi_high_swing.blend` | `models/player/animation_updates/man_watusi_high_swing_baked_1f88ae08ed40.glb` | pass | FAIL: pose mismatch |
| man / low_dip | 0–96 | `animations/man_and_woman/man_watusi_low_dip.blend` | `models/player/animation_updates/man_watusi_low_dip_baked_3c40c2b0488e.glb` | pass | FAIL: pose mismatch |
| man / low_swing | 0–96 | `animations/man_and_woman/man_watusi_low_swing.blend` | `models/player/animation_updates/man_watusi_low_swing_baked_145eb0a6b35d.glb` | FAIL: reach | FAIL: pose mismatch |
| man / position_low | 0–96 | `animations/man_and_woman/man_watusi_position_low.blend` | `models/player/animation_updates/man_watusi_position_low_baked_a753e3da06ae.glb` | pass | FAIL: pose mismatch |
| man / position_open | 0–96 | `animations/man_and_woman/man_watusi_position_open.blend` | `models/player/animation_updates/man_watusi_position_open_baked_bc3163d0b072.glb` | pass | FAIL: pose mismatch |
| man / position_ready | 0–96 | `animations/man_and_woman/man_watusi_position_ready.blend` | `models/player/animation_updates/man_watusi_position_ready_baked_3d48ce85220c.glb` | pass | FAIL: pose mismatch |
| man / position_weight_left | 0–96 | `animations/man_and_woman/man_watusi_position_weight_left.blend` | `models/player/animation_updates/man_watusi_position_weight_left_baked_83af896b19b5.glb` | pass | FAIL: pose mismatch |
| man / position_weight_right | 0–96 | `animations/man_and_woman/man_watusi_position_weight_right.blend` | `models/player/animation_updates/man_watusi_position_weight_right_baked_54e34481c7e7.glb` | pass | FAIL: pose mismatch |
| man / routine | 0–384 | `animations/man_and_woman/man_watusi_routine.blend` | `models/player/animation_updates/man_watusi_routine_baked_035143811d26.glb` | pass | FAIL: pose mismatch |
| man / shoulder_accent | 0–96 | `animations/man_and_woman/man_watusi_shoulder_accent.blend` | `models/player/animation_updates/man_watusi_shoulder_accent_baked_b405145d2e28.glb` | pass | FAIL: pose mismatch |
| man / side_reach | 0–96 | `animations/man_and_woman/man_watusi_side_reach.blend` | `models/player/animation_updates/man_watusi_side_reach_baked_b05c525e0c5c.glb` | pass | FAIL: pose mismatch |
| man / step_touch_left | 0–96 | `animations/man_and_woman/man_watusi_step_touch_left.blend` | `models/player/animation_updates/man_watusi_step_touch_left_baked_8a00936bef6f.glb` | pass | FAIL: pose mismatch |
| man / step_touch_right | 0–96 | `animations/man_and_woman/man_watusi_step_touch_right.blend` | `models/player/animation_updates/man_watusi_step_touch_right_baked_2f03fedc7af4.glb` | pass | FAIL: pose mismatch |
| woman / alternating_swing | 0–96 | `animations/man_and_woman/woman_watusi_alternating_swing.blend` | `models/player/animation_updates/woman_watusi_alternating_swing_baked_8b3f96736b91.glb` | pass | pass |
| woman / basic_sway | 0–96 | `animations/man_and_woman/woman_watusi_basic_sway.blend` | `models/player/animation_updates/woman_watusi_basic_sway_baked_7d1d5d9c9671.glb` | pass | pass |
| woman / double_time_sway | 0–96 | `animations/man_and_woman/woman_watusi_double_time_sway.blend` | `models/player/animation_updates/woman_watusi_double_time_sway_baked_78384dfce6f7.glb` | pass | pass |
| woman / elbow_pump | 0–96 | `animations/man_and_woman/woman_watusi_elbow_pump.blend` | `models/player/animation_updates/woman_watusi_elbow_pump_baked_ac7e2f9a1abf.glb` | pass | pass |
| woman / forward_back_swing | 0–96 | `animations/man_and_woman/woman_watusi_forward_back_swing.blend` | `models/player/animation_updates/woman_watusi_forward_back_swing_baked_e905ba0cf8fa.glb` | pass | pass |
| woman / high_swing | 0–96 | `animations/man_and_woman/woman_watusi_high_swing.blend` | `models/player/animation_updates/woman_watusi_high_swing_baked_c39f1c8eaded.glb` | pass | pass |
| woman / low_dip | 0–96 | `animations/man_and_woman/woman_watusi_low_dip.blend` | `models/player/animation_updates/woman_watusi_low_dip_baked_5b280177b113.glb` | pass | pass |
| woman / low_swing | 0–96 | `animations/man_and_woman/woman_watusi_low_swing.blend` | `models/player/animation_updates/woman_watusi_low_swing_baked_ace0ddcbec6e.glb` | FAIL: reach | pass |
| woman / position_low | 0–96 | `animations/man_and_woman/woman_watusi_position_low.blend` | `models/player/animation_updates/woman_watusi_position_low_baked_0539d156bd56.glb` | pass | pass |
| woman / position_open | 0–96 | `animations/man_and_woman/woman_watusi_position_open.blend` | `models/player/animation_updates/woman_watusi_position_open_baked_969e61581345.glb` | pass | pass |
| woman / position_ready | 0–96 | `animations/man_and_woman/woman_watusi_position_ready.blend` | `models/player/animation_updates/woman_watusi_position_ready_baked_07d29c19d43d.glb` | pass | pass |
| woman / position_weight_left | 0–96 | `animations/man_and_woman/woman_watusi_position_weight_left.blend` | `models/player/animation_updates/woman_watusi_position_weight_left_baked_7212c5d822b6.glb` | pass | pass |
| woman / position_weight_right | 0–96 | `animations/man_and_woman/woman_watusi_position_weight_right.blend` | `models/player/animation_updates/woman_watusi_position_weight_right_baked_cd991af5b2d4.glb` | pass | pass |
| woman / shoulder_accent | 0–96 | `animations/man_and_woman/woman_watusi_shoulder_accent.blend` | `models/player/animation_updates/woman_watusi_shoulder_accent_baked_4b1fa0ad825d.glb` | pass | pass |
| woman / side_reach | 0–96 | `animations/man_and_woman/woman_watusi_side_reach.blend` | `models/player/animation_updates/woman_watusi_side_reach_baked_d85d65b15790.glb` | pass | pass |
| woman / step_touch_left | 0–96 | `animations/man_and_woman/woman_watusi_step_touch_left.blend` | `models/player/animation_updates/woman_watusi_step_touch_left_baked_b1985ae1e8bb.glb` | pass | pass |
| woman / step_touch_right | 0–96 | `animations/man_and_woman/woman_watusi_step_touch_right.blend` | `models/player/animation_updates/woman_watusi_step_touch_right_baked_1262a038516a.glb` | pass | pass |

The 0–96 loops have a duplicate endpoint; entry/exit are 0–48 single-play clips;
the Man routine is 0–384 with a duplicate loop endpoint. Woman's intended
`woman_watusi_enter.blend`, `woman_watusi_exit.blend`, and
`woman_watusi_routine.blend` have **no durable source or export**. The interrupted
builder had printed `AUTHOR woman_watusi_enter`; its in-memory state was discarded
when the owned process received SIGTERM.

## Code, documentation, evidence, and storage

- `scripts/create_watusi.py`: reproducible draft author/bake/export pipeline. The
  low-swing hand-height decrement was edited from 0.16 to 0.10 before the stop;
  the running builder had already loaded 0.16, so **saved low-swing assets still
  use 0.16**. The 0.10 change remains an unexecuted proposed correction.
- `scripts/review_watusi.py`: subframe IK/plant/wrist/limb/proxy-clearance/seam
  diagnostics and source-to-baked pose comparison. Proxy tests cover local hand
  clearance, rather than full mesh collision coverage. Angular seam velocity is
  a remaining review item.
- `scripts/render_watusi.py`: draft Blender 5.2 CPU Cycles front/side renderer;
  latest lighting adjustment remains unrendered.
- `scripts/test_watusi.py`: full-repertoire check plus `--available` structural
  and saved-pose verification for interrupted output. Available verification
  currently exits with failure for the 20 Man source/bake mismatches.
- `scripts/watusi.md`: intended 40-clip catalogue, timing, reuse, and workflow;
  explicitly annotated with the interrupted state.
- `docs/animation_reviews/watusi/metrics_Woman_basic_sway.json`: successful
  single-clip in-session prototype report. This is narrower than fresh-load
  verification and does not certify the whole repertoire.
- `docs/animation_work_status/watusi_solo_repertoire_evidence/`: raw build,
  render, import, and test logs; recovered motion metrics; saved-bake comparison;
  binary inventory; 14 existing PNGs. No complete build `metrics.json` was written
  because the process was interrupted before its final report write.
- `apps/a-game/.gitattributes`: exact-path overrides for the 88 task binaries.
  Their largest actual file is 6,049,824 bytes; aggregate size is 68,856,170 bytes.
  All are at or below 104,857,600 bytes and use ordinary Git. Existing repository
  LFS policies continue to apply to other files. Git attributes were inspected
  before staging. This task creates no new LFS payload.

## Validation and concrete blockers

Commands below run from `apps/a-game`, with `GODOT` set to
`/workspace/.cloud-onboarding/bin/godot` (4.7.2) and `BLENDER` set to
`/workspace/.cloud-onboarding/bin/blender` (5.2.2).

1. `python tests/run_tests.py --suite fast`: **9/9 pass**, 6.30 seconds after
   stopping. Earlier initial run was 8/9 because hair .res assets were still LFS
   pointers; fetching their contents resolved that prerequisite.
2. `python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_single_animation_layout.py`:
   **11/11 pass**, including the nine fast tests and two focused slow tests.
3. `python scripts/test_watusi.py --available`: **FAIL** after structural and GLB
   checks. All 37 source families have the expected action pair, role, slot,
   range, shared-scene reference, and NLA bindings. GLB finite values, one-clip
   layout, participant separation, duration, loop endpoints, and import-loop
   settings passed before Blender verification. Saved pose comparison passes for
   17 Woman clips and fails for all 20 Man clips. Largest observed Man error is
   approximately 0.0641 m / 2.066 radians at finger bones; endpoint error reaches
   approximately 0.0269 m. Diagnose shared-scene rotation modes/control state and
   replay bindings before any future acceptance. The cause remains unconfirmed.
4. `python -m py_compile scripts/create_watusi.py scripts/review_watusi.py scripts/render_watusi.py scripts/test_watusi.py`: pass.
5. Build-time half-frame review: 35 pass, two fail. Man low-swing maximum IK error
   is 0.008705 m; Woman low-swing is 0.011922 m against a 0.003 m threshold. The
   recorded geometry/reach failure remains in the saved outputs.
6. Godot `--headless --editor --import`: attempted before all local LFS assets
   were restored; log records 1,255 errors including pointer .res/.scn resources
   and downstream scene imports. Full app LFS contents were subsequently fetched,
   but global import and runtime playback were not rerun following the stop.
   No successful gameplay validation is claimed. Three unrelated generated
   import/eye-resource modifications from this task were restored to HEAD.
7. The environment lacks Game Rig Tools. The draft evaluated-frame bake uses
   Blender 5.2 and existing writer/export components. A native visual-bake trial
   exposed inherited-shear toe drift; rigid frame sampling reduced the prototype
   endpoint error to approximately 0.0000032 m. The rigid bake omits local segment
   volume scaling; fresh-load Man failures still require investigation.
8. Workbench rendering failed with EGL_BAD_MATCH; CPU Cycles produced the saved
   images. Full surface clearance, finger posture review, smooth-transition
   playback, and final visual acceptance are pending.

## Process and saved-output preservation

Owned authoring PID 1601 and rendering PID 2644 received SIGTERM immediately
following the stop instruction. Their completed output files were copied into
the evidence directory. No authoring or rendering process remains running.
Only read-only validation processes ran afterward and completed. The builder's
last saved export was `woman_watusi_position_open_baked_969e61581345.glb`.
The last authoring marker was `AUTHOR woman_watusi_enter`.

Temporary `.cache/watusi` products remain local; the durable source/export files,
logs, metrics, and completed images are committed. `/tmp/watusi-git-askpass`
contains only code referencing the configured token variable and is removed
following delivery; it contains no stored token. The combined source discovers
new clips through its normal helper workflow when all asset prerequisites exist.

## Remaining work and exact resume commands

Resume animation work only after a new user instruction authorizes it. Start
with diagnosis and review of the Man fresh-load mismatch, then correct low-swing
reach, verify the proposed 0.10 decrement, complete Woman's three remaining
clips, and rerun all geometric, loop-velocity, surface, transition, and runtime
checks. Reconcile generator output with existing saved files and concurrent
registry changes before any regeneration.

```sh
cd /workspace/sanjo-solutions/apps/a-game
export BLENDER=/workspace/.cloud-onboarding/bin/blender
export GODOT=/workspace/.cloud-onboarding/bin/godot
# Read-only reproduction of current acceptance failure:
python scripts/test_watusi.py --available
python tests/run_tests.py --suite fast
python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_single_animation_layout.py
# Only after renewed animation authorization and diagnosis:
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/create_watusi.py -- --character Man --move low_swing
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/create_watusi.py -- --character Woman --move low_swing
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/create_watusi.py -- --character Woman --move enter
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/create_watusi.py -- --character Woman --move exit
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/create_watusi.py -- --character Woman --move routine
# A complete rebuild writes the aggregate metrics expected by the full test:
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/create_watusi.py
python scripts/test_watusi.py
blender -t 4 -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/render_watusi.py
"$GODOT" --headless --editor --import --quit
```

## Integration

The preservation commit carries this record and task-owned files. Immediately
before integration, fetch origin/main and preserve concurrent updates to the
animation registry, attributes, and AGENTS.md. Use ordinary pushes and retry
with the newer main on an ordinary rejection. Final task/documentation/merge
hashes and remote verification are reported in the chat delivery response;
commit self-identification is available through `git log --follow` on this file.


### Rebase and documentation checkpoint

The preservation commit rebased successfully onto `18e528c73` and became
`99bc7f48a`. Concurrent animation/documentation changes were preserved. This
new upstream commit supplies `scripts/blender/install_animation_tools.py` and
bundled Game Rig Tools; the earlier missing-add-on observation describes the
original checkout. Read the current `scripts/blender/README.md` before a future
resume, and use the same isolated Blender profile for authoring and verification.
The stop instruction remains active; this integration performed no animation
repairs or generation. Two guidance bullets were added under AGENTS.md's
Animation validation and delivery subsection to cover durable per-clip
checkpoints, generator/output revision correspondence, and this draft's evidence.


After rebasing, the updated required fast suite passed **10/10** in 9.68 seconds.
`python scripts/lfs_policy.py check` passed for 23,501 indexed files. The shared
scene SHA-256 still matches the initial LFS payload, so the saved verification
report uses the same shared-template bytes after this integration. The new fast
suite log is `watusi_solo_repertoire_evidence/post_rebase_fast.log`.


### Concurrent integration resolution

Immediately before the merge, origin/main advanced to `43b08e485`. Conflicts in
app `.gitattributes` and AGENTS.md were resolved by retaining both tasks' entries.
Main's active animation-update registry was retained verbatim; Watusi's candidate
registry was saved in the evidence directory, which now has `.gdignore`. The
newer repository guidance reserves runtime publication for reviewed matching
revisions. All 37 Watusi source/export pairs remain preserved at their recorded
paths as draft assets; this merge performs no animation changes.

Merge-resolution verification: the fast suite passed **10/10** in 9.49 seconds, the LFS size policy passed for 24,174 indexed files, and `git diff --cached --check` passed. See `watusi_solo_repertoire_evidence/merge_fast.log`.
