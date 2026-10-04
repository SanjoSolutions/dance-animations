import { test } from 'node:test';
import assert from 'node:assert/strict';
import { retrieveMoves, retrieveVariant } from './moves.ts';

const entry = (id, performers, style = 'hip_hop') => ({ id, style, performers });
test('solo character versions share a move choice with the move name', () => {
  const moves = retrieveMoves([entry('hip_hop_man_bart_simpson', ['man']), entry('hip_hop_woman_bart_simpson', ['woman'])], 'hip_hop');
  assert.equal(moves.length, 1);
  assert.equal(moves[0].label, 'Bart simpson');
  assert.equal(retrieveVariant(moves[0], 'woman').id, 'hip_hop_woman_bart_simpson');
});
test('style prefixes and character suffixes become separate selectors', () => {
  const move = retrieveMoves([entry('solo_rumba_basic_forward_back_man', ['man'], 'solo_rumba')], 'solo_rumba')[0];
  assert.equal(move.label, 'Basic forward back');
  assert.equal(retrieveVariant(move, 'woman').id, 'solo_rumba_basic_forward_back_man');
});
test('a routine named after its style groups both solo character choices', () => {
  const moves = retrieveMoves([
    entry('solo_disco_dance', ['man'], 'solo_disco_dance'),
    entry('solo_disco_dance_woman', ['woman'], 'solo_disco_dance'),
  ], 'solo_disco_dance');
  assert.equal(moves.length, 1);
  assert.equal(moves[0].label, 'Routine');
  assert.ok(moves[0].solo);
  assert.equal(retrieveVariant(moves[0], 'man').id, 'solo_disco_dance');
  assert.equal(retrieveVariant(moves[0], 'woman').id, 'solo_disco_dance_woman');
});
test('a move name retains meaningful words and recognizes style aliases', () => {
  assert.equal(retrieveMoves([entry('shuffle_man_running_man',['man'],'shuffle')],'shuffle')[0].label,'Running man');
  assert.equal(retrieveMoves([entry('house_woman_jacking',['woman'],'house_dance')],'house_dance')[0].label,'Jacking');
});
test('partner moves retain both performers and their own choice', () => {
  const moves = retrieveMoves([entry('hip_hop_man_basic', ['man']), entry('hip_hop_basic', ['man', 'woman'])], 'hip_hop');
  assert.equal(moves.length, 2);
  assert.equal(moves.find(move => !move.solo).label, 'Basic (Partners)');
});
