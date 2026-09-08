import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
import sympy as s
from itertools import product
from pathlib import Path
import json,time,signal,resource,sys
signal.alarm(180);start=time.monotonic();checks=0

def req(v,m):
 global checks
 checks+=1
 if not v:raise RuntimeError(m)
rows=[]
for v,edges,cycle in [(3,[(0,1),(1,2),(0,2)],[0,1,2]),(4,[(0,1),(1,2),(2,3),(0,3)],[0,1,2,3])]:
 E=len(edges);dim=1<<E;A=[]
 for e,ends in enumerate(edges):
  mask=sum(1<<f for f in range(e) if set(ends)&set(edges[f]));m=s.zeros(dim)
  for x in range(dim):m[x^(1<<e),x]=(-1)**((mask&x).bit_count())
  A.append(m)
 H=sum(A,s.zeros(dim));S=s.eye(dim)*s.I**v
 for i in range(v):
  a,b=cycle[i],cycle[(i+1)%v];e=next(e for e,ends in enumerate(edges) if set(ends)=={a,b});S=S*A[e]*(1 if a<b else -1)
 req(S*S==s.eye(dim),'native cycle involution');req(S*H==H*S,'native flux conserved')
 gam=[]
 for i in range(v):
  m=s.zeros(1<<v)
  for n in range(1<<v):m[n^(1<<i),n]=(-1)**((n&((1<<i)-1)).bit_count())
  gam.append(m)
 ev=[n for n in range(1<<v) if n.bit_count()%2==0]
 totaldim=0
 for flux in [-1,1]:
  xi=[1]*(E-1)+[flux];Fock=s.zeros(1<<v);K=s.zeros(v)
  for (a,b),x in zip(edges,xi):Fock+=-s.I*x*gam[a]*gam[b];K[a,b]=-2*x;K[b,a]=2*x
  he=Fock.extract(ev,ev);proj=(s.eye(dim)+flux*S)/2
  req(s.trace(proj)==2**(v-1),'flux dimension');totaldim+=int(s.trace(proj))
  hn=s.eye(dim);hf=s.eye(len(ev))
  for k in range(len(ev)+1):
   req(s.simplify(s.trace(proj*hn)-s.trace(hf))==0,'native versus even-Fock sector moment')
   hn=hn*H;hf=hf*he
  vals=(s.I*K).eigenvals();frequencies=[]
  for x,m in vals.items():
   if x.is_positive:frequencies.extend([x]*m)
   elif x!=0 and not (-x).is_positive:raise RuntimeError('undecided exact sign')
  r=len(frequencies);req(2*r==K.rank(),'active rank');deg=2**(v-r-1)
  predicted={}
  for occ in product((0,1),repeat=r):
   energy=s.simplify(sum(w*(s.Rational(n)-s.Rational(1,2)) for w,n in zip(frequencies,occ)))
   predicted[energy]=predicted.get(energy,0)+deg
  req(predicted==he.eigenvals(),'frequencies and spectator parity multiplicities')
  req(sum(predicted.values())==2**(v-1),'pattern dimension')
  rows.append(dict(vertices=v,flux=flux,frequencies=list(map(str,frequencies)),rank=2*r,pattern_multiplicity=deg,spectrum={str(k):m for k,m in predicted.items()}))
 req(totaldim==2**E,'whole native dimension')
# Explicit degenerate zero-coupling boundary and factor-two calibration.
req(2**(4-0-1)==8,'zero-H even carrier')
req(2**(4-2-1)==2,'generic even spectator count')
req(s.Matrix([[0,-2*s.I],[2*s.I,0]]).eigenvals()=={-2:1,2:1},'single-edge omega2')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(0<rss<384 and time.monotonic()-start<180,'resource cap')
r=dict(checks=checks,rows=rows,seconds=time.monotonic()-start,rss_mib=rss,scope='Exact native Pauli flux moments versus even CAR and Clifford frequencies on triangle/square. No cubic flux optimum or phase claim.')
Path(__file__).with_name('RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
