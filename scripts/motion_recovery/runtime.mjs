// Compare candidate playback on actual MPFB skeletons with native authored joints.
import {readFile, writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {AnimationMixer, Group, LoopOnce, Vector3, Quaternion, PropertyBinding} from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {MeshoptDecoder} from 'three/addons/libs/meshopt_decoder.module.js';
import {clone} from 'three/addons/utils/SkeletonUtils.js';
import {bindClip} from '../../src/clip-binding.ts';

globalThis.createImageBitmap = async () => ({width:1,height:1,close(){}});
globalThis.self = globalThis;
const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
async function load(file) {
  const bytes = await readFile(file);
  return loader.parseAsync(bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength), '');
}
const catalog = JSON.parse(await readFile('catalog.json', 'utf8'));
const templates = new Map(await Promise.all(['man','woman'].map(async actor => [actor,(await load(catalog.models[actor].file)).scene])));
const position = new Vector3();
const orientation = new Quaternion(), expectedOrientation = new Quaternion();
const installed = process.argv.includes('--installed');
for (const identifier of process.argv.slice(2).filter(argument => argument !== '--installed')) {
  const directory = `.cache/motion-recovery/${identifier}`;
  const report = JSON.parse(await readFile(`${directory}/checkpoint.json`, 'utf8'));
  const entry = catalog.animations.find(entry => entry.id === identifier);
  const file = installed ? entry.file : report.export;
  const sourceHash = installed ? entry.sourceSha256 : report.sourceSha256;
  const reference = JSON.parse(await readFile(`${directory}/runtime-reference.json`, 'utf8'));
  async function retrieveSamples(name) {
    const bytes = await readFile(`${directory}/${name}`);
    return new Float32Array(bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength));
  }
  const flatPositions = reference.positionsFile ? await retrieveSamples(reference.positionsFile) : null;
  const flatRotations = reference.rotationsFile ? await retrieveSamples(reference.rotationsFile) : null;
  const hasRotations = Boolean(flatRotations || reference.rotations);
  const models = new Map(report.performers.map(actor => [actor, clone(templates.get(actor))]));
  const group = new Group(); group.add(...models.values());
  const source = await load(file);
  const clip = await bindClip(source, models);
  const mixer = new AnimationMixer(group);
  const action = mixer.clipAction(clip).setLoop(LoopOnce,1); action.clampWhenFinished = true; action.play();
  const bones = report.performers.map((actor, index) => report.boneNames[index].map(name => {
    const bone = models.get(actor).getObjectByName(PropertyBinding.sanitizeNodeName(name));
    if (!bone) throw new Error(`${identifier}: missing ${actor} ${name}`);
    return bone;
  }));
  let maximum = 0, worst = null, maximumRotation = 0, worstRotation = null;
  for (const [index, frame] of report.sampledFrames.entries()) {
    mixer.setTime(frame / report.rate); group.updateMatrixWorld(true);
    for (const [actor, joints] of bones.entries()) for (const [joint, bone] of joints.entries()) {
      bone.getWorldPosition(position);
      const offset = flatPositions ? (index * reference.shape[1] + actor) * reference.shape[2] + joint : 0;
      const expected = flatPositions ? flatPositions.subarray(offset * 3, offset * 3 + 3) : reference.positions[index][actor][joint];
      const error = Math.hypot(position.x - expected[0], position.y - expected[2], position.z + expected[1]);
      if (!Number.isFinite(error)) throw new Error(`${identifier}: finite transforms at ${frame}`);
      if (error > maximum) { maximum = error; worst = {frame, performer:report.performers[actor], bone:report.boneNames[actor][joint]}; }
      if (hasRotations) {
        bone.getWorldQuaternion(orientation).normalize();
        expectedOrientation.fromArray(flatRotations ? flatRotations.subarray(offset * 4, offset * 4 + 4) : reference.rotations[index][actor][joint]).normalize();
        const rotationError = orientation.angleTo(expectedOrientation);
        if (rotationError > maximumRotation) { maximumRotation = rotationError; worstRotation = {frame, performer:report.performers[actor], bone:report.boneNames[actor][joint]}; }
      }
    }
  }
  const duration = (report.storedRange[1] - report.storedRange[0]) / report.rate;
  const result = {sourceSha256:sourceHash, exportSha256:createHash('sha256').update(await readFile(file)).digest('hex'),
    validatorSha256:createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex'),
    sampledFrames: report.sampledFrames.length, maximumJointPositionError:maximum, worst, duration:clip.duration,
    maximumJointRotationError: hasRotations ? maximumRotation : null, worstRotation,
    durationError:Math.abs(clip.duration-duration), tracks:clip.tracks.length, animation:clip.name,
    passed:maximum < .002 && maximumRotation < .035 && Math.abs(clip.duration-duration)<.00001};
  await writeFile(`${directory}/${installed ? 'runtime-installed' : 'runtime'}.json`, JSON.stringify(result,null,2)+'\n');
  console.log(identifier, JSON.stringify(result));
  if (!result.passed) process.exitCode=1;
  mixer.stopAllAction();mixer.uncacheRoot(group);
}
