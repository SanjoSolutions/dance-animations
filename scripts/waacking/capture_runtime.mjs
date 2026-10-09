// Capture exported MPFB playback through the review viewer's public controls.
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {chromium} from '../../.cache/waacking-browser/node_modules/playwright/index.mjs';

const root=fileURLToPath(new URL('../../',import.meta.url));
const directory=path.join(root,'.cache/waacking-runtime-frames');
await mkdir(directory,{recursive:true});
process.env.TEMP=path.join(root,'.cache/waacking-temp');
process.env.TMP=process.env.TEMP;
const catalog=JSON.parse(await readFile(path.join(root,'catalog.json'),'utf8'));
const entries=catalog.animations.filter(entry=>entry.style==='waacking');
const inputs=await Promise.all(entries.map(async entry=>{
  const report=JSON.parse(await readFile(path.join(root,'.cache/motion-recovery',entry.id,'checkpoint.json'),'utf8'));
  return {id:entry.id,sourceSha256:report.sourceSha256,exportSha256:report.exportSha256};
}));
const browser=await chromium.launch({channel:'msedge',headless:true,args:['--use-angle=swiftshader','--renderer-process-limit=1']});
const frames=[];
try {
  const page=await browser.newPage({viewport:{width:1440,height:1450}});
  const errors=[];page.on('pageerror',error=>errors.push(error.message));
  await page.goto('http://127.0.0.1:5193/scripts/waacking/preview.html');
  await page.locator('#status').filter({hasText:'16 MPFB clips'}).waitFor({timeout:120000});
  const loaded=await page.locator('.clip-label').evaluateAll(labels=>labels.map(label=>({id:label.dataset.id,sourceSha256:label.dataset.source,exportSha256:label.dataset.export})));
  if(JSON.stringify(loaded)!==JSON.stringify(inputs))throw new Error('Capture source/export revisions require matching candidates');
  await page.getByRole('button',{name:'Pause',exact:true}).click();
  for(const view of ['front','side','back']){
    await page.locator('#view').selectOption(view);
    for(let index=0;index<32;index++){
      const time=index/8;
      await page.locator('#time').evaluate((input,value)=>{input.value=String(value);input.dispatchEvent(new Event('input',{bubbles:true}));},time);
      await page.waitForFunction(value=>document.querySelector('#seconds').textContent===value.toFixed(2)+' s',time);
      const file=path.join(directory,`${view}-${String(index).padStart(3,'0')}.png`);
      await page.screenshot({path:file});
      frames.push({view,time,file:path.relative(root,file).replaceAll('\\','/'),sha256:createHash('sha256').update(await readFile(file)).digest('hex')});
    }
    console.log('RUNTIME CAPTURE',view,32);
  }
  if(errors.length)throw new Error(errors.join('\n'));
  await writeFile(path.join(directory,'capture.json'),JSON.stringify({inputs,frames,models:catalog.models,browser:await browser.version(),sampleRate:8,duration:4,coverage:'Actual exported GLBs on the project MPFB base models; front, side and back'},null,2)+'\n');
}finally{await browser.close();}
