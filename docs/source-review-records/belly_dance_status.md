# Belly dance animation work status

Recorded by Codex on October 2, 2026, at approximately 16:59 Europe/Berlin (14:59 UTC).
Chat: **Create belly dance animations** (`01a0fd08-fb37-7764-a1bc-ce3bae98606d`).
Project: A-Game, `/workspace/sanjo-solutions/apps/a-game`, sanjo-solutions cloud environment.
Task branch at stop: `codex/belly-dance-repertoire`.
Starting/current commit at the stop instruction: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
The preservation commit was rebased onto current main as `b423254ad` after fetching `18e528c73`. Final documentation and integration hashes appear in the chat's final response and Git history.

## Stop decision and scope

The user directed all running animation chats to stop animation work and preserve their present state. Authoring, refinement, generation, and rendering stopped. This delivery preserves **two provisional clips and an unresolved bake study**, rather than a completed belly-dance library. Further authoring requires a new instruction to resume.

The original request covered solo belly dance for both `man_and_woman3.blend` characters, spanning classical, folk, show, and fusion approaches, reuse of fitting motion, planted contacts, body clearance, smooth transitions, interpolated validation, and loop continuity. It required Blender 5.2 throughout, per-animation source files, size-based Git storage, commits, rebase onto current main, animation workflow documentation, and a merge/push to main.

## Exact completed and partial work

- Read repository and A-Game `AGENTS.md`, paired IK authoring, per-animation source/export, motion review, and test-suite instructions.
- Verified Blender **5.2.2 LTS**, build `d13f752e3b9c`. All Blender operations used that executable.
- Installed the repository's checkout-backed Player Asset Export loader in the cloud user's Blender preferences. Game Rig Tools was absent from this checkout's Blender installation during authoring.
- Hydrated required existing Git LFS scene/character assets, the animation source directory, and the three hair meshes required by the fast suite. These existing asset bytes retain their original repository storage and content.
- Reused `RigYogaPoser`, `YogaPoseLibrary`'s neutral stance, and `DiscoWristPoser` from existing dance/yoga code. Existing disco choreography was inspected; its action was retained unchanged.
- Defined **40 procedural phrase specifications**: 16 classical, 6 folk-inspired, 6 show, 6 fusion, and 6 position/transition phrases. Only the first phrase, classical hip slides, reached saved animation assets for both actors. The remaining **78 planned actor clips have no authored, baked, or exported files**.
- Saved two source files using `AnimationFileWriter`, each containing one actor's editable action and matching `.baked` action. Both use `shared_scene_data.blend`, frames **0–96**, **24 fps**, and a **4-second** loop with a duplicate endpoint. Each source has exactly one actor role.
- Exported two provisional GLBs using Blender's glTF exporter, `AnimationClipScene`, participant filtering, and `AnimationUpdates.publish`. The current supplemental registry retains both provisional references as part of the preserved state. Treat these entries as draft assets pending bake and visual acceptance.
- Wrote a preview script, but generated **zero renders or preview images**.

## Files and assets

All paths in this record are relative to `apps/a-game`.

