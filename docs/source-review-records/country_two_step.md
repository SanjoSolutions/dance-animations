# Country two-step animation work status

Recorded 2026-10-02, stopping-point inspection at 15:00 UTC (17:00 Europe/Berlin).
Task/chat title: Country two-step animations for man_and_woman3.blend.
Workspace: `/workspace/sanjo-solutions/apps/a-game` in the sanjo-solutions cloud environment.
Task branch at stop: `codex/country-two-step`.
Current commit at stop: `3c52737c74b488501e9cfe47e7029547c6f5fe88`.
Author of this status and task GitHub commit communications: Codex.

## Stop instruction and delivery state

The user instructed all animation chats to stop authoring, refinement, generation,
and rendering, preserve the present state, document it, commit, integrate current
main, and push. All owned Blender and test processes had completed at the stop.
Process inspection found zero remaining owned animation/test processes. Subsequent
work is preservation, verification of existing bytes, documentation, and Git delivery.

There are **60 authored paired procedural IK sources, 0 baked clips, and 0 runtime
exports**. Treat these as procedural blocking studies with numerical validation,
awaiting complete dance-quality acceptance and runtime delivery. This task remains
partial relative to the original request for natural motion across all Country
two-step moves and positions. It provides a broad curated repertoire; regional
variants and arbitrary combinations extend beyond the delivered catalog.

## Original scope and completed work

Create coordinated Country two-step animation for both characters in
`man_and_woman3.blend`, use Blender 5.2 throughout, follow per-animation source
workflow, reuse suitable existing motion/tooling, validate interpolation, support,
clearance, transitions, and loops. Preserve concurrent work, commit sources, rebase
onto origin/main, document useful findings in AGENTS.md, merge and push main.

Completed work uses Blender **5.2.2 LTS**, build `d13f752e3b9c`, executable
`/workspace/tools/blender-5.2.2-linux-x64/blender`. System Blender 4.3 was excluded
from this task's Blender work. Git LFS scene dependencies were hydrated before use.

* Authored 11 positions, 13 basics/travel phrases, 2 couple turns, 6 underarm turns,
  20 directed position transitions, 6 wrap/release studies, and 2 passing figures.
* Both roles share action timing: `Man.rigify` = player/leader;
  `Woman.rigify` = partner/follower. Every clip has both action slots, matched NLA
  bindings, participant BOTH metadata, explicit ranges, and rhythm markers.
* Used sparse IK keys for support, toe-off, swing apex, landing, and hand contact;
  stationary controls retain one initial key. Native wrist constraints stay active.
* Reused `PairedAnimationAuthoring`, calibrated palm solving, `RigYogaPoser`,
  `ActivityMotionAuthor`, and `AnimationFileWriter`. Existing solo disco motion was
  inspected; its choreography was unsuitable for QQSS, so its motion was not copied.
* Composed an individual source successfully and discovered all 60 sources through
  the existing animation chooser, with paired slot bindings verified.
* Shared scenes, the combined library, original character geometry, and runtime
  libraries retain their existing contents. Test/import edits to existing resources
  were restored before preservation.

## Files and asset state

Paths below are relative to `apps/a-game`.

| File | State and purpose |
| --- | --- |
| `scripts/create_country_two_step.py` | Saved reproducible source authoring script; generation stopped |
| `scripts/validate_country_two_step.py` | Saved fractional-frame source validator and optional review renderer |
| `scripts/country_two_step.md` | Timing, coverage, roles, storage, playback, authoring and verification guide |
| `animations/man_and_woman/country_two_step_catalog.json` | Exact 60-source catalog, ranges, key frames, travel vectors and playback ends |
| `animations/man_and_woman/country_two_step_validation.json` | Aggregated four completed passing runs; asset hashes and sizes rechecked during preservation |
| `animations/man_and_woman/.gitattributes` | 60 exact-name ordinary-Git exceptions for these sources |
| `docs/animation_work_status/country_two_step.md` | This stopping-point record |
| `docs/animation_work_status/country_two_step/` | Preserved validation reports, test logs, diagnostic scripts and already-rendered review images; inventory below |

