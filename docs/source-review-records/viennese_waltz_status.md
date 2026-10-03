# Viennese waltz preservation status

Recorded by Codex on 2026-10-02. Animation stop observed at 15:01:26 UTC (17:01:26 Europe/Berlin). Chat/task title: “Viennese waltz for man_and_woman3.blend” (descriptive task title; application sidebar title was unavailable). Source branch: `codex/viennese-waltz`. Current commit at stop: `3c52737c74b488501e9cfe47e7029547c6f5fe88`. Project: A-Game, `/workspace/sanjo-solutions/apps/a-game`, sanjo-solutions managed cloud environment.

## Stop and delivery scope

The user's latest instruction stops animation authoring, refinement, generation, and rendering. This record preserves the present state for later authorized work. All owned Blender processes had completed before the stop; `ps -o pid,ppid,etime,args -C blender` showed an empty process list. Post-stop work consists of documentation, archiving existing outputs, verification, and Git delivery. Tests started for preservation have completed. Animation work remains paused.

Original scope: create a broad, organized Viennese waltz repertoire for both characters, with natural motion, planted contacts, body clearance, smooth transitions, interpolated and loop checks, and reuse of suitable existing work. Use Blender 5.2 throughout, follow per-animation files, store assets at or below 104,857,600 bytes in ordinary Git, commit/rebase, document useful lessons, merge main, push, and upload required assets. The stop instruction prioritizes preserving these partial studies over completing that repertoire.

## Exact completed state

38 individually saved paired procedural blocking studies exist. All are **authored partial sources; baked: none; exported: none**. The names describe intended figures and positions, rather than certified dance technique or completed choreography. Even a geometric validation pass requires artistic playback review. Pivot and fleckerl studies particularly require technique review. Coverage is 7 position studies, 9 core figure phrases, 10 social/open variations, and 12 directed transitions. There is no claim of every Viennese waltz move or syllabus being complete.

Man is lead (`Man.rigify`, slot `OBMan.rigify`); Woman is follow (`Woman.rigify`, slot `OBWoman.rigify`). Every source has synchronized paired slots, BOTH participant metadata, NLA slot bindings, count/bar markers, and an editable action. The unchanged shared scene provides rigs and geometry. Sources compose and are discoverable through the existing chooser. The combined `man_and_woman3.blend`, shared scene, anatomical sources, and runtime libraries were left unchanged.

Blender used for all Blender work: `/workspace/tools/blender-5.2.2-linux-x64/blender`, version 5.2.2 LTS, build `d13f752e3b9c`. The system Blender 4.3.2 was excluded. Saved timing is 24 fps, 180 quarter-note beats/minute, 3/4, 8 frames/count. Source composition inherits the shared scene's 24 fps. Four change phrases span 0–24; `closed_to_shadow` spans 0–96; the other 33 span 0–48. The catalog records exact loop flags, playback ends, root displacement, first foot, hold endpoints, contact intervals, and planted targets. Traveling loops require accumulated root displacement.

The authoring script reuses the existing paired IK/contact API, yoga pose/control infrastructure, activity action-channel writer, and AnimationFileWriter. The existing disco neutral-wrist construction informed fitting; its solo dance animation was not copied as a waltz phrase.

### Saved assets versus procedural source

The current generator is ahead of saved output. A complete 38-file build was followed by selective rebuilds of `closed_to_counter_promenade`, `closed_to_shadow`, `natural_turn`, `natural_fleckerl`, `open_natural_turn`, and `reverse_pivot`. Later generator edits include extra radial clearance and lower free hands that were never generated. Batched restoration, torso-local transitions, grip correction/release, extended shadow/side-by-side timing, revised change travel, and cyclic alternating-support changes are present in code but only selectively reflected in binaries. The saved catalog and SHA-256 manifest are authoritative for this checkpoint. Running the current generator will change the preserved studies and requires new authorization.

## File inventory

All paths below are relative to `apps/a-game`.

