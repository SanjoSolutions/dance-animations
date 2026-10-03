import { assetUrl, type DanceAnimation } from './catalog';
import { decodeAnimationData } from './animation-data';

/** Pages packages gzip files explicitly; browsers decode them before GLB loading. */
export async function retrieveAnimationData(entry: DanceAnimation): Promise<ArrayBuffer> {
  const response = await fetch(assetUrl(entry.transportFile ?? entry.file));
  if (!response.ok) throw new Error(`Could not load the animation (${response.status}).`);
  return decodeAnimationData(await response.arrayBuffer());
}
