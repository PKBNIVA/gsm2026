const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.cwd()+'/report.html',{waitUntil:'networkidle'});await p.waitForTimeout(1500);
await p.pdf({path:'raw.pdf',format:'A4',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:true,headerTemplate:'<span></span>',footerTemplate:'<div style="font-size:7pt;color:#8a94a3;width:100%;padding:0 15mm;display:flex;justify-content:space-between"><span>Sociana · Website audit and plan</span><span class="pageNumber"></span></div>',margin:{top:'16mm',bottom:'17mm',left:'15mm',right:'15mm'}});
await b.close();})();
