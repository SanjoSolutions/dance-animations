# Bollywood solo animation work status

Recorded October 2, 2026, 17:00 Europe/Berlin. Chat title: Bollywood solo repertoire for man_and_woman3.blend (task description; UI title was unavailable). Task branch: `codex/bollywood-solo-repertoire`. Commit at the stopping point: `fe09ef7b6a54f03909f7335d9673a27c15007d69`. The preservation commit containing this record identifies the delivered task state through Git history.

## Scope and stop

Original scope: create a broad, organized Bollywood solo repertoire for both characters in A-Game, reuse suitable existing motion, use Blender 5.2 throughout, follow the per-animation source workflow, validate interpolation and contacts, commit, rebase onto origin/main, update the Animation instructions, merge into main, push, and verify uploads.

The user's October 2 stop instruction changed the active goal to preserving and delivering the present state. Authoring stopped after `bollywood_woman_snake_arms`. Owned Blender PID 1654 received SIGTERM and exited. The next `lotus_open` phrase had no durable source, bake, export, or report. Every durable animation output has a matching completion report; the inventory contains zero orphan source or GLB files. Further authoring, refinement, generation, and rendering await an explicit resume instruction.

## Completed assets and delivery state

Thirty independently playable solo clips cover fifteen moves for each character. Every listed source contains one editable Rigify action and its matching `.baked` action, one character slot each, using existing `shared_scene_data.blend`. Each clip spans frames 0–96 at 24 fps (four seconds), with a repeated loop endpoint and short ready-stance holds. Man clips use PLAYER; Woman clips use PARTNER. Each clip has an individual GLB export and companion `.glb.import` configured for linear looping. `models/player/animation_updates.tres` references the exports. These clips are provisional choreography requiring the remaining visual and surface review before a production-quality claim.

The repertoire composes `DiscoCharacter`, its forearm-relative wrist calibration, `DiscoChoreography.retrieve_feet`, and `RigYogaPoser`. Blender 5.2.2 LTS performed authoring, native visual baking, the compact GLB export, verification, and the early preview render. At authoring time, the installed environment provided Player Asset Export and Rigify; Game Rig Tools was unavailable. The task uses Blender's native visual bake and the repository's `AnimationFileWriter`, `AnimationClipScene`, `AnimationParticipants`, and `AnimationUpdates` workflow. Control constraints and the shared scene remain editable.

