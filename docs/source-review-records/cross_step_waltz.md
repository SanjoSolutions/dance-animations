# Cross-step waltz preservation status

- Date: 2026-10-02 UTC; preservation recorded after the stop instruction.
- Chat/task title: Create Cross-step waltz animations for man_and_woman3.blend (descriptive task title; UI title unavailable).
- Project: A-Game, `/workspace/sanjo-solutions/apps/a-game`, sanjo-solutions cloud environment.
- Task branch: `codex/cross-step-waltz`.
- Current commit at stop: `3c52737c74b488501e9cfe47e7029547c6f5fe88`; all task work was still local at this point.
- Delivery authority: user instructed all animation chats to stop animation work, record state, commit durable outputs, integrate concurrent main, and push normally.
- State: **partial authored procedural blocking studies**, pending choreography and visual acceptance. 43 saved paired sources; 0 baked clips; 0 runtime exports. These sources are discoverable by the existing file workflow, so consumers should consult this status before using them as finished motion.

## Original scope and stopping point

The original request was a broad, organized Cross-step waltz repertoire for both characters, both lead-role variants, natural planted contacts, body clearance, smooth transitions, interpolated validation, and Blender 5.2 throughout. The planned catalog contains 41 figures per lead role (82 paired sources): eight positions, three foundations, seven travel figures, six turns, three rhythm/open figures, and fourteen directed hold transitions. Cross-step waltz has an open-ended vocabulary; this was the intended coverage, rather than a claim of every teacher-specific variation.

Saved: 21 man-lead and 22 woman-lead sources, each containing BOTH `Man.rigify` and `Woman.rigify`. Eight positions in both roles, basic/reverse/side cross, four travel directions, natural/reverse turns, hesitation, open break, butterfly cross, and shadow walk exist in both roles. Grapevine exists only in woman-lead. Both promenade walks failed palm reach during authoring. Man-lead grapevine, the eight solo/underarm/wheel variants, and all 28 directed-transition variants remain unsaved. Thus 39 intended sources remain absent.

Both author workers were terminated. The last man catalog includes shadow walk; the woman catalog includes grapevine. An underarm-turn attempt had begun and produced no saved source. The current generator contains a later consecutive-footfall separation planner and adaptive swing arc that were being explored in memory. **The current generator does not reproduce the saved sources byte-for-byte or represent a validated replacement.** Its coarse probe still found shin/foot overlap in natural and reverse turns. Preserve it as an unfinished procedural study, requiring renewed user authorization before further animation work.

## Files, architecture, and authoring state

- `scripts/create_cross_step_waltz.py`: partial generator using `PairedAnimationAuthoring`, the existing disco forearm-relative wrist calibration, `RigYogaPoser`, `ActivityMotionAuthor`, and `AnimationFileWriter`. It preserves native wrist constraints, uses sparse meaningful IK poses, reduces constant curves, and records paired action/NLA metadata. Existing dance clips were inspected for reuse; their footwork differed, so paired authoring and wrist tooling were reused instead of claiming reused finished choreography.
- `scripts/validate_cross_step_waltz.py`: saved-source interpolation validator and historical render helper. Reports include dependency hashes, slots, timing, reach, foot plants, palms, floor, torso/leg proxies, motion, and loop pose/velocity. The latest generator study changes expected foot targets, so prior sampled results are historical and a fresh validation after approved regeneration is required.
- `scripts/cross_step_waltz.md`: intended coverage, timing, workflow, and explicit partial-state notice.
- `animations/man_and_woman/cross_step_waltz_catalog.json`: preservation merge of both worker catalogs, all 43 saved sources, two authoring failures, and explicit authored/baked/exported counts.
- `animations/man_and_woman/cross_step_waltz_validation.json`: the last completed 33-source sampled report, with its original dependency hashes and `passed: false`.
- `animations/man_and_woman/.gitattributes`: exact-filename ordinary-Git exceptions for these 43 small sources; previous assets retain their rules.
- `docs/animation_work_status/cross_step_waltz_evidence/`: frozen worker catalogs, earlier canonical records, validation reports, existing review images, interrupted test/build/probe logs, read-only audit script/report, and file manifest. The manifest enumerates each evidence file and hash.
- Shared scene, anatomical rigs, and `man_and_woman3.blend` remain unchanged. Blender/Godot dependency downloads only hydrated existing LFS objects. Incidental Godot import edits from this task were restored individually.

