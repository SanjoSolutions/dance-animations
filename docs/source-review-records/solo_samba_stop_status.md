# Solo samba animation work: preserved partial state

Date: October 2, 2026 (Europe/Berlin). Stop request received around 16:56 CEST.
Chat title: **Create Solo samba animations**.
Chat ID: `01a0fd09-db76-7081-a1f6-f05b3f632070`.
Task branch: `codex/solo-samba`.
Checkout: `/workspace/sanjo-solutions`, app `apps/a-game`, sanjo-solutions cloud environment.
Current commit at the stopping point: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
Implementation and assets were working-tree changes at that point. The subsequent
preservation and documentation commits are identifiable in Git history by this file.

## Delivery status

**Partial procedural blocking studies; animation production stopped at the user's request.**
Fifteen per-animation source files and fifteen corresponding GLBs are preserved:
eight Man clips and seven Woman clips. Each source contains an editable authoring
action and a matching `.baked` action. Saved bakes have known validation failures.
These files represent work in progress, rather than a completed samba repertoire.

The task's entries were removed from the active `models/player/animation_updates.tres`
during delivery packaging so these known-failing candidates stay outside runtime
playback. The exact registry at the stop point is preserved as
`docs/animation_work_status/solo_samba_evidence/animation_updates_at_stop.tres`.
Existing runtime entries remain intact. GLBs and their import configurations remain
at their generated paths. The combined Blender library discovers source files on
reopen; treat the `solo_samba_` source prefix as draft work until validation passes.

## Original scope and preparation

Create a broad, organized solo samba repertoire for both characters from
`man_and_woman3.blend`, including moves, positions, smooth transitions, planted
contacts, clearance, and interpolated/loop review. Reuse suitable existing motion.
Use Blender 5.2 for all Blender operations, preserve the per-animation source
workflow, store binaries at or below 104,857,600 bytes in Git, commit and rebase,
add useful Animation guidance to AGENTS.md, merge into main, push, and verify.

Read the repository and app AGENTS.md, paired IK authoring guide, motion-review
guide, player animation workflow, source-directory README, and existing disco
and yoga posing implementations. Used the cloud-environment runtime skill and
checked network/credential readiness. Blender is **5.2.2 LTS**, build `d13f752e3b9c`.
Installed the existing checkout-backed Player Asset Export loader for Blender 5.2.
Game Rig Tools was absent from this environment's enabled add-ons at the stopping point.
The subsequent rebase onto `18e528c73` brought the newly bundled Game Rig Tools
installer and existing bake/rotation-mode guidance into the checkout. Those
concurrent changes provide the supported tooling for a future authorized resume.

Hydrated existing LFS inputs: `man_and_woman3.blend`,
`animations/man_and_woman/shared_scene_data.blend`,
`animations/man_and_woman/solo_disco_dance.blend`, `man_anatomical_study.blend`,
and `woman_anatomical_study_speculum.blend`. Existing hair physics mesh resources
were hydrated to satisfy the fast suite. Shared inputs remain unchanged.

## Authored, baked, and exported state

All saved clips use **24 FPS, frames 0–96**, with frame 96 the duplicate loop
endpoint (play frames 0–95 for repetition); duration is four seconds at 120 BPM.
Each file has one participant slot per action. Man authoring uses `Man.rigify`
and `PLAYER`; its bake uses `Man.rigify_deform`. Woman uses `Woman.rigify`,
`PARTNER`, and `Woman.rigify_deform`. These are independent solo clips.

The seven saved figures shared by both characters are `no_pe`, `bounce`,
`pelvic_action`, `forward_basic`, `backward_basic`, `side_basic`, and
`progressive_basic`. Man additionally has `outside_basic`.

Man's eight saved clips and Woman's `no_pe` use the experimental parent-first
`SambaVisualBake`. Woman's other six retain earlier native visual bakes from
`bpy_extras.anim_utils.bake_action_objects`; that earlier bake implementation
was replaced in the working script during investigation. Their saved sources
and GLBs preserve the actual prior output. **Current scripts do not reproduce
all historical asset bytes.**

Man `whisks` reached authored in-memory poses and a passing source-motion report,
then was terminated during GLB export. Its authoring and baked actions were never
saved as a source file, and its GLB never reached the published update directory.
The temporary `interrupted_export_clip.glb` is actually the preceding completed
`solo_samba_man_outside_basic.baked` export, as identified by its JSON payload.
Woman `outside_basic` failed an earlier source seam check and has no saved asset.

