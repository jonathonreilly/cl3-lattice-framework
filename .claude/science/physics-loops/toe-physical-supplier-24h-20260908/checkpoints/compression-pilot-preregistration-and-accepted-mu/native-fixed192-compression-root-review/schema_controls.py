"""Fabricated zero-pair schema only; no matrix, entry, index or pivot calls."""
from pathlib import Path
import tempfile,json,hashlib,types
R=Path(__file__).resolve().parent
m=types.ModuleType('schema');exec(compile((R/'schema.py').read_bytes(),str(R/'schema.py'),'exec'),m.__dict__)
def write(p,x):p.write_text(json.dumps(x)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
with tempfile.TemporaryDirectory() as tmp:
 o=Path(tmp);rf={'worker_freeze':'f','authorization':{'binding_sha256':'b'},'source_ast_sha256':'s'}
 context={'binding_sha256':'b','source_freeze_sha256':'s','radii':{'etaA':'0','etaB':'0','etac':'0','etaa0':'0','alpha_max':'1'}}
 write(o/'STARTED.json',rf['authorization']);write(o/'CONTEXT.json',context);rows=[]
 for i in range(5):
  d=o/f'ORBIT_{i}';d.mkdir();diag=[[0,m.S]]*399
  e={'stage':'checkpoint','orbit':i,'pairs':0,'raw_residual_upper':'795','coordinate_radius_squared':'0','coordinate_intervals':[],'residual_pass':False,'coordinate_pass':True}
  (d/'EVENTS.ndjson').write_text(json.dumps({'stage':'diagonals_complete','orbit':i,'step':0,'diagonals':diag})+'\n'+json.dumps(e)+'\n')
  write(d/'RESULT.json',{'status':'PRECISION_STALL','pairs':0,'history':[]});rows.append({'orbit':i,'status':'PRECISION_STALL','pairs':0,'result_sha256':sha(d/'RESULT.json'),'events_sha256':sha(d/'EVENTS.ndjson')})
 write(o/'PARTIAL.json',e);result={'status':'COMPLETE_FIXED_FOUR_PAIR_PROBE','orbits':rows,'seconds':1};write(o/'RESULT.json',result)
 w={'status':'COMPLETE_COST_PRECISION_PROBE_ONLY','seconds':2,'rss_bytes':1000,'freeze_sha256':'f','binding_sha256':'b','result_sha256':sha(o/'RESULT.json'),'all_scientific_targets_met':False};write(o/'WORKER_COMPLETE.json',w)
 m.check(o,rf,3);checks=1
 for key,value in [('rss_bytes',True),('seconds',float('nan')),('all_scientific_targets_met',True),('freeze_sha256','bad')]:
  bad=dict(w);bad[key]=value;write(o/'WORKER_COMPLETE.json',bad)
  try:m.check(o,rf,3)
  except (ValueError,KeyError):checks+=1
  else:raise ValueError('mutant accepted '+key)
 write(o/'WORKER_COMPLETE.json',w);write(o/'FAILURE.json',{})
 try:m.check(o,rf,3)
 except ValueError:checks+=1
 else:raise ValueError('failure accepted')
 print(json.dumps({'status':'PASS','checks':checks,'scope':'fabricated zero-pair receipt/schema only','native_calls':0}))
