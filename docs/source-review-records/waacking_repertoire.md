# Waacking repertoire — stopped partial animation study

- Date: 2026-10-02 (Europe/Berlin).
- Chat title / task label: Waacking solo animations for man_and_woman3.blend.
- Branch at freeze: `codex/waacking-repertoire`.
- Baseline commit at freeze: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Project: A-Game, `/workspace/sanjo-solutions/apps/a-game`, sanjo-solutions cloud environment.
- Disposition: user-directed stop. Preserve the current state; further authoring, generation, refinement, and rendering require a new instruction to resume.
- Readiness: **partial procedural animation study; saved-bake fidelity is blocked**. These assets represent candidate motion, with passing author-session measurements and a failing independent saved-source comparison.

## Original scope and stopping point

The original request covered a broad Waacking repertoire for both characters, with independent solo roles, natural motion, planted contacts, clearance, smooth transitions, interpolated and loop validation, reuse of suitable existing motion, per-animation files, and Blender 5.2 throughout. It also requested commits, integration with concurrent main, an Animation-section documentation update, asset publication, and a verified push.

The procedural catalog contains 31 movement specifications (62 intended solo clips): eight rotations, four wraps, five accents, six positions, four footwork patterns, two rocking turns, and two combined phrases. Eight rotations for both roles reached authored, baked, and GLB-exported candidate state. The remaining 23 specifications per role exist only in Python and have zero completed source/export assets.

Work stopped during diagnosis of fractional-frame deform twist. `MCH-upper_arm_tweak.L.001` blends the upper-arm and forearm tweak transforms at influence 0.5; the source deform twist changes sharply between frames 60.5 and 60.75 in the focused example. The native bake interpolates this transition differently. Further motion and rig refinement stopped immediately on the user's stop instruction.

## Exact preserved assets

Each source below contains one authoring action and its `.baked` action, with a single actor slot per action, using `shared_scene_data.blend`. Names begin `waacking_man_` or `waacking_woman_`; roles are `PLAYER` (Man) and `PARTNER` (Woman). Each clip spans frames **0–96 inclusive**, at **24 fps / 120 BPM**, with frame 96 repeating frame 0 (4 seconds). Source controls use sparse pose keys at three-frame intervals and one initial key for constant channels; settled boundary keys were added at 1 and 95. Native visual bakes sample integer frames. Individual import settings select looping playback.

Every row is **authored candidate / baked candidate / exported candidate**, rather than an accepted animation. `models/player/animation_updates.tres` retains the concurrent main registry. During final integration, the 16 provisional Waacking GLBs and their import settings were moved unchanged into the task evidence directory, covered by `.gdignore`. The pre-integration registry is preserved as `waacking_repertoire_evidence/provisional_animation_updates.tres`. These candidates are excluded from active runtime publication.