The procedural vocabulary in `choreography.py` contains 42 planned figures per
character: foundations, basics, walks, crosses, footwork, turns, arm/body styling,
eight positions, and entry/finish transitions. Names in that specification
represent planned choreography, rather than completed assets. Choreographic
fidelity and naturalness still need expert/visual review; the vocabulary makes
no claim to exhaust every regional samba tradition.

### Exact source/export inventory

Every row below is a **draft**, with authoring action, baked action, and generated
GLB present. The adjacent `<export>.import` file is also preserved. Byte sizes
and SHA-256 digests, action slots, ranges, and export channel counts are recorded
in `solo_samba_evidence/asset_inventory.json`.

| Source relative to apps/a-game | Source bytes | Export relative to apps/a-game | Export bytes |
| --- | ---: | --- | ---: |
| `animations/man_and_woman/solo_samba_man_backward_basic.blend` | 2419195 | `models/player/animation_updates/solo_samba_man_backward_basic_baked_f03653ffe2b9.glb` | 464280 |
| `animations/man_and_woman/solo_samba_man_bounce.blend` | 2409637 | `models/player/animation_updates/solo_samba_man_bounce_baked_cb661f537d6c.glb` | 458412 |
| `animations/man_and_woman/solo_samba_man_forward_basic.blend` | 2426218 | `models/player/animation_updates/solo_samba_man_forward_basic_baked_c92447d9d44a.glb` | 469096 |
| `animations/man_and_woman/solo_samba_man_no_pe.blend` | 2414700 | `models/player/animation_updates/solo_samba_man_no_pe_baked_508fc598f275.glb` | 479632 |
| `animations/man_and_woman/solo_samba_man_outside_basic.blend` | 2424352 | `models/player/animation_updates/solo_samba_man_outside_basic_baked_99d49f06e0f3.glb` | 481852 |
| `animations/man_and_woman/solo_samba_man_pelvic_action.blend` | 2389985 | `models/player/animation_updates/solo_samba_man_pelvic_action_baked_748a4dd1f0b3.glb` | 464524 |
| `animations/man_and_woman/solo_samba_man_progressive_basic.blend` | 2439459 | `models/player/animation_updates/solo_samba_man_progressive_basic_baked_b5746d6e6c6f.glb` | 486160 |
| `animations/man_and_woman/solo_samba_man_side_basic.blend` | 2439224 | `models/player/animation_updates/solo_samba_man_side_basic_baked_72fccf867240.glb` | 474100 |
| `animations/man_and_woman/solo_samba_woman_backward_basic.blend` | 343684 | `models/player/animation_updates/solo_samba_woman_backward_basic_baked_ca711f81c0ca.glb` | 330668 |
| `animations/man_and_woman/solo_samba_woman_bounce.blend` | 335594 | `models/player/animation_updates/solo_samba_woman_bounce_baked_6178760b11ed.glb` | 334620 |
| `animations/man_and_woman/solo_samba_woman_forward_basic.blend` | 348279 | `models/player/animation_updates/solo_samba_woman_forward_basic_baked_de8d538d26a5.glb` | 329524 |
| `animations/man_and_woman/solo_samba_woman_no_pe.blend` | 2464795 | `models/player/animation_updates/solo_samba_woman_no_pe_baked_638fd810e3c5.glb` | 481420 |
| `animations/man_and_woman/solo_samba_woman_pelvic_action.blend` | 327079 | `models/player/animation_updates/solo_samba_woman_pelvic_action_baked_0df69001dd50.glb` | 334624 |
| `animations/man_and_woman/solo_samba_woman_progressive_basic.blend` | 347763 | `models/player/animation_updates/solo_samba_woman_progressive_basic_baked_429bed0ed13e.glb` | 329528 |
| `animations/man_and_woman/solo_samba_woman_side_basic.blend` | 347205 | `models/player/animation_updates/solo_samba_woman_side_basic_baked_6230edb7835e.glb` | 329764 |

## Code and evidence files

Paths below are relative to `apps/a-game`.

- `scripts/solo_samba/choreography.py`: 42-figure procedural contact/pose vocabulary;
  1-a-2 contact timing, swing clearance, turns, styling, and transition specifications.
- `scripts/solo_samba/author.py`: independent participant action construction,
  sparse keys, existing disco/yoga IK reuse, per-animation writer, export publisher.
  The publisher takes a local file lock when updating the shared runtime registry.
