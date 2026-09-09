import json,hashlib,math
from pathlib import Path
from fractions import Fraction as F

def need(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def check(out,rf,elapsed,progress=lambda x:None):
 out=Path(out);rd=lambda n:json.loads((out/n).read_text());r=rd('RESULT.json');w=rd('WORKER_COMPLETE.json');p=rd('PARTIAL.json')
 need(rd('STARTED.json')==rf['authorization'],'STARTED');need(w['status']=='COMPLETE_NEW_RHO5_ONLY'and w['runtime_sha256']==rf['worker_freeze']and w['binding_sha256']==rf['binding_sha256']and w['result_sha256']==sha(out/'RESULT.json'),'worker binding')
 for x in [r['seconds'],w['seconds'],p['seconds'],elapsed]:need(type(x)in(int,float)and math.isfinite(x)and 0<x<30,'finite time')
 need(p['seconds']<=r['seconds']<=w['seconds']<29 and w['seconds']<=elapsed,'nested time');need(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'RSS')
 need(r['status']=='COMPLETE_NEW_RHO5_COMPONENT_CERTIFICATES'and r['oracle_calls']==0 and type(r['oracle_calls'])is int and r['node_integrands_recomputed']==0,'scope');need(len(r['rows'])==3 and p['rows']==r['rows']and p['stage']=='complete','three rows/partial')
 flags=[]
 for name,row in zip(['cminus','mu','nu'],r['rows']):
  need(row['observable']==name and rd(name+'.json')==row,'row binding');a,b=map(F,row['interval']);lo,hi=map(F,row['original_interval']);width=F(row['width']);need(lo<=a<=b<=hi and width==b-a and F(row['target'])==F(2,10**28),'interval and target');need(type(row['target_met'])is bool and row['target_met']==(width<=F(2,10**28)),'flag');flags.append(row['target_met'])
 need(type(r['all_targets_met'])is bool and r['all_targets_met']==all(flags),'overall target');need(type(p['event'])is int and p['event']==416,'event count')
 expected={'RESULT.json','WORKER_COMPLETE.json','STARTED.json','PARTIAL.json','cminus.json','mu.json','nu.json'}|{f'EVENT_{i:04d}.json'for i in range(1,p['event']+1)};need({x.name for x in out.iterdir()}==expected,'membership');need(rd(f"EVENT_{p['event']:04d}.json")=={'stage':'complete'},'last event');progress({'stage':'verified_saved_receipts'})
 return {'status':'PASS_NEW_CERTIFICATE_SCHEMA','all_targets_met':all(flags),'rows':3,'node_formulas_replayed':0,'scope':'receipt/target schema only; worker performs component reconstruction'}
