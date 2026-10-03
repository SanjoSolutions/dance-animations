import { test } from 'node:test';
import assert from 'node:assert/strict';
import { AnimationClip, Group, Object3D, VectorKeyframeTrack } from 'three';
import { DanceMotion } from './motion.ts';
import { readFile } from 'node:fs/promises';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import { clone } from 'three/addons/utils/SkeletonUtils.js';
import { bindClip } from './clip-binding.ts';

const close = (actual, expected) => assert.ok(Math.abs(actual - expected) < 1e-5, `${actual} ≈ ${expected}`);

function createMotion(actors = ['man'], preservePlacement = true) {
  const group = new Group();
  const performers = new Map();
  const roots = [];
  const hips = [];
  for (const actor of actors) {
    const model = new Group();
    const root = new Object3D();
    root.name = `${actor === 'man' ? 'Man' : 'Woman'}.rigify_deform`;
    const hip = new Object3D();
    root.add(hip);
    model.add(root);
    group.add(model);
    performers.set(actor, model);
    roots.push(root);
    hips.push(hip);
  }
  const motion = new DanceMotion(group, performers, preservePlacement);
  const clip = (positions, height, travel = 0) => new AnimationClip('move', 1, roots.flatMap((root, index) => [
    new VectorKeyframeTrack(`${root.uuid}.position`, [0, 1], [positions[index], 0, 0, positions[index] + travel, 0, 0]),
    new VectorKeyframeTrack(`${hips[index].uuid}.position`, [0, 1], [0, height, 0, 0, height, 0]),
  ]));
  return { motion, group, roots, hips, clip };
}

test('preloaded solo clips blend on the same characters and retain their floor-plane root position', () => {
  const { motion, group, roots, hips, clip } = createMotion();
  const character = group.children[0];
  motion.select(clip([5], 1, 2), 0, 0);
  motion.update(.5, .5);
  close(roots[0].position.x, 6);
  const next = clip([-3], 3, 2);
  motion.prepare(next);
  close(roots[0].position.x, 6);
  close(hips[0].position.y, 1);
  motion.select(next, .5, .2);
  motion.update(0, .5);
  close(roots[0].position.x, 6);
  close(hips[0].position.y, 1);
  motion.update(.1, .6);
  close(roots[0].position.x, 6.1);
  close(hips[0].position.y, 2);
  motion.update(.1, .6);
  close(hips[0].position.y, 2);
  motion.update(.2, .7);
  close(roots[0].position.x, 6.4);
  close(hips[0].position.y, 3);
  assert.equal(group.children[0], character);
  motion.dispose();
});

test('partner transitions preserve their shared center and the new move’s authored spacing', () => {
  const { motion, roots, clip } = createMotion(['man', 'woman']);
  motion.select(clip([4, 6], 1), 0, 0);
  motion.update(.5, .5);
  const next = clip([-2, 2], 2);
  motion.prepare(next);
  motion.select(next, .5, .2);
  motion.update(0, .5);
  close((roots[0].position.x + roots[1].position.x) / 2, 5);
  motion.update(.2, .7);
  close((roots[0].position.x + roots[1].position.x) / 2, 5);
  close(roots[1].position.x - roots[0].position.x, 4);
  motion.dispose();
});

test('rapid choices blend from the visible pose and cancelled preloads retain the active pose', () => {
  const { motion, hips, clip } = createMotion();
  motion.select(clip([0], 1), 0, 0);
  motion.update(0, 0);
  motion.select(clip([0], 3), 0, .2);
  motion.update(.1, .1);
  close(hips[0].position.y, 2);
  const cancelled = clip([0], 9);
  motion.prepare(cancelled);
  motion.release(cancelled);
  close(hips[0].position.y, 2);
  motion.select(clip([0], 5), .1, .2);
  motion.update(0, .1);
  close(hips[0].position.y, 2);
  motion.update(.1, .2);
  close(hips[0].position.y, 3.5);
  motion.update(.4, .5);
  close(hips[0].position.y, 5);
  motion.dispose();
});

test('prop-based dances retain the incoming clip’s authored placement', () => {
  const { motion, roots, clip } = createMotion(['man'], false);
  motion.select(clip([5], 1), 0, 0);
  motion.update(0, 0);
  motion.select(clip([0], 2), 0, .2);
  motion.update(.2, .2);
  close(roots[0].position.x, 0);
  motion.dispose();
});

test('actual House clips reuse MPFB characters through finite blended poses', async () => {
  globalThis.createImageBitmap = async () => ({ width: 1, height: 1, close() {} });
  globalThis.self = globalThis;
  const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
  const load = async path => {
    const bytes = await readFile(path);
    return loader.parseAsync(bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength), '');
  };
  const catalog = JSON.parse(await readFile('catalog.json', 'utf8'));
  const model = clone((await load(catalog.models.man.file)).scene);
  const group = new Group().add(model);
  const performers = new Map([['man', model]]);
  const motion = new DanceMotion(group, performers);
  const first = await bindClip(await load('animations/house_dance/house_man_salsa_step.glb'), performers);
  const next = await bindClip(await load('animations/house_dance/house_man_train.glb'), performers);
  const root = [];
  model.traverse(node => { if (/^Man[._]?rigify_deform$/.test(node.name)) root.push(node); });
  assert.equal(root.length, 1);
  motion.select(first, 0, 0);
  motion.update(first.duration * .75, 10);
  const position = root[0].position.clone();
  motion.prepare(next);
  motion.select(next, 10, .25);
  motion.update(0, 10);
  close(root[0].position.x, position.x);
  close(root[0].position.z, position.z);
  for (const time of [.05, .125, .25, .5]) {
    motion.update(time, 10 + time);
    group.updateMatrixWorld(true);
    model.traverse(node => assert.ok(node.matrixWorld.elements.every(Number.isFinite), node.name));
  }
  assert.equal(group.children[0], model);
  motion.dispose();
});
