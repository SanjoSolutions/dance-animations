import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { AnimationMixer, Box3, Group, LoopOnce, Vector3 } from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import { clone } from 'three/addons/utils/SkeletonUtils.js';
import { bindClip } from './clip-binding.ts';
import { DanceMotion } from './motion.ts';
import { DancePlayback } from './music/playback.ts';
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

for (const [style, label, count] of [['jazz', 'Jazz', 18], ['gogo', 'Go-go', 64], ['cutting_shapes', 'Cutting shapes', 36], ['solo_disco_dance', 'Disco', 1]]) {
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

test('Salsa cross body outside turn keeps both chest regions attached to each torso', async () => {
  const entry = catalog.animations.find(entry => entry.id === 'salsa_cross_body_outside_turn');
  const source = await load(entry.file);
  for (const models of [catalog.models, catalog.wardrobe.profiles.latin.models]) {
    for (const actor of entry.performers) {
      const model = clone((await load(models[actor].file)).scene);
      const clip = await bindClip(source, new Map([[actor, model]]));
      const mixer = new AnimationMixer(model);
      const action = mixer.clipAction(clip).setLoop(LoopOnce, 1);
      action.clampWhenFinished = true;
      action.play();
      const torso = model.getObjectByName('DEF-spine004');
      const chest = ['L', 'R'].map(side => model.getObjectByName(`DEF-breast${side}`));
      assert.ok(torso && chest.every(Boolean), `${actor}: chest and torso joints`);
      const offsets = [];
      // Cover every stored frame, fractional poses, and the directed move's endpoint.
      for (let sample = 0; sample <= 640; sample++) {
        mixer.setTime(sample / 96);
        model.updateMatrixWorld(true);
        for (const [index, joint] of chest.entries()) {
          const offset = torso.worldToLocal(joint.getWorldPosition(new Vector3()));
          if (sample === 0) offsets[index] = offset.clone();
          assert.ok(offset.distanceTo(offsets[index]) < .0003,
            `${models[actor].file}: ${joint.name} follows its torso at frame ${sample / 4}`);
        }
      }
      mixer.stopAllAction();
      mixer.uncacheRoot(model);
    }
  }
});

const recovery = JSON.parse(await readFile('docs/animation_work_status/priority_recovery/evidence.json', 'utf8'));
const music = JSON.parse(await readFile('music.json', 'utf8'));
const directed = recovery.clips.filter(clip => clip.loop === false);

function retrievePose(group) {
  group.updateMatrixWorld(true);
  const pose = [];
  group.traverse(node => {
    if (node.isBone) pose.push(...node.matrixWorld.elements);
    if (node.isSkinnedMesh) {
      node.skeleton.update();
      const count = node.geometry.attributes.position.count;
      for (const index of [0, Math.floor(count / 2), count - 1]) {
        pose.push(...node.getVertexPosition(index, new Vector3()).applyMatrix4(node.matrixWorld).toArray());
      }
    }
  });
  assert.ok(pose.length > 0 && pose.every(Number.isFinite));
  return pose;
}

function comparePose(actual, expected) {
  assert.equal(actual.length, expected.length);
  const error = actual.reduce((maximum, value, index) => Math.max(maximum, Math.abs(value - expected[index])), 0);
  assert.ok(error < 1e-6, `Maximum bone matrix / sampled surface component difference: ${error}`);
}

for (const record of directed) {
  test(`${record.id} plays once on actual MPFB models, holds its endpoint, and restarts`, async context => {
    let elapsed = 0;
    context.mock.method(performance, 'now', () => elapsed * 1000);
    const entry = catalog.animations.find(entry => entry.id === record.id);
    const performers = new Map(entry.performers.map(actor => [actor, clone(actor === 'man' ? man.scene : woman.scene)]));
    const group = new Group().add(...performers.values());
    const clip = await bindClip(await load(entry.file), performers);
    const motion = new DanceMotion(group, performers);
    context.after(() => motion.dispose());
    motion.select(clip, 0, 0);
    motion.update(0, 0);
    const start = retrievePose(group);
    motion.update(clip.duration, clip.duration);
    const end = retrievePose(group);
    const playback = new DancePlayback();
    const track = music.tracks.find(track => track.style === entry.style);
    await playback.select(clip.duration, track, {}, () => {}, undefined, entry.loop !== false);
    const duration = playback.retrievePosition().duration;
    const sample = () => {
      const position = playback.retrievePosition();
      motion.update(position.sourceTime, position.elapsed);
      return position;
    };
    for (const fraction of [0, .25, .5, .75, .999]) {
      elapsed = duration * fraction;
      assert.equal(sample().paused, false);
      retrievePose(group);
    }
    for (const fraction of [1, 1.5, 3]) {
      elapsed = duration * fraction;
      const position = sample();
      assert.equal(position.paused, true);
      assert.ok(Math.abs(position.sourceTime - clip.duration) < 1e-6);
      comparePose(retrievePose(group), end);
    }
    playback.restart();
    assert.equal(sample().paused, false);
    comparePose(retrievePose(group), start);
    elapsed += duration / 2;
    assert.ok(Math.abs(sample().sourceTime - clip.duration / 2) < 1e-6);
  });
}

for (const [directedId, loopId] of [
  ['hip_hop_man_neutral_to_low', 'hip_hop_man_down_bounce'],
  ['new_york_hustle_send_out', 'new_york_hustle_basic_closed'],
  ['salsa_cross_body_lead', 'salsa_basic'],
]) {
  test(`${directedId} holds until automatic selection and ${loopId} repeats on actual models`, async context => {
    let elapsed = 0;
    context.mock.method(performance, 'now', () => elapsed * 1000);
    const entry = catalog.animations.find(entry => entry.id === directedId);
    const next = catalog.animations.find(entry => entry.id === loopId);
    assert.ok(entry && next);
    const performers = new Map(entry.performers.map(actor => [actor, clone(actor === 'man' ? man.scene : woman.scene)]));
    const group = new Group().add(...performers.values());
    const motion = new DanceMotion(group, performers);
    context.after(() => motion.dispose());
    const clip = await bindClip(await load(entry.file), performers);
    const nextClip = await bindClip(await load(next.file), performers);
    const playback = new DancePlayback();
    const track = music.tracks.find(track => track.style === entry.style);
    const buffer = {};
    playback.setLoop(true, true);
    await playback.select(clip.duration, track, buffer, start => motion.select(clip, start, 0), undefined, entry.loop !== false);
    const sample = () => {
      const position = playback.retrievePosition();
      motion.update(position.sourceTime, position.elapsed);
      return position;
    };
    const duration = playback.retrievePosition().duration;
    elapsed = duration;
    sample();
    const endpoint = retrievePose(group);
    elapsed = duration * 1.25;
    assert.equal(sample().paused, false);
    comparePose(retrievePose(group), endpoint);
    const interval = 16;
    const deadline = interval * track.meter * 60 / track.tempo;
    const selected = playback.select(nextClip.duration, track, buffer, start => motion.select(nextClip, start, 0), interval, next.loop !== false);
    elapsed = deadline - .01;
    assert.equal(sample().paused, false);
    comparePose(retrievePose(group), endpoint);
    elapsed = deadline;
    const incoming = sample();
    assert.equal(await selected, true);
    assert.equal(incoming.sourceTime, 0);
    const entryPose = retrievePose(group);
    elapsed += incoming.duration / 4;
    sample();
    const quarterPose = retrievePose(group);
    elapsed = deadline + incoming.duration;
    assert.equal(sample().paused, false);
    comparePose(retrievePose(group), entryPose);
    elapsed += incoming.duration / 4;
    sample();
    comparePose(retrievePose(group), quarterPose);
    playback.restart();
    sample();
    comparePose(retrievePose(group), entryPose);
  });
}