- `scripts/solo_samba/visual_bake.py`: experimental parent-first visual bake;
  **blocking study with unresolved saved-bake errors**.
- `scripts/solo_samba/review.py`: interpolated contact, reach, wrist, proxy-clearance,
  and loop diagnostics. Half-frame sampling plus 0.05-frame seam samples.
- `scripts/solo_samba/verify_saved.py`: read-back action/GLB verification and
  authored-versus-baked deform-pose comparison; currently fails the pilot clips.
- `scripts/solo_samba/render_review.py`: Blender 5.2 neutral-surface review renderer.
- `scripts/solo_samba/review_man.json`: nine source-motion entries, including the
  unsaved whisk study; the eight saved Man source-motion entries pass.
- `scripts/solo_samba/review_woman.json`: seven passing saved source-motion entries
  and the earlier failed, unsaved outside-basic candidate. Historical records use
  193 or 195 samples depending on the seam-review revision.
- `scripts/solo_samba/saved_review_man.json`, `saved_review_woman.json`: saved-bake
  pilot failures with exact hashes of the examined source/export bytes.
- `.gitattributes`: exact-path Git storage exceptions for this task's small binaries.
- `docs/animation_work_status/solo_samba_evidence/asset_inventory.json`,
  `inventory_saved.py`, `inventory_saved.log`: read-only saved-asset inventory.
- Evidence `man.log`, `woman.log`, `pilot.log`, `saved_pilot.log`,
  `saved_review_man_stop.log`: generation and saved-file validation logs.
- Evidence `diagnose.py`, `diagnose.log`, `bake_diagnostic.py`,
  `bake_diagnostic.log`: temporary bake investigation scripts/logs, preserved for resume.
- Evidence `woman_front.png`, `render.log`: one actual mesh review at frame 21,
  produced before the stop request; neutral Workbench shading in Blender 5.2.2.
  EGL warnings occurred, and Blender still saved the image successfully.
- Evidence `fast.log`, `fast_stop.log`, `focused_checks.log`, `selection.log`:
  test results and conservative full test-selection output.
- Evidence `animation_updates_at_stop.tres`: snapshot of the pre-quarantine catalog.
- Evidence `interrupted_export_clip.glb`: the preserved scratch output identified above.

## Verification and concrete blockers

All commands run from `apps/a-game`, with Blender 5.2.2.

1. `python tests/run_tests.py --suite fast`: **9/9 pass**, including the run after
   stopping. Initial execution failed because three hair physics `.res` files were
   LFS pointers; hydrating those existing assets resolved the prerequisite.
2. `python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_motion_review.py --changed scripts/player_assets/test_animation_file_export.py`:
   **11/12 pass**. The fast nine, per-animation file fixture, and motion-review
   fixture pass. The export fixture fails with `StopIteration` in
   `test_bake_cache.py:17`, while locating the absent `game_rig_tools` add-on.
3. `blender --background --factory-startup --python-exit-code 1 --python docs/animation_work_status/solo_samba_evidence/inventory_saved.py`:
   **pass**, 15 source files with matching GLBs, action metadata, valid binary
   headers and declared lengths. This establishes structure, rather than motion quality.
4. `blender --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/solo_samba/verify_saved.py -- --character Woman --figures no_pe`:
   **fail**. Source plants approximately 0.170 mm, matching loop endpoints,
   maximum wrist bend approximately 12.01 degrees. Saved bake maximum position
   error **0.010461 m**, maximum rotation error **0.160978 rad**, maximum integer
   frame position error **0.004736 m**. Position worst sample: frame 10.5,
   `DEF-knee-helper.R`.
5. The same saved verifier with `--character Man --figures no_pe`:
   **fail**. Source plants approximately 0.190 mm, matching loop endpoints,
   wrist bend approximately 11.43 degrees. Saved bake maximum position error
   **1.136393 m**, maximum rotation error **2.827030 rad**, integer-frame error
   **1.136072 m**. Position worst sample: frame 42.5, `DEF-f_ring.03.R`.
   The experimental baker changes runtime bone rotation modes while the saved
   per-animation files reuse the shared rig; persistence/rotation-mode compatibility
   is a concrete next investigation, alongside scale/shear reconstruction.
   This is a diagnosis direction, rather than an established fix.
