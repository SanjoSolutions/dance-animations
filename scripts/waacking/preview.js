import * as THREE from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {MeshoptDecoder} from 'three/addons/libs/meshopt_decoder.module.js';
import {clone} from 'three/addons/utils/SkeletonUtils.js';
import {bindClip} from '/src/clip-binding.ts';

class ClipPreview {
  constructor(entry, model, animation, report) {
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color('#303640');
    this.scene.add(model);
    model.traverse(object => {
      if (object.isMesh) object.material = new THREE.MeshStandardMaterial({
        color: entry.performers[0] === 'man' ? 0x97bec9 : 0xceb7a6,
        roughness: .8, side: THREE.DoubleSide,
      });
    });
    this.scene.add(new THREE.HemisphereLight(0xffffff, 0x3d4658, 2));
    const light = new THREE.DirectionalLight(0xffffff, 3);
    light.position.set(2, 4, 3);
    this.scene.add(light);
    const floor = new THREE.Mesh(new THREE.PlaneGeometry(4, 4), new THREE.MeshStandardMaterial({color: 0x414954}));
    floor.rotation.x = -Math.PI / 2;
    floor.position.y = -.002;
    this.scene.add(floor, new THREE.GridHelper(3, 12, 0x728090, 0x4b5563));
    this.camera = new THREE.PerspectiveCamera(38, 1, .01, 20);
    this.mixer = new THREE.AnimationMixer(model);
    this.mixer.clipAction(animation).setLoop(THREE.LoopRepeat, Infinity).play();
    const label = document.createElement('div');
    label.className = 'clip-label';
    label.textContent = entry.id.replace('waacking_', '').replaceAll('_', ' ') + (report ? ' · candidate' : ' · saved clip');
    label.dataset.id = entry.id;
    label.dataset.source = report?.sourceSha256 || entry.sourceSha256;
    label.dataset.export = report?.exportSha256 || entry.exportSha256 || '';
    document.querySelector('#labels').append(label);
  }

  render(renderer, time, view, width, height) {
    this.camera.aspect = width / height;
    this.camera.position.set(view === 'side' ? 3.2 : 0, 1, view === 'back' ? -3.2 : view === 'side' ? 0 : 3.2);
    this.camera.lookAt(0, .95, 0);
    this.camera.updateProjectionMatrix();
    this.mixer.setTime(Math.max(0, time));
    renderer.render(this.scene, this.camera);
  }
}

class PlaybackReview {
  constructor(clips) {
    this.clips = clips;
    this.renderer = new THREE.WebGLRenderer({canvas: document.querySelector('canvas'), antialias: true});
    this.renderer.setPixelRatio(1);
    this.renderer.setScissorTest(true);
    this.playing = true;
    this.time = 0;
    this.previous = 0;
    this.input = document.querySelector('#time');
    this.view = document.querySelector('#view');
    document.querySelector('#play').onclick = () => this.selectPlayback(!this.playing);
    this.input.oninput = () => { this.selectPlayback(false); this.time = Number(this.input.value); };
    document.querySelector('#status').textContent = `${clips.length} MPFB clips · 4 seconds · 120 BPM`;
    requestAnimationFrame(time => this.draw(time));
  }

  selectPlayback(playing) {
    this.playing = playing;
    document.querySelector('#play').textContent = playing ? 'Pause' : 'Play';
  }

  draw(now) {
    if (this.playing && this.previous) this.time = (this.time + Math.max(0, now - this.previous) / 1000) % 4;
    this.previous = now;
    this.input.value = String(this.time);
    document.querySelector('#seconds').textContent = this.time.toFixed(2) + ' s';
    const width = this.renderer.domElement.clientWidth, height = this.renderer.domElement.clientHeight;
    this.renderer.setSize(width, height, false);
    const tileWidth = width / 4, tileHeight = height / 4;
    this.clips.forEach((clip, index) => {
      const x = (index % 4) * tileWidth, y = (3 - Math.floor(index / 4)) * tileHeight;
      this.renderer.setViewport(x, y, tileWidth, tileHeight);
      this.renderer.setScissor(x, y, tileWidth, tileHeight);
      clip.render(this.renderer, this.time, this.view.value, tileWidth, tileHeight);
    });
    requestAnimationFrame(time => this.draw(time));
  }
}

const catalog = await fetch('/catalog.json').then(response => response.json());
const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
const templates = new Map(await Promise.all(['man', 'woman'].map(async actor => [actor, (await loader.loadAsync('/' + catalog.models[actor].file)).scene])));
const clips = [];
for (const entry of catalog.animations.filter(entry => entry.style === 'waacking')) {
  const response = await fetch(`/.cache/motion-recovery/${entry.id}/checkpoint.json`);
  const report = response.ok && response.headers.get('content-type')?.includes('application/json') ? await response.json() : null;
  const actor = entry.performers[0], model = clone(templates.get(actor));
  const source = await loader.loadAsync('/' + (report?.export || entry.file).replaceAll('\\', '/'));
  clips.push(new ClipPreview(entry, model, await bindClip(source, new Map([[actor, model]])), report));
}
new PlaybackReview(clips);