24 fps, 120 BPM, 12 frames per beat. Position/basic/travel sources generally store 0–72; natural/reverse turn sources store 0–144. For loops the endpoint duplicates frame 0 and playback ends one frame earlier. Traveling clips play through their endpoint. Exact ranges and role assignments follow. Every row is authored-only; baked and exported states are false. Sampled status refers to a matching saved-file SHA-256 in the historical report, not full visual acceptance.

| Source filename under animations/man_and_woman | Lead | Stored frames | Playback end | Prior sampled result |
| --- | --- | --- | --- | --- |
| `cross_step_waltz_basic_man_lead.blend` | man_lead | 0–72 | 71 | passed |
| `cross_step_waltz_basic_woman_lead.blend` | woman_lead | 0–72 | 71 | passed |
| `cross_step_waltz_butterfly_cross_man_lead.blend` | man_lead | 0–72 | 71 | pending |
| `cross_step_waltz_butterfly_cross_woman_lead.blend` | woman_lead | 0–72 | 71 | pending |
| `cross_step_waltz_grapevine_woman_lead.blend` | woman_lead | 0–72 | 72 | pending |
| `cross_step_waltz_hesitation_man_lead.blend` | man_lead | 0–72 | 71 | pending |
| `cross_step_waltz_hesitation_woman_lead.blend` | woman_lead | 0–72 | 71 | pending |
| `cross_step_waltz_natural_turn_man_lead.blend` | man_lead | 0–144 | 143 | failed |
| `cross_step_waltz_natural_turn_woman_lead.blend` | woman_lead | 0–144 | 143 | failed |
| `cross_step_waltz_open_break_man_lead.blend` | man_lead | 0–72 | 71 | pending |
| `cross_step_waltz_open_break_woman_lead.blend` | woman_lead | 0–72 | 71 | pending |
| `cross_step_waltz_position_butterfly_man_lead.blend` | man_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_butterfly_woman_lead.blend` | woman_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_closed_man_lead.blend` | man_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_closed_woman_lead.blend` | woman_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_open_one_hand_man_lead.blend` | man_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_open_one_hand_woman_lead.blend` | woman_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_open_two_hand_man_lead.blend` | man_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_open_two_hand_woman_lead.blend` | woman_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_promenade_man_lead.blend` | man_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_promenade_woman_lead.blend` | woman_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_reverse_promenade_man_lead.blend` | man_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_reverse_promenade_woman_lead.blend` | woman_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_shadow_man_lead.blend` | man_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_shadow_woman_lead.blend` | woman_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_side_by_side_man_lead.blend` | man_lead | 0–72 | 71 | passed |
| `cross_step_waltz_position_side_by_side_woman_lead.blend` | woman_lead | 0–72 | 71 | passed |
| `cross_step_waltz_reverse_cross_man_lead.blend` | man_lead | 0–72 | 71 | passed |
| `cross_step_waltz_reverse_cross_woman_lead.blend` | woman_lead | 0–72 | 71 | passed |
| `cross_step_waltz_reverse_turn_man_lead.blend` | man_lead | 0–144 | 143 | pending |
| `cross_step_waltz_reverse_turn_woman_lead.blend` | woman_lead | 0–144 | 143 | failed |
| `cross_step_waltz_shadow_walk_man_lead.blend` | man_lead | 0–72 | 72 | pending |
| `cross_step_waltz_shadow_walk_woman_lead.blend` | woman_lead | 0–72 | 72 | pending |
| `cross_step_waltz_side_cross_man_lead.blend` | man_lead | 0–72 | 71 | passed |
| `cross_step_waltz_side_cross_woman_lead.blend` | woman_lead | 0–72 | 71 | passed |
| `cross_step_waltz_traveling_backward_man_lead.blend` | man_lead | 0–72 | 72 | failed |
| `cross_step_waltz_traveling_backward_woman_lead.blend` | woman_lead | 0–72 | 72 | failed |
| `cross_step_waltz_traveling_forward_man_lead.blend` | man_lead | 0–72 | 72 | passed |
| `cross_step_waltz_traveling_forward_woman_lead.blend` | woman_lead | 0–72 | 72 | passed |
| `cross_step_waltz_traveling_left_man_lead.blend` | man_lead | 0–72 | 72 | failed |
| `cross_step_waltz_traveling_left_woman_lead.blend` | woman_lead | 0–72 | 72 | failed |
| `cross_step_waltz_traveling_right_man_lead.blend` | man_lead | 0–72 | 72 | failed |
| `cross_step_waltz_traveling_right_woman_lead.blend` | woman_lead | 0–72 | 72 | failed |

