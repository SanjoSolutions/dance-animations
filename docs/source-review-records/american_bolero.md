# American bolero preservation status

Recorded by Codex on **2026-10-02**. Authoring stopped at **15:00:36 UTC**
(17:00:36 Europe/Berlin) following the user's stop-and-preserve instruction.

- Chat title: **Create American bolero animations**.
- Chat ID: `01a0fce9-71b8-760a-8e37-5962d3c0a06f`.
- Project: A-Game; cloud environment: sanjo-solutions.
- Checkout: `/workspace/sanjo-solutions/apps/a-game`.
- Task branch: `codex/american-bolero`.
- Current commit at stop: `3c52737c74b488501e9cfe47e7029547c6f5fe88`.
  All task additions were working-tree files at that point.
- Original scope: a broad, organized American bolero repertoire with coordinated
  partner motion for `man_and_woman3.blend`, all dance moves/positions requested,
  reuse where appropriate, planted contacts, clearance, smooth transitions,
  interpolation/loop checks, Blender 5.2 throughout, per-animation sources,
  documentation, commits, rebase, merge and push.
- Current authority: preserve the present state and deliver it. Further authoring,
  refinement, generation, rendering, baking and export are paused pending an
  explicit request to resume. A completed exhaustive repertoire is **not** claimed.

## Completed work and production state

**49 editable paired procedural blocking/choreography studies** are saved: 24
figure interpretations, nine position loops and 16 directed formation transitions.
These are partial assets that need further artistic review. **49 authored sources,
0 baked actions, 0 new GLB/runtime exports.** Both roles share each action:
`Man.rigify` is leader/player; `Woman.rigify` is follower/partner. Reverse-role
variants remain outside the saved set. Each file has a two-slot action, participant
metadata, NLA binding metadata, a shared-scene descriptor and phase markers.

All Blender authoring, saved-file checks and rendering used **Blender 5.2.2 LTS**:
`/workspace/.cloud-onboarding/3d-tools/blender-5.2.2/blender`.
The environment's `/usr/bin/blender` is 4.3.2 and is unsuitable for this task.
Animation timing is 24 fps, 96 BPM, 15 frames/beat. Position loops store 0–120
and play 0–119. Figures and transitions store 0–150; loops play 0–149,
while directed clips play 0–150 once. Fractional keys represent syncopation;
pose-marker frame numbers are rounded to integers.

The author composes the existing Yoga neutral poser, paired IK API, calibrated
palms, DiscoWristPoser, sparse motion writer and AnimationFileWriter. Existing disco
choreography was inspected but its rhythm/style did not fit bolero. Saved work
includes pelvis reach caps, grounded replacement feet, calibrated hand positions,
native wrist constraints and loop closure. The final released-arm styling pass
saved **44/49** sources; its remaining five files retain earlier arm styling:
`spot_turns`, `sweetheart_wrap`, `swivels`, `syncopated_breaks`,
`underarm_turn_right`. All five still have earlier complete source saves.

`man_and_woman3.blend`, `shared_scene_data.blend`, anatomical sources and existing
animations retain their tracked contents. Actual linked source LFS objects were
hydrated locally, together with existing runtime/hair assets needed for tests.

## Files and assets

Paths below are relative to `apps/a-game`.

- `scripts/create_american_bolero.py`: preserved procedural author and refinement
  code, including targeted selections/resume; execution is paused.
- `scripts/validate_american_bolero.py`: saved-file metadata, interpolation,
  contact, reach, floor and loop checks; optional preview rendering.
- `scripts/american_bolero.md`: repertoire/timing/limitations and future commands,
  with an explicit partial-work notice.
- `animations/man_and_woman/american_bolero_catalog.json`: all 49 recipes' names,
  categories, descriptions, ranges, markers, authored times, plants and contacts.
- `animations/man_and_woman/american_bolero_validation.json`: latest preservation
  validation report; see the verification section for its actual outcome.
- `animations/man_and_woman/.gitattributes`: exact-filename ordinary-Git exceptions
  for these 49 source files; existing storage rules remain intact.
- `docs/animation_work_status/american_bolero.md`: this status record.
- `docs/animation_work_status/american_bolero/assets.json`: exact source paths,
  byte sizes, SHA-256 hashes, ranges, roles, refinement and production state.
- `docs/animation_work_status/american_bolero/saved_review_outputs.tar.gz`:
  preserved pre-stop playback frames, still reviews, contact sheets, debug probe
  source/render and inspection scripts. These show mixed intermediate revisions;
  the archive is historical evidence, not final-quality approval.
- `docs/animation_work_status/american_bolero/saved_review_outputs.json`: archive
  checksum and every archived file's path, byte size and checksum.
