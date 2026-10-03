# Ballet solo animation checkpoint

- Date: October 2, 2026, 16:56 CEST (Europe/Berlin).
- Chat/task title: Ballet solo repertoire for man_and_woman3.blend (descriptive task title).
- Task branch: `codex/ballet-solo-repertoire`.
- Current commit at the stopping checkpoint: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Rebased preservation commit: `b8ac2e8fbdf553d608472658b89469ec524c738c`, based on origin/main `18e528c73` (Game Rig Tools bundle).
- Checkout: `/workspace/sanjo-solutions/apps/a-game` in the sanjo-solutions cloud environment.
- Latest instruction: stop animation authoring, refinement, generation, and rendering; preserve current outputs, verify, commit, integrate into main, and push.
- State: **partial procedural blocking studies**, preserved for future review. The original Ballet request remains partially fulfilled.

## Original scope

Create a broad, organized Ballet repertoire for both characters using Blender 5.2, the existing IK helpers, and one authoring file per animation. Reuse compatible existing work, review natural movement, surface clearance, planted contacts, interpolation, and loop seams. Store binaries of at most 104,857,600 bytes in regular Git; reserve LFS for larger files. Commit animation work, fetch and rebase onto origin/main, update the Animation section of AGENTS.md in a separate commit, merge into main, push, and verify remote main. Every new commit carries exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer.

## Completed and saved

Blender **5.2.2 LTS**, build `d13f752e3b9c`, performed all Blender operations. The procedural catalog defines 121 variants per character. The saved delivery contains **28 Woman solo studies**: five foot positions, six arm positions, port de bras, four cambres, three epaulement poses, reverence, and demi/grand plies in first, second, fourth, and fifth position.

Each saved source has one editable `ballet_woman_*` action, one matching `.baked` action, one Woman control-rig slot, one Woman deform-rig slot in the matching bake, and `PARTNER` participant metadata. Sources reference the existing `shared_scene_data.blend`. Every saved source has a compact GLB and adjacent `.glb.import` settings, registered in `models/player/animation_updates.tres`. Saved clips run at **24 fps**, start at frame **0**, and use loop playback. The table supplies inclusive final frames.

**Man:** preparation and pose probes only; saved authoring, baked, and exported clip counts are each zero. The remaining 93 Woman variants also have zero saved authoring/baked/exported files.

**Confirmed compatibility issue:** the generator changes root and finger controls to Euler rotation in memory, while the saved shared rig uses `QUATERNION` for those controls. The saved action files retain Euler curves rather than those temporary rig-mode changes. Freshly loaded authoring playback can therefore differ from the working-session review and the baked GLB. Correct and revalidate the channel modes in a newly authorized animation session. The current stop instruction preserves these partial assets unchanged.

The catalog and generator are a procedural starting point. The running Blender process loaded the recipe before subsequent recipe edits. In particular, the saved third-position study still uses the earlier fifth-like stance, while the current recipe differentiates third position. Later jump/step recipe refinements also remain recipe-only. Saved Blender sources are the authoritative checkpoint; recipe reproduction requires a fresh review.

### Exact asset inventory

All paths in this record are relative to `apps/a-game`. Each GLB has an adjacent file formed by appending `.import`. Authoring, baked, and exported states are **saved** for every row below; artistic acceptance remains **blocking study**.