All following `.blend` files reside in `animations/man_and_woman/`. Each is authored
and editable; each has **baked = 0, exported = 0**, with both leader/follower roles.

| Source filename | Family | Stored frames | Playback end | Repetition |
| --- | --- | --- | ---: | --- |
| `country_two_step_position_closed.blend` | Position | 0–72 | 71 | Stationary loop |
| `country_two_step_position_open_single.blend` | Position | 0–72 | 71 | Stationary loop |
| `country_two_step_position_open_double.blend` | Position | 0–72 | 71 | Stationary loop |
| `country_two_step_position_promenade.blend` | Position | 0–72 | 71 | Stationary loop |
| `country_two_step_position_counter_promenade.blend` | Position | 0–72 | 71 | Stationary loop |
| `country_two_step_position_side_by_side.blend` | Position | 0–72 | 71 | Stationary loop |
| `country_two_step_position_sweetheart.blend` | Position | 0–72 | 71 | Stationary loop |
| `country_two_step_position_shadow.blend` | Position | 0–72 | 71 | Stationary loop |
| `country_two_step_position_cuddle.blend` | Position | 0–72 | 71 | Stationary loop |
| `country_two_step_position_skaters.blend` | Position | 0–72 | 71 | Stationary loop |
| `country_two_step_position_right_hand_to_right_hand.blend` | Position | 0–72 | 71 | Stationary loop |
| `country_two_step_basic_forward.blend` | Basic and travel | 0–72 | 71 | Accumulated pair travel |
| `country_two_step_basic_backward.blend` | Basic and travel | 0–72 | 71 | Accumulated pair travel |
| `country_two_step_basic_in_place.blend` | Basic and travel | 0–72 | 71 | Stationary loop |
| `country_two_step_progressive_open.blend` | Basic and travel | 0–72 | 71 | Accumulated pair travel |
| `country_two_step_promenade_walk.blend` | Basic and travel | 0–72 | 71 | Accumulated pair travel |
| `country_two_step_counter_promenade_walk.blend` | Basic and travel | 0–72 | 71 | Accumulated pair travel |
| `country_two_step_sweetheart_walk.blend` | Basic and travel | 0–72 | 71 | Accumulated pair travel |
| `country_two_step_shadow_walk.blend` | Basic and travel | 0–72 | 71 | Accumulated pair travel |
| `country_two_step_side_by_side_walk.blend` | Basic and travel | 0–72 | 71 | Accumulated pair travel |
| `country_two_step_skaters_walk.blend` | Basic and travel | 0–72 | 71 | Accumulated pair travel |
| `country_two_step_cuddle_walk.blend` | Basic and travel | 0–72 | 71 | Accumulated pair travel |
| `country_two_step_diagonal_progression_left.blend` | Basic and travel | 0–72 | 71 | Accumulated pair travel |
| `country_two_step_diagonal_progression_right.blend` | Basic and travel | 0–72 | 71 | Accumulated pair travel |
| `country_two_step_couple_turn_left.blend` | Couple turn | 0–288 | 287 | Stationary loop |
| `country_two_step_couple_turn_right.blend` | Couple turn | 0–288 | 287 | Stationary loop |
| `country_two_step_follower_underarm_left.blend` | Underarm turn | 0–144 | 144 | One shot |
| `country_two_step_follower_underarm_right.blend` | Underarm turn | 0–144 | 144 | One shot |
| `country_two_step_leader_underarm_left.blend` | Underarm turn | 0–144 | 144 | One shot |
| `country_two_step_leader_underarm_right.blend` | Underarm turn | 0–144 | 144 | One shot |
| `country_two_step_follower_double_turn_left.blend` | Underarm turn | 0–288 | 288 | One shot |
| `country_two_step_follower_double_turn_right.blend` | Underarm turn | 0–288 | 288 | One shot |
| `country_two_step_closed_to_open_single.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_open_single_to_closed.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_closed_to_open_double.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_open_double_to_closed.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_closed_to_promenade.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_promenade_to_closed.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_closed_to_counter_promenade.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_counter_promenade_to_closed.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_closed_to_side_by_side.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_side_by_side_to_closed.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_closed_to_sweetheart.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_sweetheart_to_closed.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_closed_to_shadow.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_shadow_to_closed.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_closed_to_cuddle.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_cuddle_to_closed.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_closed_to_skaters.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_skaters_to_closed.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_closed_to_right_hand_to_right_hand.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_right_hand_to_right_hand_to_closed.blend` | Position transition | 0–144 | 144 | One shot |
| `country_two_step_wrap_to_cuddle.blend` | Wrap and release | 0–144 | 144 | One shot |
| `country_two_step_unwrap_from_cuddle.blend` | Wrap and release | 0–144 | 144 | One shot |
| `country_two_step_wrap_to_sweetheart.blend` | Wrap and release | 0–144 | 144 | One shot |
| `country_two_step_unwrap_from_sweetheart.blend` | Wrap and release | 0–144 | 144 | One shot |
| `country_two_step_tuck_to_open.blend` | Wrap and release | 0–144 | 144 | One shot |
| `country_two_step_open_to_tuck.blend` | Wrap and release | 0–144 | 144 | One shot |
| `country_two_step_open_circling_basic.blend` | Passing figure | 0–288 | 288 | One shot |
| `country_two_step_change_places.blend` | Passing figure | 0–144 | 144 | One shot |

