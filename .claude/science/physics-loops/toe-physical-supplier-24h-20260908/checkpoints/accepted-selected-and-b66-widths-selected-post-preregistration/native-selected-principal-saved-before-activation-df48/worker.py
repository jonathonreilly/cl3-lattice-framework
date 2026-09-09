import json,time,hashlib,math
from pathlib import Path
from fractions import Fraction
from replay import check

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()
def dump(p,x):
 with p.open('w')as f:json.dump(x,f,default=str);f.write('\n');f.flush()
def compute(plan,out):
 out=Path(out);rows=[];current={};start=time.monotonic()
 def persist(stage,data):
  nonlocal current
  current={'stage':stage,'orbit':len(rows)}
  with (out/'INDEPENDENT.ndjson').open('a')as f:json.dump({'current':current,'data':data},f,default=str);f.write('\n');f.flush()
  dump(out/'PARTIAL.json',{'current':current,'rows':rows})
 try:
  persist('initial_pins',{})
  for p,h in plan['inputs'].items():
   if sha(p)!=h:raise ValueError('input pin '+p)
  acc=json.loads(Path(plan['acceptance']).read_text())
  if acc['status']!='ACCEPTED_DIRECT_SELECTED_PRINCIPAL_ENCLOSURES' or acc['result_sha256']!=plan['result_sha256']:raise ValueError('acceptance')
  if acc['worker_freeze']!=plan['producer_freeze'] or acc['root_freeze']!=plan['root_freeze']:raise ValueError('source linkage')
  for key,cap in [('external_seconds',120),('external_max_rss',384*1048576),('sampled_whole_tree_peak',384*1048576)]:
   v=acc[key]
   if type(v)not in (int,float)or not math.isfinite(v)or not 0<v<=cap:raise ValueError('resource receipt')
  for i in range(5):
   d=Path(plan['output'])/f'ORBIT_{i}';persist('before_orbit_parse',{})
   if {p.name for p in d.iterdir()}!={'SELECTED.json','EVENTS.ndjson','CANDIDATE.json','RESULT.json'}:raise ValueError('orbit membership')
   saved=[]
   with (d/'EVENTS.ndjson').open()as f:
    for n,line in enumerate(f):
     if n>=2705 or len(line)>8*1048576:raise ValueError('event size/count')
     e=json.loads(line)
     if type(e['sequence'])is not int or e['sequence']!=n:raise ValueError('sequence')
     saved.append(e)
   if len(saved)!=2705:raise ValueError('fixed completed events')
   ids=json.loads((d/'SELECTED.json').read_text());t=json.loads((d/'CANDIDATE.json').read_text());a=json.loads((d/'RESULT.json').read_text())
   ans=check(ids,saved,t,a,persist);rows.append({'orbit':i,**ans});persist('orbit_complete',{})
   del saved,t,a,ids
  persist('final_pins',{})
  for p,h in plan['inputs'].items():
   if sha(p)!=h:raise ValueError('final input pin '+p)
  persist('complete',{});dump(out/'RESULT.json',{'status':'PASS_INDEPENDENT_SELECTED_SAVED','rows':rows,'seconds':time.monotonic()-start,'entry_truth_inherited':True})
 except BaseException as exc:
  dump(out/'FAILURE.json',{'error':repr(exc),'current':current,'rows':rows});raise
