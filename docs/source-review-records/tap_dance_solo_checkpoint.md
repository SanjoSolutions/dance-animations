# Tap dance solo animation checkpoint

- Recorded: October 2, 2026 (Europe/Berlin), after the user's instruction to stop all animation authoring and preserve current work.
- Chat/task title: “Tap dance for man_and_woman3.blend — solo animations for both characters” (descriptive task label; the desktop title was unavailable).
- Project/environment: A-Game, `apps/a-game`, sanjo-solutions cloud environment.
- Task branch: `codex/tap-dance`.
- Base/current commit when animation work stopped: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Delivery state: **PARTIAL PROCEDURAL BLOCKING STUDY. Further animation work requires a new instruction to resume.** Saved outputs belong to several iterations; the current generator reproduces the latest experimental approach, rather than every earlier asset byte for byte.

## Original scope and stopping point

The original request covered a broad tap vocabulary, positions, transitions, planted contacts, body clearance, loop continuity, and independent man/woman animations for `man_and_woman3.blend`. It required Blender 5.2 throughout, the repository's per-animation workflow, reuse of fitting existing motion, direct Git storage through 104,857,600 bytes, commits, rebasing, an Animation documentation update, main integration, and pushing.

Preparation read the root and A-Game AGENTS files, animation workflow, paired IK authoring, and motion-review documentation. Blender **5.2.2 LTS**, build `d13f752e3b9c`, performed all Blender authoring, baking, export, rendering, and evaluation. Required LFS source assets were fetched through the configured GitHub identity. Existing `RigYogaPoser`, `YogaPoseLibrary` mountain pose, and `DiscoCharacter` proportion/wrist helpers were reused. The existing disco action itself remained unchanged.

The procedural definitions cover **56 named moves/positions**, planned as **210 independent clips** after actor and lead-foot variants. Generation stopped during partial execution. Saved-file bake equivalence and surface calibration were being investigated. **Zero clips have completed the full acceptance process.** Initial successful contact reports establish only their recorded checks in that authoring process.

## Durable files and asset state

[checkpoint_inventory.json](tap_dance_evidence/checkpoint_inventory.json) enumerates every saved source, export, import configuration, and per-clip report with its exact repository-relative path, byte size, SHA-256, and available roles/frame ranges. This inventory is the authoritative asset list for this checkpoint.

| Group | Saved state |
| --- | --- |
| `scripts/tap_dance_repertoire.py` | 56 vocabulary definitions, event tokens, mirrored lead-foot variants, and ten position definitions. Several named combinations remain preliminary approximations. |
| `scripts/create_tap_dance.py` | Experimental sparse IK generator, author-process half-frame contact checks, visual matrix bake, per-animation writer, and compact GLB export. Preserved at the exact stopping revision. |
| `scripts/review_tap_dance.py` | Saved-source reload, editable/baked comparisons, knee-angle checks, planted-foot rotation, and loop angular velocity checks. Latest run fails. |
| `animations/man_and_woman/tap_*.blend` | **95** partial per-animation source files created using `AnimationFileWriter` and the existing `shared_scene_data.blend`. The writer saves an authoring action and matching `.baked` action family; full independent reload verification remains pending for this collection. |
| `models/player/animation_updates/tap_*.glb` | **94** partial exported GLBs. 93 contain one baked animation; the earlier `tap_man_wing_left_baked_4ab105cd9b95.glb` contains an additional authoring animation and remains an explicitly failed export experiment. |
| `models/player/animation_updates/tap_*.glb.import` | **94** import configurations. Later exports use compact settings and a linear loop; earlier files retain the settings from their generation iteration. |
| `animations/tap_dance/tap_*.json` | **94** author-process reports: **50 man** (`PLAYER`) and **44 woman** (`PARTNER`). Each report identifies its exact source/export, rhythm events, category, frame range, and measured values. |
| `docs/animation_work_status/tap_dance_evidence/` | Raw generation, validation, surface, rendered-review and fast-test evidence; saved-review JSON; inventory; experimental runtime-registration patch. |
| `.gitattributes` | Main's generated 100 MiB size policy retained during rebase; task assets use ordinary Git under that policy. Initial task-specific exceptions became redundant and were removed. |

Reported clips comprise 48 fundamentals, 45 combination variants, and one wing study. Recorded frame ranges start at **0**, with ends **64, 80, 96, 112, or 144**, at **24 fps**. The final frame is intended as a repeat endpoint. The inventory and per-clip JSON give the exact range and actor for each file. Both actors use separate single-participant action families, rather than a paired dance action.

