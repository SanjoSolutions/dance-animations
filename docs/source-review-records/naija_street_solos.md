# Naija street solos: preserved work status

- Date: October 2, 2026 (Europe/Berlin).
- Chat title: Create Naija dance animations.
- Chat ID: `01a0fd04-fd15-73a2-a91c-fcd74495a048`.
- Environment and checkout: sanjo-solutions cloud, `/workspace/sanjo-solutions/apps/a-game`.
- Task branch: `task/naija-street-solos`.
- Commit at stop: `fe09ef7b6a54f03909f7335d9673a27c15007d69` (durable task files awaited their first commit).
- Author of this record and GitHub commits: Codex.
- State: animation work stopped by explicit user instruction. Preserve these procedural studies for later review.

## Scope and delivery state

Original scope: create a broad organized Naija street-style move/position repertoire
for both characters in `man_and_woman3.blend`, reuse suitable existing motion,
follow per-animation authoring, validate interpolated motion and contacts, commit,
rebase, document Animation guidance, merge main and push. The user subsequently
instructed “don't bake,” then stopped all running animation work in favor of
recording and delivery.

48 editable sources are saved, with one native authoring action and one character
slot per file: 16 dance variations, four stance loops and four stance transitions
for each character. These are procedural blocking studies and stylized movement
interpretations, with representative clay pose review. They are a bounded catalog,
not an exhaustive or instructor-certified Naija dance syllabus. Detailed movement
polish and full continuous visual sign-off remain future work.

All clips span frames 0–96 at 24 fps, eight beats at 120 BPM. Forty clips loop;
eight transitions play once. Man files use `PLAYER` / `Man.rigify`; Woman files use
`PARTNER` / `Woman.rigify`. Moving controls have quarter-beat pose keys, stationary
channels have one initial key, and the sources retain native IK and metadata.

Authored: 48. Baked in the preserved sources: 0. Exported game clips delivered: 0.
An early prototype produced a baked/exported groove clip before the no-bake
instruction was handled; that prototype GLB, import file and update reference were
removed, and its source was regenerated as authoring-only. Current source loading
checks confirm exactly one authoring action per file. Existing shared Blender files,
existing baked libraries and game exports retain their original task-start contents.
The combined Blender library discovers the new source files through its existing
Player Asset Export workflow; this task leaves `man_and_woman3.blend` unchanged.

## Exact source inventory

Paths below are relative to `apps/a-game/animations/man_and_woman/`.
“Pass” means the saved-action numerical checks pass; artistic approval is separate.

| File | Category | Loop | Saved-motion result |
| --- | --- | --- | --- |
| `man_naija_groove_bounce.blend` | dance | yes | Pass |
| `man_naija_step_touch.blend` | dance | yes | Pass |
| `man_naija_shaku_shaku.blend` | dance | yes | Pass |
| `man_naija_shaku_side_step.blend` | dance | yes | Pass |
| `man_naija_shoki.blend` | dance | yes | Pass |
| `man_naija_skelewu.blend` | dance | yes | Pass |
| `man_naija_alanta.blend` | dance | yes | Pass |
| `man_naija_galala.blend` | dance | yes | Partial: angular seam |
| `man_naija_konto.blend` | dance | yes | Pass |
| `man_naija_etighi.blend` | dance | yes | Pass |
| `man_naija_alingo.blend` | dance | yes | Pass |
| `man_naija_shakiti_bobo.blend` | dance | yes | Pass |
| `man_naija_zanku_legwork.blend` | dance | yes | Pass |
| `man_naija_zanku_kick.blend` | dance | yes | Pass |
| `man_naija_gbe_body.blend` | dance | yes | Pass |
| `man_naija_heel_toe.blend` | dance | yes | Pass |
| `man_naija_ready.blend` | position | yes | Pass |
| `man_naija_low.blend` | position | yes | Pass |
| `man_naija_wide.blend` | position | yes | Pass |
| `man_naija_staggered.blend` | position | yes | Pass |
| `man_naija_ready_to_low.blend` | transition | once | Pass |
| `man_naija_low_to_ready.blend` | transition | once | Pass |
| `man_naija_ready_to_wide.blend` | transition | once | Pass |
| `man_naija_wide_to_ready.blend` | transition | once | Pass |
| `woman_naija_groove_bounce.blend` | dance | yes | Pass |
| `woman_naija_step_touch.blend` | dance | yes | Pass |
| `woman_naija_shaku_shaku.blend` | dance | yes | Pass |
| `woman_naija_shaku_side_step.blend` | dance | yes | Pass |
| `woman_naija_shoki.blend` | dance | yes | Pass |
| `woman_naija_skelewu.blend` | dance | yes | Partial: angular seam |
| `woman_naija_alanta.blend` | dance | yes | Pass |
| `woman_naija_galala.blend` | dance | yes | Partial: angular seam |
| `woman_naija_konto.blend` | dance | yes | Pass |
| `woman_naija_etighi.blend` | dance | yes | Pass |
| `woman_naija_alingo.blend` | dance | yes | Pass |
| `woman_naija_shakiti_bobo.blend` | dance | yes | Pass |
| `woman_naija_zanku_legwork.blend` | dance | yes | Pass |
| `woman_naija_zanku_kick.blend` | dance | yes | Pass |
| `woman_naija_gbe_body.blend` | dance | yes | Pass |
| `woman_naija_heel_toe.blend` | dance | yes | Pass |
| `woman_naija_ready.blend` | position | yes | Pass |
| `woman_naija_low.blend` | position | yes | Pass |
| `woman_naija_wide.blend` | position | yes | Pass |
| `woman_naija_staggered.blend` | position | yes | Pass |
| `woman_naija_ready_to_low.blend` | transition | once | Pass |
| `woman_naija_low_to_ready.blend` | transition | once | Pass |
| `woman_naija_ready_to_wide.blend` | transition | once | Pass |
| `woman_naija_wide_to_ready.blend` | transition | once | Pass |

