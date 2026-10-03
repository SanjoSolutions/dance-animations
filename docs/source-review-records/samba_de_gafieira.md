# Samba de gafieira animation work status

Recorded October 2, 2026 (UTC). Chat/task title: Samba de gafieira partner animations.
Working branch at stop: `samba-de-gafieira`. Starting/current commit before
preservation: `3c52737c74b488501e9cfe47e7029547c6f5fe88`.

The user's stop instruction supersedes the original animation completion scope.
This delivery preserves **46 partial procedural blocking studies** and their
authoring tools. Production motion approval, complete visual review, runtime
baking, and runtime export remain future work. Further choreography requires
fresh user authorization.

## Original scope and completed preparation

The original request covered a broad, organized Samba de gafieira repertoire for
both characters in `man_and_woman3.blend`, natural motion, contacts, clearance,
transitions, Blender 5.2 authoring, individual source files, validation, repository
documentation, commits, integration with concurrent main, and push verification.
The curated 46-clip vocabulary represents eight positions, fourteen position
transitions, eight footwork studies, and sixteen figure studies. Regional variants,
role reversal, aerial lifts, deep dips, airborne puladinhos, and additional
performance figures remain choreography extensions.

Repository instructions, the player animation workflow, paired authoring guide,
and Acro Yoga tooling were read. Blender 5.2.2 LTS build `d13f752e3b9c` was installed
at `/tmp/a-game-blender/blender-5.2.2-linux-x64/blender`; the `blender52` wrapper
sets four threads. All Blender authoring, validation, and renders used that build.
The system Blender executable is 4.3.2; select the explicit 5.2 executable when
resuming. Existing LFS character, shared-scene, prop, and app fixtures were
hydrated. Player Asset Export was enabled. Existing disco animation was examined
as a reuse candidate; reusable paired IK, contact, action, and split-file tooling
provided the suitable foundation for samba-specific timing and floor patterns.

## Durable files and delivery state

All paths below are relative to `apps/a-game`.

* `scripts/create_samba_de_gafieira.py`: vocabulary, planned support steps, paired
  poses, calibrated palm positions, native wrist constraints, soft finger curl,
  sparse curve simplification, boundary settling, and `AnimationFileWriter` output.
* `scripts/validate_samba_de_gafieira.py`: saved-source checks, evaluated contacts,
  floor geometry, own-leg and partner-leg clearance proxies, loop and transition
  measurements, and optional technical preview rendering.
* `scripts/samba_de_gafieira.md`: repertoire, timing, roles, workflow, limitations,
  and paused delivery notice.
* `animations/man_and_woman/samba_de_gafieira_catalog.json`: exact source names,
  categories, descriptions, positions, frames, playback ends, phase markers,
  support intervals, hand contact frames, and authored/baked/exported flags.
* `animations/man_and_woman/samba_de_gafieira_validation.json`: latest saved-source
  numerical report. Its hashes identify the measured binary revisions.
* `animations/man_and_woman/.gitattributes`: 46 exact-filename ordinary-Git
  exceptions. Existing shared scenes and character storage settings are preserved.
* `docs/animation_work_status/samba_de_gafieira/asset_inventory.json`: every draft's
  bytes, SHA-256, roles, frame ranges, delivery flags, and current validation result.
* `docs/animation_work_status/samba_de_gafieira/pre_stop_validation.json`: historical
  full report, with 37 passing studies and nine own-leg clearance failures before
  the last in-flight revision completed.
* `docs/animation_work_status/samba_de_gafieira/review_evidence.zip`: existing cache
  outputs, including 268 phase images, contact sheets, probe images, authoring logs,
  test logs, and validation logs. These are historical/mixed-revision previews;
  their presence represents saved evidence rather than completed visual approval.
* `docs/animation_work_status/samba_de_gafieira/source_composition_check.py`:
  preserved read-only diagnostic for the saved basic clip and composed rig bindings.

Each source contains synchronized `Man.rigify` leader and `Woman.rigify` follower
action slots and NLA bindings. All 46 are authored drafts; baked clips: **0**;
exported runtime clips: **0**. The combined library discovers these sources through
the established chooser; its binary and shared scene were preserved as supplied.
Technical review images are rendered outputs, separate from runtime exports.

Timing is 24 fps, nominal 120 beats per minute, with quick/quick/slow intervals of
12/12/24 frames. Stored phrases use 0–96 or 0–192. Cyclic clips have duplicate
closing poses and play through 95 or 191. Directed figures and transitions play
once through their stored endpoint. The inventory table below records each source.

