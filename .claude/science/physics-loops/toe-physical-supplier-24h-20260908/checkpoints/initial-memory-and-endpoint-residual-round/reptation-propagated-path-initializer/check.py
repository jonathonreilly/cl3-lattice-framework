import os,time,signal,resource,json,sys
for v in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[v]='1'
start=time.monotonic();signal.alarm(180)
import numpy as np
from core import geometry,legal,count
from initialize import initialize
from itertools import product
from fractions import Fraction as F
from pathlib import Path
p=Path(__file__).resolve().parent;checks=0

def req(c):
 global checks
 checks+=1
 if not c:raise RuntimeError('initializer check')
def invariants(x,L):
 rs=list(product(range(L),repeat=3));ix={(r,a):3*i+a for i,r in enumerate(rs) for a in range(3)}
 for r in rs:
  deg=0
  for a in range(3):
   rm=list(r);rm[a]=(rm[a]-1)%L;deg+=int(x[ix[r,a]])+int(x[ix[tuple(rm),a]])
  req(deg==3)
 flux=[]
 for a in range(3):
  flux.append([sum((-1)**sum(r)*(2*int(x[ix[r,a]])-1) for r in rs if r[a]==k) for k in range(L)])
 return flux
rows=[]
for L,n,seed in ((2,20,812911),(4,96,812912)):
 a,info=initialize(L,n,np.random.default_rng(seed));x=a.states[0].copy();fl=invariants(x,L);req(np.all((x==0)|(x==1)))
 for j,label in enumerate(a.labels):
  if label>=0:req(legal(x,a.faces[label]));x[a.faces[label]]^=1
  req(invariants(x,L)==fl)
  if j+1 in (n//2,n):
   k=1 if j+1==n//2 else 2;req(np.array_equal(x,a.states[k]));req(a.nf[k]==count(x,a.faces));req(np.max(abs(a.O[k]-a.coeff@(x.astype(float)-.5)))<1e-10)
 rows.append(dict(L=L,n=n,info=info))
# Exact n2 all-start comparison uses current graph labels, including duplicate geometric moves.
faces,coef,seed=geometry(2);toint=lambda x:sum(int(v)<<j for j,v in enumerate(x));states=[toint(seed)];ids={states[0]:0};adj=[]
for b in states:
 x=np.array([(b>>j)&1 for j in range(24)],np.uint8);ys=[]
 for f in faces:
  if legal(x,f):
   y=b^sum(1<<int(e) for e in f)
   if y not in ids:ids[y]=len(states);states.append(y)
   ys.append(ids[y])
 adj.append(ys)
req(len(states)==864);nf=list(map(len,adj));G=[]
for i,ys in enumerate(adj):
 row={i:F(1)-F(19*nf[i],480)}
 for j in ys:row[j]=row.get(j,F(0))+F(1,24)
 G.append(row)
b=[sum(row.values()) for row in G];Z=sum(v*v for v in b);tv=F(0);qsum=gsum=F(0)
for i,row in enumerate(G):
 for j,g in row.items():
  for k,gg in G[j].items():
   q=g*gg/(864*b[i]*b[j]);pi=g*gg/Z;qsum+=q;gsum+=pi;tv+=abs(q-pi)/2
req(qsum==gsum==1);req(tv>0)
import hashlib
result=dict(checks=checks,fixtures=rows,exact_uniformstart_n2_Q_vs_pi_TV=str(tv),seconds=time.monotonic()-start,sha256={n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ('core.py','initialize.py','check.py','PREREGISTRATION.md')})
(p/'CHECK_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
