// Sample actual MPFB sole vertices through candidate playback.
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {AnimationMixer,Group,LoopOnce,Vector3} from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {MeshoptDecoder} from 'three/addons/libs/meshopt_decoder.module.js';
import {clone} from 'three/addons/utils/SkeletonUtils.js';
import {bindClip} from '../../src/clip-binding.ts';

globalThis.createImageBitmap=async()=>({width:1,height:1,close(){}});globalThis.self=globalThis;
const loader=new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
async function load(file){const bytes=await readFile(file);return loader.parseAsync(bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength),'');}
const templates=new Map(await Promise.all(['man','woman'].map(async actor=>[actor,(await load(`models/mpfb-${actor}.glb`)).scene])));
const position=new Vector3();
for(const id of process.argv.slice(2)){
 const directory=`.cache/motion-recovery/${id}`;const report=JSON.parse(await readFile(`${directory}/checkpoint.json`,'utf8'));
 const models=new Map(report.performers.map(actor=>[actor,clone(templates.get(actor))]));
 const group=new Group();group.add(...models.values());group.updateMatrixWorld(true);
 const feet=[];
 for(const [actor,model] of models){
  const body=model.getObjectByName(actor==='man'?'Manbody':'Womanbody');
  const indices=body.geometry.getAttribute('skinIndex'),weights=body.geometry.getAttribute('skinWeight');
  for(const side of ['L','R']){
   const vertices=[];for(let index=0;index<indices.count;index++){
    let weight=0;for(let slot=0;slot<4;slot++){const bone=body.skeleton.bones[indices.getComponent(index,slot)];if(bone&&new RegExp(`^DEF-(foot|toe).*${side}$`).test(bone.name))weight+=weights.getComponent(index,slot);}
    if(weight>.8)vertices.push(index);
   }
   const heights=vertices.map(index=>{body.getVertexPosition(index,position);return position.y;});
   const minimum=Math.min(...heights);const sole=vertices.filter((_,index)=>heights[index]<minimum+.018);
   if(sole.length===0)throw new Error(`${actor}/${side}: sole coverage`);
   feet.push({actor,side,body,sole,minimum:Infinity,maximumMinimum:-Infinity,atMinimum:0});
  }
 }
 const clip=await bindClip(await load(report.export),models);const mixer=new AnimationMixer(group);
 const action=mixer.clipAction(clip).setLoop(LoopOnce,1);action.clampWhenFinished=true;action.play();
 for(const frame of report.sampledFrames){
  mixer.setTime(frame/report.rate);group.updateMatrixWorld(true);
  for(const foot of feet){foot.body.skeleton.update();let minimum=Infinity;
   for(const index of foot.sole){foot.body.getVertexPosition(index,position);foot.body.localToWorld(position);minimum=Math.min(minimum,position.y);}
   if(minimum<foot.minimum){foot.minimum=minimum;foot.atMinimum=frame;}foot.maximumMinimum=Math.max(foot.maximumMinimum,minimum);
  }
 }
 const result={exportSha256:createHash('sha256').update(await readFile(report.export)).digest('hex'),sampledFrames:report.sampledFrames.length,units:'meters',soleBand:.018,feet:feet.map(({actor,side,sole,minimum,maximumMinimum,atMinimum})=>({actor,side,vertices:sole.length,minimum,maximumMinimum,atMinimum}))};
 await writeFile(`${directory}/surfaces.json`,JSON.stringify(result,null,2)+'\n');console.log(id,JSON.stringify(result));mixer.stopAllAction();mixer.uncacheRoot(group);
}