| Character | Movement | Blender source | GLB export |
| --- | --- | --- | --- |
| Man | alternating | `animations/man_and_woman/waacking_man_alternating.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_man_alternating_baked_7db64b6a52ca.glb` |
| Man | backward_single_left | `animations/man_and_woman/waacking_man_backward_single_left.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_man_backward_single_left_baked_85978e77cf30.glb` |
| Man | backward_single_right | `animations/man_and_woman/waacking_man_backward_single_right.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_man_backward_single_right_baked_4de856994524.glb` |
| Man | double_backward | `animations/man_and_woman/waacking_man_double_backward.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_man_double_backward_baked_5bc81fa089f0.glb` |
| Man | double_forward | `animations/man_and_woman/waacking_man_double_forward.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_man_double_forward_baked_f7862f03309a.glb` |
| Man | forward_single_left | `animations/man_and_woman/waacking_man_forward_single_left.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_man_forward_single_left_baked_47bc0a93fd24.glb` |
| Man | forward_single_right | `animations/man_and_woman/waacking_man_forward_single_right.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_man_forward_single_right_baked_b9e3103706c0.glb` |
| Man | windmill | `animations/man_and_woman/waacking_man_windmill.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_man_windmill_baked_a4d77eea72a1.glb` |
| Woman | alternating | `animations/man_and_woman/waacking_woman_alternating.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_woman_alternating_baked_9b02180ce0d4.glb` |
| Woman | backward_single_left | `animations/man_and_woman/waacking_woman_backward_single_left.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_woman_backward_single_left_baked_7a426551558a.glb` |
| Woman | backward_single_right | `animations/man_and_woman/waacking_woman_backward_single_right.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_woman_backward_single_right_baked_9d4de8705e8e.glb` |
| Woman | double_backward | `animations/man_and_woman/waacking_woman_double_backward.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_woman_double_backward_baked_487d6425be15.glb` |
| Woman | double_forward | `animations/man_and_woman/waacking_woman_double_forward.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_woman_double_forward_baked_8a1636d150a9.glb` |
| Woman | forward_single_left | `animations/man_and_woman/waacking_woman_forward_single_left.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_woman_forward_single_left_baked_a3fba23b3a14.glb` |
| Woman | forward_single_right | `animations/man_and_woman/waacking_woman_forward_single_right.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_woman_forward_single_right_baked_aacfb253e185.glb` |
| Woman | windmill | `animations/man_and_woman/waacking_woman_windmill.blend` | `docs/animation_work_status/waacking_repertoire_evidence/provisional_exports/waacking_woman_windmill_baked_8d19799adf0a.glb` |

Each GLB has a matching `.glb.import`. Each source has an author-session report at `scripts/waacking/review/<source_stem>.json`. The reports describe sampled evaluated controls; they establish neither saved-file correctness nor full mesh collision clearance.

**Mixed revisions:** only `waacking_man_forward_single_left` was rebuilt with the latest preserved finger-mode correction and shoulder-following outward elbow pole. The other 15 files predate these changes. Their inherited disco helper changes finger controls to Euler mode while the shared source uses quaternion mode, so a fresh source open can differ from the original authoring session. All 16 need a deliberate rebuild after resolving the blockers. The generator's `--resume` option checks existence and a passing author-session report, not a source-code revision hash; using it now would retain stale candidates.

## Code, manifests, and evidence

- `scripts/waacking/choreography.py`: 31-entry vocabulary and procedural poses. Reuses the disco step-touch trajectory and the existing yoga stance foundation. Wraps, accents, positions, footwork, turns, and phrases remain procedural specifications.
- `scripts/waacking/build.py`: Blender 5.2 version guard, proportional character posing, sparse authoring, native visual baking, existing `AnimationFileWriter`, `AnimationClipScene`, and `AnimationUpdates` publication helpers. Reuses `DiscoCharacter` and its wrist alignment, preserving the shared finger modes in the latest revision. Game Rig Tools was absent in this cloud Blender profile during authoring, so the task used native Blender baking. The subsequent rebase onto `18e528c73` brings the bundled installer at `scripts/blender/install_animation_tools.py`; it was not run during the stopped task.
- `scripts/waacking/validate.py`: 193 half-frame samples per author-session report; foot plants, wrist bend, hand reach, local torso/head proxies, and loop position/orientation/velocity. These checks cover the supplied landmarks and proxy geometry.
- `scripts/waacking/verify_saved_sources.py`: independent saved-source, role-slot, GLB ownership, and fractional-frame bake comparison. Originally named `test_saved_sources.py`; renamed during preservation to keep this failing manual study outside automatic test discovery. Its full-run path expects the planned 62-entry manifest and will fail against the focused manifest.
- `scripts/waacking/render_review.py`: Blender 5.2 CPU Cycles clay review renderer. The Workbench attempt encountered EGL errors and was terminated. Rendering is stopped.
- `scripts/waacking/review/manifest.json`: **focused manifest for Man forward-single-left only**, overwritten by the last focused build; it is not a complete inventory.
- `docs/animation_work_status/waacking_repertoire_evidence/asset_inventory.json`: authoritative frozen binary inventory, exact sizes, SHA-256 values, and partial-state labels.
- `docs/animation_work_status/waacking_repertoire_evidence/storage_attributes_before.txt` and `storage_attributes_after.txt`: effective Git storage attributes before and after file-specific exceptions.
- `docs/animation_work_status/waacking_repertoire_evidence/logs/`: preserved build, render, fast-test, layout, mode, twist, constraint, and failed saved-bake evidence. Historical logs retain their original temporary paths and earlier utility filename.
- `docs/animation_work_status/waacking_repertoire_evidence/diagnostics/waacking_modes.py`, `waacking_constraints.py`, and `waacking_twist.py`: saved inspection scripts; the twist script imports the renamed verification utility. These scripts assume the recorded workspace path.
- `docs/animation_work_status/waacking_repertoire_evidence/previews/waacking_woman_double_forward_000.png`, `_018.png`, `_030.png`, `_042.png`, `_054.png`, `_066.png`, `_078.png`, `_090.png`: eight unchanged earlier candidate clay renders, copied from `.cache/waacking_review/`. They precede the latest focused Man corrections and are review evidence, not acceptance evidence.
- `.gitattributes`: exact-path regular-Git exceptions for the 16 new `.blend`, 16 new `.glb`, and eight preserved `.png` files. Every measured binary is at most 849,822 bytes; aggregate binary size is 21,321,312 bytes. These are below the user's 104,857,600-byte limit. Existing shared and unrelated LFS rules retain their scope.

