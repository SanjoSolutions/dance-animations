# Shuffle dance partial work status

- Date: October 2, 2026, Europe/Berlin (CEST). Stop and preservation occurred around 16:56–17:02.
- Chat/task title: “Shuffle dancing solo animations for man_and_woman3.blend” (descriptive task title).
- Project: A-Game, `apps/a-game`, sanjo-solutions cloud environment.
- Branch at stop: `work`; delivery branch: `codex/shuffle_dance_preservation`.
- Starting/current pre-preservation commit: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
- Author of this record and Git delivery: Codex.
- State: **Stopped at the user's explicit instruction. Partial procedural animation studies.**

## Scope and stopping point

The original request covered a broad, organized solo shuffle repertoire for both
characters in `man_and_woman3.blend`, Blender 5.2 throughout, sparse IK authoring,
planted contacts and body clearance, interpolated and loop validation, separate
animation files, runtime exports, documentation, commits, rebase, and main publication.

The generator defines 33 phrases per character, a target of 66 solo clips. At the
stop, **27 source files and 27 published GLBs existed: 23 man clips and four woman
clips**. Every preserved source contains one editable action and its matching
`.baked` action. All preserved clips span **0–48 at 24 FPS**, use a two-second loop,
and have one participant. Man clips use **PLAYER** and woman clips use **PARTNER**.
The remaining turns, transition phrases, combination, several stances, and most
woman counterparts exist only as generator definitions. These are planned work.

The source scene and shared rig/geometry files retain their original contents.
The work reuses `DiscoCharacter`, `DiscoWristPoser`, and `RigYogaPoser`. The installed
checkout-backed Player Asset Export loader supplies the per-animation workflow.
Game Rig Tools is absent from this cloud image, so the generator uses Blender's
native visual bake and the existing compact export scene and publication helpers.
Blender version: **5.2.2 LTS**, build `d13f752e3b9c`.

## Preserved source and export inventory

Every name below maps to
`animations/man_and_woman/<name>.blend`. Exact GLB and import-setting paths, byte
sizes, SHA-256 hashes, modification times, role metadata, and action ranges are
recorded in [asset_inventory.json](shuffle_dance_evidence/asset_inventory.json).
Each published GLB has an adjacent `.glb.import`. The shared runtime references
are retained in `models/player/animation_updates.tres` alongside existing clips.

“Bake keys / export samples” is the largest count on a channel, including the
repeated endpoint: 49 denotes the earlier whole-frame bake; 97 denotes the newer
half-frame bake and 48-Hz export. Numerical verification evaluates the source and
saved bake at every half frame, with following constraints muted on the baked rig.
It additionally checks GLB structure, solo rig membership, action name, and length.
It does **not** compare each GLB channel to the source or run a complete Godot import.

