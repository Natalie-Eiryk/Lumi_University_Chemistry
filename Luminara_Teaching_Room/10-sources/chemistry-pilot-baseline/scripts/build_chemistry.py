#!/usr/bin/env python3
"""Rebuild the source-limited chemistry pilot. No network or original-file edits."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'30-modules/chem-1117-f2026/source'
def build():
 d=json.loads((SRC/'content.json').read_text('utf8'))
 assert d['schema']=='luminara-chemistry-content/1'
 assert len(d['pages'])==7 and len(d['lessons'])==6 and len(d['terms'])==12 and len(d['examples'])==11
 for kind in ['pages','lessons','terms','examples']:
  ids=[i['id'] for i in d[kind]]
  assert len(ids)==len(set(ids))
 assert d['source']['folderInspected'] is False and d['source']['rawFileIncluded'] is False
 pages={p['id'] for p in d['pages']};terms={t['id'] for t in d['terms']}
 for l in d['lessons']:
  assert set(l['pages'])<=pages and set(l['terms'])<=terms and len(l['handrails'])==3
 for t in d['terms']:assert t['page'] in pages
 for e in d['examples']:assert e['note'] in ['physical','chemical']
 data=json.dumps(d,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
 html=(SRC/'template.html').read_text('utf8').replace('__STYLE__',(SRC/'style.css').read_text('utf8')).replace('__DATA__',data).replace('__SCRIPT__',(SRC/'app.js').read_text('utf8'))
 (ROOT/'web/chemistry.html').write_text(html,'utf8')
 receipt={'version':d['version'],'htmlSha256':hashlib.sha256(html.encode()).hexdigest(),'lessonCount':len(d['lessons']),'termCount':len(d['terms']),'workbookExampleCount':len(d['examples']),'sourceFolderInspected':False,'originalPDFIncluded':False}
 (SRC/'build-info.json').write_text(json.dumps(receipt,indent=2)+'\n')
 return receipt
if __name__=='__main__':print(json.dumps(build(),indent=2))
