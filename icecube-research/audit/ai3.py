import json,subprocess,concurrent.futures as cf
Q=json.load(open('../chatgpt-answers-2026-11-19.json'))
qs=list(dict.fromkeys(r['q'] for r in Q))
def ask(q,web,run):
    body={"model":"gpt-4.1","input":q}
    if web: body["tools"]=[{"type":"web_search_preview","user_location":{"type":"approximate","country":"IN","city":"Kochi"}}]
    for a in range(3):
        r=subprocess.run(["curl","-sS","https://api.openai.com/v1/responses","-H","Authorization: Bearer sk-dummy","-H","Content-Type: application/json","-d",json.dumps(body)],capture_output=True,text=True,timeout=240)
        try:
            d=json.loads(r.stdout); txt=" ".join(c.get("text","") for o in d.get("output",[]) if o["type"]=="message" for c in o["content"])
            if txt: return {"q":q,"web":web,"run":run,"text":txt}
        except Exception: pass
    return {"q":q,"web":web,"run":run,"text":"","error":r.stdout[:300]}
jobs=[(q,True,k) for q in qs for k in range(3)]+[(q,False,k) for q in qs for k in range(2)]
with cf.ThreadPoolExecutor(6) as ex: res=list(ex.map(lambda a:ask(*a),jobs))
json.dump(res,open("chatgpt-runs-2026-11-20.json","w"),indent=1)
print("done",len(res),sum(1 for r in res if not r['text']))
