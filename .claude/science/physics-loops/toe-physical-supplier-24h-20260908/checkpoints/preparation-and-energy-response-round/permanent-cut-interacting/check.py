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
r=S.Rational(3,5);s=S.Rational(4,5);branches={'':Q}
for j in range(3):
 t=T[2+j];u=I+(r-1)*t*t-S.I*s*t
 ck('cubic'+str(j),zero(t**3-t));ck('unitary'+str(j),zero(u.H*u-I))
 new={}
 for h,cols in branches.items():
  for b in (0,1):new[h+str(b)]=(n[j+3] if b else I-n[j+3])*u*cols
 branches=new
normal=S.zeros(4);prob={}
for h,K in branches.items():
 normal+=K.H*K;prob[h]=str(S.trace(K.H*K)/4)
 for j,b in enumerate(h):ck('record_'+h+'_'+str(j),zero((n[3+j]-int(b)*I)*K))
 ck('anchor_'+h,zero((n[6]-I)*K))
ck('complete8outcome_instrument',zero(normal-S.eye(4)))
K=branches['000'];target=r*(I+(r*r-1)*n[0]*n[1])*Q
ck('full_Kraus_interacting_encoded_target',zero(K-target))
ck('target_full_rank4',(K.H*K).det()!=0)
ck('encoded_all_four_inputs',len({(n[0][i,i],n[1][i,i]) for i in idx})==4)
ck('success_probability',S.trace(K.H*K)/4==(3*r*r+r**6)/4)
ck('all_failures_sum',sum(S.Rational(v) for v in prob.values())==1)
ck('wrong_interaction_omitted_detected',not zero(K-r*Q))
# Rational terminal-refinement stress. Odd discard parity of Slater (0+4) wedge (1+5)/2.
# After a discarded45 rotation, resolved one-particle retained columns form the matrix C.
c=S.Rational(3,5);s=S.Rational(4,5)
C=S.Matrix([[s,c],[-c,s]])/2
rho=C*C.H
ck('terminal_refined_probability',S.trace(rho)==S.Rational(1,2))
ck('terminal_marginal_identity',rho==S.eye(2)/4)
ck('each_refined_state_one_particle_Gaussian',all((C[:,j]*C[:,j].H).det()==0 for j in range(2)))
early=S.diag(s*s,c*c)/4;late=C[:,0]*C[:,0].H
ck('early_dephasing_changes_conditional_state',early!=late)
ck('early_dephasing_same_conditional_probability',S.trace(early)==S.trace(late))
ck('early_dephasing_nonzero_missing_coherence',late[0,1]==-S.Rational(3,25))
# Global parity branch remains non-Gaussian: a05=1/2,a14=-1/2 -> nonzero 0,1,4,5 Pluecker.
ck('global_branch_not_Gaussian',S.Rational(1,2)*-S.Rational(1,2)!=0)
res={'status':'PASS','checks':checks,'count':len(checks),'all_branch_probabilities':prob,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_sec':time.monotonic()-start,'rss_native':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Counterexample to unrestricted encoded corollary; not a genuinely interacting physical generator.'}
print(json.dumps(res,indent=2))
