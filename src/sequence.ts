import type { DanceMove } from './moves.ts';
import { PreferenceStore } from './preferences.ts';

export type PlaybackMode = 'single' | 'sequential' | 'random';

export class DanceSequence {
  private mode: PlaybackMode = 'random';
  private readonly choose: () => number;

  constructor(choose: () => number = Math.random) { this.choose = choose; }

  setMode(mode: PlaybackMode): void { this.mode = mode; }
  retrieveMode(): PlaybackMode { return this.mode; }

  retrieveNext(moves: readonly DanceMove[], current: string): DanceMove | undefined {
    if (moves.length > 0 && this.mode === 'sequential') {
      const index = moves.findIndex(move => move.id === current);
      return moves[(index + 1) % moves.length];
    } else if (moves.length > 0 && this.mode === 'random') {
      return moves[Math.floor(this.choose() * moves.length)];
    } else {
      return undefined;
    }
  }
}

export class MoveIntervals {
  private readonly store: PreferenceStore;

  constructor(storage?: Pick<Storage, 'getItem' | 'setItem'>) {
    this.store = new PreferenceStore('dance-animation-intervals', storage);
  }

  /** Returns the change interval in bars. Zero uses the animation duration. */
  retrieveInterval(style: string, defaultInterval: number): number {
    const value = this.store.retrieve(style);
    return typeof value === 'number' && Number.isSafeInteger(value) && value >= 0 ? value : defaultInterval;
  }

  /** Stores a change interval in bars for this style. */
  setInterval(style: string, interval: number): void {
    if (Number.isSafeInteger(interval) && interval >= 0) {
      this.store.save(style, interval);
    } else {
      throw new RangeError('Choose a whole interval starting at zero.');
    }
  }
}
