from pathlib import Path
import json,hashlib,time,os
from core import ledger

def save(p,x):
 tmp=p.with_name(p.name+'.tmp')
 with tmp.open('w') as f:f.write(json.dumps(x,indent=2)+'\n');f.flush();os.fsync(f.fileno())
 os.replace(tmp,p)
def run(out,plan):
 out=Path(out);out.mkdir(exist_ok=False);current={};completed=0;start=time.monotonic()
 def emit(x):
  nonlocal current,completed
  current=x
  with (out/'EVENTS.jsonl').open('a') as f:f.write(json.dumps(x)+'\n');f.flush();os.fsync(f.fileno())
  if x['stage']=='node_complete':completed+=1
  save(out/'PARTIAL.json',{'current':current,'completed':completed})
 try:
  data={}
  for key,item in plan['geometry'].items():
   emit({'stage':'before_parse','role':key});raw=Path(item['path']).read_bytes()
   if hashlib.sha256(raw).hexdigest()!=item['sha256']:raise ValueError('geometry pin')
   data[key]=json.loads(raw)
  ans=ledger(data['new']['rows'],data['old']['rows'],data['outer']['nodes'],emit);ans['seconds']=time.monotonic()-start
  for item in plan['geometry'].values():
   if hashlib.sha256(Path(item['path']).read_bytes()).hexdigest()!=item['sha256']:raise ValueError('final geometry pin')
  save(out/'RESULT.json',ans)
 except BaseException as e:
  try:save(out/'FAILURE.json',{'current':current,'completed':completed,'error':repr(e)})
  except BaseException as x:e.add_note('retention '+repr(x))
  raise
