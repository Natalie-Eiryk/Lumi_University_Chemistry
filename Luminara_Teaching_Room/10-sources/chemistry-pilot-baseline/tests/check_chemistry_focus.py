from pathlib import Path
import json,shutil,hashlib
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1];H=(R/'web/chemistry.html').read_text()
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path=shutil.which('chromium'),args=['--no-sandbox']);p=b.new_page(viewport={'width':390,'height':900})
 fixture="<script>window._test={};Object.defineProperty(window,'localStorage',{value:{getItem:k=>_test[k]??null,setItem:(k,v)=>_test[k]=v}});</script>"
 p.set_content(fixture+H);p.locator('[data-open-lesson="changes"]').click();p.locator('#bring-desk').click();p.locator('#jump-write').click();p.locator('#lesson-response').fill('My example and the composition criterion belong beside each other.')
 assert p.locator('#lesson-response').evaluate('(e)=>document.activeElement===e')
 a=p.locator('.sourcepane').bounding_box();t=p.locator('#lesson-response').bounding_box()
 assert 0<=a['y']<900 and 0<=t['y']<900,(a,t)
 p.screenshot(path=str(R/'evidence/chemistry/chemistry-mobile-writing.png'))
 b.close()
(R/'evidence/chemistry/focus-results.json').write_text(json.dumps({'passed':True,'groupCount':1,'description':'Mobile jump-to-writing preserves simultaneous source access and focus','htmlSha256':hashlib.sha256(H.encode()).hexdigest()},indent=2)+'\n')
print('PASS mobile writing focus with source pane still present')
