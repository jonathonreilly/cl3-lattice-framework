import json,hashlib,math
from pathlib import Path
def check(out,worker_freeze,elapsed):
 def req(x,m):
  if not x:raise ValueError(m)
 w=json.loads((out/'WORKER_COMPLETE.json').read_text());v=json.loads((out/'RESULT.json').read_text())
 req(w['status']=='COMPLETE_SAVED_ONLY' and w['runtime_sha256']==worker_freeze,'worker binding')
 req(w['result_sha256']==hashlib.sha256((out/'RESULT.json').read_bytes()).hexdigest(),'result hash')
 req(type(w['seconds']) in (int,float) and type(w['rss_bytes']) is int,'resource types')
 req(math.isfinite(w['seconds']) and 0<w['seconds']<=elapsed<30,'timing')
 req(0<w['rss_bytes']<=384*1048576,'RSS')
 req(v['status']=='PASS_ALL_SAVED_APPEND_ENTRIES','saved status')
 req(v['append_calls']==0 and v['oracle_calls']==0,'scope')
 req(type(v['entries']) is int and v['entries']==5970 and type(v['rows']) is int and v['rows']==1995 and type(v['checks']) is int and v['checks']>0,'scientific classification')
 return dict(status='ACCEPTED_SAVED_RECONCILIATION_SCHEMA',result_sha256=w['result_sha256'],external_pending=True)
