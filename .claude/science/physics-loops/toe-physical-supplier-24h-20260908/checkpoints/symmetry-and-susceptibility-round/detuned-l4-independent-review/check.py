from pathlib import Path
import os,sys,hashlib,json,ast,copy
os.environ['OPENBLAS_NUM_THREADS']='1';sys.dont_write_bytecode=True
import numpy as np
p=Path(__file__).resolve().parent;s=p.parent/'detuned-l4-pilot';load=lambda n:json.loads((s/n).read_text());reported=load('ANALYSIS.json');checks=[]
def ck(k,b):
 if not bool(b):raise AssertionError(k)
 checks.append(k)
# Verify exactly the announced bool wrapper delta in the AST.
a=ast.parse((s/'analyze_BEFORE_JSON_REPAIR.py').read_text());b=ast.parse((s/'analyze.py').read_text())
class Strip(ast.NodeTransformer):
 def visit_Call(self,n):
  n=self.generic_visit(n)
  return n.args[0] if isinstance(n.func,ast.Name) and n.func.id=='bool' and len(n.args)==1 else n
ck('serialization_delta_only',ast.dump(a)==ast.dump(Strip().visit(b)))
results={};stored={};maxres=0.
for gi,(pop,burn) in enumerate([(512,160),(1024,160),(1024,320)]):
 cells=[load(f'cell_g{gi}_v{vi}.json') for vi in range(3)]
 for vi,c in enumerate(cells):
  ck(f'cell_identity_{gi}_{vi}',c['L']==4 and c['group']==gi and c['V']==[.93,.95,.97][vi] and c['population']==pop and c['burn']==burn and len(c['replicas'])==8)
  ck(f'cell_resource_{gi}_{vi}',0<c['elapsed_seconds']<180 and 0<c['rss_mib']<384)
  for ri,r in enumerate(c['replicas']):
   ck(f'raw_{gi}_{vi}_{ri}',r['replica']==ri and r['seed']==1030000+10000*gi+ri and all(all(z is True for z in f.values()) for f in r['postconditions']))
   ns=np.array(r['count_samples_last40']);ck(f'window_{gi}_{vi}_{ri}',len(ns)==40 and abs(r['mixed_energy']-(c['V']-1)*ns.mean())<1e-12 and np.max(abs(np.array(r['half_window_energy'])-(c['V']-1)*ns.reshape(2,20).mean(1)))<1e-12)
   ck(f'blocks_{gi}_{vi}_{ri}',len(r['blocks'])==(8 if vi==1 else 0))
   for bl in r['blocks']:
    fi=[12,24].index(bl['F']);ck(f'block_{gi}_{ri}_{bl["F"]}_{bl["origin"]}',bl['seed']==2030000+100000*gi+1000*ri+10*bl['origin']+fi and len(bl['C0_12'])==12 and np.max(abs(np.array(bl['raw_sums_12'])-pop*np.array(bl['C0_12'])))<1e-12)
 E=np.array([[r['mixed_energy'] for r in c['replicas']] for c in cells]).T
 # Common vector = three energies + four denominators; direct covariance/Jacobian contraction.
 D=[];keys=[]
 for h in [1,2]:
  ix=[i for i,m in enumerate(cells[1]['modes']) if m[0]==h];ck(f'six_modes_{gi}_{h}',len(ix)==6)
  for F in [12,24]:
   keys.append((h,F));D.append([sum(sum(np.array(bl['C0_12'])[ix]) for bl in r['blocks'] if bl['F']==F)/4 for r in cells[1]['replicas']])
 Z=np.column_stack([E,np.array(D).T]);cov=np.cov(Z,rowvar=False,ddof=1);mean=Z.mean(0);c=np.array([-.95/.04,-1,.95/.04]);B=mean[:3]@c;rows={}
 for j,(h,F) in enumerate(keys):
  T=mean[3+j];fac=(2 if h==1 else 4)/64;mu=fac*B/T;grad=np.zeros(7);grad[:3]=fac/T*c;grad[3+j]=-fac*B/T**2;se=np.sqrt(grad@cov@grad/8)
  old=next(r for r in reported['groups'][str(gi)]['moments'] if r['harmonic']==h and r['F']==F)
  residual=max(abs(mu-old['moment']),abs(se-old['SE']));maxres=max(maxres,residual);ck(f'ratio_jacobian_{gi}_{h}_{F}',residual<1e-12)
  rows[str((h,F))]={'mu':mu,'SE':se};stored[gi,h,F]=(mu,grad,cov)
 for h in [1,2]:
  x,g,_=stored[gi,h,12];y,k,_=stored[gi,h,24];ss=np.sqrt((g-k)@cov@(g-k)/8)
  if gi==2:
   old=next(r for r in reported['comparisons'] if r['name']=='forward' and r['harmonic']==h);ck(f'paired_forward_{h}',abs(x-y-old['difference'])<1e-12 and abs(ss-old['SE'])<1e-12)
 g=stored[gi,1,24][1];k=stored[gi,2,24][1];actual=np.array([[g@cov@g,g@cov@k],[k@cov@g,k@cov@k]]);ck(f'harmonic_covariance_{gi}',np.max(abs(actual-reported['harmonic_influence_covariance'][str(gi)]))<1e-12)
 for vi in range(3):
  delta=np.array([r['half_window_energy'][0]-r['half_window_energy'][1] for r in cells[vi]['replicas']]);old=reported['groups'][str(gi)]['half_window'][vi];ck(f'paired_half_{gi}_{vi}',abs(delta.mean()-old['difference'])<1e-12 and abs(np.std(delta,ddof=1)/np.sqrt(8)-old['SE'])<1e-12)
 results[str(gi)]=rows
for h in [1,2]:
 for name,ga,gb in [('population',0,1),('burn',1,2)]:
  x,g,C=stored[ga,h,24];y,k,D=stored[gb,h,24];ss=np.sqrt((g@C@g+k@D@k)/8);old=next(r for r in reported['comparisons'] if r['name']==name and r['harmonic']==h);ck(f'independent_{name}_{h}',abs(x-y-old['difference'])<1e-12 and abs(ss-old['SE'])<1e-12)
status=load('STATUS.json');ck('nine_status',len(status)==9 and all(r['exit']==0 for r in status));wall=sum(r['wall_seconds'] for r in status);ck('aggregate',wall+load('MICRO.json')['elapsed_seconds']<600)
out={'actual_check_calls':len(checks),'all_pass':True,'ratio_SE_max_residual':maxres,'independent_Jacobian_results':results,'production_wall':wall,'hashes':{n:hashlib.sha256((s/n).read_bytes()).hexdigest() for n in ['REPORT.md','ANALYSIS.json','analyze.py','pilot.py','PROPOSAL.md']}};(p/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
