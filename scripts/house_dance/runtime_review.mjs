/** Compare exported House animation tracks with fresh native deformation samples. */
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile, readdir, mkdir, writeFile } from 'node:fs/promises';
import { AnimationMixer, LoopOnce, Vector3 } from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import { clone } from 'three/addons/utils/SkeletonUtils.js';
import { bindClip } from '../../src/clip-binding.ts';

globalThis.createImageBitmap = async () => ({ width:1, height:1, close() {} });
globalThis.self = globalThis;
const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
const digest = bytes => createHash('sha256').update(bytes).digest('hex');
async function load(path) {
  const bytes = await readFile(path);
  return loader.parseAsync(bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength),'');
}
const templates = new Map(await Promise.all(['man','woman'].map(async actor => [actor,await load(`models/mpfb-${actor}.glb`)])));
const requested = process.argv.slice(2);
const names = requested.length ? requested : (await readdir('.cache/house/runtime-reference')).filter(name=>name.endsWith('.json')).map(name=>name.slice(0,-5)).sort();
await mkdir('.cache/house/runtime', { recursive:true });
let failed = 0;
for (const name of names) {
  const reference = JSON.parse(await readFile(`.cache/house/runtime-reference/${name}.json`,'utf8'));
  const native = JSON.parse(await readFile(`.cache/house/validated/${name}.json`,'utf8'));
  const source = await readFile(`.cache/house/candidates/sources/${name}.blend`);
  assert.equal(digest(source),reference.sourceSha256,name);
  const file = `.cache/house/candidates/${name}.glb`;
  assert.equal(digest(await readFile(file)),native.exportSha256,name);
  const actor = name.split('_')[1];
  const animation = await load(file);
  assert.equal(animation.animations[0].name,name+'.baked');
  const model = clone(templates.get(actor).scene);
  const clip = await bindClip(animation,new Map([[actor,model]]));
  assert.equal(clip.duration,4,name);
  const mixer = new AnimationMixer(model);
  const action = mixer.clipAction(clip);action.setLoop(LoopOnce,1);action.clampWhenFinished=true;action.play();
  const bones = reference.bones.map(bone => {
    const node = model.getObjectByName(bone);
    assert.ok(node,`${name}: ${bone}`);
    return node;
  });
  let maximumPositionError = 0;
  let worst;
  for (const [index,frame] of reference.frames.entries()) {
    mixer.setTime(frame/24);model.updateMatrixWorld(true);
    for (const [boneIndex,bone] of bones.entries()) {
      assert.ok(bone.matrixWorld.elements.every(Number.isFinite),name);
      const position = new Vector3().setFromMatrixPosition(bone.matrixWorld);
      const error = position.distanceTo(new Vector3(...reference.positions[index][boneIndex]));
      if (error>maximumPositionError) {maximumPositionError=error;worst={frame,bone:bone.name};}
    }
  }
  const report = {id:name,passed:maximumPositionError<.005,sourceSha256:reference.sourceSha256,
    exportSha256:native.exportSha256,modelSha256:digest(await readFile(`models/mpfb-${actor}.glb`)),
    frames:reference.frames.length,bones:bones.length,tracks:clip.tracks.length,duration:clip.duration,
    maximumPositionError,worst,tolerance:.005,units:'meters'};
  await writeFile(`.cache/house/runtime/${name}.json`,JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report));
  if (!report.passed) failed++;
  mixer.stopAllAction();mixer.uncacheRoot(model);
}
process.exitCode = failed ? 1 : 0;
