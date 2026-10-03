import { AnimationAction, AnimationClip, AnimationMixer, Group, LoopOnce, Object3D, SkinnedMesh, Vector3 } from 'three';
import type { Performer } from './clip-binding.ts';

class CharacterPlacement {
  private readonly roots: Object3D[] = [];

  constructor(performers: Map<Performer, Object3D>) {
    for (const model of performers.values()) {
      model.traverse(node => {
        if (/^(Man|Woman|Human)[._]?rigify_deform(?:_\d+)?$/.test(node.name)) this.roots.push(node);
      });
    }
  }

  align(clip: AnimationClip): void {
    const positions = this.roots.map(root => clip.tracks.find(track => track.name === `${root.uuid}.position`));
    if (this.roots.length > 0 && positions.every(track => track)) {
      const current = new Vector3();
      const incoming = new Vector3();
      for (const [index, root] of this.roots.entries()) {
        current.add(root.position);
        const track = positions[index]!;
        incoming.add(new Vector3().fromArray(track.values, track.getValueSize() === 9 ? 3 : 0));
      }
      const offset = current.sub(incoming).divideScalar(this.roots.length);
      // Shared floor-plane placement keeps each partner's authored spacing and height.
      for (const track of positions) {
        const stride = track!.getValueSize();
        const first = stride === 9 ? 3 : 0;
        for (let index = first; index < track!.values.length; index += stride) {
          track!.values[index] += offset.x;
          track!.values[index + 2] += offset.z;
        }
      }
    }
  }
}

interface OutgoingMotion {
  action: AnimationAction;
  /** Frozen source pose time in seconds. */
  time: number;
  weight: number;
}

/** Samples successive clips on the same characters, with continuous placement and pose blending. */
export class DanceMotion {
  private readonly group: Group;
  private readonly preservePlacement: boolean;
  private readonly mixer: AnimationMixer;
  private readonly placement: CharacterPlacement;
  private action?: AnimationAction;
  private outgoing: OutgoingMotion[] = [];
  /** Blend start on the transport clock, in seconds. */
  private start = 0;
  /** Blend duration in seconds. */
  private duration = 0;

  constructor(group: Group, performers: Map<Performer, Object3D>, preservePlacement = true) {
    this.group = group;
    this.preservePlacement = preservePlacement;
    this.mixer = new AnimationMixer(group);
    this.placement = new CharacterPlacement(performers);
  }

  prepare(clip: AnimationClip): void {
    const action = this.mixer.clipAction(clip);
    action.setLoop(LoopOnce, 1);
    action.clampWhenFinished = true;
  }

  /** Start and duration are measured in seconds on the shared transport. */
  select(clip: AnimationClip, start: number, duration: number): void {
    if (this.action) {
      if (this.preservePlacement) this.placement.align(clip);
      this.outgoing = [...this.outgoing, { action: this.action, time: this.action.time, weight: this.action.getEffectiveWeight() }]
        .map(motion => ({ ...motion, weight: motion.action.getEffectiveWeight() }));
    }
    this.prepare(clip);
    this.action = this.mixer.clipAction(clip).reset().play();
    this.start = start;
    this.duration = duration;
    this.action.setEffectiveWeight(this.outgoing.length > 0 ? 0 : 1);
    if (duration === 0) this.finishTransition();
  }

  /** Sample a source pose and the transport clock, both measured in seconds. */
  update(sourceTime: number, elapsed: number): void {
    if (this.action) {
      const fraction = this.duration > 0 ? Math.min(1, Math.max(0, (elapsed - this.start) / this.duration)) : 1;
      const weight = fraction * fraction * (3 - 2 * fraction);
      for (const motion of this.outgoing) this.sample(motion.action, motion.time, motion.weight * (1 - weight));
      this.sample(this.action, sourceTime, this.outgoing.length > 0 ? weight : 1);
      this.mixer.update(0);
      if (fraction === 1) this.finishTransition();
    }
  }

  finishTransition(): void {
    for (const motion of this.outgoing) this.release(motion.action.getClip());
    this.outgoing = [];
    this.action?.setEffectiveWeight(1);
  }

  release(clip: AnimationClip): void {
    this.mixer.uncacheAction(clip, this.group);
  }

  dispose(): void {
    this.mixer.stopAllAction();
    this.mixer.uncacheRoot(this.group);
    this.group.traverse(object => {
      if (object instanceof SkinnedMesh) object.skeleton.dispose();
    });
  }

  private sample(action: AnimationAction, time: number, weight: number): void {
    action.paused = false;
    action.enabled = true;
    action.time = time;
    action.setEffectiveWeight(weight);
  }
}
