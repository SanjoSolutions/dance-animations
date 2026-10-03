# Solo Irish stepdance — stopped-work checkpoint

- Date: October 2, 2026 (Europe/Berlin).
- Chat/task title: Solo Irish stepdance animations for man_and_woman3.blend, A-Game. This descriptive title identifies the task; the desktop sidebar title was unavailable.
- Environment and checkout: sanjo-solutions cloud environment, `/workspace/sanjo-solutions/apps/a-game`.
- Task branch: `codex/solo-irish-stepdance`.
- Commit before checkpoint: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Author of this checkpoint and GitHub delivery: Codex.
- Controlling instruction: stop animation work immediately, preserve its present state, commit, integrate concurrent main changes, and push. Further authoring, generation, refinement, and rendering require a renewed instruction.

## Original scope and stopping point

The original request was a broad solo Irish stepdance repertoire for both characters in `man_and_woman3.blend`, using Blender 5.2 and the repository's individual animation-file workflow. It included natural motion, IK, planted contacts, body clearance, interpolated and loop validation, suitable reuse, exports, storage based on actual sizes, an animation commit followed by rebase, an Animation-section documentation commit, and integration into main.

**This is a partial procedural blocking study, not a completed repertoire.** The catalog defines 79 named/lead variants for each of Man and Woman (158 proposed solo entries). Exactly one earlier Woman hop prototype has a saved authoring action, a saved baked action, and a GLB. The other 157 entries have recipes only. Actions evaluated during later checks lived in temporary Blender processes and were discarded; the scripts, reports, and rendered studies preserve those experiments. The prototype predates the latest calibration and grounded-target changes in the authoring script.

All Blender execution used **Blender 5.2.2 LTS**, build `d13f752e3b9c`. Game Rig Tools was absent from the original checkout/environment during authoring. The integration update below records the subsequently fetched bundled tools. The prototype used Blender's native `bpy_extras.anim_utils.bake_action_objects` visual bake, followed by the repository's `AnimationFileWriter`, `AnimationClipScene`, glTF options, and `AnimationUpdates`. Native bake equivalence remains a blocker. The saved combined library, shared scene, character models, and existing animations retain their original Git contents.

## Durable files and exact asset state

Paths below are relative to `apps/a-game`.

| File | State and purpose |
| --- | --- |
| `animations/man_and_woman/irish_stepdance_woman_hop_left.blend` | Earlier editable prototype; contains `irish_stepdance_woman_hop_left` and `irish_stepdance_woman_hop_left.baked`; 199,957 bytes. Uses the existing `shared_scene_data.blend` template and stored track bindings. |
| `models/player/animation_updates/irish_stepdance_woman_hop_left_baked_56249e3073d5.glb` | Earlier exported prototype; 267,232 bytes, one animation, 630 channels, Woman skeleton only. |
| Same GLB path plus `.import` | Godot AnimationLibrary import settings; requested looping and existing animation metadata import script. Actual Godot import/playback of this new clip remains pending. |
| `scripts/irish_stepdance/catalog.py` | 79 recipe variants: positions, soft-shoe footwork, hard-shoe footwork, traveling steps, jumps, turns, transitions, and seven rhythm-phrase families. Recipes are authored hypotheses requiring further review. |
| `scripts/irish_stepdance/author.py` | Blender 5.2 gate, rig-specific foot calibration, existing yoga Rigify poser and disco forearm-relative wrist reuse, sparse action writer, constant grounded-target cache, native bake, per-animation source writer, and GLB publisher. Publication raises on failed motion review. |
| `scripts/irish_stepdance/review.py` | Half-frame source-rig and evaluated-surface checks; contacts, IK reach, ankle/knee spacing proxies, endpoint position/orientation, and boundary velocity. It is a diagnostic, not complete mesh self-collision or artistic approval. |
| `scripts/irish_stepdance/preview.py` | Blender Workbench contact-sheet generator. Saved images are blocking studies, not finished animation previews. |
| `scripts/irish_stepdance/verify_saved_prototype.py` | Preserved diagnostic for source-versus-baked bone positions. The equivalent temporary script ran before the stop instruction and found finger differences. |
| `scripts/irish_stepdance/reports/catalog_inventory.json` | Exact 158-entry inventory with role, frame range, 24 fps, loop/once choice, and individual authored/baked/exported existence flags. |
| `scripts/irish_stepdance/reports/binary_manifest.json` | Actual byte sizes, SHA-256 hashes, and direct-Git storage for all four new binaries. |
| `scripts/irish_stepdance/reports/Woman_hop_left.json` | Earlier source-motion check; predates latest script edits. This is not baked/exported parity approval. |
| `scripts/irish_stepdance/reports/both_selection.json` | Latest completed targeted motion review, 10 entries across both characters. |
| `scripts/irish_stepdance/reports/contact_sheet.png` | Earlier Woman frontal blocking study, 1,746,213 bytes. |
| `scripts/irish_stepdance/reports/man_side.png` | Man side-view blocking study, 1,675,920 bytes; predates final grounded-target cache edit. |
| `scripts/irish_stepdance/reports/review_all.log` | Interrupted intermediate sweep: 43 Man entries, 23 passing that version's checks; last completed entry `irish_stepdance_man_treble_right`. |
| `scripts/irish_stepdance/reports/review_target.log` | Latest targeted sweep: 10 entries, 5 passing; remaining failures listed below. |
| `scripts/irish_stepdance/reports/build.log` | Earlier Woman hop generation/export log and source-review result. Export completed; the process then failed in action cleanup. That cleanup bug was corrected in the preserved authoring script. |
| `scripts/irish_stepdance/reports/verify_bake.log` | Saved source/bake parity diagnostic: maximum bone-position difference 0.01661730884680933 meters, concentrated in finger segments. |
| `scripts/irish_stepdance/reports/preview.log`, `preview_side.log` | Completed render logs; EGL fallback warnings preceded successful PNG outputs. |
| `scripts/irish_stepdance/reports/fast_suite.log`, `test_selection.log`, `structural_verification.json` | Final preservation-stage test and serialization evidence. |
| Repository `.gitattributes` | Main now supplies the generated 100 MiB threshold policy. The initial four exact-path exceptions became redundant during rebase and were removed in favor of that concurrent policy. All four binaries remain direct Git blobs. |

