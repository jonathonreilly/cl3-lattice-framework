from pathlib import Path
from itertools import product
from fractions import Fraction as F
import json,time,signal,hashlib
import numpy as np
signal.alarm(180);start=time.monotonic();checks=0
def need(c,s):
 global checks
 checks+=1
 if not c:raise RuntimeError(s)
vs=list(product(range(4),repeat=3));ix={v:i for i,v in enumerate(vs)};edges=[];signs=[]
for v in vs:
 for a in range(3):
  q=list(v);q[a]=(q[a]+1)%4;i,j=sorted((ix[v],ix[tuple(q)]));edges.append((i,j));signs.append((-1)**sum(v[:a]))
black=[i for i,v in enumerate(vs) if sum(v)%2==0];white=[i for i in range(64) if i not in black];bi={v:i for i,v in enumerate(black)};wi={v:i for i,v in enumerate(white)}
def certificate(mask):
 B=np.zeros((32,32),dtype=np.int64)
 for e,((i,j),s) in enumerate(zip(edges,signs)):
  s*=(-1 if mask>>e&1 else 1)
  if i in bi:B[bi[i],wi[j]]=-s
  else:B[bi[j],wi[i]]=s
 E=B@B.T-6*np.eye(32,dtype=np.int64)
 need(int(np.max(abs(E)))<=6,'entry bound')
 need(192*30**9<2**63,'int64 multiplication safe')
 P=np.eye(32,dtype=np.int64);tr=[]
 for k in range(1,11):P=P@E;tr.append(int(np.trace(P)))
 c=[1]
 for k in range(1,11):
  num=sum((-1)**(j-1)*c[k-j]*tr[j-1] for j in range(1,k+1));need(num%k==0,'Newton integrality');c.append(num//k)
 s=F(49,4);q=sum(F(c[k])*s**(10-k) for k in range(11));qp=sum(F(c[k])*(10-k)*s**(9-k) for k in range(10));need(q>0,'positive shifted determinant')
 ti=22/s+qp/q;c0=F(5,2);upper=(192+32*c0*c0)/(4*c0)+c0*(32-c0*c0*ti);gap=32*F(2449489742783178,10**15)-upper
 return {'mask_hex':hex(mask),'trace_coefficients':c,'trace_sqrt_upper':str(upper),'gap_lower':str(gap)}
a=Path('/private/tmp/toe-24h-probes-20260908/native-sixth-spectator-gap-certificates');source=json.loads((a/'RESULT.json').read_text());rows=[]
for r in source['rows']:
 if 'trace_sqrt_upper' not in r:continue
 z=certificate(int(r['mask_hex'],16));need(z['trace_sqrt_upper']==r['trace_sqrt_upper'] and z['gap_lower']==r['gap_lower'],'independent inverse-trace equality');rows.append(z)
z=certificate(int(source['unrestricted_star']['mask_hex'],16));need(z['gap_lower']==source['unrestricted_star']['gap_lower'],'same parity caveat');rows.append(z)
print(json.dumps({'checks':checks,'PASS':True,'rows':rows,'seconds':time.monotonic()-start,'scope':'exact rank-ten trace method on existing five fixtures; no full prefix scan','comparison_source_sha256':hashlib.sha256((a/'RESULT.json').read_bytes()).hexdigest()},indent=2))
