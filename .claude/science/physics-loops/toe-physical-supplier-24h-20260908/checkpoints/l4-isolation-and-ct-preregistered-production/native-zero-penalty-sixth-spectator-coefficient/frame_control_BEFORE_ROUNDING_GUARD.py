from fractions import Fraction as F
from itertools import product,combinations
import json,math,time,signal
import numpy as np
signal.alarm(180);start=time.monotonic();count=0
def need(c,s):
 global count
 count+=1
 if not c:raise RuntimeError(s)
vs=list(product(range(4),repeat=3));ix={v:i for i,v in enumerate(vs)};N=64
K=[[0]*N for _ in range(N)];edges=[]
for v in vs:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%4;w=tuple(w);i,j=sorted((ix[v],ix[w]));edges.append((i,j));K[i][j]=-2*(-1)**sum(v[:a]);K[j][i]=-K[i][j]
v,w=edges[0];inc=[set() for _ in vs]
for e,(i,j) in enumerate(edges):inc[i].add(e);inc[j].add(e)
cut=inc[v]^inc[w];S=sorted({i for e in cut for i in edges[e]});black=[i for i,v in enumerate(vs) if sum(v)%2==0]
raw=[];norm=[]
for s in S:
 c=[F(i==s) if s in black else F(K[i][s]) for i in black]
 for b,d in zip(raw,norm):
  q=sum(x*y for x,y in zip(c,b))/d;c=[x-q*y for x,y in zip(c,b)]
 d=sum(x*x for x in c)
 if d:raw.append(c);norm.append(d)
need(len(raw)==10,'black dimension')
for i,b in enumerate(raw):
 for j,c in enumerate(raw):need(sum(x*y for x,y in zip(b,c))==(norm[i] if i==j else 0),'rational Gram')
B=np.zeros((64,10));kf=np.array(K,dtype=float)
for j,b in enumerate(raw):B[black,j]=[float(x)/math.sqrt(float(norm[j])) for x in b]
C=-kf@B/math.sqrt(24);Q=np.column_stack((B,C))
need(np.max(abs(Q.T@Q-np.eye(20)))<2e-15,'numerical frame control only')
need(np.max(abs(B.T@kf@C-math.sqrt(24)*np.eye(10)))<3e-15,'vacuum sign')
states=np.array([x for x in range(1024) if x.bit_count()%2==0]);index={int(b):i for i,b in enumerate(states)}
def fock(M):
 h=np.diag([sum(M[i,i]*(((int(b)>>i)&1)-.5) for i in range(10)) for b in states])
 for i,j in combinations(range(10),2):
  for col,b in enumerate(states):
   b=int(b);sgn=(-1)**((b&((1<<i)-1)).bit_count()+(b&((1<<j)-1)).bit_count())
   a=.5*sgn*(M[j,i]*(1-2*((b>>i)&1))-M[i,j]*(1-2*((b>>j)&1)))
   h[index[b^(1<<i)^(1<<j)],col]+=a
 return h
H=fock(B.T@kf@C)
need(np.max(abs(H-np.diag([math.sqrt(24)*(int(b).bit_count()-5) for b in states])))<2e-14,'empty active vacuum')
# Compare complete bilinear columns against literal JW Majorana action,
# independently of the paired-coefficient formula above.
def ma(b,i,is_b):
 s=(-1)**((b&((1<<i)-1)).bit_count())
 if is_b:s*=1j*(1-2*((b>>i)&1))
 return b^(1<<i),s
for i,j in ((0,0),(0,1),(1,0),(4,9),(9,4)):
 M=np.zeros((10,10));M[i,j]=2;H=fock(M)
 for col,b in enumerate(states):
  q,z=ma(int(b),j,True);q,y=ma(q,i,False);z*=1j*y
  need(H[index[q],col]==z and np.count_nonzero(H[:,col])==1,'literal i a_i b_j')
# One perturbed real quadratic matrix, all columns symmetric.
e=0;i,j=edges[e];k2=kf.copy();k2[i,j]*=-1;k2[j,i]*=-1;H=fock(B.T@k2@C)
need(np.max(abs(H-H.T))<1e-14,'perturbed Hermiticity')
print(json.dumps({'checks':count,'PASS':True,'raw_black_basis':[[str(x) for x in b] for b in raw],'norms':list(map(str,norm)),'seconds':time.monotonic()-start,'scope':'exact rational frame plus floating matrix controls; no resolvent or coefficient certification'},indent=2))