## Validation and concrete blockers

1. Required fast suite: `python tests/run_tests.py --suite fast` **10/10 passed in 10.02 seconds**, after stopping authoring. Full output: `cross_step_waltz_evidence/waltz_preservation_fast.log`.
2. Read-only Blender 5.2.2 audit: **43/43 passed** actual size, real binary, catalog/file correspondence, two slots, BOTH participant metadata, action ranges, and serialized NLA owner/slot/timing checks. Each asset is 120,647–187,647 bytes, totaling 5,822,133 bytes. Exact sizes/SHA-256 values: `saved_source_inventory.json`. This audit loads actions only; it creates no poses or Blender source files.
3. `python -m py_compile scripts/create_cross_step_waltz.py scripts/validate_cross_step_waltz.py`: passed.
4. Prior interpolation report: 33 saved-file hashes match, 24 passed, 9 failed leg-capsule clearance; 10 sources await sampled validation. Failing sources: backward/left/right travel and natural turn for both lead roles, plus woman-lead reverse turn. Interpolation spacing 1.5 frames; loop derivatives sampled 0.25 frames from each endpoint. Tolerances: IK 0.005 m, plant XY drift 0.004 m, palm gap 0.025 m, floor penetration 0.012 m, torso proxy gap >=0, leg capsule penetration <=0.005 m, loop pose 0.0001 m, loop velocity difference 0.018 m/frame. The nine failures are genuine pending motion issues, not waived checks.
5. Last coarse in-memory planner probe was terminated. Completed probe figures: basic, backward travel, left travel, natural turn, reverse turn, grapevine, underarm turn right. Natural turn minimum proxy gap -0.042015 m and reverse turn -0.028622 m still fail. These are coarse 6-frame man-lead study samples, not acceptance results or saved assets. Closed-to-shadow probe was incomplete.
6. Related suite command: `BLENDER=/tmp/a-game-blender52 PATH=/tmp/a-game-tools:$PATH python tests/run_tests.py --suite changed --changed animations/man_and_woman/cross_step_waltz_basic_man_lead.blend --slow-timeout 90`. Its fast checks passed 10/10; among completed slow checks 6 passed and 11 failed. The 18th slow check (`test_pair_animation_player_pose.gd`) was interrupted under the stop instruction. The suite did not complete. Preserved full log: `waltz_scoped_tests.log`. Failures include existing Godot character resource/texture imports, `Woman_rigify_deform/Skeleton3D:DEF-shoulder.L` assertion, scene instantiation errors, and 90-second timeouts. Source-only waltz changes have no runtime export; runtime integration remains unverified. Earlier dependency hydration resolved initial hair-mesh LFS-pointer fast-test failures.
7. Historical reviews: 16 existing PNGs, frames 0/18/36/54, covering early basic man-lead plus closed-position role variants. `review/` and `refined_review/` predate the final saved basic source revision. `early_review/` records closed positions. These are partial historical images, not full-library playback approval. No further frames were rendered after the stop instruction. Turns, most travel, missing transitions, finger ergonomics, and full mesh interpenetration still need visual review after authorization.

## Process and environment state

All owned Blender authoring/probe and Godot suite processes are stopped. SIGTERM was sent to the final probe PID 5764 and suite PID 5040; the runner cleaned its active child. Defunct Python test-fixture children adopted by PID 1 are exited zombies, with no running computation or asset writes. Final preservation audit and fast-suite processes completed. Current outputs have been copied from ignored `.cache/cross_step_waltz` and `/tmp` into the evidence directory; these original temporary paths are optional local copies.

All Blender work used `/tmp/blender-5.2.2-linux-x64/blender`, Blender 5.2.2 LTS build `d13f752e3b9c`. The system Blender is 4.3.2 and must be bypassed. The temporary single-thread wrapper `/tmp/a-game-blender52` and PATH symlink `/tmp/a-game-tools/blender` point to 5.2.2. Godot is 4.6.3. Fresh environments must retrieve actual LFS dependencies; existing source pointers cannot be opened as Blender assets. Credentials stay in environment-backed Git authentication, with no credentials stored here.

## Exact verification and future resume commands

These verification commands preserve source files:

