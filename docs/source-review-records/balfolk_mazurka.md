# Balfolk mazurka animation work status

## Stop record

- Date: October 2, 2026, 17:00 CEST (Europe/Berlin). Inventory and verification completed after the stop.
- Chat title: **Create Balfolk mazurka animations**.
- Chat ID: `01a0fcff-e0f2-7502-b00e-b15ec10ba071`.
- Stop instruction received through coordination chat `01a0fd1a-3673-7683-ae29-577f2ee1a927`: preserve the present state, record it, commit, integrate concurrent main changes, and push.
- Environment: sanjo-solutions cloud; checkout `/workspace/sanjo-solutions`; app `apps/a-game`.
- Task branch: `codex/balfolk-mazurka`.
- HEAD at stop: `fe09ef7b6a54f03909f7335d9673a27c15007d69`. Task changes were still uncommitted at that point.
- Blender: **5.2.2 LTS**, build `d13f752e3b9c`, installed binary `/home/agent/.local/bin/blender`.
- Authorship: Codex. GitHub delivery and commit descriptions for this task are authored by Codex.

**This is a partial procedural blocking study, preserved at the user's stop instruction. The repertoire remains in progress.** Authoring, refinement, generation, and rendering stopped. Subsequent work consists of recording, read-only asset inspection, tests, storage classification, and Git delivery.

## Original scope and later direction

Create a broad, organized Balfolk mazurka repertoire for `man_and_woman3.blend`, coordinating both characters, reusing suitable existing animation, preserving planted contacts and body clearance, and validating interpolation and loops. Follow the repository's paired IK and individual animation source workflow, use Blender 5.2 throughout, store binaries of at most 104,857,600 bytes in ordinary Git, commit/rebase, update the Animation guidance, and integrate/push main.

The user subsequently instructed **“don't bake.”** Accordingly, every asset in this snapshot is an editable authoring source. Baked actions created: **0**. Runtime animation exports created: **0**. Runtime model/library updates: **0**. The stop instruction then replaced further animation completion with preservation and delivery.

## Saved animation sources

All paths below are relative to `apps/a-game/animations/man_and_woman/`. Every file contains one paired authoring action with the `OBMan.rigify` and `OBWoman.rigify` slots and refers to `shared_scene_data.blend`. Roles are Man as leader (`player`) and Woman as follower (`partner`). Timing is 24 fps and a nominal 90 BPM, 3/4 phrase, with 16 frames per beat. The 96-frame clips occupy two bars; the turn occupies eight bars. Loop endpoints are duplicate boundary samples; playback can omit the duplicated final frame.

| File | Bytes | Frames | State at stop |
| --- | ---: | --- | --- |
| `mazurka_hold_closed.blend` | 502906 | 0–96 | Static closed hold; earlier half-frame check passed; rendered pose reviewed. |
| `mazurka_hold_open_single_hand.blend` | 494582 | 0–96 | Static one-hand hold; earlier half-frame check passed; preview preserved. |
| `mazurka_hold_open_two_hand.blend` | 497102 | 0–96 | Static two-hand hold; earlier half-frame check passed; preview preserved. |
| `mazurka_hold_promenade.blend` | 496084 | 0–96 | Static promenade; earlier half-frame check passed; rendered pose reviewed. |
| `mazurka_hold_promenade_reverse.blend` | 493860 | 0–96 | Static reverse promenade; earlier half-frame check passed; preview preserved. |
| `mazurka_basic.blend` | 523856 | 0–96 | Looping mirrored basic phrase and third-beat suspension; earlier half-frame check passed; rendered midpoint reviewed. |
| `mazurka_turn_clockwise.blend` | 619864 | 0–384 | **Failed clearance study**; source retained exactly as saved. Details below. |
| `mazurka_transition_closed_to_open_two_hand.blend` | 503222 | 0–96 | One-shot hold change; earlier interpolated contact/proxy checks passed. |
| `mazurka_transition_open_two_hand_to_closed.blend` | 503122 | 0–96 | One-shot return; earlier interpolated contact/proxy checks passed. |
| `mazurka_transition_open_single_hand_to_promenade.blend` | 521811 | 0–96 | One-shot stepped opening; expanded half-frame checks passed. |
| `mazurka_transition_promenade_to_open_single_hand.blend` | 513705 | 0–96 | Reversal of the opening; expanded half-frame checks passed. |
| `mazurka_transition_open_two_hand_to_promenade_reverse.blend` | 522205 | 0–96 | Last completed save during shutdown; expanded half-frame checks passed; surface rendering remains outstanding. |

