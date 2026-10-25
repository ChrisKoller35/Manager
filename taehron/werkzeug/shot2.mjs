// Screenshot der Ansicht «Zauberplätze & Fähigkeiten» je Klasse, 860x1440 (fuer das Reel «3 Klassen, 3 Looks»)
import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
const [cls,lvl,out]=process.argv.slice(2);
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const ctx=await b.newContext({viewport:{width:390,height:653},deviceScaleFactor:860/390,isMobile:true,hasTouch:true,locale:'de-CH'});
const p=await ctx.newPage();
await p.goto(`http://localhost:5173/?lang=de#${cls}`); await p.waitForTimeout(2500);
await p.getByText(/Charakter-Werte/).first().click(); await p.waitForTimeout(500);
const lv=p.locator('input').nth(10); await lv.fill(lvl); await lv.press('Tab'); await p.waitForTimeout(500);
await p.getByText(/Charakter-Werte/).first().click(); await p.waitForTimeout(500);
await p.reload(); await p.waitForTimeout(2500);
const y=await p.getByText('Fähigkeiten').first().evaluate(e=>e.getBoundingClientRect().top+scrollY-70);
await p.evaluate(y=>window.scrollTo(0,y),y); await p.waitForTimeout(600);
await p.screenshot({path:out}); console.log('ok',out);
await b.close();
