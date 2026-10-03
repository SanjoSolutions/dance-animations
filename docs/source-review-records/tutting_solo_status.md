# Tutting animation work status — stopped for delivery

- Recorded: 2026-10-02T17:05:56+02:00 (Europe/Berlin). Stop instruction received on October 2, 2026; owned animation processes were terminated at approximately 17:01 local time.
- Chat/task title: Tutting solo animations for man_and_woman3.blend (descriptive task title; the UI chat title is unavailable in this context).
- Project: A-Game, `apps/a-game`, sanjo-solutions cloud environment.
- Task branch: `animation/tutting`.
- Commit at the stopping point: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Original scope: a broad solo tutting repertoire for both characters, Blender 5.2 authoring/rendering/export, per-animation sources, natural movement/contact/clearance/loop review, Git storage through 100 MiB, commits/rebase, Animation guidance, integration into main and push.
- Current directive: preserve and deliver the present state. Animation authoring, refinement, baking and rendering stopped. Resume animation work when the user authorizes it.

## Completion and limitations

**This is preserved work in progress: procedural dance studies, not a finished production repertoire.**

There are 24 separately named solo clips per character: eight held position studies and sixteen movement phrases. All 48 have editable control actions, matching `.baked` actions in individual Blender sources, and single-clip GLB exports. The original combined library and shared scene remain unchanged; Player Asset Export discovers the individual sources when reopening the combined library.

Fourteen sources completed the corrected native bake, export and reopened-source verification: all eight Man position studies and six Woman position studies. `tutting_man_arm_wave` was separately corrected, rebaked and exported, with source-motion checks passing; its corrected saved-bake parity still needs a rerun. The other 33 files retain the earlier bake and export. Their initial control-endpoint checks passed, but actual deform-hand continuity has a known unresolved risk.

The blocking findings are concrete:

1. Changing finger control rotation modes to Euler did not persist through the shared-scene file workflow. Every current source was regenerated with quaternion finger keys; the earlier Euler versions were replaced.
2. The shared `Natural Wrist Rotation` Euler limiter produces a deform-hand flip during certain palm turns while the IK/ORG hand remains smooth. In the original Man arm-wave study, frames 37.5, 62.5 and 85.5 showed large baked/interpolated errors, up to 0.1961 m at a fingertip and about 1.3973 radians. The task-local scripts now use the existing per-action `animation_wrist_constraint=false` setting with a measured quaternion comfort cone. Fifteen saved files contain that setting; only fourteen completed the full verification pass before stopping.
3. Native visual baking preserves a small existing control/deform rest-length difference near toes. The verifier allows 0.01 m positional and 0.06 radian rotational source/bake differences while separately requiring planted baked feet within 0.002 m. This tolerance is explicit; the two rigs are not reported as exactly identical.
4. Clearance checks use an elliptical torso envelope and hand segments. They complement rendered geometry review; full mesh/finger intersection review remains pending. Earlier front/side renders and a Man repertoire sheet are preserved as **pre-final-refinement evidence**, not approval of the final saved state.
5. Game Rig Tools is unavailable in this cloud Blender profile. The task uses Blender 5.2.2's native visual baking API plus the repository's `AnimationFileWriter`, `AnimationClipScene`, glTF options and `AnimationUpdates` interfaces. Future normal panel baking requires the optional add-on and its configured rig pairs.

## Files and assets

Every exact source/export path, SHA-256, byte size, participant, frame range and wrist setting is recorded in [asset_inventory.json](tutting_evidence/asset_inventory.json). Each source contains one authoring action and its matching `.baked` action. Import settings sit beside each GLB as `.glb.import`. `models/player/animation_updates.tres` references all 48 new clips and preserves the six existing update entries.

