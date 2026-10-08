/** Verify the public viewer controls and the local House review gallery. */
import assert from 'node:assert/strict';
import {writeFile} from 'node:fs/promises';
import {chromium} from '../../.cache/house/browser/node_modules/playwright-core/index.mjs';
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
try {
 const page=await browser.newPage({viewport:{width:1200,height:850}});const errors=[];page.on('pageerror',e=>errors.push(String(e)));
 await page.addInitScript(()=>localStorage.setItem('dance-animation-playback',JSON.stringify({music:false,mode:'single'})));
 await page.goto('http://127.0.0.1:5173/?style=house_dance&animation=house_woman_ready_to_low&character=woman&mode=single');
 await page.waitForFunction(()=>!document.querySelector('#play').disabled,{timeout:60000});
 assert.equal(await page.locator('#animation option').count(),45);
 assert.equal(await page.locator('#style').inputValue(),'house_dance');
 await page.locator('#loop').check();
 await page.locator('#timeline').evaluate(e=>{e.value=e.max;e.dispatchEvent(new Event('input',{bubbles:true}));});
 await page.waitForFunction(()=>document.querySelector('#play').textContent==='Play');
 const held=await page.locator('#timeline').inputValue();assert.equal(held,await page.locator('#timeline').getAttribute('max'));
 await page.locator('#play').click();await page.waitForFunction(()=>Number(document.querySelector('#timeline').value)<1);
 await page.screenshot({path:'.cache/house/viewer-browser.png'});
 await page.goto('http://127.0.0.1:5173/docs/house_dance_review/index.html');
 await page.waitForFunction(()=>document.querySelectorAll('article').length===90);
 await page.locator('#actor').selectOption('woman');assert.equal(await page.locator('article').count(),45);
 await page.locator('video').first().evaluate(e=>e.load());await page.waitForFunction(()=>Number.isFinite(document.querySelector('video').duration));
 const duration=await page.locator('video').first().evaluate(e=>e.duration);assert.ok(Math.abs(duration-4.125)<.05);
 await page.screenshot({path:'.cache/house/gallery-browser.png'});assert.deepEqual(errors,[]);
 const report={passed:true,viewerMoves:45,performers:['man','woman'],directedTransition:'holds endpoint with Loop checked; Play restarts at entry',galleryClips:90,filteredClips:45,reviewVideoDuration:duration,browser:'Chromium WebGL',consoleErrors:errors};
 await writeFile('.cache/house/browser-review.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
} finally {await browser.close();}