## Timing, partial technique, and limitations

24 fps, 120 BPM, quick–quick–slow–slow: steps at frames 0, 12, 24, 48; next phrase
at 72. Position/basic clips store 0–72, singles/transitions/wraps/change places
0–144, and full couple/double turns/open circling 0–288.

14 stationary loops use duplicate closing poses; playback omits the closing frame.
12 traveling cycles require accumulating the catalog travel vector for the entire
pair at each repetition. Their native action cyclic flag stays off to prevent a
world-space return to the start. 34 figures play once. Loop validation removes the
known translation for traveling phrases and checks endpoint position and velocity.

Wraps and facing transitions currently release hands and regrip. They are
**procedural released-wrap blocking studies**, rather than continuously held advanced
wrap technique. Directed position transitions match the corresponding hold clips
at their endpoints. Joining arbitrary figures still needs sequence-specific alignment.

The numeric clearance checks measure torso separation and floor samples. They do
not certify all limb/mesh collisions or physical balance. Visual review covered
base positions and representative turn/transition phases, rather than continuous
playback of all 60 clips. Natural dance quality, all-body clearance, and technique
acceptance remain open. Source preservation takes priority over further refinement.

## Verification completed before stopping

* Saved-source validation: **60/60 passed**, 16,084 samples, using Blender 5.2.2.
  All four processes exited 0. Sample spacing was half a frame plus authored phase
  boundaries; evaluated mesh floor checks used five times per clip. Checks include
  slots/NLA/metadata, finite keys, movement, IK reach, feet, palms, floor, torso,
  wrist angle, loop position/velocity, and directed position endpoints.
* Maximum measured IK reach and planted-foot error: 0.0002322 m. Maximum palm gap:
  0.0182984 m. Minimum sampled floor height: -0.001095 m. Minimum torso separation:
  0.3941474 m. Maximum loop position residual: 0.0000012 m; velocity residual:
  0.0026566 m/frame. Maximum directed join error: 0.000001 m. Exact tolerances and
  per-source results are preserved in the aggregate JSON.
* Final authoring-time fast suite: **10/10 passed**, 6.14 seconds, exit 0.
* Preservation-time fast suite rerun: **10/10 passed**, 6.33 seconds, exit 0.
* Post-rebase fast suite: **10/10 passed**, 6.42 seconds, exit 0.
* Final integrated fast suite: **10/10 passed**, 6.21 seconds, exit 0.
* Concurrent-main retry fast suite: **10/10 passed**, 5.98 seconds, exit 0.
* Selected broader suite: **34/67 passed**, 1592.71 seconds, exit 1. The retained
  `suite_scoped.txt` contains every failure. Observed blockers include the missing
  Game Rig Tools add-on (`StopIteration` in bake/export tests), headless GPU-fluid
  rendering errors, runtime resource errors/leaks, and multiple 90-second timeouts
  in Godot and combined-library Blender checks. Process-cleanup assertions also
  failed during the loaded run; the later standalone fast suite passed. These
  observations do not establish that every broader failure is environmental.
