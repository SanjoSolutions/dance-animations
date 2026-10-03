# Partner cha-cha-cha: preserved partial work

Recorded by Codex on 2026-10-02; animation work stopped at 15:02:01 UTC (17:02:01 Europe/Berlin) on the user's coordinated stop instruction.

- Chat/task title: Partner cha-cha-cha animation task. The exact sidebar title was outside the thread tool's 50-item retrieval window; this descriptive title identifies the original request.
- Environment: sanjo-solutions cloud, project A-Game, `/workspace/sanjo-solutions/apps/a-game`.
- Task branch at stop: `codex/partner-cha-cha`.
- HEAD at stop: `3c52737c74b488501e9cfe47e7029547c6f5fe88`. Task changes were working-tree changes at that point.
- Delivery state: preservation snapshot, **partial procedural blocking studies**. This record supersedes completion implications in the original repertoire draft.

## Original scope and preserved result

The original request was a broad coordinated Partner cha-cha-cha repertoire for both characters in `man_and_woman3.blend`, with natural motion, planted contacts, body clearance, smooth transitions, interpolated checks and loop continuity, reused suitable motion, Blender 5.2 throughout, per-animation sources, documentation, commits, integration and push.

The recipe defines 64 clips: 36 figures, 10 positions and 18 directed transitions. **63 authored source files exist**; `partner_cha_cha_transition_promenade_to_open.blend` is missing after an IK reach failure. All sources are editable partial studies, with **zero baked runtime actions and zero GLB/runtime exports**. They have paired Man lead / Woman follow control-rig slots and NLA binding metadata. Role-reversed versions were not authored. Dance-expert review and full visual acceptance remain outstanding; figure labels describe the procedural intent rather than a certified syllabus.

Blender **5.2.2 LTS**, build `d13f752e3b9c`, executable `/workspace/tools/blender-5.2.2-linux-x64/blender`, was used for all authoring, scripting, validation and rendering. The system Blender 4.3.2 was discovered by version inspection and was not used for animation work.

The controls reuse `RigYogaPoser`, `YogaPoseLibrary`, `DiscoWristPoser`, paired calibrated palm targets, `PoseSolver`, `ActivityMotionAuthor.write_samples`, `AnimationTracks`, and `AnimationFileWriter`. Existing disco posing/wrist treatment was reused; these footfalls and partner routes are new procedural recipes. Sparse lift, apex, landing and hold keys drive world-space ankle targets, torso weight shift and shared hand targets with native wrist constraints.

## Files and authored/baked/exported state

All paths below are relative to `apps/a-game/`.

| File or group | Preserved purpose/state |
| --- | --- |
| `scripts/partner_cha_cha_choreography.py` | Planned repertoire, formations, footwork and support intervals; latest recipe can differ from saved clips. |
| `scripts/create_partner_cha_cha.py` | Blender author, split source writer, selective regeneration/hand refinement and catalog assembly; intermediate work. |
| `scripts/validate_partner_cha_cha.py` | Saved-file structural and interpolated motion checks, sampled surface checks and review rendering. |
| `scripts/test_partner_cha_cha_choreography.py` | Four support, timing, loop stance and stationary-foot tests. |
| `scripts/partner_cha_cha.md` | Authoring guide, amended to identify the paused partial state and future-only rebuild commands. |
| `animations/man_and_woman/.gitattributes` | Exact filename ordinary-Git rules for the 64 intended sources; existing shared-source storage retained. |
| `docs/animation_work_status/partner_cha_cha_evidence/saved_source_inventory.json` | Read-only Blender inventory: actual frame ranges, roles, slots, pose frames, markers, formations, source sizes and SHA-256. |
| `docs/animation_work_status/partner_cha_cha_evidence/validation_by_saved_hash.json` | Existing validation records matched against preserved binary SHA-256; null means current content lacks a matching record. |
| `docs/animation_work_status/partner_cha_cha_evidence/inspect_saved_sources.py` | Read-only inventory check; never saves or changes a Blender source. |
| `docs/animation_work_status/partner_cha_cha_evidence/prior_work/` | Preserved prior logs, partial JSON report, 90 individual PNG review frames, three JPG contact sheets, one eleven-pose open-basic PNG strip and its frame-fraction JSON. Images represent earlier iterations and are visual evidence, not acceptance of every current binary. |
| `docs/animation_work_status/partner_cha_cha_evidence/delivery_*.log` | Stop-time structural and test verification results. |

