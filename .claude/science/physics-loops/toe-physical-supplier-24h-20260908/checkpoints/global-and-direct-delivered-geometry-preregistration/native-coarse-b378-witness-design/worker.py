from pathlib import Path
import json,time,os
from fractions import Fraction as F
from binder import load
from bcore import one,moment,pi_bounds

def save(p,x):
 tmp=p.with_name(p.name+'.tmp')
 with tmp.open('w') as f:json.dump(x,f,default=str);f.write('\n');f.flush();os.fsync(f.fileno())
 os.replace(tmp,p)
def run(out,plan):
 out=Path(out);out.mkdir(exist_ok=False);rows=[];current={};start=time.monotonic()
 def emit(stage,data):
  nonlocal current
  current={'stage':stage,'pole':len(rows),'data':data}
  if stage=='before_node' and data['id']%26: return
  # Before-node progress overwrites one small file; only panel/high/final evidence is appended.
  save(out/'PARTIAL.json',{'current':current,'completed':len(rows)})
  if stage in ('panel','final_interval','moment'):
   with (out/'PANELS.jsonl').open('a') as f:json.dump(current,f,default=str);f.write('\n');f.flush();os.fsync(f.fileno())
 try:
  new,catalog=load(plan,emit);pi=pi_bounds();moments=[]
  for n in range(41):emit('before_moment',{'n':n});moments.append(moment(n));emit('moment',{'n':n,'value':moments[-1]})
  for row in new:
   ans=one(row['s'],row['A'],catalog,moments,pi,emit)
   result={'id':row['id'],'s':row['s'],'B':ans,'required_radius':row['target_radius'],'target_met':(ans[1]-ans[0])/2<=row['target_radius']}
   save(out/('B_%03d.json'%row['id']),result);rows.append(result)
  save(out/'RESULT.json',{'status':'COMPLETE_NEW_B378_ONLY','rows':rows,'seconds':time.monotonic()-start,'all_targets_met':all(r['target_met'] for r in rows),'witness_computed':False});emit('complete',{})
 except BaseException as e:
  try:save(out/'FAILURE.json',{'current':current,'completed':len(rows),'error':repr(e)})
  except BaseException as x:e.add_note('retention '+repr(x))
  raise