- `docs/animation_work_status/american_bolero/logs/`: preserved command outputs,
  including historical failures, the interrupted styling run and final checks.

Every row below is a **partial authored study; baked=false; exported=false**.
The full filename is `animations/man_and_woman/american_bolero_<stem>.blend`.
"Saved" in the last column means the final styling pass reported a completed save;
it does not mean artistic completion.

| Stem | Category | Stored range | Playback end | Loop | Final arm pass |
| --- | --- | --- | --- | --- | --- |
| basic | Foundation | 0–150 | 149 | yes | saved |
| checked_lunge | Lines | 0–150 | 149 | yes | saved |
| closed_to_counter_promenade | Transitions | 0–150 | 150 | once | saved |
| closed_to_double_hand | Transitions | 0–150 | 150 | once | saved |
| closed_to_fan | Transitions | 0–150 | 150 | once | saved |
| closed_to_open_facing | Transitions | 0–150 | 150 | once | saved |
| closed_to_promenade | Transitions | 0–150 | 150 | once | saved |
| closed_to_right_angle | Transitions | 0–150 | 150 | once | saved |
| closed_to_shadow | Transitions | 0–150 | 150 | once | saved |
| closed_to_side_by_side | Transitions | 0–150 | 150 | once | saved |
| counter_promenade_to_closed | Transitions | 0–150 | 150 | once | saved |
| cross_body_lead | Passing figures | 0–150 | 150 | once | saved |
| crossover_breaks | Breaks | 0–150 | 149 | yes | saved |
| double_hand_to_closed | Transitions | 0–150 | 150 | once | saved |
| fan_to_closed | Transitions | 0–150 | 150 | once | saved |
| fifth_position_breaks | Breaks | 0–150 | 149 | yes | saved |
| forward_back_basic | Foundation | 0–150 | 149 | yes | saved |
| hand_to_hand | Breaks | 0–150 | 149 | yes | saved |
| horseshoe | Open figures | 0–150 | 150 | once | saved |
| left_rock_turn | Turns | 0–150 | 150 | once | saved |
| left_side_pass | Passing figures | 0–150 | 150 | once | saved |
| open_break | Breaks | 0–150 | 149 | yes | saved |
| open_facing_to_closed | Transitions | 0–150 | 150 | once | saved |
| opening_out_left | Open figures | 0–150 | 149 | yes | saved |
| opening_out_right | Open figures | 0–150 | 149 | yes | saved |
| outside_partner_breaks | Breaks | 0–150 | 149 | yes | saved |
| position_closed | Positions | 0–120 | 119 | yes | saved |
| position_counter_promenade | Positions | 0–120 | 119 | yes | saved |
| position_double_hand | Positions | 0–120 | 119 | yes | saved |
| position_fan | Positions | 0–120 | 119 | yes | saved |
| position_open_facing | Positions | 0–120 | 119 | yes | saved |
| position_promenade | Positions | 0–120 | 119 | yes | saved |
| position_right_angle | Positions | 0–120 | 119 | yes | saved |
| position_shadow | Positions | 0–120 | 119 | yes | saved |
| position_side_by_side | Positions | 0–120 | 119 | yes | saved |
| promenade_to_closed | Transitions | 0–150 | 150 | once | saved |
| reverse_underarm_turn_left | Turns | 0–150 | 150 | once | saved |
| right_angle_to_closed | Transitions | 0–150 | 150 | once | saved |
| right_rock_turn | Turns | 0–150 | 150 | once | saved |
| right_side_pass | Passing figures | 0–150 | 150 | once | saved |
| shadow_to_closed | Transitions | 0–150 | 150 | once | saved |
| shoulder_to_shoulder | Breaks | 0–150 | 149 | yes | saved |
| side_basic | Foundation | 0–150 | 149 | yes | saved |
| side_by_side_to_closed | Transitions | 0–150 | 150 | once | saved |
| spot_turns | Turns | 0–150 | 150 | once | pending |
| sweetheart_wrap | Open figures | 0–150 | 149 | yes | pending |
| swivels | Turns | 0–150 | 149 | yes | pending |
| syncopated_breaks | Rhythm variations | 0–150.0 | 149.0 | yes | pending |
| underarm_turn_right | Turns | 0–150 | 150 | once | pending |

## Verification

The final post-stop read-only validation **passed 49/49 saved clips** (exit 0),
including all 16 directed-transition endpoint comparisons. Every report checksum
matches the preserved source manifest. All sampled loops passed pose and velocity
continuity. This is numeric verification of partial studies, not artistic approval.

