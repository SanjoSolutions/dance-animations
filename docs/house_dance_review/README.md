# House repertoire completion

Local review, 2026-10-08. The preserved 45-definition plan now has a source and runtime export for both performers: **90 solo clips**, comprising 70 standing phrases/positions, 12 supported-floor studies, and eight directed transitions. The catalog retains each clip’s procedural-study status and imported provenance.

Open the [motion gallery](index.html) through the project’s development server. Each clip has a front/side video, a contact sheet, and a measured review record. The normal animation viewer also lists the complete House repertoire. The sources live in `animations/house_dance/sources/`; matching GLBs live in `animations/house_dance/`.

## Authored contract

Every source uses Blender 5.2.2, the current shared MPFB rigs, and native solo PLAYER or PARTNER action bindings. Each contains an editable control action and its native deformation bake. Sources cover frames 0–96 at 24 fps: four seconds, eight beats at 120 BPM. Loop playback excludes the duplicated endpoint. The four directed transition definitions play once and hold their destination pose in the viewer.

The vocabulary and exact footfall recipes are in [`repertoire.py`](../../scripts/house_dance/repertoire.py). Standing motion reuses the original idle stance and relaxed-finger setup. The procedural recipes were recovered from `SanjoSolutions/sanjo-solutions` commit `7f9ce654056b1f4972743cc332585fef765e5c13`, under `apps/a-game/scripts/player_assets/house_dance/`, and adapted to this checkout’s source, contact, and export helpers. `reference.json` records the neutral-pose source and hash. Each action and clip report records its applicable recipe hashes.

Changes include evaluated sole-height calibration, complete pose restoration between sparse-key solves, fitted floor fingers, knee and palm clearance, wider half-turn foot paths, forearm-relative wrist orientation, and the woman’s articulated toe-support clearance. Turns use the native root control for heading, keeping local limb-twist interpolation continuous. Half-turn support intervals include corrective foot keys. Their wrist keys are fitted again after composing the portable source against the shared template. Floor studies retain their explicit per-action wrist-limit setting through the project’s animation helper. Standing clips use the native wrist constraints. Shared characters, rest skeletons, drivers, and the studio template retain their existing files.

## Validation and evidence

[`summary.json`](summary.json) contains the aggregate measured limits. Every file in `clips/` links the saved source/export hashes, recipe/dependency hashes, and these independent checks:

1. Native control review at 195 times, including half frames and loop-boundary samples: support targets, limb reach, separation, clearance, and loop continuity.
2. Freshly reopened source review of all 209 deformation bones at 387 times, including quarter frames. Evaluated MPFB base-body skin review samples foot support, floor height, palms, and fingers at 195 times. Surface intersection checks cover opposing legs/feet and forearms/palms against the torso at authored keys and six-frame intervals.
3. Native Game Rig Tools baking at 48 samples per second through `dance_tools.export_action`. Baked playback is evaluated with live follow constraints muted. Editable and baked actions are saved back on the source’s 24 fps timeline. The denser bake preserves fast interpolated accents.
4. Actual Three.js runtime binding on both project MPFB character models, comparing every deformation-bone position at the same 387 times. Maximum accepted position error is 5 mm; native integer-frame matrix error is below 0.0001 and angular error below 0.06 radians.
5. Source installation through `dance_tools.save_source`, a fresh reopen from the final project-relative location, exact action-curve signatures, dependency resolution, and eight additional integer/fractional playback comparisons.
6. Dual-view WebGL captures of all 90 clips: 33 samples at three-frame spacing, encoded at eight frames per second. The saved videos include the duplicated endpoint for loop inspection. Contact sheets show eight selected poses.

[`transitions.json`](transitions.json) compares the 16 entry/exit endpoints for `relaxed_to_ready`, `ready_to_relaxed`, `ready_to_low`, and `low_to_ready` against their named standing-position clips on the actual runtime models. Tolerances are 0.1 mm in position and 0.001 radians in orientation.

Surface gates allow at most 4 mm of penetration and 12 mm of planted support gap. Sampling and selected surface pairs establish the stated coverage. The studies carry local motion/surface review rather than professional dance-authenticity or dynamic-balance certification. Floor studies start and finish in their supported floor formation; the four planned transition definitions connect standing positions. Arbitrary viewer crossfades remain general pose blends.

## Reproduction

Use the project’s Blender setup from [the Blender workflow](../blender.md). Task scripts and caches stay inside the checkout. Run stages in order; each Blender worker starts a fresh process and writes a per-clip checkpoint/log. Select clip IDs after the stage to regenerate a subset.

```sh
python scripts/house_dance/batch.py author --workers 2
python scripts/house_dance/batch.py export --workers 2
python scripts/house_dance/batch.py validate --workers 2
node scripts/house_dance/runtime_review.mjs
node scripts/house_dance/review_transitions.mjs
python scripts/house_dance/batch.py finalize --workers 2
```

For the visual review, run the Vite development server, install `playwright-core` in `.cache/house/browser`, and supply the clip IDs to `node scripts/house_dance/capture.mjs --motion`. Chromium and FFmpeg produce the captures; Pillow builds the gallery with `python scripts/house_dance/gallery.py`. Inspect the saved views before running `python scripts/house_dance/sync_catalog.py`, which requires matching passing source, runtime, relocation, and visual evidence for all 90 clips.

Final [project checks](project-checks.json) pass: `npm run check` verifies 3,623 runtime clips and 3,541 source hashes, `npm test` passes all 42 tests, and `npm run build` packages the complete runtime library. The [browser check](browser-review.json) confirms the 45 House choices, performer selection, directed endpoint/restart behavior, and all 90 gallery entries. The required pre-existing slow-dance LFS source was hydrated for the full inventory check. Publication follows the local quality-review policy in `AGENTS.md`.

The [original preservation record](../source-review-records/house_dance.md) remains the historical account of the earlier 49-source stopping point.
