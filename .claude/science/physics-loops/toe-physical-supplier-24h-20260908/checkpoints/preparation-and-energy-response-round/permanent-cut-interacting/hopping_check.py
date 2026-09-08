import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import sympy as S
from functools import reduce
from itertools import product
import json,time,hashlib,resource
from pathlib import Path
start=time.monotonic();checks={}
def ck(k,p):
 if not bool(p):raise AssertionError(k)
 checks[k]=True
def zero(x):return x==S.zeros(*x.shape)
vertices=[(0,0,0),(1,0,0),(2,0,0),(0,1,0),(1,1,0),(2,1,0),(0,0,1)]
edges=[(0,1),(1,2),(0,3),(1,4),(2,5),(0,6)]
I=S.eye(64);x=S.Matrix([[0,1],[1,0]]);z=S.diag(1,-1)
def site(a,k):return S.kronecker_product(*[a if j==k else S.eye(2) for j in range(6)])
Z=[site(z,k) for k in range(6)];X=[site(x,k) for k in range(6)]
B=[reduce(lambda a,b:a*b,[Z[k] for k,e in enumerate(edges) if v in e],I) for v in range(7)];n=[(I-b)/2 for b in B]
T=[]
for k,(a,b) in enumerate(edges):
 A=X[k]
 for u,v in [(a,b),(b,a)]:
  for q,e in enumerate(edges):
   if q!=k and u in e and (e[1] if e[0]==u else e[0])<v:A=A*Z[q]
 T.append(S.I*A*(B[a]-B[b])/2)
P=(I-n[3])*(I-n[4])*(I-n[5])*n[6]
idx=[j for j in range(64) if P[j,j]==1];Q=I[:,idx]
ck('ready_rank4',len(idx)==4)
ck('odd_active_parity',zero((B[0]*B[1]*B[2]+I)*Q))
ck('quadratic_identity_on_code',zero((n[0]*n[1]-(n[0]+n[1]+n[2]-I)/2)*Q))
ck('identity_NOT_ambient',not zero(n[0]*n[1]-(n[0]+n[1]+n[2]-I)/2))
ck('actual_virtual_NN',all(sum(abs(vertices[a][j]-vertices[b][j]) for j in range(3))==1 for a,b in edges))
ck('six_distinct_physical_centers',len({tuple(vertices[a][j]+vertices[b][j] for j in range(3)) for a,b in edges})==6)

r=S.Rational(3,5);t=T[0];D=n[0]-n[1];c=S.sqrt(2)/2
U=I+(c-1)*t*t-S.I*c*t
R=I+(c-1)*D*D-S.I*c*D
W=S.simplify(R*U)
ck('W_unitary',zero(S.simplify(W.H*W-I)))
ck('W_D_to_T',zero(S.simplify(W*D*W.H-t)))
H=t+2*n[0]*n[1]
ck('physical_quadratic_only_on_ready',zero((H-(t+n[0]+n[1]+n[2]-I))*Q))
branches={'':S.simplify(W.H*Q)}
for j,rr in enumerate((r*r,S.Integer(1),r)):
 tt=T[2+j];u=I+(rr-1)*tt*tt-S.I*S.sqrt(1-rr*rr)*tt
 ck('leaf_unitary'+str(j),zero(S.simplify(u.H*u-I)))
 new={}
 for h,cols in branches.items():
  for b in (0,1):new[h+str(b)]=S.simplify((n[j+3] if b else I-n[j+3])*u*cols)
 branches=new
branches={h:S.simplify(W*K) for h,K in branches.items()}
normal=S.zeros(4);prob={}
for h,K in branches.items():
 normal+=K.H*K;prob[h]=str(S.simplify(S.trace(K.H*K)/4))
 for j,b in enumerate(h):ck('record_'+h+'_'+str(j),zero(S.simplify((n[3+j]-int(b)*I)*K)))
 ck('anchor_'+h,zero(S.simplify((n[6]-I)*K)))
ck('complete8outcomes',zero(S.simplify(normal-S.eye(4))))
pm=(t*t-t)/2;pp=(t*t+t)/2;pz=I-t*t
F=pm+r*r*pp+r*pz+(r**3-r)*n[0]*n[1]
K=branches['000'];ck('full_success_spectral_target',zero(S.simplify(K-F*Q)))
ck('full_ready_rank',S.simplify((K.H*K).det())!=0)
ck('success_retains_encoding',zero(S.simplify((B[0]*B[1]*B[2]+I)*K)))
weight=S.simplify(S.trace(K.H*K)/4)
ck('probability_spectral',weight==(1+r*r+r**4+r**6)/4)
energy=S.simplify(S.trace(K.H*H*K)/(4*weight))
kinetic=S.simplify(S.trace(K.H*t*K)/(4*weight))
ck('hopping_not_zero',kinetic!=0)
ck('omitting_interaction_detected',not zero(S.simplify(K-(pm+r*r*pp+r*pz)*Q)))
res={'status':'PASS','checks':checks,'count':len(checks),'probabilities':prob,'success_probability':str(weight),'conditional_H':str(energy),'conditional_T':str(kinetic),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_sec':time.monotonic()-start}
print(json.dumps(res,indent=2))
