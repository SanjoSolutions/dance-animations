# Partner paso doble — stopped work preservation

Date: 2026-10-02 (UTC). Recorded after the user's stop instruction.
Chat/task title: Partner paso doble animations (task label; UI title unavailable).
Branch at stop: `codex/partner-paso-doble`.
Current commit at stop: `3c52737c74b488501e9cfe47e7029547c6f5fe88`.
Project: A-Game, `apps/a-game`, sanjo-solutions cloud environment.

## Delivery state

**Paused, incomplete procedural blocking studies.** Preserve these sources for
resumption; motion acceptance remains pending. The original request covered all
Partner paso doble moves and positions with coordinated Man/Woman animation,
natural movement, planted contacts, clearance, smooth transitions, existing-asset
reuse, per-animation sources, Blender 5.2, validation, documentation, and Git delivery.
The planned interpretation comprises 58 clips: nine positions, 33 figures, and
16 directed transitions. The saved state contains **57 authored source studies**:
nine positions, 33 figures, and 15 directed transitions. The missing source is
`partner_paso_doble_spanish_line_to_closed.blend`.

**Authored: 57 partial studies. Baked: zero new actions. Exported: zero new GLBs
or Godot runtime clips.** Chooser discovery exposes the individual sources; their
presence conveys saved work, not motion approval. Existing runtime assets, shared
scene, anatomical source models, and combined library retain their tracked contents.

All Blender authoring, diagnostics, renders, and the preservation audit used
`/workspace/tools/blender-5.2.2-linux-x64/blender`, 5.2.2 LTS, build `d13f752e3b9c`.
The environment's Blender 4.3.2 executable was version-inspected only.
LFS dependencies were retrieved before use. Authoring reused `RigYogaPoser`, the
mountain posture, `DiscoWristPoser`, paired calibrated-palm authoring, native IK,
`ActivityMotionAuthor.write_samples`, and `AnimationFileWriter`. Existing complete
dance clips were examined as authoring references; the saved sources contain new
procedural motion rather than a certified reuse of an existing paso repertoire.

## Files and saved-state provenance

All paths below are relative to `apps/a-game`.

- `scripts/create_partner_paso_doble.py`: current generator, 58 intended definitions,
  paired formations, footfalls, root turns, sparse controls, selective foot correction,
  and calibrated hands. The latest hand-release transition approach remains unvalidated.
- `scripts/validate_partner_paso_doble.py`: saved-action motion checker, intended
  full-repertoire checks and interpolated sampling; current procedural definitions
  differ from several saved assets. A full run is expected to need reconciliation.
- `scripts/render_partner_paso_doble.py`: review-sheet renderer; retained for a future
  authorized session. Further rendering stopped.
- `scripts/partner_paso_doble.md`: intended choreography/workflow guide with a pause
  notice. Its timing descriptions describe the current generator's intent.
- `animations/man_and_woman/partner_paso_doble_catalog.json`: historical partial
  catalog, 43 records and 15 inherited authoring failures. It is not an authoritative
  inventory of the 57 files. A selected successful build can still exit with failure
  because the writer carries forward unrelated historical failure records.
- `animations/man_and_woman/partner_paso_doble_validation.json`: obsolete early
  two-clip report. Retained as historical evidence, not certification of current files.
- `animations/man_and_woman/.gitattributes`: exact-filename ordinary-Git exceptions
  for these 57 binaries, each 121,115–188,220 bytes; total 7,893,511 bytes.
- `docs/animation_work_status/partner_paso_doble/saved_source_inventory.json`:
  authoritative stop-state hashes, sizes, saved action names, slots, ranges, markers,
  key counts, finite-key checks, participant metadata, and serialized NLA bindings.
- `docs/animation_work_status/partner_paso_doble/inspect_saved_sources.py`:
  reproducible read-only Blender 5.2 library/action audit; it neither evaluates motion
  nor writes Blender assets.
- `docs/animation_work_status/partner_paso_doble/evidence/`: all retained task-specific
  `/tmp/paso*` logs, JSON snapshots, diagnostic scripts, and import-side-effect patches;
  plus the final preservation audit/test logs. Patch files are historical backup
  evidence only. Their import changes were restored and are excluded from delivery.
- `docs/animation_work_status/partner_paso_doble/previews/`: 18 historical PNGs:
  nine closed-position frames, eight sur-place frames, and one two-row pilot sheet.
  These show earlier variants and are not a review of the final saved file hashes.
  Exact PNG attributes retain these small files in ordinary Git.
- `docs/animation_work_status/partner_paso_doble/evidence_inventory.json` lists every
  preserved evidence/preview/tool file with byte size and SHA-256.

