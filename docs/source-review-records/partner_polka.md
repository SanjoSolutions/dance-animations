# Partner polka — stopped and preserved

- Date: 2026-10-02 (UTC). Last saved generation output: `chasse_right`, 15:01 UTC.
- Chat title: Create Partner polka animations. Chat ID: `01a0fcfb-b89b-7575-9480-0d2e1c8ce048`.
- Stop instruction: delegated from `01a0fd1a-3673-7683-ae29-577f2ee1a927`; preservation, verification, commits, and delivery take precedence over further animation work.
- Branch at stop: `codex/partner-polka`. Base/current commit before preservation: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Original scope: a broad Partner polka repertoire for both characters in `man_and_woman3.blend`, including positions, steps, turns, transitions, natural motion, contacts, clearance, loop validation, individual source files, exports, documentation, and main delivery.
- Completion: partial procedural animation studies. Sixteen sources and sixteen exports saved; thirteen current sources pass saved interpolated target checks; fourteen sources match their baked actions. The full requested repertoire and artistic validation remain pending.

## Authoring and saved assets

All Blender work used `/workspace/.cloud-onboarding/bin/blender`, Blender **5.2.2 LTS**, build `d13f752e3b9c`. Sources use the existing per-animation file workflow and linked `shared_scene_data.blend`; `man_and_woman3.blend` discovers these actions through that workflow. Existing source files remain unchanged. Reused the idle setup, paired authoring/calibrated palm helpers, and `DiscoWristPoser` wrist orientation helper after inspecting the existing animation library. The polka choreography itself is newly authored procedural work.

Every listed source contains an authoring action named `partner_polka_<figure>` with `Man.rigify` and `Woman.rigify` slots, plus `<action>.baked` with both deform-rig slots. The man/player leads and the woman/partner follows the coordinated motion. Timing is 24 fps at 120 BPM. Native Blender `bake_action_objects` produced the saved bakes. Game Rig Tools was unavailable, so its UI bake workflow was not exercised. Existing single-animation export layout validation and update publication helpers produced the GLBs, each containing one animation and 1,263 channels for both roles.

Source paths are `animations/man_and_woman/partner_polka_<figure>.blend`. Export import settings are beside each GLB as `<file>.glb.import`.

| Figure | Inclusive frames | Source bytes | Export path | Saved state |
| --- | --- | ---: | --- | --- |
| `basic_step_close_step_hop` | 0–48 | 2,080,647 | `models/player/animation_updates/partner_polka_basic_step_close_step_hop_baked_b9277a89bcbe.glb` | Saved target checks and bake comparison pass |
| `chasse_left` | 0–48 | 2,175,337 | `models/player/animation_updates/partner_polka_chasse_left_baked_62c2c0807d64.glb` | Saved target checks and bake comparison pass |
| `chasse_right` | 0–48 | 2,194,024 | `models/player/animation_updates/partner_polka_chasse_right_baked_80de5c81f409.glb` | Saved target checks and bake comparison pass |
| `closed_to_open_double` | 0–96 | 1,686,199 | `models/player/animation_updates/partner_polka_studies/partner_polka_closed_to_open_double_baked_f3e6c09a829c.glb` | BLOCKING STUDY: saved source differs from bake; export quarantined |
| `hold_closed` | 0–48 | 1,887,268 | `models/player/animation_updates/partner_polka_hold_closed_baked_c712887b2651.glb` | Saved target checks and bake comparison pass |
| `hold_counter_promenade` | 0–48 | 1,976,952 | `models/player/animation_updates/partner_polka_hold_counter_promenade_baked_fc20177abc35.glb` | Saved target checks and bake comparison pass |
| `hold_open_double` | 0–48 | 1,895,766 | `models/player/animation_updates/partner_polka_hold_open_double_baked_91cf79469794.glb` | Saved target checks and bake comparison pass |
| `hold_open_single` | 0–48 | 1,889,354 | `models/player/animation_updates/partner_polka_hold_open_single_baked_628ecc4aed2d.glb` | Saved target checks and bake comparison pass |
| `hold_promenade` | 0–48 | 1,954,348 | `models/player/animation_updates/partner_polka_hold_promenade_baked_c28ca5ecb598.glb` | Saved target checks and bake comparison pass |
| `hold_shadow` | 0–48 | 1,887,355 | `models/player/animation_updates/partner_polka_hold_shadow_baked_898404aeb6c5.glb` | Saved target checks and bake comparison pass |
| `hold_side_by_side` | 0–48 | 1,920,812 | `models/player/animation_updates/partner_polka_hold_side_by_side_baked_74ea0aa67a6a.glb` | Saved target checks and bake comparison pass |
| `hold_varsouvienne` | 0–48 | 1,946,944 | `models/player/animation_updates/partner_polka_hold_varsouvienne_baked_f7f8611aba4d.glb` | Saved target checks and bake comparison pass |
| `natural_turn` | 0–96 | 1,981,132 | `models/player/animation_updates/partner_polka_studies/partner_polka_natural_turn_baked_805e215e8071.glb` | BLOCKING STUDY: saved source differs from bake; export quarantined |
| `progressive_backward` | 0–48 | 2,200,070 | `models/player/animation_updates/partner_polka_progressive_backward_baked_999f29be4983.glb` | Saved target checks and bake comparison pass |
| `progressive_forward` | 0–48 | 2,206,221 | `models/player/animation_updates/partner_polka_progressive_forward_baked_6b38fcf65712.glb` | Saved target checks and bake comparison pass |
| `underarm_turn_left` | 0–144 | 5,566,390 | `models/player/animation_updates/partner_polka_underarm_turn_left_baked_a56ecf9a2eb0.glb` | Earlier prototype: bake comparison passes; saved target calibration pending |

