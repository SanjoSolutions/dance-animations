# Slow dance preservation status

- Recorded: 2026-10-02 UTC. Animation authoring stopped at the user's stop-and-preserve instruction; subsequent work is preservation, verification, storage conversion, and integration only.
- Chat: **Animate slow dancing moves** (`01a0fc9a-7452-7068-a60f-61bed5151070`).
- Original branch: `work`; stop-time commit: `ea7ca0cbd4878d4c781aa1278574f895ddddb5f8` (parent `7f024cbcf`). Local backup branch: `slow-dance-pre-storage-backup`.
- Delivery branch: `slow-dance-preservation`, isolated checkout `/workspace/slow-dance-delivery`. Rebuild the unpublished task commit on current main to comply with the updated 100 MiB storage policy; the old LFS-based commit remains a local backup, rather than outgoing history.
- Original scope: “Create animations for man_and_woman3.blend for Slow dancing, including animations for all dance moves and positions in Slow dancing.”

## Saved work and its limits

32 paired social slow-dance moves/positions and a 210-second routine were procedurally authored and refined before the stop instruction. This is the named core social repertoire below; slow dancing has an open-ended vocabulary, so this is not an exhaustive universal syllabus. Each clip has editable paired Rigify source slots and a matching native deform bake. These are procedural choreography assets with sampled landmark review and representative mesh previews; comprehensive surface-collision review and final visual polish remain unfinished.

- **Authored:** 33 actions, including the routine, in 33 individual `animations/man_and_woman/slow_dance_*.blend` source files.
- **Baked:** 33 paired `.baked` actions, evaluated into the native deform rigs at integer frames. This is a native bake, with measured approximation tolerances below, rather than a claim of exact Game Rig Tools retargeting.
- **Exported:** no new GLB/Godot runtime exports. Runtime import and gameplay integration remain unfinished.
- Roles: `Man.rigify` = player/lead; `Woman.rigify` = partner/follow. Baked slots use `Man.rigify_deform` and `Woman.rigify_deform`. Synchronize both participants and their origins.
- Timing: 24 fps, 80 BPM, 18 frames/beat. The routine is `slow_dance_routine`, frames **0–5040**, once, with 32 chapter markers. Loops store a matching final endpoint and play through `end - 1`.
- The stop-time combined `man_and_woman3.blend` held 507 total actions, including all 66 slow-dance source/baked actions. Its preview selected the routine at frame 216. Integration must retain newer main's existing actions and preview state.

## Exact clip inventory

Every row corresponds to `animations/man_and_woman/slow_dance_<suffix>.blend` and contains both the source action and its `.baked` counterpart.

| Action suffix | Movement or position | Frames | Playback |
| --- | --- | --- | --- |
| `closed_hold` | Relaxed closed ballroom hold and breathing | 0–144 | Loop |
| `close_embrace` | Close embrace with hands at shoulders and upper back | 0–144 | Loop |
| `open_hold` | Open single-hand hold | 0–144 | Loop |
| `two_hand_hold` | Open two-hand hold | 0–144 | Loop |
| `promenade_hold` | Side-by-side promenade hold | 0–144 | Loop |
| `wrapped_hold` | Wrapped sweetheart hold | 0–144 | Loop |
| `sway` | Side-to-side weight transfer in closed hold | 0–144 | Loop |
| `step_touch` | Alternating side steps and collected foot touches | 0–144 | Loop |
| `forward_back_rock` | Forward and backward rock steps | 0–144 | Loop |
| `box_step` | Six-step social box basic | 0–216 | Loop |
| `quarter_turn_left` | Progressive left quarter-turn and recovery | 0–144 | Loop |
| `quarter_turn_right` | Progressive right quarter-turn and recovery | 0–144 | Loop |
| `travel_left` | Travel left with a side-close-side and return | 0–144 | Loop |
| `travel_right` | Travel right with a side-close-side and return | 0–144 | Loop |
| `underarm_turn_left` | Left underarm turn, release, and reconnection | 0–216 | Loop |
| `underarm_turn_right` | Right underarm turn, release, and reconnection | 0–216 | Loop |
| `open_break` | Step apart into an open hold and return | 0–144 | Loop |
| `promenade` | Open to promenade, walk together, and close | 0–216 | Loop |
| `wrap_unwrap` | Wrap to sweetheart position and unwind | 0–288 | Loop |
| `gentle_dip` | Supported shallow dip and balanced recovery | 0–144 | Loop |
| `enter` | Offer hands and settle into closed hold | 0–144 | Once |
| `release` | Release the hold and step apart | 0–144 | Once |
| `closed_to_close` | Transition from closed hold to close embrace | 0–144 | Once |
| `close_to_closed` | Transition from close embrace to closed hold | 0–144 | Once |
| `closed_to_open` | Transition from closed to open hold | 0–144 | Once |
| `open_to_closed` | Transition from open to closed hold | 0–144 | Once |
| `closed_to_promenade` | Open to side-by-side promenade | 0–144 | Once |
| `promenade_to_closed` | Return from promenade to closed hold | 0–144 | Once |
| `closed_to_wrapped` | Turn into a sweetheart hold | 0–144 | Once |
| `wrapped_to_closed` | Unwind into closed hold | 0–144 | Once |
| `closed_to_two_hand` | Transition from closed to two-hand hold | 0–144 | Once |
| `two_hand_to_closed` | Transition from two-hand to closed hold | 0–144 | Once |


