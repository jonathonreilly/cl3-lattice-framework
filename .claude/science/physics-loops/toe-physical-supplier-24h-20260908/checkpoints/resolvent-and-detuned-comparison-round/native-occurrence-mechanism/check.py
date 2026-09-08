import os,time
start=time.monotonic()
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import numpy as np,json,hashlib,resource,sys
from pathlib import Path
from functools import reduce
edges=[(0,1),(1,2),(2,3),(0,4),(1,5),(3,6)];I=np.eye(64,dtype=complex);z=np.diag([1,-1]);x=np.array([[0,1],[1,0]])
def site(a,k):return reduce(np.kron,[a if j==k else np.eye(2) for j in range(6)])
Z=[site(z,k) for k in range(6)];X=[site(x,k) for k in range(6)];B=[reduce(np.matmul,[Z[k] for k,e in enumerate(edges) if v in e],I) for v in range(7)];n=[(I-b)/2 for b in B];T=[]
for k,(i,j) in enumerate(edges):
 a=X[k].copy()
 for v,w in [(i,j),(j,i)]:
  for q,e in enumerate(edges):
   if v in e and q!=k:
    other=e[1] if e[0]==v else e[0]
    if other<w:a=a@Z[q]
 T.append(1j*a@(B[i]-B[j])/2)
def pulse(k,c,s):return I+(c-1)*(T[k]@T[k])-1j*s*T[k]
P=reduce(np.matmul,[I-n[v] for v in [2,3,4,5]],I);checks={}
def ck(k,v):
 if not bool(v):raise AssertionError(k)
 checks[k]=True
def zero(a):return np.max(abs(a))<1e-11
ck('ready_rank4',abs(np.trace(P)-4)<1e-12)
ck('evenparity',zero(reduce(np.matmul,B,I)-I))
for k in range(6):ck(f'nativehop{k}',zero(T[k]-T[k].conj().T) and zero(T[k]@T[k]@T[k]-T[k]))
D=pulse(4,5/13,12/13)@pulse(3,3/5,4/5);U=pulse(1,0,1)@pulse(2,0,1)@pulse(0,0,1)@pulse(1,0,1)
ck('transportunitary',zero(U.conj().T@U-I));ck('oldleafrecordscommute',zero(U@Z[3]-Z[3]@U) and zero(U@Z[4]-Z[4]@U))
normal=I*0;rows=[]
for a in [0,1]:
 for b in [0,1]:
  Q=(n[4] if a else I-n[4])@(n[5] if b else I-n[5]);M=Q@D@P;K=U@M;normal+=K.conj().T@K
  ck(f'vacancy{a}{b}',zero(n[0]@K) and zero(n[1]@K))
  ck(f'deterministiccuts{a}{b}',zero(Z[0]@K-(-1)**a*K) and zero(Z[1]@K-(-1)**(a+b)*K))
  ck(f'numbertransport{a}{b}',zero(K.conj().T@n[2]@K-M.conj().T@n[0]@M) and zero(K.conj().T@n[3]@K-M.conj().T@n[1]@M))
  ck(f'coherenttransport{a}{b}',zero(K.conj().T@T[2]@K-M.conj().T@T[0]@M))
  rows.append(dict(outcome=[a,b],probability_mixed_ready=float(np.trace(K.conj().T@K).real/4)))
ck('completeallbranches',zero(normal-P))
# no-positive-click survival effect, all-input not just diagonal test.
M=(I-n[4])@(I-n[5])@D@P;C=(I+(3/5-1)*n[0])@(I+(5/13-1)*n[1]);ck('noclickfulloperator',zero(M-C@P))
# No detector reuse: their own hopping fails Record commutation.
ck('reuseforbiddenoperator',not zero(T[3]@Z[3]-Z[3]@T[3]))
finite=[]
for N in [1,4,16,64]:
 survival=np.cos(1/N)**(2*N);weak=np.cos(np.sqrt(1/N))**(2*N);finite.append(dict(N=N,fixed_strength_survival=float(survival),weakscaled_survival=float(weak),leaves_consumed=2*N))
print(json.dumps(dict(checks=checks,count=len(checks),branches=rows,limits=finite,seconds=time.monotonic()-start,rss_native=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2))
