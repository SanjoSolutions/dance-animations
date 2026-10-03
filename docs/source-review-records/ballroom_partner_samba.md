# Ballroom partner samba — paused work status

Recorded: 2026-10-02, stopping inspection at 15:00:32 UTC (17:00:32 Europe/Berlin).
Chat title (descriptive): Ballroom partner samba for man_and_woman3.blend.
Project: A-Game, sanjo-solutions cloud environment.
Task branch: `codex/ballroom-partner-samba`.
Commit at stop: `3c52737c74b488501e9cfe47e7029547c6f5fe88`.
This record accompanies the first task checkpoint commit; the stop commit above
is the starting repository state, rather than a commit containing these assets.

## Instruction and scope

The user explicitly stopped animation authoring, refinement, generation, and
rendering across active animation chats. This task now preserves its saved state,
records evidence, verifies repository checks, and delivers its commits through
main. Resuming animation work requires a subsequent user instruction.

Original scope: a broad organized repertoire of coordinated ballroom partner
samba figures and positions for both characters in `man_and_woman3.blend`, using
Blender 5.2, existing per-animation tooling, suitable reusable motion, planted
contacts, clearance, smooth transitions, and interpolated/loop validation; then
commit, rebase onto current main, document lessons, merge, push, and upload assets.

## Exact saved state

**62 authored procedural blocking studies; zero baked actions delivered; zero
Godot exports.** These are partial animation assets requiring further quality
work, rather than completed or certified ballroom technique. Both participants
are intended in every source: `Man.rigify` is player/leader and `Woman.rigify` is
partner/follower. A paired action uses synchronized slots and NLA bindings.
Shared scenes, character models, and the combined library remain unchanged.

The saved set contains 40 figure studies, eight position studies, and 14 directed
transitions. Authoring uses 24 fps and a practice tempo of 96 BPM. Figure and
transition action plans span 0–150; position plans span 0–120. Loop playback is
intended to end before the duplicated closing sample (149 or 119). Traveling
figures and directed transitions play once through 150. Final saved NLA playback
ranges still need a complete audit: some files were written before the latest
range fix and the whole-library polish pass was never completed.

Implemented reusable authoring components: the existing yoga rig poser, disco
wrist alignment, paired calibrated-palm solver, activity action sampler, and
`AnimationFileWriter`. Samba-specific code adds world-space ankle landing
anchors, transfer arcs, complementary partner foot patterns, formation changes,
and sparse keyed controls. These procedural interpretations need dance-quality
review; a named figure alone establishes neither full syllabus fidelity nor
physical balance.

Four disjoint generation partitions finished after two failed subsets were
corrected and resumed. An intermediate contact/tangent refinement processed 41
catalog entries. The latest natural/reverse roll rebuild finished successfully,
saved both files, and ran its two-source refinement with zero extra contact
samples. The current generator includes fixes introduced during the batches;
all 62 binaries have **not** been regenerated from that final script version.

No Blender, authoring, validation, or rendering process remained running at the
stop inspection. Existing process outputs were already saved. After the stop,
work was limited to preservation documentation, copying evidence, Python syntax
checks, repository tests, storage inspection, and Git delivery.

## Relevant files and preserved evidence

All paths below are relative to `apps/a-game`.

| File or group | State and purpose |
| --- | --- |
| `scripts/create_ballroom_samba.py` | Paused procedural generator and targeted saved-contact refinement; running it changes assets. |
| `scripts/validate_ballroom_samba.py` | Saved-action validation and optional renderer; final revision has yet to run across the library. |
| `scripts/ballroom_samba.md` | Repertoire, timing, workflow, and explicit checkpoint caveats. |
| `animations/man_and_woman/ballroom_samba_catalog.json` | Partial main catalog: 42 entries. Preserved as saved. |
| `animations/man_and_woman/ballroom_samba_validation.json` | Historical three-clip report, `passed: false`; predates latest roll changes and validator revision. |
| `animations/man_and_woman/.gitattributes` | Exact exceptions for the 62 task sources; existing asset rules preserved. |
| `docs/animation_work_status/ballroom_partner_samba/asset_inventory.json` | Complete 62-file inventory, actual sizes/SHA-256, planned timing/roles, catalog coverage, and report-hash comparisons. |
| `docs/animation_work_status/ballroom_partner_samba/catalog_0.json` through `catalog_3.json` | Preserved partition catalogs with 16, 16, 15, 15 entries; together cover 62 names. Earlier metadata snapshots, rather than final verification. |
| `docs/animation_work_status/ballroom_partner_samba/storage_audit.txt` | Actual Git attributes for 62 Blender sources and ten review PNGs before staging. |
| `docs/animation_work_status/ballroom_partner_samba/review/` | Ten existing review stills, frames 0/30/60/90/120 for natural basic and promenade walks; no further rendering after stop. Exact PNG ordinary-Git exceptions live beside them. |
| `docs/animation_work_status/ballroom_partner_samba/check_composition.py` | Preserved read-only source-composition assertions. |
| `docs/animation_work_status/ballroom_partner_samba/*.log` | Generation failures/resumptions, last roll save, refinement, diagnostic probes, saved validation, and test evidence. |

