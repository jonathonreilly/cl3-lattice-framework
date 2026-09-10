import json,hashlib,math
from pathlib import Path
def check(out,rf,elapsed):
 def req(x,m):
  if not x:raise ValueError(m)
 sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
 w=json.loads((out/'WORKER_COMPLETE.json').read_text());v=json.loads((out/'RESULT.json').read_text());part=json.loads((out/'PARTIAL.json').read_text())
 req(not any((out/n).exists() for n in ('FAILURE.json','DISPATCH_FAILURE.json')),'no failures')
 req(w['status']=='COMPLETE_SAVED_ONLY' and w['runtime_sha256']==rf['worker_freeze'] and w['binding_sha256']==rf['authorization']['binding_sha256'],'worker binding')
 req(w['result_sha256']==sha(out/'RESULT.json'),'result hash')
 req(all(type(t)in(int,float) and math.isfinite(t) and t>0 for t in (w['seconds'],v['seconds'],elapsed)) and v['seconds']<=w['seconds']<29 and w['seconds']<=elapsed<30,'times')
 req(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'RSS')
 req(v['status']=='PASS_ALL_SAVED_APPEND_ENTRIES' and type(v['checks'])is int and v['checks']>0,'saved status')
 req(all(type(v[k])is int for k in ('entries','rows','oracle_calls','append_calls')) and v['entries']==6015 and v['rows']==2010 and v['oracle_calls']==v['append_calls']==0,'scope census')
 req(v['scope']=='exact midpoint arithmetic; physical scalar error ledger separate','scope text')
 req(part['error'] is None and part['stage']=='row_arithmetic' and type(part['row'])is int and part['row']==2009 and type(part['entries'])is int and part['entries']==6014,'last pre-entry partial')
 return dict(status='ACCEPTED_ALL_FIRST_ACTION_SAVED_ENTRIES_SCHEMA',result_sha256=w['result_sha256'],entries=6015,rows=2010,external_pending=True)