- `scripts/create_viennese_waltz.py`: procedural authoring work in progress; current code differs from some saved studies.
- `scripts/validate_viennese_waltz.py`: saved-file geometric validator and existing diagnostic renderer; overall motion validation fails.
- `scripts/viennese_waltz.md`: draft workflow and repertoire guide, marked paused/partial at delivery.
- `animations/man_and_woman/viennese_waltz_catalog.json`: exact saved ranges, paired roles, plant/contact declarations, key frames and repeat displacement.
- `animations/man_and_woman/viennese_waltz_validation.json`: final pre-stop full validation, 38 source hashes, measurements, worst frames, tolerances, and 12 transition endpoint comparisons.
- `animations/man_and_woman/.gitattributes`: 38 exact-filename ordinary-Git exceptions, retaining existing Acro Yoga exceptions and shared-source LFS rules.
- `docs/animation_work_status/viennese_waltz_status.md`: this preservation record.
- `docs/animation_work_status/viennese_waltz_asset_manifest.json`: each source's exact byte size and SHA-256.
- `docs/animation_work_status/viennese_waltz_preserved_evidence.zip`: existing review output and session logs/scripts, described below.

Every row below is authored partial / baked none / exported none. “Pass” means the current geometric checks pass, rather than artistic completion. Each filename has the prefix `viennese_waltz_` and suffix `.blend` and resides in `animations/man_and_woman/`.

| Filename stem after prefix | Stored frames | Playback end / mode | Bytes | Geometric result |
| --- | --- | --- | ---: | --- |
| `backward_change_natural_to_reverse` | 0–24 | 23 / loop | 127263 | Pass |
| `backward_change_reverse_to_natural` | 0–24 | 23 / loop | 127686 | leg_gap |
| `closed_hold` | 0–48 | 47 / loop | 121760 | Pass |
| `closed_to_counter_promenade` | 0–48 | 48 / once | 166936 | Pass |
| `closed_to_open_facing` | 0–48 | 48 / once | 153025 | Pass |
| `closed_to_promenade` | 0–48 | 48 / once | 164296 | Pass |
| `closed_to_shadow` | 0–96 | 96 / once | 208205 | leg_gap |
| `closed_to_side_by_side` | 0–48 | 48 / once | 161023 | palm_gap, torso_gap, leg_gap, self_leg_gap |
| `closed_to_two_hand` | 0–48 | 48 / once | 151138 | palm_gap |
| `contra_check_and_recovery` | 0–48 | 48 / once | 135812 | Pass |
| `counter_promenade_hold` | 0–48 | 47 / loop | 122462 | Pass |
| `counter_promenade_progressive` | 0–48 | 47 / loop | 144265 | Pass |
| `counter_promenade_to_closed` | 0–48 | 48 / once | 166287 | palm_gap |
| `forward_change_natural_to_reverse` | 0–24 | 23 / loop | 127569 | Pass |
| `forward_change_reverse_to_natural` | 0–24 | 23 / loop | 128601 | Pass |
| `hesitation_left` | 0–48 | 47 / loop | 135943 | Pass |
| `hesitation_right` | 0–48 | 47 / loop | 135022 | Pass |
| `natural_fleckerl` | 0–48 | 47 / loop | 170784 | leg_gap |
| `natural_pivot` | 0–48 | 47 / loop | 168329 | leg_gap, self_leg_gap |
| `natural_turn` | 0–48 | 47 / loop | 170624 | Pass |
| `open_facing_hold` | 0–48 | 47 / loop | 121875 | Pass |
| `open_facing_to_closed` | 0–48 | 48 / once | 153968 | Pass |
| `open_natural_turn` | 0–48 | 47 / loop | 170338 | loop_velocity, self_leg_gap |
| `open_reverse_turn` | 0–48 | 47 / loop | 168567 | self_leg_gap |
| `promenade_hold` | 0–48 | 47 / loop | 122480 | Pass |
| `promenade_progressive` | 0–48 | 47 / loop | 145004 | Pass |
| `promenade_to_closed` | 0–48 | 48 / once | 164367 | Pass |
| `reverse_fleckerl` | 0–48 | 47 / loop | 169330 | leg_gap, self_leg_gap |
| `reverse_pivot` | 0–48 | 47 / loop | 170952 | self_leg_gap |
| `reverse_turn` | 0–48 | 47 / loop | 168281 | leg_gap, self_leg_gap |
| `shadow_hold` | 0–48 | 47 / loop | 121748 | Pass |
| `shadow_progressive` | 0–48 | 47 / loop | 134544 | Pass |
| `shadow_to_closed` | 0–48 | 48 / once | 159795 | palm_gap, leg_gap, self_leg_gap |
| `side_by_side_hold` | 0–48 | 47 / loop | 121093 | Pass |
| `side_by_side_progressive` | 0–48 | 47 / loop | 134298 | Pass |
| `side_by_side_to_closed` | 0–48 | 48 / once | 160907 | palm_gap, torso_gap, leg_gap, self_leg_gap |
| `two_hand_hold` | 0–48 | 47 / loop | 121922 | Pass |
| `two_hand_to_closed` | 0–48 | 48 / once | 151801 | palm_gap |

