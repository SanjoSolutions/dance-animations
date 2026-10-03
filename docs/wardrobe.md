# MPFB wardrobe

The viewer selects a fitted outfit automatically from the dance style. `wardrobe.json` contains garment choices and style groups. Styles outside a specific group use the street practice outfit. Practice clothing supports styles whose traditional costumes are outside this wardrobe's scope.

Mazurka uses the ballroom outfit: a full-skirt dress and a navy suit with a plain shirt.

| Group | Man | Woman |
| --- | --- | --- |
| Street | T-shirt, jeans, sneakers | T-shirt, jeans, sneakers |
| Club | Blue T-shirt, jeans, sneakers | T-shirt, denim shorts, sneakers |
| Ballroom | Navy suit, plain shirt, dress shoes | Full-skirt dress, flats |
| Latin | Navy suit, plain shirt, dress shoes | Red halter dress, flats |
| Swing | Striped shirt, jeans, lace-up shoes | Flapper dress, flats |
| Ballet | Tank, fitted pants, ballet flats | Swan tutu, ballet flats |
| Movement practice | Tank, fitted pants, sneakers | Full-length knitted top with long sleeves, full-length pants, sneakers |
| Pole practice | Tank, fitted pants, bare feet | Full-length knitted top with long sleeves, full-length pants, bare feet |

These are skinned MPFB meshes with embedded skin, eye, hair, garment, and shoe textures. Skin coverage masks follow the active garments. The main Blender studio and shared source template link fitted garment meshes, materials, and packed textures from `assets/wardrobe/<garment>.blend`. Local garment objects retain vertex groups, deformation modifiers, rig attachments, and outfit visibility. **Helpers > Animation > Select animation** selects the outfit with the animation. Material Preview shows the textures in Blender.

Women's outfits cover the waist with full-length tops or dress bodices.

The Woman uses Melissa's saved appearance from a-game's playground:
the standard MPFB `braid01` hairstyle in dark brown (`#36241a`). Its strand
texture retains the original alpha, with Melissa's shader tint baked for glTF.
The braid follows the head deformation bone in every outfit and Blender source.

`main.blend` and the shared template link editable MPFB body targets from `assets/characters/mpfb-characters.blend`. Both studios and all 17 garment libraries are below 100 MB; the largest garment library is 40.9 MB. Relative library paths keep the project portable. Preserve the directory layout when copying the project. Animation sources prepared through the shared template retain these clothing and character links.

`assets/wardrobe/libraries.json` maps garments and characters to fitted mesh datablocks. To edit a garment asset, append its named collection into a Blender scene. The collection includes fitted geometry, vertex groups, materials, and packed textures. Edit the mesh while preserving its vertex groups, then save the collection to its library file. Reload that library in the studio to review the result. The native studio retains the character rigs and animation controls.

Garments follow the deformation skeleton. Their fitting and masks reduce body intersections; cloth simulation and individual motion-by-motion costume refinement remain additional authoring work. Pole practice uses covered outfits; leg grip technique needs individual review.

## Rebuilding

Use Blender 5.2 with MPFB enabled and the selected assets installed:

```sh
blender --background --python-exit-code 1 --python scripts/build_wardrobe.py
```

The default source is the MPFB library under `Documents/blender/mpfb/data`. Pass `-- /path/to/mpfb/data` to choose another library. Original selected asset folders are copied into `assets/mpfb/`; the builder fits them onto the standard bodies, assigns glTF-compatible PBR materials, packs garment textures into individual clothing libraries, links those libraries into both studios, and exports each outfit under `models/wardrobe/`. Character skin, eye, and hair textures remain packed in the studios. The builder enforces the 100 MB limit for studios and garment libraries. Run this after studio reconstruction. The shared deformation skeleton and animation files retain their existing structure.

For selected runtime exports, add `-- --profiles practice pole --characters woman`. The native studios and clothing libraries receive the full wardrobe configuration.

To split an existing fitted wardrobe into libraries, use `blender --factory-startup --background --python-exit-code 1 --python scripts/link_wardrobe.py`. This updates both studios and checks sampled garment positions before and after linking.

Validate clothing links, portable paths, library rebuilding, and the size limit with `blender --factory-startup --background --python-exit-code 1 --python scripts/link_wardrobe.test.py`. The existing `scripts/wardrobe.test.py` checks outfit selection, packed textures, and coverage masks.

## Attribution

Original asset headers and material files retain their licenses. [MakeHuman's asset pack index](https://static.makehumancommunity.org/assets/assetpacks.html) documents the system and community collections. `assets/mpfb/attribution.json` lists the bundled assets, authors, licenses, and export changes.

- MakeHuman system assets, skin, eyes, hair, teeth, tongue, casual outfits, elegant suit, and system shoes: Data Collection AB, Joel Palmius, and Jonas Hauquier; [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/), explicitly released in September 2020 in the source headers.
- Full-skirt camisole dress, halter dress, navy suit, knitted top, wool pants, and ballet flats: Margaret Toigo (MRT); [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).
- Flapper Dress 1: AEthelraed Unraed; [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).
- Sleeveless shirt and tennis shoes: punkduck; [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).
- Ballet Dress The Swan: Mindfront (Sweden); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Adaptations consist of fitting, interpolated deformation weights, coverage masks, PBR material conversion, and Blender/GLB packaging. The navy suit's tie geometry is removed for the plain-shirt outfits. The original copied asset files accompany the exports. Character and wardrobe credit is available through the demo's source inventory. Rebuild distribution notices with `python scripts/license_notices.py`, then embed them in the native assets with `blender --factory-startup --background --python-exit-code 1 --python scripts/embed_blend_licenses.py` after changing the wardrobe.
