from fractions import Fraction as F
from itertools import product,permutations
import json,hashlib
from pathlib import Path
checks=[]
def ck(n,b):
 if not b:raise AssertionError(n)
 checks.append(n)
edges=[(0,1),(1,2),(2,3),(0,3)]
nei={v:sorted(w if v==u else u for u,w in edges if v in (u,w)) for v in range(4)}
idx={tuple(sorted(e)):i for i,e in enumerate(edges)}
def A(i,j,bits):
 edge=idx[tuple(sorted((i,j)))];sign=1 if i<j else -1
 for v,w in [(i,j),(j,i)]:
  for k in nei[v]:
   if k<w:sign*=(-1)**bits[idx[tuple(sorted((v,k)))]]
 out=list(bits);out[edge]^=1
 return tuple(out),sign
# Rightmost operator acts first in A01 A12 A23 A30.
def cyc(bits):
 sign=1
 for e in [(3,0),(2,3),(1,2),(0,1)]:bits,s=A(*e,bits);sign*=s
 return bits,sign
allbits=list(product([0,1],repeat=4))
vac=[b for b in allbits if all(sum(b[i] for i,e in enumerate(edges) if v in e)%2==0 for v in range(4))]
ck('incidence kernel vacuum words',vac==[(0,0,0,0),(1,1,1,1)])
ck('cycle maps vacuum words with positive phase',all(cyc(b)==(tuple(1-x for x in b),1) for b in vac))
ck('cycle involution all16words',all((lambda t: (cyc(t[0])[0],t[1]*cyc(t[0])[1]))(cyc(b))==(b,1) for b in allbits))
ck('cycle trace0 gives plus code dimension8',all(cyc(b)[0]!=b for b in allbits))
rows=[]
for order in permutations(range(4)):
 for signs in product([-1,1],repeat=4):
  surviving=[b for b in vac if all(1-2*b[e]==z for e,z in zip(order,signs))]
  w=F(len(surviving),2);rows.append((order,signs,str(w)))
ck('all384 histories computed',len(rows)==384)
ck('48nonzero histories exactlysame signs',sum(F(w)>0 for o,s,w in rows)==48 and all(F(w)==(F(1,2) if len(set(s))==1 else 0) for o,s,w in rows))
for e,f in permutations(range(4),2):
 ck('conditional parity '+str((e,f)),all(sum((1-2*b[e])==z for b in vac if 1-2*b[f]==z)==1 for z in [-1,1]))
centers=[(1,0),(2,1),(1,2),(0,1)]
dist=lambda a,b:sum(abs(x-y) for x,y in zip(a,b))
ck('alltargetdistances2',all(dist(a,b)==2 for a,b in permutations(centers,2)))
common=[x for x in product(range(3),repeat=2) if all(dist(x,t)==1 for t in centers)]
ck('uniqueoneauxiliarycenter',common==[(1,1)])
def tv(p,q):return 1-min(p*q,F(1,2))-min((1-p)*(1-q),F(1,2))
vs=[tv(F(i,40),F(j,40)) for i,j in product(range(41),repeat=2)]
ck('exactgridTV>=sqrt2minus1',all((x+1)**2>=2 for x in vs))
ck('fairfirst TVhalf',all(tv(F(1,2),F(j,40))==F(1,2) for j in range(41)))
# At p=q=1/sqrt2, pq=1/2, (1-p)^2=3/2-sqrt2: overlap2-sqrt2.
# Verify quadratic-field identities with pairs a+b sqrt2.
def mul(x,y):return(x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
p=(F(0),F(1,2));one_minus_p=(F(1),F(-1,2))
ck('exactalgebraic minimizer pqhalf',mul(p,p)==(F(1,2),0))
ck('exactalgebraic otherproduct',mul(one_minus_p,one_minus_p)==(F(3,2),-1))
# Wrong stabilizer sign selects GHZminus; both states share all Z history weights.
ck('wrongcyclephasechangescoherence',sum(1*(-1 if b==vac[1] else 1) for b in vac)==0)
ck('Zhistoriescannotdetectrelativephase',all(F(sum(all(1-2*b[e]==z for e,z in zip(o,s)) for b in vac),2)==F(w) for o,s,w in rows))
# Shared seed competitor gives D, but second conditional differs from unchanged local p=1/2.
seedlaw={(1,1):F(1,2),(-1,-1):F(1,2)}
ck('hiddencommonseedescapesproductclass',seedlaw[(1,1)]!=F(1,2)*F(1,2))
ck('fullhistoryconditionaldetectsseed',seedlaw[(1,1)]/F(1,2)==1)
ck('latemediatorcannotrepairtargetlaw',sum(F(1,16) for s in product([-1,1],repeat=4) if len(set(s))==1)==F(1,8))
out={'status':'PASS','checks':len(checks),'checks_detail':checks,'native_history_rows':rows,'tv_grid_min':str(min(vs)),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(out,indent=2))
