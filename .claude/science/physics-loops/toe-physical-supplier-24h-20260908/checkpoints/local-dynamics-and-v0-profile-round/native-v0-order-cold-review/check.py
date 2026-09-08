from pathlib import Path
import importlib.util,itertools,json,hashlib
import numpy as np
p=Path('/private/tmp/toe-24h-probes-20260908/native-v0-order-design')
s=importlib.util.spec_from_file_location('reviewed',p/'observables.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
checks=0
def req(v):
 global checks
 checks+=1
 if not v:raise RuntimeError('independent literal check')
for L in (2,4,8):
 o=m.OrderMenu(L); N=L**3
 for case in range(4):
  x=np.array([((i*i+3*i+case*7)//(case+1))%2 for i in range(3*N)],dtype=int)
  z=o.measure(x)
  for k,b in enumerate(o.corners):
   for a in range(3):
    v=sum((-1)**sum((b[j]+1)*r[j] for j in range(3))*(2*x[3*((r[0]*L+r[1])*L+r[2])+a]-1) for r in itertools.product(range(L),repeat=3))/(2*N)
    req(abs(v-z['electric'][k,a])<1e-14)
   for j,(a,c) in enumerate(((0,1),(0,2),(1,2))):
    total=0
    for r in itertools.product(range(L),repeat=3):
     def bit(rr,d):return x[3*((rr[0]*L+rr[1])*L+rr[2])+d]
     ra=list(r);ra[a]=(ra[a]+1)%L;rc=list(r);rc[c]=(rc[c]+1)%L
     f=(bit(r,a)==bit(rc,a) and bit(ra,c)==bit(r,c) and bit(r,a)!=bit(r,c))
     total+=(-1)**sum(b[t]*r[t] for t in range(3))*f
    req(abs(total/N-z['flippability'][k,j])<1e-14)
  for key in ('electric','flippability'):
   req(np.array_equal(z[key+'_square'],z[key]**2));req(np.array_equal(z[key+'_fourth'],z[key]**4))
# Fixed cadence includes positions 0,...,T-1, including offset zero exactly once per period.
for M in (8,1536):
 T=768*M
 req(all(len(range(cid%M,T,M))==768 for cid in range(16)))
out={'checks':checks,'scope':'Independent deterministic literal formulas on non-sampled arbitrary bit fixtures; no ice ensemble or production','source_sha256':hashlib.sha256((p/'observables.py').read_bytes()).hexdigest()}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
