// Apply lossless Meshopt buffer encoding after sampling and key compaction.
import { NodeIO } from '@gltf-transform/core';
import { EXTMeshoptCompression } from '@gltf-transform/extensions';
import { MeshoptEncoder, MeshoptDecoder } from 'meshoptimizer';
import { readFile, writeFile, rename } from 'node:fs/promises';
await Promise.all([MeshoptEncoder.ready, MeshoptDecoder.ready]);
const io = new NodeIO().registerExtensions([EXTMeshoptCompression]).registerDependencies({
  'meshopt.encoder': MeshoptEncoder, 'meshopt.decoder': MeshoptDecoder,
});
const catalog = JSON.parse(await readFile('catalog.json','utf8'));
const requested = process.argv.slice(2);
const entries = requested.length ? catalog.animations.filter(entry=>requested.includes(entry.id)) : catalog.animations;
let before=0,after=0;
for (const [index,entry] of entries.entries()) {
  const original = await readFile(entry.file);
  const document = await io.readBinary(original);
  const arrays = document.getRoot().listAccessors().map(accessor=>[accessor.getName(),accessor.getType(),accessor.getArray().slice()]);
  document.createExtension(EXTMeshoptCompression).setRequired(true)
    .setEncoderOptions({method:EXTMeshoptCompression.EncoderMethod.QUANTIZE});
  // No quantize transform or lossy filter is applied. Verify every numeric value.
  const encoded = await io.writeBinary(document);
  const decoded = await io.readBinary(encoded);
  const actual = decoded.getRoot().listAccessors();
  if (actual.length !== arrays.length) throw new Error(`${entry.id}: accessor coverage`);
  for (const [i,[,type,values]] of arrays.entries()) {
    const result = actual[i].getArray();
    if (actual[i].getType() !== type || values.length !== result.length || values.some((value,j)=>value !== result[j])) {
      throw new Error(`${entry.id}: lossless compression parity, accessor ${i}`);
    }
  }
  await writeFile(`${entry.file}.tmp`,encoded);
  await rename(`${entry.file}.tmp`,entry.file);
  before+=original.length;after+=encoded.length;
  if ((index+1)%100===0) console.log(`Compressed ${index+1}/${entries.length}: ${(before/1048576).toFixed(1)} → ${(after/1048576).toFixed(1)} MiB`);
}
console.log(`Lossless GLB encoding: ${(before/1048576).toFixed(1)} → ${(after/1048576).toFixed(1)} MiB`);
