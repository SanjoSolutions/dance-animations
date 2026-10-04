import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { AnimationMixer, Vector3 } from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import { createCharacterPreview } from './character-preview.ts';
import { bindClip } from './clip-binding.ts';
import { retrieveMoves, retrieveVariant } from './moves.ts';

globalThis.createImageBitmap = async () => ({ width: 1, height: 1, close() {} });
globalThis.self = globalThis;
const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
async function load(file) {
  const bytes = await readFile(file);
  return loader.parseAsync(bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength), '');
}

function retrieveHeading(model) {
  const left = model.getObjectByName('DEF-shoulderL').getWorldPosition(new Vector3());
  const right = model.getObjectByName('DEF-shoulderR').getWorldPosition(new Vector3());
  return left.sub(right).cross(new Vector3(0, 1, 0)).normalize();
}

test('Jazz character choices share a heading through holds, steps, kicks, and turns', async () => {
  const catalog = JSON.parse(await readFile('catalog.json', 'utf8'));
  const templates = new Map(await Promise.all(['man', 'woman'].map(async actor =>
    [actor, (await load(catalog.models[actor].file)).scene])));
  for (const move of retrieveMoves(catalog.animations, 'jazz')) {
    const previews = [];
    for (const actor of ['man', 'woman']) {
      const entry = retrieveVariant(move, actor);
      const model = createCharacterPreview(templates.get(actor), entry.previewRotation);
      const clip = await bindClip(await load(entry.file), new Map([[actor, model]]));
      const mixer = new AnimationMixer(model);
      mixer.clipAction(clip).play();
      previews.push({ model, mixer, duration: clip.duration });
    }
    for (const fraction of [0, .25, .5, .75, .99]) {
      for (const preview of previews) {
        preview.mixer.setTime(preview.duration * fraction);
        preview.model.updateMatrixWorld(true);
      }
      const agreement = retrieveHeading(previews[0].model).dot(retrieveHeading(previews[1].model));
      assert.ok(agreement > .99, `${move.id} at ${fraction}: heading agreement ${agreement}`);
      for (const preview of previews) {
        assert.ok(retrieveHeading(preview.model).z > .99, `${move.id} at ${fraction}: forward heading`);
      }
    }
    for (const preview of previews) {
      preview.mixer.stopAllAction();
      preview.mixer.uncacheRoot(preview.model);
    }
  }
});
