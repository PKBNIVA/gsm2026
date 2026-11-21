const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const n of ['1-record','2-ceremony','3-control','4-editorial','5-concierge','6-bold']){
 const p=await b.newPage({viewport:{width:1440,height:900},deviceScaleFactor:1.25});
 await p.goto('file://'+process.cwd()+'/concepts/'+n+'.html');await p.waitForTimeout(2500);
 await p.screenshot({path:'shots/'+n+'.jpg',type:'jpeg',quality:84,fullPage:true});
 const m=await b.newPage({viewport:{width:390,height:780},deviceScaleFactor:2});
 await m.goto('file://'+process.cwd()+'/concepts/'+n+'.html');await m.waitForTimeout(2000);await m.screenshot({path:'shots/'+n+'-m.jpg',type:'jpeg',quality:82});
 console.log(n, await p.evaluate(()=>document.documentElement.scrollHeight), await m.evaluate(()=>document.documentElement.scrollWidth));}
await b.close();})();
