import { AnimationMixer, Color, DirectionalLight, HemisphereLight, LoopOnce, Mesh, MeshStandardMaterial, PerspectiveCamera, PlaneGeometry, Scene, Vector3, WebGLRenderer } from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import { clone } from 'three/addons/utils/SkeletonUtils.js';
import { bindClip, type Performer } from '../../src/clip-binding';
import { retrieveCharacterFile } from '../../src/wardrobe';

const scene = new Scene();
scene.background = new Color('#e9eef4');
const renderer = new WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
renderer.setSize(400, 440);
renderer.setPixelRatio(1);
document.body.append(renderer.domElement);
scene.add(new HemisphereLight(0xffffff, 0x71809c, 2.5));
for (const [x, y, z] of [[2,4,3], [-3,2,-2]]) {
  const light = new DirectionalLight(0xffffff, 2.5);
  light.position.set(x,y,z); scene.add(light);
}
const floor = new Mesh(new PlaneGeometry(12,12),new MeshStandardMaterial({ color:0xdce3ec, roughness:1 }));
floor.rotation.x = -Math.PI/2; floor.position.y = -.003; scene.add(floor);
const camera = new PerspectiveCamera(34,400/440,.01,100);
const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
const catalog = await fetch('/catalog.json').then(response => response.json());
const templates = new Map();
for (const actor of ['man','woman'] as const) {
  templates.set(actor, await loader.loadAsync('/'+retrieveCharacterFile(catalog,'house_dance',actor)));
}
let model, mixer, clip, current;

Object.assign(window, {
  async loadHouse(name: string) {
    const actor = name.split('_')[1] as Performer;
    if (model) scene.remove(model);
    model = clone(templates.get(actor).scene); scene.add(model);
    const source = await loader.loadAsync('/.cache/house/candidates/'+name+'.glb');
    clip = await bindClip(source,new Map([[actor,model]]));
    mixer = new AnimationMixer(model);
    const action = mixer.clipAction(clip); action.setLoop(LoopOnce,1); action.clampWhenFinished=true; action.play();
    current=name;
    return {duration:clip.duration,tracks:clip.tracks.length};
  },
  poseHouse(frame: number, angle = .35) {
    mixer.setTime(frame/24); model.updateMatrixWorld(true);
    camera.position.set(Math.sin(angle)*4.2,1.8,Math.cos(angle)*4.2);camera.lookAt(0,.85,0);
    renderer.render(scene,camera);
    document.getElementById('label')!.textContent=current+' · '+frame.toFixed(1);
    return renderer.domElement.toDataURL('image/png');
  },
});

Object.assign(window, {
  async captureHouse() {
    renderer.setSize(800,440);
    renderer.setScissorTest(true);
    const frames: string[]=[];
    for (let frame=0;frame<=96;frame+=3) {
      mixer.setTime(frame/24);model.updateMatrixWorld(true);
      for (const [index,angle] of [.25,1.4].entries()) {
        renderer.setViewport(index*400,0,400,440);renderer.setScissor(index*400,0,400,440);
        camera.position.set(Math.sin(angle)*4.2,1.8,Math.cos(angle)*4.2);camera.lookAt(0,.85,0);
        renderer.render(scene,camera);
      }
      frames.push(renderer.domElement.toDataURL('image/jpeg',.88).split(',')[1]);
      await new Promise(resolve=>setTimeout(resolve,0));
    }
    renderer.setScissorTest(false);renderer.setSize(400,440);
    return frames;
  },
});
