# Directed clip playback

The catalog now marks 24 reviewed directed clips with `loop: false`: eight Hip-hop transitions, Hustle `return_to_closed` and `send_out`, and fourteen Salsa figures. The existing House one-shot playback path plays each once, holds the closing pose, and supports Restart and Play. Ordinary loops keep their current behavior.

The exact clip set comes from [priority recovery evidence](priority_recovery/evidence.json). All 24 saved source and runtime export SHA-256 hashes match that report at baseline `039e2626b490e07a1c95192c265e5635cc77f07c`. Shared studio, character-library, and skeleton-schema hashes match as well. [This review's evidence](directed_playback/evidence.json) lists every clip, range, performer, file size, source/export hash, model hash, dependency revision, study label, and sampled runtime behavior.

`retrieve_playback_variants` applies the reviewed settings through catalog imports, saved-source preview merges, and native exports. The checked-in catalog change consists of these 24 fields. Saved animation bytes, original provenance, and procedural-study labels retain their recorded revisions.

## Verification

- `python scripts/import_assets.test.py`: five tests pass. Regeneration restores one-shot settings for all 24 clips with omitted, true, or false incoming loop values across import, preview, and native-export statuses. The rest of the catalog retains its mapped entries and metadata.
- `npm run check`: passes; 3,677 selectable clips, 3,558 source hashes, music coverage, and license checks.
- `npm run build`: passes; 3,677 runtime entries packaged.
- `npm test`: 73 tests pass, including all-library MPFB binding and the 27 new directed/sequence cases.
- Twenty-four actual-model regression cases bind the project's MPFB bodies through `bindClip`, `DancePlayback`, and `DanceMotion`. Samples cover 0%, 25%, 50%, 75%, and 99.9% of the phrase; endpoint holds at 100%, 150%, and 300%; and restart at 0% and 50%. Every bound bone world matrix and three skinned vertices per mesh match direct endpoint/start samples within a component tolerance of 0.000001.
- Three actual-model sequencing cases hold directed endpoints until a sixteen-bar change, then verify the incoming ordinary loop's start, quarter pose, wrap, and restart. Existing transport tests cover continuous music and phrase-based scheduling.
- Headless Edge 154.0.4258.62 browser review passes with decoded textures and the project's street/Latin wardrobe models. `hip_hop_man_neutral_to_low`, `new_york_hustle_send_out`, and `salsa_cross_body_lead` finish naturally with Loop checked and hold their endpoints. Restart, ordinary loop wrapping, and sequential advancement pass for all three styles. Endpoint and restart screenshots received visual inspection. Browser page errors: zero.

The browser review used a temporary profile and project-local Playwright dependencies after the in-app browser's Windows sandbox failed to start. The local runner and six screenshots are in `.cache/directed-playback/`; the compact browser result is retained in the evidence above.

## Coverage boundaries

This change establishes playback metadata and runtime behavior. The saved controls, source playback, and deformation bakes retain the matching recovery revisions and their historical measurements. Blender 5.2.1 LTS is installed locally; the recovery sources were recorded with Blender 5.2.2 LTS. This task uses the existing files and performs zero authoring or rebake operations. Choreographic quality, full surface collision, and continuous visual review of all 24 clips retain their existing procedural-study coverage.

For browser reproduction, launch `node node_modules/vite/bin/vite.js --host 127.0.0.1 --port 5176 --strictPort`, select Single mode with music disabled, select the representative clips above, and let each finish with Loop checked. Use Restart, select an ordinary loop, and then use Sequential mode with Bars per move set to 0. The endpoint and restart model comparisons run with `npm test`.

Publication uses a separate `codex/directed-clip-playback` pull request. Main integration follows the user's local quality-review approval.
