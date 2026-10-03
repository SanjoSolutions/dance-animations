# Local validation

The library contains 3,500 runtime clips and 3,500 Blender sources across 92 styles. Sources retain their recorded hashes. Pole dance actions extracted from the main scene carry their own provenance.

The automated checks cover:

- Every runtime clip loads with Three.js and Meshopt support, binds to the requested MPFB skeletons, matches its catalog duration, and seeks to finite transforms at the start, middle, and end.
- Both full MPFB bodies have human proportions at rest and during a solo move. The Woman body's inherited scale was corrected in both Blender studios and the exported model.
- Paired playback binds each performer independently.
- Move grouping separates dance style and character from move names and preserves move words such as “Running man.” Selection changes push browser history entries with their URL parameters; Back and Forward restore the style, move, and character. The website uses in-memory selections and browser history.
- Clip delivery preserves GLB bytes through explicit gzip transport and automatic HTTP decompression.
- The native studio lists the entire library and loads sources on selection, keeping its initial action set compact. Selected libraries resolve inside this project.
- Native controls support selection, editing, creation, source saving, deformation baking, and GLB export. Saving and reopening the test animation preserves every deformation bone's pose within 0.0001; the observed maximum difference was 0.000000775.
- Every style resolves to a clothed MPFB character. Eight outfit groups contain textured skinned garments; each Man and Woman variant binds a solo move and retains a coherent full-height body across sampled poses.
- Both Blender studios contain packed character textures, fitted garment instances, actor collections, and working outfit coverage masks. Selecting a style changes the native outfit along with the animation. Garment meshes, materials, and packed textures are linked from 17 Blender libraries using relative paths. Women's practice and pole outfits use a full-length knitted top with long sleeves and full-length pants; the other women's outfits cover the waist with tops or dress bodices.
- Clothing linking preserves sampled evaluated garment positions within 0.000001; the observed maximum difference was 0.000000532. Studio relocation, material editing followed by library rebuilding, and saved library reopening pass. Garment deformation modifiers point to the local character rigs.
- The studios link editable MPFB body meshes and target stacks from the 15.2 MB character library. The original fitted shape is preserved within 0.000001; the observed maximum difference was 0.000000481. MPFB macro editing, save/reopen, and relocated library loading pass.
- Character controls, deformation rigs, and matching animation tracks follow the shared dance skeleton in `assets/characters/rig-schema.json`.
- Source cleanup retains original hashes while recording the updated files. Shared character labels, hand-contact options, material metadata, and exported node names belong to the dance authoring setup.
- A full scan of 3,532 Blender files, 3,531 GLB metadata documents, other tracked files, and archive contents passes the reference cleanup check. Comparing 17 updated sources with their originals preserves supported motion channels, keys, handles, action slots, and frame ranges.
- Both studios and the editable character library are below 100 MB. Every garment library is below 100 MB, with the largest approximately 40.9 MB. These files use regular Git under the project's strict size-based LFS policy.
- Fresh Blender startup composes action-only Afro house and Salsa sources and descriptor-based Hip hop sources with their characters, editable rigs, and selected native animation. Saving and reopening the working scene retains the editing setup; opening retains the original source hashes.
- The Woman's standard MPFB braid and dark brown tint match Melissa's saved playground appearance in a-game. Every exported outfit includes the textured, head-skinned braid.
- The Game Rig Tools archive passes Blender extension validation and installation in an isolated profile. Native creation, source saving, and baking also pass with the installed extension.
- Dependency copyright notices, character asset credits, and the complete GPL extension source accompany the website and installation archive. Character exports embed their applicable credits; Blender artifacts retain license and attribution texts.
- TypeScript checking, source hash validation, GLB structure validation, and the Vite production build pass. Packaged runtime assets occupy approximately 728 MiB, with Blender sources kept in Git.

Browser review covered complete Man and Woman models, solo character selection, paired merengue playback, OS dark mode, and the packaged preview's compressed delivery. The source's historical dance review records remain under `source-review-records/`.

These checks establish asset coverage and structural playback. Each procedural study and provisional export retains its review status; dance accuracy, foot placement, hand contacts, performer clearance, and loop seams remain individual visual review tasks.

Run `npm run check`, `npm test`, and `npm run build`. Run `scripts/dance_tools.test.py`, `scripts/wardrobe.test.py`, and `scripts/link_wardrobe.test.py` with `blender --factory-startup --background --python-exit-code 1 --python <script>`. Run `scripts/character_library.test.py` with MPFB enabled using `blender --background --python-exit-code 1 --python scripts/character_library.test.py`. The [Blender guide](blender.md) describes authoring and extension installation.