## Supporting files

Paths below are relative to `apps/a-game/`.

| Path | Preserved purpose/state |
| --- | --- |
| `man_and_woman3.blend` | Combined chooser library; integrate links to existing saved clips while preserving concurrent families. |
| `scripts/create_slow_dance.py` | Procedural source recipe, 32 named clips, calibrated IK targets, feet, holds, contact poses. |
| `scripts/refine_slow_dance.py` | Existing interpolation corrections and explicit fractional-frame key insertion. |
| `scripts/slow_dance_library.py` | Routine assembly, native deform baking, compatibility normalization, individual-file publication. Running it is further authoring/publication and requires a resumed task. |
| `scripts/review_slow_dance.py` | Read-only sampled source and bake review. |
| `scripts/slow_dance.md` | Repertoire, timing, edit/publish instructions, validation limits. |
| `scripts/slow_dance_review.json` | Source landmark results for all 32 clips, 4,576 samples. |
| `scripts/slow_dance_bake_review.json` | Native source/deform comparison for 33 clips including routine. |
| `docs/animation_work_status/slow_dance_man_and_woman3/authoring_checkpoint.blend` | Durable storage-compacted version of `/tmp/slow_dance_tools/verified_library.blend`, with relative dependency paths and every action curve fingerprint preserved. All 33 local sources and links to 33 identical final native bakes in the published clip files; pre-publication compatibility normalization. Individual published clips are authoritative: they additionally contain explicit `pole_parent=1` channels and normalized finger-master Euler channels. |
| `docs/animation_work_status/slow_dance_man_and_woman3/asset_manifest.json` | Delivery asset byte sizes and SHA-256 hashes, captured during preservation. |
| `docs/animation_work_status/slow_dance_man_and_woman3/.gdignore` | Excludes the checkpoint/review directory from Godot imports. |

## Verification before and at stop

- `python tests/run_tests.py --suite fast`: **10/10 passed**, 6.40 s before stop; **10/10 passed**, 6.47 s after stop (`/tmp/slow_dance_tools/stop_fast.log`). An earlier concurrent heavy-Blender run had a transient process-cleanup test failure; sequential quiet reruns passed.
- `python -m py_compile scripts/create_slow_dance.py scripts/refine_slow_dance.py scripts/slow_dance_library.py scripts/review_slow_dance.py`: passed. `git diff --check`: passed.
- Source review: all 32 clips / 4,576 samples passed. Maximum shared palm separation 0.018677385 m, contact-target error 0.013904598 m, planted ankle drift 0.002222910 m, wrist bend 29.08235 degrees; loop position/rotation endpoints matched. Tolerances: 30 mm hand separation, 20 mm contact, 5 mm foot drift, 45 degrees wrist bend, 3 mm / 0.5 degrees loop endpoints, torso spacing above 0.28 m. Torso spacing is a landmark proxy, not a surface collision test.
- Source review was assembled from unchanged clips plus a corrected wrapped-hold review. The historical reports predate the current requirement for saved-source hashes and did not record hashes when carrying results forward. The preservation manifest identifies delivered assets; it does not retroactively prove report-to-source checksums.
- Native bake review: all 33 passed at one-beat intervals with deform constraints muted. Maximum bone-head error **0.007240484 m**, maximum rotation error **1.6081119 degrees** (Woman palm, routine frame 4734). Tolerances **8 mm / 2 degrees**, reflecting connected rest-bone offsets and constraint shear represented by location/rotation/scale channels. An earlier 0.5-degree target failed and was investigated; the actual approximation remains explicit.
- Fresh-open combined-scene check passed: 66 slow-dance actions, two participant slots each, 32 markers, chooser bindings for four rigs, 5 representative source clips with passing landmark review. Command: `python /tmp/slow_dance_tools/run_final_check.py`; output `/tmp/slow_dance_tools/final_check.log`.
- Broader suite attempted: `python tests/run_tests.py --suite changed --changed man_and_woman3.blend --blender /tmp/slow_dance_tools/blender-5.2.1-linux-x64/blender`. 25 related checks selected; **incomplete**, with missing Game Rig Tools/add-ons and memory pressure in the authoring environment. Runner stopped safely; `/tmp/slow_dance_tools/related_tests.log`. Newer main subsequently bundled Game Rig Tools; its availability does not turn the historical failed/incomplete suite into a pass.
- Representative mesh previews inspected before stop: closed hold, wrapped hold, promenade hold, and underarm mid-turn. Elbow/chest intersections identified there were corrected. Full all-frame surface, wrist/finger, and transition playback review remains outstanding.

