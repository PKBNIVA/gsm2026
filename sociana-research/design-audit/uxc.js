const {chromium,devices}=require('playwright');const fs=require('fs');
const axe=fs.readFileSync('ax/node_modules/axe-core/axe.min.js','utf8');
const B='https://sociana.in';
const pages=[['home','/']];
const comps=JSON.parse(process.env.COMPS||'[]');
const measure=()=>{const vh=innerHeight,vw=innerWidth;const vis=e=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e);return r.width>0&&r.height>0&&s.visibility!=='hidden'&&s.display!=='none'&&+s.opacity>0.05};
 const inFold=e=>{const r=e.getBoundingClientRect();return vis(e)&&r.top<vh&&r.bottom>0&&r.left<vw&&r.right>0};
 const h1=document.querySelector('h1');const ctaRx=/book a demo|demo|get in touch|contact|quote|pricing|try|start|whatsapp|talk to|sign up|get started|request/i;
 const act=[...document.querySelectorAll('a,button')].filter(vis);
 const foldCta=act.filter(e=>inFold(e)&&(ctaRx.test(e.innerText||e.getAttribute('aria-label')||'')||/wa\.me|whatsapp|tel:/.test(e.href||'')));
 const small=act.filter(e=>{const r=e.getBoundingClientRect();return (r.width<44||r.height<44)});
 const texts=[];const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){const t=n.textContent.trim();if(t.length>1&&n.parentElement&&vis(n.parentElement)){const s=getComputedStyle(n.parentElement);texts.push([t.length,parseFloat(s.fontSize),s.fontFamily.split(',')[0].replace(/["']/g,'').trim(),s.textTransform])}}
 const tot=texts.reduce((a,t)=>a+t[0],0);const fam={};texts.forEach(t=>fam[t[2]]=(fam[t[2]]||0)+t[0]);
 const sizes=new Set(texts.map(t=>Math.round(t[1])));
 const foldWords=[...document.querySelectorAll('h1,h2,h3,p,li,a,button,span')].filter(e=>inFold(e)&&e.children.length===0).map(e=>e.innerText||'').join(' ').split(/\s+/).filter(Boolean).length;
 const body=[...document.querySelectorAll('p')].filter(vis).map(p=>parseFloat(getComputedStyle(p).fontSize));
 const pw=[...document.querySelectorAll('p')].filter(p=>vis(p)&&p.innerText.length>200).map(p=>Math.round(p.innerText.length/Math.max(1,(p.getBoundingClientRect().height/parseFloat(getComputedStyle(p).lineHeight||24)))));
 return {h1Text:h1?h1.innerText.slice(0,70):null,h1InFold:h1?inFold(h1):false,h1Top:h1?Math.round(h1.getBoundingClientRect().top):null,foldCta:foldCta.length,foldCtaLabels:[...new Set(foldCta.map(e=>(e.innerText||e.getAttribute('aria-label')||e.href||'').trim().slice(0,24)))].slice(0,5),foldWords,
  screens:+(document.documentElement.scrollHeight/vh).toFixed(1),overflow:document.documentElement.scrollWidth>vw+1,actions:act.length,smallTargets:small.length,
  under14:Math.round(100*texts.filter(t=>t[1]<14).reduce((a,t)=>a+t[0],0)/tot),upper:Math.round(100*texts.filter(t=>t[3]==='uppercase').reduce((a,t)=>a+t[0],0)/tot),families:Object.entries(fam).sort((a,b)=>b[1]-a[1]).map(([k,v])=>k+' '+Math.round(100*v/tot)+'%'),sizeCount:sizes.size,
  pMedian:body.sort((a,b)=>a-b)[Math.floor(body.length/2)]||null,charsPerLine:pw.sort((a,b)=>a-b)[Math.floor(pw.length/2)]||null,imgs:document.images.length,videos:document.querySelectorAll('video').length}};
(async()=>{const b=await chromium.launch();const out={};
for(const [vp,ctxo] of [['mobile',{...devices['iPhone 13']}],['desktop',{viewport:{width:1440,height:900}}]]){const ctx=await b.newContext(ctxo);
 for(const [n,u] of [...pages.map(([n,p])=>[n,B+p]),...(vp==='mobile'?comps:[])]){const p=await ctx.newPage();try{await p.goto(u,{waitUntil:'domcontentloaded',timeout:60000});await p.waitForTimeout(4500);
  const m=await p.evaluate(measure);
  if(!n.startsWith('c-')){await p.addScriptTag({content:axe});const r=await p.evaluate(async()=>{const r=await axe.run(document,{runOnly:['wcag2a','wcag2aa']});return r.violations.map(v=>[v.id,v.impact,v.nodes.length])});m.axe=r;}
  if(['home','pricing','occasion-dealer','case-hccb','contact'].includes(n)||n.startsWith('c-'))await p.screenshot({path:`shots/${vp}-${n}.jpg`,type:'jpeg',quality:70});
  out[vp+':'+n]=m;console.log(vp,n,'h1fold',m.h1InFold,'cta',m.foldCta,'screens',m.screens,'small',m.smallTargets+'/'+m.actions,'u14',m.under14,'upper',m.upper,'axe',(m.axe||[]).map(a=>a[0]+':'+a[2]).join(','));}catch(e){console.log(vp,n,'ERR',e.message.slice(0,80))}await p.close();}
 await ctx.close();}
fs.writeFileSync('ux-comp.json',JSON.stringify(out,null,1));await b.close();})();