| Clip | Solo role | Editable + baked source | Individual GLB | Surface review |
| --- | --- | --- | --- | --- |
| bollywood_man_bhangra_bounce | Man / PLAYER | `animations/man_and_woman/bollywood_man_bhangra_bounce.blend` (808901 bytes) | `models/player/animation_updates/bollywood_man_bhangra_bounce_baked_93ef7d8f411c.glb` (363024 bytes) | pending |
| bollywood_man_bhangra_overhead | Man / PLAYER | `animations/man_and_woman/bollywood_man_bhangra_overhead.blend` (821193 bytes) | `models/player/animation_updates/bollywood_man_bhangra_overhead_baked_75ad8cb3686a.glb` (362888 bytes) | pending |
| bollywood_man_bhangra_shoulders | Man / PLAYER | `animations/man_and_woman/bollywood_man_bhangra_shoulders.blend` (806106 bytes) | `models/player/animation_updates/bollywood_man_bhangra_shoulders_baked_3d75d4e6a2f9.glb` (362892 bytes) | pending |
| bollywood_man_chest_pulse | Man / PLAYER | `animations/man_and_woman/bollywood_man_chest_pulse.blend` (819008 bytes) | `models/player/animation_updates/bollywood_man_chest_pulse_baked_748138e44417.glb` (358912 bytes) | pending |
| bollywood_man_forward_back | Man / PLAYER | `animations/man_and_woman/bollywood_man_forward_back.blend` (821909 bytes) | `models/player/animation_updates/bollywood_man_forward_back_baked_65c60c731492.glb` (360728 bytes) | pending |
| bollywood_man_garba_sweep | Man / PLAYER | `animations/man_and_woman/bollywood_man_garba_sweep.blend` (849673 bytes) | `models/player/animation_updates/bollywood_man_garba_sweep_baked_5839d087c5b3.glb` (359004 bytes) | pending |
| bollywood_man_heel_dig | Man / PLAYER | `animations/man_and_woman/bollywood_man_heel_dig.blend` (827191 bytes) | `models/player/animation_updates/bollywood_man_heel_dig_baked_7f28ad445dc7.glb` (360724 bytes) | pending |
| bollywood_man_hip_sway | Man / PLAYER | `animations/man_and_woman/bollywood_man_hip_sway.blend` (811656 bytes) | `models/player/animation_updates/bollywood_man_hip_sway_baked_20e9cd5ea69c.glb` (357464 bytes) | pending |
| bollywood_man_knee_lift | Man / PLAYER | `animations/man_and_woman/bollywood_man_knee_lift.blend` (818276 bytes) | `models/player/animation_updates/bollywood_man_knee_lift_baked_54797f675811.glb` (360724 bytes) | pending |
| bollywood_man_shoulder_shimmy | Man / PLAYER | `animations/man_and_woman/bollywood_man_shoulder_shimmy.blend` (810793 bytes) | `models/player/animation_updates/bollywood_man_shoulder_shimmy_baked_e315018d21a6.glb` (359832 bytes) | pending |
| bollywood_man_snake_arms | Man / PLAYER | `animations/man_and_woman/bollywood_man_snake_arms.blend` (812550 bytes) | `models/player/animation_updates/bollywood_man_snake_arms_baked_504e9f1bac26.glb` (360588 bytes) | pending |
| bollywood_man_step_touch | Man / PLAYER | `animations/man_and_woman/bollywood_man_step_touch.blend` (842666 bytes) | `models/player/animation_updates/bollywood_man_step_touch_baked_843bd326ed45.glb` (359276 bytes) | pending |
| bollywood_man_thumka_left | Man / PLAYER | `animations/man_and_woman/bollywood_man_thumka_left.blend` (802000 bytes) | `models/player/animation_updates/bollywood_man_thumka_left_baked_52922659c22b.glb` (362100 bytes) | pending |
| bollywood_man_thumka_right | Man / PLAYER | `animations/man_and_woman/bollywood_man_thumka_right.blend` (800439 bytes) | `models/player/animation_updates/bollywood_man_thumka_right_baked_8da281f6b65d.glb` (357468 bytes) | pending |
| bollywood_man_wrist_circles | Man / PLAYER | `animations/man_and_woman/bollywood_man_wrist_circles.blend` (809755 bytes) | `models/player/animation_updates/bollywood_man_wrist_circles_baked_b1a82721667f.glb` (360592 bytes) | pending |
| bollywood_woman_bhangra_bounce | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_bhangra_bounce.blend` (807267 bytes) | `models/player/animation_updates/bollywood_woman_bhangra_bounce_baked_944de335f97b.glb` (357120 bytes) | pending |
| bollywood_woman_bhangra_overhead | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_bhangra_overhead.blend` (820711 bytes) | `models/player/animation_updates/bollywood_woman_bhangra_overhead_baked_1ae60c7b3868.glb` (357124 bytes) | pending |
| bollywood_woman_bhangra_shoulders | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_bhangra_shoulders.blend` (810808 bytes) | `models/player/animation_updates/bollywood_woman_bhangra_shoulders_baked_4c36a296e1d3.glb` (357124 bytes) | pending |
| bollywood_woman_chest_pulse | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_chest_pulse.blend` (809744 bytes) | `models/player/animation_updates/bollywood_woman_chest_pulse_baked_986985becc12.glb` (356324 bytes) | pending |
| bollywood_woman_forward_back | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_forward_back.blend` (819320 bytes) | `models/player/animation_updates/bollywood_woman_forward_back_baked_f70ab2312f60.glb` (354640 bytes) | pending |
| bollywood_woman_garba_sweep | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_garba_sweep.blend` (832491 bytes) | `models/player/animation_updates/bollywood_woman_garba_sweep_baked_a2b2460f78b5.glb` (357864 bytes) | pending |
| bollywood_woman_heel_dig | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_heel_dig.blend` (826945 bytes) | `models/player/animation_updates/bollywood_woman_heel_dig_baked_4299f6561210.glb` (354772 bytes) | pending |
| bollywood_woman_hip_sway | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_hip_sway.blend` (804676 bytes) | `models/player/animation_updates/bollywood_woman_hip_sway_baked_205f639f5811.glb` (356320 bytes) | pending |
| bollywood_woman_knee_lift | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_knee_lift.blend` (821198 bytes) | `models/player/animation_updates/bollywood_woman_knee_lift_baked_d9c8f6032605.glb` (354772 bytes) | pending |
| bollywood_woman_shoulder_shimmy | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_shoulder_shimmy.blend` (804860 bytes) | `models/player/animation_updates/bollywood_woman_shoulder_shimmy_baked_9383c258f7ae.glb` (358656 bytes) | pending |
| bollywood_woman_snake_arms | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_snake_arms.blend` (806079 bytes) | `models/player/animation_updates/bollywood_woman_snake_arms_baked_cbe85fce66ef.glb` (354776 bytes) | pending |
| bollywood_woman_step_touch | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_step_touch.blend` (829290 bytes) | `models/player/animation_updates/bollywood_woman_step_touch_baked_c03e7dcd4f5f.glb` (356324 bytes) | pass |
| bollywood_woman_thumka_left | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_thumka_left.blend` (802160 bytes) | `models/player/animation_updates/bollywood_woman_thumka_left_baked_c3068f2236ef.glb` (354776 bytes) | pending |
| bollywood_woman_thumka_right | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_thumka_right.blend` (804622 bytes) | `models/player/animation_updates/bollywood_woman_thumka_right_baked_3481288d5298.glb` (354776 bytes) | pending |
| bollywood_woman_wrist_circles | Woman / PARTNER | `animations/man_and_woman/bollywood_woman_wrist_circles.blend` (810522 bytes) | `models/player/animation_updates/bollywood_woman_wrist_circles_baked_8b21060bbe6d.glb` (354776 bytes) | pending |

