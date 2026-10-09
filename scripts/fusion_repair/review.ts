import {AnimationMixer,Color,DirectionalLight,Group,HemisphereLight,LoopOnce,Mesh,MeshStandardMaterial,PerspectiveCamera,PlaneGeometry,Scene,WebGLRenderer} from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {MeshoptDecoder} from 'three/addons/libs/meshopt_decoder.module.js';
import {clone} from 'three/addons/utils/SkeletonUtils.js';
import {bindClip,type Performer} from '../../src/clip-binding';
const scene=new Scene();scene.background=new Color('#e9eef4');
const renderer=new WebGLRenderer({antialias:true,preserveDrawingBuffer:true});renderer.setSize(960,540);renderer.setPixelRatio(1);document.body.append(renderer.domElement);
scene.add(new HemisphereLight(0xffffff,0x71809c,2.5));
for(const [x,y,z] of [[2,4,3],[-3,2,-2]]){const light=new DirectionalLight(0xffffff,2.5);light.position.set(x,y,z);scene.add(light);}
const floor=new Mesh(new PlaneGeometry(12,12),new MeshStandardMaterial({color:0xdce3ec,roughness:1}));floor.rotation.x=-Math.PI/2;floor.position.y=-.003;scene.add(floor);
const camera=new PerspectiveCamera(34,480/540,.01,100);
const loader=new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
const templates=new Map();for(const actor of ['man','woman'])templates.set(actor,(await loader.loadAsync('/models/mpfb-'+actor+'.glb')).scene);
let group:Group,mixer:AnimationMixer,current:string,activeAction:any;
function pose(time:number){activeAction.reset().play();mixer.setTime(time);group.updateMatrixWorld(true);renderer.setScissorTest(true);for(const [index,angle]of [.26,Math.PI/2].entries()){renderer.setViewport(index*480,0,480,540);renderer.setScissor(index*480,0,480,540);camera.position.set(Math.sin(angle)*4.6,1.65,Math.cos(angle)*4.6);camera.lookAt(0,.9,0);renderer.render(scene,camera);}document.getElementById('label')!.textContent=current+' | '+time.toFixed(3)+' s | front / side';}
Object.assign(window,{
 async loadFusion(name:string){if(group){scene.remove(group);mixer.stopAllAction();mixer.uncacheRoot(group);}group=new Group();const models=new Map<Performer,Group>();for(const actor of ['man','woman'] as Performer[]){const model=clone(templates.get(actor));group.add(model);models.set(actor,model as Group);}scene.add(group);const source=await loader.loadAsync('/.cache/motion-recovery/'+name+'/'+name+'.glb');const clip=await bindClip(source,models);mixer=new AnimationMixer(group);activeAction=mixer.clipAction(clip).setLoop(LoopOnce,1);activeAction.clampWhenFinished=true;activeAction.play();current=name;pose(0);return {duration:clip.duration,tracks:clip.tracks.length};},
 poseFusion(time:number){pose(time);return renderer.domElement.toDataURL('image/png').split(',')[1];},
 async captureFusion(){const frames=[];for(let frame=0;frame<=96;frame++){pose(frame/24);frames.push(renderer.domElement.toDataURL('image/jpeg',.9).split(',')[1]);await new Promise(resolve=>setTimeout(resolve,0));}return frames;}
});