`animations/man_and_woman/tap_man_paddle_and_roll_right.blend` is the **95th source**, saved before its export/report completed. Its intended role is `PLAYER`, intended frames are **0–112**, and its source/baked family was written before export began. It has **zero matching GLB/report** in this checkpoint; reload validation is pending.

Shared geometry, shared scene data, existing animation sources, and the combined `man_and_woman3.blend` remain unchanged. Only the first experimental toe-tap had been added to `animation_updates.tres`. That task-owned registration was removed for delivery so the failed checkpoint stays outside the active runtime update library. Its exact prior diff is preserved in `experimental_runtime_registration.patch`. The remaining partial exports were already outside that registry. Blender's source-directory discovery can still expose these partial authoring files; review this status before selecting them as finished animation assets.

## Validation and known failures

- `python tests/run_tests.py --suite fast`: **9/9 pass**, 3.00 seconds in the post-stop run (`stop_fast.log`). The initial run passed 8/9 because hair `.res` assets were LFS pointers. Fetching the three hair mesh resources resolved that prerequisite; their tracked content stayed unchanged.
- `python tests/run_tests.py --changed scripts/create_tap_dance.py --changed scripts/review_tap_dance.py --changed scripts/tap_dance_repertoire.py`: **9/9 pass**, 2.87 seconds (`stop_scoped_tests.log`). This scope selects the fast set and zero slow checks.
- A broader source/GLB selection was inspected using `--list`: **9 fast and 186 slow** checks (`selected.log`). That broad suite was **not run**. It includes unrelated gameplay and existing animation tests, and Game Rig Tools-dependent checks. Game Rig Tools is absent from this environment.
- `python -m py_compile scripts/create_tap_dance.py scripts/tap_dance_repertoire.py scripts/review_tap_dance.py`: pass after stopping.
- Static GLB verification after stopping: all 94 files have valid GLB v2 header lengths and readable JSON. The wing export's additional authoring animation is recorded as a structural failure. This check establishes container structure, rather than runtime playback fidelity.
- Author-process checks sampled each completed reported clip at half frames. All 94 saved report objects have `passed: true`; their checks cover declared ankle plants, ankle separation, IK reach, a hand/torso clearance proxy, and positional loop endpoints/velocity. They **do not establish complete mesh clearance, correct tap technique, or faithful saved bake playback**.
- Saved-file check command: `blender -t 1 -b animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 --python scripts/review_tap_dance.py -- --match tap_man_ball_change_left`. Latest result: **FAIL**. Maximum editable/baked position difference **0.103241681 m**, angle difference **0.360642076 rad**, including integer samples. See `bake_review5.log` and `saved_review.json`.
- Earlier saved-file probes failed with approximately **0.011347 m** position and **0.032455 rad** angle differences. Dense native baking and later native rest-length matrix conversion were investigated. The last attempt changed action switching to preserve Rigify drivers. The discrepancy grew, and its cause remains unresolved. Inspect driver evaluation, NLA bindings/time mapping, target rest lengths, and connected bones before adopting either bake approach.
- Evaluated skin-surface probes found the man's soles approximately **18–19 mm below nominal z=0** in earlier clips; the woman's tapping sole reached approximately **2.55 mm below z=0**. The latest generator adds constant root offsets of 20 mm and 4 mm respectively. Only the latest `tap_man_ball_change_left` was regenerated after that change; the wider set retains earlier floor placement. Full revalidation remains pending.
- An existing Blender Workbench render of the man's toe-tap at frame 20 is preserved as `man_toe_tap_review.png`. It documents an intermediate arm refinement, rather than final visual acceptance. The render logged EGL context warnings and produced the image. Additional planned renders were stopped.
- Baked GLBs use the existing deform-rig naming and compact scene helper. Runtime Godot import/playback and complete skeleton/track compatibility remain unverified.

## Processes and storage

At the stop inspection, **zero owned Blender authoring, generation, rendering, or review processes remained active**. Three generation shards had already been terminated during refinement; their partial logs and outputs are preserved. The last saved review had exited with a failing assertion. No additional Blender operation was started after the stop instruction.