Evidence logs include `build_part_0.log` through `build_part_3.log`,
`resume_part_0.log`, `resume_part_2.log`, `refine_first.log`, `roll_rebuild2.log`,
`probe_roll.log`, `wrist_axes.log`, `polished_check.log`, `composition.log`,
`fast.log`, `fast_retry.log`, `workflow_tests.log`, `preservation_fast.log`, and
`preservation_workflow.log`. Earlier exploratory scripts and older renders remain
in `/workspace/scratch/samba`; the repository checkpoint preserves the relevant
latest images, completed catalogs, and diagnostic results. The scratch askpass
helper is credential infrastructure and is intentionally outside Git.

## Verification and known failures

All Blender work used `/workspace/.cloud-onboarding/3d-tools/blender-5.2.2/blender`,
verified as **Blender 5.2.2 LTS**, build `d13f752e3b9c`, 2026-09-15.

| Command/check | Result |
| --- | --- |
| `python tests/run_tests.py --suite fast` at preservation | 10/10 passed, 6.17 seconds; `preservation_fast.log`. |
| `BLENDER=/workspace/.cloud-onboarding/3d-tools/blender-5.2.2/blender python tests/run_tests.py --suite changed --changed scripts/player_assets/test_animation_files.py` | 11/11 passed, 8.35 seconds; `preservation_workflow.log`. Includes fast checks. |
| `python -m py_compile scripts/create_ballroom_samba.py scripts/validate_ballroom_samba.py` | Passed after stopping animation work. |
| `git diff --check` | Passed at preservation. |
| Natural-basic source composition with startup script and `check_composition.py` | Passed before stop: runtime scene and both matching action-slot bindings; `composition.log`. |
| Latest saved-motion check, selected natural basic/promenade walks/reverse roll | Failed overall: two of three clips have recorded failures; see below. |
| Storage/hash inspection | 62 Blender files total 11,158,739 bytes; all 72 task binaries including PNGs at most 204,474 bytes; actual binaries, exact ordinary-Git attributes. |

The original fast test attempt failed because hair mesh LFS fixtures were
pointers and a process-cleanup test also failed. Fetching actual fixtures and
rerunning produced 10/10, followed by the fresh passing preservation runs above.
There is no remaining test-environment blocker.

The saved validation report checked actual keyframes, intermediate poses, and
fractional samples for three clips. Its limits include IK 5 mm, planted position
6 mm, planted rotation 0.03 rad, palm gap 12 mm, floor -8 mm, capsule clearance
zero, loop-pose 0.0001, and boundary velocity 0.003 world units/frame.

* Natural basic: 121 samples, 0.231 mm IK/plant error, 1.638 mm palm gap,
  1.834 mm minimum skin height, 59.269 mm capsule clearance, exact loop pose.
  Boundary velocity measured 0.0048068, exceeding 0.003. The source hash still
  matches. The validator was subsequently changed from a 0.25-frame velocity
  sample interval to 0.01; this change has **not** established a passing result.
* Promenade samba walks: 127 samples, 0.233 mm IK error, 7.992 mm palm gap,
  3.637 mm minimum skin height, 365.254 mm capsule clearance; no recorded
  failures. The report hash still matches. This is a traveling once-only clip.
* Reverse roll: 121 samples and -75.330 mm capsule clearance, failing the coarse
  body test. Its report hash differs from the current source: both roll variants
  were rebuilt afterward. Authoring-session probes showed improved clearance,
  but the latest saved revisions have **not** passed reloaded validation.

