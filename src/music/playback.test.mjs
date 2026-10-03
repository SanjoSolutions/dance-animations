import { test } from 'node:test';
import assert from 'node:assert/strict';
import { DancePlayback } from './playback.ts';

test('audible playback and visual sampling share pause, seek, speed, loop, restart, and selection state', async context => {
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
  const track = { tempo: 120, endingHold: 0 };
  const playback = new DancePlayback();
  const buffer = await playback.prepare('https://example.test/music.wav');
  playback.select(4, track, buffer);
  playback.setPaused(true);
  playback.seek(0);
  await playback.setMusic(true);
  playback.setPaused(false);
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
  assert.equal(sources.at(-1).playbackRate.value, 2);
  audioContext.currentTime = 10.5;
  assert.equal(playback.retrievePosition().time, 3);
  playback.setLoop(false);
  assert.equal(sources.at(-1).endTime, 11);
  audioContext.currentTime = 11;
  assert.equal(playback.retrievePosition().time, 4);
  assert.equal(playback.retrievePosition().paused, true);
  playback.restart();
  assert.equal(sources.at(-1).offset, 0);
  assert.equal(playback.retrievePosition().time, 0);
  playback.setLoop(true);
  audioContext.currentTime = 16;
  assert.equal(playback.retrievePosition().time, 2);
  const sourceCount = sources.length;
  await playback.setMusic(false);
  assert.equal(sources.at(-1).stopped, true);
  audioContext.currentTime = 16.5;
  assert.equal(playback.retrievePosition().time, 3);
  assert.equal(sources.length, sourceCount);
  playback.select(2, track, buffer);
  assert.equal(playback.retrievePosition().time, 0);
  playback.clear();
  assert.equal(playback.retrievePosition().paused, true);
});