The saved prototype uses frames **0–24 inclusive at 24 fps**, with frame 24 repeating frame 0, a one-second loop. Its role is **PARTNER / Woman**, with control slot `Woman.rigify` and baked deform slot `Woman.rigify_deform`. The Man counterpart has a recipe and diagnostic results, but a saved Man action/bake/export is still pending. The inventory records all other planned frame ranges. Hard-shoe names describe footwork studies; footwear geometry and percussion audio were outside this checkpoint.

The prototype GLB was initially added to `models/player/animation_updates.tres` by the experimental publisher. During preservation, its own reference was removed while retaining every earlier reference. The GLB and import file remain on disk for review. Runtime publication awaits bake and motion fixes. The source directory's existing discovery workflow can still expose the explicitly documented prototype in Blender.

## Validation and concrete blockers

Commands ran from `apps/a-game` unless specified otherwise.

1. `blender --version`: Blender 5.2.2 LTS verified before Blender work.
2. `python tests/run_tests.py --suite fast`: initial 8/9 caused by LFS pointer files for three hair meshes. After hydrating `playground/hair/physics/*_mesh.res`, all 9 passed. The final preservation-stage rerun passed **9/9 in 4.90 seconds**; see `fast_suite.log`.
3. `python tests/run_tests.py --changed scripts/irish_stepdance/author.py --changed scripts/irish_stepdance/catalog.py --changed scripts/irish_stepdance/review.py --changed scripts/irish_stepdance/preview.py --list`: selected 9 fast and 0 slow tests. No additional scene-generation test was started after the stop instruction.
4. Python AST parsing passed for the four authoring/review scripts; the saved diagnostic script was subsequently copied from the already-executed temporary diagnostic. GLB header, version, byte length, one-animation name, 630 channels, one-second duration, and Woman-only skeleton were inspected directly. These checks establish serialization, not animation quality.
5. The earlier Woman hop source check passed sampled contact, reach, spacing, and loop checks. Its recorded loop velocity mismatch was about 0.00351 meters/second. This result applies to the earlier prototype version.
6. Latest targeted command: `blender -t 3 -b animations/man_and_woman/shared_scene_data.blend --python scripts/irish_stepdance/author.py -- --only '(hop|rise_and_grind|heel_dig|tip_heel|toe_rise)_left' --review-only`. Five of ten passed. Man/Woman hop and toe rise passed; Woman heel dig passed. Man heel dig reached about **34.4 mm IK error**. Man tip-heel reached about **21.1 mm IK error** and **9.49 mm floor penetration**. Rise-and-grind penetrated about **10.07 mm** for Man and **9.52 mm** for Woman. Woman tip-heel penetrated about **8.60 mm**. Exact frames, metrics, tolerances, and Boolean outcomes are in `both_selection.json`.
7. Read-only native-bake parity diagnostic found a maximum **16.617 mm** difference in finger-bone positions. The native bake is not accepted as equivalent to the source rig. Investigate finger rotation modes, parent/constraint conversion, and connected deform-bone transforms before publishing.
8. Grounded-target caching reduced sampled support-foot drift to roughly 0.4 mm or below in the latest targeted clips. This does not resolve the pitch-transition floor penetration or reach failures. Ankle/knee spacing is a proxy; full limb/surface clearance and visual continuity review remain outstanding.
9. `git diff --check` passed before staging. Actual binary sizes were inspected and `git check-attr filter diff merge text -- <each exact binary path>` returned all four attributes unset for each file. Every new binary is below 104,857,600 bytes and is stored directly in Git; this task creates no new LFS objects. After rebase, the generated root policy supplies direct Git storage; `python scripts/lfs_policy.py check` passed for 23,380 staged files.

Existing dependencies hydrated for inspection/testing: shared scene, idle and disco source files, both linked character model files, the existing linked prop file, and three hair test fixtures. Hydration retains their existing Git/LFS representation. Git credential prompts used the configured `SANJO_GITHUB_LFS_TOKEN` via an ephemeral askpass helper with username `codex.sanjo.solutions@gmail.com`; credentials were never recorded in logs or committed.

