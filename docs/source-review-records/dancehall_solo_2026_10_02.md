# Dancehall solo animation work status

Recorded: October 2, 2026, 16:59 Europe/Berlin (14:59 UTC). Animation work stopped at approximately 16:56 Europe/Berlin on the user's cross-chat stop instruction.

Chat title: Dancehall solo animation repertoire (descriptive title; desktop title unavailable).
Project/environment: A-Game, `apps/a-game`, sanjo-solutions managed cloud environment.
Task branch: `codex/dancehall-solo`.
Checkout commit at pause: `fe09ef7b6a54f03909f7335d9673a27c15007d69`.
Delivery state: **paused, partial procedural blocking studies**. These assets preserve work in progress; they represent authored movement interpretations, with choreography authenticity and final natural-motion review still pending.

## Original scope and stopping point

The original request was a broad, organized Dancehall repertoire for both characters in `man_and_woman3.blend`, with solo clips, natural motion, planted contacts, body clearance, smooth transitions, interpolated/loop validation, reuse of appropriate existing motion, Blender 5.2 throughout, and the existing per-animation source workflow. It also requested ordinary Git for assets at or below 104,857,600 bytes, animation and documentation commits, integration with concurrent main work, uploads, and a verified main push.

A catalog of 32 movement studies and eight positions per character was implemented (80 planned clips). At the stop, **59 sources, 59 matching native bakes, and 59 individual GLB exports** were saved: 40 man and 19 woman clips. The next woman study, Wacky Dip, had no durable source/export at the stop. Twenty-one woman clips remain planned. The catalog is a selected repertoire, rather than an exhaustive historical Dancehall syllabus.

All Blender processes used **Blender 5.2.2 LTS**, build `d13f752e3b9c`. Game Rig Tools was absent during authoring. Integration later fetched `18e528c73` from main, which bundles it through `scripts/blender/install_animation_tools.py`; this resolves availability for a future authorized resume, while the saved clips retain their native Blender bakes. Baking used Blender's native visual `bpy_extras.anim_utils.bake_action_objects`, retaining rig constraints and verifying the resulting deform matrices. Files and publication use the existing `AnimationFileWriter`, `AnimationClipScene`, `AnimationParticipants`, and `AnimationUpdates` helpers. The original combined library, shared scene, and character model sources remain unchanged.

## Timing, roles, and source layout

Every saved source contains exactly one authoring action and its `.baked` action, with one participant slot in each. `dancehall_man_*` uses `Man.rigify` / `Man.rigify_deform`, role `PLAYER`; `dancehall_woman_*` uses `Woman.rigify` / `Woman.rigify_deform`, role `PARTNER`.

All clips span frames **0–120**, 24 fps, at a 96 BPM working tempo. Native phase markers are `entry_start=0`, `activity_start=30`, `activity_end=90`, and `dissolve_end=120`. Loop only **30–90** for activity playback. Entry and release connect to the ready stance; the full five-second clip is a sectioned sequence. Constant authoring channels have one key; changing controls generally have quarter-beat keys, with zero boundary tangents. Matching native bakes sample integer frames 0–120.

Source path for every saved row below: `animations/man_and_woman/<name>.blend`. Matching report: `output/dancehall/<name>.json`. GLB path: `models/player/animation_updates/<export filename>`, with its adjacent `.glb.import`. `models/player/animation_updates.tres` retains existing updates and references all 59 saved Dancehall exports. The runtime registry includes these provisional studies as part of the preserved state. Early exports retain the exporter's copied full-library `.glb.import` subresource settings; later exports use compact per-clip settings. Normalizing those inherited settings remains a delivery/runtime follow-up for the next authorized animation task.

## Exact clip inventory

The three state columns below mean authored / baked / exported. `output/dancehall/delivery_inventory.json` records every retained source, GLB, import setting, pose preview, surface report, and per-clip numerical report with actual bytes and SHA-256. `saved_source_inspection.json` records the independently reopened source actions, roles, ranges, and hashes.

