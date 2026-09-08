import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
from pathlib import Path
import numpy as np,itertools,subprocess,json,hashlib,contextlib,io,runpy
p=Path(__file__).resolve().parent;src=Path('/private/tmp/toe-24h-probes-20260908/phase-preparation')
# Scratch instrumentation only: capture complete matrices at each original row emission.
text=(src/'path_probe.py').read_text().replace('rows=[]','rows=[]\nbound_cases=[]')
text=text.replace("  rows.append({'family':", "  bound_cases.append((family,beta,O.copy(),Qready.copy(),{k:v.copy() for k,v in branches.items()},V.copy()))\n  rows.append({'family':")
f=p/'captured_path_probe.py';f.write_text(text)
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(f))
edges=[(0,1),(1,2),(2,3),(0,4),(1,5),(2,6),(3,7),(0,8)]
masks=[a for a in range(512) if a.bit_count()%2==0];ix={a:k for k,a in enumerate(masks)};dim=256
car=[];phys=[];map_phys=[]
for k in range(256):
 bit=[(k>>(7-j))&1 for j in range(8)];a=sum((sum(bit[j] for j,e in enumerate(edges) if v in e)%2)<<v for v in range(9));map_phys.append(a)
for eidx,(u,v) in enumerate(edges):
 C=np.zeros((dim,dim),complex);P=np.zeros_like(C)
 for j,a in enumerate(masks):
  if ((a>>u)&1)!=((a>>v)&1):
   b=a^(1<<u)^(1<<v);sgn=(-1)**sum((a>>w)&1 for w in range(u+1,v));C[ix[b],j]=sgn
 for j,a in enumerate(map_phys):
  bu=1-2*((a>>u)&1);bv=1-2*((a>>v)&1)
  sign=1
  for x,y in [(u,v),(v,u)]:
   for l,e in enumerate(edges):
    if x in e and l!=eidx and (e[1] if e[0]==x else e[0])<y:sign*=1-2*((j>>(7-l))&1)
  P[j^(1<<(7-eidx)),j]=.5j*sign*(bu-bv)
 car.append(C);phys.append(P)
# Independent dictionary phases from CAR/native transition edges, per fixed-N component.
phase={};inv_phys={a:j for j,a in enumerate(map_phys)}
for root in range(256):
 if root in phase:continue
 phase[root]=1.;todo=[root]
 while todo:
  j=todo.pop();a=map_phys[j]
  for C,P in zip(car,phys):
   inds=np.flatnonzero(abs(P[:,j])>.5)
   if not len(inds):continue
   k=int(inds[0]);b=map_phys[k];q=P[k,j]*phase[j]/C[ix[b],ix[a]]
   if k in phase:assert abs(phase[k]-q)<1e-12
   else:phase[k]=q;todo.append(k)
D=np.zeros((256,256),complex)
for j,a in enumerate(map_phys):D[j,ix[a]]=phase[j]
checks={};res={}
def ck(n,a,b,tol=5e-10):
 err=float(np.linalg.norm(a-b));res[n]=err;checks[n]=err<tol;assert err<tol,(n,err)
ck('dictionary_unitary',D.conj().T@D,np.eye(256))
for j in range(8):
 ck('native_bit_operator_'+str(j),phys[j],d['T'][j]);ck('CAR_dictionary_'+str(j),D.conj().T@phys[j]@D,car[j])
nums=[np.diag([(a>>j)&1 for a in masks]) for j in range(9)];I=np.eye(256)
for family,beta,O,Qready,branches,V in d['bound_cases']:
 tag=str(family)+'_'+str(beta)
 # Exterior-power lift by minors; no QR/Givens construction used.
 G=np.zeros((256,256),complex)
 for a in masks:
  aa=[j for j in range(4) if (a>>j)&1]
  for b in masks:
   if a>>4!=b>>4:continue
   bb=[j for j in range(4) if (b>>j)&1]
   if len(aa)!=len(bb):continue
   G[ix[a],ix[b]]=np.linalg.det(O[np.ix_(aa,bb)]) if aa else 1.
 ck('wedge_compiled_rotation_'+tag,D@G@D.conj().T,V)
 couplings=[(1,2,3),(2,1,2)][family];h=np.diag(couplings,1)+np.diag(couplings,-1);eps=np.linalg.eigvalsh(h)
 Qc=D.conj().T@Qready;r=np.exp(-beta*abs(eps)/2);sines=np.sqrt(1-r*r)
 bs={'':G.conj().T@Qc}
 for j in range(4):
  C=car[3+j];u=I+(r[j]-1)*(C@C)-1j*sines[j]*C;fresh={}
  for key,col in bs.items():
   moved=u@col;fresh[key+'0']=(I-nums[4+j])@moved;fresh[key+'1']=nums[4+j]@moved
  bs=fresh
 for key,col in bs.items():ck('full_branch_'+tag+'_'+key,D@G@col,branches[key])
 probs={key:float(np.linalg.norm(col)**2/16) for key,col in bs.items()};success=''.join(str(int(x<0)) for x in eps)
 predicted=np.prod((1+np.exp(-beta*abs(eps)))/2)
 ck('probability_'+tag,np.array([probs[success]]),np.array([predicted]),2e-12)
 ck('all16_probabilities_'+tag,np.array([sum(probs.values())]),np.ones(1),2e-12)
 H=sum(a*C for a,C in zip(couplings,car[:3]));K=G@bs[success];energy=np.trace(K.conj().T@H@K).real/(16*probs[success]);expected=sum(eps/(1+np.exp(beta*eps)))
 ck('energy_'+tag,np.array([energy]),np.array([expected]),2e-11)
print(json.dumps({'status':'PASS','count':len(checks),'max_residual':max(res.values()),'checks':checks,'residuals':res,'method':'independent bit-action native matrices, CAR phase dictionary and exterior minors; all96 full branch operators compared','author_source_sha256':hashlib.sha256((src/'path_probe.py').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
