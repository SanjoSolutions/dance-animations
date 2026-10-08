/** Check the four directed transitions against their actual runtime position clips. */
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { AnimationMixer, LoopOnce, Quaternion, Vector3 } from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import { clone } from 'three/addons/utils/SkeletonUtils.js';
import { bindClip } from '../../src/clip-binding.ts';

globalThis.createImageBitmap = async () => ({ width: 1, height: 1, close() {} });
globalThis.self = globalThis;
const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
async function load(path) {
  const bytes = await readFile(path);
  return loader.parseAsync(bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength), '');
}
const transitions = [
  ['relaxed_to_ready', 'relaxed_position', 'ready_position'],
  ['ready_to_relaxed', 'ready_position', 'relaxed_position'],
  ['ready_to_low', 'ready_position', 'low_position'],
  ['low_to_ready', 'low_position', 'ready_position'],
];
const endpoints = [];
const exports = {};
for (const actor of ['man', 'woman']) {
  const template = await load(`models/mpfb-${actor}.glb`);
  async function sample(phrase, time) {
    const name = `house_${actor}_${phrase}`;
    const file = `.cache/house/candidates/${name}.glb`;
    exports[name] = createHash('sha256').update(await readFile(file)).digest('hex');
    const model = clone(template.scene);
    const clip = await bindClip(await load(file), new Map([[actor, model]]));
    const mixer = new AnimationMixer(model);
    const action = mixer.clipAction(clip);
    action.setLoop(LoopOnce, 1); action.clampWhenFinished = true; action.play();
    mixer.setTime(time); model.updateMatrixWorld(true);
    const bones = new Map();
    model.traverse(node => {
      if (node.isBone && node.name.startsWith('DEF-')) {
        bones.set(node.name, {
          position: new Vector3().setFromMatrixPosition(node.matrixWorld),
          rotation: node.getWorldQuaternion(new Quaternion()).normalize(),
        });
      }
    });
    mixer.stopAllAction(); mixer.uncacheRoot(model);
    return bones;
  }
  for (const [transition, first, last] of transitions) {
    for (const [position, time] of [[first, 0], [last, 4]]) {
      const expected = await sample(position, 0);
      const actual = await sample(transition, time);
      let maximumPositionError = 0, maximumAngularError = 0;
      for (const [name, bone] of expected) {
        maximumPositionError = Math.max(maximumPositionError, bone.position.distanceTo(actual.get(name).position));
        maximumAngularError = Math.max(maximumAngularError, bone.rotation.angleTo(actual.get(name).rotation));
      }
      const passed = maximumPositionError < .0001 && maximumAngularError < .001;
      endpoints.push({ actor, transition, position, time, bones: actual.size, maximumPositionError, maximumAngularError, passed });
    }
  }
}
await mkdir('.cache/house', { recursive: true });
await writeFile('.cache/house/transitions.json', JSON.stringify({ exports, endpoints, passed: endpoints.every(item => item.passed) }, null, 2) + '\n');
console.log(JSON.stringify(endpoints));
assert.ok(endpoints.every(item => item.passed), 'Transition endpoints match their named positions');
