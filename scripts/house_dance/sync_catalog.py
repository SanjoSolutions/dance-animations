"""Reconcile the complete validated House repertoire and retain imported provenance."""
import hashlib
import json
from pathlib import Path
import shutil

from repertoire import CATALOG

ROOT = Path(__file__).resolve().parents[2]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_style(existing, replacements):
    by_name = {entry['id']: entry for entry in replacements}
    previous_names = {entry['id'] for entry in existing}
    result = [by_name[entry['id']] if entry['style'] == 'house_dance' else entry for entry in existing]
    boundary = max(index for index, entry in enumerate(result) if entry['style'] == 'house_dance') + 1
    result[boundary:boundary] = sorted((entry for entry in replacements if entry['id'] not in previous_names),
                                     key=lambda entry: entry['id'])
    return result


def main():
    catalog_path, inventory_path = ROOT / 'catalog.json', ROOT / 'source-inventory.json'
    catalog = json.loads(catalog_path.read_text())
    inventory = json.loads(inventory_path.read_text())
    previous_entries = {entry['id']: entry for entry in catalog['animations']}
    previous_sources = {entry['id']: entry for entry in inventory}
    entries, sources, reviews = [], [], []
    evidence = ROOT / 'docs/house_dance_review'
    (evidence / 'clips').mkdir(parents=True, exist_ok=True)
    inspection = json.loads((ROOT / '.cache/house/visual-inspection.json').read_text())
    transitions = json.loads((ROOT / '.cache/house/transitions.json').read_text())
    assert transitions['passed'] and len(transitions['endpoints']) == 16
    for name, checksum in transitions['exports'].items():
        assert digest(ROOT / '.cache/house/candidates' / (name + '.glb')) == checksum, name
    shutil.copyfile(ROOT / '.cache/house/transitions.json', evidence / 'transitions.json')
    for phrase, module in CATALOG:
        for actor in ('man', 'woman'):
            name = f'house_{actor}_{phrase.name}'
            final = json.loads((ROOT / '.cache/house/finalized' / (name + '.json')).read_text())
            native = json.loads((ROOT / '.cache/house/validated' / (name + '.json')).read_text())
            runtime = json.loads((ROOT / '.cache/house/runtime' / (name + '.json')).read_text())
            visual = json.loads((ROOT / '.cache/house/visual' / name / 'coverage.json').read_text())
            assert native['passed'] and runtime['passed'], name
            assert digest(ROOT / final['sourceFile']) == final['sourceSha256'], name
            assert digest(ROOT / final['exportFile']) == native['exportSha256'] == runtime['exportSha256'] == visual['exportSha256'], name
            assert native['sourceSha256'] == runtime['sourceSha256'] == final['candidateSourceSha256'], name
            for filename, checksum in native['recipeSha256'].items():
                assert digest(Path(__file__).parent / filename) == checksum, (name, filename)
            assert visual.get('motion') and len(visual['frames']) == 33, name
            assert inspection[name]['exportSha256'] == native['exportSha256'], name
            assert native['skin']['maximumPalmGap'] is None or native['skin']['maximumPalmGap'] <= .012, name
            if native['sourceSeam']['loop']:
                assert native['sourceSeam']['positionError'] < .003 and native['sourceSeam']['velocityError'] < .1, name
            visual.update(inspection=inspection[name], video=f'media/{name}.webm', contactSheet=f'media/{name}.jpg')
            review = dict(native, sourceSha256=final['sourceSha256'], sourceFile=final['sourceFile'],
                          exportFile=final['exportFile'], sourceBytes=final['sourceBytes'],
                          relocation=final, runtime=runtime, visualReview=visual)
            (evidence / 'clips' / (name + '.json')).write_text(json.dumps(review, indent=2)+'\n')
            previous = previous_entries.get(name, {})
            entry = dict(previous, id=name, style='house_dance', label=phrase.name.replace('_',' ').capitalize() + ' · ' + actor.capitalize(),
                         performers=[actor], duration=4, file=final['exportFile'], sourceFile=final['sourceFile'],
                         sourceSha256=final['sourceSha256'], exportSha256=native['exportSha256'],
                         animationName=name+'.baked', status='Native deformation bake',
                         studyStatus='Procedural study; local motion and surface review',
                         loop=module!='transitions', tempo=120, beats=8, sampleRate=48,
                         reviewFile=(evidence / 'clips' / (name+'.json')).relative_to(ROOT).as_posix())
            if 'originalExport' not in entry:
                entry.update(originalExport=None, originalExportSha256=None)
            original = dict(previous_sources.get(name, {}))
            original.setdefault('originalSha256', original.get('sha256'))
            original.setdefault('previousSourceSha256', original.get('sha256'))
            original.update(id=name, style='house_dance', file=final['sourceFile'], sha256=final['sourceSha256'],
                            bytes=final['sourceBytes'], runtimeExport=final['exportFile'],
                            studyStatus=entry['studyStatus'], provenance='Original procedural House practice phrase; restored native IK recipe')
            original.setdefault('original', None)
            entries.append(entry); sources.append(original); reviews.append(review)
    assert len(entries)==90 and len({entry['id'] for entry in entries})==90
    catalog['animations'] = replace_style(catalog['animations'], entries)
    inventory = replace_style(inventory, sources)
    next(style for style in catalog['styles'] if style['id']=='house_dance').update(playable=90, sources=90)
    catalog['sourceCount'] = len(inventory)
    catalog['sourceOnlyCount'] = sum(entry['runtimeExport'] is None for entry in inventory)
    catalog_path.write_text(json.dumps(catalog, indent=2)+'\n')
    inventory_path.write_text(json.dumps(inventory, indent=2)+'\n')
    summary = dict(clips=90, phrases=45, performers=['man','woman'], frames=[0,96], effectiveFrameRate=24,
                   runtimeSampleRate=48, duration=4, tempo=120, beats=8,
                   maximumSkinPenetration=max(0, -min(review['skin']['minimumHeight'] for review in reviews)),
                   maximumSupportGap=max(review['skin']['maximumSupportGap'] for review in reviews),
                   maximumPalmGap=max(review['skin']['maximumPalmGap'] or 0 for review in reviews),
                   maximumBakePositionError=max(review['bake']['maximumPositionError'] for review in reviews),
                   maximumBakeAngularError=max(review['bake']['maximumAngularError'] for review in reviews),
                   maximumRuntimePositionError=max(review['runtime']['maximumPositionError'] for review in reviews),
                   maximumRelocatedPlaybackError=max(review['relocation']['freshRelocatedPlaybackError'] for review in reviews),
                   totalSourceBytes=sum(review['sourceBytes'] for review in reviews),
                   passed=True, status='Local procedural repertoire review', publication='Awaiting local quality review')
    (evidence / 'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary), flush=True)


if __name__=='__main__':
    main()
