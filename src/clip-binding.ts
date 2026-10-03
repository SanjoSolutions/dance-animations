import { AnimationClip, Object3D, PropertyBinding } from 'three';
import type { GLTF } from 'three/addons/loaders/GLTFLoader.js';

export type Performer = 'man' | 'woman';

function performerFor(node: Object3D): Performer | undefined {
  let current: Object3D | null = node;
  while (current) {
    if (/^Man[._]?rigify_deform/.test(current.name)) return 'man';
    if (/^(Woman|Human)[._]?rigify_deform/.test(current.name)) return 'woman';
    current = current.parent;
  }
}

function baseName(name: string): string {
  // GLTFLoader disambiguates duplicate joint names across the two skeletons.
  return name.replace(/_\d+$/, '');
}

/** Bind each actor's joint tracks to that actor's MPFB instance using UUIDs. */
export async function bindClip(source: GLTF, models: Map<Performer, Object3D>): Promise<AnimationClip> {
  if (source.animations.length !== 1) throw new Error('Expected one animation in the clip.');
  const targets = new Map<Performer, Map<string, Object3D>>();
  for (const [actor, model] of models) {
    const nodes = new Map<string, Object3D>();
    model.traverse(node => nodes.set(baseName(node.name), node));
    targets.set(actor, nodes);
  }
  const tracks = [];
  const sourceNodes = await source.parser.getDependencies('node') as Object3D[];
  const sourceTargets = new Map(sourceNodes.map(node => [node.name || node.uuid, node]));
  for (const track of source.animations[0].tracks) {
    const binding = PropertyBinding.parseTrackName(track.name);
    const original = sourceTargets.get(binding.nodeName);
    if (!original) throw new Error(`Missing animation target: ${track.name}`);
    const actor = performerFor(original);
    if (actor) {
      const target = targets.get(actor)?.get(baseName(original.name));
      if (!target) throw new Error(`Missing ${actor} joint: ${original.name}`);
      const bound = track.clone();
      bound.name = `${target.uuid}.${binding.propertyName}`;
      tracks.push(bound);
    }
  }
  if (tracks.length === 0) throw new Error('The clip has no matching MPFB skeleton tracks.');
  return new AnimationClip(source.animations[0].name, source.animations[0].duration, tracks);
}
