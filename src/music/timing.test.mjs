import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { PhraseTiming, PlaybackClock } from './timing.ts';

const tracks = JSON.parse(readFileSync(new URL('../../music.json', import.meta.url))).tracks;
const catalog = JSON.parse(readFileSync(new URL('../../catalog.json', import.meta.url)));
const close = (actual, expected) => assert.ok(Math.abs(actual - expected) < 1e-6, `${actual} ≈ ${expected}`);

test('every style has an original licensed track and every clip repeats on a musical subdivision', () => {
  assert.deepEqual(tracks.map(track => track.style).sort(), catalog.styles.map(style => style.id).sort());
  for (const entry of catalog.animations) {
    const track = tracks.find(track => track.style === entry.style);
    assert.equal(track.license, 'MIT-0');
    assert.ok(track.timingBasis);
    const timing = new PhraseTiming(entry.duration, track);
    assert.ok(timing.duration > 0);
    assert.equal(timing.beats * 2 % 1, 0);
    const repeatedTime = timing.retrievePosition(timing.duration * 100, true).time;
    close(Math.min(repeatedTime, timing.duration - repeatedTime), 0);
    close(timing.retrievePosition(timing.duration / 2, true).sourceTime, timing.sourceDuration / 2);
    assert.equal(timing.retrievePosition(timing.duration, false).finished, true);
  }
});

test('authored Hip hop and triple-meter Waltz timing preserves beat landings', () => {
  const hipHop = new PhraseTiming(2.5, tracks.find(track => track.style === 'hip_hop'));
  assert.equal(hipHop.beats, 4);
  close(hipHop.duration, 2.5);
  close(hipHop.retrievePosition(.625, true).sourceTime, .625);
  const waltz = tracks.find(track => track.style === 'slow_waltz');
  assert.equal(waltz.meter, 3);
  assert.equal(waltz.tempo, 90);
  const timing = new PhraseTiming(2, waltz);
  assert.equal(timing.beats, 3);
  close(timing.duration, 2);
});

test('Tutting closing hold supplies the same beat spacing across repeated phrases', () => {
  const timing = new PhraseTiming(5 + 4 / 24, tracks.find(track => track.style === 'tutting'));
  close(timing.duration, 5);
  close(timing.sourceDuration, 5);
  close(timing.retrievePosition(6, true).sourceTime, 1);
});

test('the shared clock retains phase through pause, seek, speed, and clock changes', () => {
  let now = 10;
  const clock = new PlaybackClock(() => now);
  clock.setPaused(false);
  now += 2;
  close(clock.retrieveTime(), 2);
  clock.setPaused(true);
  now += 10;
  close(clock.retrieveTime(), 2);
  clock.seek(1.5);
  clock.setSpeed(2);
  clock.setPaused(false);
  now += 1;
  close(clock.retrieveTime(), 3.5);
  let audioTime = 200;
  clock.useTimeSource(() => audioTime);
  close(clock.retrieveTime(), 3.5);
  audioTime += .25;
  close(clock.retrieveTime(), 4);
  clock.seek(0);
  close(clock.retrieveTime(), 0);
});

test('the clock advances through a delayed render by the full elapsed musical time', () => {
  let now = 0;
  const clock = new PlaybackClock(() => now);
  clock.setPaused(false);
  now = 90;
  close(clock.retrieveTime(), 90);
});
