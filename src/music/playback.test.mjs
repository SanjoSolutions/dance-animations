import { test } from 'node:test';
import assert from 'node:assert/strict';
import { DancePlayback } from './playback.ts';

async function preparePlayback(context) {
  const sources = [];
  let audioContext;
  class AudioContext {
    currentTime = 0;
    state = 'suspended';
    destination = {};
    constructor() { audioContext = this; }
    createGain() { return { gain: { value: 0, setTargetAtTime() {} }, connect() {} }; }
    addEventListener() {}
    async decodeAudioData() { return { duration: 16 }; }
    async resume() { this.state = 'running'; }
    createBufferSource() {
      const source = {
        playbackRate: { value: 1 }, connect() {}, disconnect() {},
        start(time, offset) { this.startTime = time; this.offset = offset; },
        stop(time) { if (time === undefined) this.stopped = true; else this.endTime = time; },
      };
      sources.push(source);
      return source;
    }
  }
  context.mock.method(globalThis, 'fetch', async () => ({ ok: true, arrayBuffer: async () => new ArrayBuffer(8) }));
  const original = globalThis.AudioContext;
  globalThis.AudioContext = AudioContext;
  context.after(() => { globalThis.AudioContext = original; });
  const track = { style: 'hip_hop', tempo: 120, animationTempo: 120, meter: 4, endingHold: 0 };
  const playback = new DancePlayback();
  const buffer = await playback.prepare('https://example.test/music.wav');
  playback.select(4, track, buffer);
  playback.setPaused(true);
  playback.seek(0);
  await playback.setMusic(true);
  playback.setPaused(false);
  return { playback, track, buffer, audioContext, sources };
}

test('music sets dance timing and retains its recorded rate through preview speed, pause, seek, and loop changes', async context => {
  const { playback, track, buffer, audioContext, sources } = await preparePlayback(context);
  assert.equal(sources.at(-1).offset, 0);
  audioContext.currentTime = 1.5;
  assert.equal(playback.retrievePosition().sourceTime, 1.5);
  playback.setPaused(true);
  assert.equal(sources.at(-1).stopped, true);
  audioContext.currentTime = 10;
  assert.equal(playback.retrievePosition().time, 1.5);
  playback.seek(2);
  playback.setPaused(false);
  assert.equal(sources.at(-1).offset, 2);
  playback.setSpeed(2);
  assert.equal(sources.at(-1).playbackRate.value, 1);
  audioContext.currentTime = 10.5;
  assert.equal(playback.retrievePosition().time, 2.5);
  playback.setLoop(false);
  assert.equal(sources.at(-1).endTime, 12);
  audioContext.currentTime = 12;
  assert.equal(playback.retrievePosition().time, 4);
  assert.equal(playback.retrievePosition().paused, true);
  playback.restart();
  assert.equal(sources.at(-1).offset, 0);
  assert.equal(playback.retrievePosition().time, 0);
  playback.setLoop(true);
  audioContext.currentTime = 17;
  assert.equal(playback.retrievePosition().time, 1);
  const sourceCount = sources.length;
  await playback.setMusic(false);
  assert.equal(sources.at(-1).stopped, true);
  audioContext.currentTime = 17.5;
  assert.equal(playback.retrievePosition().time, 2);
  assert.equal(sources.length, sourceCount);
  playback.select(2, track, buffer);
  assert.equal(playback.retrievePosition().time, 0);
  playback.clear();
  assert.equal(playback.retrievePosition().paused, true);
});

const close = (actual, expected) => assert.ok(Math.abs(actual - expected) < 1e-6, `${actual} ≈ ${expected}`);

test('same-style moves retain continuous audio through loading and begin on the next measure', async context => {
  const { playback, track, buffer, audioContext, sources } = await preparePlayback(context);
  const recording = sources.at(-1);
  const sourceCount = sources.length;
  audioContext.currentTime = .5;
  playback.beginSelection(track.style);
  assert.equal(recording.stopped, undefined);
  audioContext.currentTime = 5.2;
  close(playback.retrievePosition().sourceTime, 1.2);
  let starts = 0;
  const selection = playback.select(2, track, buffer, () => { starts += 1; });
  audioContext.currentTime = 5.8;
  close(playback.retrievePosition().sourceTime, 1.8);
  assert.equal(starts, 0);
  audioContext.currentTime = 6.1;
  close(playback.retrievePosition().sourceTime, .1);
  assert.equal(await selection, true);
  assert.equal(starts, 1);
  assert.equal(sources.length, sourceCount);
  assert.equal(recording.stopped, undefined);
  audioContext.currentTime = 8.1;
  close(playback.retrievePosition().time, .1);
  const nextSelection = playback.select(3, track, buffer);
  audioContext.currentTime = 10.05;
  close(playback.retrievePosition().sourceTime, .05);
  assert.equal(await nextSelection, true);
  playback.setPaused(true);
  playback.setPaused(false);
  close(sources.at(-1).offset, 10.05);
  close(playback.retrievePosition().sourceTime, .05);
  playback.beginSelection('salsa');
  await playback.select(4, { ...track, style: 'salsa' }, buffer);
  close(sources.at(-1).offset, 0);
  close(playback.retrievePosition().sourceTime, 0);
});

