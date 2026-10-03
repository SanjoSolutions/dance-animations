import { PhraseTiming, PlaybackClock, type MusicTrack } from './timing.ts';

interface MoveSelection {
  timing: PhraseTiming;
  /** Starting position in seconds on the continuous music clock. */
  start: number;
  /** Automatic change interval in bars; zero uses the current phrase. */
  interval?: number;
  activate: (start: number) => void;
  complete: (started: boolean) => void;
}

export class DancePlayback {
  private readonly clock = new PlaybackClock(() => performance.now() / 1000);
  private context?: AudioContext;
  private gain?: GainNode;
  private source?: AudioBufferSourceNode;
  private buffer?: AudioBuffer;
  private readonly buffers = new Map<string, Promise<AudioBuffer>>();
  private timing?: PhraseTiming;
  private track?: MusicTrack;
  private selection?: MoveSelection;
  /** Starting position in seconds on the continuous music clock. */
  private motionOrigin = 0;
  private enabled = false;
  private awaitingAudio = false;
  private looping = true;
  private advancing = false;
  private volume = .5;
  private previewSpeed = 1;
  private soundRequest = 0;
  onError: (message: string) => void = () => {};

  async prepare(file: string): Promise<AudioBuffer> {
    if (!this.context) {
      this.context = new AudioContext();
      this.gain = this.context.createGain();
      this.gain.gain.value = this.volume;
      this.gain.connect(this.context.destination);
      this.context.addEventListener('statechange', () => {
        if (this.context?.state === 'running') {
          this.clock.useTimeSource(() => this.context!.currentTime);
        } else {
          this.clock.useTimeSource(() => performance.now() / 1000);
          if (this.enabled) this.setPaused(true);
        }
      });
    }
    let buffer = this.buffers.get(file);
    if (!buffer) {
      buffer = fetch(file).then(async response => {
        if (!response.ok) throw new Error(`Music loading failed (${response.status}).`);
        return this.context!.decodeAudioData(await response.arrayBuffer());
      }).catch(error => { this.buffers.delete(file); throw error; });
      this.buffers.set(file, buffer);
    }
    return buffer;
  }

  beginSelection(style?: string): void {
    this.cancelSelection();
    if (this.track?.style !== style) this.clear();
  }

  select(sourceDuration: number, track: MusicTrack, buffer: AudioBuffer, activate: (start: number) => void = () => {}, interval?: number): Promise<boolean> {
    this.cancelSelection();
    const timing = new PhraseTiming(sourceDuration, track);
    const matching = this.timing && this.track?.style === track.style && this.buffer === buffer;
    const continuing = matching && (interval !== undefined || this.enabled && this.source && !this.clock.retrievePaused());
    this.track = track;
    if (continuing) {
      const start = this.retrieveSelectionStart(interval);
      return new Promise(complete => {
        this.selection = { timing, start, interval, activate, complete };
        this.scheduleSoundEnd();
      });
    } else {
      this.stopSound();
      this.buffer = buffer;
      this.timing = timing;
      this.motionOrigin = 0;
      this.clock.seek(0);
      this.clock.setPaused(false);
      activate(0);
      if (this.enabled) void this.setMusic(true).catch(() => {});
      else this.startSound();
      return Promise.resolve(true);
    }
  }

  clear(): void {
    this.cancelSelection();
    this.setPaused(true);
    this.buffer = undefined;
    this.timing = undefined;
    this.track = undefined;
  }

  async setMusic(enabled: boolean): Promise<void> {
    const request = ++this.soundRequest;
    this.enabled = enabled;
    if (this.selection) {
      if (!enabled && this.selection.interval === undefined) this.activateSelection(this.clock.retrieveTime());
      else this.selection.start = this.retrieveSelectionStart(this.selection.interval);
    }
    this.clock.setSpeed(enabled ? 1 : this.previewSpeed);
    this.stopSound();
    if (!enabled && this.awaitingAudio) {
      this.awaitingAudio = false;
      this.clock.setPaused(false);
    }
    if (enabled && this.context) {
      if (this.context.state !== 'running' && !this.clock.retrievePaused()) {
        this.awaitingAudio = true;
        this.clock.setPaused(true);
      }
      try {
        await this.context.resume();
        if (request === this.soundRequest && this.enabled) {
          this.clock.useTimeSource(() => this.context!.currentTime);
          if (this.awaitingAudio) {
            this.awaitingAudio = false;
            this.clock.setPaused(false);
          }
          this.startSound();
        }
      } catch (error) {
        if (request === this.soundRequest) {
          this.enabled = false;
          this.clock.setSpeed(this.previewSpeed);
          if (this.awaitingAudio) {
            this.awaitingAudio = false;
            this.clock.setPaused(false);
          }
          this.onError(error instanceof Error ? error.message : String(error));
        }
        throw error;
      }
    }
  }

  setVolume(volume: number): void {
    this.volume = Math.min(1, Math.max(0, volume));
    this.gain?.gain.setTargetAtTime(this.volume, this.context!.currentTime, .015);
  }

