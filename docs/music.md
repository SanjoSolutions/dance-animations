# Music

Every catalog style has an original eight-bar instrumental practice loop in
`assets/music/<style>.wav`. Codex composed these arrangements for the project.
The renderer synthesizes every instrument mathematically. The music uses the
project's MIT-0 license, including commercial use, modification, and redistribution.
The compositions use original melodic motifs, bass lines, chord progressions,
and percussion. Styles named after songs have original practice accompaniments.

`music.json` records every title, style, tempo, meter, beat count, duration,
SHA-256 hash, arrangement, license, and timing reference. The music files are
22,050 Hz mono, 16-bit PCM WAVs. Each file belongs in regular Git according to
the project's 100 MiB size threshold. Builds include the tracks and manifest.

`assets/music/arrangements.json` is the editable score configuration. Run
`npm run music:compose` to reproduce all tracks with NumPy. A style-specific
seed gives each arrangement its own melodic motif and key. Instrument tails
wrap around the track boundary, creating periodic sample data. Waltzes and
Mazurka use triple meter; Flamenco has a twelve-beat accent cycle; other
arrangements use four-beat bars. These synthesized practice arrangements provide
style-inspired accompaniment for the procedural studies.

The preview samples motion and plays audio from one transport clock. With sound
active, Web Audio supplies the clock. Silent preview uses the browser clock.
Pause freezes both, seek places both at the chosen phrase position, and restart
starts both on the downbeat. Speed changes update the same clock and the audio
playback rate; audio pitch follows playback speed. The full music arrangement
continues across repeated move cycles. Each move repeats on a half-beat boundary,
while the original poses are sampled across the fitted duration. The timeline
shows the fitted performance duration; the asset details retain the source duration.
The sound control starts audio through a browser user gesture.

Track tempos follow the authored timing where the review records supply it.
Timing references live beside the individual arrangements. Other arrangements
use an explicit practice tempo and half-beat phrase fitting. Quickstep's exported
frame timing corresponds to 160 BPM (200 planned BPM at 30 fps, exported at
24 fps). Nightclub Two-Step corresponds to 72 BPM by the same conversion from
90 planned BPM. Slow Waltz uses 90 quarter-note beats per minute, or 30 bars per
minute. Tutting trims its final four-frame hold from cyclic playback, preserving
its one-second shape-marker spacing. The Blender and GLB asset bytes retain
their existing provenance and historical review state.

Validation covers every style's track, every clip's fitted beat cycle, the shared
transport behavior, waveform levels, periodic boundaries, hashes, and distribution.
Musical synchronization is a playback timing stage. Authored control quality,
saved source playback, deform bakes, and the source records' visual review remain
separate validation stages. The procedural-study classifications remain applicable.