## Exact stopping point and processes

The final owned authoring process was PID 10501, running:

```sh
/tmp/a-game-blender/blender-5.2.2-linux-x64/blender -t 4 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/create_samba_de_gafieira.py -- --only cortado cruzado enceradeira giro_casal_left giro_casal_right lateral piao saida_lateral tranca
```

At the first preservation process check it had already exited normally. Its log
records all nine saved sources followed by `Blender quit`. The remaining preview
renderer (formerly PID 9711) had also exited. Animation authoring and rendering
stayed stopped after that check. Read-only numerical verification and repository
tests continued for delivery. Each verification process completed before staging.

The nine revisions addressed crossing support lanes; traveling couple turns also
received 192-frame phrases. Their prior report hashes differ from the saved
assets. The historical report remains preserved separately. Other 37 source hashes
match that historical report. Complete visual review of the latest nine revisions
remains open. Incidental imported Godot resource edits from test setup were restored.

## Verification and environmental blockers

* `python tests/run_tests.py --suite fast`: **10/10 passed**, 6.68 seconds, after
  stop; `stop_fast.log` in the evidence archive. Earlier hair fixture failures were
  resolved by retrieving actual LFS objects.
* `BLENDER=/tmp/a-game-blender/blender52 python tests/run_tests.py --changed scripts/player_assets/test_animation_files.py --changed scripts/player_assets/test_paired_animation_authoring.py --changed scripts/player_assets/test_motion_review.py`:
  **14/14 passed**, 12.73 seconds; `authoring_suite.log`.
* `BLENDER=/tmp/a-game-blender/blender52 python tests/run_tests.py --changed animations/man_and_woman/samba_de_gafieira_basico.blend --slow-timeout 60`:
  **22/67 passed**, 1186 seconds; `suite.log`. Godot 4.6.3 reported missing
  `PopupMenu.search_bar_enabled`, runtime `EditorInterface.get_resource_filesystem`
  errors, and scene failures. Several checks reached the explicit 60-second
  timeout. Blender bake checks encountered missing Game Rig Tools (`StopIteration`),
  and other legacy checks emitted driver/script errors. These are recorded failures,
  with baseline attribution still requiring investigation in a matching environment.
* Saved basic source composition diagnostic: **passed**, both editable control
  rigs, correct paired slots/NLA bindings, 24 fps; `source_check.log`.
* `python -m py_compile scripts/create_samba_de_gafieira.py scripts/validate_samba_de_gafieira.py`:
  **passed** during preservation.

The saved-source validator samples every three frames, half-frame offsets, phase
boundaries, and evaluated mesh floor geometry every twelve frames. Tolerances are
5 mm IK reach error, 4 mm plant drift, 25 mm calibrated palm gap, 10 mm floor
penetration, 20 mm torso proxy gap, 5 mm leg capsule gap, 0.2 mm loop closure,
0.008 m/frame loop velocity difference, 0.002 radians loop rotation, and 0.03
radians/frame angular velocity difference. Torso proxies use 0.15 m radii and leg
capsules use 0.05 m radii. Full skin collision, physical balance, dance authenticity,
and natural wrists/fingers require complementary visual and specialist review.

## Remaining work and exact resume commands

Concurrent main now supplies `scripts/blender/install_animation_tools.py` for
bundled Game Rig Tools and Player Asset Export setup. Follow
`scripts/blender/README.md` and use the same profile for all later Blender
processes. The earlier addon failure describes the actual pre-integration test
environment; the newly available setup offers the resume path.

After fresh authorization, review the current numerical report, inspect complete
playback from multiple views, refine the remaining clearance/ergonomic issues,
review role variants if added, and validate any changed source again. Address the
recorded Godot/addon environment failures before runtime baking/export validation.
Keep authored, baked, and exported states separate. Current sources constitute
partial procedural studies even when their numerical checks pass.

Run from `/workspace/sanjo-solutions/apps/a-game` in this environment:

```sh
export BLENDER=/tmp/a-game-blender/blender52
"$BLENDER" --version
"$BLENDER" --background --python-exit-code 1 --python scripts/blender/install_animation_tools.py
git lfs pull --include='apps/a-game/**'
"$BLENDER" -b animations/man_and_woman/samba_de_gafieira_basico.blend --disable-autoexec --python-exit-code 1 --python docs/animation_work_status/samba_de_gafieira/source_composition_check.py
"$BLENDER" -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_samba_de_gafieira.py
python tests/run_tests.py --suite fast
```