## Verification and concrete blockers

Final full motion validation completed before stop with exit 1: **23/38 pass; 15/38 fail**. All report SHA-256 values match the preserved binaries. All 12 directed hold-transition endpoint checks pass (maximum error below 0.000001 world units). Samples include half frames, keys and plant boundaries; mesh floor checks run every 8 frames. Tolerances and capsule radii remain recorded in the JSON report. These approximations do not establish full mesh/body clearance or biomechanical balance.

Outstanding measured failures: partner or same-person leg clearance in turns/fleckerls/pivots and large transitions; palm separation in several transitions; torso clearance in side-by-side transitions; open natural turn loop velocity. For example, closed-to-shadow minimum leg gap is -0.0216173, natural fleckerl -0.00732236, open natural turn self-leg gap -0.04361 and loop velocity 0.03212/frame. The complete table and report locate each failure. Current guide and generator design claims require comparison with saved outputs before resuming.

Commands run from the app:

```sh
/workspace/tools/blender-5.2.2-linux-x64/blender -t 4 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_viennese_waltz.py
# Exit 1; 23 pass, 15 fail. Preserved /tmp/waltz-validate-all.log.
```

Existing source-composition check (`/tmp/check_waltz_source.py`, preserved in the evidence archive) opened `viennese_waltz_closed_hold.blend` with Blender 5.2.2 and `animation_file_startup.initialize()`: PASS, 24 fps, range 0–48, runtime composed scene, available linked libraries, chooser and both rig animation data. Existing combined-library check (`/tmp/check_waltz_library.py`) opened unchanged `man_and_woman3.blend`, registered Player Asset Export, linked all 38 sources, and asserted chooser entries, two action slots and both NLA bindings: PASS. These checks did not save the combined library.

Preservation verification on 2026-10-02:

- Required fast suite: 10/10 PASS in 6.38s (`waltz-stop-fast.log`).
- Fast plus focused animation-file, motion-landmark and paired-authoring tooling: 13/13 PASS in 11.80s (`waltz-stop-verification.log`).
- Initial ordinary multi-CPU runs exposed an existing process-cleanup scheduling race in `tests/test_run_tests.py::RunnerOutcomeTest.test_completion_releases_resources_owned_by_descendants` (assertion immediately after descendant SIGKILL). CPU-affinity-constrained runs pass. Test code remains unchanged.
- Initial LFS fixture availability failures were resolved by fetching the three hair mesh fixtures. Shared scene, anatomical sources, linked prop and existing split-animation LFS dependencies were retrieved. The environment retains these local objects.
- Source hash comparison: 38/38 match the final report. The delivery process also checks whitespace, staged binary bytes and effective Git attributes before committing.

Exact passing commands:

```sh
cd /workspace/sanjo-solutions/apps/a-game
python - <<'PYFAST'
import os, subprocess
os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
raise SystemExit(subprocess.call(['python', 'tests/run_tests.py', '--suite', 'fast']))
PYFAST
python - <<'PYFOCUSED'
import os, subprocess
os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
os.environ['BLENDER'] = '/workspace/tools/blender-5.2.2-linux-x64/blender'
raise SystemExit(subprocess.call(['python', 'tests/run_tests.py',
    '--changed', 'scripts/create_viennese_waltz.py',
    '--changed', 'scripts/validate_viennese_waltz.py',
    '--changed', 'scripts/player_assets/test_animation_files.py',
    '--changed', 'scripts/player_assets/test_paired_animation_authoring.py']))
PYFOCUSED
```

## Preserved processes and visual outputs

