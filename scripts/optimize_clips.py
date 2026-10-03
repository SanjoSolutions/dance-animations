"""Compact review clips with a verified bound on every sampled transform.

Translations and scales retain 0.00005 component precision; quaternion
components retain 0.000025 precision. Original Blender keys stay intact.
"""
from concurrent.futures import ProcessPoolExecutor
import copy
import json
from pathlib import Path
import sys
import numpy as np
from import_assets import read_glb,write_glb

ROOT = Path(__file__).resolve().parents[1]


def interpolate(first, last, fractions, rotation):
    if rotation:
        first = first / np.linalg.norm(first)
        last = last / np.linalg.norm(last)
        dot = float(np.dot(first,last))
        if dot < 0:
            last = -last
            dot = -dot
        angle = np.arccos(np.clip(dot,-1,1))
        if angle > 1e-6:
            return (np.sin((1-fractions)*angle)[:,None]*first + np.sin(fractions*angle)[:,None]*last)/np.sin(angle)
    values = (1-fractions[:,None])*first + fractions[:,None]*last
    if rotation:
        values /= np.linalg.norm(values,axis=1)[:,None]
    return values


def reduce_keys(times, values, rotation):
    tolerance = 0.000025 if rotation else 0.00005
    if np.max(np.abs(values-values[0])) <= tolerance:
        return times[[0,-1]],values[[0,0]]
    retained = {0,len(times)-1}
    segments = [(0,len(times)-1)]
    while segments:
        start,end = segments.pop()
        if end > start+1:
            fractions = (times[start+1:end]-times[start])/(times[end]-times[start])
            predicted = interpolate(values[start],values[end],fractions,rotation)
            errors = np.max(np.abs(predicted-values[start+1:end]),axis=1)
            worst = int(np.argmax(errors))
            if errors[worst] > tolerance:
                middle = start+1+worst
                retained.add(middle)
                segments.extend(((start,middle),(middle,end)))
    indices = sorted(retained)
    # Validate the output at every original sample before writing it.
    for start,end in zip(indices,indices[1:]):
        if end > start+1:
            predicted = interpolate(values[start],values[end],(times[start+1:end]-times[start])/(times[end]-times[start]),rotation)
            assert np.max(np.abs(predicted-values[start+1:end])) <= tolerance+1e-7
    return times[indices],values[indices]


def optimize(entry):
    path = ROOT/entry['file']
    document,binary = read_glb(path)
    original_size = path.stat().st_size
    original_accessors = document['accessors']
    original_views = document['bufferViews']
    def retrieve(index):
        accessor = original_accessors[index]
        view = original_views[accessor['bufferView']]
        assert accessor['componentType'] == 5126
        width = {'SCALAR':1,'VEC3':3,'VEC4':4}[accessor['type']]
        return np.frombuffer(binary,dtype='<f4',count=accessor['count']*width,
            offset=view.get('byteOffset',0)+accessor.get('byteOffset',0)).reshape(-1,width).astype(np.float64)
    packed = bytearray();document['accessors']=[];document['bufferViews']=[];shared={}
    def append(values,kind):
        encoded = values.astype('<f4').tobytes()
        signature = kind,encoded
        if signature not in shared:
            index = len(document['accessors']);view=len(document['bufferViews'])
            document['bufferViews'].append(dict(buffer=0,byteOffset=len(packed),byteLength=len(encoded)))
            record=dict(bufferView=view,componentType=5126,type=kind,count=len(values))
            if kind=='SCALAR':record.update(min=[float(values.min())],max=[float(values.max())])
            document['accessors'].append(record);packed.extend(encoded);shared[signature]=index
        return shared[signature]
    animation=document['animations'][0]
    samplers=[]
    for channel in animation['channels']:
        original=animation['samplers'][channel['sampler']]
        times=retrieve(original['input']).ravel();values=retrieve(original['output'])
        if entry['status']=='Saved-source draft preview' and original.get('interpolation','LINEAR')=='LINEAR' and len(times)>2:
            times,values=reduce_keys(times,values,channel['target']['path']=='rotation')
        sampler=dict(original,input=append(times.reshape(-1,1),'SCALAR'),output=append(values,original_accessors[original['output']]['type']))
        channel['sampler']=len(samplers);samplers.append(sampler)
    animation['samplers']=samplers
    # Keep targets and their complete ancestry. Empty export markers add no motion.
    parents={child:index for index,node in enumerate(document['nodes']) for child in node.get('children',[])}
    required=set()
    for channel in animation['channels']:
        index=channel['target']['node']
        while index is not None and index not in required:
            required.add(index);index=parents.get(index)
    mapping={old:new for new,old in enumerate(sorted(required))}
    nodes=[]
    for index in sorted(required):
        node=copy.deepcopy(document['nodes'][index])
        if 'children' in node:node['children']=[mapping[child] for child in node['children'] if child in required]
        nodes.append(node)
    document['nodes']=nodes
    for channel in animation['channels']:channel['target']['node']=mapping[channel['target']['node']]
    for scene in document['scenes']:scene['nodes']=[mapping[index] for index in scene['nodes'] if index in required]
    temporary=path.with_suffix('.glb.tmp')
    write_glb(temporary,document,bytes(packed))
    temporary.replace(path)
    return original_size,path.stat().st_size


def main():
    catalog=json.loads((ROOT/'catalog.json').read_text());entries=catalog['animations']
    if '--jobs' in sys.argv:
        identifiers=set(json.loads(Path(sys.argv[sys.argv.index('--jobs')+1]).read_text()))
        entries=[entry for entry in entries if entry['id'] in identifiers]
    elif '--start' in sys.argv:entries=entries[int(sys.argv[sys.argv.index('--start')+1]):]
    elif len(sys.argv)>1:entries=[entry for entry in entries if entry['id'] in sys.argv[1:]]
    before=after=0
    with ProcessPoolExecutor(max_workers=4) as pool:
        for index,(original,current) in enumerate(pool.map(optimize,entries),1):
            before+=original;after+=current
            if index%100==0:print(f'Compacted {index}/{len(entries)} clips: {before/1048576:.1f} → {after/1048576:.1f} MiB',flush=True)
    print(f'Compact GLBs: {before/1048576:.1f} → {after/1048576:.1f} MiB',flush=True)


if __name__=='__main__':main()