| Clip | Authored / baked / exported | Export filename | Review state |
| --- | --- | --- | --- |
| `dancehall_man_bounce` | Saved / saved / saved | `dancehall_man_bounce_baked_eab804ee4b43.glb` | Procedural study; sole calibration pending |
| `dancehall_man_rockaway` | Saved / saved / saved | `dancehall_man_rockaway_baked_1df7743849c3.glb` | Procedural study; sole calibration pending |
| `dancehall_man_step_touch` | Saved / saved / saved | `dancehall_man_step_touch_baked_34fd136d0f16.glb` | Procedural study; sole calibration pending |
| `dancehall_man_forward_back` | Saved / saved / saved | `dancehall_man_forward_back_baked_eaba9b33690e.glb` | Procedural study; sole calibration pending |
| `dancehall_man_heel_dig` | Saved / saved / saved | `dancehall_man_heel_dig_baked_1db8b3408bb0.glb` | Sole calibration saved; 14 surface checkpoints pass |
| `dancehall_man_knee_lift` | Saved / saved / saved | `dancehall_man_knee_lift_baked_c5f6fea47d91.glb` | Procedural study; sole calibration pending |
| `dancehall_man_bogle` | Saved / saved / saved | `dancehall_man_bogle_baked_d541546a514b.glb` | Procedural study; sole calibration pending |
| `dancehall_man_butterfly` | Saved / saved / saved | `dancehall_man_butterfly_baked_cf7e8d70e339.glb` | Procedural study; sole calibration pending |
| `dancehall_man_tatty` | Saved / saved / saved | `dancehall_man_tatty_baked_22bc47a706bf.glb` | Procedural study; sole calibration pending |
| `dancehall_man_pepper_seed` | Saved / saved / saved | `dancehall_man_pepper_seed_baked_15886d5e2d1d.glb` | Procedural study; sole calibration pending |
| `dancehall_man_world_dance` | Saved / saved / saved | `dancehall_man_world_dance_baked_92047927d93d.glb` | Procedural study; sole calibration pending |
| `dancehall_man_tootsie` | Saved / saved / saved | `dancehall_man_tootsie_baked_482c586726db.glb` | Procedural study; sole calibration pending |
| `dancehall_man_log_on` | Saved / saved / saved | `dancehall_man_log_on_baked_92bd9ab256d9.glb` | Procedural study; sole calibration pending |
| `dancehall_man_signal_di_plane` | Saved / saved / saved | `dancehall_man_signal_di_plane_baked_561cebe1b034.glb` | Procedural study; sole calibration pending |
| `dancehall_man_pon_di_river` | Saved / saved / saved | `dancehall_man_pon_di_river_baked_e476ff969b17.glb` | Procedural study; sole calibration pending |
| `dancehall_man_pon_di_bank` | Saved / saved / saved | `dancehall_man_pon_di_bank_baked_3f99491dd203.glb` | Procedural study; sole calibration pending |
| `dancehall_man_row_di_boat` | Saved / saved / saved | `dancehall_man_row_di_boat_baked_d39d88833935.glb` | Procedural study; sole calibration pending |
| `dancehall_man_give_dem_a_run` | Saved / saved / saved | `dancehall_man_give_dem_a_run_baked_078589f55ec8.glb` | Procedural study; sole calibration pending |
| `dancehall_man_willie_bounce` | Saved / saved / saved | `dancehall_man_willie_bounce_baked_ca881d1af91d.glb` | Procedural study; sole calibration pending |
| `dancehall_man_wacky_dip` | Saved / saved / saved | `dancehall_man_wacky_dip_baked_529f1ee89da4.glb` | Procedural study; sole calibration pending |
| `dancehall_man_nuh_linga` | Saved / saved / saved | `dancehall_man_nuh_linga_baked_c17c1ca4e306.glb` | Procedural study; sole calibration pending |
| `dancehall_man_gully_creepa` | Saved / saved / saved | `dancehall_man_gully_creepa_baked_c4b64b78d251.glb` | Procedural study; sole calibration pending |
| `dancehall_man_over_di_wall` | Saved / saved / saved | `dancehall_man_over_di_wall_baked_ca00cfd101be.glb` | Procedural study; sole calibration pending |
| `dancehall_man_sweep` | Saved / saved / saved | `dancehall_man_sweep_baked_95f0b0f562f8.glb` | Procedural study; sole calibration pending |
| `dancehall_man_summer_swing` | Saved / saved / saved | `dancehall_man_summer_swing_baked_0bab352ce509.glb` | Procedural study; sole calibration pending |
| `dancehall_man_rum_ram` | Saved / saved / saved | `dancehall_man_rum_ram_baked_3287b4c98715.glb` | Procedural study; sole calibration pending |
| `dancehall_man_wine_clockwise` | Saved / saved / saved | `dancehall_man_wine_clockwise_baked_e317f7c78cae.glb` | Procedural study; sole calibration pending |
| `dancehall_man_wine_counterclockwise` | Saved / saved / saved | `dancehall_man_wine_counterclockwise_baked_b9643344e528.glb` | Procedural study; sole calibration pending |
| `dancehall_man_tick_tock` | Saved / saved / saved | `dancehall_man_tick_tock_baked_e9c8695c3757.glb` | Procedural study; sole calibration pending |
| `dancehall_man_body_wave` | Saved / saved / saved | `dancehall_man_body_wave_baked_af0343d65c84.glb` | Procedural study; sole calibration pending |
| `dancehall_man_shoulder_roll` | Saved / saved / saved | `dancehall_man_shoulder_roll_baked_ab68dfa967a0.glb` | Procedural study; sole calibration pending |
| `dancehall_man_dutty_wine` | Saved / saved / saved | `dancehall_man_dutty_wine_baked_74c5839372de.glb` | Procedural study; sole calibration pending |
| `dancehall_man_ready` | Saved / saved / saved | `dancehall_man_ready_baked_1b50d09b8891.glb` | Procedural study; sole calibration pending |
| `dancehall_man_wide` | Saved / saved / saved | `dancehall_man_wide_baked_48e03ffddbc1.glb` | Procedural study; sole calibration pending |
| `dancehall_man_low` | Saved / saved / saved | `dancehall_man_low_baked_585af33e9f43.glb` | Sole calibration saved; 14 surface checkpoints pass |
| `dancehall_man_stagger_left` | Saved / saved / saved | `dancehall_man_stagger_left_baked_2f6726addc4a.glb` | Procedural study; sole calibration pending |
| `dancehall_man_stagger_right` | Saved / saved / saved | `dancehall_man_stagger_right_baked_3c1369b69f6a.glb` | Procedural study; sole calibration pending |
| `dancehall_man_hands_up` | Saved / saved / saved | `dancehall_man_hands_up_baked_c5b5ef6fccc9.glb` | Procedural study; sole calibration pending |
| `dancehall_man_forward_hinge` | Saved / saved / saved | `dancehall_man_forward_hinge_baked_cb4637b915c0.glb` | Procedural study; sole calibration pending |
| `dancehall_man_open_chest` | Saved / saved / saved | `dancehall_man_open_chest_baked_41395e68daeb.glb` | Procedural study; sole calibration pending |
| `dancehall_woman_bounce` | Saved / saved / saved | `dancehall_woman_bounce_baked_a2707190bccb.glb` | 14 surface checkpoints pass; broader review pending |
| `dancehall_woman_rockaway` | Saved / saved / saved | `dancehall_woman_rockaway_baked_648ec964376e.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_step_touch` | Saved / saved / saved | `dancehall_woman_step_touch_baked_b1354c9524ce.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_forward_back` | Saved / saved / saved | `dancehall_woman_forward_back_baked_3a61033332e2.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_heel_dig` | Saved / saved / saved | `dancehall_woman_heel_dig_baked_16654252de12.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_knee_lift` | Saved / saved / saved | `dancehall_woman_knee_lift_baked_aa0d640fe47a.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_bogle` | Saved / saved / saved | `dancehall_woman_bogle_baked_3da48d7264ea.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_butterfly` | Saved / saved / saved | `dancehall_woman_butterfly_baked_2ab83b41c99f.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_tatty` | Saved / saved / saved | `dancehall_woman_tatty_baked_e069325cd41e.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_pepper_seed` | Saved / saved / saved | `dancehall_woman_pepper_seed_baked_6a57dc66940f.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_world_dance` | Saved / saved / saved | `dancehall_woman_world_dance_baked_9c98b0aba42f.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_tootsie` | Saved / saved / saved | `dancehall_woman_tootsie_baked_888635f82b32.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_log_on` | Saved / saved / saved | `dancehall_woman_log_on_baked_e224318a61d3.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_signal_di_plane` | Saved / saved / saved | `dancehall_woman_signal_di_plane_baked_8f336858b43c.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_pon_di_river` | Saved / saved / saved | `dancehall_woman_pon_di_river_baked_284fc585efc6.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_pon_di_bank` | Saved / saved / saved | `dancehall_woman_pon_di_bank_baked_998312b038d2.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_row_di_boat` | Saved / saved / saved | `dancehall_woman_row_di_boat_baked_3c8b6689a3a9.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_give_dem_a_run` | Saved / saved / saved | `dancehall_woman_give_dem_a_run_baked_5cafc1a1ce34.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_willie_bounce` | Saved / saved / saved | `dancehall_woman_willie_bounce_baked_22e21d1c535b.glb` | Procedural study; surface/choreography review pending |
| `dancehall_woman_wacky_dip` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_nuh_linga` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_gully_creepa` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_over_di_wall` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_sweep` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_summer_swing` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_rum_ram` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_wine_clockwise` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_wine_counterclockwise` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_tick_tock` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_body_wave` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_shoulder_roll` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_dutty_wine` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_ready` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_wide` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_low` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_stagger_left` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_stagger_right` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_hands_up` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_forward_hinge` | Pending / pending / pending | — | Planned; no saved asset |
| `dancehall_woman_open_chest` | Pending / pending / pending | — | Planned; no saved asset |

## Supporting files and reuse

- `scripts/dancehall/choreography.py`: 40-item catalog, normalized target choreography, positions, and entry/release interpolation. Reuses/adapts the existing disco step sequence and proportional rig conventions.
- `scripts/dancehall/author.py`: sparse action writer, participant/phase metadata, native bake, numerical validation, source save, individual export, and resume selection. Composes `DiscoCharacter`, `RigYogaPoser`, and `DiscoWristPoser`; source poses originate in the existing mountain/ready conventions. No pre-existing named Dancehall clip was found.
- `scripts/dancehall/review.py`: half-frame endpoint/contact proxies, knee/wrist checks, activity-loop position/rotation/velocity, and integer-frame bake comparison.
- `scripts/dancehall/review_surfaces.py`: read-only evaluated anatomical surface checkpoints using the existing `AnatomicalSurface` / `BodyClearance` helpers.
- `scripts/dancehall/preview.py`: Blender Workbench source previews. Its final floor/framing edits are saved, but the existing six images predate those edits. No further rendering occurred after the stop.
- `scripts/dancehall/verify_exports.gd`: direct GLTFDocument checks against published man/woman skeletons and the native phase-marker importer. An optional expected inventory count supports partial delivery.
- `scripts/dancehall/inspect_saved.py`: read-only Blender source-container verification.
- `output/dancehall/previews/`: six saved PNGs: man Bogle at frames 37.5, 45, 52.5, 60; woman Bounce at 37.5 and 45. The man previews crop the soles and predate final framing changes.
- `output/dancehall/surfaces/`: four 14-checkpoint reports for man Bogle, man Heel Dig, man Low, and woman Bounce.
- `output/dancehall/logs/`: preserved authoring, calibration, fast/related suite, direct export, source inspection, and surface logs. Earlier failed runs remain labeled by their original filenames.

## Validation and precise limitations

All 59 saved per-clip reports recorded a passing numerical rig review and passing native bake comparison before saving. Each rig review sampled 241 half frames over 0–120; each bake comparison sampled all 121 integer frames. Across those reports: maximum foot endpoint error 0.225 mm, maximum hand endpoint error 0.111 mm, maximum wrist bend 6.552 degrees, activity endpoint positional mismatch below 1e-12 meters, maximum loop linear derivative mismatch 0.001513 meters/frame, maximum baked deform position difference 0.437 mm, and maximum baked rotation difference 0.000691 radians. These metrics measure the specified rig/proxy checks; they do not establish complete skin grounding or final dance quality.

**Known surface blocker:** the man's skinned sole extends below the ankle reference and varies with pose. Man Bogle's saved surface report measures -19.25 to -21.14 mm relative to floor zero. Earlier Low measured about -28.78 mm. Thirty-eight man clips still use this original ankle-reference grounding. The latest authoring code calibrates both foot targets against evaluated skin for the man; only **man Heel Dig and man Low** were regenerated with that calibration before the stop. Their 14-checkpoint sole minima are 0.471–0.500 mm above floor zero, with zero reported body-region overlaps. Woman Bounce has -0.0965 to +0.0003 mm minima and zero reported overlaps. Other clips have no comparable complete surface report.

The latest `review.py` measures horizontal planted drift and angular velocity vectors. Most saved reports came from its earlier version, which measured ankle-reference positional drift and compared angular-speed magnitudes. Heel Dig and Low were regenerated with the later review. Do not describe the older reports as passing the newer full angular-vector check.

The source script evolved during generation. **Man Step Touch, Tootsie, and Log On** still contain the earlier choreography; the current script adds collecting steps and more distinct arm accents. The saved Man Tootsie and Log On studies share their earlier motion pattern. The generator also changes finger controls to Euler mode in its temporary scene, while the shared Rigify source uses quaternion defaults. Fresh-source finger playback compatibility requires correction/review; container inspection alone does not prove those Euler finger channels evaluate after reopening. Existing man clips therefore require an explicit rebuild and review when animation work is authorized again. `--resume` alone skips their existing passing reports. The current code is a continuation checkpoint, rather than a byte-reproducible recipe for every saved source.

Direct delivery verification:

```sh
python tests/run_tests.py --suite fast
godot --headless --path . --script scripts/dancehall/verify_exports.gd -- 59
blender -b --python-exit-code 1 --python scripts/dancehall/inspect_saved.py
```

The direct Godot export verification passed **59 clips / 7,917 animated bone tracks**, with matching participant skeletons, resolvable bone names, five-second duration, and all four native markers. Godot available here is **4.6.3**; project documentation also describes 4.7 workflows. Source inspection passed **59/59** containers, each with exactly the expected two actions, one slot per action, correct role, range, and markers.

The fast suite passed **9/9** earlier after hydrating existing hair physics resources. A delivery rerun after project import returned **8/9** because existing hair model GLBs lacked usable Godot imports; the activity JSON check printed success but emitted dependency compilation errors, which the runner correctly treated as failure. The final retry, after hydrating the seven existing hair-model GLBs and refreshing imports, passed **9/9 in 2.88 seconds**. Its log is `output/dancehall/logs/dancehall_delivery_fast_retry.log`.

The broader command `python tests/run_tests.py --changed animations/man_and_woman/dancehall_woman_bounce.blend --slow-timeout 90` selected nine fast and 57 slow checks. It was stopped during the user's preservation request. Several related checks passed; existing player/paired scenes failed on imported-resource prerequisites, including animation libraries and character dependencies, or hit 90-second timeouts. This run is **incomplete**, not a suite pass. The captured log is `output/dancehall/logs/dancehall_suite.log`. The Game Rig Tools-dependent checks required an add-on absent during that run; the integrated checkout now supplies its installer. The command using only the new Python script paths selected the nine fast checks and passed them; it supplied no additional slow coverage.

## Processes and preserved state

Owned authoring process PID 2263 and the broader test runner PID 2316 plus child PID 3447 received termination signals at the stop. The owned surface process PID 3642 was also targeted; its final saved Heel Dig surface report completed before termination took effect. All owned animation processes are stopped; one reaped-by-parent-pending Godot process was defunct at the final process check. Current durable outputs were retained. The temporary in-memory next action was discarded when its Blender process ended. All later Blender work was read-only saved-source inspection; all later Godot work was verification/import prerequisite setup. No post-stop animation generation, refinement, bake, export, or rendering was performed.

The disposable `/workspace/scratch/dancehall_*.log` paths hold the original execution logs; durable copies of relevant logs live under `output/dancehall/logs/`. Shared LFS dependencies were downloaded for inspection and testing. They retain their repository contents and are outside the task's staged changes. Godot's unrelated tracked import/model side effects are restored before commit. Existing update references are preserved when integrating concurrent edits.

## Remaining work and exact resume commands

Resume animation work only after a new user instruction authorizes it. Use a separate task branch and the enabled checkout-backed Player Asset Export add-on. Hydrate the combined/shared/character dependencies if necessary. Run commands below from `apps/a-game` with Blender 5.2 selected:

```sh
# Enable the tools now bundled by concurrent main, retaining one Blender 5.2 profile.
blender --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py

