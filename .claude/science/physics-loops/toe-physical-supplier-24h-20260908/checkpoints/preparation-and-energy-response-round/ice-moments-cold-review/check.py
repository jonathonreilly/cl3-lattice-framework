import os,sys
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS']:os.environ[k]='1'
sys.dont_write_bytecode=True
import importlib.util,json
from fractions import Fraction as F
p='/private/tmp/toe-physical-supplier-24h-20260908/scripts/spin_half_cartesian_plaquette_source_2026_09_07.py';spec=importlib.util.spec_from_file_location('geom',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
links,faces,states,arcs=m.component();n=len(states);O=[sum((-1)**(sum(r)+r[0])*(2*((x>>i)&1)-1) for i,(r,a) in enumerate(links) if a==1) for x in states];adj=[[]for _ in states];checks={};unsigned_fail=0
for ii,jj,ff,ss in arcs:
 i,j,f,sign=map(int,[ii,jj,ff,ss]);root,orientation,ids,mask=faces[f];adj[i].append(j)
 if orientation==0:
  predicted=4*((-1)**(sum(root)+root[0]))*sign
  assert O[j]-O[i]==predicted
  unsigned_fail+=O[j]-O[i]!=4*((-1)**(sum(root)+root[0]))
 else:assert O[j]==O[i]
checks['all_signed_updates']=True;checks['root_parity_only_adverse']=unsigned_fail>0
z=sum(o*o for o in O);v=O[:];mom=[]
for k in range(9):
 mom.append(F(sum(a*b for a,b in zip(O,v)),z));v=[sum(v[i]-v[j]for j in adj[i]) for i in range(n)]
expected=['1','8/5','16/5','80/9','568/15','2144/9','28592/15','784576/45','7890176/45'];assert list(map(str,mom))==expected;checks['python_integer_moments']=True
Y=[];local=[];second=[]
for i in range(n):
 vals=[12*(O[j]-O[i])**2 for j in adj[i]]+[0]*(24-len(adj[i]));Y.extend(vals);local.append(F(sum(vals),24));second.append(sum(O[i]-O[j]for j in adj[i])**2)
def var(v):return sum(x*x for x in v)/F(len(v))-(sum(v)/F(len(v)))**2
va,vl=var(Y),var(local);assert va==F(32768,9) and vl==F(7168,27);checks['exact_numerator_variances']=True
S=F(z,n);infl=sum((F(y)-mom[1]*O[i]**2)**2 for i in range(n) for y in ([12*(O[j]-O[i])**2 for j in adj[i]]+[0]*(24-len(adj[i]))))/F(n*24)/S**2
inflocal=sum((x-mom[1]*o*o)**2 for x,o in zip(local,O))/n/S**2
assert float(inflocal)==6.4768;checks['ratio_influence']=True
assert var(second)==F(41984,9);in2=sum((F(x)-mom[2]*o*o)**2 for x,o in zip(second,O))/n/S**2;assert in2==F(9232,625);checks['second_variance']=True
print(json.dumps({'checks':checks,'count':len(checks),'root_parity_only_failed_arcs':unsigned_fail,'moments':list(map(str,mom)),'ratio_influence_single':str(infl),'ratio_influence_local':str(inflocal),'second_ratio_variance':str(in2)},indent=2))