- `scripts/tutting/repertoire.py`: named geometry, position studies and phrase specifications.
- `scripts/tutting/author.py`: sparse IK authoring, quaternion wrist correction, native visual baking and per-animation publication. The script includes the intended wrist fix beyond the state of the 33 earlier binaries.
- `scripts/tutting/validate.py`: half-frame contact, joint, clearance-proxy, deform-hand-step and loop checks.
- `scripts/tutting/verify_sources.py`: reopen sources, compare all deform bones at integer/half frames, check baked foot plants and exported skeleton paths/rest transforms.
- `scripts/tutting/refresh_bakes.py`: apply the per-clip wrist choice, rebake/export existing sources and run saved-source verification; this was the interrupted operation.
- `scripts/tutting/preview.py`, `render_sheet.py`: Blender clay render utilities; execution stopped.
- `scripts/tutting/verify_imports.gd`: read imported libraries and verify 48 solo roles and forward-loop settings; full execution remains pending after a fresh import.
- `scripts/tutting/README.md`: repertoire/workflow guide, with this status taking precedence for completion claims.
- `docs/animation_work_status/tutting_evidence/`: asset inventory, per-clip initial reports, partial final reports, existing PNG review renders and captured logs. `validation_man.json` has eight completed clips; `validation_woman.json` has six. Per-clip JSON files from the initial generation use the earlier control-only check and are explicitly superseded by those final reports where present.
- Exact-file `.gitattributes` entries beside sources, exports and evidence images place all task binaries in ordinary Git. All are at most 104,857,600 bytes. The largest source/export is 1,177,771 bytes. Shared repository storage rules remain intact.

### Per-clip saved state

All ranges are inclusive at 24 fps. Man sources use `PLAYER`; Woman sources use `PARTNER`. Moving phrases return to the ready stance; position studies hold one shape. “Initial bake” marks the 33 clips awaiting actual deform continuity review. “Verified” refers to the completed saved-source checks, not final artistic approval.