The asset inventory totals **57,793,519 bytes**, excluding documentation/evidence. The largest inventoried file is **1,718,224 bytes**. All task binaries, including the saved render, are under 104,857,600 bytes and use direct Git storage. Initial staging used exact-path exceptions; rebase retained main's newer generated size policy, which already keeps these paths in ordinary Git. Existing LFS source files were downloaded for work and keep their existing attributes. This task creates zero new LFS objects; ordinary Git push transfers its asset bytes.

Temporary `/tmp/tap-dance` inspection scripts and logs may remain in this environment. Durable evidence is copied into this checkpoint directory. The temporary credential helper reads the configured `SANJO_GITHUB_LFS_TOKEN`; it contains no credential value and is intentionally outside Git.

## Integration verification

- Rebased checkpoint commit: `341d55d40`.
- `python apps/a-game/tests/run_tests.py --suite fast` after rebase: **10/10 pass**, 5.96 seconds (`after_rebase_fast.log`).
- All **377** inventoried source/export/import/report files retain their recorded byte sizes and SHA-256 after rebase.
- `python scripts/lfs_policy.py check`: pass for **23,758** staged repository files at checkpoint integration. Task assets remain ordinary Git blobs.
- The Animation section of `AGENTS.md` adds guidance on retaining Rigify drivers, limiting temporary-scene GLB export to the active scene, and distinguishing in-process contact reports from saved-bake acceptance.

## Concurrent-main integration context

The checkpoint was rebased onto `18e528c73` after stopping. Concurrent main already provides `scripts/lfs_policy.py` and the bundled Game Rig Tools setup in `scripts/blender/README.md`. Its generated `.gitattributes` superseded the task's initial path exceptions. Game Rig Tools was absent during the recorded experiments; the newly fetched setup is available for a future authorized resume and was not installed or exercised after the stop. Other tasks' shared assets and instructions were preserved.

## Remaining work and explicit blockers

1. Diagnose and correct the saved editable/baked mismatch before generating additional clips or publishing the current ones.
2. Validate retained Rigify drivers, per-action slot/NLA activation, native deformation conversion, and actual exported playback.
3. Calibrate sole and ball/heel pivot contacts against each character's actual surface. Regenerate prior assets only after renewed authorization.
4. Refine preliminary rhythm definitions, weight transfers, jumps, wings, heel/ball pivots, and combinations against recognizable tap technique; finish positions, missing combinations, and smooth composable transitions.
5. Complete the 210-clip plan if the resumed scope still requests it. The checkpoint includes 94 reported exports and one source-only partial file.
6. Sample saved and exported motion at interpolation subframes; complete surface/body-clearance, hand/finger/wrist comfort, planted-contact, loop position/rotation/velocity, and visual playback review.
7. Replace the failed early wing GLB, complete the paddle-and-roll source export, run focused Blender/Godot checks, and register accepted clips through the existing update workflow.

## Resume commands after renewed authorization

Run from `apps/a-game`. These commands are instructions for a future authorized resume; they were not executed after stopping.

```bash
# Inspect current evidence and the failing saved clip before further generation.
cat docs/animation_work_status/tap_dance_evidence/saved_review.json
blender --version
# Newly available from concurrent main; use an isolated task profile per its README.
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
blender -t 1 -b animations/man_and_woman/solo_disco_dance.blend \
  --python-exit-code 1 --python scripts/review_tap_dance.py \
  -- --match tap_man_ball_change_left

# After repairing and reviewing the generator, rebuild this isolated diagnostic.
blender -t 1 -b animations/man_and_woman/solo_disco_dance.blend \
  --python-exit-code 1 --python scripts/create_tap_dance.py \
  -- --match tap_man_ball_change_left

# After the diagnostic passes, review all saved reported clips.
blender -t 2 -b animations/man_and_woman/solo_disco_dance.blend \
  --python-exit-code 1 --python scripts/review_tap_dance.py

# A complete rebuild overwrites this task's sources/exports, after fixes and approval.
blender -t 2 -b animations/man_and_woman/solo_disco_dance.blend \
  --python-exit-code 1 --python scripts/create_tap_dance.py
python tests/run_tests.py --suite fast
```

`--resume` skips existing JSON reports, including reports from the earlier flawed bake iterations. A repaired full regeneration should therefore use the complete rebuild command rather than trusting that flag. The generator writes individual GLBs but currently leaves accepted-library registration to the publication stage.

GitHub commit and push operations for this checkpoint are authored by **Codex**, with exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer on each new commit. The final chat delivery records the actual task/documentation/integration commit hashes and remote-main verification, which become known after this status document is committed.
