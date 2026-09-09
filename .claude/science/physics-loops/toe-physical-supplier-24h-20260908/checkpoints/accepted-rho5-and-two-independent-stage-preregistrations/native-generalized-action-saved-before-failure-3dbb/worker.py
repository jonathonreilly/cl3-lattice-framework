import json,time,hashlib,math,os
from pathlib import Path
from fractions import Fraction as F
from stream import SavedStages,verify,sha

def save(p,x):
 temp=p.with_suffix(p.suffix+'.tmp')
 with temp.open('w')as f:json.dump(x,f,default=str);f.write('\n');f.flush()
 os.replace(temp,p)

def compute(plan,out):
 out=Path(out);rows=[];current={};start=time.monotonic();seq=0
 def persist(stage,data):
  nonlocal current,seq
  current=dict(orbit=len(rows),stage=stage,sequence=seq);save(out/'PARTIAL.json',dict(current=current,rows=rows))
  save(out/f'{seq:05d}_{stage}.json',data);seq+=1
  if seq>25000:raise ValueError('output stage cap')
 def read(path):
  if sha(Path(path))!=plan['inputs'][path]:raise ValueError('input hash')
  return json.loads(Path(path).read_text())
 try:
  persist('binding',{})
  for path,h in plan['inputs'].items():
   if sha(Path(path))!=h:raise ValueError('initial closure')
  a=read(plan['acceptance'])
  if a['status']!='ACCEPTED_FIRST_GENERALIZED_24_ACTION_TARGET_EXCLUDED'or a['result_sha256']!=plan['result_sha256']or a['worker_freeze']!=plan['producer_freeze']:raise ValueError('accepted scope')
  for key,cap in [('external_seconds',180),('external_rss_bytes',384*1048576),('sampled_whole_tree_peak',384*1048576)]:
   v=a[key]
   if type(v)not in(int,float)or not math.isfinite(v)or not 0<v<=cap or (key!='external_seconds'and type(v)is not int):raise ValueError('accepted resource')
  pp=read(plan['pole_binding']);pole_rows=read(pp['poles'])['rows']
  if len(pole_rows)!=66:raise ValueError('66 poles')
  pi=sum(map(F,pp['pi_interval']))/2
  if not 3<pi<4:raise ValueError('pi midpoint')
  poles=[];alpha=[]
  for i,row in enumerate(pole_rows):
   if type(row['id'])is not int or row['id']!=i:raise ValueError('pole id')
   ss=F(row['s_midpoint']);lo,hi=map(F,row['weight'])
   if not 0<lo<=hi or hi-lo>F(2,2**140)or not F(1,128)<=ss<=16:raise ValueError('family')
   poles.append(ss);alpha.append(35*(lo+hi)/(4*pi))
  for oi in range(5):
   persist('orbit_start',{})
   d=Path(plan['output'])/f'ORBIT_{oi}';names=plan['events'][oi]
   if sorted(x.name for x in d.iterdir())!=sorted([Path(x).name for x in names]+['RESULT.json']):raise ValueError('output membership')
   record=read(names[0]);ans=read(str(d/'RESULT.json'))
   if type(record['orbit'])is not int or record['orbit']!=oi:raise ValueError('orbit')
   stream=SavedStages(names,plan['inputs'],persist)
   result=verify(record,poles,alpha,ans,stream)
   rows.append(dict(orbit=oi,**result));persist('orbit_complete',{})
  for path,h in plan['inputs'].items():
   if sha(Path(path))!=h:raise ValueError('final closure')
  save(out/'RESULT.json',dict(status='PASS_INDEPENDENT_GENERALIZED_STAGES',rows=rows,seconds=time.monotonic()-start,stage_files=seq,inherited_native_entry_truth=True))
  save(out/'PARTIAL.json',dict(current={'stage':'complete'},rows=rows))
 except BaseException as e:
  save(out/'FAILURE.json',dict(error=repr(e),current=current,rows=rows));raise
