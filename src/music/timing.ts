export interface MusicTrack {
  style: string;
  title: string;
  file: string;
  /** Quarter-note beats per minute. */
  tempo: number;
  /** Authored motion tempo in quarter-note beats per minute. */
  animationTempo: number;
  meter: number;
  beats: number;
  /** In seconds. */
  duration: number;
  license: string;
  licenseFile: string;
  author: string;
  composer: string;
  contributors: string;
  source: string;
  licenseUrl: string;
  fit: string;
  /** Automatic move interval in bars; zero uses each animation's duration. */
  changeInterval: number;
  timingBasis: string;
  /** Closing pose hold in seconds, excluded from cyclic sampling. */
  endingHold: number;
}

export interface MusicCatalog { tracks: MusicTrack[] }

export class PhraseTiming {
  readonly beats: number;
  /** Performance phrase duration in seconds. */
  readonly duration: number;
  /** Source sampling duration in seconds. */
  readonly sourceDuration: number;

  constructor(sourceDuration: number, track: MusicTrack) {
    this.sourceDuration = Math.max(sourceDuration - track.endingHold, .001);
    this.beats = Math.max(.5, Math.round(this.sourceDuration * track.animationTempo / 60 * 2) / 2);
    this.duration = this.beats * 60 / track.tempo;
  }

  retrievePosition(elapsed: number, looping: boolean): { time: number; sourceTime: number; finished: boolean } {
    const finished = !looping && elapsed >= this.duration;
    const time = looping ? elapsed % this.duration : Math.min(elapsed, this.duration);
    return { time, sourceTime: time / this.duration * this.sourceDuration, finished };
  }
}

/** A single anchored clock drives audio offsets and animation sampling. */
export class PlaybackClock {
  private position = 0;
  private anchor = 0;
  private speed = 1;
  private paused = true;
  private readTime: () => number;

  constructor(readTime: () => number) { this.readTime = readTime; }

  retrieveTime(): number {
    return this.position + (this.paused ? 0 : (this.readTime() - this.anchor) * this.speed);
  }

  retrievePaused(): boolean { return this.paused; }
  retrieveSpeed(): number { return this.speed; }

  setPaused(paused: boolean): void {
    this.position = this.retrieveTime();
    this.anchor = this.readTime();
    this.paused = paused;
  }

  setSpeed(speed: number): void {
    if (speed > 0 && Number.isFinite(speed)) {
      this.position = this.retrieveTime();
      this.anchor = this.readTime();
      this.speed = speed;
    } else {
      throw new Error('Choose a positive playback speed.');
    }
  }

  seek(position: number): void {
    this.position = Math.max(0, position);
    this.anchor = this.readTime();
  }

  useTimeSource(readTime: () => number): void {
    this.position = this.retrieveTime();
    this.readTime = readTime;
    this.anchor = this.readTime();
  }
}
