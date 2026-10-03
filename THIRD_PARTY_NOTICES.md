# Licenses and credits

Original project content, including the dance motions, demo, and project-specific
helpers, uses the [MIT-0 license adapted to content](LICENSE). This is the
requested MIT-0 wording with “Content” in place of “Software.” The third-party
components below retain their respective licenses, including within Blender
files, exported character models, and the compiled website.

## Characters and clothing

MakeHuman/MPFB's hm08 base mesh and system assets were explicitly released under
CC0 in September 2020 by Data Collection AB, Joel Palmius, and Jonas Hauquier.
The original base-mesh notice is in `licenses/makehuman-base-notice.txt`.
Original garment and material headers remain under `assets/mpfb/`.

`assets/mpfb/attribution.json` lists each selected asset, its author, license,
source, and modifications. [The wardrobe guide](docs/wardrobe.md) identifies
the outfits. The CC BY assets are:

| Asset | Author | License | Source |
| --- | --- | --- | --- |
| Sleeveless Shirt | punkduck | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) | [MakeHuman asset packs](https://static.makehumancommunity.org/assets/assetpacks.html) |
| TennisShoes | punkduck | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) | [MakeHuman asset packs](https://static.makehumancommunity.org/assets/assetpacks.html) |
| Ballet Dress The Swan | Mindfront (Sweden) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | [MakeHuman asset packs](https://static.makehumancommunity.org/assets/assetpacks.html) |

Adaptations include fitting to the standard characters, deformation weights,
coverage masks, PBR material conversion, and Blender/glTF packaging. The navy
suit's tie geometry was removed. Full-length practice garments include added
body coverage masks. Preserve the relevant author, source, license, and change
notices when redistributing character or wardrobe assets. The project license
covers the project's contributions; these third-party asset licenses continue
to apply. CC0 and CC BY legal texts accompany the website under
`public/third-party/`.

## Blender code

- `scripts/blender/extensions/game_rig_tools/` is Game Rig Tools, maintained
  upstream by TinkerBoi/CGDive, with contributions identified in its sources and
  changelog. Its manifest specifies GPL-2.0-or-later; its supplied LICENSE is
  GPL version 3. This project distributes that fork under GPL version 3, retaining
  the original manifest, complete source, license, and modification history.
  [Fork details](scripts/blender/extensions/game_rig_tools/NOTICE.md) describe
  the adaptations and installation archive.
- The embedded `Human.rigify_ui.py` scripts in the studios and character library derive from
  Blender Rigify, copyright 2010–2023 Blender Foundation and its contributors,
  under GPL-2.0-or-later. Exact readable copies are in `licenses/rigify/`,
  with their GPL license under `public/third-party/`. This license applies to
  the embedded code; character geometry and dance motion have their own terms.
- MPFB and Blender are authoring dependencies installed separately. Their
  installed source and license notices accompany their distributions. NumPy
  is an optional maintenance dependency installed through pip with its own
  license notices.

## Website and build dependencies

Three.js, Bootstrap, and the embedded meshoptimizer 0.22 decoder use MIT.
`public/third-party/npm-notices.txt` contains complete copyright and license
notices from the installed npm dependency tree, including build dependencies
and the decoder's version-specific license. The generated website serves these
notices and [its credits page](public/licenses.html) alongside the bundles.

Run `python scripts/license_notices.py` after dependency or wardrobe changes.
It requires a license notice for every installed package and records original
asset headers in `public/third-party/asset-notices.txt`. `npm run build` runs
this step before packaging the website.