All five holds have one key per scalar curve. The basic phrase has up to 25 keys per curve; transitions up to 13; the turn up to 97. The five transitions contain serialized `mazurka_foot_contacts`. The earlier saved holds, basic, and turn predate that metadata and require metadata reconstruction before the latest generic reviewer can run against them. The current generator includes later refinements that have yet to be regenerated and verified across these saved sources.

`animations/man_and_woman/mazurka_review.json` contains **only the last reverse-promenade entry transition**, rather than a full-repertoire certificate. Source names, exact bytes, SHA-256 hashes, action ranges, slots, and metadata availability are recorded in [saved_source_inventory.json](balfolk_mazurka_evidence/saved_source_inventory.json).

The combined library and shared scene were hydrated for reading and retained their original tracked contents. Newly saved per-animation sources belong to the existing discovery workflow. Reopening and reviewing all twelve from the combined library remains outstanding.

## Authoring and review code

- `scripts/player_assets/author_balfolk_mazurka.py`: unfinished procedural authoring tool. It reuses the relaxed `share_company` pose through `PairedAnimationAuthoring`, creates calibrated palm holds, keys paired IK steps, writes individual sources with `AnimationFileWriter`, and defines a proposed 34-clip repertoire. It supports `--only` glob selection and an optional `--preview`. Its final full-run path has **not** completed. Running it writes animation sources; use it only after a new instruction to resume authoring.
- `scripts/player_assets/balfolk_mazurka_review.py`: half-frame review of serialized foot contact intervals, palm separation, torso/ankle proxies, knee/elbow angles, and loop position/angular/velocity continuity. The last completed transition was checked with this revision. Measurements establish the specified contacts/proxies; full mesh, finger-surface, and choreography approval remains a separate review.
- `animations/man_and_woman/.gitattributes`: twelve exact filename exceptions for the preserved sources.
- `docs/animation_work_status/balfolk_mazurka_evidence/.gitattributes`: seven exact filename exceptions for the pre-existing render outputs copied into this record.

## Validation and known limits

Earlier basic-loop evaluation sampled 193 half-frame positions: maximum planted ankle drift 0.001943 m, joined palm gap 0.014138 m, torso proxy clearance at least 0.194366 m, loop endpoint distance 0.001708 m, endpoint angle 0.002290 rad, and linear velocity mismatch 0.042316 m/s. That report predates the expanded angular-velocity, support-coverage, and joint checks. Its temporary JSON was later overwritten by the turn report; these values are preserved from the chat's execution output and remain historical observations.

The saved clockwise turn sampled 769 half-frame positions. Its maximum planted ankle drift was 0.003702 m; joined palm gap 0.013195 m; endpoint distance 0.000000277 m; endpoint angle 0.000000175 rad; linear velocity mismatch 0.041838 m/s. **The review failed** because minimum ankle separation was 0.106930 m against the 0.12 m threshold. The tightest observed integer-frame pose is frame 128, between the leader's left and right ankles. The generator now contains a wider turning placement, but that change has **not** been applied to or verified in the saved turn. Preserve this asset as a blocking study. The full historical report is [mazurka_review.json](balfolk_mazurka_evidence/mazurka_review.json), distinct from the newer report in the animation directory.

The two promenade opening/closing transitions passed expanded checks, with approximately 0.000615 m maximum ankle drift and 0.021121 m maximum joined-palm gap. The final reverse-promenade entry passed with 193 samples, four foot contact intervals, zero missing-support samples, 0.000715 m maximum ankle drift, 0.004834 rad maximum planted ankle angle error, 0.012660 m maximum joined-palm gap, 0.194366 m minimum torso proxy clearance, and 0.184841 m minimum ankle separation. These one-shot transitions report loop checks as inapplicable. Preserved logs contain the per-joint angle ranges.

After the stop, the following checks completed:

```bash
cd /workspace/sanjo-solutions/apps/a-game
export BLENDER=/home/agent/.local/bin/blender
export GODOT=/workspace/.cloud-onboarding/3d-tools/godot-4.7.2/godot
python tests/run_tests.py --suite fast
python tests/run_tests.py \
  --changed scripts/player_assets/author_balfolk_mazurka.py \
  --changed scripts/player_assets/balfolk_mazurka_review.py \
  --changed scripts/player_assets/test_animation_files.py \
  --changed scripts/player_assets/test_paired_animation_authoring.py \
  --changed scripts/player_assets/test_motion_review.py
blender --background --factory-startup --python-exit-code 1 \
  --python docs/animation_work_status/balfolk_mazurka_evidence/inspect_saved_sources.py
python -m py_compile scripts/player_assets/author_balfolk_mazurka.py \
  scripts/player_assets/balfolk_mazurka_review.py
```

