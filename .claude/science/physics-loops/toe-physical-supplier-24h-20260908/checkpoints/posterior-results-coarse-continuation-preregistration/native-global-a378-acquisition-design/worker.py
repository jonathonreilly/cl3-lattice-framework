from pathlib import Path
from fractions import Fraction as F
import json,time

def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def run(out,oracle,generate):
 out=Path(out);out.mkdir(exist_ok=False);start=time.monotonic();rows=[];current={'stage':'geometry'}
 def progress(x):
  nonlocal current
  current=x
  with (out/'ROOT_PROGRESS.jsonl').open('a') as f:f.write(json.dumps(x)+'\n')
  save(out/'PARTIAL.json',{'current':current,'completed':len(rows)})
 try:
  nodes=generate(progress)
  if len(nodes)!=378:raise ValueError('fixed node census')
  save(out/'NODES.json',{'rows':nodes,'count':len(nodes),'scope':'new Gauss21 ratio4 family'})
  for n in nodes:
   current={'stage':'before_oracle','id':n['id'],'s':n['s']};save(out/'PARTIAL.json',{'current':current,'completed':len(rows)})
   t=time.monotonic();raw=oracle(F(n['s']));row={'id':n['id'],'seconds':time.monotonic()-t,'raw':raw};save(out/('RAW_%03d.json'%n['id']),row)
   a=list(map(F,raw['A']))
   if len(a)!=2 or not 0<a[0]<=a[1]:raise ValueError('positive A interval')
   d=list(map(F,raw['Aprime']))
   if len(d)!=2 or not d[0]<=d[1]<=0:raise ValueError('negative derivative interval')
   if F(raw['s'])!=F(n['s']) or raw['terms']!=160:raise ValueError('oracle input/terms')
   row['target_met']=a[1]-a[0]<=F(1,10**30);rows.append(row)
   current={'stage':'retained','id':n['id']};save(out/'PARTIAL.json',{'current':current,'completed':len(rows),'target_met':row['target_met']})
  save(out/'RESULT.json',{'status':'COMPLETE','scope':'A-only378scalar acquisition','count':378,'all_targets_met':all(r['target_met'] for r in rows),'rows':rows,'seconds':time.monotonic()-start})
 except BaseException as e:
  try:save(out/'FAILURE.json',{'current':current,'completed':len(rows),'error':repr(e),'seconds':time.monotonic()-start})
  except BaseException as x:e.add_note('retention failure: '+repr(x))
  raise