The eight holds include a small breathing/sway loop. Basic step-close-step-hop also loops. Progressive and chassé clips retain travel and import with looping disabled. Underarm left imports as a six-second loop. These are procedural blocking studies pending comprehensive visual review, including detailed fingers, shoulders, balance, and mesh clearance.

The two older `natural_turn` and `closed_to_open_double` exports and their original malformed import settings are preserved unchanged under `models/player/animation_updates/partner_polka_studies/`, protected by `.gdignore`. Their active manifest references were removed during preservation to keep malformed imports out of normal Godot import. Their source files remain beside the other sources to preserve relative library links; the combined Blender library can still discover these study actions. `partner_polka_evidence/animation_updates_at_stop.tres` preserves the original manifest. Current `models/player/animation_updates.tres` contains fourteen task exports plus all six pre-existing entries at the stopping point.

`underarm_turn_left` is an earlier prototype with correct reopened bake correspondence but lacks saved hold-target calibration metadata. Its original in-memory target report passed; the later saved-source target review remains pending. This distinction is explicit in its verification JSON.

## Relevant code and evidence

- `scripts/player_assets/partner_polka.py`: 49 figure specifications, eight holds, paired target/support schedules, regional variations, and fourteen planned hold transitions.
- `scripts/player_assets/author_partner_polka.py`: sparse IK authoring, enum property keys, quaternion continuity, constant-curve simplification, native paired bake, per-animation source save and GLB publication. Generation stopped after the thirteenth current-generation figure. Earlier studies account for three additional saved files.
- `scripts/player_assets/review_partner_polka.py`: saved-source evaluation and bake comparison; optional rendering exists but is paused by the stop instruction.
- `docs/animation_reviews/partner_polka/*.json`: sixteen original in-memory generation reports. Earlier study reports describe their live authoring state, not successful reopened-source validation.
- `docs/animation_work_status/partner_polka_evidence/*_verification.json` and corresponding logs: all sixteen reopened sources, frame ranges, slots, target review where available, and every-integer-frame bake comparisons.
- `partner_polka_evidence/verify_saved_sources.py`: exact preservation verifier used; records earlier-study failures rather than raising before writing evidence. Its path configuration reflects this cloud checkout.
- `partner_polka_evidence/verify_godot_imports.gd`: actual Godot library/role/duration/loop verification script.
- `partner_polka_evidence/polka-all.log`, `polka-underarm.log`, `polka-reopen.log`, `polka-shadow-review.log`: saved authoring/reopen logs, including interrupted runs.
- Six already-rendered PNGs: closed hold frames 0, 12, 24, 36 and shadow hold frames 0, 24. These limited Workbench views are preserved as produced; rendering stopped before the rest of the review. EGL initialization emitted warnings while saved images were produced.
- `partner_polka_evidence/file_inventory.json`: exact relevant file paths, byte sizes, and SHA-256 digests at preservation time. The inventory excludes itself and this status record.
- App `.gitattributes`: individual exceptions only for the 38 task binary files (16 sources, 16 GLBs, six PNGs), each at most 100 MiB. All task binaries are direct Git blobs; larger existing dependencies retain their existing LFS attributes.