The shared scene, combined library, anatomical character sources, dildo source and disco source were fetched from existing LFS objects and remain unchanged. The three hair physics mesh resources needed by fast tests were also fetched, retaining their existing storage. No shared rig edits belong to this task. Temporary diagnostic scripts and profiling data remain in ignored `.cache/partner_cha_cha/`; their useful logs and all existing review images are preserved under `prior_work/`.

### Source inventory

Every entry below is authored partial source, baked **no**, exported **no**, Man lead / Woman follow, at **24 fps and 120 BPM**. Frames 12, 24, 36, 42 and 48 carry the first 2, 3, 4, &, 1 sequence. Loop playback omits the duplicate final frame. Once clips include their last frame. Filenames all live under `animations/man_and_woman/` and begin `partner_cha_cha_`.

**Dependency scope:** all preserved motion checks ran against the shared scene and character revisions at stop-time HEAD `3c52737c74b488501e9cfe47e7029547c6f5fe88`. Concurrent main updates changed those dependencies and paired authoring helpers. The matched clip hashes establish historical evidence, not acceptance of playback with the newer dependencies. See `partner_cha_cha_evidence/dependency_revisions.json`; revalidate against the integrated dependencies on authorized resumption.

“Pass” covers the recorded samples and tolerances only. “Pending” includes sources whose earlier results predate the preserved binary. All 63 sources passed structural readback after stopping.

