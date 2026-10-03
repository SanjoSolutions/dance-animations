"""Import the a-game dance library, retaining source identity and study status.

Usage: python scripts/import_assets.py ../sanjo-solutions/apps/a-game
Runtime GLBs contain their original sampled transforms and no character meshes.
"""
from __future__ import annotations

import argparse
from collections import Counter
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import struct

ROOT = Path(__file__).resolve().parents[1]
STYLES = {
    'afro_house': 'Afro house', 'amapiano': 'Amapiano',
    'american_bolero': 'American bolero', 'bachata': 'Bachata',
    'ballet': 'Ballet', 'ballroom_samba': 'Ballroom samba',
    'belly': 'Belly dance', 'bhangra': 'Bhangra', 'blues': 'Blues',
    'bollywood': 'Bollywood', 'boogie_woogie': 'Boogie-woogie',
    'boot_scootin': 'Boot scootin’ boogie', 'brazilian_zouk': 'Brazilian zouk',
    'breaking': 'Breaking', 'cha_cha_slide': 'Cha Cha Slide',
    'chicken_dance': 'Chicken dance', 'contemporary': 'Contemporary',
    'country_swing': 'Country swing', 'country_two_step': 'Country two-step',
    'country_waltz': 'Country waltz', 'cross_step_waltz': 'Cross-step waltz',
    'cumbia': 'Cumbia', 'cupid_shuffle': 'Cupid shuffle',
    'cutting_shapes': 'Cutting shapes', 'dancehall': 'Dancehall',
    'disco_freestyle': 'Disco freestyle', 'discofox': 'Discofox',
    'electric_slide': 'Electric slide', 'flamenco': 'Flamenco',
    'forro': 'Forró', 'foxtrot': 'Foxtrot', 'funky_chicken': 'Funky chicken',
    'fusion': 'Fusion', 'gogo': 'Go-go', 'hip_hop': 'Hip hop',
    'house_dance': 'House', 'irish_stepdance': 'Irish stepdance',
    'jazz': 'Jazz', 'jive': 'Jive', 'kizomba': 'Kizomba',
    'kpop_neon': 'K-pop Neon Practice', 'krump': 'Krump', 'naija': 'Naija',
    'lambada': 'Lambada', 'litefeet': 'Litefeet', 'locking': 'Locking',
    'lyrical': 'Lyrical', 'macarena': 'Macarena', 'mashed_potato': 'Mashed potato',
    'mazurka': 'Mazurka', 'merengue': 'Merengue', 'modern_jive': 'Modern jive',
    'musical_theatre': 'Musical theatre', 'new_york_hustle': 'New York hustle',
    'nightclub_two_step': 'Nightclub two-step', 'partner_cha_cha': 'Partner cha-cha',
    'partner_paso_doble': 'Partner paso doble', 'partner_polka': 'Polka',
    'partner_rumba': 'Partner rumba', 'partner_schottische': 'Schottische', 'partner_mambo': 'Mambo',
    'playful_freestyle': 'Playful freestyle', 'pole_dance': 'Pole dance',
    'popping': 'Popping', 'quickstep': 'Quickstep', 'rock_n_roll': 'Rock ’n’ roll',
    'robot': 'Robot', 'salsa': 'Salsa', 'samba_de_gafieira': 'Samba de gafieira',
    'semba': 'Semba', 'shuffle': 'Shuffle', 'slow_dance': 'Slow dance',
    'slow_waltz': 'Slow waltz', 'solo_cha_cha': 'Solo cha-cha',
    'solo_charleston': 'Charleston', 'solo_disco_dance': 'Disco',
    'solo_jazz': 'Solo jazz', 'solo_jive': 'Solo jive', 'solo_monkey': 'Monkey',
    'solo_paso_doble': 'Paso doble', 'solo_rumba': 'Solo rumba',
    'solo_samba': 'Solo samba', 'swing': 'Swing', 'tango': 'Tango',
    'tap': 'Tap', 'triple_two_step': 'Triple two-step', 'tutting': 'Tutting',
    'twist': 'Twist', 'urban_kiz': 'Urban kiz', 'viennese_waltz': 'Viennese waltz',
    'vogue': 'Vogue', 'voguing': 'Voguing', 'waacking': 'Waacking',
    'watusi': 'Watusi', 'wobble': 'Wobble',
}


def identity(name):
    return re.sub(r'(?:[._]baked)(?:_[a-f0-9]+)?$', '', name)


def style_for(name):
    name = re.sub(r'^(man|woman|male|female)_', '', name.lower())
    if name == 'pole_dance_chopper_to_crucifix':
        return None
    for key in sorted(STYLES, key=len, reverse=True):
        if name == key or name.startswith(key + '_'):
            return key
    if name.startswith('house_'):
        return 'house_dance'
    return None


