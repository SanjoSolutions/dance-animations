import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { AnimationMixer, Box3, Group, Vector3 } from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import { clone } from 'three/addons/utils/SkeletonUtils.js';
import { bindClip } from './clip-binding.ts';
import { retrieveMoves, retrieveVariant } from './moves.ts';

// Geometry tests run in Node; actual texture decoding is checked in the browser.
globalThis.createImageBitmap = async () => ({ width: 1, height: 1, close() {} });
globalThis.self = globalThis;

const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
async function load(path) {
  const bytes = await readFile(path);
  return loader.parseAsync(bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength), '');
}
const catalog = JSON.parse(await readFile('catalog.json', 'utf8'));
const man = await load(catalog.models.man.file);
const woman = await load(catalog.models.woman.file);

for (const [style, label, count] of [['jazz', 'Jazz', 18], ['gogo', 'Go-go', 64], ['cutting_shapes', 'Cutting shapes', 36]]) {
  test(`every ${label} move offers Man and Woman solos with their original tracks and provenance`, async () => {
    const moves = retrieveMoves(catalog.animations, style);
    assert.equal(moves.length, count);
    for (const move of moves) {
      assert.ok(move.solo, move.id);
      assert.equal(move.variants.length, 2, move.id);
      const manEntry = retrieveVariant(move, 'man');
      const womanEntry = retrieveVariant(move, 'woman');
      for (const key of ['file', 'sourceFile', 'sourceSha256', 'originalExport', 'originalExportSha256', 'animationName', 'duration', 'status']) {
        assert.equal(womanEntry[key], manEntry[key], `${move.id}: ${key}`);
      }
      const source = await load(manEntry.file);
      const models = new Map([['man', clone(man.scene)], ['woman', clone(woman.scene)]]);
      const complete = await bindClip(source, models);
      for (const actor of ['man', 'woman']) {
        const entry = retrieveVariant(move, actor);
        assert.deepEqual(entry.performers, [actor], move.id);
        const model = models.get(actor);
        const identifiers = new Set();
        model.traverse(node => identifiers.add(node.uuid));
        const solo = await bindClip(source, new Map([[actor, model]]));
        assert.deepEqual(solo.tracks, complete.tracks.filter(track => identifiers.has(track.name.split('.')[0])), entry.id);
        assert.ok(solo.tracks.length > 100, entry.id);
        assert.equal(solo.duration, complete.duration, entry.id);
      }
    }
  });
}

test('both standard MPFB bodies fit their skeletons at rest and during a solo move', async () => {
  for (const [actor, template] of [['man', man], ['woman', woman]]) {
    const model = clone(template.scene);
    const body = model.getObjectByName(actor === 'man' ? 'Manbody' : 'Womanbody');
    assert.ok(body);
    model.updateMatrixWorld(true);
    const bounds = new Box3().setFromObject(body, true);
    assert.ok(bounds.getSize(new Vector3()).y > 1.5, `${actor}: full-height base body`);
    const clip = await bindClip(await load(`animations/hip_hop/hip_hop_${actor}_bart_simpson.glb`), new Map([[actor, model]]));
    const mixer = new AnimationMixer(model);
    mixer.clipAction(clip).play();
    for (const time of [0, 1, 2]) {
      mixer.setTime(time);
      model.updateMatrixWorld(true);
      const height = new Box3().setFromObject(body, true).getSize(new Vector3()).y;
      assert.ok(height > 1.5 && height < 2.2, `${actor}: coherent skinned body at ${time}`);
    }
  }
});

test('all library clips bind to the requested MPFB performers and seek to finite transforms', async () => {
  for (const entry of catalog.animations) {
    const source = await load(entry.file);
    const models = new Map(entry.performers.map(actor => [actor, clone(actor === 'man' ? man.scene : woman.scene)]));
    const group = new Group();
    group.add(...models.values());
    let clip;
    try { clip = await bindClip(source, models); }
    catch (error) { throw new Error(entry.id, { cause: error }); }
    assert.ok(clip.tracks.length > 0, entry.id);
    assert.ok(Math.abs(clip.duration - entry.duration) < .05, `${entry.id}: duration ${clip.duration} vs ${entry.duration}`);
    const mixer = new AnimationMixer(group);
    mixer.clipAction(clip).play();
    for (const fraction of [0, .5, .99]) {
      mixer.setTime(clip.duration * fraction);
      group.updateMatrixWorld(true);
      for (const model of models.values()) {
        model.traverse(node => assert.ok(node.matrixWorld.elements.every(Number.isFinite), `${entry.id}: ${node.name}`));
      }
    }
    mixer.stopAllAction();
    mixer.uncacheRoot(group);
  }
});

test('a paired clip animates each skeleton independently', async () => {
  const entry = catalog.animations.find(entry => entry.id === 'merengue_basic_in_place');
  assert.ok(entry);
  const source = await load(entry.file);
  const models = new Map([['man', clone(man.scene)], ['woman', clone(woman.scene)]]);
  const clip = await bindClip(source, models);
  for (const model of models.values()) {
    const identifiers = new Set();
    model.traverse(node => identifiers.add(node.uuid));
    const ownTracks = clip.tracks.filter(track => identifiers.has(track.name.split('.')[0]));
    assert.ok(ownTracks.length > 100, 'Each performer has independent bound tracks');
    assert.ok(ownTracks.some(track => {
      const width = track.getValueSize();
      return track.values.some((value, index) => Math.abs(value - track.values[index % width]) > 1e-4);
    }), 'Each performer moves');
  }
});
