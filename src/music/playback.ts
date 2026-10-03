import { PhraseTiming, PlaybackClock, type MusicTrack } from './timing.ts';

export class DancePlayback {
  private readonly clock = new PlaybackClock(() => performance.now() / 1000);
  private context?: AudioContext;
  private gain?: GainNode;
  private source?: AudioBufferSourceNode;
  private buffer?: AudioBuffer;
  private readonly buffers = new Map<string, Promise<AudioBuffer>>();
  private timing?: PhraseTiming;
  private enabled = false;
  private looping = true;
  private volume = .65;
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

  select(sourceDuration: number, track: MusicTrack, buffer: AudioBuffer): void {
    this.stopSound();
    this.buffer = buffer;
    this.timing = new PhraseTiming(sourceDuration, track);
    this.clock.seek(0);
    this.clock.setPaused(false);
    this.startSound();
  }

  clear(): void {
    this.setPaused(true);
    this.buffer = undefined;
    this.timing = undefined;
  }

  async setMusic(enabled: boolean): Promise<void> {
    const request = ++this.soundRequest;
    this.enabled = enabled;
    this.stopSound();
    if (enabled && this.context) {
      try {
        await this.context.resume();
        if (request === this.soundRequest && this.enabled) {
          this.clock.useTimeSource(() => this.context!.currentTime);
          this.startSound();
        }
      } catch (error) {
        if (request === this.soundRequest) {
          this.enabled = false;
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
    if (!paused && !this.looping && this.timing && this.clock.retrieveTime() >= this.timing.duration) {
      this.clock.seek(0);
    }
    this.clock.setPaused(paused);
    this.stopSound();
    this.startSound();
  }

  setSpeed(speed: number): void {
    this.clock.setSpeed(speed);
    this.stopSound();
    this.startSound();
  }

  setLoop(looping: boolean): void {
    const position = this.retrievePosition();
    this.looping = looping;
    this.clock.seek(position.time);
    this.stopSound();
    this.startSound();
  }

  seek(time: number): void {
    this.clock.seek(Math.min(time, this.timing?.duration ?? 0));
    this.stopSound();
    this.startSound();
  }

  restart(): void {
    this.clock.seek(0);
    this.setPaused(false);
  }

  retrievePosition(): { time: number; sourceTime: number; duration: number; paused: boolean } {
    if (this.timing) {
      const position = this.timing.retrievePosition(this.clock.retrieveTime(), this.looping);
      if (position.finished && !this.clock.retrievePaused()) {
        this.clock.seek(this.timing.duration);
        this.setPaused(true);
      }
      return { ...position, duration: this.timing.duration, paused: this.clock.retrievePaused() };
    } else {
      return { time: 0, sourceTime: 0, duration: 0, paused: true };
    }
  }

  private startSound(): void {
    if (this.enabled && this.buffer && this.timing && this.context?.state === 'running' && !this.clock.retrievePaused()) {
      const elapsed = this.clock.retrieveTime();
      const remaining = this.timing.duration - elapsed;
      if (this.looping || remaining > 0) {
        const source = this.context.createBufferSource();
        source.buffer = this.buffer;
        source.loop = true;
        source.playbackRate.value = this.clock.retrieveSpeed();
        source.connect(this.gain!);
        const start = this.context.currentTime;
        source.start(start, elapsed % this.buffer.duration);
        if (!this.looping) source.stop(start + remaining / this.clock.retrieveSpeed());
        this.source = source;
      }
    }
  }

  private stopSound(): void {
    if (this.source) {
      this.source.stop();
      this.source.disconnect();
      this.source = undefined;
    }
  }
}