def read_glb(path):
    data = path.read_bytes()
    if data[:4] != b'glTF':
        raise ValueError(f'Hydrate the Git LFS object: {path}')
    document = json.loads(data[20:20 + struct.unpack_from('<I', data, 12)[0]])
    position = 20 + struct.unpack_from('<I', data, 12)[0]
    binary = data[position + 8:] if position < len(data) else b''
    return document, binary


def write_glb(path, document, binary):
    binary += b'\0' * (-len(binary) % 4)
    document['buffers'] = [{'byteLength': len(binary)}]
    encoded = json.dumps(document, separators=(',', ':')).encode()
    encoded += b' ' * (-len(encoded) % 4)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(struct.pack('<4sII', b'glTF', 2, 28 + len(encoded) + len(binary))
                    + struct.pack('<I4s', len(encoded), b'JSON') + encoded
                    + struct.pack('<I4s', len(binary), b'BIN\0') + binary)


def compact_buffers(document, binary):
    """Copy only referenced accessor and image bytes, with deterministic indices."""
    old_accessors = document.pop('accessors', [])
    old_views = document.pop('bufferViews', [])
    accessors, views, packed = [], [], bytearray()
    mapped_accessors, mapped_views = {}, {}

    def view(index):
        if index not in mapped_views:
            item = copy.deepcopy(old_views[index])
            offset, length = item.get('byteOffset', 0), item['byteLength']
            packed.extend(b'\0' * (-len(packed) % 4))
            item.update(buffer=0, byteOffset=len(packed))
            packed.extend(binary[offset:offset + length])
            mapped_views[index] = len(views)
            views.append(item)
        return mapped_views[index]

    def accessor(index):
        if index not in mapped_accessors:
            item = copy.deepcopy(old_accessors[index])
            if 'bufferView' in item:
                item['bufferView'] = view(item['bufferView'])
            if 'sparse' in item:
                for key in ('indices', 'values'):
                    item['sparse'][key]['bufferView'] = view(item['sparse'][key]['bufferView'])
            mapped_accessors[index] = len(accessors)
            accessors.append(item)
        return mapped_accessors[index]

    for animation in document.get('animations', []):
        for sampler in animation['samplers']:
            for key in ('input', 'output'):
                sampler[key] = accessor(sampler[key])
    for mesh in document.get('meshes', []):
        for primitive in mesh['primitives']:
            primitive['attributes'] = {key: accessor(value) for key, value in primitive['attributes'].items()}
            if 'indices' in primitive:
                primitive['indices'] = accessor(primitive['indices'])
    for skin in document.get('skins', []):
        if 'inverseBindMatrices' in skin:
            skin['inverseBindMatrices'] = accessor(skin['inverseBindMatrices'])
    for image in document.get('images', []):
        if 'bufferView' in image:
            image['bufferView'] = view(image['bufferView'])
    document.update(accessors=accessors, bufferViews=views)
    return bytes(packed)


def export_animation(path, document, binary, animation, destination):
    result = copy.deepcopy(document)
    result['animations'] = [copy.deepcopy(animation)]
    for key in ('meshes', 'skins', 'materials', 'images', 'textures', 'samplers',
                'extensionsUsed', 'extensionsRequired', 'extras'):
        result.pop(key, None)
    for node in result.get('nodes', []):
        for key in ('mesh', 'skin', 'weights', 'extras'):
            node.pop(key, None)
    for scene in result.get('scenes', []):
        scene.pop('extras', None)
    # Shape tracks belong to game-specific attachments; base dance motion is skeletal.
    result['animations'][0]['channels'] = [channel for channel in animation['channels']
                                           if channel['target']['path'] != 'weights']
    binary = compact_buffers(result, binary)
    write_glb(destination, result, binary)


def participants(document, animation):
    parents = {child: index for index, node in enumerate(document['nodes']) for child in node.get('children', [])}
    performers = set()
    for channel in animation['channels']:
        index = channel['target']['node']
        while True:
            name = document['nodes'][index].get('name', '')
            if name.startswith('Man.') or name.startswith('Man_'):
                performers.add('man')
                break
            if name.startswith(('Woman.', 'Woman_', 'Human.')):
                performers.add('woman')
                break
            if index not in parents:
                break
            index = parents[index]
    return sorted(performers)


