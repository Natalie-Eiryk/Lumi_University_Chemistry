"""Chemistry pilot interaction checks. Storage fixture is TEST ONLY, never shipped in HTML."""
from pathlib import Path
import hashlib,json,shutil,sys,tempfile,threading,http.client
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from serve_lab import make_server, HOST, PORT
H=(ROOT/'web/chemistry.html').read_text('utf8');D=json.loads((ROOT/'30-modules/chem-1117-f2026/source/content.json').read_text('utf8'))
KEY='luminara-chem1117-workbook-pilot-v1';BIO=['luminara-key-terms-ch1-3-v1','luminara-bioethics-cases-1-4-v1','luminara-learning-circuits-v1','luminara-principle-observatory-v1','luminara-bioethics-context-reader-v1','luminara-bioethics-beside-v1']
OUT=ROOT/'evidence/chemistry';OUT.mkdir(exist_ok=True);groups=[];errors=[];requests=[]
def check(name):groups.append(name);print('PASS',name,flush=True)
def load(c,seed=None,mode=''):
 seed=seed or {k:'BIOETHICS_UNCHANGED' for k in BIO}
 p=c.new_page();p.on('pageerror',lambda e:errors.append(str(e)));p.on('request',lambda r:requests.append(r.url))
 fixture="""<script>window._testStore=JSON.parse(%s);window._failWrites=%s;Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem(k){return Object.prototype.hasOwnProperty.call(_testStore,k)?_testStore[k]:null},setItem(k,v){if(_failWrites)throw new Error('TEST_WRITE_REFUSED');_testStore[k]=String(v)},removeItem(k){delete _testStore[k]},clear(){throw new Error('TEST_NO_GLOBAL_CLEAR')}}});</script>"""%(json.dumps(json.dumps(seed)),str(mode=='fail').lower())
 p.set_content(fixture+H);return p
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path=shutil.which('chromium'),args=['--no-sandbox']);c=b.new_context(viewport={'width':1440,'height':1100},accept_downloads=True)
 p=load(c)
 assert p.get_by_role('heading',name='Start where the idea catches.').is_visible()
 assert len(p.locator('[data-open-lesson]').all())==6
 assert p.get_by_role('tab').count()==5
 check('01 five-space chemistry pilot renders with six source-limited routes')
 for l in D['lessons']:
  p.get_by_role('tab',name='Find a way in').click();p.locator('[data-open-lesson="'+l['id']+'"]').click()
  assert l['pre'] in p.locator('.thinkingpane').inner_text()
  assert l['post'] in p.locator('.thinkingpane').inner_text()
  for s in ['notice','change','return']:
   p.locator('[data-stage="'+s+'"]').click();p.locator('#lesson-response').fill('Fixture thought '+l['id']+' '+s)
  p.locator('[data-stage="notice"]').click();assert p.locator('#lesson-response').input_value()=='Fixture thought '+l['id']+' notice'
 check('02 all 18 guided stops preserve their individual writing and pre/post guidance')
 p.locator('#lesson-response').fill('<img src=x onerror="window.bad=true"> my own question')
 handle=p.locator('#lesson-response').element_handle();p.locator('#source-select').select_option('p4')
 assert handle.evaluate('(e)=>e===document.querySelector("#lesson-response")')
 assert '<img src=x' in p.locator('#lesson-response').input_value()
 assert not p.evaluate('window.bad===true')
 check('03 source changes leave the textarea node and typed content intact; markup stays inert')
 before=p.locator('#lesson-response').input_value();p.locator('#quiet').check()
 assert not p.locator('.thinkingpane .guide').first.is_visible();assert p.locator('.sourcepane').is_visible();assert p.locator('#lesson-response').input_value()==before
 p.locator('#quiet').uncheck();p.locator('#large').check();p.locator('#large').uncheck()
 check('04 quiet and larger-type controls preserve context and responses')
 for page in D['pages']:
  p.locator('#source-select').select_option(page['id'])
  assert page['title'] in p.locator('#source-content').inner_text()
  assert 'Learner notes—not an instructor answer key.' in p.locator('#source-content').text_content()
 check('05 seven source transcriptions retain separate handwritten and unresolved layers')
 p.get_by_role('tab',name='Name & meaning').click()
 for typ in ['printed','chart']:
  p.locator('#match-filter').select_option(typ)
  for i in range(6):
   t=[x for x in D['terms'] if (x['tier']=='Printed definition')==(typ=='printed')][i]
   assert p.locator('.prompt').inner_text()==t['text']
   p.locator('[data-term-choice="'+t['id']+'"]').click();p.locator('#term-reason').fill('My terminology reason')
   p.locator('#compare-term').click();assert 'matches the supplied' in p.locator('.feedback').inner_text()
   p.locator('[data-rate="nameRating"]').select_option('with-help');p.locator('[data-rate="meaningRating"]').select_option('explain')
   p.locator('#next-term').click()
 check('06 all twelve matches use recovered definitions/chart associations, with separate self-ratings')
 p.locator('#match-filter').select_option('printed');p.locator('[data-term-choice="unsure"]').click();p.locator('#term-cue').click();p.locator('#compare-term').click()
 assert 'reference to compare' in p.locator('.feedback').last.inner_text()
 assert json.loads(p.evaluate('localStorage.getItem('+json.dumps(KEY)+')'))['terms']['matter']['help'] is True
 check('07 unsure/cue paths track help without claiming correctness or independent recall')
 p.get_by_role('tab',name='Change detective').click()
 for ex in D['examples']:
  p.locator('#example-select').select_option(ex['id']);assert p.get_by_role('heading',name=ex['prompt'],exact=True).is_visible()
  p.locator('[data-example-choice="'+ex['note']+'"]').click();p.locator('#example-reason').fill('My composition reason');p.locator('#compare-example').click()
  assert 'handwritten classification: '+ex['note'] in p.locator('.feedback').inner_text()
  assert 'No independent instructor key' in p.locator('.feedback').inner_text()
  p.locator('#example-revision').fill('My revised question')
 check('08 eleven workbook prompts compare with learner annotations, not an invented answer key')
 seed=p.evaluate('window._testStore');p.close();p=load(c,seed)
 p.get_by_role('tab',name='Source & thinking').click();p.locator('#lesson-select').select_option('matter');assert 'Fixture thought matter notice'==p.locator('#lesson-response').input_value()
 check('09 serialized chemistry notebook restores across fresh test documents')
 p.get_by_role('tab',name='Notebook & sources').click();p.locator('#journal').fill('Private fixture anchor');p.locator('#questions').fill('Private fixture clarification')
 with p.expect_download() as download:p.locator('#export-json').click()
 packet=json.loads(Path(download.value.path()).read_text());assert packet['format']=='luminara-chemistry-private-backup/1';assert packet['state']['journal']=='Private fixture anchor'
 with p.expect_download() as download:p.locator('#export-md').click()
 assert 'Private fixture anchor' in Path(download.value.path()).read_text()
 check('10 real download events deliver chemistry-only JSON and learner-writing Markdown')
 p.locator('#journal').fill('Newer text');p.locator('#import-file').set_input_files({'name':'backup.json','mimeType':'application/json','buffer':json.dumps(packet).encode()});p.locator('#cancel-import').click();assert p.locator('#journal').input_value()=='Newer text'
 p.locator('#import-file').set_input_files({'name':'backup.json','mimeType':'application/json','buffer':json.dumps(packet).encode()});p.locator('#confirm-import').click();assert p.locator('#journal').input_value()=='Private fixture anchor'
 check('11 validated import requires confirmation and cancel leaves existing writing untouched')
 original=p.evaluate('localStorage.getItem('+json.dumps(KEY)+')')
 for bad in [{'format':'bioethics-backup'},dict(packet,state=dict(packet['state'],__proto__={})),dict(packet,state=dict(packet['state'],contentVersion='999'))]:
  p.locator('#import-file').set_input_files({'name':'bad.json','mimeType':'application/json','buffer':json.dumps(bad).encode()});assert 'Import stopped:' in p.locator('#import-message').inner_text();assert p.evaluate('localStorage.getItem('+json.dumps(KEY)+')')==original
 check('12 Bioethics, prototype-shaped, and incompatible chemistry imports reject without mutation')
 for k in BIO:assert p.evaluate('localStorage.getItem('+json.dumps(k)+')')=='BIOETHICS_UNCHANGED'
 check('13 all six existing Bioethics keys remain untouched')
 p.evaluate('window._failWrites=true');p.locator('#journal').fill('Unsaved but retained');assert p.locator('#journal').input_value()=='Unsaved but retained';assert p.evaluate('localStorage.getItem('+json.dumps(KEY)+')')==original;assert 'Not saved:' in p.locator('#save-status').inner_text()
 with p.expect_download() as download:p.locator('#export-json').click()
 assert json.loads(Path(download.value.path()).read_text())['state']['journal']=='Unsaved but retained'
 check('14 failed saves preserve old saved bytes and current exportable session writing')
 p.close();p=load(c,{**{k:'BIOETHICS_UNCHANGED' for k in BIO},KEY:'{corrupt'})
 p.get_by_role('tab',name='Notebook & sources').click();p.locator('#journal').fill('Recovery fragment');assert p.evaluate('localStorage.getItem('+json.dumps(KEY)+')')=='{corrupt';assert 'Session-only' in p.locator('#save-status').inner_text()
 check('15 corrupt prior notebook is not silently replaced')
 p.close();p=load(c);p.get_by_role('tab',name='Notebook & sources').click();p.locator('#journal').fill('Tab A');p.evaluate('window._testStore['+json.dumps(KEY)+']="different-tab"');p.locator('#journal').fill('Tab A later');assert p.locator('#conflict').is_visible();assert p.evaluate('localStorage.getItem('+json.dumps(KEY)+')')=='different-tab'
 check('16 different stored bytes stop further writes instead of overwriting another tab')
 p.close();p=load(c)
 p.get_by_role('tab',name='Find a way in').focus();p.keyboard.press('ArrowRight');assert p.get_by_role('tab',name='Source & thinking').get_attribute('aria-selected')=='true';p.keyboard.press('End');assert p.get_by_role('tab',name='Notebook & sources').get_attribute('aria-selected')=='true'
 check('17 keyboard tab navigation uses arrows, Home, and End')
 for w in [320,390,820,1440]:
  p.set_viewport_size({'width':w,'height':1000})
  for tab in ['Find a way in','Source & thinking','Name & meaning','Change detective','Notebook & sources']:
   p.get_by_role('tab',name=tab).click();assert p.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),(w,tab)
 p.set_viewport_size({'width':1440,'height':1080});p.get_by_role('tab',name='Source & thinking').click();p.locator('#lesson-select').select_option('changes');p.locator('#bring-desk').click();p.screenshot(path=str(OUT/'chemistry-desktop.png'))
 p.set_viewport_size({'width':390,'height':900});p.locator('#bring-desk').click();p.screenshot(path=str(OUT/'chemistry-mobile.png'))
 assert p.locator('.sourcepane').is_visible() and p.locator('.thinkingpane').is_visible()
 check('18 five spaces fit four viewport widths; actual desktop/mobile previews captured')
 assert not requests,requests;assert not errors,errors
 check('19 no automatic network requests or JavaScript errors in exercised states')
 b.close()
 # Try real network navigation without fixture or changed policies; report separately.
 server=make_server(ROOT,0);th=threading.Thread(target=server.serve_forever,daemon=True);th.start()
 native={'status':'not-run'}
 try:
  with tempfile.TemporaryDirectory() as profile:
   cx=pw.chromium.launch_persistent_context(profile,executable_path=shutil.which('chromium'),args=['--no-sandbox'])
   try:
    page=cx.new_page();url=f'http://{HOST}:{server.server_port}/chemistry/';page.goto(url,timeout=10000)
    page.get_by_role('tab',name='Notebook & sources').click();page.locator('#journal').fill('native isolated profile marker');cx.close()
    cx=pw.chromium.launch_persistent_context(profile,executable_path=shutil.which('chromium'),args=['--no-sandbox']);page=cx.new_page();page.goto(url);page.get_by_role('tab',name='Notebook & sources').click();assert page.locator('#journal').input_value()=='native isolated profile marker';native={'status':'passed','scope':'isolated Linux Chromium HTTP profile only; not Windows'}
   except Exception as e:native={'status':'blocked' if 'ERR_BLOCKED_BY_ADMINISTRATOR' in str(e) else 'failed','error':str(e)[:1200]}
   finally:cx.close()
 finally:server.shutdown();server.server_close();th.join()
 (OUT/'native-browser.json').write_text(json.dumps(native,indent=2)+'\n')
(OUT/'ui-results.json').write_text(json.dumps({'passed':True,'groupCount':len(groups),'groups':groups,'htmlSha256':hashlib.sha256(H.encode()).hexdigest(),'storageMethod':'explicit TEST ONLY fixture; native attempt separate','pageErrors':errors,'automaticRequests':requests},indent=2)+'\n')
print(json.dumps({'groupsPassed':len(groups),'native':native},indent=2))
