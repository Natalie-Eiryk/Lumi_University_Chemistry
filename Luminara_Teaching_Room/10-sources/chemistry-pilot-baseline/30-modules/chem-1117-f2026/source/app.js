'use strict';
(() => {
const DATA=JSON.parse(document.getElementById('chemistry-data').textContent);
const KEY='luminara-chem1117-workbook-pilot-v1', FORMAT='luminara-chemistry-private-backup/1';
const TABS=['route','explore','match','change','notes'], STAGES=['notice','change','return'];
const pageMap=Object.fromEntries(DATA.pages.map(x=>[x.id,x]));
const lessonMap=Object.fromEntries(DATA.lessons.map(x=>[x.id,x]));
const termMap=Object.fromEntries(DATA.terms.map(x=>[x.id,x]));
const exampleMap=Object.fromEntries(DATA.examples.map(x=>[x.id,x]));
const own=(o,k)=>Object.prototype.hasOwnProperty.call(o,k);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const clone=x=>JSON.parse(JSON.stringify(x));
const $=s=>document.querySelector(s);
const fresh=()=>({schema:1,contentVersion:DATA.version,updatedAt:'',ui:{tab:'route',lesson:'matter',stage:'notice',page:'p1',quiet:false,large:false,term:'matter',example:'change-01',matchFilter:'printed'},lessons:{},terms:{},examples:{},journal:'',questions:''});
let state=fresh(), lastStored=null, saveBlocked='', pendingImport=null;
const record=(root,id,base)=>{if(!own(state[root],id))state[root][id]=base;return state[root][id];};
const lessonRecord=id=>record('lessons',id,{notice:'',change:'',return:''});
const termRecord=id=>record('terms',id,{reason:'',choice:'',revealed:false,help:false,nameRating:'',meaningRating:''});
const exampleRecord=id=>record('examples',id,{choice:'',reason:'',compared:false,revision:''});
function obj(x,label){if(!x||typeof x!=='object'||Array.isArray(x))throw Error(label+' must be an object.');}
function keys(x,allowed,label){obj(x,label);for(const k of Object.keys(x))if(!allowed.includes(k))throw Error('Unknown '+label+' field: '+k);}
function text(x,max=12000){if(typeof x!=='string'||x.length>max)throw Error('Text is missing or exceeds the allowed length.');}
function enumVal(x,values){if(!values.includes(x))throw Error('Unknown selection.');}
function bool(x){if(typeof x!=='boolean')throw Error('Invalid flag.');}
function validate(s){
 keys(s,['schema','contentVersion','updatedAt','ui','lessons','terms','examples','journal','questions'],'notebook');
 if(s.schema!==1||s.contentVersion!==DATA.version)throw Error('This notebook needs a different schema/content migration.');
 text(s.updatedAt,80);text(s.journal,20000);text(s.questions,20000);
 const u=s.ui;keys(u,['tab','lesson','stage','page','quiet','large','term','example','matchFilter'],'display');
 enumVal(u.tab,TABS);enumVal(u.lesson,Object.keys(lessonMap));enumVal(u.stage,STAGES);enumVal(u.page,Object.keys(pageMap));bool(u.quiet);bool(u.large);enumVal(u.term,Object.keys(termMap));enumVal(u.example,Object.keys(exampleMap));enumVal(u.matchFilter,['printed','chart','all']);
 for(const [group,ids,fields] of [['lessons',lessonMap,['notice','change','return']],['terms',termMap,['reason','choice','revealed','help','nameRating','meaningRating']],['examples',exampleMap,['choice','reason','compared','revision']]]){
  obj(s[group],group);for(const [id,r] of Object.entries(s[group])){
   if(!own(ids,id))throw Error('Unknown '+group+' ID.');keys(r,fields,group+' record');
   for(const f of fields)if(!own(r,f))throw Error('Incomplete '+group+' record.');
   if(group==='lessons')fields.forEach(f=>text(r[f]));
   if(group==='terms'){text(r.reason);enumVal(r.choice,['','unsure',...Object.keys(termMap)]);bool(r.revealed);bool(r.help);enumVal(r.nameRating,['','not-yet','with-help','independent']);enumVal(r.meaningRating,['','question','partial','explain']);}
   if(group==='examples'){enumVal(r.choice,['','physical','chemical','unsure']);text(r.reason);text(r.revision);bool(r.compared);}
  }
 }
 if(JSON.stringify(s).length>500000)throw Error('Notebook exceeds the pilot size limit.');
 return s;
}
function status(message,failed=false){$('#save-status').textContent=message;$('#save-status').style.fontWeight=failed?'700':'400';}
try{lastStored=localStorage.getItem(KEY);if(lastStored!==null)state=validate(JSON.parse(lastStored));status(lastStored?'Chemistry notebook loaded here · keep a private backup':'New chemistry notebook · notes will save in this browser');}
catch(e){saveBlocked='load';status('Prior storage unavailable or unreadable; it was not replaced. Current work is session-only. Export a backup.',true);}
function save(){
 state.updatedAt=new Date().toISOString();
 if(saveBlocked){status('Session-only changes · saving is paused. Export this chemistry notebook.',true);return false;}
 try{
  const current=localStorage.getItem(KEY);
  if(current!==lastStored){saveBlocked='conflict';$('#conflict').hidden=false;throw Error('Notebook changed in another tab.');}
  const encoded=JSON.stringify(validate(state));localStorage.setItem(KEY,encoded);lastStored=encoded;
  status('Chemistry notes saved in this browser · not a disk backup');return true;
 }catch(e){status('Not saved: '+e.message+' Current writing remains in this tab; export a backup.',true);return false;}
}
window.addEventListener('storage',e=>{if((e.key===KEY||e.key===null)&&e.newValue!==lastStored){saveBlocked='conflict';$('#conflict').hidden=false;status('Another tab changed storage. Saves paused; export current writing.',true);}});
function guide(text){return `<div class="guide"><span class="eyebrow">Ms. Luminara · authored guidance</span><p>${esc(text)}</p></div>`;}
function sourceHTML(id){const p=pageMap[id];return `<span class="tag">Recovered workbook · page ${p.page}</span><h2>${esc(p.title)}</h2><p class="small">Selected printed text transcribed from the inspected page. The original PDF is not bundled; this is not a facsimile.</p><blockquote>${p.printed.map(t=>`<p>${esc(t)}</p>`).join('')}</blockquote><details class="annotation"><summary>Natalie’s handwritten layer</summary><ul>${p.notes.map(t=>`<li>${esc(t)}</li>`).join('')}</ul><p class="small">Learner notes—not an instructor answer key.</p></details><div class="limits"><b>Keep this boundary visible</b><ul>${p.limits.map(t=>`<li>${esc(t)}</li>`).join('')}</ul></div><p class="small">Source: ${esc(DATA.source.title)} · page ${p.page}. Library copy inspected September 21, 2026. Its membership in the requested Windows folder is unverified.</p>`;}
function sourcePane(id){return `<aside class="sourcepane" aria-label="Source beside your work"><label for="source-select" class="small">Keep another page beside me</label><select id="source-select">${DATA.pages.map(p=>`<option value="${p.id}"${p.id===id?' selected':''}>Page ${p.page} · ${esc(p.title)}</option>`).join('')}</select><div id="source-content">${sourceHTML(id)}</div></aside>`;}
function switchTab(tab,focus=false){if(!TABS.includes(tab))return;state.ui.tab=tab;render();save();if(focus)$('#tab-'+tab).focus();}
function render(){
 document.body.classList.toggle('quiet',state.ui.quiet);document.body.classList.toggle('large',state.ui.large);$('#quiet').checked=state.ui.quiet;$('#large').checked=state.ui.large;
 for(const b of document.querySelectorAll('[data-tab]')){const on=b.dataset.tab===state.ui.tab;b.setAttribute('aria-selected',String(on));b.tabIndex=on?0:-1;}
 $('#workspace').setAttribute('aria-labelledby','tab-'+state.ui.tab);
 ({route:renderRoute,explore:renderExplore,match:renderMatch,change:renderChange,notes:renderNotes}[state.ui.tab])();
}
function renderRoute(){
 $('#workspace').innerHTML=`<div class="intro"><span class="tag pending">Source-limited pilot · not a full course map</span><h2>Start where the idea catches.</h2><p>We have one actual workbook to examine. Its printed text, your marginal thinking, and the new learning questions stay separate. The rest of CHEM 1117 is waiting for its sources—not being filled from a generic chemistry syllabus.</p></div><div class="grid">${DATA.lessons.map((l,i)=>`<article class="card"><span class="eyebrow">${String(i+1).padStart(2,'0')} · Pages ${l.pages.map(p=>pageMap[p].page).join(', ')}</span><h3>${esc(l.title)}</h3><p>${esc(l.short)}</p><button data-open-lesson="${l.id}">Walk beside this example →</button></article>`).join('')}</div>${guide('There is no entrance exam at this door. Open the part you can already begin to see. We will use that foothold to find the language, then give you room to return to it without pretending that reading, remembering, and explaining are the same task.')}<div class="two"><article class="box"><h3>Name & meaning</h3><p>Six printed definitions and six associations from your completed chart. The chart descriptors keep their branch context; they do not masquerade as full definitions.</p><button data-goto="match">Find the name</button></article><article class="box"><h3>Change detective</h3><p>The eleven examples printed on page 5, with the page-4 definitions alongside. Compare your answer with your earlier handwritten classification; disagreement becomes a question, not an automatic failure.</p><button data-goto="change">Work an example</button></article></div><div class="source-boundary"><b>Not yet inspected:</b> the named Windows folder, course syllabus, later modules, grading conventions, and remaining worked examples. The original recovered PDF could be read in Files but could not be copied into this build. <button data-goto="notes">Source record & next intake</button></div>`;
}
function renderExplore(){
 const l=lessonMap[state.ui.lesson],r=lessonRecord(l.id),stage=state.ui.stage;
 const q=stage==='notice'?l.question:stage==='change'?l.change:l.return;
 $('#workspace').innerHTML=`<div class="toolbar"><label>Choose a route<select id="lesson-select">${DATA.lessons.map(x=>`<option value="${x.id}"${x.id===l.id?' selected':''}>${esc(x.title)}</option>`).join('')}</select></label><button id="bring-desk">Bring desk into view</button><button id="jump-write">Write beside the source</button></div><div class="desk" id="desk">${sourcePane(state.ui.page)}<article class="thinkingpane"><span class="eyebrow">${esc(l.short)}</span><h2>${esc(l.title)}</h2>${guide(l.pre)}<div class="stepnav" aria-label="Thinking stops">${STAGES.map((s,i)=>`<button data-stage="${s}" aria-pressed="${s===stage}">${i+1}. ${s==='notice'?'Notice & explain':s==='change'?'Compare another':'Bring it back'}</button>`).join('')}</div><p class="prompt">${esc(q)}</p><details class="handrails"><summary>Find a foothold · three small steps</summary><ol>${l.handrails.map(x=>`<li>${esc(x)}</li>`).join('')}</ol></details><label class="field" for="lesson-response">Your thought · fragments welcome</label><textarea id="lesson-response" maxlength="12000" data-write="lessons" data-id="${l.id}" data-field="${stage}">${esc(r[stage])}</textarea>${guide(l.post)}<p class="small">The source stays available. This free-text response is not automatically graded. Switching stops preserves each response.</p></article></div>`;
}
function termPool(){return DATA.terms.filter(t=>state.ui.matchFilter==='all'||(state.ui.matchFilter==='printed')===(t.tier==='Printed definition'));}
function renderMatch(){
 const pool=termPool();if(!pool.some(t=>t.id===state.ui.term))state.ui.term=pool[0].id;
 const t=termMap[state.ui.term],r=termRecord(t.id);
 // Fixed alphabetical choices are accessible and not represented as independent recall.
 const options=pool.slice().sort((a,b)=>a.name.localeCompare(b.name));
 $('#workspace').innerHTML=`<div class="intro"><span class="eyebrow">Recognition first · separate recall later</span><h2>Which name fits this wording?</h2><p>Match the supplied wording to its label. This is supported recognition, not proof of independent recall or mastery.</p></div><div class="toolbar"><label>Source kind<select id="match-filter"><option value="printed"${state.ui.matchFilter==='printed'?' selected':''}>Printed definitions · 6</option><option value="chart"${state.ui.matchFilter==='chart'?' selected':''}>Completed chart associations · 6</option><option value="all"${state.ui.matchFilter==='all'?' selected':''}>Both · 12</option></select></label><button id="next-term">Another wording →</button></div><div class="two"><article class="box"><span class="tag">${esc(t.tier)} · page ${pageMap[t.page].page}</span>${t.tier!=='Printed definition'?'<p class="small">For the completed chart, read the descriptor within its parent branch. This is a chart association, not a complete general definition.</p>':''}<p class="prompt">${esc(t.text)}</p><div class="choicegrid">${options.map(o=>`<button class="choice" data-term-choice="${o.id}" aria-pressed="${r.choice===o.id}">${esc(o.name)}</button>`).join('')}<button class="choice" data-term-choice="unsure" aria-pressed="${r.choice==='unsure'}">Not sure yet</button></div><label class="field" for="term-reason">What wording helped you choose?</label><textarea id="term-reason" maxlength="12000" data-write="terms" data-id="${t.id}" data-field="reason">${esc(r.reason)}</textarea><div class="actions"><button id="term-cue">Give me a handle</button><button class="primary" id="compare-term">Compare with the source</button></div>${r.help?`<p class="feedback">${esc(t.cue)} · Help used</p>`:''}${r.revealed?termFeedback(t,r):''}</article><article class="box"><h3>Understanding and remembering may arrive separately.</h3>${guide('First inspect the relationship inside the sentence. Then choose the name. You can use a familiar example to explain why the wording fits; repeating the wording alone is not the only way to show what you see. If the name slips away, keep the meaning you found and use it as your route back.')}<details id="match-source"><summary>Open the related workbook page · source support</summary>${sourceHTML(t.page)}</details><p class="small">Opening the source or requesting a handle is recorded as assisted practice. No streaks, countdowns, or penalty for uncertainty.</p></article></div>`;
 $('#match-source').addEventListener('toggle',e=>{if(e.currentTarget.open&&!r.help){r.help=true;save();}});
}
function termFeedback(t,r){const lead=r.choice===t.id?'That matches the supplied source association.':r.choice==='unsure'||!r.choice?'Here is a reference to compare with your first impression.':'The source assigns this wording a different label. Keep the feature you noticed, then compare the two labels.';
 return `<div class="feedback"><b>${esc(lead)}</b><p><strong>${esc(t.name)}</strong> · ${esc(t.text)}</p><p>${esc(t.cue)}</p><p class="small">${esc(t.tier)}. This checks the displayed association, not the quality of your explanation.</p></div><div class="two"><label>Name recall<select data-rate="nameRating"><option value="">Not rated</option><option value="not-yet"${r.nameRating==='not-yet'?' selected':''}>Still finding the name</option><option value="with-help"${r.nameRating==='with-help'?' selected':''}>Name with help</option><option value="independent"${r.nameRating==='independent'?' selected':''}>Could recall before choices</option></select></label><label>Meaning<select data-rate="meaningRating"><option value="">Not rated</option><option value="question"${r.meaningRating==='question'?' selected':''}>Still have a question</option><option value="partial"${r.meaningRating==='partial'?' selected':''}>Some pieces connected</option><option value="explain"${r.meaningRating==='explain'?' selected':''}>Can explain in my words</option></select></label></div><p class="small">These ratings are your report, not an automatic assessment.</p>`;
}
function renderChange(){
 const ex=exampleMap[state.ui.example],r=exampleRecord(ex.id);
 $('#workspace').innerHTML=`<div class="toolbar"><label>Workbook example<select id="example-select">${DATA.examples.map(e=>`<option value="${e.id}"${e.id===ex.id?' selected':''}>${esc(e.prompt)}</option>`).join('')}</select></label><button id="next-example">Next example →</button><button id="bring-desk">Bring desk into view</button><button id="jump-write">Write beside the source</button></div><div class="desk" id="desk">${sourcePane(state.ui.page)}<article class="thinkingpane"><span class="eyebrow">Page 5 prompt · page 4 definitions</span><h2>${esc(ex.prompt)}</h2>${guide('The verb gives us a scene; the definition gives us a criterion. Before choosing a label, point to what you would need to know about the substance’s composition. Your earlier handwritten answer is available for comparison, not as an authority you are forbidden to question.')}<div class="choicegrid">${[['physical','Physical change'],['chemical','Chemical change'],['unsure','Not sure / need context']].map(([id,label])=>`<button class="choice" data-example-choice="${id}" aria-pressed="${r.choice===id}">${label}</button>`).join('')}</div><label class="field" for="example-reason">Which part of the definition supports your choice?</label><textarea id="example-reason" maxlength="12000" data-write="examples" data-id="${ex.id}" data-field="reason">${esc(r.reason)}</textarea><details class="handrails"><summary>A smaller step</summary><p>Read the two composition phrases on page 4. What would your chosen example have to establish for one to fit? You may record a missing piece rather than invent it.</p></details><button id="compare-example" class="primary">Compare with my earlier note</button>${r.compared?`<div class="feedback"><b>Your visible handwritten classification: ${esc(ex.note)}.</b><p>${r.choice===ex.note?'Your present choice agrees with that note. What reason connects it to the printed definition?':'Your present response differs or remains open. That is a place to inspect the reasoning—not a reason to count the earlier note as a verified answer key.'}</p><p class="small">No independent instructor key was retrieved. This is comparison with a learner annotation.</p></div><label class="field" for="example-revision">What would you keep, revise, or ask?</label><textarea id="example-revision" maxlength="12000" data-write="examples" data-id="${ex.id}" data-field="revision">${esc(r.revision)}</textarea>`:''}</article></div>`;
}
function renderNotes(){
 const written=[];for(const [id,r] of Object.entries(state.lessons))for(const [field,value] of Object.entries(r))if(value.trim())written.push([lessonMap[id].title+' · '+field,value]);for(const [id,r] of Object.entries(state.terms))if(r.reason.trim())written.push([termMap[id].name+' · why it fits',r.reason]);for(const [id,r] of Object.entries(state.examples)){if(r.reason.trim())written.push([exampleMap[id].prompt+' · my reason',r.reason]);if(r.revision.trim())written.push([exampleMap[id].prompt+' · revision/question',r.revision]);}
 $('#workspace').innerHTML=`<div class="intro"><span class="eyebrow">Keep the thought · keep its source</span><h2>The notebook is yours.</h2><p>Chemistry saves to its own key. These export/import buttons do not read or replace the Bioethics notebooks. Keep a private backup outside the browser.</p></div><div class="actions"><button class="primary" id="export-json">Export chemistry backup (.json)</button><button id="export-md">Export my discussion notes (.md)</button><button id="import-start">Import chemistry backup</button></div><p id="import-message" role="status" aria-live="polite"></p><div class="two"><article class="box"><label class="field" for="journal">My anchor · something that makes the idea stick</label><textarea id="journal" maxlength="20000" data-top="journal">${esc(state.journal)}</textarea></article><article class="box"><label class="field" for="questions">Questions to bring back to the source or instructor</label><textarea id="questions" maxlength="20000" data-top="questions">${esc(state.questions)}</textarea></article></div><details class="box" style="margin-top:20px"><summary>Read my collected fragments (${written.length})</summary>${written.length?written.map(([t,v])=>`<article class="notecard"><b>${esc(t)}</b><p>${esc(v)}</p></article>`).join(''):'<p>Your typed thoughts will appear here. No teaching prose is inserted into your writing.</p>'}</details><article class="box" style="margin-top:20px"><h3>What the source actually supports</h3><p><b>${esc(DATA.source.title)}</b> · Library copy · seven page images inspected. Printed text, selected legible handwriting, and the chart structure were checked visually rather than relying on the noisy extracted text.</p><p>The original PDF could not be materialized through the authorized Files path, so it is <b>not included</b>. The source pane shows labeled transcriptions, not page images. The full Windows folder has not been opened or inventoried.</p><p class="small">${esc(DATA.source.rights)}</p><details><summary>Source record</summary><pre style="white-space:pre-wrap;overflow-wrap:anywhere">${esc(JSON.stringify(DATA.source,null,2))}</pre></details><h3>Bring in the actual course folder next</h3><p>In the full Teaching Room package, Stage-Chemistry.cmd invokes the existing non-destructive source-staging tool for the folder you named. It creates a separate snapshot and inventory, never rewrites the original, and does not upload anything. A ZIP of just <b>Chem_1117_F2026</b> can then be attached for inspection. Do not include the parent School &amp; Legal directory.</p><p>The syllabus, sequence, instructor examples, grading methods, and AI-use instructions remain unverified here. Later modules will be organized from those sources, not guessed from course numbers.</p><h3>Proposed next learning layers—not loaded lessons</h3><ul class="questions"><li>Original course example beside the workspace, including diagrams and your handwriting.</li><li>Required solution layout and unit/rounding conventions copied from the actual instructor model.</li><li>Guided comparison, faded support, and separate name/meaning retrieval.</li><li>Optional first-principles or physics extensions with their own evidence label, never substituted for the assigned method.</li></ul></article>`;
}
function exportFile(name,text,type){const url=URL.createObjectURL(new Blob([text],{type}));const a=document.createElement('a');a.href=url;a.download=name;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),30000);}
function backup(){return {format:FORMAT,createdAt:new Date().toISOString(),containsPrivateLearnerData:true,sourceId:DATA.source.id,state:clone(state)};}
function markdown(){const out=['# My CHEM 1117 pilot notes','','Private learner writing; not an assignment submission.','Source: '+DATA.source.title+' (seven-page Library copy).','Full requested folder has not been reviewed.','','## My anchor',state.journal,'','## Questions',state.questions];for(const [id,r] of Object.entries(state.lessons)){for(const k of STAGES)if(r[k])out.push('','## '+lessonMap[id].title+' — '+k,r[k]);}for(const [id,r] of Object.entries(state.terms))if(r.reason)out.push('','## '+termMap[id].name,'My reason: '+r.reason,'Name self-report: '+r.nameRating,'Meaning self-report: '+r.meaningRating);for(const [id,r] of Object.entries(state.examples))if(r.reason||r.revision)out.push('','## '+exampleMap[id].prompt,'My choice: '+r.choice,'My reason: '+r.reason,'My revision/question: '+r.revision);return out.join('\n\n');}
function openLesson(id){state.ui.lesson=id;state.ui.stage='notice';state.ui.page=lessonMap[id].pages[0];switchTab('explore');}
function nextTerm(){const p=termPool();const i=p.findIndex(t=>t.id===state.ui.term);state.ui.term=p[(i+1)%p.length].id;renderMatch();save();}
function nextExample(){const a=DATA.examples;state.ui.example=a[(a.findIndex(x=>x.id===state.ui.example)+1)%a.length].id;renderChange();save();}
document.addEventListener('click',e=>{
 const b=e.target.closest('button');if(!b)return;
 if(b.dataset.tab)return switchTab(b.dataset.tab);
 if(b.dataset.goto){if(b.dataset.goto==='change')state.ui.page='p4';return switchTab(b.dataset.goto);}
 if(b.dataset.openLesson)return openLesson(b.dataset.openLesson);
 if(b.dataset.stage){state.ui.stage=b.dataset.stage;renderExplore();save();return;}
 if(b.dataset.termChoice){const r=termRecord(state.ui.term);r.choice=b.dataset.termChoice;save();renderMatch();return;}
 if(b.dataset.exampleChoice){const r=exampleRecord(state.ui.example);r.choice=b.dataset.exampleChoice;save();renderChange();return;}
 switch(b.id){
  case 'bring-desk':$('#desk')?.scrollIntoView({block:'start',behavior:'instant'});break;
  case 'jump-write':{const pane=$('.thinkingpane'),field=pane?.querySelector('textarea');if(field){pane.scrollTop+=field.getBoundingClientRect().top-pane.getBoundingClientRect().top-70;field.focus({preventScroll:true});}break;}
  case 'next-term':nextTerm();break;
  case 'term-cue':termRecord(state.ui.term).help=true;save();renderMatch();break;
  case 'compare-term':termRecord(state.ui.term).revealed=true;save();renderMatch();break;
  case 'next-example':nextExample();break;
  case 'compare-example':exampleRecord(state.ui.example).compared=true;save();renderChange();break;
  case 'export-json':exportFile('Luminara_Chem1117_Private_Backup.json',JSON.stringify(backup(),null,2),'application/json');break;
  case 'export-md':exportFile('Luminara_Chem1117_My_Notes.md',markdown(),'text/markdown');break;
  case 'import-start':$('#import-file').value='';$('#import-file').click();break;
 }
});
document.addEventListener('input',e=>{
 const t=e.target;if(t.dataset.write){const group=t.dataset.write,id=t.dataset.id,field=t.dataset.field;if(!['lessons','terms','examples'].includes(group)||!own(state[group],id))return;state[group][id][field]=t.value;save();}
 if(t.dataset.top&&['journal','questions'].includes(t.dataset.top)){state[t.dataset.top]=t.value;save();}
});
document.addEventListener('change',e=>{
 const t=e.target;
 if(t.id==='source-select'){state.ui.page=t.value;$('#source-content').innerHTML=sourceHTML(t.value);save();}
 if(t.id==='lesson-select')openLesson(t.value);
 if(t.id==='match-filter'){state.ui.matchFilter=t.value;state.ui.term=termPool()[0].id;renderMatch();save();}
 if(t.id==='example-select'){state.ui.example=t.value;renderChange();save();}
 if(t.dataset.rate){termRecord(state.ui.term)[t.dataset.rate]=t.value;save();}
 if(t.id==='quiet'||t.id==='large'){state.ui[t.id]=t.checked;document.body.classList.toggle(t.id,t.checked);save();}
});
for(const b of document.querySelectorAll('[data-tab]'))b.addEventListener('keydown',e=>{let i=TABS.indexOf(b.dataset.tab);if(e.key==='ArrowRight')i=(i+1)%TABS.length;else if(e.key==='ArrowLeft')i=(i+TABS.length-1)%TABS.length;else if(e.key==='Home')i=0;else if(e.key==='End')i=TABS.length-1;else return;e.preventDefault();switchTab(TABS[i],true);});
$('#import-file').addEventListener('change',async e=>{
 const f=e.target.files[0];if(!f)return;try{if(f.size>600000)throw Error('Backup exceeds this pilot’s size limit.');const packet=JSON.parse(await f.text());keys(packet,['format','createdAt','containsPrivateLearnerData','sourceId','state'],'backup');if(packet.format!==FORMAT||packet.sourceId!==DATA.source.id||packet.containsPrivateLearnerData!==true)throw Error('Not a chemistry-pilot backup. Bioethics imports belong in the Bioethics lab.');text(packet.createdAt,80);pendingImport=clone(validate(packet.state));$('#import-dialog').showModal();}catch(err){pendingImport=null;$('#import-message').textContent='Import stopped: '+err.message+' Existing work unchanged.';}
});
$('#cancel-import').addEventListener('click',()=>{pendingImport=null;$('#import-dialog').close();});
$('#import-dialog').addEventListener('cancel',()=>{pendingImport=null;});
$('#confirm-import').addEventListener('click',()=>{
 if(!pendingImport)return;try{
  const candidate=clone(validate(pendingImport));candidate.ui.tab='notes';candidate.updatedAt=new Date().toISOString();
  // Persist candidate before mutating the live notebook. A failed write leaves it unchanged.
  const encoded=JSON.stringify(candidate);localStorage.setItem(KEY,encoded);lastStored=encoded;state=candidate;saveBlocked='';$('#conflict').hidden=true;
  pendingImport=null;$('#import-dialog').close();render();status('Chemistry backup imported and saved locally. Bioethics was not changed.');$('#import-message').textContent='Import complete: chemistry pilot only.';
 }catch(err){pendingImport=null;$('#import-dialog').close();$('#import-message').textContent='Import stopped: '+err.message+' Existing session work unchanged.';}
});
if(location.origin!=='http://127.0.0.1:47831')$('#preview-warning').hidden=false;
render();
})();