| Clip suffix (`ballet_woman_`) | Frames | Source | Export |
| --- | --- | --- | --- |
| arms_fifth | 0–48 | `animations/man_and_woman/ballet_woman_arms_fifth.blend` | `models/player/animation_updates/ballet_woman_arms_fifth_baked_f1f606a03243.glb` |
| arms_first | 0–48 | `animations/man_and_woman/ballet_woman_arms_first.blend` | `models/player/animation_updates/ballet_woman_arms_first_baked_6611713342f2.glb` |
| arms_fourth | 0–48 | `animations/man_and_woman/ballet_woman_arms_fourth.blend` | `models/player/animation_updates/ballet_woman_arms_fourth_baked_43806a910058.glb` |
| arms_preparatory | 0–48 | `animations/man_and_woman/ballet_woman_arms_preparatory.blend` | `models/player/animation_updates/ballet_woman_arms_preparatory_baked_e1c4110149c8.glb` |
| arms_second | 0–48 | `animations/man_and_woman/ballet_woman_arms_second.blend` | `models/player/animation_updates/ballet_woman_arms_second_baked_181b06509e5d.glb` |
| arms_third | 0–48 | `animations/man_and_woman/ballet_woman_arms_third.blend` | `models/player/animation_updates/ballet_woman_arms_third_baked_15331d02ac7c.glb` |
| cambre_back | 0–144 | `animations/man_and_woman/ballet_woman_cambre_back.blend` | `models/player/animation_updates/ballet_woman_cambre_back_baked_0823bdec47de.glb` |
| cambre_forward | 0–144 | `animations/man_and_woman/ballet_woman_cambre_forward.blend` | `models/player/animation_updates/ballet_woman_cambre_forward_baked_02d123c7ce81.glb` |
| cambre_left | 0–144 | `animations/man_and_woman/ballet_woman_cambre_left.blend` | `models/player/animation_updates/ballet_woman_cambre_left_baked_8c20319e77ad.glb` |
| cambre_right | 0–144 | `animations/man_and_woman/ballet_woman_cambre_right.blend` | `models/player/animation_updates/ballet_woman_cambre_right_baked_877f8535469e.glb` |
| demi_plie_fifth | 0–120 | `animations/man_and_woman/ballet_woman_demi_plie_fifth.blend` | `models/player/animation_updates/ballet_woman_demi_plie_fifth_baked_3f6a2d5c7ab2.glb` |
| demi_plie_first | 0–120 | `animations/man_and_woman/ballet_woman_demi_plie_first.blend` | `models/player/animation_updates/ballet_woman_demi_plie_first_baked_35f4646a414f.glb` |
| demi_plie_fourth | 0–120 | `animations/man_and_woman/ballet_woman_demi_plie_fourth.blend` | `models/player/animation_updates/ballet_woman_demi_plie_fourth_baked_851837bdfa1d.glb` |
| demi_plie_second | 0–120 | `animations/man_and_woman/ballet_woman_demi_plie_second.blend` | `models/player/animation_updates/ballet_woman_demi_plie_second_baked_c2f612297b34.glb` |
| epaulement_croise | 0–48 | `animations/man_and_woman/ballet_woman_epaulement_croise.blend` | `models/player/animation_updates/ballet_woman_epaulement_croise_baked_e3d3e2d62455.glb` |
| epaulement_ecarte | 0–48 | `animations/man_and_woman/ballet_woman_epaulement_ecarte.blend` | `models/player/animation_updates/ballet_woman_epaulement_ecarte_baked_e56a9c486da8.glb` |
| epaulement_efface | 0–48 | `animations/man_and_woman/ballet_woman_epaulement_efface.blend` | `models/player/animation_updates/ballet_woman_epaulement_efface_baked_eb6d7acdfa53.glb` |
| feet_fifth | 0–48 | `animations/man_and_woman/ballet_woman_feet_fifth.blend` | `models/player/animation_updates/ballet_woman_feet_fifth_baked_a2267c52914f.glb` |
| feet_first | 0–48 | `animations/man_and_woman/ballet_woman_feet_first.blend` | `models/player/animation_updates/ballet_woman_feet_first_baked_071537413b91.glb` |
| feet_fourth | 0–48 | `animations/man_and_woman/ballet_woman_feet_fourth.blend` | `models/player/animation_updates/ballet_woman_feet_fourth_baked_0a34360b0f72.glb` |
| feet_second | 0–48 | `animations/man_and_woman/ballet_woman_feet_second.blend` | `models/player/animation_updates/ballet_woman_feet_second_baked_43124fee4adc.glb` |
| feet_third | 0–48 | `animations/man_and_woman/ballet_woman_feet_third.blend` | `models/player/animation_updates/ballet_woman_feet_third_baked_a165d981036c.glb` |
| grand_plie_fifth | 0–120 | `animations/man_and_woman/ballet_woman_grand_plie_fifth.blend` | `models/player/animation_updates/ballet_woman_grand_plie_fifth_baked_11749cb2ae0e.glb` |
| grand_plie_first | 0–120 | `animations/man_and_woman/ballet_woman_grand_plie_first.blend` | `models/player/animation_updates/ballet_woman_grand_plie_first_baked_539126f52486.glb` |
| grand_plie_fourth | 0–120 | `animations/man_and_woman/ballet_woman_grand_plie_fourth.blend` | `models/player/animation_updates/ballet_woman_grand_plie_fourth_baked_b0b9834917f7.glb` |
| grand_plie_second | 0–120 | `animations/man_and_woman/ballet_woman_grand_plie_second.blend` | `models/player/animation_updates/ballet_woman_grand_plie_second_baked_c83a76196308.glb` |
| port_de_bras | 0–144 | `animations/man_and_woman/ballet_woman_port_de_bras.blend` | `models/player/animation_updates/ballet_woman_port_de_bras_baked_56d4caad8450.glb` |
| reverence | 0–144 | `animations/man_and_woman/ballet_woman_reverence.blend` | `models/player/animation_updates/ballet_woman_reverence_baked_d82f2a5fe901.glb` |