Maximum measured errors (meters except loop velocity in meters/frame):
- `maximum_ik_error`: `0.000233943`.
- `maximum_plant_drift`: `0.000233943`.
- `maximum_palm_gap_error`: `0.006479950`.
- `loop_error`: `0.000000000`.
- `loop_velocity_error`: `0.000525361`.
- `transition_endpoint_error`: `0.000000798`.

Commands run from the app checkout:

```sh
export BLENDER=/workspace/.cloud-onboarding/3d-tools/blender-5.2.2/blender
python tests/run_tests.py --suite fast
BLENDER="$BLENDER" python tests/run_tests.py \
  --changed scripts/player_assets/test_animation_files.py \
  --changed scripts/player_assets/test_paired_animation_authoring.py \
  --changed scripts/player_assets/test_motion_review.py
python -m py_compile scripts/create_american_bolero.py scripts/validate_american_bolero.py
"$BLENDER" -t 2 --background animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/validate_american_bolero.py
```

The post-stop fast run passed **10/10** (10.45 s); focused checks passed **14/14**
(24.47 s, including ten fast checks). Python compilation passed. These checks
verify the preservation tooling; their success does not certify choreography.
The final saved-file validator runs without render arguments and writes only its
JSON report, leaving every `.blend` intact. Source hashes identify the tested bytes.

The validator samples keys, phase midpoints and fractional frames every three
frames. Tolerances in meters: IK/plant drift 0.006, palm-gap error 0.020,
floor penetration 0.008, torso-center separation at least 0.30, stride at most
0.75, loop closure 0.0001. Loop velocity tolerance is 0.012 meters/frame.
Mesh-floor sampling covers start, middle authored pose and end. Torso distance
is a clearance proxy; palm positions do not establish complete finger-surface
contact or physical balance. Numeric passing results do not replace visual review.

Earlier verification history is retained in the logs:

- Basic source composition using `animation_file_startup.py` and the archived
  `check_source.py` passed (`BOLERO_SOURCE_COMPOSITION_PASS american_bolero_basic`),
  checking 24 fps, chooser presence, two action slots and corresponding NLA slots.
- A 32-clip intermediate pass had 29 passes and three failures: crossover breaks,
  opening out right and spot turns. Subsequent pre-stop reach/path fixes were
  followed by a passing 12-clip targeted check, including transition references.
- Shadow styling had a passing targeted check and four rendered stills.
- Earlier targeted JSON reports were overwritten by each later validator run;
  their logs remain historical evidence with their own source checksums.
- An earlier broad `BLENDER="$BLENDER" python tests/run_tests.py` attempt selected
  ten fast and 57 slow checks. Existing runtime `.res` LFS pointers and missing
  `.godot/imported` resources caused model-load errors; an activity check stalled.
  The run was interrupted and its process tree cleaned up. Existing assets were
  then hydrated, but a complete runtime import and broad rerun remain outstanding.
  The broad suite is **not recorded as passing**.

## Processes and preserved outputs

At the stop instruction, PID 3931 was running the Blender `--style-existing`
pass. SIGTERM ended it (exit 143) after 44 logged completed saves. The owned Xvfb
server PID 3144, display `:99`, was subsequently terminated. Further animation
processes were not started. The read-only validator and both test-suite processes exited successfully;
zero owned Blender, render, Xvfb or test processes remain at preservation completion.

The original outputs remain locally in
`/workspace/sanjo-solutions/apps/a-game/.cache/american_bolero/`.
`playback/` contains 4 fps review PNG sequences; `review/` contains selected
Cycles stills; `styled/` contains the shadow styling example. Contact sheets are
`playback_sheet.jpg`, `figures_sheet.jpg`, `positions_sheet.jpg`. The committed
archive preserves these existing outputs together with `probe.blend`, `probe.png`
and diagnostic scripts. Logs are copied separately. The cache's downloaded Xvfb
package/extracted executable and package-index HTML are environment utilities,
not task assets. The probe is an exploratory scene, not a deliverable animation.

## Remaining work and blockers

1. Obtain renewed authorization before running any authoring, refinement or render
   command. Preservation takes precedence over the original completion request.
2. Finish/review the five pending released-arm refinements; inspect all 49 saved
   clips in playback and verify natural shoulders, wrists, fingers, support,
   planted contacts, limb clearance and transitions. Final visual approval is open.
3. Address the final report's failures if present, then rerun full saved-file
   checks. Validate sequencing of traveling figures with pair-level alignment.
4. Broaden authentic choreography with a chosen syllabus/reference. Current open
   promenade, released underarm rotation and released/single-hand sweetheart
   versions are simplified blocking interpretations. Continuous overhead contacts,
   a two-hand wrap and reverse-role variants remain future work.