| Filename suffix (`.blend`) | Stored frames | Playback end / mode | Bytes | Current-hash motion check |
| --- | --- | --- | ---: | --- |
| `alemana` | 0–192 | 192 / once | 200340 | Pass |
| `chase` | 0–384 | 383 / loop | 293070 | Pending |
| `closed_basic` | 0–96 | 95 / loop | 152849 | Pass |
| `closed_hip_twist` | 0–192 | 192 / once | 205013 | Pass |
| `compact_chasse` | 0–96 | 95 / loop | 144456 | Pending |
| `cross_body_lead` | 0–384 | 384 / once | 303561 | Pending |
| `cuban_breaks` | 0–96 | 95 / loop | 150462 | Pending |
| `curl` | 0–192 | 192 / once | 197581 | Pass |
| `fan` | 0–192 | 192 / once | 200517 | FAIL: body_surface_overlap |
| `follow_my_leader` | 0–192 | 191 / loop | 175643 | Pending |
| `forward_and_backward_locks` | 0–96 | 95 / loop | 150582 | Pending |
| `hand_to_hand` | 0–192 | 191 / loop | 210447 | Pending |
| `hip_twist_chasse` | 0–96 | 95 / loop | 148225 | Pending |
| `hockey_stick` | 0–192 | 192 / once | 193762 | FAIL: body_surface_overlap |
| `in_place_basic` | 0–96 | 95 / loop | 140576 | Pending |
| `left_and_right_chasses` | 0–96 | 95 / loop | 149319 | Pending |
| `natural_top` | 0–384 | 384 / once | 334466 | Pass |
| `new_york_left` | 0–192 | 191 / loop | 213308 | Pending |
| `new_york_right` | 0–192 | 191 / loop | 212444 | Pending |
| `open_basic` | 0–96 | 95 / loop | 149533 | Pass |
| `open_hip_twist` | 0–192 | 192 / once | 199015 | Pass |
| `position_closed` | 0–96 | 95 / loop | 125595 | Pending |
| `position_counter_promenade` | 0–96 | 95 / loop | 126134 | Pending |
| `position_double_hand` | 0–96 | 95 / loop | 125088 | Pending |
| `position_fan` | 0–96 | 95 / loop | 125151 | Pending |
| `position_open` | 0–96 | 95 / loop | 125004 | Pending |
| `position_promenade` | 0–96 | 95 / loop | 125988 | Pending |
| `position_right_hand` | 0–96 | 95 / loop | 126146 | Pending |
| `position_shadow` | 0–96 | 95 / loop | 124766 | Pending |
| `position_side_by_side` | 0–96 | 95 / loop | 125178 | Pending |
| `position_tandem` | 0–96 | 95 / loop | 124630 | Pending |
| `reverse_top` | 0–384 | 384 / once | 332850 | Pass |
| `ronde_chasse` | 0–96 | 95 / loop | 150125 | Pending |
| `rope_spinning` | 0–384 | 384 / once | 251801 | Pass |
| `shoulder_to_shoulder` | 0–192 | 191 / loop | 214405 | Pending |
| `side_basic` | 0–96 | 95 / loop | 148510 | Pending |
| `spiral` | 0–192 | 192 / once | 193003 | Pass |
| `split_cuban_breaks` | 0–96 | 95 / loop | 148738 | Pass |
| `spot_turn_left` | 0–192 | 192 / once | 215891 | Pending |
| `spot_turn_right` | 0–192 | 192 / once | 214423 | Pending |
| `sweetheart` | 0–384 | 383 / loop | 244744 | Pass |
| `three_cha_chas` | 0–192 | 191 / loop | 178025 | Pending |
| `time_steps` | 0–96 | 95 / loop | 148577 | Pass |
| `transition_closed_to_open` | 0–192 | 192 / once | 182187 | Pending |
| `transition_counter_promenade_to_open` | 0–192 | 192 / once | 217479 | Pending |
| `transition_double_hand_to_open` | 0–192 | 192 / once | 175767 | Pending |
| `transition_fan_to_open` | 0–192 | 192 / once | 193731 | Pending |
| `transition_open_to_closed` | 0–192 | 192 / once | 182665 | Pending |
| `transition_open_to_counter_promenade` | 0–192 | 192 / once | 217819 | Pending |
| `transition_open_to_double_hand` | 0–192 | 192 / once | 175150 | Pending |
| `transition_open_to_fan` | 0–192 | 192 / once | 195688 | Pending |
| `transition_open_to_promenade` | 0–192 | 192 / once | 216584 | Pending |
| `transition_open_to_right_hand` | 0–192 | 192 / once | 162448 | Pending |
| `transition_open_to_shadow` | 0–192 | 192 / once | 200260 | Pending |
| `transition_open_to_side_by_side` | 0–192 | 192 / once | 199663 | Pending |
| `transition_open_to_tandem` | 0–192 | 192 / once | 188821 | Pending |
| `transition_right_hand_to_open` | 0–192 | 192 / once | 162927 | Pending |
| `transition_shadow_to_open` | 0–192 | 192 / once | 198981 | Pending |
| `transition_side_by_side_to_open` | 0–192 | 192 / once | 197945 | Pending |
| `transition_tandem_to_open` | 0–192 | 192 / once | 188224 | Pending |
| `turkish_towel` | 0–384 | 383 / loop | 264711 | Pending |
| `underarm_turn_left` | 0–192 | 192 / once | 201019 | Pass |
| `underarm_turn_right` | 0–192 | 192 / once | 199820 | Pass |

## Validation commands and results

Commands were run from the app directory. Full logs are in `partner_cha_cha_evidence/`.