* Individual composition: `TWO_STEP_SOURCE_COMPOSITION_PASS 430 country_two_step_basic_forward`.
* Chooser discovery and both rig slots: `TWO_STEP_DISCOVERY_PASS 60`.
* `python -m py_compile scripts/create_country_two_step.py scripts/validate_country_two_step.py`
  passed; both scripts were Black formatted.
* Preservation independently verified the SHA-256 and byte count of every current
  source against the completed validation reports. 60 sources total 8,915,809 bytes;
  smallest 122,666, largest 209,155. Each is below 104,857,600 bytes.

Commands used (from the app directory):

```sh
python .cache/country_two_step/validate_groups.py foundations
python .cache/country_two_step/validate_groups.py transitions
python tests/run_tests.py --suite fast
PATH=/workspace/tools/blender-5.2.2-linux-x64:$PATH \
  BLENDER=/workspace/tools/blender-5.2.2-linux-x64/blender \
  python tests/run_tests.py --suite changed \
  --changed animations/man_and_woman/country_two_step_basic_forward.blend --slow-timeout 90
```

`validate_groups.py` is preserved in the evidence directory. It launches two
Blender 5.2.2 processes per group with `--disable-autoexec --python-exit-code 1`,
separate report paths, and explicit `--only` selections. The four source reports
record the exact selections. A full sequential validation command appears below.

## Saved outputs and processes

48 already-rendered PNG outputs are preserved: 11 base-position images, five
follower-underarm phases, 30 motion/transition images, and two contact sheets.
Rendering used Blender 5.2.2 Workbench at 360 × 440 with one subdivision level;
contact-sheet composition also used Blender 5.2.2. The two sheets are 1080 × 2200.
These images are review evidence, not baked or runtime exports.

Contact sheet `review_0.png` rows: basic forward, couple turn left, leader underarm
left, leader underarm right, closed to promenade. `review_1.png` rows: side by side
to closed, closed to shadow, sweetheart to closed, closed to skaters, cuddle to
closed. Columns are 25%, 50%, and 75% of each clip. The evidence `review/` keeps
final base positions and follower-turn phases; stale earlier pose variants remain
only in ignored cache and are excluded from this delivery.

All durable sources and final review outputs are saved. There are zero active owned
Blender, authoring, rendering, or suite processes. Ignored `.cache/country_two_step/`
retains temporary probes, superseded renders, and build/import logs in this
workspace; retained final evidence below supplies the portable stopping-point record.

Evidence inventory (relative to `docs/animation_work_status/country_two_step/`):