5. Bake/export requested runtime clips via the existing add-on workflow and save
   their individual sources. Runtime delivery has not begun.
6. Restore Godot's imported runtime resources before attempting the broad suite;
   use the suite runner's timeout and cleanup behavior. Environmental test failure
   history must remain distinct from actual animation validation failures.

## Exact resume commands (future reference only)

After explicit authorization to resume, restore the checkout and shared LFS
sources, then use Blender 5.2.2. Inspect this record and the report before edits.

```sh
cd /workspace/sanjo-solutions/apps/a-game
export BLENDER=/workspace/.cloud-onboarding/3d-tools/blender-5.2.2/blender
"$BLENDER" --version
# Finish only the five saved studies whose final styling pass was pending.
"$BLENDER" -t 2 --background animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/create_american_bolero.py \
  -- --style-existing --only spot_turns sweetheart_wrap swivels syncopated_breaks underarm_turn_right
# Validate the complete current set; targeted reports overwrite the same JSON.
"$BLENDER" -t 2 --background animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/validate_american_bolero.py
# Optional future still review; this renders and therefore requires resumed authority.
"$BLENDER" -t 2 --background animations/man_and_woman/shared_scene_data.blend \
  --disable-autoexec --python-exit-code 1 --python scripts/validate_american_bolero.py \
  -- --render-only --render .cache/american_bolero/resumed_review
python tests/run_tests.py --suite fast
BLENDER="$BLENDER" python tests/run_tests.py
```

For runtime output, enable Player Asset Export, open an individual source through
**Helpers > Animation > Select animation > Edit animation file**, choose
**Bake & Export Active Animation**, and save the source to preserve the baked
animation. Record actual exported paths and hashes after that future operation.

## Storage and integration

The 49 `.blend` files total **7,480,404 bytes**, ranging from **123,016** to
**174,671 bytes**. Actual sizes and inherited attributes were inspected before
staging: root `*.blend` initially selected LFS; exact-filename overrides select
ordinary Git for this task. Every new binary/archive is at most 104,857,600 bytes.
The evidence archive contains 837 files and is **93,190,451 bytes**, using ordinary Git
(`filter: unspecified` inspected before staging). Existing linked/shared source LFS settings
remain intact. Publishing these task assets uses ordinary Git object upload;
this task introduces zero new LFS objects requiring separate upload.

The preservation commit is followed by a fetch/rebase onto `origin/main`, a
separate `# Animation` guidance commit, then integration with freshly fetched
main and an ordinary push. Concurrent task changes are retained. Final task and
merge hashes and remote-main verification are reported in the chat delivery.
Each new commit carries exactly one Codex co-author trailer; GitHub commit
communications are authored by Codex.

### Integration verification update

The preservation commit rebased onto `8648f10ee` as
`b19227aed7e32f908c8254777605397359a5f4d1`. The sole conflict was appended
`.gitattributes` entries; both task sets were retained. Concurrent main converted
shared/anatomical sources from LFS to ordinary Git under the repository size
policy. SHA-256 comparison against the original LFS OIDs confirmed identical
contents for all three scene/character dependencies; this task made zero changes
to those contents. The saved-source numeric report therefore retains its tested
geometry. The newer IK helper changes quaternion sign alignment during authoring;
existing saved bolero curves remain byte-identical.

After rebase, `python scripts/lfs_policy.py check` passed for 24,231 indexed
files. The fast suite passed 10/10 (8.99 s), and the same focused checks passed
14/14 (17.40 s). The newly documented bundled animation-tools setup was run with
Blender 5.2.2 and passed; it changed local preferences only. See the three
`integrated_*.log` files. All 837 archived review files also passed an archive
extraction/checksum comparison against `saved_review_outputs.json`.

A separate documentation commit adds paired-rhythm, contact-preservation and
report-coverage guidance under `# Animation` in `AGENTS.md`. For future Blender
processes on this newer main, follow its setup requirement before opening scenes:

```sh
cd /workspace/sanjo-solutions/apps/a-game
export BLENDER=/workspace/.cloud-onboarding/3d-tools/blender-5.2.2/blender
"$BLENDER" --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
```

The final pre-push merge was based on freshly fetched `2d0db14bd`. Both append
conflicts (`AGENTS.md` and per-animation `.gitattributes`) retained both chats'
content. All 49 indexed source hashes and the three shared/character dependency
hashes matched their preserved values. The storage-policy check passed for
30,320 indexed files, and the merged fast suite passed 10/10 (8.41 s); see
`logs/merged_fast.log`. Push retries integrate newer main through ordinary merges.