```sh
cd /workspace/sanjo-solutions/apps/a-game
BLENDER=/tmp/blender-5.2.2-linux-x64/blender
"$BLENDER" --version
python tests/run_tests.py --suite fast
"$BLENDER" -t 1 --background --factory-startup --disable-autoexec --python-exit-code 1 \
  --python docs/animation_work_status/cross_step_waltz_evidence/inspect_saved_sources.py
python -m py_compile scripts/create_cross_step_waltz.py scripts/validate_cross_step_waltz.py
```

**Run the following authoring commands only after the user authorizes animation work to resume.** First review the frozen reports, repair the planner and palm reach, and retain the committed sources as the comparison baseline. The following starts a fresh focused catalog; `--resume` skips names in an existing catalog even if generator code changed, so it must not be used to imply regeneration of revised figures.

```sh
cd /workspace/sanjo-solutions/apps/a-game
BLENDER=/tmp/blender-5.2.2-linux-x64/blender
mkdir -p .cache/cross_step_waltz/resume
"$BLENDER" -t 1 --background animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/create_cross_step_waltz.py \
  -- --only basic --roles 0 1 --catalog .cache/cross_step_waltz/resume/basic_catalog.json
"$BLENDER" -t 1 --background animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/validate_cross_step_waltz.py \
  -- --catalog .cache/cross_step_waltz/resume/basic_catalog.json \
  --report .cache/cross_step_waltz/resume/basic_validation.json
"$BLENDER" -t 1 --background animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/create_cross_step_waltz.py \
  -- --catalog .cache/cross_step_waltz/resume/full_catalog.json
"$BLENDER" -t 1 --background animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/validate_cross_step_waltz.py \
  -- --catalog .cache/cross_step_waltz/resume/full_catalog.json \
  --report .cache/cross_step_waltz/resume/full_validation.json \
  --render .cache/cross_step_waltz/resume/review
BLENDER=/tmp/a-game-blender52 PATH=/tmp/a-game-tools:$PATH python tests/run_tests.py \
  --suite changed --changed animations/man_and_woman/cross_step_waltz_basic_man_lead.blend --slow-timeout 90
```

Full generation replaces existing task source filenames; review diffs and reports before publishing. Future acceptance requires completing 39 missing sources, fixing nine saved-source clearance failures and both promenade palm failures, checking all role variants and directed transitions, validating new saved sources against the exact authoring revision, and reviewing interpolated playback. Baking/exporting remain separate requested delivery stages.

## Storage and integration record

All preserved sources and images are below 104,857,600 bytes. Exact filename attributes place these intended task files in ordinary Git. Existing shared source LFS rules remain unchanged. The delivery checks compare staged blob sizes and SHA-256 values to working files and reject task LFS pointers. Consequently these new assets upload through ordinary Git, with no new LFS objects required.

This status records the pre-commit state; its containing task commit identifies the frozen artifacts. Delivery will fetch current origin/main, rebase the task changes while preserving concurrent work, commit the separate Animation guidance update, fetch immediately before main integration, and use ordinary pushes with retries through history-preserving integration. Final delivery reports identify the actual task/documentation/merge hashes and verified remote main. Every new commit carries exactly one Codex co-author trailer; repository communications for this task are Codex-authored.

### Post-rebase verification

Preservation commit after rebase: `f24c69063da41e8cce4aeea679ec411e49d9c08b`. Rebased onto `629cffdc1` from origin/main. Resolved the sole `.gitattributes` conflict by retaining all concurrent Tango, New York Hustle, solo cha-cha, and Cross-step waltz entries. Root `python scripts/lfs_policy.py check` passed for 24,482 staged files. The fast suite was repeated against the integrated checkout and passed **10/10 in 8.76 seconds** (`cross_step_waltz_evidence/post_rebase_fast.log`). The Animation section now links this partial study and records crossing-leg clearance and resume-catalog provenance lessons. Evidence has `.gdignore` to keep historical reviews outside Godot import discovery. Concurrent main may update shared dependencies; historical reports retain their original dependency hashes and stop commit.

Main integration subsequently fetched `88421f0cc`, retained every pre-merge main line in both conflicting additive files (`AGENTS.md` and the source `.gitattributes`), and repeated the fast suite: **10/10 passed in 9.97 seconds**. See `cross_step_waltz_evidence/main_integration_fast.log`. The merged-index storage policy passed for 26,990 files before this final log was added. Source hashes remain those recorded by the preservation audit.