Results: **9/9 fast checks passed** in 3.06 s; **13/13 selected checks passed** in 8.61 s, comprising the fast suite and four Blender checks (animation files, motion landmarks, motion review, paired authoring). Read-only source inspection passed for all **12 paired editable sources**, confirmed zero baked actions, and recorded the original byte hashes. Python syntax checks passed. These fixture and metadata checks establish workflow integrity; they do not approve the unfinished choreography. Broad export/bake checks were outside the preservation scope and the user's no-bake direction.

Initial environment issues were resolved for this verification: hair resource LFS pointers were hydrated, and the correct installed Godot 4.7.2 executable was selected. The first fast run had passed 8/9 because three hair meshes were pointers; a subsequent attempt used an incorrect Godot filename. The final logs above supersede those environment failures. Game Rig Tools was absent when authoring began; the user then removed baking from scope. Git LFS downloads used the configured environment credential through an ephemeral askpass helper; credential contents were kept out of logs and commits.

## Preserved evidence and process state

The [evidence directory](balfolk_mazurka_evidence/) contains:

- `saved_source_inventory.json`, `storage_inventory.json`, `saved_source_inspection.log`, and the read-only `inspect_saved_sources.py` verifier.
- `final_fast.log` and `final_related.log`, plus earlier successful `mazurka_fast.log` and `mazurka_tests.log`.
- `mazurka_author.log`: earlier transition passes and a prior failed reverse-promenade release attempt; this is an iteration log, not the final outcome for that entry transition.
- `mazurka_counter.log`: the final entry transition's authored frames, successful review, and saved-file confirmation immediately before termination.
- `mazurka_diagnose.log` and `turn_diagnose.py`: the saved turn's close-ankle diagnostic.
- `mazurka_holds.json`: an earlier three-hold target snapshot, preceding promenade additions; diagnostic evidence rather than a complete current library.
- `mazurka_review.json`: the failed saved-turn report and sampled landmarks.
- `authoring_probe.py`, `authoring_probe.log`, and `initial_source_inspection.log`: early calibration/discovery evidence. The probe script authors a temporary in-memory pose; treat it as authoring and run only after resumption is authorized.
- Seven existing Blender 5.2 previews: `mazurka_basic.png`, `mazurka_closed.png`, `mazurka_open_single_hand.png`, `mazurka_open_two_hand.png`, `mazurka_promenade.png`, `mazurka_promenade_reverse.png`, and `mazurka_turn.png`. These images were created before the stop and copied byte-for-byte afterward; they represent the earlier pose versions and use a neutral clay render.

The owned in-flight command was:

```bash
blender --background animations/man_and_woman/share_company.blend \
  --python-exit-code 1 --python scripts/player_assets/author_balfolk_mazurka.py \
  -- --only 'mazurka_transition_*promenade_reverse*'
```

Process PID 2499, tool session 57995, received SIGTERM. It completed and saved the forward entry before termination; its reverse return had no saved output. The process was subsequently confirmed absent. Further authored state in that process was volatile and was not recovered. No task-owned authoring or rendering process remains. Temporary draft fragments in `/tmp` are superseded by the preserved scripts; the credential helper is excluded from this record.

## Storage and delivery

All 19 preserved binary files (12 Blender sources and 7 existing PNG previews) were inspected before staging: total 7,667,648 bytes; largest file 619,864 bytes. Each is below 104,857,600 bytes and belongs in ordinary Git. Before the exact-path exceptions, the repository's global Blender/PNG rules selected LFS. The exceptions explicitly unset filter/diff/merge and keep binary text handling. Other assets retain their existing attributes. The storage inventory records before/after attributes, exact sizes, and hashes. This task creates no new LFS objects; ordinary Git push carries its assets.

This snapshot is committed with the task files. Integration follows a fresh fetch/rebase onto origin/main, a separate Animation-guidance documentation commit, and an ordinary history-preserving main push. Final commit IDs and remote verification are reported in the chat's delivery response; this record's HEAD-at-stop field intentionally identifies the stopping point.

## Post-rebase preservation verification