`man_and_woman3.blend`, `shared_scene_data.blend`, the anatomical models, and existing animation sources retain their original saved contents. Hydrated dependencies include the shared/source/anatomical scenes, `dildo.blend`, the two player model GLBs, and missing hair-mesh test fixtures. Hydration is a checkout prerequisite, not a task asset change. The combined scene discovers the new per-animation sources when reopened with Player Asset Export enabled.

## Validation and known failures

Commands below run from `apps/a-game`.

1. `blender --version`: **Blender 5.2.2 LTS**, hash `d13f752e3b9c`. All authoring, baking, export, and rendering used this executable.
2. Author build: `blender -b -t 4 animations/man_and_woman/shared_scene_data.blend --python scripts/waacking/build.py`. Sixteen candidates reached `COMPLETE` before the build was stopped. Their 193-sample author-session reports pass their configured tolerances. Latest Man forward-single-left: planted-foot error 0.00022077 m, hand reach error 0.00000210 m, wrist bend 14.9589 degrees, loop position/orientation/velocity error 0. These findings concern the evaluated working source.
3. Saved-file check, rerun read-only during preservation: `blender -b -t 4 animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/waacking/verify_saved_sources.py -- waacking_man_forward_single_left`. **FAIL**, exit 1. Largest endpoint error 0.01397244 m at `DEF-elbow-helper.L`, frame 7.5; largest rotation difference 63.1157 degrees at `DEF-upper_arm.L.001`, frame 60.5. Integer-frame maxima: 0.00779795 m and 1.22460 degrees. Required comparison limits remain 0.006 m and 3 degrees. See `logs/stop_verify.log`. Acceptance limits were retained; the failed study is preserved.
4. Raw GLB/model target check: the first Man clip's **214 animated node targets all matched** `models/player/man.glb` (zero missing targets). This establishes target paths for that clip, not gameplay or whole-repertoire acceptance. See `logs/waacking_layout.log`.
5. `python tests/run_tests.py --suite fast`: the initial run was 8/9 because three hair meshes were still LFS pointers; scoped hydration produced 9/9. A later run was 8/9 because the manual Blender comparison had a `test_` filename without a catalog runtime; renaming that utility resolves the discovery issue. The final preservation run passed **9/9** in 5.02 seconds; see `logs/final_fast.log`. Integration checks after rebasing passed **10/10** in 8.03 seconds; see `logs/integration_fast.log`.
6. `python -m py_compile scripts/waacking/*.py`: passed during preservation.
7. Godot import/playback of all candidates, evaluated surface-intersection checks, full saved-source verification, final mesh-motion review, and the remaining repertoire are outstanding. The full slow suite was not run: the task is a stopped asset study with a known failing focused comparison and incomplete source inventory.