test('rapid move choices replace queued transitions and pause retains their musical phase', async context => {
  const { playback, track, buffer, audioContext } = await preparePlayback(context);
  audioContext.currentTime = .6;
  const superseded = playback.select(2, track, buffer);
  playback.beginSelection(track.style);
  assert.equal(await superseded, false);
  const selected = playback.select(3, track, buffer);
  audioContext.currentTime = .7;
  playback.setPaused(true);
  audioContext.currentTime = 20;
  close(playback.retrievePosition().sourceTime, .7);
  playback.setPaused(false);
  audioContext.currentTime = 21.4;
  close(playback.retrievePosition().sourceTime, .1);
  assert.equal(await selected, true);
});

test('a queued one-shot move keeps the recording alive until the new phrase completes', async context => {
  const { playback, track, buffer, audioContext, sources } = await preparePlayback(context);
  playback.setLoop(false);
  audioContext.currentTime = 2.9;
  const source = sources.at(-1);
  const sourceCount = sources.length;
  const selected = playback.select(2, track, buffer);
  close(source.endTime, 6);
  audioContext.currentTime = 4.1;
  close(playback.retrievePosition().sourceTime, .1);
  assert.equal(await selected, true);
  assert.equal(sources.length, sourceCount);
  assert.equal(playback.retrievePosition().paused, false);
  audioContext.currentTime = 6;
  close(playback.retrievePosition().sourceTime, 2);
  assert.equal(playback.retrievePosition().paused, true);
});

test('automatic moves finish their phrase and join the following measure with continuous music', async context => {
  const { playback, track, buffer, audioContext, sources } = await preparePlayback(context);
  playback.setPaused(true);
  await playback.select(3, track, buffer);
  playback.setLoop(false, true);
  const recording = sources.at(-1);
  const sourceCount = sources.length;
  const selected = playback.select(2, track, buffer, () => {}, 0);
  audioContext.currentTime = 3.5;
  close(playback.retrievePosition().sourceTime, 3);
  assert.equal(playback.retrievePosition().paused, false);
  audioContext.currentTime = 4.05;
  close(playback.retrievePosition().sourceTime, .05);
  assert.equal(await selected, true);
  assert.equal(sources.length, sourceCount);
  assert.equal(recording.stopped, undefined);
});

test('sixteen-bar changes preload, repeat moves, retain music, and restart their deadline', async context => {
  const { playback, track, buffer, audioContext, sources } = await preparePlayback(context);
  playback.setLoop(true, true);
  let starts = 0;
  const selected = playback.select(2, track, buffer, () => { starts += 1; }, 16);
  audioContext.currentTime = 31.9;
  close(playback.retrievePosition().sourceTime, 3.9);
  assert.equal(starts, 0);
  playback.restart();
  const sourceCount = sources.length;
  const recording = sources.at(-1);
  audioContext.currentTime = 63.8;
  close(playback.retrievePosition().sourceTime, 3.9);
  assert.equal(starts, 0);
  audioContext.currentTime = 64.025;
  close(playback.retrievePosition().sourceTime, .125);
  assert.equal(await selected, true);
  assert.equal(starts, 1);
  assert.equal(sources.length, sourceCount);
  assert.equal(recording.stopped, undefined);
  // Loading that finishes after its deadline joins the next available measure.
  audioContext.currentTime = 96.1;
  const late = playback.select(3, track, buffer, () => { starts += 1; }, 16);
  close(playback.retrievePosition().sourceTime, .2);
  assert.equal(starts, 1);
  audioContext.currentTime = 98.05;
  close(playback.retrievePosition().sourceTime, .15);
  assert.equal(await late, true);
  assert.equal(starts, 2);
});

test('music toggles preserve automatic deadlines and manual selections join silent preview immediately', async context => {
  const { playback, track, buffer, audioContext } = await preparePlayback(context);
  playback.setLoop(true, true);
  let starts = 0;
  const automatic = playback.select(2, track, buffer, () => { starts += 1; }, 16);
  audioContext.currentTime = 1;
  await playback.setMusic(false);
  close(playback.retrievePosition().sourceTime, 1);
  assert.equal(starts, 0);
  audioContext.currentTime = 2;
  await playback.setMusic(true);
  audioContext.currentTime = 32.05;
  close(playback.retrievePosition().sourceTime, .05);
  assert.equal(await automatic, true);
  assert.equal(starts, 1);
  const manual = playback.select(3, track, buffer, () => { starts += 1; });
  await playback.setMusic(false);
  assert.equal(await manual, true);
  close(playback.retrievePosition().sourceTime, 0);
  assert.equal(starts, 2);
});

test('default music waits for browser audio permission and Play resumes the shared transport', async context => {
  const { playback, audioContext, sources } = await preparePlayback(context);
  audioContext.currentTime = .5;
  audioContext.state = 'suspended';
  let resume;
  const permission = new Promise(resolve => { resume = resolve; });
  context.mock.method(audioContext, 'resume', async () => { await permission; audioContext.state = 'running'; });
  const starting = playback.setMusic(true);
  assert.equal(playback.retrievePosition().paused, true);
  audioContext.currentTime = 20;
  close(playback.retrievePosition().time, .5);
  playback.setPaused(false);
  resume();
  await starting;
  await Promise.resolve();
  close(sources.at(-1).offset, .5);
  assert.equal(playback.retrievePosition().paused, false);
  audioContext.currentTime = 20.5;
  close(playback.retrievePosition().time, 1);
});