| File | State | Actual bytes |
| --- | --- | ---: |
| `animations/man_and_woman/belly_classical_hip_slides_man.blend` | Provisional editable `belly_classical_hip_slides_man` plus `.baked`; PLAYER / Man | 336,881 |
| `animations/man_and_woman/belly_classical_hip_slides_woman.blend` | Provisional editable `belly_classical_hip_slides_woman` plus `.baked`; PARTNER / Woman | 333,354 |
| `models/player/animation_updates/belly_classical_hip_slides_man_baked_3c597a321584.glb` | Provisional exported Man clip; 636 channels, one skin, 0–4 seconds | 354,508 |
| `models/player/animation_updates/belly_classical_hip_slides_woman_baked_c0a0bee766f9.glb` | Provisional exported Woman clip; 630 channels, one skin, 0–4 seconds | 361,356 |
| The two adjacent `.glb.import` files | Solo clip import settings with linear looping | 348 / 350 |
| `models/player/animation_updates.tres` | Existing references retained; adds the two provisional clip references | Text |
| `scripts/belly_dance/choreography.py` | Forty procedural specifications and analytic pose construction; 39 phrases remain asset-generation work | Text |
| `scripts/belly_dance/author.py` | Experimental sparse author, half-frame reviewer, native bake, and publisher; latest bake change remains unverified | Text |
| `scripts/belly_dance/preview.py` | Unexecuted Blender clay review-sheet renderer; requires several currently absent clips | Text |
| `scripts/belly_dance/validation.json` | Earlier successful **authoring-control** metrics for the two saved clips; its `passed` fields exclude later bake checks and visual acceptance | Text |
| `docs/animation_work_status/belly_dance_evidence/debug_bake_study.blend` | Procedural blocking study saved from an intermediate Man bake experiment; full scene, not a production animation source | 16,067,988 |
| `docs/animation_work_status/belly_dance_evidence/.gdignore` | Keeps the preserved study outside Godot import | Empty |
| `docs/animation_work_status/belly_dance_evidence/saved_asset_inventory.json` | Read-only saved action/slot/role/range, GLB structure, byte sizes, and SHA-256 inventory | Text |
| `docs/animation_work_status/belly_dance_evidence/inspect_saved.py` | Exact read-only inventory command script | Text |
| `docs/animation_work_status/belly_dance_evidence/initial_authoring.txt` | Log of the two original successful provisional saves/exports | Text |
| `docs/animation_work_status/belly_dance_evidence/failed_bake_review.txt` | Failed intermediate bake comparison and saved blocking-study log | Text |
| `docs/animation_work_status/belly_dance_evidence/stopped_scale_preserving_experiment.txt` | Last experiment's log, ending after the Man control review | Text |
| `docs/animation_work_status/belly_dance_evidence/fast_checks.txt` | Fast suite after stopping | Text |
| `docs/animation_work_status/belly_dance_evidence/related_checks.txt` | Focused related suite after stopping | Text |
| `.gitattributes` | Exact-path direct-Git exceptions for these five binary files only | Text |
| `scripts/belly_dance/README.md` | Pointer to this partial-state record | Text |

`man_and_woman3.blend`, `shared_scene_data.blend`, the anatomical character sources, and existing animations retain their saved contents. The two new source files are discoverable through the existing source-directory workflow. The combined Blender file was not rewritten.

## Validation evidence and limits

For both saved clips, the editable controls passed **193 samples at half-frame intervals** over frames 0–96:

| Metric | Man | Woman |
| --- | ---: | ---: |
| Maximum foot IK endpoint error | 0.0002032 m | 0.0001933 m |
| Maximum wrist bend | 11.332 degrees | 11.946 degrees |
| Minimum hand-to-torso proxy clearance | 0.19755 m | 0.19500 m |
| Loop endpoint position/rotation difference | 0 / 0 | 0 / 0 |
| Loop velocity difference | 0.0000892 m/s | 0.0000640 m/s |

An additional Man control review before stopping recorded planted-foot drift 0.0000738 m, minimum toe landmark height 0.0087911 m, and minimum forearm-to-torso proxy gap 0.203110 m. These measurements describe sampled rig landmarks and coarse clearance proxies. Full skin/finger collision review, rendered motion review, complete transition evaluation, Godot playback, and saved baked/GLB contact acceptance remain outstanding.

A stricter native bake comparison **failed**: `DEF-toe.L` differed by approximately **0.0076812 m** at frame 12. Earlier source-versus-bake comparison also found approximately 0.00764 m at `DEF-toe.R`, frame 81. Disabling native key cleanup and releasing connected-bone locks in an ephemeral armature copy did not establish a successful fix. A final experiment replaced the full-transform bridge with position/rotation constraints and unit scale; the user stopped work before its bake comparison or publication finished. The mismatch cause remains a hypothesis involving hierarchy scale/decomposition. The current script differs from the revision that created the two saved binaries, so those binaries are the preserved earlier outputs, not verified products of the current script.

Commands run from the app directory after stopping:

```sh
python tests/run_tests.py --suite fast
# 9/9 passed, 5.48 seconds.
python tests/run_tests.py \
  --changed scripts/player_assets/test_animation_files.py \
  --changed scripts/player_assets/test_single_animation_layout.py \
  --changed scripts/player_assets/test_animation_participants.py
# 12/12 passed, including 9 fast and 3 related slow checks, 14.83 seconds.
blender -b -t 2 --factory-startup --python-exit-code 1 \
  --python docs/animation_work_status/belly_dance_evidence/inspect_saved.py
# Saved source/GLB inventory completed; no authoring, baking, or rendering.
```

The initial fast run reported 8/9 because three existing hair `.res` files were LFS pointers. Hydrating `apps/a-game/playground/hair/physics/*_mesh.res` resolved that prerequisite; a rerun passed 9/9 before the stop as well. Broad changed-file discovery selected 186 slow checks through shared animation dependencies. The focused three slow checks above were run; the complete 186-check selection remains unexecuted. The available Godot executable reported 4.6.3; Blender remained 5.2.2.

## Processes and saved output preservation