The following authoring/rendering commands are future resume examples, subject to
fresh authorization. Choose the relevant clip after reading its recorded result:

```sh
"$BLENDER" -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/create_samba_de_gafieira.py -- --only piao
"$BLENDER" -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_samba_de_gafieira.py -- --only piao --render .cache/samba_de_gafieira/resumed_review
# Refresh the full report after selected validation overwrites it:
"$BLENDER" -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_samba_de_gafieira.py
```

Use **Bake & Export Active Animation** in Player Asset Export for any later runtime
delivery, then save that individual source. The catalog and completion record
should reflect actual baked and exported assets.

## Preservation verification result

Read-only validation after the stop completed with exit code 1: **43/46 studies
passed**. All 46 source hashes match the current report. Remaining failures are
`giro_casal_left`, `giro_casal_right`, and `piao`, each for own-leg capsule
clearance (minimum gaps -0.099977, -0.047390, and -0.033924 m respectively).
The required gap is +0.005 m. These three studies require motion refinement
after fresh authorization. All fourteen transition endpoint comparisons passed;
maximum displacement was 0.000001914 m. The report records loop, contact,
reach, floor, and partner-clearance measurements separately.

Command: `/tmp/a-game-blender/blender52 -b animations/man_and_woman/shared_scene_data.blend --disable-autoexec --python-exit-code 1 --python scripts/validate_samba_de_gafieira.py`.
Log: `stop_validation.log` in the evidence archive. Authoring/rendering processes
and owned verification processes have completed.

The 46 source binaries total 6,902,068 bytes; largest: 177,845 bytes. The evidence archive is 38,466,006 bytes (SHA-256 `ae4b2202cc97a61de3137e2f219c987835c5ccdf1450bb407da8fdceb3646e48`). All fit the 104,857,600-byte ordinary-Git limit. Each source has `filter: unset`; the archive has `filter: unspecified`. Existing asset storage remains scoped to its prior rules.

## Saved source inventory

Every filename below belongs to `animations/man_and_woman/`. Roles for every row: Man leader / Woman follower. State for every row: authored draft; baked 0; exported 0. Numerical PASS means the measured checks passed, with visual/physical approval still open.

