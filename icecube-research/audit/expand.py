import json,subprocess,urllib.parse,concurrent.futures as cf,collections,re,string
seeds=["event management kochi","event management company kochi","event management kerala","event management company kerala","corporate event kochi","corporate event kerala","event organisers kochi","event planners kochi","conference organisers kochi","conference kerala","government event management","inauguration event","product launch event kochi","exhibition stall kochi","stall fabrication kerala","roadshow kerala","mall activation kochi","brand activation kerala","team building kochi","corporate team outing kerala","mice kerala","dealer meet kerala","annual day event kochi","award night event kochi","event management cost","event company near me","stage decoration kochi","led wall rental kochi","sound and light kochi","anchor for event kochi","event venue kochi","convention centre kochi","event management trivandrum","event management calicut","event management thrissur"]
qs=[]
for s in seeds:
    qs.append(s)
    for ch in "abcdefghijklmnoprstw": qs.append(s+" "+ch)
def sug(q):
    try:
        r=subprocess.run(["curl","-sS","-m","12","https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=in&q="+urllib.parse.quote(q)],capture_output=True,text=True)
        return json.loads(r.stdout)[1]
    except Exception: return []
with cf.ThreadPoolExecutor(10) as ex: res=list(ex.map(sug,qs))
allp=collections.Counter(p.lower().strip() for r in res for p in r)
json.dump(allp,open('phrases-2026-11-21.json','w'),indent=0)
print('queries',len(qs),'unique phrases',len(allp))
groups=[('Wedding',r'wedding|marriage|bridal|engagement|haldi|mehndi|reception'),('Jobs, courses, salary',r'job|vacanc|salary|course|college|degree|intern|career|hiring|fresher|institute|diploma|syllabus|mba|bba|fees'),('Birthday and private parties',r'birthday|baby|party|anniversary|house ?warming|naming'),('Cost and price',r'cost|price|rate|charge|budget|package|cheap|quotation'),('Venues',r'venue|hall|convention|auditorium|resort|hotel'),('Corporate and conference',r'corporate|conference|seminar|dealer|annual|award|mice|offsite|business'),('Government and inauguration',r'government|govt|inaugurat|tender|protocol'),('Launch, activation, roadshow',r'launch|activation|roadshow|road show|promotion|btl'),('Exhibition and stalls',r'exhibition|stall|expo|booth'),('Team building',r'team'),('Equipment and staff (stage, LED, sound, anchor)',r'stage|led|sound|light|anchor|emcee|dj|decor'),('Other Kerala cities',r'trivandrum|thiruvananthapuram|calicut|kozhikode|thrissur|kottayam|kannur|kollam|palakkad|alappuzha|malappuram'),('Best / top / list / near me',r'best|top|list|near|biggest|famous|leading|contact|number|review')]
left=dict(allp); out=[]
for name,rx in groups:
    m=[p for p in left if re.search(rx,p)]
    for p in m: left.pop(p)
    out.append((name,len(m),sorted(m,key=lambda x:-allp[x])[:6]))
out.append(('Other',len(left),sorted(left,key=lambda x:-allp[x])[:8]))
for n,c,ex in out: print(f"{c:4} {n}: {ex}")