### Code and evidence

- `scripts/ballet/repertoire.py`: sparse pose recipes for 121 variants, organized into positions, upper body, barre, adagio, turns, allegro, and traveling steps. Several advanced movements still require choreography-specific refinement and validation.
- `scripts/ballet/author.py`: proportion-scaled IK positioning, calibrated palm frames, sparse channel writing, per-clip review, and optional publication. Reuses `RigYogaPoser`, the yoga neutral pose, and the existing animation-file writer. Existing disco wrist helper setup informed the initial study.
- `scripts/ballet/review.py`: half-frame sampling of limb reach, repeated-position foot intervals, and loop endpoints/velocity. Toe height and a wrist/torso cylinder proxy are diagnostic values; the pass flag gates reach, contact drift, and loop checks.
- `scripts/ballet/publish.py`: Blender-native visual pose baking through `bpy_extras.anim_utils`, followed by the repository's `AnimationClipScene`, glTF options, `AnimationUpdates`, and `AnimationFileWriter`. Game Rig Tools was absent during authoring, so its Action Bakery operator was not used. Rebased main supplied the bundled add-on, which was subsequently enabled for verification.
- `scripts/ballet/verify_saved.py`: read-only source/GLB structural verification; writes only its verification report.
- `scripts/ballet/reports/woman.json`: exact names, frames, roles through naming, output paths, byte counts, channel counts, and sampled motion results for the 28 saved studies.
- `scripts/ballet/reports/saved_assets.json`: successful reread of all 28 saved authoring/baked action families and GLBs.
- `docs/animation_work_status/ballet_solo_evidence/authoring_log.txt`: preserved completed batch output through `ballet_woman_grand_plie_fifth`.
- `docs/animation_work_status/ballet_solo_evidence/pose_probe_pre_export.json`: earlier key-pose probes for both characters. Includes earlier penche/balance reach failures and predates later recipe edits; this is diagnostic history, not final acceptance.
- `docs/animation_work_status/ballet_solo_evidence/diagnostic_demi_plie.png`: exploratory Blender Workbench render of the Woman demi-plie. It predates the final palm-orientation edit and shows an intermediate study, not the final exported appearance.
- `docs/animation_work_status/ballet_solo_evidence/fast_tests.txt`, `focused_tests.txt`, `saved_verification.txt`, and `full_test_selection.txt`: exact verification outputs.
- `docs/animation_work_status/ballet_solo_evidence/storage_inventory.json`: every new binary's actual byte count and storage choice.
- `.gitattributes`: exact-path regular-Git exceptions for the 28 sources, 28 GLBs, and one diagnostic PNG. Existing model, texture, and shared-scene LFS rules remain in place.
- `models/player/animation_updates.tres`: existing references plus the 28 delivered Ballet exports.

Existing dependencies were downloaded through LFS for local evaluation: the shared scene, linked Man/Woman anatomical studies, its linked prop, and candidate idle/rest/disco/yoga sources. The original character models, shared scene, combined library, and existing animation files retain their repository contents. Three existing hair meshes were also downloaded to satisfy the fast suite.

