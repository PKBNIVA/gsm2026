import re,html,json,subprocess,concurrent.futures as cf,collections
def get(u):
    r=subprocess.run(["curl","-sS","-L","-m","30","-A","Mozilla/5.0 (compatible; AuditBot)","-o","-","-w","\n__META__%{http_code} %{time_total} %{size_download} %{num_redirects}",u],capture_output=True,text=True,errors="ignore")
    s=r.stdout; m=re.search(r"\n__META__(\d+) ([\d.]+) (\d+) (\d+)$",s)
    return (s[:m.start()] if m else s), (m.groups() if m else ("0","0","0","0"))
sm,_=get("https://www.icecubeevents.com/sitemap.xml")
urls=re.findall(r"<loc>\s*([^<\s]+)\s*</loc>",sm)
def audit(u):
    s,(code,t,size,red)=get(u)
    title=re.findall(r"<title[^>]*>(.*?)</title>",s,re.S); title=html.unescape(re.sub(r"\s+"," ",title[0])).strip() if title else ""
    desc=re.findall(r'<meta\s+name="description"\s+content="([^"]*)"',s,re.S); desc=html.unescape(re.sub(r"\s+"," ",desc[0])).strip() if desc else ""
    canon=re.findall(r'rel="canonical"\s+href="([^"]*)"',s)
    h1=[re.sub(r"<[^>]+>","",h).strip() for h in re.findall(r"<h1[^>]*>(.*?)</h1>",s,re.S)]
    body=re.sub(r"<script.*?</script>|<style.*?</style>|<header.*?</header>|<footer.*?</footer>|<nav.*?</nav>|<form.*?</form>","",s,flags=re.S)
    words=len(html.unescape(re.sub(r"<[^>]+>"," ",body)).split())
    imgs=re.findall(r"<img\b[^>]*>",s); noalt=[i for i in imgs if not re.search(r'alt="[^"]+"',i)]
    return dict(url=u,code=code,time=float(t),kb=int(size)//1024,title=title,tlen=len(title),desc=desc,dlen=len(desc),canon=canon[0] if canon else "",h1=len(h1),words=words,imgs=len(imgs),noalt=len(noalt),schema=s.count("application/ld+json"),stray="--&gt;" in s or re.search(r">\s*--&gt;|-->\s*<",s) is not None)
with cf.ThreadPoolExecutor(8) as ex: rows=list(ex.map(audit,urls))
json.dump(rows,open("crawl.json","w"),indent=1)
print("urls",len(rows))
print("status",collections.Counter(r["code"] for r in rows))
tt=collections.Counter(r["title"] for r in rows); dd=collections.Counter(r["desc"] for r in rows)
print("dup titles",sum(v for v in tt.values() if v>1), "dup desc",sum(v for v in dd.values() if v>1))
print("title>60",sum(r["tlen"]>60 for r in rows),"desc>160",sum(r["dlen"]>160 for r in rows),"desc missing",sum(r["dlen"]==0 for r in rows))
print("best in title",sum("best event management" in r["title"].lower() for r in rows))
print("double brand",sum(r["title"].count("Icecube Events")>1 for r in rows))
print("h1!=1",sum(r["h1"]!=1 for r in rows),"h1 0",sum(r["h1"]==0 for r in rows),"h1>1",sum(r["h1"]>1 for r in rows))
print("words<300",sum(r["words"]<300 for r in rows),"median words",sorted(r["words"] for r in rows)[len(rows)//2])
print("schema pages",sum(r["schema"]>0 for r in rows))
print("imgs",sum(r["imgs"] for r in rows),"noalt",sum(r["noalt"] for r in rows))
print("canon mismatch",sum(r["canon"].rstrip('/')!=r["url"].rstrip('/') for r in rows))
print("avg time",round(sum(r["time"] for r in rows)/len(rows),2),"max",max(r["time"] for r in rows))
print("types",collections.Counter(re.sub(r"https://www.icecubeevents.com/([^/]*).*",r"\1",r["url"]) or "home" for r in rows))
for r in rows:
  if r["code"]!="200": print("BAD",r["code"],r["url"])
