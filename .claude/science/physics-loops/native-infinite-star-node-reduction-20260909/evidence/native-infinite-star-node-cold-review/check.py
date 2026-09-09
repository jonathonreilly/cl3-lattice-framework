"""Independent integer gauge/orbit and rational tail controls. No physical run."""
from itertools import permutations,product,combinations
from fractions import Fraction as F
import json
count=0

def require(x):
 global count
 if not x:raise ValueError('control')
 count+=1

def bond(r,s):
 d=[s[i]-r[i] for i in range(3)];i=next(i for i,x in enumerate(d) if x)
 return (-1)**(sum(r[:i]) if d[i]==1 else sum(s[:i]))*(1 if d[i]==1 else -1)

def perm(r,p):
 out=[0]*3
 for i in range(3):out[p[i]]=r[i]
 return tuple(out)
wrong=0
for p in permutations(range(3)):
 inv=[(i,j) for i in range(3) for j in range(i+1,3) if p[i]>p[j]]
 g=lambda r:(-1)**sum(r[i]*r[j] for i,j in inv)
 for r in product(range(-2,3),repeat=3):
  for a in range(3):
   s=list(r);s[a]+=1;s=tuple(s)
   require(bond(perm(r,p),perm(s,p))*g(r)*g(s)==bond(r,s))
   if p==(2,1,0):wrong+=bond(perm(r,p),perm(s,p))*(-1)**(r[0]*r[2]+s[0]*s[2])!=bond(r,s)
for a in range(3):
 for r in product(range(-2,3),repeat=3):
  for b in range(3):
   s=list(r);s[b]+=1;s=tuple(s)
   tr=lambda x:tuple(x[i]+(i==a) for i in range(3))
   gr=lambda x:(-1)**sum(x[a+1:])
   require(bond(tr(r),tr(s))*gr(r)*gr(s)==bond(r,s))
   rf=lambda x:tuple(-x[i] if i==a else x[i] for i in range(3))
   require(bond(rf(r),rf(s))*(-1)**(r[a]+s[a])==bond(r,s))
require(wrong>0)
# Direct ordered pair orbit action in signed-coordinate vectors.
neighbors=[tuple(sign*(i==a) for i in range(3)) for a in range(3) for sign in (1,-1)]
pairs=list(combinations(neighbors,2));words={(frozenset(a),frozenset(c)) for a in pairs for c in pairs if not set(a)&set(c)}
require(len(words)==90);sizes=[]
while words:
 a,c=next(iter(words));orbit=set()
 for p in permutations(range(3)):
  for signs in product((-1,1),repeat=3):
   action=lambda x:tuple(signs[i]*perm(x,p)[i] for i in range(3))
   orbit.add((frozenset(map(action,a)),frozenset(map(action,c))))
 require(orbit<=words);sizes.append(len(orbit));words-=orbit
require(sorted(sizes)==[6,12,12,12,48])
delta=F(3483,102400);beta=F(3);T=1024;x=delta*T
exp_lower=F(1);term=F(1)
for j in range(1,161):term*=x/j;exp_lower+=term
tail=F(90,8)*(2/delta**2+beta*T/delta**2+2*beta/delta**3)/exp_lower
require(tail<F(1,10**6))
print(json.dumps({'status':'PASS','predicates':count,'nonadjacent_single_product_gauge_mismatches':wrong,'ordered_pair_orbit_sizes':sorted(sizes),'original_gap_tail_below_1e_minus6':True,'physical_runs':0},indent=2))
