import json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def req(x,m):
 if not x:raise ValueError(m)
def check(out,rf,elapsed):
 out=Path(out);read=lambda n:json.loads((out/n).read_text());r=read('RESULT.json');w=read('WORKER_COMPLETE.json');p=read('PARTIAL.json');b=json.loads(Path(rf['binding_path']).read_text());original=json.loads(Path(b['result']).read_text())
 req(read('STARTED.json')==rf['authorization'],'start')
 req(w['status']=='COMPLETE_SAVED_ONLY'and w['runtime_sha256']==rf['worker_freeze']and w['binding_sha256']==rf['authorization']['binding_sha256']and w['result_sha256']==sha(out/'RESULT.json'),'worker')
 req(type(w['seconds'])in(int,float)and math.isfinite(w['seconds'])and 0<w['seconds']<29 and w['seconds']<=elapsed<30 and type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'resources')
 req(r['status']=='PASS_SAVED_RECONSTRUCTION'and r['observable']=='nu=E_X_power_3_over_2'and r['source_result_sha256']==sha(b['result']),'source/status')
 for k,v in(('panels',67),('tail_terms',40),('saved_nodes_reconstructed',1742),('oracle_calls',0),('new_oracle_calls',0)):req(type(r[k])is int and r[k]==v,'count '+k)
 req(r['interval']==original['interval']and r['scientific_status']==original['status']=='CERTIFIED_TARGET'and r['middle_width_gate']is True,'accepted scalar')
 req(type(r['predicates'])is int and r['predicates']>0 and p=={'stage':'complete','predicates':r['predicates'],'panels':list(range(67)),'current':{'panel':66,'node':1741}},'final partial')
 expected={'STARTED.json','PARTIAL.json','RESULT.json','WORKER_COMPLETE.json'}|{f'PANEL_{j:02d}.json'for j in range(67)};req(set(x.name for x in out.iterdir())==expected,'outputs/failure')
 base=Path(b['result']).parent
 for j in range(67):
  x=read(f'PANEL_{j:02d}.json');y=json.loads((base/f'PANELS/{j:02d}.json').read_text());req(type(x['panel'])is int and x['panel']==j-64 and x['independent_value']==y['value'],'saved panel '+str(j))
 return {'status':'PASS_FULL_NODE_SAVED_SCHEMA','result_sha256':sha(out/'RESULT.json'),'source_result_sha256':sha(b['result']),'panels':67,'nodes':1742,'oracle_calls':0,'scientific_status':r['scientific_status'],'external_pending':True}
