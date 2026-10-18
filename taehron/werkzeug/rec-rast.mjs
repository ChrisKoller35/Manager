// Aufnahme fuer Regel-Shorts «Kurze/Lange Rast». Aufruf: node rec-rast.mjs <klasse> <stufe> <out-ordner>
import { chromium } from 'playwright';
import fs from 'fs';
const [cls, lvl, out] = process.argv.slice(2);
fs.mkdirSync(out+'/frames',{recursive:true});
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const ctx = await b.newContext({ viewport:{width:390,height:653}, deviceScaleFactor:860/390, isMobile:true, hasTouch:true, locale:'de-CH' });
const p = await ctx.newPage();
await p.goto(`http://localhost:5173/?lang=de#${cls}`); await p.waitForTimeout(2500);
await p.getByText(/Charakter-Werte/).first().click(); await p.waitForTimeout(500);
const lv = p.locator('input').nth(10); await lv.fill(lvl); await lv.press('Tab'); await p.waitForTimeout(500);
await p.getByText(/Charakter-Werte/).first().click(); await p.waitForTimeout(500);
await p.reload(); await p.waitForTimeout(2500); await p.evaluate(()=>window.scrollTo(0,0)); await p.waitForTimeout(600);
const tapCSS = `.__tap{position:fixed;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;background:rgba(255,255,255,.45);border:2px solid rgba(255,255,255,.9);pointer-events:none;z-index:99999;animation:__t .55s ease-out forwards}@keyframes __t{0%{transform:scale(.4);opacity:1}100%{transform:scale(1.5);opacity:0}}`;
await p.addStyleTag({content: tapCSS});
await p.evaluate(()=>{const d=document.createElement('div');d.style.cssText='position:fixed;left:0;top:0;width:1px;height:1px;opacity:.01;z-index:99999;pointer-events:none';document.body.appendChild(d);let i=0;(function f(){d.style.transform='translateX('+(i++%2)+'px)';requestAnimationFrame(f)})();});
const marks={}; const cdp = await ctx.newCDPSession(p); let n=0; const meta=[];
cdp.on('Page.screencastFrame', async f => { const name=`${out}/frames/f${String(n).padStart(5,'0')}.jpg`; n++; fs.writeFileSync(name, Buffer.from(f.data,'base64')); meta.push([name,f.metadata.timestamp]); try{await cdp.send('Page.screencastFrameAck',{sessionId:f.sessionId});}catch{} });
const mark = k => { marks[k]=Date.now()/1000; console.log('mark',k); };
const tapAt = async (x,y) => { await p.evaluate(([x,y])=>{const d=document.createElement('div');d.className='__tap';d.style.left=x+'px';d.style.top=y+'px';document.body.appendChild(d);setTimeout(()=>d.remove(),700);},[x,y]); await p.waitForTimeout(120); await p.mouse.click(x,y); };
const tapEl = async loc => { const bb = await loc.boundingBox(); await tapAt(bb.x+bb.width/2, bb.y+bb.height/2); };
const smooth = async (dy, ms=900) => { const steps=Math.round(ms/16); const s0=await p.evaluate(()=>scrollY); for(let i=1;i<=steps;i++){const k=i/steps; const e=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2; await p.evaluate(y=>window.scrollTo(0,y), s0+dy*e); await p.waitForTimeout(16);} };
// Rauten (Slots) einer Zeile finden: Buttons ohne Text, quadratisch, in der Slot-Karte
const slots = async () => p.evaluate(()=>[...document.querySelectorAll('button')].filter(b=>{const r=b.getBoundingClientRect();return !b.innerText.trim()&&!b.getAttribute('aria-label')?.match(/Feedback|Bild|Schlie/)&&r.width>40&&r.width<70&&Math.abs(r.width-r.height)<3&&r.top>60&&r.top<540}).map(b=>{const r=b.getBoundingClientRect();return [r.x+r.width/2,r.y+r.height/2]}));
await cdp.send('Page.startScreencast',{format:'jpeg',quality:92,maxWidth:860,maxHeight:1440,everyNthFrame:1});
mark('start');
await p.waitForTimeout(2600);
const head = await p.getByText('Fähigkeiten').first().evaluate(e=>e.getBoundingClientRect().top + scrollY - 70);
await smooth(head - await p.evaluate(()=>scrollY), 1300); await p.waitForTimeout(500);
mark('slots');
const s = await slots(); console.log('slots', JSON.stringify(s));
// je Zeile von rechts nach links antippen (Regel aus dem Logbuch)
const rows = {}; for (const [x,y] of s) { const k=Math.round(y/10); (rows[k]=rows[k]||[]).push([x,y]); }
const plan = JSON.parse(process.env.PLAN||'[]'); // Anzahl pro Zeile
let ri=0; for (const k of Object.keys(rows).sort((a,b)=>a-b)) { const r=rows[k].sort((a,b)=>b[0]-a[0]); const m = plan[ri++] ?? r.length; for (const [x,y] of r.slice(0,m)) { await tapAt(x,y); await p.waitForTimeout(380); } }
if (process.env.HPDOWN) { const dn = p.getByRole('button',{name:'▼'}).first(); for (let i=0;i<+process.env.HPDOWN;i++){ await tapEl(dn); await p.waitForTimeout(260);} }
await p.waitForTimeout(900);
mark('rest');
await tapEl(p.getByText(process.env.REST||'Kurze Rast',{exact:true})); await p.waitForTimeout(700);
mark('back');
await p.waitForTimeout(2600);
mark('end');
await cdp.send('Page.stopScreencast'); await p.waitForTimeout(300);
await p.screenshot({path:`${out}/final.png`});
fs.writeFileSync(`${out}/meta.json`, JSON.stringify({meta, marks})); console.log('frames', n);
await b.close();
