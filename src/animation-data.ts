/** Decode explicit gzip transport or a GLB already decoded by the HTTP server. */
export async function decodeAnimationData(data: ArrayBuffer): Promise<ArrayBuffer> {
  const signature = new Uint8Array(data, 0, Math.min(4, data.byteLength));
  if (signature[0] === 0x1f && signature[1] === 0x8b) {
    data = await new Response(new Blob([data]).stream().pipeThrough(new DecompressionStream('gzip'))).arrayBuffer();
  }
  const header = new Uint8Array(data, 0, Math.min(4, data.byteLength));
  if (String.fromCharCode(...header) !== 'glTF') throw new Error('Expected an animation GLB.');
  return data;
}
