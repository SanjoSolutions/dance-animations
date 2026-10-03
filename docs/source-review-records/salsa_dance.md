# Salsa dance work status

- Date: 2026-10-02 (Europe/Berlin).
- Chat/task: Create animations for `man_and_woman3.blend` — Salsa dance. The desktop sidebar title was unavailable to this execution session.
- Stop instruction: the user directed all animation chats to stop animation work and prioritize recording, preservation, verification, and delivery. Authoring, refinement, generation, and rendering stopped immediately on receipt. Subsequent Blender execution is read-only validation.
- Branch at recording: `work`.
- Current commit before this record: `80bbe3ece` (animation guidance).
- Rebased asset commit: `82c917344`.
- Upstream used for rebase: `c5cb5336b`.
- Original task commit `3b414bff7` was replaced before publication to store the task binaries as regular Git; the intermediate conversion commit was `f1547d5fc`.

## Scope and stopping point

The request asked for salsa animations, including all salsa moves. The saved result is a finite 35-clip On1 repertoire: foundations, leader/follower turns, cross-body figures, Cuban figures, and 13 shines. Regional styles, every named variation, and arbitrary combinations are outside this finite catalog.

These are **procedurally authored, editable animation/blocking studies**, with targeted IK/contact checks and representative rendered pose reviews. They are complete saved control-rig actions for the listed repertoire, rather than a claim of comprehensive choreographic or physical realism. Full mesh collision, balance, finger-surface contact throughout every clip, expert dance review, and continuous rendered playback remain separate review work.

All 35 source assets are saved. No source file is an interrupted generation or partial write. The natural-motion/presentation review is partial as described above. All salsa actions are **authored**; salsa deform-rig **bakes and game exports were not produced**. Existing unrelated baked actions in the combined scenes belong to earlier work.

The user stop instruction arrived while Git rebase was paused on `.gitattributes` and `man_and_woman3.blend` conflicts. Resolution retained the latest upstream size-based LFS policy and main Blender scene. The previously saved salsa combined scene was preserved byte-for-byte as `man_and_woman3_salsa_checkpoint.blend`, at the app root so its relative library paths retain their base directory. The 35 salsa source files are also byte-identical to their validated pre-rebase versions.

`man_and_woman3.blend` at the rebase commit is the upstream scene, preserving concurrent animation libraries. The salsa source files are available to the existing Helpers source discovery. Explicit relinking/resaving of the newer main scene was left for a resumed task; no post-stop animation installation or scene regeneration occurred. The checkpoint contains the prior scene and links, including the salsa selection; its dependencies resolve to the current checkout, so it is not a self-contained snapshot of all historical linked assets.

## Durable files

- `man_and_woman3_salsa_checkpoint.blend`: previous combined salsa scene, 35 salsa links plus the 367 original tracks verified before rebase; selected `salsa_basic`, playback 0–79 at 24 FPS.
- `scripts/salsa_choreography.py`: finite move catalog, routes, On1 footfall timing, and sparse key samples.
- `scripts/create_salsa_dance.py`: paired IK writer, relaxed wrist/contact preparation, quaternion sign alignment, loop closure, contact correction, split-file writer, and optional library installer.
- `scripts/review_salsa_dance.py`: read-only saved-motion measurement and optional representative rendering. The delivery run omits `--render`.
- `scripts/test_salsa_choreography.py`: four choreography tests.
- `scripts/salsa_dance.md`: move catalog, playback/editing instructions, and generation/review commands. Its installation description refers to the authored salsa scene; the checkpoint and newer main distinction is recorded here.
- `scripts/salsa_dance_validation.json`: pre-rebase successful evaluation of all 35 saved clips over 3,235 frames with Blender 5.2.2.
- `AGENTS.md`, `# Animation`: salsa examples, raised handhold staging, and quaternion/loop lessons added in commit `80bbe3ece` alongside upstream guidance.
- `docs/animation_work_status/salsa_asset_manifest.json`: exact preserved asset sizes and SHA-256 values, plus the shared scene used for delivery verification.
- `docs/animation_work_status/salsa_delivery_validation.json`: delivery verification result, recorded after the read-only check finishes.

Every task Blender file is at or below 100 MiB and is stored as a real regular-Git binary. The checkpoint is 30,406,294 bytes. The generated root storage policy from upstream is retained. These task commits require no LFS upload.

## Clip inventory and roles