## Verification results and limits

- `python tests/run_tests.py --suite fast`: **9/9 passed**, final run 2.89 seconds. The initial run was 8/9 because three pre-existing hair `.res` files were LFS pointers; fetching those assets resolved that prerequisite.
- `blender -b --factory-startup --python-exit-code 1 --python scripts/ballet/verify_saved.py`: **28/28 saved source/bake/export families passed**. Checks include action names, sole-participant slots, frame ranges, shared-scene references, owner bindings, GLB structure, channel counts, and stored binary sizes.
- `python tests/run_tests.py --changed scripts/ballet/author.py --changed scripts/ballet/repertoire.py --changed scripts/ballet/publish.py --changed scripts/ballet/review.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_animation_file_export.py --changed scripts/player_assets/test_single_animation_layout.py`: **11/12 passed**. `test_animation_files.py` and `test_single_animation_layout.py` passed. `test_animation_file_export.py` failed at fixture setup with `StopIteration` because the `game_rig_tools` add-on is absent.
- `python tests/run_tests.py --list`: the broad source-asset patterns select 9 fast and 186 slow checks. The complete 186-check selection was not executed; the focused verification above covers the saved-file workflow and layout.
- Authored motion review: **5,020 evaluated samples**, every half frame, across the 28 delivered clips. Maximum limb endpoint error: **0.000229034 m**. Maximum measured drift across detected stationary-foot intervals: **0.000104013 m**. Every delivered clip passed the configured loop endpoint/orientation/velocity gates. Exact per-clip values are in `woman.json`.
- Toe bone diagnostics stayed above the stage reference (minimum 0.003648672 m). These bone landmarks and the wrist cylinder proxy are distinct from a full skin intersection or sole-surface test.
- Visual review covered exploratory demi-plie renders. Whole-repertoire playback, final palm/finger appearances, mesh clearance, skin-level foot contact, balance, export-vs-authoring motion equivalence, and game-model playback remain pending. Structural GLB verification is not a claim of final Godot integration acceptance.

### Rebased-main verification

After preserving the assets, `git fetch origin` and `git rebase origin/main` completed cleanly. Main at `18e528c73` supplies the previously missing Game Rig Tools bundle. `blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py` successfully enabled it for verification. This setup changed Blender user preferences; it authored zero task animations.

- Fast suite rerun: **10/10 passed** in 6.34 seconds (current main includes an additional fast check).
- The same focused command above: **13/13 passed** in 11.19 seconds. The previously blocked `test_animation_file_export.py` now passes.
- Saved-file verifier rerun: **28/28 passed**.
- `python /workspace/sanjo-solutions/scripts/lfs_policy.py check`: **passed** for 23,457 indexed files at the initial post-rebase check. Main's generated root attributes now enforce the size policy repository-wide; the task's exact-path overrides remain scoped to its own assets.
- The shared scene has identical binary content before and after rebase: **15,356,737 bytes**, SHA-256 `18a0f6bb84cc90426444e4bf4c81d78e3b81ebd84097a7c16afc098cd9948130`. Its Git representation changed from an LFS pointer to a regular blob on main.
- A read-only Blender query confirms `QUATERNION` on both actors' `root`, `f_index.01.L`, and `f_middle.02.R` controls. This confirms the Euler-channel compatibility issue described above. Structural verification passes independently of that artistic/playback issue.

Exact additional evidence: `ballet_solo_evidence/rebased_tool_setup.txt`, `rebased_fast_tests.txt`, `rebased_focused_tests.txt`, `rebased_saved_verification.txt`, and `shared_rotation_modes.txt`. The storage inventory also records SHA-256 hashes for every new binary. The separate AGENTS.md documentation update adds guidance on stable batch recipes and precise interruption checkpoints.

## Processes, storage, and stopping point

The owned batch was launched as Woman publication followed by Man publication. On the stop instruction, Blender PID 1644 received SIGTERM. It terminated; the shell's `&&` prevented the Man batch from starting. The last completed saved clip is `ballet_woman_grand_plie_fifth`; `eleve` was the next scheduled recipe. Any in-memory work after the last completed clip has no saved asset claim. All durable outputs above are preserved. No Blender authoring or rendering process remains running.

