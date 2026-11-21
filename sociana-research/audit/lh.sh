#!/bin/bash
# usage: lh.sh name url
export CHROME_PATH=$(ls -d /opt/pw-browsers/chromium-*/chrome-linux*/chrome | head -1)
lh/node_modules/.bin/lighthouse "$2" --quiet --chrome-flags="--headless=new --no-sandbox" --form-factor=mobile --output=json --output-path=lhr/$1.json >/dev/null 2>&1
python3 - "$1" <<'PY'
import json,sys
d=json.load(open(f"lhr/{sys.argv[1]}.json"));c=d["categories"];a=d["audits"]
print(sys.argv[1],{k:round((v["score"] or 0)*100) for k,v in c.items()},"LCP",a["largest-contentful-paint"]["displayValue"],"TBT",a["total-blocking-time"]["displayValue"],"CLS",a["cumulative-layout-shift"]["displayValue"],"FCP",a["first-contentful-paint"]["displayValue"],"MB",round(a["total-byte-weight"]["numericValue"]/1e6,2))
PY
