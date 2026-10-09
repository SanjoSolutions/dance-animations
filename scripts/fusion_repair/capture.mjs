/** Capture front/side playback on the project's actual MPFB bodies. */
import {copyFile,mkdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {chromium} from '../../.cache/fusion-repair/browser/node_modules/playwright-core/index.mjs';
const rendererRevision=createHash('sha256').update(await readFile('scripts/fusion_repair/review.ts')).digest('hex');
const browser=await chromium.launch({channel:'msedge',headless:true,args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
try{
 const page=await browser.newPage({viewport:{width:960,height:580}});page.on('pageerror',error=>console.error(error));
 await page.goto('http://127.0.0.1:5187/scripts/fusion_repair/review.html');await page.waitForFunction(()=>typeof window.loadFusion==='function');
 for(const name of process.argv.slice(2)){
  const revision=createHash('sha256').update(await readFile(`.cache/motion-recovery/${name}/${name}.glb`)).digest('hex');
  const directory=`.cache/fusion-repair/visual/${name}/${revision.slice(0,12)}-${rendererRevision.slice(0,8)}`;await mkdir(directory,{recursive:true});
  await page.evaluate(name=>window.loadFusion(name),name);
  const frames=await page.evaluate(()=>window.captureFusion());
  for(const[index,encoded]of frames.entries())await writeFile(`${directory}/frame-${String(index).padStart(3,'0')}.jpg`,Buffer.from(encoded,'base64'));
  execFileSync('ffmpeg',['-v','error','-y','-framerate','24','-i',`${directory}/frame-%03d.jpg`,'-c:v','libx264','-pix_fmt','yuv420p','-crf','22','-threads','1',`${directory}/front-side.mp4`]);
  for(const frame of [0,6,18,27,33,42,54,66,75,81,90,96])await copyFile(`${directory}/frame-${String(frame).padStart(3,'0')}.jpg`,`${directory}/review-${frame}.jpg`);
  await writeFile(`${directory}/coverage.json`,JSON.stringify({id:name,exportSha256:createHash('sha256').update(await readFile(`.cache/motion-recovery/${name}/${name}.glb`)).digest('hex'),rendererRevision,frames:97,rate:24,views:['front at 15 degrees','side'],models:['models/mpfb-man.glb','models/mpfb-woman.glb'],renderer:'Edge / Three.js WebGL'},null,2)+'\n');console.log('CAPTURED',name);
 }
}finally{await browser.close();}