## Verification results and limits

1. `GODOT=/workspace/.cloud-onboarding/bin/godot python tests/run_tests.py --suite fast`: **9/9 pass**. An initial attempt failed because the default Godot was 4.6.3 and hair assets were LFS pointers. Fetching those existing LFS objects and selecting Godot 4.7.2 resolved the environment issues. Final log: `partner_polka_evidence/polka-fast.log`.
2. `GODOT=/workspace/.cloud-onboarding/bin/godot BLENDER=/workspace/.cloud-onboarding/bin/blender python tests/run_tests.py --changed scripts/player_assets/test_paired_animation_authoring.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_single_animation_layout.py --changed scripts/player_assets/test_motion_review.py`: **14/14 pass**, including nine fast and five related slow checks. Log: `partner_polka_evidence/polka-related-tests.log`. The entire unrelated slow suite was not run.
3. Read-only reopen checks: thirteen sources pass half-frame interpolation sampling and contact-boundary samples. Limits: target error 0.025 m, planted drift 0.004 m, held-hand error 0.008 m, torso proxy gap 0.02 m, foot proxy gap 0.005 m, loop position 0.004 m, rotation 0.04 radians, velocity 0.12. Traveling clips are intentionally nonlooping. These checks use positional proxies, not full mesh collision certification.
4. Native baked versus author-driven deform matrices at every integer frame: fourteen pass the 0.0001 threshold; maximum passing error about 0.000012696. `closed_to_open_double` fails at 1.9336615 and `natural_turn` at 1.9527953. Earlier enum-parent and rotation-mode state was not fully serialized into those two sources. Their preserved exports describe the earlier live pose, so those files require repair after authorization resumes.
5. Godot 4.7.2 isolated import of all fourteen active GLBs: **14/14 pass**, each one `AnimationLibrary` animation, 1,263 tracks, both deform skeletons, expected duration and loop flags. Logs: `polka-godot-import.log`, `polka-godot-verify.log`. This verifies the exported libraries, not full in-game choreography or mesh appearance.
6. Binary inspection: valid GLB containers and paired channels; every task binary is below 104,857,600 bytes. Actual sizes and exact-path attributes were checked before staging; all 38 staged binary blob lengths matched their files. The post-rebase `python scripts/lfs_policy.py check` passed for 24,912 indexed files. Direct-Git assets travel with the ordinary Git push; this task adds no LFS assets or separate hosted-asset upload requirement.

## Processes and exact stopping point

Owned authoring and rendering processes received SIGINT and then SIGTERM when SIGINT did not finish them. Saved outputs were preserved. The read-only preservation verifier completed all sixteen sources afterward; the isolated Godot verifier completed all fourteen active exports. At this record's completion, no task-owned Blender authoring, rendering, or verification process remains running. Temporary `/tmp/polka_import_check` holds the verification fixture; `.cache/player_assets/polka_export.glb` is a redundant last-export cache. Durable outputs and relevant logs are included in this commit. Authentication helpers and credentials remain outside the repository.

## Remaining work and blockers

The user's explicit stop instruction is the current blocker to further authoring, refinement, baking, exporting, and rendering. Resume requires a new instruction. The 33 planned figures with no saved source are:

`reverse_turn`, `quarter_turns`, `rock_step`, `heel_toe`, `kick_polka`, `heel_click`, `galop_left`, `galop_right`, `promenade_travel`, `counter_promenade_travel`, `side_by_side_basic`, `shadow_basic`, `varsouvienne_basic`, `open_double_basic`, `open_single_basic`, `change_places_left`, `change_places_right`, `couple_circle_left`, `couple_circle_right`, `underarm_turn_right`, `open_double_to_closed`, `closed_to_open_single`, `open_single_to_closed`, `closed_to_promenade`, `promenade_to_closed`, `closed_to_counter_promenade`, `counter_promenade_to_closed`, `closed_to_side_by_side`, `side_by_side_to_closed`, `closed_to_shadow`, `shadow_to_closed`, `closed_to_varsouvienne`, `varsouvienne_to_closed`.

