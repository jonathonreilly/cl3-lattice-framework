import json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from events_schema import validate
def check(out,rf,elapsed):
 out=Path(out);read=lambda n:json.loads((out/n).read_text())
 def req(x,m):
  if not x:raise ValueError(m)
 r=read('RESULT.json');w=read('WORKER_COMPLETE.json');p=read('PARTIAL.json')
 req(read('STARTED.json')==rf['authorization'],'start')
 req(w['status']=='COMPLETE_SELECTED_PRINCIPAL'and w['runtime_sha256']==rf['worker_freeze']and w['binding_sha256']==rf['authorization']['binding_sha256']and w['result_sha256']==hashlib.sha256((out/'RESULT.json').read_bytes()).hexdigest(),'worker')
 req(type(w['seconds'])in(int,float)and math.isfinite(w['seconds'])and 0<w['seconds']<119 and w['seconds']<=elapsed<120 and type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'resource')
 req(type(r['seconds'])in(int,float)and math.isfinite(r['seconds'])and 0<r['seconds']<=w['seconds'],'result time')
 b=json.loads(Path(rf['binding_path']).read_text())
 req(r['status']=='COMPLETE_SELECTED_PRINCIPAL_ATTEMPT'and len(r['orbits'])==5 and p=={'current':{'stage':'complete'},'rows':r['orbits']},'complete')
 req({x.name for x in out.iterdir()}=={'STARTED.json','RESULT.json','PARTIAL.json','WORKER_COMPLETE.json'}|{f'ORBIT_{i}'for i in range(5)},'membership')
 flags=[]
 for i,row in enumerate(r['orbits']):
  d=out/f'ORBIT_{i}';a=json.loads((d/'RESULT.json').read_text());ids=json.loads((d/'SELECTED.json').read_text())
  req(type(row['orbit'])is int and row['orbit']==i and row['status']==a['status'],'orbit')
  req(len(ids)==24 and len(set(ids))==24 and all(type(x)is int and 0<=x<399 for x in ids),'selected')
  history_path=b['histories'][i];req(hashlib.sha256(Path(history_path).read_bytes()).hexdigest()==b['inputs'][history_path],'bound history')
  history=json.loads(Path(history_path).read_text());req(ids==[h['index']for h in history['history']],'exact selected order')
  allowed={'SELECTED.json','EVENTS.ndjson','RESULT.json'}
  if (d/'CANDIDATE.json').exists():allowed.add('CANDIDATE.json')
  req({x.name for x in d.iterdir()}==allowed,'orbit membership')
  events=[json.loads(x)for x in (d/'EVENTS.ndjson').read_text().splitlines()]
  req(all(type(e['sequence'])is int and e['sequence']==j for j,e in enumerate(events)),'event sequence')
  validate(events,a,json.loads((d/'CANDIDATE.json').read_text())if 'CANDIDATE.json'in allowed else None,i,req)
  if a['status']=='CERTIFIED_ENCLOSURE':
   req('CANDIDATE.json'in allowed and len(a['center'])<=96 and all(len(x)==48 for x in a['center']),'box shape')
   b=F(a['radius']);req(b>=0 and 0<=F(a['e'])<1 and type(a['width_pass'])is bool and a['width_pass']==(2*b<=F(1,2**39)),'width')
   l1=max(sum(abs(F(x[j]))+b for x in a['center'])for j in range(48));req(type(a['l1_pass'])is bool and a['l1_pass']==(l1<=2**40),'l1')
   req(any(e['stage']=='coefficient_box'for e in events),'box retention');flags.append(a['width_pass']and a['l1_pass'])
  else:req(a['status']in('INDETERMINATE_RESIDUAL','INDETERMINATE_LIMIT_OR_CANDIDATE'),'honest incomplete certificate');flags.append(False)
 return {'status':'PASS_SELECTED_PRINCIPAL_SCHEMA','coefficient_gate_passes':sum(flags),'arithmetic_independently_replayed':False}