The interrupted full batch used an earlier in-memory generator revision than the
current source file. Later subset runs replaced selected assets. In particular,
`paso_transition_fix.log` records saving position_closed, position_promenade,
promenade_close, and closed_to_shadow with the latest hand-release code; its exit
failure lists inherited catalog failures. These four results received structural
inspection only. Source code and all saved binaries therefore span mixed revisions.

## Actual saved clips, timing, and roles

Every listed clip contains the synchronized `OBMan.rigify` and `OBWoman.rigify`
slots: Man is leader/player, Woman is follower/partner. Participant metadata is
`BOTH`. Timing intent is 24 fps, 120 BPM, 12 frames per beat. The following ranges
and playback ends come from saved action metadata, not current generator guesses.
“Loop” records intent only; seam acceptance remains pending. Duplicate final loop
poses use the preceding playback frame. Directed transitions and travel play once.

| Source stem (`animations/man_and_woman/`; append `.blend`) | Stored frames | Playback end | Intent |
| --- | --- | --- | --- |
| `partner_paso_doble_appels` | 0–48 | 47 | Loop |
| `partner_paso_doble_attack` | 0–96 | 95 | Loop |
| `partner_paso_doble_banderillas` | 0–192 | 191 | Loop |
| `partner_paso_doble_basic_backward` | 0–96 | 96 | Once |
| `partner_paso_doble_basic_forward` | 0–96 | 96 | Once |
| `partner_paso_doble_chasse_cape` | 0–192 | 191 | Loop |
| `partner_paso_doble_chasse_left` | 0–96 | 96 | Once |
| `partner_paso_doble_chasse_right` | 0–96 | 96 | Once |
| `partner_paso_doble_closed_to_counter_promenade` | 0–96 | 96 | Once |
| `partner_paso_doble_closed_to_open_counter_promenade` | 0–96 | 96 | Once |
| `partner_paso_doble_closed_to_open_facing` | 0–96 | 96 | Once |
| `partner_paso_doble_closed_to_open_promenade` | 0–96 | 96 | Once |
| `partner_paso_doble_closed_to_opposition` | 0–96 | 96 | Once |
| `partner_paso_doble_closed_to_promenade` | 0–96 | 96 | Once |
| `partner_paso_doble_closed_to_shadow` | 0–96 | 96 | Once |
| `partner_paso_doble_closed_to_spanish_line` | 0–96 | 96 | Once |
| `partner_paso_doble_counter_promenade_to_closed` | 0–96 | 96 | Once |
| `partner_paso_doble_coup_de_chapeau` | 0–96 | 95 | Loop |
| `partner_paso_doble_coup_de_pique` | 0–96 | 95 | Loop |
| `partner_paso_doble_drag` | 0–96 | 95 | Loop |
| `partner_paso_doble_elevation` | 0–96 | 95 | Loop |
| `partner_paso_doble_fallaway_reverse` | 0–96 | 96 | Once |
| `partner_paso_doble_farol` | 0–192 | 191 | Loop |
| `partner_paso_doble_finale` | 0–96 | 96 | Once |
| `partner_paso_doble_flamenco_taps` | 0–96 | 95 | Loop |
| `partner_paso_doble_fregolina` | 0–192 | 191 | Loop |
| `partner_paso_doble_grand_circle` | 0–192 | 191 | Loop |
| `partner_paso_doble_huit` | 0–192 | 191 | Loop |
| `partner_paso_doble_la_passe` | 0–288 | 287 | Loop |
| `partner_paso_doble_left_foot_variation` | 0–96 | 95 | Loop |
| `partner_paso_doble_open_counter_promenade_to_closed` | 0–96 | 96 | Once |
| `partner_paso_doble_open_facing_to_closed` | 0–96 | 96 | Once |
| `partner_paso_doble_open_promenade_to_closed` | 0–96 | 96 | Once |
| `partner_paso_doble_open_telemark` | 0–96 | 96 | Once |
| `partner_paso_doble_opposition_to_closed` | 0–96 | 96 | Once |
| `partner_paso_doble_position_closed` | 0–96 | 95 | Loop |
| `partner_paso_doble_position_counter_promenade` | 0–96 | 95 | Loop |
| `partner_paso_doble_position_open_counter_promenade` | 0–96 | 95 | Loop |
| `partner_paso_doble_position_open_facing` | 0–96 | 95 | Loop |
| `partner_paso_doble_position_open_promenade` | 0–96 | 95 | Loop |
| `partner_paso_doble_position_opposition` | 0–96 | 95 | Loop |
| `partner_paso_doble_position_promenade` | 0–96 | 95 | Loop |
| `partner_paso_doble_position_shadow` | 0–96 | 95 | Loop |
| `partner_paso_doble_position_spanish_line` | 0–96 | 95 | Loop |
| `partner_paso_doble_promenade` | 0–96 | 96 | Once |
| `partner_paso_doble_promenade_close` | 0–96 | 96 | Once |
| `partner_paso_doble_promenade_counter_promenade` | 0–96 | 95 | Loop |
| `partner_paso_doble_promenade_to_closed` | 0–96 | 96 | Once |
| `partner_paso_doble_separation` | 0–96 | 95 | Loop |
| `partner_paso_doble_shadow_to_closed` | 0–96 | 96 | Once |
| `partner_paso_doble_sixteen` | 0–192 | 191 | Loop |
| `partner_paso_doble_spanish_lines` | 0–96 | 95 | Loop |
| `partner_paso_doble_sur_place` | 0–96 | 95 | Loop |
| `partner_paso_doble_syncopated_separation` | 0–192 | 191 | Loop |
| `partner_paso_doble_tour_de_piste` | 0–192 | 192 | Once |
| `partner_paso_doble_travelling_spins` | 0–192 | 192 | Once |
| `partner_paso_doble_twists` | 0–96 | 95 | Loop |

