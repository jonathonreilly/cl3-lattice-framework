import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import numpy as np,itertools,json,time,signal,resource,sys
from scipy.linalg import expm,eigh
signal.alarm(180);start=time.monotonic();I=np.eye(64);z=np.diag([1,-1]);x=np.array([[0,1],[1,0]])
def site(a,j):
 r=np.array([[1.]])
 for k in range(6):r=np.kron(r,a if k==j else np.eye(2))
 return r
Z=[site(z,j) for j in range(6)];X=[site(x,j) for j in range(6)];edges=[(0,1),(0,2),(0,4),(0,6),(1,3),(1,5)];B=[]
for v in range(7):
 b=I.copy()
 for k,e in enumerate(edges):
  if v in e:b=b@Z[k]
 B.append(b)
N=[(I-b)/2 for b in B];T=[]
for k,(i,j) in enumerate(edges):
 a=X[k].copy()
 for l,e in enumerate(edges):
  if l==k:continue
  if (i in e and next(v for v in e if v!=i)<j) or (j in e and next(v for v in e if v!=j)<i):a=a@Z[l]
 T.append(1j*a@(B[i]-B[j])/2)
P=(I-N[2])@(I-N[3])@N[4]@N[5];inds=np.where(np.diag(P)>.5)[0];assert len(inds)==4
D=N[0]-N[1];R=expm(-1j*np.pi*D/4);J=R.conj().T@T[0]@R;beta=np.log(2);checks=[]
def ck(n,r):checks.append({'name':n,'residual':float(r)});assert np.isfinite(r) and r<1e-10,n
def pulse(t,r):return I+(r-1)*(t@t)-1j*np.sqrt(1-r*r)*t
records=[(1,2,False),(4,3,False),(2,4,True),(5,5,True)]
def run(s,full=False):
 h=np.array([[s,1.],[1.,-s]]);eps,O=eigh(h)
 if np.linalg.det(O)<0:O[:,0]*=-1
 theta=np.arctan2(O[0,1],O[0,0]);V=expm(-1j*theta*J);H=T[0]+s*D
 ck('diagonalization_'+str(s),np.linalg.norm(V@(eps[0]*N[0]+eps[1]*N[1])@V.conj().T-H))
 pulses=[pulse(T[e],np.exp(-beta*(2 if filled else 2+eps[mode])/2)) for (e,leaf,filled),mode in zip(records,[0,1,0,1])]
 K=V.conj().T@P;old=[]
 for (e,leaf,filled),u in zip(records,pulses):
  for r in old:ck('permanence',np.linalg.norm(u@Z[r]-Z[r]@u))
  Q=N[leaf] if filled else I-N[leaf];K=Q@u@K;old.append(e)
 K=V@K;target=.25*expm(-beta*H/2)@P;ck('full_K_'+str(s),np.linalg.norm(K-target))
 weight=np.trace(K.conj().T@K).real/4;Zpart=np.trace(P@expm(-beta*H)).real;ck('partition_'+str(s),abs(weight-Zpart/64))
 if full:
  effects=np.zeros((64,64),complex)
  for bits in itertools.product([0,1],repeat=4):
   A=V.conj().T@P
   for (_,leaf,_),u,b in zip(records,pulses,bits):A=(N[leaf] if b else I-N[leaf])@u@A
   A=V@A;effects+=A.conj().T@A
  ck('complete16_'+str(s),np.linalg.norm(effects-P))
  for e in old:ck('final_records',np.linalg.norm(V@Z[e]-Z[e]@V))
 return weight,float(np.trace(P@expm(-beta*H)@D).real/Zpart)
rows=[]
for s in [0.,.75,-.75]:
 p,m=run(s,True);rows.append({'s':s,'success':p,'meanD':m})
p,m=run(.75);der=[]
for step in [1e-4,5e-5]:
 pp,_=run(.75+step);pm,_=run(.75-step);der.append({'step':step,'derivative':(np.log(pp)-np.log(pm))/(2*step),'target':-beta*m})
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);assert 0<rss<384
print(json.dumps({'rows':rows,'derivatives':der,'checks':checks,'count':len(checks),'rss_mib':rss,'seconds':time.monotonic()-start},indent=2,allow_nan=False))