## Processes, checkpoints, and stopping point

No owned animation authoring, baking, export, or render process was active when the stop request arrived. All finished outputs were retained. Preservation-only Blender saves remap the checkpoint's relative library paths and compress existing data; read-only fingerprint checks verify that compression preserves existing action curves. No new choreography or render is produced during delivery.

The original checkout `/workspace/sanjo-solutions` and `/tmp/slow_dance_tools` remain available locally. The latter contains superseded procedural blocking/pose/refinement studies and partial bakes. These scratch studies are not deliverable final clips:

- `bake_sample.blend`, `baked_partial.blend`, `baked_unchanged.blend`, `comfortable.blend`, `compact.blend`, `complete.blend`, `contact_corrected.blend`, `conversion_pilot.blend`, `final_baked.blend`, `final_working.blend`, `fully_baked.blend`, `holds_corrected.blend`, `neutral.blend`, `pose.blend`, `ready_to_publish.blend`, `refined_compact.blend`, `refined_complete.blend`, `refined_sample.blend`, `refined_sample2.blend`, `refined_sample3.blend`, `root_turn.blend`, `slow_dance.blend`, `stable.blend`.
- `rebaked_clips.blend`: all sources and 32 individual bakes, routine bake absent.
- `rebaked_routine.blend`: all sources and routine bake, individual bakes absent.
- `verified_library.blend`: combined final pre-publication checkpoint, preserved durably as `authoring_checkpoint.blend` above.
- Generated `.blend1` backups remain local/ignored. They are superseded snapshots. Scratch files/logs under `/tmp` are environment-local; the authored library, latest checkpoint, source recipes, reports, and delivery manifest are the durable record.

Stopping point: authored source and native baked library saved; final visual/collision review and game exports unfinished. The user's stop instruction is the current boundary for further animation work.

## Resume commands (after the user resumes animation work)

```sh
cd /workspace/slow-dance-delivery/apps/a-game
export BLENDER=/tmp/slow_dance_tools/blender-5.2.1-linux-x64/blender
export BLENDER_USER_CONFIG="$PWD/.cache/blender/config"
export BLENDER_USER_SCRIPTS="$PWD/.cache/blender/scripts"
export BLENDER_USER_EXTENSIONS="$PWD/.cache/blender/extensions"
"$BLENDER" --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
python tests/run_tests.py --suite fast
"$BLENDER" man_and_woman3.blend
```

Choose `slow_dance_*` through **Helpers > Animation > Select animation**, then open the individual source to continue visual review/editing. Existing sources are already authored and baked; avoid rerunning generation for preservation. If reconstructing the library from the pre-publication checkpoint is specifically needed, first back up the current combined library and then run:

```sh
"$BLENDER" -b docs/animation_work_status/slow_dance_man_and_woman3/authoring_checkpoint.blend \
  --python-exit-code 1 --python scripts/slow_dance_library.py -- \
  --output man_and_woman3.blend --directory animations/man_and_woman \
  --source man_and_woman3.blend
```

That command normalizes the pre-publication channels and republishes existing actions; inspect newer concurrent scene changes before using it. For runtime delivery, continue the repository's `docs/player-animation-workflow.md` using **Bake & Export Active Animation**, then validate saved GLB imports and gameplay. Broader related checks use the bounded suite runner command above, sequentially, after obtaining required imports/add-ons.

## Delivery verification

Integration, storage verification, final fast-suite results, and remote delivery are recorded below as completed. Git commit identities are available from the history of this status file; the obsolete local LFS commit is retained only as a backup.

### Completed preservation checks