Each clip's detailed half-frame and bake report lives in `animations/bollywood/<clip>.json`. The report lists the source, export, actual byte sizes, Blender version, and measured results. The read-only preservation audit includes SHA-256 hashes and a complete path inventory for all sources, exports, imports, and reports.

## Supporting files and procedural blocking studies

- `scripts/bollywood/repertoire.py`: procedural catalog and choreography. The planned catalog has 26 motifs per character; 15 motifs have durable outputs.
- `scripts/bollywood/author.py`: source writer, native visual bake, compact individual export, and motion-report orchestration. Resume only the unfinished motifs with explicit arguments, because a default run regenerates the full catalog.
- `scripts/bollywood/review.py`: evaluated IK, wrist, contact, proxy clearance, loop-boundary, and baked-transform measurements.
- `scripts/bollywood/surface_review.py`: skin-topology review using forearm/hand/finger vertices against torso/head surfaces and sole-height sampling. One successful saved-source run is recorded for Woman step touch.
- `scripts/bollywood/render_review.py`: unfinished contact-sheet study, saved before the stop and never executed. Its catalog assumes all 26 motifs exist, so the partial catalog currently blocks the default command. Its `main()` requires Blender arguments after `--`; keep that delimiter in a future run.
- `scripts/bollywood/README.md`: preservation and resume guide.
- `animations/bollywood/.gdignore`: keeps reports outside Godot imports.
- `docs/animation_work_status/bollywood_solo_evidence/woman_snake_arms_blocking_preview.png`: early, one-frame procedural blocking preview of the woman's snake-arm pose, rendered before the final loop-boundary revision. It is a silhouette study rather than a full-motion or current-bake approval. Preserve it as evidence; it establishes neither complete surface coverage nor production readiness.
- Evidence: `authoring_at_stop.log`, `fast_suite.log`, `related_selection.log`, `surface_review.log`, `blocking_preview.log`, `preservation_audit.log`, and `verify_preserved.py` in the same evidence directory.
- Exact-name `.gitattributes` in the source, export, and evidence directories store only this task's binaries directly in Git. The root LFS policy continues to cover other files.

