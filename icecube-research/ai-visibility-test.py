import json,subprocess,re,concurrent.futures as cf
Q=["Best event management company in Kochi for corporate events?",
"Which company can manage a government event or VIP visit in Kerala?",
"Top corporate conference organisers in Kerala",
"Event management company in Kochi for a product launch",
"Who can organise an international conference in Kerala?",
"Exhibition stall design and fabrication companies in Kochi",
"Inauguration event management company in Kerala",
"Team building event organisers in Kochi",
"Roadshow event management company in Kerala",
"Mall activation agency in Kochi",
"How much does a 300-person corporate event cost in Kochi?",
"I need an event company in Kerala that has handled ministers and protocol. Who should I shortlist?"]
def ask(q,web):
    body={"model":"gpt-4.1","input":q}
    if web: body["tools"]=[{"type":"web_search_preview","user_location":{"type":"approximate","country":"IN","city":"Kochi"}}]
    r=subprocess.run(["curl","-sS","https://api.openai.com/v1/responses","-H","Authorization: Bearer sk-dummy","-H","Content-Type: application/json","-d",json.dumps(body)],capture_output=True,text=True,timeout=180)
    d=json.loads(r.stdout); txt=" ".join(c.get("text","") for o in d.get("output",[]) if o["type"]=="message" for c in o["content"])
    return {"q":q,"web":web,"text":txt}
jobs=[(q,w) for q in Q for w in (True,False)]
with cf.ThreadPoolExecutor(6) as ex: res=list(ex.map(lambda a:ask(*a),jobs))
json.dump(res,open("results.json","w"),indent=1)
for r in res:
    names=re.findall(r"\*\*\[?([^\]\*]{3,60})",r["text"])
    print(("WEB " if r["web"] else "MEM ")+("ICECUBE✓ " if "icecube" in r["text"].lower() else "-------- ")+r["q"][:60]+" | "+"; ".join(dict.fromkeys(n.strip() for n in names))[:260])