## Supporting files

All paths below are relative to `apps/a-game/`.

- `scripts/naija_choreography.py`: catalog and procedural pose trajectories.
- `scripts/author_naija_street.py`: Blender 5.2 source-only authoring and sparse native keys; retains the existing shared-scene writer.
- `scripts/review_naija_street.py`: evaluated motion/contact/clearance and loop measurements.
- `scripts/test_naija_street.py`: reads the saved action files, checks solo bindings, samples poses and compares stance transition endpoints.
- `scripts/render_naija_street.py`: temporary evaluated-surface clay filmstrips, using Blender 5.2 rendering.
- `tests/test_suites.json`: focused Blender verification registration and source triggers.
- `animations/man_and_woman/naija_street.md`: exact repertoire, reuse, authoring and review commands.
- `animations/man_and_woman/naija_review.json`: final saved-source report, including the three failures.
- `animations/man_and_woman/naija_previews/man_front.png`: Shaku Shaku, Shoki and Alanta poses.
- `animations/man_and_woman/naija_previews/woman_front.png`: Shaku Shaku, Skelewu and Alanta poses.
- `animations/man_and_woman/naija_previews/man_side.png`: Zanku kick, Shakiti Bobo and ready-to-wide poses.
- `animations/man_and_woman/naija_previews/woman_side.png`: Zanku kick, Shakiti Bobo and ready-to-low poses.
- `animations/man_and_woman/.gitattributes`: exact-file plain-Git rules for the 48 sources and four previews.
- `docs/animation_work_status/naija_street_solos.md`: this stop record.
- `docs/animation_work_status/naija_street_solos_fast.txt`: final fast-suite output.
- `docs/animation_work_status/naija_street_solos_verification.txt`: final focused-suite output with failure diagnostics.

`DiscoCharacter`, `RigYogaPoser`, neutral-wrist calibration and character proportions
come from the existing disco authoring implementation. `step_touch` additionally
reuses its foot trajectory. The existing disco source remains unchanged.

## Verification and remaining failures

Blender used throughout authoring, sampling and rendering: 5.2.2 LTS, build
`d13f752e3b9c`. Godot used for final required fast checks: 4.7.2.

Final fast command (from `apps/a-game`):

```sh
GODOT=/workspace/.cloud-onboarding/bin/godot python tests/run_tests.py --suite fast
```

Result: **9/9 passed in 5.25 seconds**. An earlier initial fast run encountered
three hair LFS pointers; restoring those prerequisites and selecting Godot 4.7.2
resolved that setup issue.

Final focused verification, already running when the stop instruction arrived,
was allowed to finish because it reads motion and writes a diagnostic report:

```sh
GODOT=/workspace/.cloud-onboarding/bin/godot \
BLENDER=/workspace/.cloud-onboarding/bin/blender \
python tests/run_tests.py --changed scripts/naija_choreography.py \
  --changed scripts/author_naija_street.py --changed scripts/review_naija_street.py \
  --changed scripts/test_naija_street.py
```

Result: **9/10 checks passed in 181.88 seconds**. The saved-source check fails on
three angular seam measurements. It evaluated 9,360 poses: 195 samples per clip,
with half-frame interior coverage and 0.05-frame boundary intervals. All 48 clips
pass planted contacts, ankle-height, foot separation, torso/forearm clearance
proxies, knee and wrist bounds, loop position/orientation and linear-velocity
limits. All 16 stance transition endpoint checks pass. Forty-five clips pass the
complete numerical check.

The remaining angular-velocity differences exceed the 0.15 radians/second limit:

