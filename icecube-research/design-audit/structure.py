import json,re,subprocess,html,collections,concurrent.futures as cf
from urllib.parse import urljoin,urlparse
B="https://www.icecubeevents.com"
urls=[r['url'] for r in json.load(open('../audit/crawl.json'))]
def get(u): return subprocess.run(["curl","-sL","-m","30","-A","Mozilla/5.0",u],capture_output=True,text=True,errors="ignore").stdout
def norm(u):
    p=urlparse(u); 
    if p.netloc.replace('www.','')!='icecubeevents.com': return None
    path=p.path.rstrip('/') or '/'
    if re.search(r'\.(css|js|png|jpg|jpeg|webp|svg|pdf|mp4|ico)$',path,re.I): return None
    return B+(path if path!='/' else '')+( '?'+p.query if p.query else '')
def page(u):
    s=get(u)
    def links(seg): return [n for n in (norm(urljoin(u,h)) for h in re.findall(r'<a\b[^>]*href="([^"#]+)"',seg)) if n]
    head=''.join(re.findall(r'<header.*?</header>',s,re.S)); foot=''.join(re.findall(r'<footer.*?</footer>',s,re.S))
    body=re.sub(r'<header.*?</header>|<footer.*?</footer>','',s,flags=re.S)
    return u,dict(nav=links(head),foot=links(foot),body=links(body),crumb=bool(re.search(r'(?i)breadcrumb',s)),forms=len(re.findall(r'<form\b',s)),
      inputs=len(re.findall(r'<(input|select|textarea)\b(?![^>]*type="hidden")',body+foot)),h=[(int(a),html.unescape(re.sub(r'<[^>]+>','',b)).strip()[:60]) for a,b in re.findall(r'<h([1-4])[^>]*>(.*?)</h\1>',s,re.S)],
      cta=len(re.findall(r'(?i)get in touch|let.s talk|send inquiry|contact us|enquire|plan (an|your) event|whatsapp|wa\.me',body)),tel=len(re.findall(r'href="tel:',s)),wa=len(re.findall(r'wa\.me|api\.whatsapp',s)),search=bool(re.search(r'type="search"|name="(q|s|search)"',s)))
P=json.load(open('structure.json'))
P={(norm(u) or u):d for u,d in P.items()}
home=B
# click depth BFS over all links
adj={u:set(d['nav']+d['foot']+d['body']) for u,d in P.items()}
depth={home:0}; q=[home]
while q:
    u=q.pop(0)
    for v in adj.get(u,()):
        v2=v.split('?')[0]
        if v2 in P and v2 not in depth: depth[v2]=depth[u]+1; q.append(v2)
typ=lambda u: re.sub(B+r"/?([^/]*).*",r"\1",u) or "home"
print('depth distribution',collections.Counter(depth.get(u,'unreachable') for u in P))
byt=collections.defaultdict(list)
for u in P: byt[typ(u)].append(depth.get(u,'unreachable'))
for k,v in byt.items(): print(k,collections.Counter(v))
inl=collections.Counter()
for u,d in P.items():
    for v in set(d['body']): 
        v=v.split('?')[0]
        if v in P and v!=u: inl[v]+=1
print('body inlinks: pages with 0 contextual inlinks',sum(1 for u in P if inl[u]==0),'of',len(P))
for k in ['service','works','blog']:
    us=[u for u in P if typ(u)==k]; print(k,'median contextual inlinks',sorted(inl[u] for u in us)[len(us)//2],'min',min(inl[u] for u in us),'max',max(inl[u] for u in us))
# cross-links
sv=[u for u in P if typ(u)=='service']; wk=[u for u in P if typ(u)=='works']; bl=[u for u in P if typ(u)=='blog']
print('service pages linking to any event page (body):',sum(any(typ(v.split("?")[0])=='works' for v in P[u]['body']) for u in sv),'of',len(sv))
print('event pages linking to a service page (body):',sum(any(typ(v)=='service' for v in P[u]['body']) for u in wk),'of',len(wk))
print('event pages linking to other events:',sum(any(typ(v)=='works' and v!=u for v in P[u]['body']) for u in wk))
print('blog posts linking to service (body):',sum(any(typ(v)=='service' for v in P[u]['body']) for u in bl),'of',len(bl))
print('homepage body links to: services',len({v for v in P[home]['body'] if typ(v)=='service'}),'events',len({v for v in P[home]['body'] if typ(v)=='works'}),'blog',len({v for v in P[home]['body'] if typ(v)=='blog'}))
print('NAV',[v.replace(B,'') or '/' for v in dict.fromkeys(P[home]['nav'])])
print('FOOT',[v.replace(B,'') or '/' for v in dict.fromkeys(P[home]['foot'])])
print('breadcrumbs on',sum(d['crumb'] for d in P.values()),'search on',sum(d['search'] for d in P.values()))
print('forms per page',collections.Counter(d['forms'] for d in P.values()),'tel links pages',sum(d['tel']>0 for d in P.values()),'whatsapp pages',sum(d['wa']>0 for d in P.values()))
# our-works pagination & filters
ow=get(B+'/our-works'); print('our-works: event links on page 1',len(set(re.findall(r'/works/[a-z0-9-]+',ow))),'pages',sorted(set(re.findall(r'our-works\?page=(\d+)',ow))),'categories',len(set(re.findall(r'our-works\?category=(\d+)',ow))))
linked=set()
for pg in ['','?page=2','?page=3','?page=4','?page=5']: linked|=set(re.findall(r'/works/[a-z0-9-]+',get(B+'/our-works'+pg)))
print('events reachable via portfolio pagination',len(linked),'of',len(wk))
# url patterns
print('service slugs ending -icecube-events',sum(u.endswith('-icecube-events') for u in sv),'blog',sum('icecube' in u.split('/')[-1] for u in bl),'longest url',max(len(u) for u in P))
# heading outline samples
for u in [home,sv[0],wk[0]]: print(u.replace(B,'') or '/',P[u]['h'][:14])
