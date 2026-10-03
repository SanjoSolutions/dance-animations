import 'bootstrap/dist/css/bootstrap.min.css';
import './style.css';
import { assetUrl, type DanceCatalog, type DanceAnimation } from './catalog';
import { DanceViewer } from './viewer';
import { retrieveMoves, retrieveVariant, type DanceMove } from './moves';
import type { Performer } from './clip-binding';
import { retrieveAnimationData } from './animation-asset';
import type { MusicCatalog } from './music/timing';

function element<T extends HTMLElement>(id: string): T {
  const result = document.getElementById(id);
  if (!result) throw new Error(`Missing interface element: ${id}`);
  return result as T;
}
const style = element<HTMLSelectElement>('style');
const animation = element<HTMLSelectElement>('animation');
const character = element<HTMLSelectElement>('character');
const reportError = element<HTMLAnchorElement>('report-error');
const status = element('status');
const play = element<HTMLButtonElement>('play');
const restart = element<HTMLButtonElement>('restart');
const timeline = element<HTMLInputElement>('timeline');
const loop = element<HTMLInputElement>('loop');
const music = element<HTMLInputElement>('music');
const musicStatus = element('music-status');
const colorScheme = window.matchMedia('(prefers-color-scheme: dark)');
function applyTheme(): void {
  document.documentElement.dataset.bsTheme = colorScheme.matches ? 'dark' : 'light';
}
applyTheme();
colorScheme.addEventListener('change', applyTheme);
let viewer: DanceViewer;
let paused = false;
let selection = 0;

function timeLabel(time: number): string {
  return `${Math.floor(time / 60)}:${(time % 60).toFixed(1).padStart(4, '0')}`;
}

function retrieveReportUrl(entry: DanceAnimation): string {
  const demoUrl = new URL('https://sanjosolutions.github.io/dance-animations/');
  demoUrl.searchParams.set('style', entry.style);
  demoUrl.searchParams.set('animation', entry.id);
  if (entry.performers.length === 1) demoUrl.searchParams.set('character', entry.performers[0]);
  const issueUrl = new URL('https://github.com/SanjoSolutions/dance-animations/issues/new');
  issueUrl.searchParams.set('title', `Animation error: ${entry.label}`);
  issueUrl.searchParams.set('body', `Animation: ${entry.label} (${entry.id})\nDemo: ${demoUrl.href}\n\n`);
  return issueUrl.href;
}