Timing is 144 BPM at 24 FPS, ten frames per count. Weight changes occur on counts 1, 2, 3, 5, 6, 7; 4 and 8 are holds. All actions have slots for `Man.rigify` and `Woman.rigify`. Paired `player` is Man; paired `partner` is Woman. Shines animate both independently, with initial origins spaced 1.3 meters apart. The final frame of a loop is its closing pose. Every row is authored-only, with baking/export still pending.

| Asset | Stored frames | Playback | Roles |
| --- | --- | --- | --- |
| `animations/man_and_woman/salsa_basic.blend` | 0–80 | 0–79 loop | Man leads / Woman follows |
| `animations/man_and_woman/salsa_side_basic.blend` | 0–80 | 0–79 loop | Man leads / Woman follows |
| `animations/man_and_woman/salsa_back_basic.blend` | 0–80 | 0–79 loop | Man leads / Woman follows |
| `animations/man_and_woman/salsa_cumbia_basic.blend` | 0–80 | 0–79 loop | Man leads / Woman follows |
| `animations/man_and_woman/salsa_open_break.blend` | 0–80 | 0–79 loop | Man leads / Woman follows |
| `animations/man_and_woman/salsa_guapea.blend` | 0–80 | 0–79 loop | Man leads / Woman follows |
| `animations/man_and_woman/salsa_closed_basic.blend` | 0–80 | 0–79 loop | Man leads / Woman follows |
| `animations/man_and_woman/salsa_follower_right_turn.blend` | 0–80 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_follower_left_turn.blend` | 0–80 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_leader_right_turn.blend` | 0–80 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_leader_left_turn.blend` | 0–80 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_follower_double_right_turn.blend` | 0–160 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_cross_body_lead.blend` | 0–80 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_cross_body_inside_turn.blend` | 0–160 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_cross_body_outside_turn.blend` | 0–160 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_reverse_cross_body.blend` | 0–160 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_copa.blend` | 0–80 | 0–79 loop | Man leads / Woman follows |
| `animations/man_and_woman/salsa_enchufla.blend` | 0–80 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_dile_que_no.blend` | 0–80 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_vacilala.blend` | 0–80 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_hecho.blend` | 0–80 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_around_the_world.blend` | 0–160 | Play once | Man leads / Woman follows |
| `animations/man_and_woman/salsa_mambo_shine.blend` | 0–80 | 0–79 loop | Both independent |
| `animations/man_and_woman/salsa_side_shine.blend` | 0–80 | 0–79 loop | Both independent |
| `animations/man_and_woman/salsa_suzie_q.blend` | 0–80 | 0–79 loop | Both independent |
| `animations/man_and_woman/salsa_grapevine.blend` | 0–80 | 0–79 loop | Both independent |
| `animations/man_and_woman/salsa_crossover_breaks.blend` | 0–80 | 0–79 loop | Both independent |
| `animations/man_and_woman/salsa_diagonal_breaks.blend` | 0–80 | 0–79 loop | Both independent |
| `animations/man_and_woman/salsa_diamond_step.blend` | 0–80 | 0–79 loop | Both independent |
| `animations/man_and_woman/salsa_toe_taps.blend` | 0–80 | 0–79 loop | Both independent |
| `animations/man_and_woman/salsa_heel_digs.blend` | 0–80 | 0–79 loop | Both independent |
| `animations/man_and_woman/salsa_kick_ball_change.blend` | 0–80 | 0–79 loop | Both independent |
| `animations/man_and_woman/salsa_cuban_rocks.blend` | 0–80 | 0–79 loop | Both independent |
| `animations/man_and_woman/salsa_shoulder_shimmy.blend` | 0–80 | 0–79 loop | Both independent |
| `animations/man_and_woman/salsa_body_wave.blend` | 0–80 | 0–79 loop | Both independent |

## Verification

Before rebase:

- `python tests/run_tests.py --changed scripts/test_salsa_choreography.py`: 11/11 checks passed (ten fast checks and the four-case choreography test entry).
- Blender 5.2.2 `scripts/review_salsa_dance.py`: 35/35 saved clips passed over 3,235 frames. Measured checks cover planted ankles, palm gaps, body-center clearance, loop position/rotation, wrist bending/rotation steps, and foot displacement. Body-center clearance is a proxy rather than a full surface-collision test.
- Reopened the authored combined scene: all 35 salsa sources linked, both control-rig slots present, all 367 original tracks preserved, and `salsa_basic` selected.
- Representative still renders reviewed basic/closed holds, raised turns, and circular travel. Some cached renders precede the final contact interpolation fixes; use the validation report and asset manifest to identify the delivered sources.

After rebase, during delivery:

- `python tests/run_tests.py --changed scripts/test_salsa_choreography.py`: 11/11 passed in 6.18 seconds.
- `python scripts/lfs_policy.py check` from the repository root: passed across 23,226 staged files before this status record was added; rerun after staging the record.
- SHA-256 and Git blob comparison: all 35 sources and the preserved combined-scene checkpoint match the pre-rebase bytes exactly; all are complete binaries <= 100 MiB.
- Read-only motion review against the newer upstream shared scene: passed, 35/35 saved clips over 3,235 frames; process exit 0. Exact source hashes, units, sampled step, and tolerances are recorded in `salsa_delivery_validation.json` and `salsa_asset_manifest.json`.
- `git diff --check`: passed before staging the record; rerun before commit.

## Processes and saved outputs

At the stop instruction, no owned authoring/generation/rendering process was running. Git rebase was waiting for conflict resolution. The only subsequent Blender process was the bounded, read-only `review_salsa_dance.py` check (600-second limit through `TestRunner.execute`). Its completion result is recorded above; no process is left running at final delivery.

Local diagnostic outputs remain in `.cache/salsa/`: `authoring.json`, `validation.json`, `man_and_woman3_before_salsa.blend`, and workbench PNGs for basic, closed basic, follower right turn, and around-the-world poses at frames 0, 30, and 50. These are cached diagnostics, not standalone production exports. The durable checkpoint and reports are listed above. A compatible local executable remains at `.cache/tools/blender-5.2.2/blender`.

## Remaining work and blockers

- Authoring is paused by the user, rather than blocked by a missing source asset.
- The broad request for every salsa move remains a scope/design question; the exact delivered repertoire is the table above.
- Review posture, realistic partner connection, finger fit, mesh overlap, support and balance, and recognizability of every figure before treating these procedural studies as final production motion.
- Verify playback against any subsequent shared-rig changes; a dependency update can change evaluated results even when the source action's bytes match.
- Preserve the latest main scene, existing action fingerprints, preview selection, and concurrent libraries when a future authorized task explicitly installs/relinks salsa sources. The old combined checkpoint is a reference, rather than a replacement for the newer main scene.
- Generate and independently validate deform bakes or game exports only when that delivery is requested or authoring resumes.

## Exact resume commands

Inspection and validation, with authoring still paused:

```sh
cd /workspace/sanjo-solutions
python scripts/lfs_policy.py check
cd apps/a-game
python tests/run_tests.py --changed scripts/test_salsa_choreography.py
.cache/tools/blender-5.2.2/blender --background animations/man_and_woman/shared_scene_data.blend \
  --python-exit-code 1 --python scripts/review_salsa_dance.py
