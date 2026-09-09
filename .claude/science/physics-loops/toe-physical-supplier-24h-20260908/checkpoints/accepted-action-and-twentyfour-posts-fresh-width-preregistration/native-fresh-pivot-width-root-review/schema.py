import json,math,hashlib
from pathlib import Path
def check(out,rf,elapsed):
 def req(x,m):
  if not x:raise ValueError(m)
 req(set(p.name for p in out.iterdir())=={'RESULT.json','WORKER_COMPLETE.json','ROWS.json','PARTIAL.json'},'exact output membership and failure absence')
 req(json.loads((out/'PARTIAL.json').read_text())=={'stage':'scalar','orbit':4,'row':23},'final completed scalar position')
 req(type(elapsed) in (int,float) and math.isfinite(elapsed) and 0<elapsed<30,'external root time')
 r=json.loads((out/'RESULT.json').read_text());w=json.loads((out/'WORKER_COMPLETE.json').read_text());rows=json.loads((out/'ROWS.json').read_text())
 req(r['status']=='COMPLETE_SAVED_SCALAR_DIAGNOSTIC' and r['rows']==rows,'result rows')
 req(0<len(rows)<=120 and all(type(x['orbit']) is int and 0<=x['orbit']<5 and type(x['row']) is int and 0<=x['row']<24 for x in rows),'row census')
 req(len({(x['orbit'],x['row']) for x in rows})==len(rows),'unique rows')
 req(r['forced_blockers']==[x for x in rows if x.get('must_fail_width') or x['divisor_failure']],'blocker partition')
 req(w['runtime_sha256']==rf['worker_freeze'] and w['binding_sha256']==rf['authorization']['binding_sha256'],'worker bindings')
 req(w['result_sha256']==hashlib.sha256((out/'RESULT.json').read_bytes()).hexdigest(),'result hash')
 req(w['status']=='COMPLETE_SAVED_ONLY' and type(w['rss_bytes']) is int and 0<w['rss_bytes']<=384*1048576,'worker receipt')
 req(type(w['seconds']) in (int,float) and math.isfinite(w['seconds']) and 0<w['seconds']<29 and w['seconds']<=elapsed,'time')
 return {'status':'ACCEPTED_SAVED_SCALAR_DIAGNOSTIC','rows':len(rows),'blockers':len(r['forced_blockers']),'no_native_replay':True}