def retrieve_playback_variants(entry):
    """Expose Jazz's shared-origin solo action slots as character choices."""
    if entry['style'] == 'jazz' and len(entry['performers']) > 1:
        # The Man choice retains existing library URLs.
        return [dict(entry, id=entry['id'] if actor == 'man' else f'{entry["id"]}_{actor}',
                     label=f'{entry["label"]} · {actor.capitalize()}', performers=[actor])
                for actor in entry['performers']]
    else:
        return [entry]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    args = parser.parse_args()
    source = args.source.resolve()
    activity_document = json.loads((source / 'playground/activity_import/dance_activities.json').read_text())
    activities = {entry['id']: entry for entry in activity_document['activities']}
    sources = {}
    inventory = []
    for path in sorted((source / 'animations').rglob('*.blend')):
        style = style_for(path.stem)
        if style:
            destination = ROOT / 'animations' / style / 'sources' / path.name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)
            record = {'id': path.stem, 'style': style, 'file': destination.relative_to(ROOT).as_posix(),
                      'original': path.relative_to(source).as_posix(),
                      'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'bytes': path.stat().st_size}
            inventory.append(record)
            sources[path.stem] = record
    # Latest registered runtime exports win over archived or provisional versions.
    locations = ['animations', 'docs/animation_work_status', 'output', 'models/player/animation_updates']
    entries = {}
    skipped = []
    for directory in locations:
        for path in sorted((source / directory).rglob('*.glb')):
            document, binary = read_glb(path)
            for animation in document.get('animations', []):
                name = identity(animation.get('name', path.stem))
                style = style_for(name)
                if style:
                    actors = participants(document, animation)
                    if actors:
                        destination = ROOT / 'animations' / style / f'{name}.glb'
                        export_animation(path, document, binary, animation, destination)
                        activity = activities.get(name)
                        source_record = sources.get(name)
                        inputs = [document['accessors'][sampler['input']] for sampler in animation['samplers']]
                        duration = max(item.get('max', [0])[0] for item in inputs)
                        label = activity['name'] if activity else name.replace('_', ' ').capitalize()
                        if len(actors) == 1:
                            label += ' · ' + actors[0].capitalize()
                        entries[name] = {'id': name, 'style': style, 'label': label, 'performers': actors,
                            'duration': duration, 'file': destination.relative_to(ROOT).as_posix(),
                            'sourceFile': source_record['file'] if source_record else None,
                            'originalExport': path.relative_to(source).as_posix(),
                            'originalExportSha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                            'animationName': animation.get('name'),
                            'status': 'Game export' if directory == 'models/player/animation_updates' else 'Provisional export'}
                    else:
                        skipped.append({'file': path.relative_to(source).as_posix(), 'animation': name,
                                        'reason': 'Requires another skeleton / retargeting'})
    # The base game library contains the original disco routine.
    path = source / 'models/player/animations.glb'
    document, binary = read_glb(path)
    for animation in document.get('animations', []):
        name = identity(animation.get('name', ''))
        if style_for(name) and name not in entries:
            style = style_for(name)
            destination = ROOT / 'animations' / style / f'{name}.glb'
            export_animation(path, document, binary, animation, destination)
            entries[name] = {'id': name, 'style': style, 'label': name.replace('_', ' ').capitalize(),
                'performers': participants(document, animation), 'duration': max(
                    document['accessors'][s['input']].get('max', [0])[0] for s in animation['samplers']),
                'file': destination.relative_to(ROOT).as_posix(), 'sourceFile': sources.get(name, {}).get('file'),
                'originalExport': path.relative_to(source).as_posix(),
                'originalExportSha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                'animationName': animation.get('name'), 'status': 'Game export'}
    models = {actor: {'file': f'models/mpfb-{actor}.glb',
        'source': f'animations/man_and_woman/shared_scene_data.blend#{actor.capitalize()}.body',
        'mesh': 'Standard MPFB base body'} for actor in ('man', 'woman')}
    for record in inventory:
        record['runtimeExport'] = entries.get(record['id'], {}).get('file')
    entries = {variant['id']: variant for entry in entries.values()
               for variant in retrieve_playback_variants(entry)}
    available = Counter(entry['style'] for entry in entries.values())
    authored = Counter(entry['style'] for entry in inventory)
    styles = [{'id': style, 'label': STYLES[style], 'playable': available[style], 'sources': authored[style]}
              for style in sorted(set(available) | set(authored), key=lambda style: STYLES[style])]
    catalog = {'version': 1, 'sourceRepository': 'https://github.com/SanjoSolutions/sanjo-solutions',
               'sourceCommit': __import__('subprocess').check_output(['git','rev-parse','HEAD'],cwd=source,text=True).strip(),
               'models': models, 'styles': styles,
               'animations': sorted(entries.values(), key=lambda entry: (STYLES[entry['style']], entry['label'])),
               'sourceCount': len(inventory), 'sourceOnlyCount': sum(not entry['runtimeExport'] for entry in inventory)}
    (ROOT / 'catalog.json').write_text(json.dumps(catalog, indent=2) + '\n')
    (ROOT / 'source-inventory.json').write_text(json.dumps(inventory, indent=2) + '\n')
    (ROOT / 'retargeting-needed.json').write_text(json.dumps(skipped, indent=2) + '\n')
    records = ROOT / 'docs' / 'source-review-records'
    records.mkdir(parents=True, exist_ok=True)
    for path in (source / 'docs/animation_work_status').glob('*.md'):
        shutil.copy2(path, records / path.name)
    print(json.dumps({'playableClips': len(entries), 'styles': len(styles), 'editableSources': len(inventory),
                      'sourceOnly': catalog['sourceOnlyCount'], 'retargetingNeeded': len(skipped)}, indent=2))


if __name__ == '__main__':
    main()
