import { test } from 'node:test';
import assert from 'node:assert/strict';
import { DanceSequence, MoveIntervals } from './sequence.ts';

const moves = [{ id: 'basic' }, { id: 'turn' }, { id: 'cross' }];

test('Single selects the current move for manual playback', () => {
  const sequence = new DanceSequence();
  sequence.setMode('single');
  assert.equal(sequence.retrieveMode(), 'single');
  assert.equal(sequence.retrieveNext(moves, 'basic'), undefined);
});

test('each style retains its own configurable interval across sessions', () => {
  const saved = new Map();
  const storage = { getItem: key => saved.get(key) ?? null, setItem: (key, value) => saved.set(key, value) };
  const intervals = new MoveIntervals(storage);
  assert.equal(intervals.retrieveInterval('house_dance', 16), 16);
  assert.equal(intervals.retrieveInterval('salsa', 0), 0);
  intervals.setInterval('house_dance', 8);
  intervals.setInterval('salsa', 4);
  const restored = new MoveIntervals(storage);
  assert.equal(restored.retrieveInterval('house_dance', 16), 8);
  assert.equal(restored.retrieveInterval('salsa', 0), 4);
  assert.equal(restored.retrieveInterval('slow_waltz', 0), 0);
});

test('Sequential advances in selector order and cycles to the first move', () => {
  const sequence = new DanceSequence();
  sequence.setMode('sequential');
  assert.equal(sequence.retrieveNext(moves, 'basic'), moves[1]);
  assert.equal(sequence.retrieveNext(moves, 'cross'), moves[0]);
  assert.equal(sequence.retrieveNext([moves[0]], 'basic'), moves[0]);
});

test('Random chooses from the current style and supports each available move', () => {
  let choice = 0;
  const sequence = new DanceSequence(() => choice);
  assert.equal(sequence.retrieveMode(), 'random');
  for (const [index, move] of moves.entries()) {
    choice = (index + .5) / moves.length;
    assert.equal(sequence.retrieveNext(moves, 'basic'), move);
  }
  assert.equal(sequence.retrieveNext([], 'basic'), undefined);
});