- `python tests/run_tests.py --suite fast`: **10/10 passed** at preservation time (`delivery_fast.log`).
- `python tests/run_tests.py --changed scripts/test_partner_cha_cha_choreography.py`: **11/11 passed**, including the four choreography unit tests (`delivery_related.log`).
- `/workspace/tools/blender-5.2.2-linux-x64/blender -t 2 --background --factory-startup --disable-autoexec --python-exit-code 1 --python docs/animation_work_status/partner_cha_cha_evidence/inspect_saved_sources.py`: **63/63 structural readbacks passed**, two slots, BOTH participants, two NLA bindings, finite keys, matching actual/catalog ranges, original source hashes unchanged (`delivery_inventory.log`). This read-only preservation check generated no animation or render.
- Earlier saved-source composition of `partner_cha_cha_closed_basic.blend` via `scripts/player_assets/animation_file_startup.py` passed with both control rigs (`prior_work/source_composition.log`).
- Earlier `validate_partner_cha_cha.py -- --only ...` runs logged half-frame samples plus exact phase boundaries and nine surface samples per clip. **17 current hashes have records: 15 pass, fan and hockey_stick fail `body_surface_overlap`; 46 current hashes await matching motion validation.** See the table and hash-matched JSON. The stopped figures run reached `sweetheart`; subsequent entries were not completed.
- Motion tolerances in the validator: IK 0.006 m, planted feet 0.008 m, palm spacing 0.035 m, wrist bend 40 degrees, ankle floor offset -0.008 m, body proxy clearance 0 m, loop position 0.0001 m, loop angle 0.001 rad, finite-difference velocity mismatch 0.20 m/s. Surface floor threshold -0.01 m; hand contact regions within 0.13 m are exempted from cross-character overlap detection. These checks do not prove dynamic balance, complete self-collision freedom or natural finger styling.
- An earlier ronde version failed loop velocity (0.304080 m/s); `repair_steps.log` records a later saved ronde, hand_to_hand and new_york_left. Those three current binaries remain pending motion checks.
- Earlier `tests.log` recorded a process-cleanup race in `tests/test_run_tests.py::RunnerOutcomeTest.test_completion_releases_resources_owned_by_descendants` while Blender jobs were running. Stop-time reruns passed. Earlier `fast.log` recorded missing LFS hair meshes, resolved by fetching the existing objects. These older failures are retained rather than represented as current failures.
- `check_optimized.log` used incorrect surface modifier handling and is obsolete. Later checks preserve original anatomical skin modifier enablement and masks; raw helper body meshes are unsuitable for that test.

## Stopped processes and retained outputs

At 15:02:01 UTC, SIGTERM was sent to owned Blender PID 3061 (author/refinement shard 1 of 3) and PID 3432 (figures validator). A subsequent process inspection found no remaining owned author/validator. Author shards 0 and 2 had ended; `repair_steps.log` ends with `Blender quit`. All complete source files and saved review images were preserved; no further animation authoring, refinement, generation or rendering occurred after the stop instruction.

The stopped author used `--refine-hands --rebuild time_steps split_cuban_breaks ronde_chasse hand_to_hand sweetheart turkish_towel position_promenade position_counter_promenade position_side_by_side position_shadow transition_open_to_promenade transition_promenade_to_open transition_open_to_counter_promenade transition_counter_promenade_to_open transition_open_to_side_by_side transition_side_by_side_to_open transition_open_to_shadow transition_shadow_to_open --shard 1 3`. Its final log includes IK failures for `transition_promenade_to_open` (0.01604 m palm error at beat 5) and `transition_open_to_side_by_side` (0.02631 m at beat 11.5). A previous side-by-side file survives that failed rebuild. The author deliberately leaves earlier saved files when a rebuild fails.

The stopped validator used `--only natural_top reverse_top fan hockey_stick alemana closed_hip_twist open_hip_twist spiral curl rope_spinning sweetheart turkish_towel follow_my_leader chase cross_body_lead position_closed position_fan position_shadow position_promenade position_counter_promenade`. Its complete per-clip JSON lines through sweetheart survive in `prior_work/check_figures.log`; it did not write a final report. `prior_work/validation_partial.json` is the last completed subset report, not the interrupted run's complete result.

## Remaining work and concrete blockers

1. Continue only after renewed authorization. This handoff fulfills the immediate preservation request; final animation quality remains incomplete.
2. Repair missing promenade-to-open IK reach and failed side-by-side reach. Review fan/hockey-stick surface intersections and all pending motions. Inspect both full bodies, wrists, fingers and supports during continuous playback.
3. Reconcile source revisions before rebuilding: the final side-by-side, shadow and counter-promenade transition recipes add release/travel/regrasp phases after some batches had started. Saved sources can reflect older recipes. The final hand-to-hand and ronde recipes were saved by `repair_steps`; subsequent validation was stopped.
4. Rebuild affected clips, validate their exact binary hashes and review transitions visually. A sparse pose solution or endpoint pass alone is insufficient.
5. Produce the missing 64th source, then the consolidated catalog and full validation report. `animations/man_and_woman/partner_cha_cha_catalog.json` and `partner_cha_cha_validation.json` have not been delivered.
6. Runtime baking/export remains a separate stage through Bake & Export Active Animation if requested. Preserve source baked actions and report export receipts.

