/** Render candidate clips with Chromium's WebGL renderer and the actual MPFB wardrobe. */
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { chromium } from '../../.cache/house/browser/node_modules/playwright-core/index.mjs';
const motion=process.argv.includes('--motion');
const names=process.argv.slice(2).filter(argument=>argument!=='--motion');
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
try {
  const page=await browser.newPage({viewport:{width:400,height:440}});
  page.on('pageerror',error=>console.error(error));
  await page.goto('http://127.0.0.1:5173/scripts/house_dance/review.html');
  await page.waitForFunction(()=>typeof window.loadHouse==='function');
  for (const name of names) {
    const exportSha256=createHash('sha256').update(await readFile(`.cache/house/candidates/${name}.glb`)).digest('hex');
    await page.evaluate(name=>window.loadHouse(name),name);
    const destination=`.cache/house/visual/${name}`;
    await mkdir(destination,{recursive:true});
    if (motion) {
      const frames=await page.evaluate(()=>window.captureHouse());
      for (const [index,encoded] of frames.entries()) await writeFile(`${destination}/frame-${String(index).padStart(3,'0')}.jpg`,Buffer.from(encoded,'base64'));
      execFileSync('ffmpeg',['-v','error','-y','-framerate','8','-i',`${destination}/frame-%03d.jpg`,'-c:v','libvpx-vp9','-crf','32','-b:v','0','-deadline','realtime','-cpu-used','6','-threads','1',`${destination}/motion.webm`]);
    } else for (const frame of [0,6,18,30,42,54,66,78,90,96]) {
      for (const [view,angle] of [['front',.25],['side',1.4]]) {
        await page.evaluate(([frame,angle])=>window.poseHouse(frame,angle),[frame,angle]);
        await page.screenshot({path:`${destination}/${view}-${frame}.png`});
      }
    }
    await writeFile(`${destination}/coverage.json`,JSON.stringify({id:name,exportSha256,frames:motion?Array.from({length:33},(_,index)=>index*3):[0,6,18,30,42,54,66,78,90,96],views:['front','side'],renderer:'Chromium WebGL / Three.js / project MPFB street wardrobe',motion},null,2)+'\n');
    console.log('CAPTURED',name);
  }
} finally {await browser.close();}