- Integrated against `8648f10ee`: all **527 preexisting action curve fingerprints preserved**; combined library now **593 actions**, including **66 slow-dance actions**. All linked libraries resolve. The newer main preview remains `massage_hand`, frame 35, range 0–48. `integration_report.json` records before/after fingerprints and preview values; the independent fresh-open verification passed.
- The routine's existing Blender data was losslessly recompressed with Zstandard level 19. Its decoded file SHA-256 is unchanged (`routine_storage_report.json`); the file is **101,919,294 bytes**, below 100 MiB. This changes storage only.
- The initial checkpoint storage upload returned Git LFS **HTTP 501 / Not Implemented**. Resolved for delivery by removing duplicate bake storage: the checkpoint retains 33 local source actions and links to the same 33 baked actions already saved in the clip files. **All 66 action fingerprints match the original checkpoint**; `checkpoint_compaction_report.json` records this. The resulting checkpoint is **47,480,578 bytes**, below 100 MiB. The original full local-bake checkpoint remains in the original checkout and `/tmp/slow_dance_tools/verified_library.blend`.
- Every delivered task asset now fits the repository's regular-Git size rule, so the rebuilt outgoing task commits require **zero LFS payload uploads**. Superseded local LFS commits remain on `slow-dance-pre-storage-backup`; they are outside outgoing history. No published history is rewritten.
- First delivery-checkout fast run: 8/10 because ignored Godot caches/import descriptors/UID files were absent. Restored these local prerequisites from the original checkout. A subsequent busy run reached 9/10, with the existing descendant-process cleanup timing failure. Quiet final run: **10/10 passed in 6.08 seconds**, `/tmp/slow_dance_tools/delivery_fast_final.log` (durable copy in the checkpoint folder).
- One initial all-at-once fingerprint attempt and one combined two-scene load exhausted memory. Subsequent bounded-memory fingerprints and separate-process scene loading completed. Checkpoint saves and integration checks are sequential. Early preservation processes emitted add-on shutdown-handler warnings after successful saves; preservation helpers now restore the handler lists.
- `integrate_saved_library.py`, `compact_checkpoint.py`, `scene_metadata.json`, `integration_report.json`, `authoring_checkpoint_fingerprints.json`, `checkpoint_compaction_report.json`, and `routine_storage_report.json` preserve the exact integration/storage procedure and results. These are preservation tools, not choreography generators.

Exact read-only combined-library verification (from `apps/a-game`, with the Blender profile variables above):

```sh
"$BLENDER" --background --python-exit-code 1 \
  --python docs/animation_work_status/slow_dance_man_and_woman3/integrate_saved_library.py -- --verify
```

To repeat saved-asset integration after a concurrent combined-library change, back up that newer binary, then run the same script with `--metadata-from docs/animation_work_status/slow_dance_man_and_woman3/scene_metadata.json` instead of `--verify`. This links existing clips and verifies preservation of preexisting curves; it performs no generation, refinement, bake, or render.

- Final storage reopen: the compacted checkpoint reopened with **66 matching action fingerprints**, 33 linked bakes, and all dependencies resolved. The recompressed routine also passed the combined-library reopen check.
- Fresh-process integrated motion review: **5/5 representative clips passed** (`closed_hold`, `wrapped_hold`, `promenade_hold`, `underarm_turn_right`, `gentle_dip`). `integrated_motion_review.json` records measurements and integrated dependency hashes. The earlier complete 32-clip source and 33-clip bake reports remain historical authoring-baseline evidence; they are not reclassified as complete integrated-dependency reviews. Separate authoring/delivery dependency manifests preserve both baselines.
- Preservation stage checks: `python scripts/lfs_policy.py check`, Python compilation of the four slow-dance recipe/review scripts, and `git diff --cached --check` passed. All task assets' staged full binary blobs match `asset_manifest.json`; no outgoing task asset is an LFS pointer.

### Main integration

- Rebuilt task commit: `8c180e425e591b73f6e9426f7863f9baad0ebee9`.
- Merged into local `main` as `e5cb89eaa573ac60ea27597743e2bc37b78b8a92`, after fetching remote `d826684eaf29f8cd62cabb1f172e570d11093a88`. The merge preserved the other chats' changes and required no conflicts. The combined scene, slow-dance sources, and evaluated dependencies match the verified preservation commit.
- Post-merge required fast suite: **10/10 passed in 6.43 seconds** (`main_fast_suite.log`). Storage policy: **31,190 indexed files passed**. `git lfs push --dry-run origin main` completed with zero objects to upload.
- Delivery uses ordinary history-preserving pushes. Remote main can advance concurrently; later integration commits and the final verified remote result are identified in the delivery response and Git history. No animation authoring, baking, export, or render was resumed.