# Rebuild all 40 man studies with the current sole calibration and distinct footwork.
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/dancehall/author.py -- --characters Man

# Continue the 21 missing woman studies; the 19 saved studies are skipped.
blender -b animations/man_and_woman/shared_scene_data.blend --python-exit-code 1 --python scripts/dancehall/author.py -- --characters Woman --resume

# Reopen and inspect a saved source, then evaluate skin contacts without editing it.
blender animations/man_and_woman/dancehall_man_low.blend
blender -b animations/man_and_woman/dancehall_man_low.blend --python-exit-code 1 --python scripts/dancehall/review_surfaces.py

# After additional animation work is authorized, render fresh whole-body previews.
blender -b animations/man_and_woman/dancehall_man_bogle.blend --python-exit-code 1 --python scripts/dancehall/preview.py -- --frames 37.5 45 52.5 60

# Verify the full inventory only after all 80 clips exist.
godot --headless --path . --script scripts/dancehall/verify_exports.gd -- 80
blender -b --python-exit-code 1 --python scripts/dancehall/inspect_saved.py
python tests/run_tests.py --suite fast
python tests/run_tests.py --changed animations/man_and_woman/dancehall_woman_bounce.blend
```

Run authoring processes sequentially: individual source files are separate, while `animation_updates.tres` is a shared publication registry. Two pre-stop short calibration runs overlapped the woman generator; the final inventory check confirms that all 59 saved GLBs are referenced. A future concurrent writer should merge the registry as a union of resource paths.

Finish dense skin-contact checks, update old angular-vector reports, inspect full-body motion from multiple views, review movement recognizability with an informed Dancehall reference, simplify keys where measured interpolation permits, and assess transitions after calibration. Complete Godot import prerequisites and the relevant suite. Preserve actual-size-based ordinary-Git exceptions per intended file; assets at or below 104,857,600 bytes belong in ordinary Git.

## Storage and publication

All retained task binaries are below 100 MiB. Before staging, their byte sizes and Git attributes are inspected, and exact-filename `.gitattributes` exceptions are committed beside the animation sources, GLB updates, and PNG previews. Existing broad repository LFS rules remain in effect for other files. This task adds no new LFS objects; ordinary Git carries its saved binaries during the main push.

GitHub interactions and commits for this task are authored by **Codex**. Each new commit includes exactly one `Co-authored-by: Codex <noreply@openai.com>` trailer. Delivery integrates the current `origin/main` using ordinary history-preserving pushes, with remote ancestry verification. Final task and integration hashes are supplied in the delivery response and Git history; this status records the pre-delivery checkout commit above.

## Integration verification

The task preservation commit rebased onto `18e528c73` as `d7dca21b502c3b3b1054c843231554c6454f4085`. An add/add conflict in the animation-source `.gitattributes` was resolved by preserving both sets of exact-file rules. The integrated fast suite passed **10/10 in 5.96 seconds**; main added the Godot test-tree check. `python scripts/lfs_policy.py check` passed for the integrated index. The four source dependencies in `output/dancehall/authored_dependencies.json` retain exactly the hashes used during authoring after that integration. Shared-scene and source-model changes remain outside this task. The final main merge and remote ancestry are verified in the delivery response.