## Verification and known failures

Final preservation verification, after animation work stopped:

- `BLENDER=/workspace/tools/blender-5.2.2-linux-x64/blender python tests/run_tests.py --suite fast`:
  **10/10 passed**, 6.21 seconds; `evidence/preservation_fast.log`.
- `BLENDER=/workspace/tools/blender-5.2.2-linux-x64/blender python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_paired_animation_authoring.py`:
  **13/13 passed**; `evidence/preservation_focused.log`. This covers the fast suite,
  per-animation file tooling, motion landmarks, and paired-authoring tooling.
- Blender 5.2 read-only `inspect_saved_sources.py`: **57/57 readable**, one paired
  action per file, both slots present, finite keys; `evidence/preservation_audit.log`.
- Blender 5.2 compiled all three current task Python scripts without running their
  authoring/validation/render entry points: passed; `evidence/preservation_syntax.log`.

Storage audit: all 75 staged binaries (57 Blender sources, 18 previews) matched
working-file bytes and used ordinary-Git blobs; shared sources retained `filter=lfs`
at that pre-rebase audit. Concurrent main subsequently converted small shared
sources to ordinary Git under the repository-wide 100 MiB policy. That policy
and the concurrent storage changes are preserved during integration.
`git diff --cached --check` reports whitespace in verbatim historical patch/log
copies; the task source/document changes pass with the evidence directory excluded.
These historical copies retain their original bytes for provenance.

These checks establish preservation integrity and tooling behavior. They do not
approve choreography, complete body clearance, or current loop/transition continuity.

Historical motion evidence: `evidence/paso_live_results.json` contains 55 checks
of mixed earlier revisions: **18 passed, 37 failed**. Failures include 29 body-overlap,
17 palm-contact, 11 planted-foot-drift, eight loop-velocity, and three IK-reach findings
(categories overlap). Interpolated samples include 1.5-frame spacing, extra .75-frame
samples each beat, and fractional loop-seam samples. Checker tolerances include
6 mm IK reach, 25 mm palm gap, 6 mm planted drift, floor ≥−12 mm, 60 mm torso capsule
clearance, zero counted body intersections outside palm-contact neighborhoods,
0.1 mm loop closure, and 0.12 loop velocity difference. Reports are historical and
lack binding to current hashes; do not transfer a passing result to a replaced file.

Selected earlier repair checks passed for five positions (`paso_check_arms.log`)
and attack/la_passe (`paso_check_timing.log`). The same timing check found an 85 mm
palm gap and 82 counted intersections in then-current promenade_close. That file
was subsequently replaced; its replacement has no motion-validation result.
The full saved suite and its visual review were incomplete at stop.

Earlier broad automatic suite selection chose 10 fast and 57 slow checks:
`BLENDER=/workspace/tools/blender-5.2.2-linux-x64/blender python tests/run_tests.py --slow-timeout 120`.
It encountered existing Godot import/resource errors; the activity-method test timed
out at 120 seconds. The run was terminated, and its owned processes cleaned up.
`paso_related_checks.log` preserves the result; `paso_checks_selected.log` preserves
selection. A bounded Godot headless import exited 0 while logging missing existing
image/floor resources (`paso_import.log`). Downloading existing LFS resources and
importing enabled the later focused checks. Tracked import/resource side effects
were restored; their backup patches remain evidence. The broad suite remains
incomplete, and runtime correctness is not claimed.

