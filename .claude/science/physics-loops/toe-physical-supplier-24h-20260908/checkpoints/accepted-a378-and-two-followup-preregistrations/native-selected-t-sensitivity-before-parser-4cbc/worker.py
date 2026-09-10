from pathlib import Path
import json,time,hashlib
from core import census,budgets

def save(p,x):p.write_text(json.dumps(x,default=str,indent=2)+'\n')
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(out,plan):
 out=Path(out);out.mkdir(exist_ok=False);current={};rows=[];start=time.monotonic()
 try:
  for i,item in enumerate(plan['candidates']):
   current={'orbit':i,'stage':'before_parse'};save(out/'PARTIAL.json',{'current':current,'completed':len(rows)})
   data=Path(item['path']).read_bytes()
   if hashlib.sha256(data).hexdigest()!=item['sha256']:raise ValueError('candidate hash')
   ans=census(json.loads(data));save(out/f'NORM_{i}.json',{'orbit':i,**ans})
   current={'orbit':i,'stage':'norm_retained'};save(out/'PARTIAL.json',{'current':current,'completed':len(rows)})
   row={'orbit':i,'candidate_sha256':item['sha256'],**budgets(ans)};save(out/f'BUDGET_{i}.json',row);rows.append(row)
  for item in plan['candidates']:
   if digest(item['path'])!=item['sha256']:raise ValueError('final candidate hash')
  current={'stage':'complete','orbit':4};save(out/'PARTIAL.json',{'current':current,'completed':5})
  save(out/'RESULT.json',{'status':'COMPLETE_NEW_T_SENSITIVITY','rows':rows,'seconds':time.monotonic()-start,'actual_consumer_precision_decided':False,'scope':'exact savedT norm and normalized-consumer sufficient thresholds only'})
 except BaseException as e:
  try:save(out/'FAILURE.json',{'current':current,'completed':len(rows),'error':repr(e)})
  except BaseException as r:e.add_note('retention '+repr(r))
  raise
