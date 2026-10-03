# Music

Every catalog style has human-composed music by Kevin MacLeod from Incompetech.
The library contains 50 publisher recordings and 50 prepared excerpts for the
92 styles. Related styles share recordings. Salsa, samba, tango, waltz, swing,
disco, funk, country, and several other styles have genre matches. Broader
rhythm matches carry an explicit practice accompaniment description in the
player, including Amapiano, Bachata, Flamenco, Forró, Kizomba, and Semba.
Styles named after songs use practice accompaniments.

## Rights and provenance

The recordings use [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
including commercial use, adaptation, and redistribution with attribution,
a license link, and an indication of changes. The player links the artist's
track page and license. `licenses.html#music` and
`public/third-party/music-notices.txt` contain complete credits, contributors,
style assignments, changes, and source hashes. Guitar credits for OctoBlues
and Maccary Bay include Brett Van Donsel. Preserve these credits with exports
or redistributed audio. The project's MIT-0 license covers its original code.

`assets/music/selections.json` records the publisher's track identifiers,
download URLs, publication dates, instruments, source hashes, license evidence,
human-creation evidence, pulse measurements, and style choices. All selected
recordings were published between 2003 and 2019. In his
[production history](https://incompetech.com/wordpress/2025/07/the-ai-elephant-in-the-room/),
MacLeod dates his first use of music AI to 2020. This selection uses that
dated evidence for human creation. Human compositions include sampled and
synthesized instruments.

`music.json` carries the runtime tracks, author credits, sources, adaptations,
source and excerpt SHA-256 hashes, measured tempos, meters, loop boundaries,
and motion timing references. Eight-bar excerpts provide repeated practice
accompaniment; OctoBlues uses a twelve-bar blues phrase. Each file is mono
22,050 Hz 16-bit PCM WAV, peak normalized with 8-millisecond edge fades.
The excerpts preserve the recordings' tempo and pitch. Motion adapts to music.

## Preparation

Download verified originals into the local cache:

```powershell
powershell -File scripts/music/download.ps1
```

The downloader checks each recording's pinned SHA-256. Publisher originals
stay in `.cache/music-sources/`; prepared excerpts belong in regular Git under
the project's 100 MiB size threshold. Builds copy the referenced excerpts,
manifest, selection evidence, and attribution notices.

Run `npm run music:prepare` with Python, NumPy, and FFmpeg on PATH to reproduce
the excerpts. `scripts/music/analyze.py` supplies editable tempo and starting
beat measurements when selecting recordings. It searches around the
publisher tempo using spectral onsets and bass accents. The selected steady
pulse replaces rubato candidates. Measurements are pinned in the selection
file; preparation uses those measurements rather than reanalyzing.
FFmpeg versions can produce slightly different decoded samples, so review
changed output hashes when regenerating with a different decoder.

## Playback timing

Motion's authored tempo and the recording's measured tempo are separate
values. A source phrase keeps its authored beat count and is sampled over
the corresponding number of beats at the music tempo. For example, a
four-beat Hip hop source at 96 BPM takes 2.5 seconds; playback against
Basic Implosion at 95 BPM takes about 2.53 seconds. This preserves its
quarter-beat positions when changing the accompaniment.

Music and motion share one transport clock. Active sound uses Web Audio's
clock; the browser clock supplies timing while audio is suspended. Pause freezes both, seek
places both at the selected phrase position, and restart starts both at
the excerpt's measured starting beat. Music plays at its recorded rate and
sets the dance tempo. The speed control applies to silent preview. The music
continues across repeated move cycles. The timeline shows the fitted
performance duration; asset details retain the source duration. Sound
is enabled by default at 50% volume. Playback attempts to start automatically; a browser
that requires a user gesture keeps the transport at Play until that gesture
starts the music and motion together.

Changing moves within the same style retains the active recording and its
clock. The current move continues while the next asset loads. The next move
starts on the first beat of the following musical measure, with its phrase
position measured from that point. Successive choices replace queued moves;
pause retains their phase. Style changes select a fresh recording. With
silent or paused playback, choosing a move starts it immediately.

Same-style moves with the same performers reuse their characters, scene,
props, mixer, camera framing, and orbit position. A short blend from the visible
pose introduces the incoming animation on the shared transport clock. The blend
takes up to half a beat, capped at 0.35 seconds and half the new phrase. Pause
freezes it; seek and restart select the active clip's pose directly. Compatible
solo moves retain their floor-plane root position. Partner moves retain a shared
root center and use the new move's authored spacing. Prop-based dances use the
incoming clip's authored root placement to preserve the prop relationship.
Changing performer configurations updates the characters and keeps the camera
for the current style. Style changes establish fresh framing.

Playback mode offers Single, Sequential, and Random, with Random as the default. Single uses the selected
animation and Loop preference. Sequential advances in selector order and
cycles to the first move. Random chooses a move from the same style. Both
automatic modes prepare the next clip, character, and bound animation while
the current move plays. Activation follows the transport clock, including
correct sampling when a render frame arrives after the scheduled boundary.

House defaults to 16 bars per move. Each style has a `changeInterval` default
in `assets/music/selections.json` (in bars). The Bars per move field overrides
the current style's value and saves it in browser storage. Zero uses the
animation duration. Positive values repeat the current move until that many
bars have elapsed. A late asset keeps the current preview and recording
active, then joins at the following musical measure. Pause preserves the
scheduled selection; Restart restarts its interval.

The URL's `mode` parameter holds `single`, `sequential`, or `random`. Changing
Playback mode pushes browser history. Automatic move changes replace the
current history entry. Back and Forward restore the style, move, character,
and mode.

Music, volume, and Playback mode choices are saved in local storage and restored
on future visits. Each style's bars per move is saved independently. A valid
URL mode takes priority over the saved mode; a fresh browser starts with Random,
music enabled, and 50% volume. Browser storage access failures retain preferences
for the current session.

Timing references accompany each style selection. Existing authored tempo
calibrations remain applicable, including Quickstep's exported 160 BPM
and Nightclub Two-Step's exported 72 BPM. Tutting trims its final four-frame
hold from cyclic playback, preserving its authored shape-marker spacing.
The Blender and GLB bytes retain their provenance and historical review state.

Validation covers every style's music, all clips' authored beat counts and
fitted cycles, shared transport behavior, waveform levels, loop boundaries,
source and output hashes, credits, and distribution. This establishes the
playback timing stage. Authored control quality, saved source playback,
deformation bakes, and pose-by-pose musical interpretation are separate review
stages. The procedural-study classifications remain applicable.