| Action | Role | Bake keys / export samples | Saved-source verification | Revision |
| --- | --- | --- | --- | --- |
| `shuffle_man_box_step_left` | PLAYER | 49 / 49 | PASS | earlier saved revision |
| `shuffle_man_charleston_left_lead` | PLAYER | 97 / 97 | PASS | latest build completed |
| `shuffle_man_charleston_right_lead` | PLAYER | 97 / 97 | PASS | latest build completed |
| `shuffle_man_heel_toe_left` | PLAYER | 49 / 49 | PASS | earlier saved revision |
| `shuffle_man_heel_toe_right` | PLAYER | 49 / 49 | PASS | earlier saved revision |
| `shuffle_man_kick_ball_change_left` | PLAYER | 97 / 97 | PASS | latest build completed |
| `shuffle_man_kick_ball_change_right` | PLAYER | 97 / 49 | PASS | INTERRUPTED: source newer than published GLB |
| `shuffle_man_ready_bounce` | PLAYER | 49 / 49 | FAIL — see blockers | earlier saved revision |
| `shuffle_man_reverse_v_step` | PLAYER | 49 / 49 | FAIL — see blockers | earlier saved revision |
| `shuffle_man_running_man` | PLAYER | 97 / 97 | PASS | latest build completed |
| `shuffle_man_running_man_diagonal_left` | PLAYER | 97 / 97 | PASS | latest build completed |
| `shuffle_man_running_man_diagonal_right` | PLAYER | 97 / 97 | PASS | latest build completed |
| `shuffle_man_running_man_high_knee` | PLAYER | 97 / 97 | PASS | latest build completed |
| `shuffle_man_running_man_low` | PLAYER | 97 / 97 | PASS | latest build completed |
| `shuffle_man_running_man_wide` | PLAYER | 97 / 97 | PASS | latest build completed |
| `shuffle_man_scissor_step` | PLAYER | 49 / 49 | PASS | earlier saved revision |
| `shuffle_man_scissor_step_wide` | PLAYER | 49 / 49 | PASS | earlier saved revision |
| `shuffle_man_side_slide_left` | PLAYER | 49 / 49 | PASS | earlier saved revision |
| `shuffle_man_side_slide_right` | PLAYER | 49 / 49 | PASS | earlier saved revision |
| `shuffle_man_t_step_left` | PLAYER | 97 / 97 | PASS | latest build completed |
| `shuffle_man_t_step_right` | PLAYER | 97 / 97 | PASS | latest build completed |
| `shuffle_man_t_step_switch` | PLAYER | 97 / 97 | PASS | latest build completed |
| `shuffle_man_v_step` | PLAYER | 49 / 49 | FAIL — see blockers | earlier saved revision |
| `shuffle_woman_charleston_left_lead` | PARTNER | 97 / 97 | PASS | earlier completed half-frame trial |
| `shuffle_woman_heel_toe_left` | PARTNER | 49 / 49 | PASS | earlier saved revision |
| `shuffle_woman_ready_bounce` | PARTNER | 49 / 49 | FAIL — see blockers | earlier saved revision |
| `shuffle_woman_running_man` | PARTNER | 49 / 49 | PASS | earlier saved revision |

These are **partial procedural/blocking studies**, including clips that pass the
numerical checks. A full visual, surface-clearance, transition, runtime-import,
and repertoire review remains outstanding. The documentation's repertoire table
is explicitly an intended catalog, rather than a claim that all clips exist.

## Code, documentation, and evidence

- `scripts/create_shuffle_dance.py`: durable generator, with quaternion-compatible
  shared-template rotations, one initial key for constant channels, quarter-beat
  control poses, explicit contact types, loop seam clamping, native half-frame
  visual bake, and 48-Hz export. The most recent complete rebuild stopped early.
- `scripts/verify_shuffle_dance.py`: saved-file verifier. Its preservation pass
  aggregates failures so each of the 27 saved sources is checked. The default
  complete-repertoire check expects all 66 sources; use the explicit file list
  shown below to verify this partial state.
- `scripts/render_shuffle_dance.py`: saved, **unexecuted and unverified** review-sheet
  script. It currently requires missing woman and turn sources. Keep it for a later
  authorized continuation.
- `scripts/shuffle_dance.md`: intended repertoire, timing, composition, commands,
  and explicit partial-state notice.
- `scripts/shuffle_dance_validation.json`: per-clip metrics from the most recent
  completed generation for each name. Metrics for the interrupted right kick
  may describe the preceding published revision; they are not a hash-bound receipt.
- `scripts/shuffle_dance_bake_validation.json`: complete preservation verification,
  with 23 passing clips and four failures.
- `.gitattributes`: exact-path Git storage exceptions for this task's measured
  binaries. Other assets retain their existing attributes.
- `docs/animation_work_status/shuffle_dance_evidence/interrupted_build.log`: final
  authoring output, including the last 12 completed clips before termination.
- `shuffle_dance_evidence/preserved_asset_verification.log`: complete saved-source
  verification output, including worst measured bone errors.
