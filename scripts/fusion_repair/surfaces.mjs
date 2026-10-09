// Measure MPFB sole geometry through complete Fusion support intervals.
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
const baseline=process.argv.includes('--baseline');
for(const id of process.argv.slice(2).filter(value=>value!=='--baseline')){
 const directory=`.cache/motion-recovery/${id}`;
 const report=JSON.parse(await readFile(`${directory}/checkpoint.json`,'utf8'));
 if(baseline)report.export=`animations/fusion/${id}.glb`;
 const contacts=JSON.parse(await readFile(`${directory}/contacts.json`,'utf8'));
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
   feet.push({actor,side,body,sole,minimum:Infinity,maximumMinimum:-Infinity,intervals:contacts.feet.find(foot=>foot.actor===actor&&foot.side===side).intervals.map(({start,end})=>({start,end,drift:0,samples:0}))});
  }
 }
 const clip=await bindClip(await load(report.export),models);const mixer=new AnimationMixer(group);
 const action=mixer.clipAction(clip).setLoop(LoopOnce,1);action.clampWhenFinished=true;action.play();
 for(const frame of report.sampledFrames){
  mixer.setTime(frame/report.rate);group.updateMatrixWorld(true);
  for(const foot of feet){
   foot.body.skeleton.update();const positions=foot.sole.map(index=>{foot.body.getVertexPosition(index,position);foot.body.localToWorld(position);return position.clone();});
   const minimum=Math.min(...positions.map(point=>point.y));foot.minimum=Math.min(foot.minimum,minimum);foot.maximumMinimum=Math.max(foot.maximumMinimum,minimum);
   for(const interval of foot.intervals)if(frame*24/report.rate>=interval.start&&frame*24/report.rate<=interval.end){
    interval.reference??=positions;interval.samples++;
    interval.drift=Math.max(interval.drift,...positions.map((point,index)=>point.distanceTo(interval.reference[index])));
   }
  }
 }
 const maximumPlantDrift=Math.max(...feet.flatMap(foot=>foot.intervals.map(interval=>interval.drift)));
 const result={id,exportSha256:createHash('sha256').update(await readFile(report.export)).digest('hex'),sampledFrames:report.sampledFrames.length,units:'meters',soleBand:.018,maximumPlantDrift,limits:{plantDrift:.003,minimum:-.002},feet:feet.map(({actor,side,sole,minimum,maximumMinimum,intervals})=>({actor,side,vertices:sole.length,minimum,maximumMinimum,intervals:intervals.map(({reference,...interval})=>interval)})),passed:maximumPlantDrift<=.003&&feet.every(foot=>foot.minimum>=-.002)};
 await writeFile(`${directory}/surfaces${baseline?'-baseline':''}.json`,JSON.stringify(result,null,2)+'\n');console.log(id,'sole drift',maximumPlantDrift,'minimum',Math.min(...feet.map(foot=>foot.minimum)),'passed',result.passed);if(!result.passed)process.exitCode=1;
 mixer.stopAllAction();mixer.uncacheRoot(group);
}