## Processes and saved state

At freeze, no owned Blender authoring or rendering processes remained. The earlier all-clip build and failed Workbench render were explicitly terminated; native CPU renders and focused builds had completed. The final preserved verification process finished with the expected assertion failure. Existing outputs are preserved; further generation and rendering are stopped. Python caches and Blender backup files remain ignored working intermediates. Important temporary logs and previews have durable copies under the evidence directory above.

## Resume instructions — only after authorization to resume animation work

Read this status and the inventory first. Use Blender 5.2.2 and keep the existing source files as recovery points. Resolve the Rigify fractional-frame twist and saved-bake fidelity before rebuilding the remaining clips. Confirm source channel rotation modes against freshly loaded shared rigs. Check complete mesh motion and hand/finger clearance after the correction.

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender --version
# For future authoring, install the tools now bundled in the rebased repository:
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
blender -b -t 4 animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/waacking/verify_saved_sources.py -- waacking_man_forward_single_left
blender -b -t 4 animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python docs/animation_work_status/waacking_repertoire_evidence/diagnostics/waacking_twist.py
# After the blocker is resolved and authoring is authorized:
blender -b -t 4 animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/waacking/build.py -- --moves forward_single_left --characters Man
blender -b -t 4 animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/waacking/verify_saved_sources.py -- waacking_man_forward_single_left
# Rebuild all entries, including the older 15 revisions, after focused acceptance:
blender -b -t 4 animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/waacking/build.py
blender -b -t 4 animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/waacking/verify_saved_sources.py
python tests/run_tests.py --suite fast
```

The full builder writes a new full manifest only on completion. A focused run writes a focused manifest. Before staging future generated files, measure actual binary sizes, inspect effective Git attributes, and extend storage exceptions only to the intended files at or below 100 MiB. Complete relevant Godot imports and playback verification before claiming gameplay readiness.

## Delivery record

The task commit preserves this status, the partial sources/exports, the then-current update registry, and evidence. The integration merge archives provisional exports under `.gdignore`, preserves the original registry as evidence, and keeps concurrent main runtime references intact. Integration uses the then-current `origin/main`, preserving concurrent work with ordinary Git history. The subsequent documentation commit adds the applicable shared-rig/source-mode lesson and a link to this status under `# Animation` in `AGENTS.md`. Exact task, documentation, integration, and remote verification hashes are reported in the final chat response; this file records the pre-commit state to avoid a self-referential commit hash.

The preservation commit rebased cleanly onto `18e528c73`; its rebased task hash is `8275d8788b307e28a0ef23bedf6f331ffc46a446`. `python scripts/lfs_policy.py check` passed for all 23,455 then-staged files during integration verification.

Integration fetched concurrent main `5e5236e7c`. Additive conflicts in app attributes and Animation guidance retain both deliveries. The runtime registry follows current main; frozen Waacking references are archived separately. Export bytes and SHA-256 hashes remain unchanged after relocation. The original focused manifest and historical logs retain original output paths; the verification utility resolves preserved exports from the evidence archive. The sources remain in their existing per-animation directory so their shared-scene relative paths remain valid. No animation generation or rendering occurred during integration.

After conflict resolution and export archival, the fast suite passed **10/10** in 8.56 seconds (`logs/merged_fast.log`). The archived-source verifier reproduced the same 13.97244 mm / 63.1157-degree fidelity failure with exit 1 (`logs/archived_verify.log`). All 40 preserved binaries still match the frozen SHA-256 inventory and use ordinary Git blobs. The runtime registry matches concurrent main byte-for-byte. Integration storage attributes are preserved in `storage_attributes_integration.txt`.
