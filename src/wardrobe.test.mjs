import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { AnimationMixer, Box3, Vector3 } from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import { NodeIO } from '@gltf-transform/core';
import { retrieveCharacterFile } from './wardrobe.ts';
import { bindClip } from './clip-binding.ts';

globalThis.createImageBitmap = async () => ({ width: 1, height: 1, close() {} });
globalThis.self = globalThis;
const catalog = JSON.parse(await readFile('catalog.json', 'utf8'));
const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
const io = new NodeIO();
async function load(file) {
  const bytes = await readFile(file);
  return loader.parseAsync(bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength), '');
}

test('every style selects clothing, and street, ballroom, and ballet use distinct outfits', () => {
  for (const style of catalog.styles) for (const actor of ['man', 'woman']) {
    assert.match(retrieveCharacterFile(catalog, style.id, actor), /^models\/wardrobe\//);
  }
  for (const actor of ['man', 'woman']) {
    assert.equal(new Set(['hip_hop', 'slow_waltz', 'ballet'].map(style => retrieveCharacterFile(catalog, style, actor))).size, 3);
  }
});

test('each outfit includes textured skinned clothes that follow a solo dance', async () => {
  for (const profile of Object.values(catalog.wardrobe.profiles)) for (const actor of ['man', 'woman']) {
    const file = profile.models[actor].file;
    const document = await io.read(file);
    const root = document.getRoot();
    assert.ok(root.listTextures().length > 1, `${file}: skin and garment textures`);
    assert.ok(root.listMaterials().filter(material => material.getBaseColorTexture()).length > 1, file);
    assert.ok(root.listNodes().filter(node => node.getMesh() && node.getSkin()).length > 4, `${file}: skinned body and clothing`);
    if (actor === 'woman') {
      const hair = root.listNodes().find(node => node.getName().includes('braid01'));
      assert.ok(hair?.getMesh() && hair.getSkin(), `${file}: Melissa's skinned braid`);
      assert.ok(hair.getMesh().listPrimitives().every(primitive => primitive.getMaterial()?.getBaseColorTexture()), `${file}: textured braid`);
    }
    const model = (await load(file)).scene;
    const clip = await bindClip(await load(`animations/hip_hop/hip_hop_${actor}_bart_simpson.glb`), new Map([[actor, model]]));
    const mixer = new AnimationMixer(model);
    mixer.clipAction(clip).play();
    for (const fraction of [0, .5, .99]) {
      mixer.setTime(clip.duration * fraction);
      model.updateMatrixWorld(true);
      const size = new Box3().setFromObject(model, true).getSize(new Vector3());
      assert.ok(size.y > 1.5 && size.y < 2.3, `${file}: full-height clothed performer`);
      model.traverse(node => assert.ok(node.matrixWorld.elements.every(Number.isFinite), file));
    }
    mixer.stopAllAction();
    mixer.uncacheRoot(model);
  }
});
