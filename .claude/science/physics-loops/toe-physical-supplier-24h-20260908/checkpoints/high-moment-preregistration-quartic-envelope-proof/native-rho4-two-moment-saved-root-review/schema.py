import json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(out,rf,elapsed):
 out=Path(out);read=lambda n:json.loads((out/n).read_text())
 def req(x,m):
  if not x:raise ValueError(m)
 r=read('RESULT.json');w=read('WORKER_COMPLETE.json');p=read('PARTIAL.json');b=json.loads(Path(rf['binding_path']).read_text());original=json.loads(Path(b['result']).read_text())
 req(read('STARTED.json')==rf['authorization'],'start')
 req(w['status']=='COMPLETE_SAVED_ONLY'and w['runtime_sha256']==rf['worker_freeze']and w['binding_sha256']==rf['authorization']['binding_sha256']and w['result_sha256']==sha(out/'RESULT.json'),'worker')
 req(all(type(x)in(int,float)and math.isfinite(x)and x>0 for x in(w['seconds'],elapsed))and w['seconds']<29 and w['seconds']<=elapsed<30 and type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'resources')
 req(r['status']=='PASS_SAVED_TWO_MOMENT_RECONSTRUCTION'and r['source_result_sha256']==sha(b['result']),'source')
 for k,v in(('panels',67),('saved_nodes_reconstructed',1742),('saved_integrand_values',3484),('oracle_calls',0)):req(type(r[k])is int and r[k]==v,'count '+k)
 req(type(r['predicates'])is int and r['predicates']>0 and p=={'stage':'complete','predicates':r['predicates'],'panels':list(range(67)),'current':{'panel':66,'node':1741}},'partial')
 req(len(r['rows'])==len(original['rows'])==2 and original['all_targets_met']is True,'two accepted targets')
 for k,name in enumerate(('cminus','mu')):
  x=r['rows'][k];y=original['rows'][k];req(x['observable']==y['observable']==name and x['interval']==y['interval']and x['target_pass']is True and y['status']=='CERTIFIED_TARGET','scalar')
  l,u=map(F,x['interval']);req(l<=u and u-l==F(y['width'])<=F(2,10**28),'exact width')
 expected={'STARTED.json','PARTIAL.json','RESULT.json','WORKER_COMPLETE.json'}|{f'PANEL_{j:02d}.json'for j in range(67)};req({x.name for x in out.iterdir()}==expected,'membership/failure')
 base=Path(b['result']).parent
 for j in range(67):
  x=read(f'PANEL_{j:02d}.json');y=json.loads((base/f'PANELS/{j:02d}.json').read_text());req(type(x['panel'])is int and x['panel']==j-64 and len(x['independent_values'])==2 and x['independent_values']==y['values'],'dual panel')
 return {'status':'PASS_DUAL_NODE_SAVED_SCHEMA','panels':67,'nodes':1742,'integrands':3484,'oracle_calls':0,'result_sha256':sha(out/'RESULT.json'),'external_pending':True}