## Verification and practical limits

Commands run from `apps/a-game`:

```sh
python tests/run_tests.py --suite fast
python tests/run_tests.py --list --changed scripts/bollywood/author.py --changed scripts/bollywood/repertoire.py --changed scripts/bollywood/review.py --changed scripts/bollywood/surface_review.py --changed scripts/bollywood/render_review.py
blender --background --factory-startup --python-exit-code 1 --python docs/animation_work_status/bollywood_solo_evidence/verify_preserved.py
blender --background animations/man_and_woman/bollywood_woman_step_touch.blend --python-exit-code 1 --python scripts/bollywood/surface_review.py
```

- Final required fast suite: 9/9 pass in 3.09 seconds. Initial setup passed 8/9 because three hair `.res` files were LFS pointers. Hydrating those existing assets restored 9/9. Setup hydration changed local binary availability, with source repository contents preserved.
- Related selection for the five new scripts: 9 fast, 0 slow. Separate Blender verification covered actual saved source and export files.
- Preservation audit: all 30 sources load through Blender 5.2 and contain precisely one authoring/baked family, a valid shared-template descriptor, the correct single-character role and binding, and frames 0–96. All 30 GLBs have valid headers, one matching animation, over 600 channels, a four-second range, the intended deform rig, and linear-loop import settings.
- Authoring measurements: 193 samples per clip at half-frame spacing. Bakes were compared at all 97 integer frames. All 30 clips passed their recorded endpoint, wrist, local proxy, plant-drift, and loop checks.
- Maximum recorded values across the 30 reports:

```json
{
  "maximum_foot_target_error": 0.00021435739905415645,
  "maximum_hand_target_error": 5.79018936244969e-06,
  "maximum_wrist_bend": 23.589484100628276,
  "maximum_planted_drift": 8.740653954112857e-05,
  "loop_position_error": 0,
  "loop_angle_error": 0,
  "loop_velocity_error": 0
}
```

- Full skin-surface sampling is complete for Woman step touch only: 34 samples, zero detected near-surface penetration, minimum sole height about -0.000136 meters, and highest lowest-sole height about 0.000161 meters. Other 29 clips retain proxy and endpoint checks and await skin-surface review. The surface test disables topology-changing modifiers to preserve vertex identity, so it checks the deforming base skin rather than final subdivision.
- Current loop checks measure landmark position, orientation, and linear velocity. Whole-body mesh intersection coverage, angular-velocity continuity, complete finger/contact ergonomics, dynamic balance, and full visual playback across all clips remain review work.
- Godot project import and actual playback of these newly exported GLBs remain pending. The audit establishes the exported layout and metadata; it does not establish runtime track resolution on the composed player model.
- The combined `man_and_woman3.blend` uses source discovery on reopen. The task created individual source files; its combined-library reopen/discovery remains pending.

## Remaining work and blockers

Unfinished motifs for both characters: `lotus_open`, `jhumka`, `filmi_point`, `diagonal_reach`, `offering_sweep`, `ready`, `namaste`, `wide_open`, `tribhanga`, `ready_to_namaste`, `namaste_to_ready`. These eleven motifs represent 22 planned clips with authored/baked/exported status pending. The overall repertoire is partial. Namaste wrist comfort, pose files with a single constant key, and transition endpoints have yet to receive an authoring validation run.

The active blocker is the user's stop instruction. At authoring time, Game Rig Tools was unavailable; the saved native-bake path provides the current bakes. Integration subsequently brought in the bundled Game Rig Tools installer described below. The contact-sheet study requires the unfinished source files. Further choreography should include support-weight transfer review and broader dance/turn variants as appropriate; the procedural catalog is an organized Bollywood-inspired subset rather than an exhaustive dance vocabulary.

All owned animation processes have exited. Durable outputs are the 30 source/export/report families, scripts, evidence logs, and early blocking PNG listed above. Temporary `/tmp/bollywood-*` diagnostics have preserved copies for the meaningful results. The shared scene and anatomical sources were hydrated from existing LFS objects and carry the repository's original content.

## Exact resume commands