.cache/tools/blender-5.2.2/blender man_and_woman3_salsa_checkpoint.blend
```

A fresh environment needs a compatible Blender 5.2 executable in place of the cached path. Run automated Blender diagnostics with the suite runner's `TestRunner.execute(command, 600)` when process-tree cleanup is required. Preserve `scripts/salsa_dance_validation.json` as the historical authoring result; the review writes its new measurement to `.cache/salsa/validation.json`.

Only after an explicit instruction to resume animation authoring, use a separate source process, starting with a scoped clip:

```sh
cd /workspace/sanjo-solutions/apps/a-game
.cache/tools/blender-5.2.2/blender --background animations/man_and_woman/shared_scene_data.blend \
  --python-exit-code 1 --python scripts/create_salsa_dance.py -- --only basic
```

The generator overwrites selected source files; compare their hashes and revalidate their full motion before delivery. Review the installer's preview-selection behavior and fingerprint the current main scene before using its `--install` option on a future integration.

## Delivery

Integration baseline: `074c6a02e`, fetched immediately before the final merge. The merged shared-scene hash matches the delivery review, every preserved salsa asset matches the manifest, and the newer upstream main Blender scene is retained byte-for-byte. Storage verification passed for 24,146 staged files.

Task asset commit: `82c917344`. Animation guidance commit: `80bbe3ece`. This status record and the delivery verification are committed together afterward. Integration uses an ordinary merge with the latest `origin/main` and an ordinary push; any concurrent push rejection is resolved by fetching and merging the newer main. The final chat response records the status/merge commit IDs and verified remote result. GitHub-authored prose, if needed, is attributed to Codex; this task uses Git commits/pushes rather than posting GitHub comments.

The first ordinary push encountered a concurrent update. Remote `d6d474350` was fetched and merged through normal Git integration, preserving both sets of changes; animation authoring remained stopped.