| Partial source | Measured angular-velocity difference |
| --- | --- |
| `man_naija_galala.blend` | 0.647425208968698 rad/s |
| `woman_naija_skelewu.blend` | 0.6556345552890467 rad/s |
| `woman_naija_galala.blend` | 0.5947979334583495 rad/s |

The final maximum planted ankle error is 0.00022242095 m. Maximum loop endpoint
position error is approximately 1.74e-17 m, orientation error is zero in the sampled
report, and maximum linear-velocity difference is 0.02230201 m/s. Fine-interval
quaternion numerical sensitivity versus genuine IK derivative behavior still
needs diagnosis for the three failures. Keep the failure gate active when resuming.
Earlier half-frame seam measurement flagged two Woman Shaku clips; finer sampling
resolved those flags and exposed the three current failures. No subsequent
animation refinement occurred after the stop instruction.

Front/side representative surface renders completed and were inspected. The
headless renderer emitted EGL fallback warnings and still saved all four PNGs.
Clearance metrics are local proxies, not a complete mesh-intersection proof.
Continuous visual playback and stylistic review of every clip remain outstanding.

## Processes, storage and blockers

All owned authoring and rendering jobs finished before the stop directive. The
last owned Blender verification process (PID 2619) subsequently finished with
exit 1 and the failures above. The final fast-suite process finished with exit 0.
There are no remaining owned animation processes.

Scratch logs and render originals remain in `/workspace/scratch/naija/`; durable
outputs are copied to the paths above. The credential helper in that scratch
directory references the configured token at runtime and contains no token value;
it is local tooling, not a task asset.

The 48 source binaries measure 101,429–119,199 bytes (5,374,964 bytes together).
The four PNGs measure 2,702,616–2,927,012 bytes. All 52 new binaries are below
104,857,600 bytes. Actual sizes, staged blob sizes and cached Git attributes were
checked: plain Git for these exact files; existing assets retain their LFS rules.
The task creates no new LFS objects, so Git publication uploads all new assets.

At authoring time Game Rig Tools was absent; Player Asset Export was installed
from the checkout. The user's no-bake instruction governs delivery regardless of
future add-on availability. Technical blockers are the three seam failures and
remaining full visual/style review. The stop instruction is the blocker for any
further authoring or rendering in this chat.

## Exact resumption commands

Resume only after a new instruction authorizes animation work. First inspect this
record and the report, and run the verification command above. For interactive
inspection of a partial source:

```sh
cd /workspace/sanjo-solutions/apps/a-game
/workspace/.cloud-onboarding/bin/blender animations/man_and_woman/man_naija_galala.blend
```

To regenerate one procedural source after an authorized code adjustment:

```sh
/workspace/.cloud-onboarding/bin/blender --background \
  animations/man_and_woman/solo_disco_dance.blend --python-exit-code 1 \
  --python scripts/author_naija_street.py -- --character Man --only galala
```

The command replaces that generated source; copy manual edits to a distinct source
before regeneration. Use `--character Woman --only galala` and `--character Woman
--only skelewu` for the other partial clips. Re-run the saved-source verification,
review changed motion visually, and inspect binary sizes/attributes before staging.
Baking and game exports require a later explicit instruction.

Integration is recorded by this file's commits and the final chat delivery: commit
durable task work, fetch/rebase onto current `origin/main`, commit the requested
Animation guidance separately, integrate concurrent main changes with ordinary
history-preserving pushes, and verify remote main contains the task commits.

## Integration checkpoint

The preserved-work commit rebased onto `origin/main` at
`18e528c73` as `ca2d3d5d0991bb8065a2b734be9a1914f9a97930`.
The original unpublished commit was `85fba3ff0`; the rebase preserved both chats'
Git attributes and test registrations. The requested Animation guidance is added
in the following documentation commit. Git LFS policy verification passed for
23,418 staged files after integration (`python scripts/lfs_policy.py check`).

Concurrent main converted shared dependencies from LFS pointers to regular Git.
Their actual binary contents match those used for the recorded motion checks:

| Dependency | SHA-256 |
| --- | --- |
| `shared_scene_data.blend` | `18a0f6bb84cc90426444e4bf4c81d78e3b81ebd84097a7c16afc098cd9948130` |
| `man_anatomical_study.blend` | `6144ac70e971bff82f432f0930eb0fe8e5c18e16ba99f8193aa8738af6b67c55` |
| `woman_anatomical_study_speculum.blend` | `d9b123f681bd8c343ed861ec8d9c8b512bede54ae0b93c8cefb33acfafda96e9` |

Main also supplies the Game Rig Tools installer now documented in AGENTS.md.
That concurrent addition is preserved; this task performed no further animation
work and continues to deliver zero baked actions or exported game clips.

Post-rebase fast verification passed **10/10 checks in 8.20 seconds**. Concurrent
main added a fast check. The full output is
`docs/animation_work_status/naija_street_solos_integrated_fast.txt`.