* `.gitattributes` (3,897 bytes)
* `composition.txt` (363 bytes)
* `discovery.py` (834 bytes)
* `discovery.txt` (5,467 bytes)
* `fast_concurrent.txt` (775 bytes)
* `fast_integrated.txt` (775 bytes)
* `fast_rebased.txt` (775 bytes)
* `fast_preservation.txt` (775 bytes)
* `fast_final.txt` (775 bytes)
* `motion_review/country_two_step_basic_forward_0.png` (135,005 bytes)
* `motion_review/country_two_step_basic_forward_1.png` (132,885 bytes)
* `motion_review/country_two_step_basic_forward_2.png` (129,767 bytes)
* `motion_review/country_two_step_closed_to_promenade_0.png` (134,448 bytes)
* `motion_review/country_two_step_closed_to_promenade_1.png` (152,256 bytes)
* `motion_review/country_two_step_closed_to_promenade_2.png` (149,481 bytes)
* `motion_review/country_two_step_closed_to_shadow_0.png` (133,870 bytes)
* `motion_review/country_two_step_closed_to_shadow_1.png` (141,582 bytes)
* `motion_review/country_two_step_closed_to_shadow_2.png` (134,879 bytes)
* `motion_review/country_two_step_closed_to_skaters_0.png` (134,587 bytes)
* `motion_review/country_two_step_closed_to_skaters_1.png` (150,985 bytes)
* `motion_review/country_two_step_closed_to_skaters_2.png` (145,234 bytes)
* `motion_review/country_two_step_couple_turn_left_0.png` (142,531 bytes)
* `motion_review/country_two_step_couple_turn_left_1.png` (131,833 bytes)
* `motion_review/country_two_step_couple_turn_left_2.png` (141,640 bytes)
* `motion_review/country_two_step_cuddle_to_closed_0.png` (130,671 bytes)
* `motion_review/country_two_step_cuddle_to_closed_1.png` (140,423 bytes)
* `motion_review/country_two_step_cuddle_to_closed_2.png` (133,119 bytes)
* `motion_review/country_two_step_leader_underarm_left_0.png` (139,344 bytes)
* `motion_review/country_two_step_leader_underarm_left_1.png` (139,167 bytes)
* `motion_review/country_two_step_leader_underarm_left_2.png` (136,299 bytes)
* `motion_review/country_two_step_leader_underarm_right_0.png` (132,041 bytes)
* `motion_review/country_two_step_leader_underarm_right_1.png` (139,312 bytes)
* `motion_review/country_two_step_leader_underarm_right_2.png` (139,923 bytes)
* `motion_review/country_two_step_side_by_side_to_closed_0.png` (149,706 bytes)
* `motion_review/country_two_step_side_by_side_to_closed_1.png` (148,035 bytes)
* `motion_review/country_two_step_side_by_side_to_closed_2.png` (133,181 bytes)
* `motion_review/country_two_step_sweetheart_to_closed_0.png` (143,607 bytes)
* `motion_review/country_two_step_sweetheart_to_closed_1.png` (146,294 bytes)
* `motion_review/country_two_step_sweetheart_to_closed_2.png` (133,189 bytes)
* `preservation_summary.json` (1,099 bytes)
* `review/country_two_step_follower_underarm_left_0.png` (141,623 bytes)
* `review/country_two_step_follower_underarm_left_1.png` (139,008 bytes)
* `review/country_two_step_follower_underarm_left_2.png` (139,204 bytes)
* `review/country_two_step_follower_underarm_left_3.png` (137,581 bytes)
* `review/country_two_step_follower_underarm_left_4.png` (141,797 bytes)
* `review/country_two_step_position_closed_0.png` (134,536 bytes)
* `review/country_two_step_position_counter_promenade_0.png` (150,757 bytes)
* `review/country_two_step_position_cuddle_0.png` (136,910 bytes)
* `review/country_two_step_position_open_double_0.png` (142,021 bytes)
* `review/country_two_step_position_open_single_0.png` (141,796 bytes)
* `review/country_two_step_position_promenade_0.png` (149,898 bytes)
* `review/country_two_step_position_right_hand_to_right_hand_0.png` (145,857 bytes)
* `review/country_two_step_position_shadow_0.png` (137,767 bytes)
* `review/country_two_step_position_side_by_side_0.png` (152,029 bytes)
* `review/country_two_step_position_skaters_0.png` (145,945 bytes)
* `review/country_two_step_position_sweetheart_0.png` (143,501 bytes)
* `review_0.png` (1,724,864 bytes)
* `review_1.png` (1,756,692 bytes)
* `suite_scoped.txt` (2,852,917 bytes; trailing whitespace normalized)
* `validate_groups.py` (1,391 bytes)
* `validation_foundations_0.json` (9,204 bytes)
* `validation_foundations_1.json` (9,184 bytes)
* `validation_transitions_0.json` (9,164 bytes)
* `validation_transitions_1.json` (9,160 bytes)

## Storage and delivery

Exact filename attributes keep all 60 new Blender sources and 48 review images in
ordinary Git. Existing shared scenes and character assets keep their LFS settings.
The source sizes above and actual image sizes were inspected before staging.
No new LFS objects are introduced; ordinary Git push transfers the new asset bytes.
The delivery commits must preserve concurrent main changes and contain exactly one
`Co-authored-by: Codex <noreply@openai.com>` trailer each. Task and integration hashes
are reported in the final chat response; this record identifies the original stop
commit above, independently of later rebase/merge hashes.

## Integration checkpoint

