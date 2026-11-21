import re,html,json,subprocess,concurrent.futures as cf,collections
B="https://sociana.in"
def get(u):
    r=subprocess.run(["curl","-sS","-L","-m","40","-A","Mozilla/5.0 (compatible; AuditBot)","-o","-","-w","\n__META__%{http_code} %{time_total} %{size_download} %{num_redirects}",u],capture_output=True,text=True,errors="ignore")
    s=r.stdout; m=re.search(r"\n__META__(\d+) ([\d.]+) (\d+) (\d+)$",s)
    return (s[:m.start()] if m else s), (m.groups() if m else ("0","0","0","0"))
idx,_=get(B+"/sitemap.xml")
subs=re.findall(r"<loc>\s*([^<\s]+)\s*</loc>",idx)
urls=[];src={}
for sm in subs:
    x,_=get(sm)
    for u in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>",x):
        if u not in src: src[u]=sm.split('/')[-1]; urls.append(u)
print("sitemaps",len(subs),"urls",len(urls))
def audit(u):
    s,(code,t,size,red)=get(u)
    title=re.findall(r"<title[^>]*>(.*?)</title>",s,re.S); title=html.unescape(re.sub(r"\s+"," ",title[0])).strip() if title else ""
    desc=re.findall(r'<meta\s+name="description"\s+content="([^"]*)"',s,re.S); desc=html.unescape(re.sub(r"\s+"," ",desc[0])).strip() if desc else ""
    canon=re.findall(r'rel="canonical"\s+href="([^"]*)"',s)
    og=re.findall(r'property="og:image"\s+content="([^"]*)"',s)
    robots=re.findall(r'<meta\s+name="robots"\s+content="([^"]*)"',s)
    h1=[re.sub(r"<[^>]+>","",h).strip() for h in re.findall(r"<h1[^>]*>(.*?)</h1>",s,re.S)]
    hs=[html.unescape(re.sub(r"<[^>]+>","",h)).strip() for h in re.findall(r"<h[23][^>]*>(.*?)</h[23]>",s,re.S)]
    main=re.findall(r"<main\b.*?</main>",s,re.S); mainh=main[0] if main else s
    body=re.sub(r"<script.*?</script>|<style.*?</style>|<header.*?</header>|<footer.*?</footer>|<nav.*?</nav>|<form.*?</form>|<svg.*?</svg>","",mainh,flags=re.S)
    words=len(html.unescape(re.sub(r"<[^>]+>"," ",body)).split())
    imgs=re.findall(r"<img\b[^>]*>",s); noalt=[i for i in imgs if not re.search(r'alt="[^"]+"',i) and 'aria-hidden="true"' not in i and 'alt=""' not in i]
    types=sorted(set(re.findall(r'"@type"\s*:\s*"([A-Za-z]+)"',s)))
    return dict(url=u,sm=src[u],code=code,time=float(t),kb=int(size)//1024,red=int(red),title=title,tlen=len(title),desc=desc,dlen=len(desc),canon=canon[0] if canon else "",og=og[0] if og else "",robots=robots[0] if robots else "",h1=len(h1),h1t=h1[0][:90] if h1 else "",words=words,imgs=len(imgs),noalt=len(noalt),schema=s.count("application/ld+json"),types=types,
      qh=sum(1 for h in hs if h.endswith("?")),faq=("FAQPage" in types),faqsec=bool(re.search(r'(?i)>\s*FAQ|frequently asked',s)),tables=len(re.findall(r"<table\b",body)),lists=len(re.findall(r"<[ou]l\b",body)),author=bool(re.search(r'"author"\s*:',s)),dated=bool(re.search(r'"dateModified"|"datePublished"',s)),lang=(re.findall(r'<html[^>]*lang="([^"]+)"',s) or [""])[0],hreflang=len(re.findall(r'hreflang="',s)))
with cf.ThreadPoolExecutor(8) as ex: rows=list(ex.map(audit,urls))
json.dump(rows,open("crawl.json","w"),indent=1)