## Processes, preservation, and remaining work

At the stop instruction, process inspection showed **no owned Blender, render, authoring, or package-install process running**. Earlier incomplete full review sweeps had already been terminated during iteration. The last targeted review and parity diagnostic had completed. The copied logs and PNGs preserve their outputs. Temporary scripts/logs also existed under `/tmp/irish-tools`; the durable diagnostics and useful results are listed above. Python bytecode and credential helpers belong to the environment, not the checkpoint.

Remaining work, only following renewed animation authorization:

- Resolve the five targeted failures while keeping sparse meaningful IK keys and fixed contact phases. The planned reach-ceiling solver and further interpolation refinements were **not implemented** before the stop.
- Resolve source/baked finger parity, using the established Game Rig Tools bake when available or proving the native alternative equivalent.
- Rerun the complete two-character sweep against the final script; the latest complete 158-entry validation does not exist.
- Build the 157 remaining action/bake/export sets only after their checks pass; rebuild the earlier Woman hop with the final accepted implementation.
- Review complete interpolated motion, full limb clearance, planted toe/heel pivots, and loop velocity; the sheets show selected poses only.
- Reopen saved sources through the add-on, verify action bindings, compare source/baked/exported motion, import into Godot, and validate skeleton targeting and per-clip loop settings.
- Inspect byte sizes and scoped attributes for every future binary, then publish only accepted clips to the runtime registry.

## Integration update

The checkpoint was rebased onto concurrent `origin/main` commit `18e528c73e6d5be8a86b1a21ff6cc2f7cfeca1f2`, producing checkpoint commit `723192ee1fc96fa55e71d265e3aa77fd31f1032a`. The attributes conflict was resolved by retaining main's generated threshold policy. Main also added `extensions/game_rig_tools/`, `scripts/blender/install_animation_tools.py`, and the setup guide in `scripts/blender/README.md`. The new Animation guidance documents matching finger rotation channels to the shared rig's saved quaternion modes, which is directly relevant to the recorded parity failure. These concurrent tools were discovered after the stop; setup, rebaking, and animation generation were left for an authorized resumption.

After this rebase, `python tests/run_tests.py --suite fast` passed **10/10 in 9.63 seconds**, including main's newly added test-tree check; the complete output is `scripts/irish_stepdance/reports/fast_after_rebase.log`. This run verifies the integrated repository fast set and leaves the earlier animation failures explicit.

The Animation section of `AGENTS.md` now links this partial checkpoint and records stable support-target calibration plus separate source/reloaded/baked evidence. Preserve the current shared rig and bundled tool changes when resuming; the old scripts have yet to be revalidated against this newer main.

## Exact resume commands

These commands document the handoff. They are **not authorization to resume generation**.

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender --version
python tests/run_tests.py --suite fast

# After renewed animation authorization, install main's bundled helpers first.
# Keep Blender 5.2, even though the general tool guide also permits newer versions.
BLENDER="$(command -v blender)"
export BLENDER_USER_CONFIG="$PWD/.cache/irish_stepdance/blender/config"
export BLENDER_USER_SCRIPTS="$PWD/.cache/irish_stepdance/blender/scripts"
export BLENDER_USER_EXTENSIONS="$PWD/.cache/irish_stepdance/blender/extensions"
mkdir -p "$BLENDER_USER_CONFIG" "$BLENDER_USER_SCRIPTS" "$BLENDER_USER_EXTENSIONS"
"$BLENDER" --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py

# Diagnose the saved prototype's existing bake; creates temporary in-memory poses only.
blender -t 2 -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 \
  --python scripts/irish_stepdance/verify_saved_prototype.py

# After renewed authoring authorization and fixes: targeted source validation.
blender -t 3 -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 \
  --python scripts/irish_stepdance/author.py -- \
  --only '(hop|rise_and_grind|heel_dig|tip_heel|toe_rise)_left' --review-only

# Complete source validation; writes both_all.json after finishing all 158 entries.
blender -t 3 -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 \
  --python scripts/irish_stepdance/author.py -- --review-only

# Generation/export overwrites this prototype and updates the runtime registry.
# Run only once the independent motion and bake blockers are resolved.
blender -t 3 -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 \
  --python scripts/irish_stepdance/author.py -- --character Woman --only hop_left

# Full generation; each failed source review currently stops publication.
blender -t 3 -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 \
  --python scripts/irish_stepdance/author.py

# Optional renewed visual review.
blender -t 2 -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 \
  --python scripts/irish_stepdance/preview.py -- --character Man --view side
```

On a fresh checkout, hydrate the existing source/model dependencies through the repository's configured GitHub identity before Blender runs. The saved prototype and study images need only ordinary Git checkout. The parity diagnostic currently prints differences; inspect its measurements rather than treating exit zero as approval.

The checkpoint commit is discoverable with `git log --format='%H %s' -- docs/animation_work_status/solo_irish_stepdance.md`. Integration and push hashes are reported in the delivery message; the pre-checkpoint hash above intentionally records the precise starting state.
