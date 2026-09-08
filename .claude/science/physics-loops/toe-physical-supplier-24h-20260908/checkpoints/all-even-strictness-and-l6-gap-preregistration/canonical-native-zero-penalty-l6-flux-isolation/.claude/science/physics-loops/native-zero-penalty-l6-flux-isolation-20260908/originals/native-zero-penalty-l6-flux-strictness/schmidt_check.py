from itertools import product
from pathlib import Path
import numpy as np,json,signal,time,resource
signal.alarm(180);start=time.monotonic();p=97;V=list(product(range(6),repeat=3));ix={v:i for i,v in enumerate(V)};K=np.zeros((216,216),dtype=np.int64)
for x in V:
 for a in range(3):
  y=list(x);y[a]=(y[a]+1)%6;i,j=sorted((ix[x],ix[tuple(y)]));K[i,j]=-2*(-1)**sum(x[:a]);K[j,i]=-K[i,j]
I=np.eye(216,dtype=np.int64);A=(-K@K)%p
# exact algebraic spectrum certificate polynomial
R=I.copy()
for q in (12,24,36,48):R=R@((A-q*I)%p)%p
if np.any(R):raise ValueError('spectrum polynomial modular')
# square roots 2sqrt3,2sqrt6,6,4sqrt3 under fixed reduction
xs=[12,24,36,48];ys=[pow(z,-1,p) for z in (20,2*14*10%p,6,40)]
F=np.zeros_like(A)
for j,x in enumerate(xs):
 R=I.copy();den=1
 for y in xs:
  if y!=x:R=R@((A-y*I)%p)%p;den=den*(x-y)%p
 F=(F+R*(ys[j]*pow(den,-1,p)%p))%p
S=K@F%p;L=[i for i,v in enumerate(V) if v[0]<3];R=[i for i,v in enumerate(V) if v[0]>=3];B=S[np.ix_(L,R)].copy();det=1
for j in range(108):
 pivot=next((i for i in range(j,108) if B[i,j]),None)
 if pivot is None:raise ValueError('rank deficient modular certificate')
 if pivot!=j:B[[j,pivot]]=B[[pivot,j]];det=-det
 q=int(B[j,j]);det=det*q%p;B[j]=B[j]*pow(q,-1,p)%p
 for i in range(j+1,108):B[i]=(B[i]-B[i,j]*B[j])%p
Path(__file__).with_name('SCHMIDT_RESULT.json').write_text(json.dumps(dict(prime=p,sqrt2=14,sqrt3=10,rank=108,det_mod_prime=int(det),seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576),indent=2)+'\n')