async function initialize(): Promise<void> {
  const response = await fetch(assetUrl('catalog.json'));
  if (!response.ok) throw new Error(`Could not load the library (${response.status}).`);
  const catalog = await response.json() as DanceCatalog;
  const musicResponse = await fetch(assetUrl('music.json'));
  if (!musicResponse.ok) throw new Error(`Could not load the music library (${musicResponse.status}).`);
  const musicCatalog = await musicResponse.json() as MusicCatalog;
  const tracks = new Map(musicCatalog.tracks.map(track => [track.style, track]));
  element('catalog-count').textContent = `${catalog.styles.length} styles · ${catalog.animations.length.toLocaleString()} animations`;
  element('source-count').textContent = `${catalog.sourceCount.toLocaleString()} editable sources; ${catalog.sourceOnlyCount.toLocaleString()} with a runtime export pending.`;
  const entries = new Map<string, DanceAnimation>(catalog.animations.map(entry => [entry.id, entry]));
  let moves: DanceMove[] = [];
  let preferredCharacter: Performer = 'man';
  for (const entry of catalog.styles) {
    style.add(new Option(`${entry.label} (${entry.playable})`, entry.id));
  }
  viewer = new DanceViewer(element('viewport'));
  await viewer.initialize(catalog);
  viewer.onMusicError = message => {
    music.checked = false;
    musicStatus.hidden = false;
    musicStatus.textContent = message;
  };
  viewer.onTime = (time, duration, isPaused) => {
    paused = isPaused;
    play.textContent = isPaused ? 'Play' : 'Pause';
    timeline.max = String(duration);
    if (document.activeElement !== timeline) timeline.value = String(time);
    element('time').textContent = `${timeLabel(time)} / ${timeLabel(duration)}`;
  };

  async function selectAnimation(pushHistory = true): Promise<void> {
    const token = ++selection;
    const move = moves.find(move => move.id === animation.value);
    const entry = move ? retrieveVariant(move, character.value as Performer || preferredCharacter) : undefined;
    viewer.clear();
    play.disabled = restart.disabled = timeline.disabled = true;
    music.disabled = true;
    status.hidden = false;
    status.textContent = entry ? 'Loading animation…' : 'This style has editable sources with runtime exports pending. See the source inventory.';
    element<HTMLAnchorElement>('download').hidden = true;
    element<HTMLAnchorElement>('source').hidden = true;
    reportError.hidden = !entry;
    if (entry) reportError.href = retrieveReportUrl(entry);
    element<HTMLAnchorElement>('music-download').hidden = true;
    if (!entry) return;
    if (pushHistory) {
      const url = new URL(location.href);
      url.searchParams.set('style', entry.style);
      url.searchParams.set('animation', entry.id);
      if (move?.solo) url.searchParams.set('character', character.value);
      else url.searchParams.delete('character');
      if (url.href !== location.href) history.pushState(null, '', url);
    }
    try {
      const track = tracks.get(entry.style);
      if (!track) throw new Error(`Choose a music track for ${entry.style}.`);
      const applied = await viewer.select(entry, track);
      if (!applied || token !== selection) return;
      status.hidden = true;
      play.disabled = restart.disabled = timeline.disabled = false;
      music.disabled = false;
      element('performers').textContent = entry.performers.map(actor => actor[0].toUpperCase() + actor.slice(1)).join(' + ');
      element('duration').textContent = `${entry.duration.toFixed(2)} s`;
      element('export-status').textContent = entry.status;
      element('music-title').textContent = track.title;
      element('music-tempo').textContent = `${track.tempo.toFixed(2).replace(/\.00$/, '')} BPM · ${track.meter === 12 ? '12-beat compás' : `${track.meter}/4`} · ${track.license}`;
      const musicDownload = element<HTMLAnchorElement>('music-download');
      musicDownload.href = assetUrl(track.file);
      musicDownload.download = `${track.style}.wav`;
      musicDownload.hidden = false;
      const download = element<HTMLAnchorElement>('download');
      download.href = assetUrl(entry.file);
      download.download = `${entry.id}.glb`;
      download.onclick = entry.transportFile ? event => {
        event.preventDefault();
        void retrieveAnimationData(entry).then(data => {
          const url = URL.createObjectURL(new Blob([data], { type: 'model/gltf-binary' }));
          const link = document.createElement('a');
          link.href = url;
          link.download = `${entry.id}.glb`;
          link.hidden = true;
          document.body.append(link);
          link.click();
          link.remove();
          setTimeout(() => URL.revokeObjectURL(url), 1000);
        }).catch(error => { status.hidden = false; status.textContent = String(error); });
      } : null;
      download.hidden = false;
      const source = element<HTMLAnchorElement>('source');
      if (entry.sourceFile) {
        // Blender archives are in the repository; only runtime clips go to Pages.
        const onPages = location.hostname.endsWith('.github.io');
        source.href = onPages
          ? `https://github.com/${location.hostname.split('.')[0]}/dance-animations/blob/main/${entry.sourceFile}`
          : assetUrl(entry.sourceFile);
        source.hidden = false;
      }
    } catch (error) {
      if (token === selection) status.textContent = error instanceof Error ? error.message : String(error);
    }
  }

  function selectMove(pushHistory = true): void {
    const move = moves.find(move => move.id === animation.value);
    element('character-field').hidden = !move?.solo;
    const actors = (['man', 'woman'] as const).filter(actor => move?.variants.some(entry => entry.performers.length === 1 && entry.performers[0] === actor));
    character.replaceChildren(...actors.map(actor => new Option(actor === 'man' ? 'Man' : 'Woman', actor)));
    if (actors.includes(preferredCharacter)) character.value = preferredCharacter;
    character.disabled = actors.length < 2;
    void selectAnimation(pushHistory);
  }
  function selectStyle(preferred?: string, pushHistory = true): void {
    moves = retrieveMoves(catalog.animations, style.value);
    animation.replaceChildren(...moves.map(move => new Option(move.label, move.id)));
    animation.disabled = moves.length === 0;
    const preferredMove = moves.find(move => move.id === preferred || move.variants.some(entry => entry.id === preferred));
    if (preferredMove) animation.value = preferredMove.id;
    selectMove(pushHistory);
  }
  function restoreSelection(): void {
    const parameters = new URLSearchParams(location.search);
    const preferred = entries.get(parameters.get('animation') ?? '');
    const parameterCharacter = parameters.get('character');
    preferredCharacter = parameterCharacter === 'man' || parameterCharacter === 'woman' ? parameterCharacter
      : preferred?.performers.length === 1 ? preferred.performers[0] : 'man';
    style.value = preferred?.style ?? parameters.get('style') ?? 'hip_hop';
    if (!style.value) style.selectedIndex = 0;
    selectStyle(parameters.get('animation') ?? undefined, false);
  }
  style.disabled = false;
  style.addEventListener('change', () => selectStyle());
  animation.addEventListener('change', () => selectMove());
  character.addEventListener('change', () => { preferredCharacter = character.value as Performer; void selectAnimation(); });
  window.addEventListener('popstate', restoreSelection);
  restoreSelection();
  play.addEventListener('click', () => viewer.setPaused(!paused));
  restart.addEventListener('click', () => viewer.restart());
  loop.addEventListener('change', () => viewer.setLoop(loop.checked));
  element<HTMLSelectElement>('speed').addEventListener('change', event => viewer.setSpeed(Number((event.target as HTMLSelectElement).value)));
  timeline.addEventListener('input', () => { viewer.setPaused(true); viewer.seek(Number(timeline.value)); });
  music.addEventListener('change', () => {
    musicStatus.hidden = true;
    void viewer.setMusic(music.checked).catch(error => {
      music.checked = false;
      musicStatus.hidden = false;
      musicStatus.textContent = error instanceof Error ? error.message : String(error);
    });
  });
  element<HTMLInputElement>('volume').addEventListener('input', event => viewer.setVolume(Number((event.target as HTMLInputElement).value)));
}

initialize().catch(error => {
  status.hidden = false;
  status.textContent = error instanceof Error ? error.message : String(error);
});
