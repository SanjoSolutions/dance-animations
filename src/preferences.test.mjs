import { test } from 'node:test';
import assert from 'node:assert/strict';
import { PlaybackPreferences } from './preferences.ts';

function createStorage() {
  const values = new Map();
  return { getItem: key => values.get(key) ?? null, setItem: (key, value) => values.set(key, value) };
}

test('fresh playback defaults to music, half volume, and Random mode', () => {
  const preferences = new PlaybackPreferences(createStorage());
  assert.equal(preferences.retrieveMusic(), true);
  assert.equal(preferences.retrieveVolume(), .5);
  assert.equal(preferences.retrieveMode(), 'random');
});

test('music, volume, and mode choices survive a new playback session', () => {
  const storage = createStorage();
  const preferences = new PlaybackPreferences(storage);
  preferences.setMusic(false);
  preferences.setVolume(.25);
  preferences.setMode('sequential');
  const restored = new PlaybackPreferences(storage);
  assert.equal(restored.retrieveMusic(), false);
  assert.equal(restored.retrieveVolume(), .25);
  assert.equal(restored.retrieveMode(), 'sequential');
  assert.equal(restored.retrieveMode('single'), 'single');
  assert.equal(restored.retrieveMode('random'), 'random');
  assert.equal(restored.retrieveMode(), 'sequential');
});

test('session preferences remain available when persistent storage requires fallback', () => {
  const preferences = new PlaybackPreferences({ getItem() { throw new Error('Storage access'); }, setItem() { throw new Error('Storage access'); } });
  preferences.setMusic(false);
  preferences.setVolume(.75);
  preferences.setMode('single');
  assert.equal(preferences.retrieveMusic(), false);
  assert.equal(preferences.retrieveVolume(), .75);
  assert.equal(preferences.retrieveMode(), 'single');
});

test('stored values outside the supported ranges recover the playback defaults', () => {
  const storage = createStorage();
  storage.setItem('dance-animation-playback', JSON.stringify({music:'on',volume:2,mode:'playlist'}));
  const preferences = new PlaybackPreferences(storage);
  assert.equal(preferences.retrieveMusic(), true);
  assert.equal(preferences.retrieveVolume(), .5);
  assert.equal(preferences.retrieveMode(), 'random');
});
