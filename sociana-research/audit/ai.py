import json,subprocess,concurrent.futures as cf
Q=["Which is the best event app for a corporate conference in India?",
"Which companies build branded, white-label event apps for iOS and Android in India?",
"What is the best app for running a dealer meet or channel partner meet in India?",
"Which event app manages each guest's flights, hotel room and airport pickup for a corporate offsite or incentive trip in India?",
"What is the best wedding guest app in India for RSVPs, room allocation and itineraries?",
"Which event registration and ticketing platform in India supports UPI payments and GST invoices?",
"Which event platforms in India offer QR code and face recognition check-in?",
"Which event app has live polls, leaderboards and games for employee engagement events in India?",
"Which white-label event app suits an event management agency in India running events for many clients?",
"How much does a custom event app cost in India?",
"Which event platform in India sends tickets, passes and reminders on WhatsApp?",
"I am planning a 500-person annual sales conference in India and want a branded event app that the vendor's team sets up and supports on the event day. Who should I shortlist?"]
CITIES=["Mumbai","Delhi","Bengaluru","Kolkata"]
def ask(q,web,run):
    body={"model":"gpt-4.1","input":q}
    if web: body["tools"]=[{"type":"web_search_preview","user_location":{"type":"approximate","country":"IN","city":web}}]
    for a in range(3):
        r=subprocess.run(["curl","-sS","-m","240","https://api.openai.com/v1/responses","-H","Authorization: Bearer sk-dummy","-H","Content-Type: application/json","-d",json.dumps(body)],capture_output=True,text=True)
        try:
            d=json.loads(r.stdout); txt="";cites=[]
            for o in d.get("output",[]):
                if o["type"]=="message":
                    for c in o["content"]:
                        txt+=c.get("text","")
                        cites+=[an.get("url") for an in c.get("annotations",[]) if an.get("url")]
            if txt: return {"q":q,"web":web or "","run":run,"text":txt,"cites":cites,"usage":d.get("usage")}
        except Exception: pass
    return {"q":q,"web":web or "","run":run,"text":"","error":r.stdout[:300]}
jobs=[(q,c,0) for q in Q for c in CITIES]+[(q,None,k) for q in Q for k in range(3)]
with cf.ThreadPoolExecutor(6) as ex: res=list(ex.map(lambda a:ask(*a),jobs))
json.dump(res,open("chatgpt-runs-2026-11-21.json","w"),indent=1)
print("done",len(res),"empty",sum(1 for r in res if not r['text']))