- `shuffle_dance_evidence/fast_suite.log` and `scoped_suite.log`: required test results.
- `shuffle_dance_evidence/earlier_bake_failures.log`: the earlier Charleston fidelity
  failure that motivated half-frame baking.
- `shuffle_dance_evidence/half_frame_bake_check.log`: passing independent Charleston
  check after that change, before the stop instruction.
- `shuffle_dance_evidence/inventory.log` and `asset_inventory.json`: read-only Blender
  inventory and exact files/hashes/sizes.
- `shuffle_dance_evidence/review_00.png`, `review_06.png`, `review_12.png`, and
  `review_18.png`: existing Blender workbench renders of an **earlier man running-man
  revision**. Frame 6 was visually inspected in chat. They are historical evidence,
  not renders of every final preserved revision.
- `shuffle_dance_evidence/last_temporary_export.glb`: preserved temporary exporter
  output. It identifies `shuffle_man_kick_ball_change_left.baked` and is a complete
  GLB, but remains evidence rather than another active runtime asset.

## Validation and known blockers

Required fast suite:

```sh
python tests/run_tests.py --suite fast
```

Result: **9/9 passed** in 5.25 seconds during preservation. An earlier attempt
reported missing LFS-backed hair fixture meshes; those fixtures were hydrated and
the suite then passed. Godot available here is 4.6.3. Blender work used 5.2.2 only.

Explicit code-scope suite:

```sh
python tests/run_tests.py --changed scripts/create_shuffle_dance.py \
  --changed scripts/verify_shuffle_dance.py --changed scripts/render_shuffle_dance.py
```

Result: **9/9 passed** in 4.59 seconds. The selector chose the fast set and zero
additional slow checks for these new script paths. The Blender verification below
provides the direct saved-animation checks; a full shared-scene integration suite
was not run and Game Rig Tools remains an environmental prerequisite for its tests.

Preservation verification:

```sh
blender --background --python-exit-code 1 --python scripts/verify_shuffle_dance.py -- \
  $(for path in animations/man_and_woman/shuffle_*.blend; do basename "$path" .blend; done)
```

Result: **23 passed, four failed**, exit 1, with every existing source visited.
The configured bounds are 0.012 meters and 0.045 radians for source-to-bake errors.
The largest passing errors were 0.0107159 meters and 0.0172219 radians.

Concrete failures preserved for later repair:

- `shuffle_man_ready_bounce`: `('shuffle_man_ready_bounce', 'bake position', 0.04654045979056123)`.
- `shuffle_man_reverse_v_step`: `('shuffle_man_reverse_v_step', 'bake position', 0.025759065542002458)`.
- `shuffle_man_v_step`: `('shuffle_man_v_step', 'bake position', 0.024862340089177887)`.
- `shuffle_woman_ready_bounce`: `('shuffle_woman_ready_bounce', 'bake rotation', 0.16092003881931305)`.

Additional blockers and review gaps:

- `shuffle_man_kick_ball_change_right.blend` contains the newer 97-key bake, while
  its published GLB contains the earlier 49-sample export. Its numerical source
  check passes, but source/export revision consistency is explicitly outstanding.
- Earlier files retain earlier choreography and interpolation. In particular,
  revised kick-ball-change weight transfer and V-step height exist in generator
  code, while some preserved GLBs still contain the preceding procedural versions.
- The two ready-bounce files predate the rotation-mode preservation correction.
- Generation checks measure feet, ground height, wrist/knee comfort, a hand/hip
  sphere proxy, and loop continuity. They establish those named checks, not whole
  body mesh separation. Surface contacts and complete natural-motion review remain.
- The target 66-clip repertoire is incomplete. Source discovery in the combined
  library and an end-to-end Godot import of the new catalog remain unverified.
- No additional animation authoring, refinement, generation, or rendering occurred
  after the stop was enforced. Verification and inventory only read the saved assets.

## Process and environment state

