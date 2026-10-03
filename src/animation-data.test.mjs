import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { gzipSync } from 'node:zlib';
import { decodeAnimationData } from './animation-data.ts';

test('clip delivery works with explicit gzip and automatic HTTP decompression', async () => {
  const original = await readFile('animations/merengue/merengue_basic_in_place.glb');
  for (const bytes of [original, gzipSync(original)]) {
    const decoded = await decodeAnimationData(bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength));
    assert.deepEqual(Buffer.from(decoded), original);
  }
});