## Stopped processes and concrete resume blockers

At stop, SIGTERM was sent only to owned Blender PIDs 4873 (full author batch),
4911 (live validator), and 5448 (latest selected pilot). The pilot log already
contained its saved outputs and failing exit. A subsequent process listing showed
no Blender or test-runner processes. Saved output files were retained; no further
animation generation, refinement, or rendering was started. Later Blender work
consisted of read-only source inspection, Python syntax compilation, and the
required bundled-tool setup after rebasing onto updated main.

Resume blockers and remaining work:

1. Obtain renewed user authorization to resume animation work; the active request
   prioritizes preservation and delivery.
2. Reconcile each saved hash against the current procedural revision. The catalog
   omits saved older assets and retains 15 authoring failures. The missing Spanish-line
   return needs authoring in a future session. Do not blindly treat an interrupted
   generator's catalog or a reused clip name as authoritative provenance.
3. Resolve inherited pose-solver failures, palm interpolation, elbow/body overlaps,
   planted drift, and seam velocity failures. Current release/rejoin transitions,
   syncopation timing, wider spins, and longer cape/fregolina timing need validation.
   Current generator durations differ from several saved ranges above.
4. Validate all reloaded clips and directed endpoints against the same generator
   revision; inspect interpolated body geometry and grounded support visually.
   Existing procedural patterns require dance-quality review of every named figure.
5. Perform full-repertoire visual review and smooth-sequence testing. Baking,
   exporting, and runtime wiring remain future authorized work.
6. Revisit the broader Godot suite after resolving the documented resource/import
   environment issues. Fast and focused checks passed in the preserved environment.

## Post-rebase verification

Rebased the preservation commit onto `origin/main` at `f20ca0346`. The attributes
conflict was resolved by retaining all concurrent exact-file rules plus this task’s
57 entries. All saved-source hashes matched after rebase. The updated main
requires bundled animation-tool setup; its Blender 5.2 setup completed successfully
(`evidence/post_rebase_tools.log`). Fast checks passed 10/10 in 6.13 seconds and
focused checks passed 13/13 in 10.41 seconds (`post_rebase_fast.log` and
`post_rebase_focused.log`). `python scripts/lfs_policy.py check` passed for 24,761
staged files before the additional delivery logs were staged.

## Exact commands for a future authorized session

Run from `/workspace/sanjo-solutions/apps/a-game`. The installed absolute Blender
path belongs to this cloud environment; verify its presence/version before use.

```sh
cd /workspace/sanjo-solutions/apps/a-game
/workspace/tools/blender-5.2.2-linux-x64/blender --version
/workspace/tools/blender-5.2.2-linux-x64/blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
# Read-only integrity audit, safe while animation authoring stays paused:
/workspace/tools/blender-5.2.2-linux-x64/blender -t 2 -b --factory-startup --disable-autoexec --python-exit-code 1 --python docs/animation_work_status/partner_paso_doble/inspect_saved_sources.py
BLENDER=/workspace/tools/blender-5.2.2-linux-x64/blender python tests/run_tests.py --suite fast
BLENDER=/workspace/tools/blender-5.2.2-linux-x64/blender python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_paired_animation_authoring.py

# Following commands require renewed authorization and blocker review first.
# A subset build may exit 1 for failures carried forward from earlier catalog runs.
/workspace/tools/blender-5.2.2-linux-x64/blender -t 2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/create_partner_paso_doble.py -- --only position_closed position_promenade promenade_close closed_to_shadow
# Full authoring after resolving the procedural blockers:
/workspace/tools/blender-5.2.2-linux-x64/blender -t 2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/create_partner_paso_doble.py
/workspace/tools/blender-5.2.2-linux-x64/blender -t 2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_partner_paso_doble.py
/workspace/tools/blender-5.2.2-linux-x64/blender -t 2 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/render_partner_paso_doble.py
```

## Git delivery

All task binaries are below 104,857,600 bytes and use exact-file ordinary-Git
exceptions; concurrent main storage rules remain in effect. Consequently this
task introduces zero new LFS upload objects. Delivery commits preserve the partial
assets, evidence, and this status. A separate Animation guidance commit records
preservation/provenance lessons after fetching and rebasing onto origin/main.
Integration uses ordinary history-preserving pushes and retains concurrent work.
Commit and merge hashes, remote-main verification, and push outcome are reported
in the final delivery message because a committed file cannot contain its own hash.
All task GitHub commit communications are authored by Codex and include exactly
one `Co-authored-by: Codex <noreply@openai.com>` trailer per new commit.
