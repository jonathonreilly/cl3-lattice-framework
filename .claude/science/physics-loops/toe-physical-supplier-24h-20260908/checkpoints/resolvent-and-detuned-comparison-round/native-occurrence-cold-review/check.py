import os,time,signal,resource,sys,json,hashlib
from pathlib import Path
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
start=time.monotonic();signal.alarm(180)
import numpy as np
from scipy.sparse import coo_matrix,diags,eye
p=Path(__file__).resolve().parent;checks={}
def ck(n,a):
 if not bool(a):raise AssertionError(n)
 checks[n]=True
def close(a,b):return np.max(abs(np.asarray(a)-np.asarray(b)))<1e-11
edges=[(0,1),(1,2),(2,3),(0,4),(1,5),(2,6),(3,7),(3,8)];size=256;indices=np.arange(size);I=eye(size,format='csr',dtype=complex)
Z=np.array([1-2*((indices>>(7-k))&1) for k in range(8)]);B=np.array([np.prod(Z[[k for k,e in enumerate(edges) if v in e]],axis=0) for v in range(9)]);n=(1-B)//2;T=[]
for k,(i,j) in enumerate(edges):
 sign=np.ones(size)
 for v,w in ((i,j),(j,i)):
  for q,e in enumerate(edges):
   if q!=k and v in e and (e[1] if e[0]==v else e[0])<w:sign*=Z[q]
 amp=1j*sign*(B[i]-B[j])/2
 T.append(coo_matrix((amp,(indices^(1<<(7-k)),indices)),shape=(size,size)).tocsr())
def pulse(k,c,s):return I+(c-1)*(T[k]@T[k])-1j*s*T[k]
ready=np.flatnonzero(np.all(n[[2,3,4,5,6,7]]==0,axis=0));ready=sorted(ready,key=lambda j:2*n[0,j]+n[1,j]);V=np.eye(size)[:,ready];ck('ready_four',len(ready)==4);ck('correlated_reservoir',all(n[8,j]==(n[0,j]+n[1,j])%2 for j in ready))
smallT=V.conj().T@(T[0]@V);N0=V.conj().T@(n[0,:,None]*V);N1=V.conj().T@(n[1,:,None]*V);W=pulse(0,4/5,3/5);w=V.conj().T@(W@V)
D=pulse(4,5/13,12/13)@pulse(3,3/5,4/5);U=pulse(1,0,1)@pulse(2,0,1)@pulse(0,0,1)@pulse(1,0,1);R=U@V
ck('transport_full_isometry',close(R.conj().T@R,np.eye(4)));ck('transport_wait',close(T[2]@R,R@smallT))
d=np.diag([(3/5)**n[0,j]*(5/13)**n[1,j] for j in ready]);C=d@w;ck('noncommuting_continuation',np.linalg.norm(d@w-w@d)>1e-3)
D2=pulse(6,5/13,12/13)@pulse(5,3/5,4/5);W2=pulse(2,4/5,3/5);branches={};effects={};total=np.zeros((4,4),complex)
for a in (0,1):
 for b in (0,1):
  mask=(n[4]==a)&(n[5]==b);K=U@(mask[:,None]*(D@(W@V)));branches[a,b]=K;effects[a,b]=K.conj().T@K
  ck(f'old_records_{a}{b}',close(Z[3,:,None]*K,(-1)**a*K) and close(Z[4,:,None]*K,(-1)**b*K))
  ck(f'cut_{a}{b}',close(Z[0,:,None]*K,(-1)**a*K) and close(Z[1,:,None]*K,(-1)**(a+b)*K))
  ck(f'vacancy_{a}{b}',close(n[0,:,None]*K,0*K) and close(n[1,:,None]*K,0*K))
  for c in (0,1):
   for e in (0,1):
    mask2=(n[6]==c)&(n[7]==e);F=mask2[:,None]*(D2@(W2@K));total+=F.conj().T@F
    ck(f'fullhistory_records_{a}{b}{c}{e}',close(Z[3,:,None]*F,(-1)**a*F) and close(Z[4,:,None]*F,(-1)**b*F) and close(Z[5,:,None]*F,(-1)**c*F) and close(Z[6,:,None]*F,(-1)**e*F))

for (a,b),eff in effects.items():
 vals=[]
 for j in ready:
  va=((1-(3/5)**2)*n[0,j]) if a else (3/5)**(2*n[0,j])
  vb=((1-(5/13)**2)*n[1,j]) if b else (5/13)**(2*n[1,j])
  vals.append(va*vb)
 ck(f'independent_effect_{a}{b}',close(eff,w.conj().T@np.diag(vals)@w))
ck('full16_completeness',close(total,np.eye(4)));ck('first00_fullcolumns',close(branches[0,0],R@C))
first=sum((effects[k] for k in effects if k!=(0,0)),np.zeros((4,4),complex));eventsum=first.copy();second={}
for a in (0,1):
 for b in (0,1):
  mask=(n[6]==a)&(n[7]==b);K=mask[:,None]*(D2@(W2@branches[0,0]));E=K.conj().T@K;ck(f'second_effect_{a}{b}',close(E,C.conj().T@effects[a,b]@C));second[a,b]=E
  if (a,b)!=(0,0):eventsum+=E
  else:ck('censor_fullcolumns',close(K,R@C@C));eventsum+=E
ck('first_positive_complete',close(eventsum,np.eye(4)))
plus=np.array([0,1,1,0])/np.sqrt(2);minus=np.array([0,1,-1,0])/np.sqrt(2);probs=[float((v.conj()@first@v).real) for v in (plus,minus)];ck('coherent_input_dependence',abs(probs[0]-probs[1])>1e-3)
# Actual adverse: dropping the waiting pulse changes a full first-positive effect.
ck('removed_wait_adverse',not close(first,np.eye(4)-d@d));ck('wrong_cumulative_cut_adverse',not close(Z[1,:,None]*branches[1,0],branches[1,0]))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);ck('resources',0<rss<384 and time.monotonic()-start<180)
out={'checks':checks,'count':len(checks),'first_positive_probabilities_coherent_pair':probs,'C_real':C.real.tolist(),'C_imag':C.imag.tolist(),'ready_indices':list(map(int,ready)),'seconds':time.monotonic()-start,'rss_mib':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};(p/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