Run read-only delivery verification any time:

```sh
cd /workspace/sanjo-solutions/apps/a-game
blender --version
python tests/run_tests.py --suite fast
blender --background --factory-startup --python-exit-code 1 --python docs/animation_work_status/bollywood_solo_evidence/verify_preserved.py
```

After an explicit user instruction to resume animation work, reopen a saved source with Player Asset Export enabled, or use the shared authoring scene for the unfinished motifs:

```sh
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
blender --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/bollywood/author.py -- --moves lotus_open jhumka filmi_point diagonal_reach offering_sweep ready namaste wide_open tribhanga ready_to_namaste namaste_to_ready --characters Man Woman
blender --background animations/man_and_woman/bollywood_man_snake_arms.blend --python-exit-code 1 --python scripts/bollywood/surface_review.py
blender --background animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/bollywood/render_review.py -- --character Woman --frame 24
```

Update the audit's expected count and storage exceptions after newly authorized assets exist. Read actual binary sizes and Git attributes before staging; store each file at or below 104,857,600 bytes directly in Git, with exact intended-file exceptions. Rebase/merge the latest origin/main while preserving the union of animation-update resource references and concurrent documentation additions. Use ordinary pushes. Git history supplies the final preservation, documentation, and integration hashes; the delivery response reports them after remote verification.

## Integration verification update

The preservation commit was rebased onto `18e528c73` (latest origin/main at the first integration fetch), yielding task commit `0761b5973bc672b4abb5ab7327421f4eeed28858`. The source-directory `.gitattributes` conflict was resolved by retaining the exact-name exceptions from both tasks. Concurrent action sources and documentation remain present.

Main now includes `scripts/blender/install_animation_tools.py` and bundled Game Rig Tools. Future resumed authoring should install this checkout's tools before opening sources, using the same Blender profile throughout. This integration adds tooling availability; the preserved task's existing bakes remain the native Blender visual-bake outputs.

Post-rebase required fast suite: **10/10 pass in 6.32 seconds**. Main added a tenth required fast check. `python scripts/lfs_policy.py check` passed for all **23,494** staged repository files. Task binaries remain full Git blobs with the measured hashes and exact-name storage exceptions. No newly authored task asset requires a Git LFS upload.

A fresh-process saved-source diagnostic on Woman snake arms found a concrete editable-source compatibility issue: `f_index.01.L` and `f_middle.01.L` load in `QUATERNION` mode while this task's authored finger curves use `rotation_euler`. The generator makes this temporary rotation-mode change across its finger controls; the shared rig retains quaternion modes on reload. Therefore the editable sources' authored finger curls require compatibility repair and saved-source playback review when work resumes. The existing bakes/export capture the in-memory pose before reload; their preserved output hashes remain unchanged. Treat all 30 source families as provisional until the finger channels are repaired through authorized resumed authoring and the resulting bake/export is revalidated. This issue was recorded after the stop; animation assets were preserved as requested.

Additional evidence files: `post_rebase_fast_suite.log` and `reloaded_finger_modes.log`. The Animation instructions now document independent solo roles, reuse of disco posing helpers, and preservation records for stopped tasks. A separate documentation commit records those lessons.

Integration onto `98440a92c` preserved both chats' Animation instructions, exact-path storage rules, and the union of 48 animation-update references. Required fast checks passed **10/10 in 5.84 seconds** on the resolved integration tree. All **120** preserved source, GLB, import, and report hashes matched the preservation audit after integration. The staged repository storage check passed for **24,132** files. `integration_fast_suite.log` retains this final fast-suite result. The delivered task uses ordinary Git blobs for its 61 binaries; the ordinary push carries their asset payloads. Git history and the delivery response supply the final merge hash and remote verification.

The first ordinary push received a concurrent-update rejection. Fetching `8648f10ee` and merging its newer main preserved all incoming instructions and the union of **58** active animation-update references. The repeated fast suite passed **10/10**; `push_retry_fast_suite.log` retains its result. The repository LFS policy check passed for **24,280** staged files before adding this retry evidence. Integration uses ordinary merges and pushes and retains the previously recorded task commits.