Owned Blender author process PID 1832 was running the first-phrase experiment when the stop arrived. SIGINT did not end it promptly, so SIGTERM terminated that exact process. A subsequent process inventory showed zero Blender processes. Its last log contained the Man authored-control review and no new `PUBLISHED` line. The prior Man/Woman source and GLB hashes remained intact. Subsequent Blender use only read saved data for inventory.

The intermediate full-scene debug file was copied byte-for-byte from `/tmp/belly-dance/debug.blend`. It retains library paths relative to that original location. To inspect it at the original path in this workspace, restore the preserved bytes as shown below. A different checkout location requires library-path repair before visual evaluation. The adjacent evidence `.gdignore` keeps this study separate from game assets. The transient `.cache/belly_dance/clip.glb` is an export staging file; the published GLB files preserve its useful outputs. `/tmp/belly-dance/git-askpass` is an environment-only credential helper and is excluded from Git; it reads the configured token at runtime and contains no token value.

## Integration-time findings

After rebasing, the current fast suite passed **10/10** in 11.30 seconds. Repeating the same focused related command passed **13/13** (10 fast plus 3 slow) in 22.25 seconds. Full logs are preserved as `belly_dance_evidence/rebased_fast_checks.txt` and `belly_dance_evidence/rebased_related_checks.txt`. `python scripts/lfs_policy.py check` from the repository root passed for 23,378 staged files before the documentation update.

After stopping, fetching main and rebasing brought in `18e528c73`, which bundles Game Rig Tools under `scripts/blender/`. The earlier missing-add-on condition now has a repository-provided setup path. This stopped task did not enable that newly fetched bundle or restart animation work. Use its setup command below for an authorized future resume. The rebased instructions also identify `scripts/player_assets/bachata_motion.py` as an inherited-scale/connected-child bake reference.

The rebased `AGENTS.md` states that the saved shared Rigify finger controls use quaternion rotations. The preserved experimental author changes finger and shoulder controls to Euler rotation modes in its temporary scene, while per-animation files store actions rather than the shared rig. Fresh-source evaluation of these channels remains a separate compatibility check. The current 0–96 source/strip playback range also retains the duplicate endpoint; reconcile it with the documented 0–95 playback convention on resume. These findings add review work; the stop instruction keeps the current authored assets frozen.

## Remaining work and resume commands

Resume only after a new user instruction authorizes animation work.

1. Resolve and validate native bake fidelity, or use the repository's Game Rig Tools workflow once available. Recheck existing actor-specific sources before replacing either provisional file.
2. Re-run control, skin/clearance, actual deform/GLB foot-contact, loop position/angular/velocity, and neutral-to-neutral transition checks for both actors.
3. Render and inspect representative movement from multiple views. The existing preview script currently references absent clips.
4. Generate and validate the other 39 phrases per actor, expanding movement coverage as needed. A procedural specification alone is not an animation deliverable.
5. Validate Godot import/playback and reconcile supplemental registry references as production clips become accepted.

Preparation and inspection, from `/workspace/sanjo-solutions/apps/a-game`:

```sh
blender --version
blender -b --python-exit-code 1 --python scripts/blender/install_animation_tools.py
mkdir -p /tmp/belly-dance
cp docs/animation_work_status/belly_dance_evidence/debug_bake_study.blend \
  /tmp/belly-dance/debug.blend
blender --enable-autoexec /tmp/belly-dance/debug.blend
```

Explicit generation commands for an authorized future resume (these overwrite corresponding task outputs and update the supplemental registry):

```sh
# First resolve the recorded bake blocker and revalidate the first phrase.
blender -b -t 4 --enable-autoexec \
  animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 \
  --python scripts/belly_dance/author.py -- --limit 1
# Continue only after both first-phrase bake reviews and visual reviews pass.
blender -b -t 4 --enable-autoexec \
  animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 \
  --python scripts/belly_dance/author.py -- --start 1 --limit 39
# This renderer needs all eight named representative moves for both actors.
blender -b -t 4 --enable-autoexec \
  animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 \
  --python scripts/belly_dance/preview.py
```

## Storage and delivery

Before staging, actual binary sizes and inherited Git attributes were inspected. All five task binaries are at or below **104,857,600 bytes**, so they are stored directly in Git through exact-file exceptions in the app's `.gitattributes`. The rebase also brought in the repository-wide size-based LFS policy. Existing global storage rules and unrelated asset storage remain intact; the task retains its exact-file exceptions. This task creates zero new LFS objects; ordinary Git push uploads its assets. Commit and merge messages identify Codex through exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer. Remote integration preserves concurrent animation work and uses ordinary history-preserving pushes.
