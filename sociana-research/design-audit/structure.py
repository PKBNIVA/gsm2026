import json,re,subprocess,html,collections,concurrent.futures as cf
from urllib.parse import urljoin,urlparse
B="https://sociana.in"
urls=[r['url'] for r in json.load(open('../audit/crawl.json'))]
def get(u): return subprocess.run(["curl","-sL","-m","40","-A","Mozilla/5.0",u],capture_output=True,text=True,errors="ignore").stdout
def norm(u):
    p=urlparse(u)
    if p.netloc.replace('www.','')!='sociana.in': return None
    path=p.path
    if re.search(r'\.(css|js|png|jpg|jpeg|webp|avif|svg|pdf|mp4|ico|txt|xml|json|webmanifest)$',path,re.I): return None
    if not path.endswith('/'): path+='/'
    return B+path
def page(u):
    s=get(u)
    def links(seg): return [n for n in (norm(urljoin(u,html.unescape(h))) for h in re.findall(r'<a\b[^>]*href="([^"#]+)"',seg)) if n]
    head=''.join(re.findall(r'<header\b.*?</header>',s,re.S)); foot=''.join(re.findall(r'<footer\b.*?</footer>',s,re.S))
    main=''.join(re.findall(r'<main\b.*?</main>',s,re.S)) or re.sub(r'<header\b.*?</header>|<footer\b.*?</footer>','',s,flags=re.S)
    return u,dict(nav=links(head),foot=links(foot),body=links(main),crumb=bool(re.search(r'BreadcrumbList',s)) and bool(re.search(r'(?i)aria-label="breadcrumb',s)),forms=len(re.findall(r'<form\b',main)),
      inputs=len(re.findall(r'<(input|select|textarea)\b(?![^>]*type="hidden")',main)),h=[(int(a),html.unescape(re.sub(r'<[^>]+>','',b)).strip()[:70]) for a,b in re.findall(r'<h([1-4])[^>]*>(.*?)</h\1>',main,re.S)],
      wa=len(re.findall(r'wa\.me|api\.whatsapp',s)),tel=len(re.findall(r'href="tel:',s)),search=bool(re.search(r'type="search"|role="search"|pagefind',s)),demo=len(re.findall(r'(?i)book a demo',main)),extlinks=len(set(re.findall(r'href="(https?://(?!sociana\.in)[^"]+)"',main))))
with cf.ThreadPoolExecutor(8) as ex: P=dict(ex.map(page,urls))
json.dump(P,open('structure.json','w'))
print(len(P))