The preservation commit rebased onto `074c6a02e32d1d0c6960425218e8abec83e3c9b0` as `1c1a3ecf669bef4b417de3e521aac0ab3698c50b`. The add/add conflict in the animation-directory attributes was resolved by retaining concurrent main entries and appending this task's exact-path entries. The shared-scene and two anatomical library payload hashes still match their original source payloads. Main now supplies bundled Game Rig Tools and a combined tools installer; the initial missing-add-on environment blocker is resolved by that concurrent contribution, while the user's no-bake instruction continues to apply. No further authoring or rendering was performed.

Read-only saved-action inspection found a concrete playback blocker: all twelve sources have serialized `animation_file_tracks` bindings with influence 0.0. Eleven also retain action/strip bounds 0–1 despite authored ranges of 0–96 or 0–384; `mazurka_transition_promenade_to_open_single_hand.blend` retains the expected 0–96 bounds. The saved-source inventory now records these bindings. Earlier in-memory motion passes therefore do **not** establish successful native chooser playback. Correct the bindings only after renewed authoring authorization, then review fresh-process native NLA playback. The generator also sets finger controls to XYZ and keys Euler rotation in memory; the shared rig uses quaternion finger controls according to the current Animation guidance. Saved finger channel compatibility remains a separate blocker to verify and correct. These sources are editable procedural studies, not finished playable clips.

Post-rebase verification with the same commands above: fast suite **10/10 passed**, scoped suite **14/14 passed**, and Blender 5.2.2 read-only inspection **12/12 passed** for source inventory, paired slots, sizes, and absence of baked actions. Logs are `post_rebase_fast.log`, `post_rebase_related.log`, and `post_rebase_inspection.log` in the evidence directory. These tool checks leave the recorded choreography and playback failures outstanding. The initial post-rebase inspection invocation used the repository root and failed to find the relative script; the corrected app-directory invocation passed. The root storage policy check passed after rebasing.

## Remaining work and exact resumption

Continue only after a new instruction to resume animation work. The proposed code repertoire contains 34 entries: five holds, nineteen movement loops, and ten directional transitions. Twelve sources exist, including the failed turn study. The other **22 defined entries remain unsaved**: seventeen movement loops and five transitions. Regional improvisations beyond that defined list require further choreography design; this snapshot supplies a partial repertoire.

Concrete remaining work:

1. Correct the recorded saved NLA range/influence and finger-channel compatibility blockers after renewed authorization. Reopen the preserved sources through the combined library and inspect their surfaces, contact fingers, wrists, heads, and partner clearance in playback.
2. Reconstruct contact metadata for the seven earlier hold/basic/turn sources before applying the newest review helper to them.
3. Re-author and validate the clockwise turn's wider step; validate counterclockwise turning separately. The saved turn remains a failing study.
4. Finish the reverse-promenade return; verify the latest free-hand reach projection across every transition. The final counter entry passed, but the revised generator's complete repertoire remains untested.
5. Generate/review the remaining defined movement and transition sources; sample interpolation and loop velocities; inspect motion and actual mesh surfaces. Keep each source's state and evidence explicit.
6. Preserve the user's no-bake instruction until they change it. Runtime exports and runtime integration remain outside this delivered snapshot.

Read-only inspection can be repeated with the commands above. After explicit resumption, use a new branch and run selected authoring first (these commands write source files):

```bash
cd /workspace/sanjo-solutions
# After fetching current main and creating an isolated resumption branch:
git switch -c codex/resume_balfolk_mazurka
cd apps/a-game
blender --version
blender --background --python-exit-code 1 \
  --python scripts/blender/install_animation_tools.py
# First resolve the saved playback blockers above in the authoring code.
# Then verify the turn correction; keep the failed snapshot in Git history.
blender --background animations/man_and_woman/share_company.blend \
  --python-exit-code 1 --python scripts/player_assets/author_balfolk_mazurka.py \
  -- --only 'mazurka_turn_*'
# Then finish the interrupted transition pair.
blender --background animations/man_and_woman/share_company.blend \
  --python-exit-code 1 --python scripts/player_assets/author_balfolk_mazurka.py \
  -- --only 'mazurka_transition_*promenade_reverse*'
# A complete regeneration is a later authoring step, after those reviews pass.
blender --background animations/man_and_woman/share_company.blend \
  --python-exit-code 1 --python scripts/player_assets/author_balfolk_mazurka.py
```

The generator raises on failed review and retains earlier completed outputs. A partial `mazurka_review.json` remains partial even when each entry it contains passed. Inspect actual binary sizes and add exact-path Git attribute exceptions for each newly created file before staging it.