The preservation commit was rebased onto `origin/main` at
`e12670ea9` and became `97b00b4ac635fc1b7bc1910c6efbdb3d9339ad15`.
The only conflict was the per-animation `.gitattributes`; every upstream entry
and every Country two-step entry was retained. The new repository storage check,
`python scripts/lfs_policy.py check` from the repository root, passed for 24,057
tracked/index files. Indexed binary hashes matched the preserved sources and images.
The post-rebase fast suite passed 10/10. The documentation commit adds QQSS timing,
travel accumulation, directed joins, and fractional-boundary validation guidance
to the app's `# Animation` section. Final integration performs another fetch and an
ordinary history-preserving push; the final chat response records its exact hashes.

Fetched main also supplies bundled animation-tool setup in
`scripts/blender/install_animation_tools.py` and `scripts/blender/README.md`.
The missing Game Rig Tools failures above describe the earlier suite environment;
the bundled installer now provides a concrete future setup path. It has not been
run as part of this stopped task, and the failed broader suite remains unresolved.

The documentation commit is `cc49f11de19fc9fd54cc57a8fd2c6f42fcd09bb9`.
The immediate pre-integration fetch advanced main to `5e5236e7c`. Integration
retained both sides of the AGENTS.md and animation-attributes additions, including
concurrent K-pop work. The integrated fast suite passed 10/10, and the repository
storage-policy check passed. All 108 indexed task binaries matched their saved
bytes after conflict resolution.

The first merge commit is `7bc019894920bebb7654e84c0cc73985a066e220`.
Its ordinary push was rejected because another chat advanced remote main. A fresh
fetch retrieved `b2cf8b15f`; the retry merge preserved both the Bollywood and
Country two-step storage entries. Fast checks passed 10/10 in 5.98 seconds and
the storage-policy check passed for 25,648 files before retry delivery.

## Remaining work and exact resume commands

Further authoring/rendering requires a subsequent user instruction to resume.
Remaining animation work: continuous visual acceptance across all 60 sources;
technique review of released wraps and footwork; full-body collision and balance
review; any additional regional figures; sequence-specific joins; bake and runtime
export followed by Godot acceptance. Baking needs the bundled Game Rig Tools installed
and enabled in the Blender 5.2 profile (see the integration checkpoint). The broader suite needs investigation of the preserved
failures, suitable headless/runtime capabilities, and appropriate timeout budgets.
Do not treat current numerical passes as completed runtime delivery.

To verify preserved sources later, from this workspace:

```sh
cd /workspace/sanjo-solutions/apps/a-game
mkdir -p .cache/country_two_step
/workspace/tools/blender-5.2.2-linux-x64/blender -t 2 --background \
  animations/man_and_woman/shared_scene_data.blend --disable-autoexec \
  --python-exit-code 1 --python scripts/validate_country_two_step.py -- \
  --report .cache/country_two_step/resume_validation.json
/workspace/tools/blender-5.2.2-linux-x64/blender -t 2 --background \
  animations/man_and_woman/shared_scene_data.blend --disable-autoexec \
  --python-exit-code 1 --python docs/animation_work_status/country_two_step/discovery.py
python tests/run_tests.py --suite fast
```

To resume a selected source only after authoring is authorized:

```sh
cd /workspace/sanjo-solutions/apps/a-game
/workspace/tools/blender-5.2.2-linux-x64/blender -t 2 --background \
  animations/man_and_woman/shared_scene_data.blend --disable-autoexec \
  --python-exit-code 1 --python scripts/create_country_two_step.py -- --only basic_forward
/workspace/tools/blender-5.2.2-linux-x64/blender -t 2 --background \
  animations/man_and_woman/shared_scene_data.blend --disable-autoexec \
  --python-exit-code 1 --python scripts/validate_country_two_step.py -- \
  --only basic_forward --report .cache/country_two_step/basic_forward_validation.json
```

For interactive editing, open the selected source with Player Asset Export enabled
or use **Helpers > Animation > Select animation**, then **Edit animation file** in
`man_and_woman3.blend`. For baking/export after the add-on prerequisite is resolved,
use **Bake & Export Active Animation** and save the individual source to preserve
its baked action. Follow `docs/player-animation-workflow.md` and record new authored,
baked, and exported states separately. The current stop order leaves these steps pending.