The report covers three of 62 files. Transition-seam coverage is empty. The
validator can skip seams whose position records are missing from its catalog;
complete catalog coverage must precede a meaningful whole-library verdict.
The final wrist diagnostic measured local tweak rotations, but it establishes
neither ergonomic approval nor natural playback. Only limited rendered stills
were inspected; whole-library playback, skin-level collision, balance, finger
comfort, and dance authenticity remain pending. Capsule checks are coarse.

## Remaining work and concrete blockers

The active blocker is the user's stop instruction. Preserve this checkpoint
until animation work is resumed. Technical work remaining then:

1. Reconcile the 42-entry main catalog with all four partition catalogs and audit
   actual saved action/NLA timing and metadata against the inventory.
2. Resolve the known loop-velocity finding, validate the latest roll saves, and
   inspect every interpolated contact/clearance failure across all 62 sources.
3. Audit the generator's final changes against older saved files; perform any
   needed refinements only after resumption, preserving the checkpoint first.
4. Review actual playback for every figure, position, and transition, especially
   wrists, partner holds, feet/support, clearance, and authentic samba timing.
5. Validate every position-to-transition seam, loop boundary, and traveling
   clip's spatial connection. Distinguish derivative continuity from a finite
   quarter-frame displacement estimate.
6. Bake/export only if the resumed task requests runtime outputs. Current saved
   sources belong to the authored procedural-study stage.

## Exact resume commands

The following commands are **future resumption instructions**, not actions
performed after the stop. Run only after a new instruction resumes the work.
The source inventory and report hashes provide the checkpoint reference.

```sh
cd /workspace/sanjo-solutions/apps/a-game
export BLENDER=/workspace/.cloud-onboarding/3d-tools/blender-5.2.2/blender
"$BLENDER" --version
python tests/run_tests.py --suite fast

# Read-only composition check of the preserved natural-basic source.
"$BLENDER" --background animations/man_and_woman/ballroom_samba_natural_basic.blend   --threads 1 --disable-autoexec --python-exit-code 1   --python scripts/player_assets/animation_file_startup.py   --python docs/animation_work_status/ballroom_partner_samba/check_composition.py

# Audit the existing known failures first; this rewrites the report, not the sources.
"$BLENDER" --background animations/man_and_woman/shared_scene_data.blend   --threads 4 --disable-autoexec --python-exit-code 1   --python scripts/validate_ballroom_samba.py --   --only natural_basic natural_roll reverse_roll samba_walks_promenade
```

To reconcile the inventory into a complete planned catalog after checking the
saved sources, use this exact merge (main entries take precedence over the older
partition snapshots). It updates metadata, rather than validating motion:

```sh
python - <<'PYCODE'
import json
from pathlib import Path
root = Path('docs/animation_work_status/ballroom_partner_samba')
target = Path('animations/man_and_woman/ballroom_samba_catalog.json')
data = json.loads(target.read_text())
records = {}
for index in range(4):
    for clip in json.loads((root / f'catalog_{index}.json').read_text())['clips']:
        records[clip['name']] = clip
for clip in data['clips']:
    records[clip['name']] = clip
assert len(records) == 62
data['clips'] = [records[name] for name in sorted(records)]
target.write_text(json.dumps(data, indent=2) + '\n')
PYCODE

# These next commands modify authored assets and render new images.
"$BLENDER" --background animations/man_and_woman/shared_scene_data.blend   --threads 4 --disable-autoexec --python-exit-code 1   --python scripts/create_ballroom_samba.py -- --polish
"$BLENDER" --background animations/man_and_woman/shared_scene_data.blend   --threads 4 --disable-autoexec --python-exit-code 1   --python scripts/validate_ballroom_samba.py -- --render /workspace/scratch/samba/resumed_review
```

A full generator rebuild uses the same authoring command with `--polish` omitted;
this replaces the source studies and should follow source review. Shared scene
and linked character/prop LFS objects were retrieved in this environment. A fresh
checkout needs those actual objects before Blender source composition.

## Delivery and storage

The task adds ordinary Git binaries only. The 62 sources and ten preserved PNGs
are individually below 104,857,600 bytes and have exact-filename attributes;
shared assets retain their LFS settings. There are zero new task LFS objects to
upload. The status and inventory preserve existing motion failures explicitly;
passing repository checks support checkpoint delivery, not animation approval.
Final task/documentation/integration hashes and remote-main verification are
reported in the chat after ordinary Git delivery, avoiding a self-referential
commit hash in this file.

## Integration verification