| Source file | Stored frames | Playback end | Mode | Numerical result | Bytes |
| --- | --- | ---: | --- | --- | ---: |
| `samba_de_gafieira_balanco.blend` | 0–96 | 95 | Loop | PASS | 138444 |
| `samba_de_gafieira_basico.blend` | 0–96 | 95 | Loop | PASS | 138055 |
| `samba_de_gafieira_boleio.blend` | 0–96 | 95 | Loop | PASS | 134859 |
| `samba_de_gafieira_caminhada_backward.blend` | 0–96 | 96 | Once | PASS | 136075 |
| `samba_de_gafieira_caminhada_forward.blend` | 0–96 | 96 | Once | PASS | 137048 |
| `samba_de_gafieira_carrinho.blend` | 0–96 | 96 | Once | PASS | 133580 |
| `samba_de_gafieira_closed_to_counter_promenade.blend` | 0–192 | 192 | Once | PASS | 176105 |
| `samba_de_gafieira_closed_to_open_single_hand.blend` | 0–192 | 192 | Once | PASS | 151511 |
| `samba_de_gafieira_closed_to_open_two_hand.blend` | 0–192 | 192 | Once | PASS | 151494 |
| `samba_de_gafieira_closed_to_promenade.blend` | 0–192 | 192 | Once | PASS | 174936 |
| `samba_de_gafieira_closed_to_separated.blend` | 0–192 | 192 | Once | PASS | 170159 |
| `samba_de_gafieira_closed_to_shadow.blend` | 0–192 | 192 | Once | PASS | 169487 |
| `samba_de_gafieira_closed_to_side_by_side.blend` | 0–192 | 192 | Once | PASS | 169039 |
| `samba_de_gafieira_cortado.blend` | 0–96 | 95 | Loop | PASS | 138990 |
| `samba_de_gafieira_counter_promenade_to_closed.blend` | 0–192 | 192 | Once | PASS | 175934 |
| `samba_de_gafieira_cruzado.blend` | 0–96 | 95 | Loop | PASS | 139916 |
| `samba_de_gafieira_enceradeira.blend` | 0–192 | 192 | Once | PASS | 177845 |
| `samba_de_gafieira_escovinha.blend` | 0–96 | 95 | Loop | PASS | 133647 |
| `samba_de_gafieira_facao.blend` | 0–96 | 95 | Loop | PASS | 135814 |
| `samba_de_gafieira_gancho.blend` | 0–96 | 95 | Loop | PASS | 137200 |
| `samba_de_gafieira_giro_casal_left.blend` | 0–192 | 192 | Once | Own-leg clearance failure | 176879 |
| `samba_de_gafieira_giro_casal_right.blend` | 0–192 | 192 | Once | Own-leg clearance failure | 176753 |
| `samba_de_gafieira_giro_cavalheiro.blend` | 0–192 | 191 | Loop | PASS | 154662 |
| `samba_de_gafieira_giro_dama_left.blend` | 0–192 | 191 | Loop | PASS | 166290 |
| `samba_de_gafieira_giro_dama_right.blend` | 0–192 | 191 | Loop | PASS | 167805 |
| `samba_de_gafieira_lateral.blend` | 0–96 | 95 | Loop | PASS | 136065 |
| `samba_de_gafieira_letra.blend` | 0–96 | 95 | Loop | PASS | 135621 |
| `samba_de_gafieira_open_single_hand_to_closed.blend` | 0–192 | 192 | Once | PASS | 152293 |
| `samba_de_gafieira_open_two_hand_to_closed.blend` | 0–192 | 192 | Once | PASS | 151055 |
| `samba_de_gafieira_passagem.blend` | 0–192 | 192 | Once | PASS | 174682 |
| `samba_de_gafieira_piao.blend` | 0–192 | 192 | Once | Own-leg clearance failure | 177479 |
| `samba_de_gafieira_position_closed.blend` | 0–96 | 95 | Loop | PASS | 130342 |
| `samba_de_gafieira_position_counter_promenade.blend` | 0–96 | 95 | Loop | PASS | 127682 |
| `samba_de_gafieira_position_open_single_hand.blend` | 0–96 | 95 | Loop | PASS | 128492 |
| `samba_de_gafieira_position_open_two_hand.blend` | 0–96 | 95 | Loop | PASS | 130166 |
| `samba_de_gafieira_position_promenade.blend` | 0–96 | 95 | Loop | PASS | 127360 |
| `samba_de_gafieira_position_separated.blend` | 0–96 | 95 | Loop | PASS | 127184 |
| `samba_de_gafieira_position_shadow.blend` | 0–96 | 95 | Loop | PASS | 126112 |
| `samba_de_gafieira_position_side_by_side.blend` | 0–96 | 95 | Loop | PASS | 125858 |
| `samba_de_gafieira_promenade_to_closed.blend` | 0–192 | 192 | Once | PASS | 173929 |
| `samba_de_gafieira_saida_lateral.blend` | 0–96 | 95 | Loop | PASS | 139672 |
| `samba_de_gafieira_separated_to_closed.blend` | 0–192 | 192 | Once | PASS | 169593 |
| `samba_de_gafieira_shadow_to_closed.blend` | 0–192 | 192 | Once | PASS | 166842 |
| `samba_de_gafieira_side_by_side_to_closed.blend` | 0–192 | 192 | Once | PASS | 167963 |
| `samba_de_gafieira_tesoura.blend` | 0–96 | 95 | Loop | PASS | 136071 |
| `samba_de_gafieira_tranca.blend` | 0–96 | 96 | Once | PASS | 135080 |

## Integration checkpoint

The preservation commit was rebased onto origin/main `074c6a02e32d1d0c6960425218e8abec83e3c9b0`; its resulting task commit is `2d7f2070b8fdc70f89413cbbe8ea0ed0d904ce1c`. The storage-attribute conflict retained every concurrent entry and all 46 Samba entries. The shared scene, both anatomical character sources, and prop payload hashes match the validated dependencies despite concurrent conversion from LFS pointers to ordinary Git. Animation sources retain their recorded hashes.

After rebase, `python tests/run_tests.py --suite fast` passed **10/10** in 6.04 seconds (`samba_de_gafieira/integration_fast.log`). `python scripts/lfs_policy.py check`, from the repository root, passed for 24,157 staged files. The evidence archive CRC check passed for all 303 archived files. The Animation section of `AGENTS.md` now documents separate own-leg clearance checks and links this checkpoint. Final integration and remote commit verification are reported with the delivery message.

Final integration fetched origin/main `7a737f5ea329674e1c5886891de156c802ed33fb` immediately before merging. Both documentation and attribute conflicts retained the concurrent entries and Samba additions. The merged fast suite passed **10/10** in 6.45 seconds (`samba_de_gafieira/merge_fast.log`); the storage policy passed for 25,879 staged files before adding this final log.
