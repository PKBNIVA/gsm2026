import json,subprocess,urllib.parse,concurrent.futures as cf,collections,re,time
seeds=["event app","event app india","event management app","event management software india","event management platform","white label event app","branded event app","custom event app","conference app","conference app india","event registration software","event registration platform india","event ticketing platform india","online ticketing platform","event check in app","qr code check in event","face recognition event check in","dealer meet app","dealer meet","channel partner meet","wedding app","wedding guest management app","wedding rsvp app","wedding website india","employee engagement app","employee engagement activities","corporate offsite","event gamification","live polling app","event networking app","exhibition lead capture app","whatsapp event invitation","event app cost","event app pricing","event app development","hybrid event platform","event guest management","hospitality management app events","step challenge app","corporate event games","team building games","wedding games","sangeet games","event management software for agencies","cvent alternative","whova alternative"]
qs=[]
for s in seeds:
    qs.append(s)
    for ch in "abcdefghijklmnoprstw": qs.append(s+" "+ch)
def sug(q):
    for a in range(3):
        try:
            r=subprocess.run(["curl","-sS","-m","12","https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=in&q="+urllib.parse.quote(q)],capture_output=True,text=True,errors="ignore")
            return json.loads(r.stdout)[1]
        except Exception: time.sleep(1)
    return None
with cf.ThreadPoolExecutor(8) as ex: res=list(ex.map(sug,qs))
json.dump(dict(zip(qs,res)),open('autocomplete-raw.json','w'),indent=0)
allp=collections.Counter(p.lower().strip() for r in res if r for p in r)
json.dump(allp,open('phrases.json','w'),indent=0)
print('seeds',len(seeds),'queries',len(qs),'failed',sum(r is None for r in res),'unique phrases',len(allp))