The checkpoint was rebased onto fetched `origin/main` at
`074c6a02e` and became task commit
`99276b4804d637a6a762c442dae5daeba510a7ba`. The sole conflict was the appended
animation `.gitattributes` sections; both main's existing rules and all samba
rules were retained. Current main independently migrated smaller shared assets
to ordinary Git. This task preserves those concurrent storage changes; the
LFS descriptions earlier in this record describe the stopping environment.

After rebase, the workflow runner command above passed 11/11 checks in 8.31
seconds, including all ten fast checks (`ballroom_partner_samba/post_rebase_checks.log`).
From the repository root, `python scripts/lfs_policy.py check` passed for 24,204
indexed files. The separate documentation update adds checkpoint/catalog guidance
and explains exact action-datablock identity when reloading names in one process.

The final main integration started from freshly fetched
`30ca3422515f79850880c506e96c2f8bf72b07cd`. Both appended documentation and
storage-rule conflicts were resolved by retaining every existing main entry and
the samba additions. The workflow suite passed again: 11/11 in 8.06 seconds
(`ballroom_partner_samba/integration_checks.log`), and the storage policy passed
for 26,450 indexed files before adding this final evidence log. No further
Blender authoring or rendering ran during integration.

The first ordinary push was rejected because another task advanced main. A
follow-up merge integrates `e971ed83b`, preserving both sides of the appended
storage rules. The updated animation-file test and all fast tests passed again:
11/11 in 8.05 seconds (`ballroom_partner_samba/push_retry_checks.log`). The
repository storage check passed for 27,939 indexed files before adding that log.

## Per-source inventory

Every row is a saved authored procedural study with both roles; baked/exported
state is false for every row. Timing is the plan recorded by the generator;
actual NLA playback endpoints remain subject to the audit above. The linked
JSON inventory supplies exact bytes, hashes, catalog presence, and validation
hash matches for every source. Paths use the common prefix
`animations/man_and_woman/`.

| Source file | Group | Planned action frames | Planned playback | Loop |
| --- | --- | --- | --- | --- |
| `ballroom_samba_argentine_crosses.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_back_rocks.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_bota_fogos_promenade_counter.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_bota_fogos_shadow.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_circular_voltas.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_closed_rocks.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_closed_to_counter_promenade.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_closed_to_left_side.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_closed_to_open.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_closed_to_promenade.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_closed_to_right_side.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_closed_to_shadow.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_closed_to_side_by_side.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_contra_bota_fogos.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_corta_jaca.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_counter_promenade_to_closed.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_criss_cross_bota_fogos.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_criss_cross_voltas.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_cruzados_locks.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_cruzados_walks.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_left_side_to_closed.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_maypole.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_natural_basic.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_natural_roll.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_open_rocks.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_open_to_closed.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_plait.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_position_closed.blend` | position | 0–120 | 0–119 | True |
| `ballroom_samba_position_counter_promenade.blend` | position | 0–120 | 0–119 | True |
| `ballroom_samba_position_left_side.blend` | position | 0–120 | 0–119 | True |
| `ballroom_samba_position_open.blend` | position | 0–120 | 0–119 | True |
| `ballroom_samba_position_promenade.blend` | position | 0–120 | 0–119 | True |
| `ballroom_samba_position_right_side.blend` | position | 0–120 | 0–119 | True |
| `ballroom_samba_position_shadow.blend` | position | 0–120 | 0–119 | True |
| `ballroom_samba_position_side_by_side.blend` | position | 0–120 | 0–119 | True |
| `ballroom_samba_progressive_basic.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_promenade_counter_runs.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_promenade_to_closed.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_reverse_basic.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_reverse_roll.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_reverse_turn.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_right_side_to_closed.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_rolling_off_arm.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_roundabout.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_samba_locks.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_samba_walks_promenade.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_shadow_circular_voltas.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_shadow_to_closed.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_side_basic.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_side_by_side_to_closed.blend` | transition | 0–150 | 0–150 | False |
| `ballroom_samba_side_samba_walk.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_solo_spot_volta_left.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_solo_spot_volta_right.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_stationary_samba_walks.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_three_step_turn.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_travelling_bota_fogos_backward.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_travelling_bota_fogos_forward.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_travelling_voltas_left.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_travelling_voltas_right.blend` | figure | 0–150 | 0–150 | False |
| `ballroom_samba_underarm_turn_left.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_underarm_turn_right.blend` | figure | 0–150 | 0–149 | True |
| `ballroom_samba_whisks_left_right.blend` | figure | 0–150 | 0–149 | True |
