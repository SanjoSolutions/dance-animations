"""Merge native sampler results and retain original export provenance."""
from array import array
from collections import Counter
import json
from pathlib import Path
import sys
from import_assets import read_glb, write_glb, retrieve_playback_variants, STYLES

ROOT = Path(__file__).resolve().parents[1]


def preserve_duration(path, duration):
    document, binary = read_glb(path)
    maximum = max(document['accessors'][sampler['input']]['max'][0]
                  for sampler in document['animations'][0]['samplers'])
    if maximum < duration:
        sampler = document['animations'][0]['samplers'][0]
        accessor = document['accessors'][sampler['output']]
        view = document['bufferViews'][accessor['bufferView']]
        offset = view.get('byteOffset',0) + accessor.get('byteOffset',0)
        width = 4 if accessor['type'] == 'VEC4' else 3
        key = binary[offset:offset+width*4]
        packed = bytearray(binary)
        def append(values, kind, width):
            view = len(document['bufferViews'])
            document['bufferViews'].append(dict(buffer=0,byteOffset=len(packed),byteLength=len(values)))
            packed.extend(values)
            index = len(document['accessors'])
            record = dict(bufferView=view,componentType=5126,type=kind,count=len(values)//(width*4))
            if kind == 'SCALAR':record.update(min=[0],max=[duration])
            document['accessors'].append(record)
            return index
        sampler['input'] = append(array('f',[0,duration]).tobytes(),'SCALAR',1)
        sampler['output'] = append(key+key,accessor['type'],width)
        write_glb(path,document,bytes(packed))


def main(results):
    catalog = json.loads((ROOT/'catalog.json').read_text())
    entries = {variant['id']:variant for entry in catalog['animations']
               for variant in retrieve_playback_variants(entry)}
    failures = []
    for path in results:
        result = json.loads(Path(path).read_text())
        failures.extend(result['failures'])
        for entry in result['animations']:
            entry['duration'] = max(entry['duration'],1/24)
            preserve_duration(ROOT/entry['file'],entry['duration'])
            for variant in retrieve_playback_variants(entry):
                previous = entries.get(variant['id'],{})
                for key in ('originalExport','originalExportSha256'):
                    if previous.get(key):variant[key] = previous[key]
                entries[variant['id']] = variant
    inventory = json.loads((ROOT/'source-inventory.json').read_text())
    sources = {entry['sourceFile']:entry for entry in entries.values() if entry['sourceFile']}
    for record in inventory:
        record['runtimeExport'] = sources.get(record['file'],{}).get('file')
    available = Counter(entry['style'] for entry in entries.values())
    authored = Counter(record['style'] for record in inventory)
    catalog.update(animations=sorted(entries.values(),key=lambda entry:(entry['style'],entry['id'])),
        sourceCount=len(inventory),sourceOnlyCount=sum(record['runtimeExport'] is None for record in inventory),
        styles=[dict(id=style,label=STYLES.get(style,style.capitalize()),playable=available[style],sources=authored[style])
                for style in sorted(set(available)|set(authored),key=lambda style:STYLES.get(style,style))])
    (ROOT/'catalog.json').write_text(json.dumps(catalog,indent=2)+'\n')
    (ROOT/'source-inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
    print(f'{len(entries)} playable clips, {len(inventory)} sources, {catalog["sourceOnlyCount"]} pending; {len(failures)} sampler failures.')
    if failures:raise RuntimeError(failures)


if __name__ == '__main__':
    main(sys.argv[1:])
