import json
# Exact integer Fock operations; no numerical array libraries.
def apply(word,state):
 sign=1
 for mode,dag in reversed(word):
  occupied=state>>mode&1
  if occupied==dag:return None,0
  sign*=(-1)**((state&((1<<mode)-1)).bit_count());state^=1<<mode
 return state,sign
single=[(1,1),(2,1),(4,1)];holes=[(6,1),(5,-1),(3,1)];checks=0
for a in range(3):
 for b in range(3):
  for basis,sector in ((single,1),(holes,2)):
   for j,(state,phase) in enumerate(basis):
    end,s=apply([(a,1),(b,0)],state);column=[0]*3
    if s:
     for k,(t,ph) in enumerate(basis):
      if end==t:column[k]=s*phase*ph
    want=[int(k==a and j==b) if sector==1 else int(a==b and k==j)-int(k==b and j==a) for k in range(3)]
    if column!=want:raise ValueError('3 versus conjugate3')
    checks+=1
# Actual distance-two/nearest-neighbour line-graph commutation parity.
def star(v):
 ans=[]
 for a in range(3):
  for direction in (1,-1):
   w=list(v);w[a]=(w[a]+direction)%6;ans.append(frozenset((v,tuple(w))))
 return ans
def cross(A,B):
 # Same edge commutes with itself; distinct intersecting edges anticommute.
 return sum(e!=f and bool(e&f) for e in A for f in B)%2
from itertools import combinations
v=star((0,0,0));adj=star((1,0,0));far=star((2,0,0))
for A in combinations(v,2):
 for B in combinations(adj,2):
  if cross(A,B):raise ValueError('adjacent even stars')
  checks+=1
if cross(v[:2],far[:2])!=1 or cross(v[:2],far[2:4]) or cross(v[2:4],far[:2]) or cross(v[2:4],far[2:4]):raise ValueError('distance two Cartan')
checks+=1
print(json.dumps({'status':'PASS','exact_predicates':checks,'physical_large_arrays':0}))