After authorization, repair the two saved-source mismatch studies and their import metadata; restore saved target metadata for the underarm prototype; validate each remaining movement before publication; evaluate all interpolated contact and clearance reports; perform comprehensive visual review; validate hold-to-move and move-to-hold endpoint compatibility and transition continuity. The current 49-entry catalog is a broad working scope, not a claim that every regional Partner polka variation is represented.

## Exact verification and future resume commands

Run commands from `/workspace/sanjo-solutions/apps/a-game`. These verification commands only read saved Blender assets:

```bash
GODOT=/workspace/.cloud-onboarding/bin/godot python tests/run_tests.py --suite fast
/workspace/.cloud-onboarding/bin/blender -b animations/man_and_woman/partner_polka_hold_closed.blend --python-exit-code 1 --python docs/animation_work_status/partner_polka_evidence/verify_saved_sources.py
```

Repeat the second command for each source in the inventory to reproduce the recorded source comparisons. The evidence verifier writes JSON/log results and its optional rendering flag must remain unused during the stop period.

To reproduce GLB verification, create an isolated project with `config_version=5` in `project.godot`, copy the fourteen top-level `models/player/animation_updates/partner_polka_*.glb` and adjacent import files to its root, copy `scripts/player_assets/import_player_animations.gd` to the same relative path in the fixture, and copy the saved verifier to its root. Then run:

```bash
/workspace/.cloud-onboarding/bin/godot --headless --editor --path /tmp/polka_import_check --import
/workspace/.cloud-onboarding/bin/godot --headless --path /tmp/polka_import_check --script verify.gd
```

Only after renewed authoring authorization, these commands resume the saved implementation:

```bash
# Repair/rebuild earlier studies explicitly; --resume alone skips existing studies.
/workspace/.cloud-onboarding/bin/blender -b animations/man_and_woman/idle.blend --python-exit-code 1 --python scripts/player_assets/author_partner_polka.py -- --only natural_turn closed_to_open_double underarm_turn_left
# Continue figures that have no source yet.
/workspace/.cloud-onboarding/bin/blender -b animations/man_and_woman/idle.blend --python-exit-code 1 --python scripts/player_assets/author_partner_polka.py -- --resume
# Reopen individual outputs before any further publication.
/workspace/.cloud-onboarding/bin/blender -b animations/man_and_woman/partner_polka_hold_closed.blend --python-exit-code 1 --python scripts/player_assets/review_partner_polka.py
```

The library dependencies are existing LFS assets: `man_and_woman3.blend`, `animations/man_and_woman/shared_scene_data.blend`, `idle.blend`, anatomical source libraries, and `models/player/animations.glb`. Use the configured GitHub account and repository LFS workflow to hydrate them in a fresh checkout. Keep Blender at 5.2 for every Blender operation. The cloud executable is 5.2.2 LTS; Godot verification uses the explicit 4.7.2 executable above.

## Integration verification

The preservation commit was rebased onto `3f53f0f50` as `1c82f4504bf5867be8700e5f6dcbcbe8f0047ba6`. Conflicts in app attributes and the runtime manifest were resolved by preserving both tasks' entries: all 83 existing remote animation references plus fourteen active Partner polka references (97 total at this integration point). Concurrent animation work and source assets were preserved.

The same fast-plus-related command was rerun after rebase: **15/15 pass**; log `partner_polka_evidence/polka-post-rebase-tests.log`. The shared scene and both anatomical source binaries changed Git storage on main, while their SHA-256 contents match the original verification dependencies exactly: shared scene `18a0f6bb84cc90426444e4bf4c81d78e3b81ebd84097a7c16afc098cd9948130`, man `6144ac70e971bff82f432f0930eb0fe8e5c18e16ba99f8193aa8738af6b67c55`, woman `d9b123f681bd8c343ed861ec8d9c8b512bede54ae0b93c8cefb33acfafda96e9`. The library tooling change uses numeric ID-property reference keys for long action names; it preserves source composition behavior.

The following documentation commit adds numeric Rigify enum-key guidance and individual GLB import guidance to the `# Animation` section of `AGENTS.md`. Current main also supplies bundled Game Rig Tools setup; the availability statement above describes the earlier authoring environment. Future resumed work should read current repository instructions and install its bundled tools before opening source scenes. Final merge and push hashes are reported in the chat delivery because a commit cannot contain its own final hash.
