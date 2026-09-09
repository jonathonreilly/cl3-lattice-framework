"""Exact five-qubit preparation/history discriminator, not a physical run."""
from fractions import Fraction as F
from itertools import product
import json
A=(0,2,4);B=(1,3);N={1:(0,2),3:(2,4)}
c,s=F(3,5),F(4,5)
def rot(k):
 x,y=F(1),F(0)
 for _ in range(k):x,y=c*x-s*y,s*x+c*y
 return x,y
# Unnormalized global factor sqrt(8) removed; every amplitude rational.
psi={x:rot(1+x[0]+x[2])[x[1]]*rot(1+x[2]+x[4])[x[3]] for x in product((0,1),repeat=5)}
def mass(h):return sum((v*v for x,v in psi.items() if all(x[i]==a for i,a in h.items())),F(0))
checks=0;histories=0

def require(x):
 global checks
 if not x:raise ValueError('exact control failed')
 checks+=1
require(mass({})==8)
seen=set()
def visit(h):
 global histories
 key=tuple(sorted(h.items()))
 if key in seen:return
 seen.add(key);histories+=1
 den=mass(h);require(den>0)
 for i in range(5):
  if i in h or (i in B and not all(j in h for j in N[i])):continue
  for a in (0,1):
   new=dict(h);new[i]=a
   expected=F(1,2) if i in A else rot(1+sum(h[j] for j in N[i]))[a]**2
   require(mass(new)/den==expected)
   visit(new)
 # Residual amplitude ratio is constant across remaining configurations.
 ratios=[]
 for x,v in psi.items():
  if not all(x[i]==a for i,a in h.items()):continue
  predicted=F(1)
  for b in B:
   if b not in h:predicted*=rot(1+sum(x[j] for j in N[b]))[x[b]]
  require(predicted!=0);ratios.append(v/predicted)
 require(len(set(ratios))==1)
visit({})
# Same local Record at site1 seen by target0, differing distant Record at3.
p=[]
for b in (0,1):
 h={1:0,3:b};p.append(mass(dict(h,**{} )|{0:1})/mass(h))
require(p[0]!=p[1])
# Direct two-site controlled rotations prepare psi from uniform roots/blank B.
v={x:F(int(x[1]==0 and x[3]==0)) for x in psi}
for b,ctrl in [(1,None),(3,None),(1,0),(1,2),(3,2),(3,4)]:
 w={x:F(0) for x in psi}
 for x,z in v.items():
  if ctrl is not None and x[ctrl]==0:w[x]+=z;continue
  y=list(x);y[b]^=1;y=tuple(y)
  w[x]+=c*z;w[y]+=s*z*(1 if x[b]==0 else -1)
 v=w
require(v==psi)
print(json.dumps({'status':'PASS','checks':checks,'distinct_eligible_prefixes':histories,'qubits':5,'nearest_neighbor_edges':[[0,1],[2,1],[2,3],[4,3]],'remote_evidence_counterexample_A0_given_B0_zero_B1':list(map(str,p)),'physical_runs':0},indent=2))