Actual new binary sizes range from roughly 167 KiB to 394 KiB; the 57 binaries total **15,777,233 bytes**, and the largest is **403,241 bytes**. All are below 104,857,600 bytes and use regular Git. `git check-attr` confirms `filter`, `diff`, `merge`, and `text` are unset for the scoped assets. This task introduces zero new LFS objects; its binary uploads occur through the ordinary Git push.

## Remaining work and blockers

1. Obtain renewed authorization before resuming animation work; the current instruction is preservation and delivery.
2. Review the 28 blocking studies in Blender, including final hands, knees, body clearance, sole contact, and transitions. Correct the saved third-position stance and synchronize versioned recipes with regenerated sources.
3. Complete 93 remaining Woman variants and all 121 Man variants, then decide any further school-specific vocabulary needed for the original broad Ballet request. The current catalog is not an exhaustive taxonomy of every Ballet step and tradition.
4. Recheck distinct identities of advanced steps, weight transfers, spotted turns, forefoot pivots, takeoff/landing timing, and ballistic jump arcs. Procedural names alone do not establish completed choreography.
5. Perform sampled skin-level clearance/contact review and full visual playback; compare native baked motion with source motion and verify Godot playback on the composed character model.
6. Keep the newly enabled, repository-bundled Game Rig Tools add-on and Player Asset Export active in the same Blender 5.2 profile. The prior add-on blocker is resolved. Reconcile the source root/finger rotation modes before further authoring or acceptance checks.
7. Keep report entries and output paths synchronized when re-running selected clips. The author script preserves existing report entries, so review the report inventory deliberately.

## Exact resume commands

Run from `/workspace/sanjo-solutions/apps/a-game`. Commands that author or publish are for a future, newly authorized animation session. Preserve existing saved files and inspect their current state first. Reconcile the confirmed root/finger rotation-mode mismatch before running the author/publish commands below.

```bash
blender --version
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
python tests/run_tests.py --suite fast
blender -b --factory-startup --python-exit-code 1 --python scripts/ballet/verify_saved.py

# Read/review an existing source with checkout-backed Helpers.
blender animations/man_and_woman/ballet_woman_demi_plie_first.blend --python scripts/player_assets/animation_file_startup.py

# Future authorized pose probe; this writes only the probe report.
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/ballet/author.py -- --probe

# Future authorized first unsaved Woman clip; review before expanding the batch.
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/ballet/author.py -- --publish --character Woman --names eleve

# Future authorized first Man study.
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/ballet/author.py -- --publish --character Man --names feet_first

# Future authorized full remaining production; these overwrite matching sources/exports.
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/ballet/author.py -- --publish --character Woman
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/ballet/author.py -- --publish --character Man
```

For a fresh checkout, fetch the referenced shared/model LFS assets using the configured GitHub identity `codex.sanjo.solutions@gmail.com`; retain injected credential handling and avoid printing token values. Current shared dependencies are present in this workspace. The final chat delivery supplies the preservation, documentation, and main-integration commit hashes plus remote verification.

## Main integration verification

The first pre-integration fetch reached `f20ca0346`. The merge preserves concurrent additions in `.gitattributes`, `AGENTS.md`, and `models/player/animation_updates.tres`. The runtime index combines main's 83 references with the 28 Ballet additions, for 111 references; three-way reconciliation preserves removals from either branch. The size-policy check passed for 24,709 indexed files before the final integration evidence was staged. The merged-tree fast suite passed **10/10** in 6.05 seconds; its output is `ballet_solo_evidence/merged_fast_tests.txt`.

The documentation commit is `dd0f63f70`; the final chat response records the integration commit and verified remote-main result. All task commits identify Codex and carry the requested single co-author trailer.

The first main merge was `67fa33926`. Its ordinary push was rejected after remote main advanced. A fresh fetch reached `7a737f5ea`; integration preserved both histories and reconciled the runtime reference sets to 284 entries.
