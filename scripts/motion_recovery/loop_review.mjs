// Measure complete-loop pose and velocity continuity on the actual MPFB skeletons.
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {AnimationMixer,Group,LoopOnce,Vector3,Quaternion} from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {MeshoptDecoder} from 'three/addons/libs/meshopt_decoder.module.js';
import {clone} from 'three/addons/utils/SkeletonUtils.js';
import {bindClip} from '../../src/clip-binding.ts';

globalThis.createImageBitmap=async()=>({width:1,height:1,close(){}});globalThis.self=globalThis;
const loader=new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
async function load(file){const bytes=await readFile(file);return loader.parseAsync(bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength),'');}
const templates=new Map(await Promise.all(['man','woman'].map(async actor=>[actor,(await load(`models/mpfb-${actor}.glb`)).scene])));
for(const id of process.argv.slice(2)){
 const directory=`.cache/motion-recovery/${id}`;const report=JSON.parse(await readFile(`${directory}/checkpoint.json`,'utf8'));
 if(report.loop){
  const models=new Map(report.performers.map(actor=>[actor,clone(templates.get(actor))]));const group=new Group();group.add(...models.values());
  const clip=await bindClip(await load(report.export),models);const mixer=new AnimationMixer(group);const action=mixer.clipAction(clip).setLoop(LoopOnce,1);action.clampWhenFinished=true;action.play();
  const bones=[];group.traverse(object=>{if(object.isBone)bones.push(object);});
  const step=.001;
  const samples=[0,step,clip.duration-step,clip.duration].map(time=>{mixer.setTime(time);group.updateMatrixWorld(true);return bones.map(bone=>({position:bone.getWorldPosition(new Vector3()),rotation:bone.getWorldQuaternion(new Quaternion()).normalize()}));});
  let position=0,rotation=0,velocity=0,worstVelocity;
  for(let index=0;index<bones.length;index++){
   position=Math.max(position,samples[0][index].position.distanceTo(samples[3][index].position));rotation=Math.max(rotation,samples[0][index].rotation.angleTo(samples[3][index].rotation));
   const outgoing=samples[1][index].position.clone().sub(samples[0][index].position).divideScalar(step);const incoming=samples[3][index].position.clone().sub(samples[2][index].position).divideScalar(step);
   const error=incoming.distanceTo(outgoing);if(error>velocity){velocity=error;worstVelocity=bones[index].name;}
  }
  const result={exportSha256:createHash('sha256').update(await readFile(report.export)).digest('hex'),position,rotation,velocity,worstVelocity,step,units:'meters, radians, meters/second',limits:{position:.001,rotation:.035,velocity:.12},passed:position<.001&&rotation<.035&&velocity<.12};
  await writeFile(`${directory}/loop.json`,JSON.stringify(result,null,2)+'\n');console.log(id,JSON.stringify(result));if(!result.passed)process.exitCode=1;mixer.stopAllAction();mixer.uncacheRoot(group);
 }
}
