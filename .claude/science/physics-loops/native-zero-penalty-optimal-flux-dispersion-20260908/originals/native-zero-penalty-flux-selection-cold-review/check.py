from itertools import product
from collections import Counter
from pathlib import Path
import json,hashlib
checks=0
def need(x):
 global checks
 checks+=1
 if not x:raise RuntimeError(checks)
# Direct occupation enumeration: active Majorana pairs and spectator pairs,
# imposing even TOTAL parity once. Energy unit is half a frequency.
for n in (2,4,6,8):
 for r in range(n//2+1):
  w=list(range(1,r+1))
  native=Counter()
  for occ in product((0,1),repeat=n):
   if sum(occ)%2==0:native[sum((2*occ[j]-1)*w[j] for j in range(r))]+=1
  aux=Counter()
  energies=w+[-x for x in w]+[0]*(n-2*r)
  fixed=Counter()
  for occ in product((0,1),repeat=n):
   e=2*sum(x*y for x,y in zip(occ,energies));aux[e]+=1
   if sum(occ)==n//2:fixed[e]+=1
  sq=Counter()
  for a,m in native.items():
   for b,k in native.items():sq[a+b]+=m*k
  need(sq==Counter({e:2**(n-2)*m for e,m in aux.items()}))
  need(min(aux)==2*min(native));need(min(fixed)==min(aux))
  need(sum(fixed.values())!=sum(aux.values()))
# Reflections: explicitly check each crossing edge joins a reflected pair;
# this also licenses the paper's independent cross-plane gauge step.
for dims in ((4,6,4),(6,4,8)):
 vertices=list(product(*map(range,dims)))
 def nxt(v,a):return tuple((v[b]+(b==a))%dims[b] for b in range(3))
 for axis in range(3):
  for s in range(dims[axis]):
   def refl(v):return tuple((2*s+1-v[b])%dims[b] if b==axis else v[b] for b in range(3))
   def left(v):return (v[axis]-s-1)%dims[axis]<dims[axis]//2
   for v in vertices:
    crossing=[nxt(v,a) for a in range(3) if left(v)!=left(nxt(v,a))]
    need(len(crossing)<=1)
    for q in crossing:need(q==refl(v))
# Source pin verification, not a theorem test.
a=Path('/private/tmp/toe-24h-probes-20260908/native-zero-penalty-flux-selection-root')
f=json.loads((a/'FINAL_FREEZE.json').read_text())
for p,h in f.items():need(hashlib.sha256((a/p).read_bytes()).hexdigest()==h)
print(json.dumps({'checks':checks,'status':'PASS','scope':'Independent occupation enumeration, cross-plane matching, frozen source pins; no numerical flux optimization'},indent=2))
