import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const ctx = await b.newContext({ viewport:{width:390,height:653}, deviceScaleFactor:860/390, isMobile:true, hasTouch:true });
const p = await ctx.newPage();
p.on('dialog', d => { console.log('dialog', d.message()); d.accept(); });
// warm cache: load druide, scroll through so lazy images load
await p.goto('http://localhost:5173/#druide'); await p.waitForTimeout(1500);
for (let y=0;y<9000;y+=400){ await p.evaluate(y=>window.scrollTo(0,y),y); await p.waitForTimeout(150);} 
await p.evaluate(()=>{localStorage.clear();});
await p.goto('http://localhost:5173/'); await p.waitForTimeout(1500);
const tapCSS = `.__tap{position:fixed;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;background:rgba(255,255,255,.45);border:2px solid rgba(255,255,255,.9);pointer-events:none;z-index:99999;animation:__t .55s ease-out forwards}@keyframes __t{0%{transform:scale(.4);opacity:1}100%{transform:scale(1.5);opacity:0}}`;
const inject = async () => { await p.addStyleTag({content: tapCSS + 'html,body{margin:0;background:#0a0a12}'}); };
await inject();
const marks = {}; let t0 = null;
const cdp = await ctx.newCDPSession(p);
let n = 0; const meta = [];
cdp.on('Page.screencastFrame', async f => {
  const name = `frames/f${String(n).padStart(5,'0')}.jpg`; n++;
  fs.writeFileSync(name, Buffer.from(f.data,'base64'));
  meta.push([name, f.metadata.timestamp]);
  if (t0===null) t0 = f.metadata.timestamp;
  try { await cdp.send('Page.screencastFrameAck',{sessionId:f.sessionId}); } catch{}
});
const mark = k => { marks[k] = Date.now()/1000; console.log('mark',k); };
const tapAt = async (x,y) => {
  await p.evaluate(([x,y])=>{const d=document.createElement('div');d.className='__tap';d.style.left=x+'px';d.style.top=y+'px';document.body.appendChild(d);setTimeout(()=>d.remove(),700);},[x,y]);
  await p.waitForTimeout(120);
  await p.mouse.click(x,y);
};
const tapEl = async loc => { const bb = await loc.boundingBox(); await tapAt(bb.x+bb.width/2, bb.y+bb.height/2); };
const smooth = async (dy, ms=900) => { const steps=Math.round(ms/16); const s0=await p.evaluate(()=>scrollY);
  for(let i=1;i<=steps;i++){const k=i/steps; const e=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2; await p.evaluate(y=>window.scrollTo(0,y), s0+dy*e); await p.waitForTimeout(16);} };
// keep repainting so screencast emits frames steadily
await p.evaluate(()=>{const d=document.createElement('div');d.style.cssText='position:fixed;left:0;top:0;width:1px;height:1px;opacity:.01;z-index:99999;pointer-events:none';document.body.appendChild(d);let i=0;(function f(){d.style.transform='translateX('+(i++%2)+'px)';requestAnimationFrame(f)})();window.__keep=d;});
await cdp.send('Page.startScreencast',{format:'jpeg',quality:92,maxWidth:860,maxHeight:1440,everyNthFrame:1});
mark('start');
await p.waitForTimeout(1600);
await smooth(160, 700); await p.waitForTimeout(300); await smooth(-160,600); await p.waitForTimeout(300);
mark('tapDruide');
await tapEl(p.locator('a[href="#druide"]'));
await p.waitForTimeout(400);
await p.evaluate(()=>{const d=document.createElement('div');d.style.cssText='position:fixed;left:0;top:0;width:1px;height:1px;opacity:.01;z-index:99999;pointer-events:none';document.body.appendChild(d);let i=0;(function f(){d.style.transform='translateX('+(i++%2)+'px)';requestAnimationFrame(f)})();});
await inject();
mark('druide');
await p.waitForTimeout(1800);
await smooth(330, 900); await p.waitForTimeout(400);
mark('slots');
const btns = p.locator('button');
const all = await btns.all();
// slots are the 6 empty buttons after "Kreiszauber"
let idx=[]; for (let i=0;i<all.length;i++){ const t=(await all[i].innerText()).trim(); if(!t) idx.push(i);} console.log('empty idx', idx);
const slotIdx = idx.filter(i=>i>4).slice(0,6);
for (const i of [slotIdx[0], slotIdx[1], slotIdx[2], slotIdx[4]]) { await tapEl(all[i]); await p.waitForTimeout(550); }
mark('hp');
const down = p.getByText('▼',{exact:true});
for (let i=0;i<3;i++){ await tapEl(down); await p.waitForTimeout(350);} 
await p.waitForTimeout(700);
mark('rast');
await tapEl(p.getByText('Lange Rast').last());
await p.waitForTimeout(1800);
mark('scrollSpells');
const target = await p.getByText('Meine Zauber').first().evaluate(e=>e.getBoundingClientRect().top + scrollY - 20);
const cur = await p.evaluate(()=>scrollY);
await smooth(target-cur, 1600); await p.waitForTimeout(900);
mark('filter');
await tapEl(p.getByText('Lvl 1',{exact:true}).first()); await p.waitForTimeout(1300);
await smooth(240, 700); await p.waitForTimeout(500);
mark('card');
await tapEl(p.getByText('Heilendes Wort').first()); await p.waitForTimeout(2600);
mark('end');
await cdp.send('Page.stopScreencast');
await p.screenshot({path:'final.png',type:'png'});
await p.waitForTimeout(300);
fs.writeFileSync('meta.json', JSON.stringify({meta, marks}));
console.log('frames', n);
await b.close();