## Exact future resume commands

These commands are recorded for a future authorized continuation. They were **not executed after the stop**. First inspect this record and hash-matched failures; the current generator can still fail on unresolved reach.

```sh
cd /workspace/sanjo-solutions/apps/a-game
export BLENDER=/workspace/tools/blender-5.2.2-linux-x64/blender
"$BLENDER" --version
# Follow scripts/blender/README.md for a consistent isolated worker profile.
"$BLENDER" --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
# Retrieve existing source objects when starting in a fresh checkout:
git lfs pull --include='apps/a-game/animations/man_and_woman/shared_scene_data.blend,apps/a-game/man_anatomical_study.blend,apps/a-game/woman_anatomical_study_speculum.blend,apps/a-game/dildo.blend,apps/a-game/animations/man_and_woman/solo_disco_dance.blend'
# After repairing the documented reach/clearance problems:
"$BLENDER" -t 2 --background animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/create_partner_cha_cha.py -- --only transition_promenade_to_open transition_open_to_side_by_side transition_side_by_side_to_open transition_open_to_shadow transition_shadow_to_open transition_open_to_counter_promenade transition_counter_promenade_to_open fan hockey_stick
"$BLENDER" -t 2 --background animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/create_partner_cha_cha.py -- --catalog-only
"$BLENDER" -t 2 --background animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_partner_cha_cha.py -- --render .cache/partner_cha_cha/review
python tests/run_tests.py --suite fast
python tests/run_tests.py --changed scripts/test_partner_cha_cha_choreography.py
```

## Storage and integration

The 63 source binaries total **11,741,830 bytes**, largest **334,466 bytes**. Existing review images also fit the 104,857,600-byte ordinary-Git threshold. Exact source filename exceptions and evidence-directory image exceptions keep these task files in ordinary Git; shared scenes retain LFS. A durable evidence file manifest records actual sizes and SHA-256. Pre-staging checks inspect actual bytes and `git check-attr`; staged-blob checks compare source hashes with this inventory. No new LFS objects or separate runtime asset uploads belong to this task.

The delivery procedure commits the preservation snapshot, fetches and rebases onto current origin/main, adds the original request's Animation guidance in a separate documentation commit, fetches again immediately before integration, merges into main preserving concurrent work, and uses ordinary pushes. Commit hashes and verified remote-main result are reported in the chat after delivery; the stop-time HEAD above is immutable provenance rather than a prediction of the delivery hash. GitHub commit communications are authored by Codex and carry exactly one required Co-authored-by trailer.

### Integration verification

The preservation commit was rebased onto `629cffdc1` as `41d7de617`. The `.gitattributes` conflict retained every concurrent entry and added 65 cha-cha comment/rule lines. After this rebase, the fast suite passed **10/10** and the related suite passed **11/11**; logs are `delivery_integrated_fast.log` and `delivery_integrated_related.log`. The root `python scripts/lfs_policy.py check` passed for 24,605 indexed files. The separate documentation update adds the paused-library and surface-modifier guidance to `# Animation` in `AGENTS.md`; evidence has `.gdignore` to keep historical reviews outside Godot asset import discovery. Further concurrent integration is reported with the final push result.

The final integration fetched main `6f1f50a35dd509bf956aedf81c0f29a6e2ad0cfb` and retained both sides of the additive AGENTS.md and storage-attribute conflicts. The dependency revision manifest records the changed shared assets; motion validation against that new scene remains pending.

Merged-tree fast verification passed **10/10** (`delivery_merged_fast.log`); the storage policy check passed for 27,704 indexed files before final evidence staging.