There are zero owned in-flight Blender, authoring, rendering or export processes. The verification processes also completed. The archive retains all existing files in `.cache/viennese_waltz/` (55 PNGs, 10,219,214 PNG bytes), including `review/`, `diagnostic/`, and 38 `overview/<clip>/000.png` images. Overview images sample frame 24 of an earlier build and are **stale relative to selective rebuilds**. Diagnostics include natural-turn frames 13/26/41 from an older pose version. The `right_offset` attempt failed during stale-catalog range validation; its log is retained. The archive also contains the earlier `/tmp/waltz-overview.png` 2880×3360 montage, `/tmp/waltz-pose.png` early pose image, all available `/tmp/waltz*.log`, and both `/tmp/check_waltz*.py` verification scripts. Rendering stopped before a current full playback review. These images are historical diagnostic evidence, not final animation previews.

## Storage and delivery

The 38 Blender sources total 5,648,300 bytes; the largest is 208,205 bytes. Each is below 104,857,600 bytes and uses an exact ordinary-Git exception. The evidence ZIP is also below that limit and follows ordinary Git attributes. Existing shared scenes, anatomical sources, props, and prior animation LFS settings are retained. This task introduces zero LFS assets; its new assets upload with the ordinary Git push. Git task and integration hashes are reported in the delivery response because a committed document cannot contain its own commit hash. Integration fetches current origin/main immediately beforehand and preserves concurrent animation chats' changes with ordinary history-preserving pushes.

## Remaining work and exact resume entry points

Resume animation work only after a new user instruction. The next authoring task is to reconcile the generator with the saved checkpoint, solve the 15 measured failures, verify every interpolated phrase and loop, review dance technique/natural motion and support, and review complete playback. Restore or improve dedicated pivots/fleckerls as needed; assess syllabus coverage with the user. Bake/export and runtime verification remain separate pending work. The original broad completion goal has not been fulfilled.

Read-only inspection can start with:

```sh
cd /workspace/sanjo-solutions/apps/a-game
cat docs/animation_work_status/viennese_waltz_status.md
cat animations/man_and_woman/viennese_waltz_validation.json
unzip -l docs/animation_work_status/viennese_waltz_preserved_evidence.zip
/workspace/tools/blender-5.2.2-linux-x64/blender --version
```

After renewed authorization, preserve this checkpoint on a new branch before generating:

```sh
cd /workspace/sanjo-solutions
 git switch -c codex/viennese-waltz-resume origin/main
cd apps/a-game
BLENDER=/workspace/tools/blender-5.2.2-linux-x64/blender
# First reconcile current generator with this checkpoint; selected generation overwrites a source.
"$BLENDER" -t 4 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/create_viennese_waltz.py -- --only natural_fleckerl
"$BLENDER" -t 4 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_viennese_waltz.py
# Diagnostic rendering, only after renewed authorization:
"$BLENDER" -t 4 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_viennese_waltz.py -- --render-only --render .cache/viennese_waltz/resumed_review
```

Re-run the fast and focused commands above after changes. Use the existing Player Asset Export UI for any later authorized bake/export and retain baked actions in individual source files. Check actual bytes and effective attributes before staging each binary. All delivery commits carry exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer. Any GitHub communication for this task is authored by Codex.

## Integration verification addendum

The preservation commit was rebased onto fetched `origin/main` at `074c6a02e`; its resulting task hash is `43b5a3c793843e2baf9fa680d47b968858057e49`. The `.gitattributes` conflict was resolved by retaining the complete incoming file and appending the 38 task-specific entries. Incoming main includes the repository-wide size-based storage policy, so current shared-source attributes now follow that upstream policy; the earlier LFS references in this record describe the authoring checkpoint. This task preserves those concurrent conversions.

After rebase, the fast plus focused tooling suite passed 13/13 in 11.34s using the same CPU-affinity command. `python scripts/lfs_policy.py check` from the repository root passed for 24,147 staged files. `git diff --check` and evidence ZIP integrity also passed. Motion measurements and rendered reviews above describe the saved pre-stop validation environment; integration did not regenerate, render, bake, or export any animation. The Animation section of `apps/a-game/AGENTS.md` now records composed-source musical timing, traveling-loop displacement/velocity checks, and the distinction between transition endpoints and intermediate clearance. All original main documentation additions were retained.