  setPaused(paused: boolean): void {
    if (!paused && !this.looping && !this.advancing && !this.selection && this.timing && this.clock.retrieveTime() - this.motionOrigin >= this.timing.duration) {
      this.clock.seek(0);
      this.motionOrigin = 0;
    }
    this.awaitingAudio = !paused && this.enabled && this.context?.state !== 'running';
    this.clock.setPaused(paused || this.awaitingAudio);
    this.stopSound();
    if (this.awaitingAudio) void this.setMusic(true).catch(() => {});
    else this.startSound();
  }

  setSpeed(speed: number): void {
    if (speed > 0 && Number.isFinite(speed)) {
      this.previewSpeed = speed;
      if (!this.enabled) this.clock.setSpeed(speed);
    } else {
      throw new Error('Choose a positive preview speed.');
    }
  }

  setLoop(looping: boolean, advancing = false): void {
    if (looping !== this.looping || advancing !== this.advancing) {
      const position = this.retrievePosition();
      const continuous = (this.looping || this.advancing) && (looping || advancing);
      if (this.looping && !looping) this.motionOrigin = this.clock.retrieveTime() - position.time;
      this.looping = looping;
      this.advancing = advancing;
      if (continuous) this.scheduleSoundEnd();
      else {
        this.stopSound();
        this.startSound();
      }
    }
  }

  seek(time: number): void {
    this.clock.seek(Math.min(time, this.timing?.duration ?? 0));
    this.motionOrigin = 0;
    if (this.selection) this.selection.start = this.retrieveSelectionStart(this.selection.interval);
    this.stopSound();
    this.startSound();
  }

  restart(): void {
    this.clock.seek(0);
    this.motionOrigin = 0;
    if (this.selection) this.selection.start = this.selection.interval === undefined ? 0 : this.retrieveSelectionStart(this.selection.interval);
    this.setPaused(false);
  }

  retrievePosition(): { time: number; sourceTime: number; duration: number; elapsed: number; paused: boolean } {
    const elapsed = this.clock.retrieveTime();
    if (this.selection && !this.clock.retrievePaused() && elapsed >= this.selection.start) this.activateSelection(this.selection.start);
    if (this.timing) {
      const position = this.timing.retrievePosition(elapsed - this.motionOrigin, this.looping);
      if (position.finished && !this.selection && !this.advancing && !this.clock.retrievePaused()) {
        this.clock.seek(this.motionOrigin + this.timing.duration);
        this.setPaused(true);
      }
      return { ...position, duration: this.timing.duration, elapsed, paused: this.clock.retrievePaused() };
    } else {
      return { time: 0, sourceTime: 0, duration: 0, elapsed, paused: true };
    }
  }

  private startSound(): void {
    if (this.enabled && this.buffer && this.timing && this.context?.state === 'running' && !this.clock.retrievePaused()) {
      const elapsed = this.clock.retrieveTime();
      const remaining = this.retrieveSoundEnd() - elapsed;
      if (this.looping || this.advancing || remaining > 0) {
        const source = this.context.createBufferSource();
        source.buffer = this.buffer;
        source.loop = true;
        source.playbackRate.value = 1;
        source.connect(this.gain!);
        const start = this.context.currentTime;
        source.start(start, elapsed % this.buffer.duration);
        this.source = source;
        this.scheduleSoundEnd();
      }
    }
  }

  private retrieveSoundEnd(): number {
    return this.selection ? this.selection.start + this.selection.timing.duration : this.motionOrigin + (this.timing?.duration ?? 0);
  }

  private retrieveSelectionStart(interval?: number): number {
    const bar = this.track!.meter * 60 / this.track!.tempo;
    const elapsed = this.clock.retrieveTime();
    if (interval === undefined) {
      return (Math.floor(elapsed / bar) + 1) * bar;
    } else {
      const length = interval > 0 ? interval * bar : this.timing!.duration;
      const finish = Math.max(elapsed, this.motionOrigin + length);
      return this.enabled ? Math.ceil(finish / bar - 1e-9) * bar : finish;
    }
  }

  private scheduleSoundEnd(): void {
    if (this.source && this.context && !this.looping && !this.advancing) {
      this.source.stop(this.context.currentTime + Math.max(0, this.retrieveSoundEnd() - this.clock.retrieveTime()));
    }
  }

  private activateSelection(start: number): void {
    if (this.selection) {
      const selection = this.selection;
      this.selection = undefined;
      this.timing = selection.timing;
      this.motionOrigin = start;
      selection.activate(start);
      selection.complete(true);
      this.scheduleSoundEnd();
    }
  }

  private cancelSelection(): void {
    this.selection?.complete(false);
    this.selection = undefined;
    this.scheduleSoundEnd();
  }

  private stopSound(): void {
    if (this.source) {
      this.source.stop();
      this.source.disconnect();
      this.source = undefined;
    }
  }
}
