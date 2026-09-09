import json,hashlib,pathlib,types,shutil,copy
from fractions import Fraction as F
P=pathlib.Path(__file__).resolve().parent
source=P.parent/'native-fixed192-compression-root-review'
m=types.ModuleType('schema');exec(compile((source/'schema.py').read_bytes(),str(source/'schema.py'),'exec'),m.__dict__)
S=2**192;count=0
rf={'authorization':{'binding_sha256':'bind'},'worker_freeze':'wf','source_ast_sha256':'ast'}
ctx={'binding_sha256':'bind','source_freeze_sha256':'ast','radii':{'etaA':'0','etaB':'0','etac':'0','etaa0':'0','alpha_max':'1'}}
def write(p,x):p.write_text(json.dumps(x)+'\n')
def make(out):
 out.mkdir();write(out/'STARTED.json',rf['authorization']);write(out/'CONTEXT.json',ctx);rows=[]
 for oi in range(5):
  d=out/f'ORBIT_{oi}';d.mkdir();history=[];events=[]
  for step in range(5):
   if step:
    i=step-1;g=[[0,0] for _ in range(399)];g[i]=[S,S]
    h={'index':i,'chirality':-1 if i%2==0 else 1,'r':[S,S],'g':g,'j':[[0,0] for _ in range(399)]};history.append(h);events.append({'orbit':oi,'stage':'pivot_saved',**h})
   diag=[[S,S] for _ in range(399)]
   events.append({'orbit':oi,'stage':'diagonals_complete','step':step,'diagonals':diag})
   cp={'orbit':oi,'stage':'checkpoint','pairs':step,'raw_residual_upper':'795','coordinate_radius_squared':'0','coordinate_intervals':[[[[0,0] for _ in range(399)] for _ in range(2)] for _ in range(step)],'residual_pass':False,'coordinate_pass':True}
   events.append(cp)
  write(d/'HISTORY.json',{'context':ctx,'orbit':oi,'history':history});write(d/'RESULT.json',{'status':'PAIR_CAP','pairs':4,'history':history})
  (d/'EVENTS.ndjson').write_text(''.join(json.dumps(e)+'\n' for e in events))
  rows.append({'orbit':oi,'status':'PAIR_CAP','pairs':4,'result_sha256':m.sha(d/'RESULT.json'),'events_sha256':m.sha(d/'EVENTS.ndjson')})
 write(out/'PARTIAL.json',cp);write(out/'RESULT.json',{'status':'COMPLETE_FIXED_FOUR_PAIR_PROBE','seconds':1,'orbits':rows});write(out/'WORKER_COMPLETE.json',{'status':'COMPLETE_COST_PRECISION_PROBE_ONLY','freeze_sha256':'wf','binding_sha256':'bind','result_sha256':m.sha(out/'RESULT.json'),'seconds':2,'rss_bytes':1000,'all_scientific_targets_met':False})
def rehash(out):
 r=json.loads((out/'RESULT.json').read_text())
 for i,row in enumerate(r['orbits']):
  d=out/f'ORBIT_{i}';row['result_sha256']=m.sha(d/'RESULT.json');row['events_sha256']=m.sha(d/'EVENTS.ndjson')
 write(out/'RESULT.json',r);w=json.loads((out/'WORKER_COMPLETE.json').read_text());w['result_sha256']=m.sha(out/'RESULT.json');write(out/'WORKER_COMPLETE.json',w)
root=P/'SYNTHETIC';root.mkdir(exist_ok=True);base=root/'base';make(base)
m.check(base,rf,3);count+=1
for kind in ('weighted_residual','coordinate_weight','history_missing','history_index','false_allpass','partial','failure','bool_rss','time','pairs_bool'):
 out=root/kind;shutil.copytree(base,out)
 if kind in ('weighted_residual','coordinate_weight'):
  f=out/'ORBIT_0/EVENTS.ndjson';ev=[json.loads(l) for l in f.read_text().splitlines()]
  if kind=='weighted_residual':ev[-1]['raw_residual_upper']='399'
  else:ev[-1]['coordinate_intervals'][0][0][0]=[0,S];ev[-1]['coordinate_radius_squared']='1';ev[-1]['coordinate_pass']=False
  f.write_text(''.join(json.dumps(e)+'\n' for e in ev))
 elif kind=='history_missing':(out/'ORBIT_0/HISTORY.json').unlink()
 elif kind=='history_index':
  f=out/'ORBIT_0/RESULT.json';x=json.loads(f.read_text());x['history'][0]['index']=True;write(f,x)
 elif kind=='partial':write(out/'PARTIAL.json',{})
 elif kind=='failure':write(out/'FAILURE.json',{})
 elif kind=='pairs_bool':
  f=out/'ORBIT_0/RESULT.json';x=json.loads(f.read_text());x['pairs']=True;write(f,x)
 else:
  f=out/'WORKER_COMPLETE.json';x=json.loads(f.read_text());x[{'false_allpass':'all_scientific_targets_met','bool_rss':'rss_bytes','time':'seconds'}[kind]]={'false_allpass':True,'bool_rss':True,'time':float('nan')}[kind];write(f,x)
 rehash(out)
 try:m.check(out,rf,3)
 except (ValueError,FileNotFoundError):count+=1
 else:raise ValueError('accepted adverse '+kind)
write(P/'SCHEMA_TEST_RESULT.json',{'status':'PASS','cases':count,'nonzero_four_pair_fixture':True,'all_adverses_rehashed':True,'native_loads':0});print(count)