| Clip | Frames | Role | Authored / baked / exported state |
| --- | --- | --- | --- |
| `tutting_man_arm_wave` | 0–124 | PLAYER | Keyed study / corrected bake, parity pending / GLB written |
| `tutting_man_box_expansion` | 0–100 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_box_trace` | 0–148 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_combination` | 0–268 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_diamond_expansion` | 0–100 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_egyptian_switches` | 0–100 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_elbow_hinges` | 0–124 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_face_frame_isolation` | 0–100 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_finger_boxes` | 0–124 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_finger_fan` | 0–172 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_level_changes` | 0–124 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_palm_flips` | 0–148 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_position_diamond` | 0–28 | PLAYER | Keyed study / corrected bake verified / GLB verified |
| `tutting_man_position_egyptian` | 0–28 | PLAYER | Keyed study / corrected bake verified / GLB verified |
| `tutting_man_position_face_frame` | 0–28 | PLAYER | Keyed study / corrected bake verified / GLB verified |
| `tutting_man_position_goalpost` | 0–28 | PLAYER | Keyed study / corrected bake verified / GLB verified |
| `tutting_man_position_low_box` | 0–28 | PLAYER | Keyed study / corrected bake verified / GLB verified |
| `tutting_man_position_reverse_egyptian` | 0–28 | PLAYER | Keyed study / corrected bake verified / GLB verified |
| `tutting_man_position_stack` | 0–28 | PLAYER | Keyed study / corrected bake verified / GLB verified |
| `tutting_man_position_tabletop` | 0–28 | PLAYER | Keyed study / corrected bake verified / GLB verified |
| `tutting_man_stack_exchange` | 0–100 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_staircase` | 0–148 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_thread_and_unthread` | 0–124 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_man_wrist_quarter_turns` | 0–124 | PLAYER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_arm_wave` | 0–124 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_box_expansion` | 0–100 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_box_trace` | 0–148 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_combination` | 0–268 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_diamond_expansion` | 0–100 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_egyptian_switches` | 0–100 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_elbow_hinges` | 0–124 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_face_frame_isolation` | 0–100 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_finger_boxes` | 0–124 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_finger_fan` | 0–172 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_level_changes` | 0–124 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_palm_flips` | 0–148 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_position_diamond` | 0–28 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_position_egyptian` | 0–28 | PARTNER | Keyed study / corrected bake verified / GLB verified |
| `tutting_woman_position_face_frame` | 0–28 | PARTNER | Keyed study / corrected bake verified / GLB verified |
| `tutting_woman_position_goalpost` | 0–28 | PARTNER | Keyed study / corrected bake verified / GLB verified |
| `tutting_woman_position_low_box` | 0–28 | PARTNER | Keyed study / corrected bake verified / GLB verified |
| `tutting_woman_position_reverse_egyptian` | 0–28 | PARTNER | Keyed study / corrected bake verified / GLB verified |
| `tutting_woman_position_stack` | 0–28 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_position_tabletop` | 0–28 | PARTNER | Keyed study / corrected bake verified / GLB verified |
| `tutting_woman_stack_exchange` | 0–100 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_staircase` | 0–148 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_thread_and_unthread` | 0–124 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |
| `tutting_woman_wrist_quarter_turns` | 0–124 | PARTNER | Keyed study / initial bake / GLB written; refinement pending |

## Verification performed

- Blender version: **5.2.2 LTS**, build `d13f752e3b9c`. All Blender authoring, scripting, rendering, baking and export used this executable.
- `GODOT=/workspace/.cloud-onboarding/bin/godot python tests/run_tests.py --suite fast`: **9/9 passed** after stopping; see `tutting_evidence/fast_final.txt`.
- A read-only Blender inventory loaded all 48 source action families and parsed all 48 GLBs: **passed**, exact roles/ranges/hashes in the inventory. Both action slots and single-clip GLB identities were checked. This establishes file integrity, not full motion correctness.
- `blender -b --python-exit-code 1 --python scripts/tutting/refresh_bakes.py -- --character man`: **8/24 completed and verified**, then terminated during the next clip's pre-bake check.
- Corresponding `--character woman`: **6/24 completed and verified**, then terminated during the next clip's pre-bake check.
- Corrected Man arm-wave source check: passed, maximum half-frame deform-hand rotation step approximately 0.142 rad; its separate pilot rebake/export completed. Saved-source verification of that corrected pilot remains pending.
- A Woman Egyptian-switches pilot previously passed saved-source verification with the earlier limiter: maximum bake position error 0.007557 m, rotation error 0.047393 rad and baked-foot drift below 0.000001 m. It was not part of the completed final refresh run and remains in the initial-bake group.
- Godot import probe for the Woman Egyptian-switches pilot: one animation, 630 tracks, 4.166667-second length, forward loop, `Woman_rigify_deform/Skeleton3D` binding; passed at that point. Full refreshed import verification remains pending.
- The broad related selection (`python tests/run_tests.py --suite changed --changed animations/man_and_woman/tutting_man_position_goalpost.blend`) selects **57 slow checks**. Runs were interrupted during generation/refinement. The last used Godot 4.7.2 and `--slow-timeout 45`; it had resource-loading errors and timeouts while animation updates lacked fresh import caches. It did **not** complete and is **not** claimed to pass. Captured output is `tutting_evidence/related3.txt`. Rerun after final asset refresh/import. Earlier attempts used a default Godot 4.6.3 and then 4.7.2; the documented resume command selects 4.7.2.

The initial fast-suite failure came from three LFS-pointer hair meshes and was resolved by hydrating them. The final fast suite is clean. The environment's Game Rig Tools prerequisite remains unresolved for tests that require it.

## Processes and preserved outputs

Owned Blender refresh processes (PIDs 4274 and 4370), the slow-suite runner (3354) and its child Godot process (4462) were terminated on the stop instruction. The build and render processes had already completed. No task authoring/rendering process remains active. Defunct process entries may remain under the container init; they perform no work.

The interrupted refreshes had not overwritten the next source: Man Egyptian switches and Woman stack retain their initial wrist setting. Fifteen corrected files are identified by the inventory. Existing temporary logs and `.cache/tutting/` remain in the originating workspace; durable evidence was copied to the tracked task evidence directory. Generated temporary GLBs duplicate the published exports. Three unrelated UID rewrites caused by the Godot editor import were reverted to preserve task scope.

## Remaining work and exact resume commands

Start in `/workspace/sanjo-solutions/apps/a-game` on a fresh task branch based on current `origin/main`. Hydrate linked Blender sources when needed. Run these only after animation work is authorized again:

```sh
blender --version
blender -b --python-exit-code 1 --python scripts/blender/install_animation_tools.py
blender -b --python-exit-code 1 --python scripts/tutting/refresh_bakes.py -- --character man
blender -b --python-exit-code 1 --python scripts/tutting/refresh_bakes.py -- --character woman
blender -b --python-exit-code 1 --python scripts/tutting/verify_sources.py
blender -b animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/tutting/render_sheet.py
/workspace/.cloud-onboarding/bin/godot --headless --editor --path . --import
/workspace/.cloud-onboarding/bin/godot --headless --path . --script scripts/tutting/verify_imports.gd
GODOT=/workspace/.cloud-onboarding/bin/godot python tests/run_tests.py --suite fast
GODOT=/workspace/.cloud-onboarding/bin/godot python tests/run_tests.py --changed animations/man_and_woman/tutting_man_position_goalpost.blend
```

Keep the two refresh commands sequential because both publish the shared update registry. Review every failure before continuing. Confirm both partial report files have 24 clips, then let the full verifier write `scripts/tutting/validation.json`. Review full motion and finger/skin clearance in Blender; finish natural-motion refinement as indicated. The vocabulary is broad and finite: evolving tutting improvisations are not exhaustively represented. Reinspect sizes and attributes before staging further generated binaries, with Git LFS reserved for files above 100 MiB.

## Delivery record

After integration preparation, the updated fast suite passed **10/10** in 6.00 seconds (`tutting_evidence/fast_rebased.txt`); `python scripts/lfs_policy.py check` verified all 24,092 staged files (`tutting_evidence/lfs_policy.txt`). Animation assets remained frozen.

The preservation commit was rebased onto fetched `origin/main` at `3f2039a5a4728878ca60db2f81ec9bb265d74a04`. The add/add conflict in the source-directory `.gitattributes` was resolved by retaining both tasks' exact-file entries. The new upstream includes bundled Blender animation tooling; the resume command above now uses `scripts/blender/install_animation_tools.py`. Game Rig Tools unavailability describes the authoring profile at the stop, and the bundled installer provides the next setup step. Motion verification above records the stopped task's original shared-scene baseline; it was not rerun against concurrently integrated shared libraries during this preservation-only delivery.


This status and the preserved task assets belong to the task preservation commit. The Animation guidance is committed separately after fetching/rebasing, followed by ordinary integration into main and push. Final commit hashes and remote-main verification are reported in the chat because a commit cannot contain its own hash. GitHub commit authorship and communications are identified as Codex, with exactly one requested co-author trailer per newly created commit.

Integration into current main at `3b81a0665` retained both chats' Animation guidance and storage exceptions. The runtime registry was merged as the union of all 103 clip references, including the 48 preserved tutting studies.

The final integration fast suite passed **10/10** in 5.93 seconds (`tutting_evidence/fast_merged.txt`). The storage-policy check passed for all 24,472 staged files after resolving the concurrent registry and attribute updates.

An ordinary push rejection required integration of concurrent `origin/main` at `4fa0d077e`. The three-way registry merge retained all 181 clip references and all current storage entries. Fast verification again passed **10/10** in 6.45 seconds (`tutting_evidence/fast_retry.txt`), the storage policy passed for 25,345 staged files, and all 96 frozen source/export SHA-256 values matched the stop inventory.
