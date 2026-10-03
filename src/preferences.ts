import type { PlaybackMode } from './sequence.ts';

export class PreferenceStore {
  private readonly values = new Map<string, unknown>();
  private readonly key: string;
  private readonly storage?: Pick<Storage, 'getItem' | 'setItem'>;

  constructor(key: string, storage?: Pick<Storage, 'getItem' | 'setItem'>) {
    this.key = key;
    this.storage = storage;
    try {
      const saved: unknown = JSON.parse(storage?.getItem(key) ?? '{}');
      if (saved && typeof saved === 'object' && !Array.isArray(saved)) {
        for (const [name, value] of Object.entries(saved)) this.values.set(name, value);
      }
    } catch { /* Defaults supply the initial settings. */ }
  }

  retrieve(name: string): unknown { return this.values.get(name); }

  save(name: string, value: unknown): void {
    this.values.set(name, value);
    try { this.storage?.setItem(this.key, JSON.stringify(Object.fromEntries(this.values))); }
    catch { /* The current session retains its settings. */ }
  }
}

function isPlaybackMode(value: unknown): value is PlaybackMode {
  return value === 'single' || value === 'sequential' || value === 'random';
}

export class PlaybackPreferences {
  private readonly store: PreferenceStore;

  constructor(storage?: Pick<Storage, 'getItem' | 'setItem'>) {
    this.store = new PreferenceStore('dance-animation-playback', storage);
  }

  retrieveMusic(): boolean {
    const value = this.store.retrieve('music');
    return typeof value === 'boolean' ? value : true;
  }

  retrieveVolume(): number {
    const value = this.store.retrieve('volume');
    return typeof value === 'number' && Number.isFinite(value) && value >= 0 && value <= 1 ? value : .5;
  }

  retrieveMode(requested?: string | null): PlaybackMode {
    const saved = this.store.retrieve('mode');
    return isPlaybackMode(requested) ? requested : isPlaybackMode(saved) ? saved : 'random';
  }

  setMusic(enabled: boolean): void { this.store.save('music', enabled); }

  setVolume(volume: number): void {
    if (Number.isFinite(volume) && volume >= 0 && volume <= 1) this.store.save('volume', volume);
    else throw new RangeError('Choose a volume between zero and one.');
  }

  setMode(mode: PlaybackMode): void {
    if (isPlaybackMode(mode)) this.store.save('mode', mode);
    else throw new RangeError('Choose Single, Sequential, or Random.');
  }
}
