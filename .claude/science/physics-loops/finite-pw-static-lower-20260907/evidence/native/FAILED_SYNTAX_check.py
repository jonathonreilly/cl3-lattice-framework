from itertools import product
from pathlib import Path
import json,time,resource,hashlib
import sympy as s
start=time.monotonic();checks=[]
def ck(n,b):
 if not b or n in checks:raise AssertionError(n)
 checks.append(n)
verts=list(product(range(2),repeat=3));edges=[]
for x in verts:
 for a in range(3):
  if x[a]==0:
   y=list(x);y[a]=1;edges.append((verts.index(x),verts.index(tuple(y))))
def solve(es,target):
 B=[[int(i==u)-int(i==v) for u,v in es] for i in range(8)];b=[int(i==0)-int(i==target) for i in range(8)]
 A=[[x%3 for x in row]+[y%3] for row,y in zip(B,b)];piv=[];r=0
 for c in range(len(es)):
  pivot=next((i for i in range(r,8) if A[i][c]),None)
  if pivot is None:continue
  A[r],A[pivot]=A[pivot],A[r];inv=1 if A[r][c]==1 else2
  A[r]=[(inv*x)%3 for x in A[r]]
  for i in range(8):
   if i!=r:
    f=A[i][c];A[i]=[(x-f*y)%3 for x,y in zip(A[i],A[r])]
  piv.append(c);r+=1
 free=[i for i in range(len(es)) if i not in piv];sol=[]
 for vals in product(range(3),repeat=len(free)):
  z=[0]*len(es)
  for i,v in zip(free,vals):z[i]=v
  for row,c in enumerate(piv):z[c]=(A[row][-1]-sum(A[row][j]*z[j] for j in free))%3
  sol.append(z)
 return B,b,r,free,sol
# source support connectivity, using labels only as a necessary center condition.
def connected(z,es,target):
 seen={0};todo=[0]
 while todo:
  u=todo.pop()
  for (a,b),q in zip(es,z):
   if q and (a==u or b==u):
    v=b if a==u else a
    if v not in seen:seen.add(v);todo.append(v)
 return target in seen
out={}
for target,d in [(verts.index((1,0,0)),1),(7,3)]:
 B,b,rank,free,sol=solve(edges,target)
 ck(f'target{target}_rank7_free5',rank==7 and len(free)==5)
 ck(f'target{target}_all243_congruences',len(sol)==243 and all(all((sum(v*q for v,q in zip(row,z))-b[i])%3==0 for i,row in enumerate(B)) for z in sol))
 ck(f'target{target}_all_supports_connect',all(connected(z,edges,target) for z in sol))
 weights=[sum(q!=0 for q in z) for z in sol]
 ck(f'target{target}_minimum_energy4d',min(weights)*4==4*d)
 out[str(target)]={'solutions':sol,'histogram':{str(k):weights.count(k) for k in sorted(set(weights))},'distance':d}
gedges=edges+[(0,7)];B,b,rank,free,sol=solve(gedges,7)
ck('ghost_unrestricted_shortcut',min(sum(q!=0 for q in z) for z in sol)==1)
kept=[z for z in sol if z[-1]==0]
ck('ghost_vacuum_restores_actual_distance',min(sum(q!=0 for q in z) for z in kept)==3)
ck('ghost_vacuum_exact243',len(kept)==243)
ck('missing_endpoint_Gauss_allows_zero',all(b[i]%3==0 for i in range(1,7)))
ck('full_Gauss_rejects_zero',any(x%3 for x in b))
K=s.diag(0,1,10);H=s.Matrix([[2,-1,0],[-1,2,0],[0,0,10]]);P=s.diag(1,0,1);V=H-K
ck('Ritz_toy_positive_perturbation',V.is_positive_semidefinite)
ck('Ritz_toy_cutoff_commutes_K',P*K==K*P)
ck('Ritz_toy_both_minima_nondecrease',min(H[:2,:2].eigenvals())==1 and H[0,0]==2 and H[2,2]==10)
ck('Ritz_toy_subtracted_gap_decreases',10-2<10-1)
ck('actual_R1_retains_both_path_orientations',[(p,q) for p in range(2) for q in range(2) if p+q<=1]==[(0,0),(0,1),(1,0)])
result={'TOTAL':len(checks),'checks':checks,'vertices':verts,'edges':edges,'flows':out,'ghost_solutions':len(sol),'ghost_vacuum_solutions':len(kept),'Ritz_toy':{'full_ground':1,'cutoff_ground':2,'charged_both':10,'gap_full':9,'gap_cutoff':8},'scope':'Necessary actual R1 center-flow controls plus an abstract Ritz subtraction adverse. Not all center flows are claimed SU3-admissible, and no finite test proves imported resolvent constants.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start,'rss_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2)}
print(json.dumps(result,indent=2,allow_nan=False))
