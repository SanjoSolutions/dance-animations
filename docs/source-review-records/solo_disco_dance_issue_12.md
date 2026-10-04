# Disco solo playback review

Recorded October 4, 2026 (Europe/Berlin). Author: Codex.

[Issue 12](https://github.com/SanjoSolutions/dance-animations/issues/12) reports
overlapping characters in `solo_disco_dance`. Its catalog entry requested both
performers at their shared origin. The routine now offers one move with Man and
Woman character choices. The original animation ID selects Man; the Woman ID is
`solo_disco_dance_woman`. Each choice binds its original performer tracks from
the shared GLB. Imports, preview merges, and native exports use the same variant
helper. Character-only suffixes group into the routine move.

## Asset identity and coverage

| Asset | SHA-256 |
| --- | --- |
| `animations/solo_disco_dance/sources/solo_disco_dance.blend` | `3cc2d41249567ac223a30bcd5f180d150664d36cb56574afb7450a6624bbc2e3` |
| `animations/solo_disco_dance/solo_disco_dance.glb` | `d852e655fc477685dc85dc96393bf54b423d74a582b7c7a75fc178501c88b732` |
| `models/wardrobe/club/mpfb-man.glb` | `f08c03e69e5c4ee47b7bfd3eccf6833316dcefeeb28810836cdb0dfc92bdd649` |
| `models/wardrobe/club/mpfb-woman.glb` | `57a320859d7b26a8695c7b1908883e9302e15d6fe82fdeddbfacda539c7d02e5` |

Blender 5.2.2 LTS inspected the saved source (version 5.2.44): authoring slots
`OBMan.rigify` and `OBWoman.rigify`, deformation slots
`OBMan.rigify_deform` and `OBWoman.rigify_deform`, stored frames 0–384 at 24 fps.
The existing `solo_disco_dance.baked` GLB lasts 16 seconds. The source, bake,
export bytes, provenance, and recorded `Game export` status retain their saved
revisions. This playback-selection fix establishes participant coverage;
authored contact, source/bake fidelity, and choreography acceptance retain their
prior review coverage.

Regression tests verify one routine with both character choices, variant
generation and repeat application, shared provenance, and exact equality of
each solo's bound tracks to its performer subset in paired binding. Track
equality covers all stored samples with exact comparison. Browser review uses
the actual clothed MPFB models and samples each character at source fractions
0, 0.25, 0.5, 0.75, and 0.99 (frames 0, 96, 192, 288, and 380.16). All ten
reviewed poses show one selected performer. The original URL, character
switching, Back/Forward navigation, and page-error checks pass.

## Validation

- `python scripts/import_assets.test.py`: passes.
- Focused Disco binding and routine grouping tests: pass.
- `npm test`: all 41 tests pass, including full-library runtime binding.
- `npm run build`: passes, packaging 3,583 selectable runtime variants.
- `python scripts/validate_licenses.py`: passes.
- `npm run check`: encounters the existing Slow dance source hash mismatch.
  `animations/slow_dance/sources/slow_dance_routine.blend` matches HEAD with
  SHA-256 `5ff34d91ebbc9739951eaa991b3d40ed710face67fc6714110985af643494161`;
  the inventory records `58716322c73963ebb8576d74edf1f30d07080e3f41d7cc70132d00cd3f3a8b20`.

The local quality review was presented to the user, who requested a pull request
for the reviewed fix. The pull request targets `main`.