6. `python -m py_compile scripts/solo_samba/*.py`: pass.
7. `python tests/run_tests.py --list`: selects 9 fast and 186 slow checks when the
   generated runtime registry is active. The full 186-test selection was not run;
   focused checks above reflect the delivery scope and current environment.

Source-motion checks establish sampled endpoint/proxy diagnostics. Full evaluated
surface collision review, foot-sole/ball contact refinement, comprehensive playback,
Godot import/runtime track resolution, all saved-bake equivalence checks, and the
complete intended repertoire remain outstanding. The existing single-clip workflow's
full-library cache is absent in this checkout. Direct `AnimationClipScene` exports
were used for these studies; production export should reconcile the normal cache
and installed Game Rig Tools workflow before activation.

## Processes and storage

The final owned authoring process (PID 1784) was sent SIGINT and then SIGTERM when
Blender continued after SIGINT. It ended during the Man whisk export. All owned
animation generation/render processes are stopped. Read-only verification processes
completed afterward. There is no running animation worker to resume.

Original scratch logs lived in `/workspace/scratch/solo-samba`; durable evidence
was copied into this directory. `.cache/solo_samba/clip.glb` is a temporary exporter
file; its final completed bytes are preserved in the evidence directory. Installed
Blender preferences and hydrated input LFS objects are environment state, rather
than task commits. Scratch authentication helpers contain variable references,
rather than token values, and belong outside the repository.

Every task binary is at or below 104,857,600 bytes. Actual sizes were inspected
before staging, and exact-path `-filter -diff -merge -text` overrides keep only
these measured assets in regular Git. The largest binary is 2,464,795 bytes.
The task creates zero new LFS objects; ordinary Git push uploads these assets.
Existing LFS/shared assets remain under their existing storage policy.

## Remaining work and exact resume commands

Resume authoring only after a new user instruction authorizes it. First investigate
the saved-bake failures using the preserved files; keep draft exports outside the
active runtime registry while they fail.

```bash
cd /workspace/sanjo-solutions/apps/a-game
blender --version
python tests/run_tests.py --suite fast
blender --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/solo_samba/verify_saved.py -- --character Man --figures no_pe
blender --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/solo_samba/verify_saved.py -- --character Woman --figures no_pe
blender --background animations/man_and_woman/solo_samba_woman_no_pe.blend --python-exit-code 1 --python docs/animation_work_status/solo_samba_evidence/bake_diagnostic.py
```

After fixing and validating the bake, the author commands below overwrite matching
per-animation sources and exports and republish them to the runtime registry.
Use the narrow `--figures no_pe` pilot before running the full vocabulary.

```bash
blender --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/solo_samba/author.py -- --character Woman --figures no_pe
blender --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/solo_samba/author.py -- --character Man --figures no_pe
# Following successful pilot verification and renewed authoring authorization:
blender --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/solo_samba/author.py -- --character Woman
blender --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/solo_samba/author.py -- --character Man
blender --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/solo_samba/verify_saved.py -- --character Woman
blender --background animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/solo_samba/verify_saved.py -- --character Man
```

Finish choreographic refinement, body/foot-surface review and transitions, verify
Godot imports and participant routing, repeat the size/attribute audit for any new
files, and activate only reviewed exports. Preserve concurrent source files and
union concurrent runtime registry paths when integrating. GitHub commit messages
for this task identify Codex as author and include exactly one
`Co-authored-by: Codex <noreply@openai.com>` trailer. Delivery uses history-preserving
integration with the latest origin/main and an ordinary push; final commit hashes
and remote verification belong to the delivery response.

## Integration verification update

The preservation commit rebased cleanly onto `18e528c73` as
`25c71e1f3` (original pre-rebase hash `d35228110`). All authored assets remained
frozen. The newly available bundled-tool installer was run solely to establish
the environment prerequisite for the existing verification fixture:

```bash
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_motion_review.py --changed scripts/player_assets/test_animation_file_export.py
# From the repository root:
python scripts/lfs_policy.py check
```

See `solo_samba_evidence/install_tools_after_rebase.log` and
`solo_samba_evidence/focused_checks_after_rebase.log` for the updated setup and
verification results: **13/13 pass** (the current ten fast checks plus three
focused slow checks). The previously blocked export fixture now passes with the
bundled Game Rig Tools enabled. The repository LFS policy check passes. Installing tooling
and running isolated verification fixtures does not regenerate the preserved
samba animation assets; their recorded bake failures remain outstanding.