Owned authoring process PID 2172 ran the full generator with its log at
`/tmp/shuffle-task/build_all.log`. SIGINT did not stop Blender immediately; SIGTERM
then stopped it. The last confirmed published clip was the man's left
kick-ball-change; its right counterpart had reached source saving/export work.
The files above capture the durable boundary. No owned authoring or rendering
process remains. Inventory and verification processes completed afterward.

Existing helper logs and renders originated in `/tmp/shuffle-task`; durable
outputs were copied into the evidence directory. The temporary credential helper
is deliberately excluded from Git. Its script reads the configured environment
binding and contains no credential value. The environment has a ready
`SANJO_GITHUB_LFS_TOKEN` binding and permits GitHub and Blender downloads.

## Storage and delivery

Actual task binaries are all at or below 104,857,600 bytes. The largest is
`shuffle_man_t_step_switch.blend`, 861,670 bytes. Exact-path exceptions set
`-filter -diff -merge -text`; effective attributes are checked before staging.
The binary assets therefore travel in the ordinary Git push, with no new LFS
object uploads required. Existing LFS-backed source assets remain unchanged.

The preservation commit contains this status record and task-owned durable files.
The task branch is rebased onto freshly fetched `origin/main`, followed by a
separate `AGENTS.md` animation-workflow documentation commit and integration into
main. Delivery hashes and remote verification are reported in the chat's final
response and remain discoverable in Git history. Every new commit includes exactly
one `Co-authored-by: Codex <noreply@openai.com>` trailer.

## Exact resume commands

Run read-only validation immediately as needed. **Resume animation work only after
new explicit user authorization.** Commands start in `apps/a-game`:

```sh
blender --version
blender --background --python-exit-code 1 \
  --python scripts/player_assets/install_blender_addon.py
python tests/run_tests.py --suite fast
blender --background --python-exit-code 1 --python scripts/verify_shuffle_dance.py -- \
  $(for path in animations/man_and_woman/shuffle_*.blend; do basename "$path" .blend; done)
```

After authorization, start with the four fidelity failures and stale right-kick
export, reviewing the selected generator changes before rebuilding both roles:

```sh
blender --background animations/man_and_woman/solo_disco_dance.blend \
  --python-exit-code 1 --python scripts/create_shuffle_dance.py -- \
  ready_bounce v_step reverse_v_step kick_ball_change_right
```

Then complete the catalog and verify all saved sources:

```sh
blender --background animations/man_and_woman/solo_disco_dance.blend \
  --python-exit-code 1 --python scripts/create_shuffle_dance.py
blender --background --python-exit-code 1 --python scripts/verify_shuffle_dance.py
blender --background --python-exit-code 1 --python scripts/render_shuffle_dance.py
```

Review generated sizes and extend only the intended exact-path storage exceptions;
reopen the combined library and run Godot import/playback validation. Preserve
concurrent changes to `animation_updates.tres` by merging resource path sets and
regenerating their reference identifiers before committing further publication.

## Post-rebase delivery note

The preservation commit rebased cleanly as `8e198d843` onto fetched main commit
`18e528c73`. That incoming main now bundles Game Rig Tools and documents
`scripts/blender/install_animation_tools.py`. The tool was absent from the active
Blender profile during authoring; future authorized work can use the new bundled
installer. The stop-state assets remain byte-for-byte unchanged through this rebase.
The root storage policy check passed for 23,459 staged files after integration.
The accompanying `AGENTS.md` update adds independent-rig visibility checks,
contact categories, and interrupted source/export revision recording.

For the next authorized setup, prefer the current repository installer:

```sh
blender --background --python-exit-code 1 \
  --python scripts/blender/install_animation_tools.py
```

The required fast suite was repeated after the rebase: **10/10 passed** in 8.54
seconds. The incoming test catalog includes one additional fast check. Its full
output is `shuffle_dance_evidence/post_rebase_fast_suite.log`.
