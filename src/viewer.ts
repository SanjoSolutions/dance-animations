import {
  AnimationAction, AnimationMixer, Box3, Color, DirectionalLight, Group,
  HemisphereLight, LoopOnce, LoopRepeat, Mesh, MeshStandardMaterial,
  Object3D, PerspectiveCamera, PlaneGeometry, Scene, Vector3, WebGLRenderer,
  GridHelper, SRGBColorSpace, ACESFilmicToneMapping,
} from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader, type GLTF } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import { clone } from 'three/addons/utils/SkeletonUtils.js';
import { bindClip, type Performer } from './clip-binding';
import { assetUrl, type DanceAnimation, type DanceCatalog } from './catalog';
import { retrieveAnimationData } from './animation-asset';
import { retrieveCharacterFile } from './wardrobe';

export class DanceViewer {
  private readonly renderer = new WebGLRenderer({ antialias: true });
  private readonly scene = new Scene();
  private readonly camera = new PerspectiveCamera(38, 1, .01, 100);
  private readonly controls: OrbitControls;
  private readonly loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
  private readonly templates = new Map<string, Promise<GLTF>>();
  private catalog?: DanceCatalog;
  private readonly props: { template: GLTF; styles: string[] }[] = [];
  private group?: Group;
  private mixer?: AnimationMixer;
  private action?: AnimationAction;
  private request = 0;
  private previous = 0;
  private speed = 1;
  private looping = true;
  private paused = false;
  onTime: (time: number, duration: number, paused: boolean) => void = () => {};

  constructor(private readonly container: HTMLElement) {
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.outputColorSpace = SRGBColorSpace;
    this.renderer.toneMapping = ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1.2;
    this.scene.background = new Color('#171e29');
    this.container.append(this.renderer.domElement);
    this.camera.position.set(3, 2, 5);
    this.controls = new OrbitControls(this.camera, this.renderer.domElement);
    this.controls.enableDamping = true;
    this.controls.minDistance = 1;
    this.controls.maxDistance = 30;
    this.scene.add(new HemisphereLight(0xe5efff, 0x4e5c74, 2.5));
    const key = new DirectionalLight(0xffffff, 3);
    key.position.set(2, 5, 4);
    this.scene.add(key);
    const rim = new DirectionalLight(0xb1eb68, 1.3);
    rim.position.set(-3, 3, -2);
    this.scene.add(rim);
    const floor = new Mesh(new PlaneGeometry(200, 200), new MeshStandardMaterial({ color: 0x202a39, roughness: 1 }));
    floor.rotation.x = -Math.PI / 2;
    floor.position.y = -.015;
    this.scene.add(floor);
    const grid = new GridHelper(20, 40, 0x536171, 0x323e50);
    grid.position.y = -.01;
    this.scene.add(grid);
    const preference = window.matchMedia('(prefers-color-scheme: dark)');
    const applyTheme = () => {
      this.scene.background = new Color(preference.matches ? '#171e29' : '#e9eef4');
      (floor.material as MeshStandardMaterial).color.set(preference.matches ? '#202a39' : '#dce3ec');
    };
    applyTheme();
    preference.addEventListener('change', applyTheme);
    new ResizeObserver(() => this.resize()).observe(container);
    this.resize();
    this.renderer.setAnimationLoop(timestamp => this.render(timestamp));
  }

  async initialize(catalog: DanceCatalog): Promise<void> {
    this.catalog = catalog;
    await Promise.all(Object.values(catalog.props ?? {}).map(async prop => {
      this.props.push({ template: await this.loader.loadAsync(assetUrl(prop.file)), styles: prop.styles });
    }));
  }

  async select(entry: DanceAnimation): Promise<boolean> {
    const request = ++this.request;
    const source = await this.loader.parseAsync(await retrieveAnimationData(entry), '');
    if (request !== this.request) return false;
    const catalog = this.catalog;
    if (!catalog) throw new Error('Load the dance catalog before selecting an animation.');
    const templates = await Promise.all(entry.performers.map(actor => {
      const file = retrieveCharacterFile(catalog, entry.style, actor);
      let template = this.templates.get(file);
      if (!template) {
        template = this.loader.loadAsync(assetUrl(file)).catch(error => {
          this.templates.delete(file);
          throw error;
        });
        this.templates.set(file, template);
      }
      return template;
    }));
    if (request !== this.request) return false;
    const next = new Group();
    const performers = new Map<Performer, Object3D>();
    for (const [index, actor] of entry.performers.entries()) {
      const template = templates[index];
      const model = clone(template.scene);
      next.add(model);
      performers.set(actor, model);
    }
    const clip = await bindClip(source, performers);
    for (const prop of this.props.filter(prop => prop.styles.includes(entry.style))) next.add(clone(prop.template.scene));
    if (request !== this.request) return false;
    const mixer = new AnimationMixer(next);
    const action = mixer.clipAction(clip);
    action.setLoop(this.looping ? LoopRepeat : LoopOnce, this.looping ? Infinity : 1);
    action.clampWhenFinished = true;
    action.play();
    mixer.setTime(0);
    // Fit the camera to a few positions throughout the phrase, preserving the
    // authored distance between partners and the character's floor height.
    const bounds = new Box3();
    for (const fraction of [0, .25, .5, .75, 1]) {
      mixer.setTime(clip.duration * fraction);
      next.updateMatrixWorld(true);
      bounds.union(new Box3().setFromObject(next, true));
    }
    mixer.setTime(0);
    const center = bounds.getCenter(new Vector3());
    next.position.set(-center.x, 0, -center.z);
    if (this.group) this.scene.remove(this.group);
    if (this.mixer && this.group) {
      this.mixer.stopAllAction();
      this.mixer.uncacheRoot(this.group);
    }
    this.group = next;
    this.mixer = mixer;
    this.action = action;
    this.scene.add(next);
    this.paused = false;
    const size = bounds.getSize(new Vector3());
    const distance = Math.max(size.y, size.x / this.camera.aspect, size.z, 1.6) * 2;
    this.controls.target.set(0, center.y, 0);
    this.camera.position.set(distance * .32, center.y + distance * .15, distance);
    this.controls.update();
    return true;
  }

  setPaused(paused: boolean): void { this.paused = paused; }
  setSpeed(speed: number): void { this.speed = speed; }
  setLoop(looping: boolean): void {
    this.looping = looping;
    this.action?.setLoop(looping ? LoopRepeat : LoopOnce, looping ? Infinity : 1);
    if (this.action?.paused) this.seek(0);
  }
  seek(time: number): void {
    if (this.action && this.mixer) {
      this.action.paused = false;
      this.action.enabled = true;
      this.action.time = Math.max(0, Math.min(time, this.action.getClip().duration));
      this.mixer.update(0);
    }
  }
  restart(): void {
    this.action?.reset().play();
    this.paused = false;
    this.mixer?.update(0);
  }

  private resize(): void {
    const width = Math.max(this.container.clientWidth, 1);
    const height = Math.max(this.container.clientHeight, 1);
    this.camera.aspect = width / height;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(width, height, false);
  }

  private render(timestamp: number): void {
    const elapsed = this.previous ? Math.min((timestamp - this.previous) / 1000, .1) : 0;
    this.previous = timestamp;
    if (!this.paused) this.mixer?.update(elapsed * this.speed);
    if (this.action) this.onTime(this.action.time, this.action.getClip().duration, this.paused || this.action.paused);
    this.controls.update();
    this.renderer.render(this.scene, this.camera);
  }
}
