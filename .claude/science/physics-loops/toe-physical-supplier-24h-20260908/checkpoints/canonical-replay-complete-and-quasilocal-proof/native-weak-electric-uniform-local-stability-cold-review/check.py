from itertools import product,combinations
from fractions import Fraction as F
import json
out=[]
for L in (4,6):
 vertices=list(product(range(L),repeat=3));edges={};inc={v:[] for v in vertices}
 def move(v,a):w=list(v);w[a]=(w[a]+1)%L;return tuple(w)
 for v in vertices:
  for a in range(3):
   k=(v,a);e=len(edges);edges[k]=e;inc[v].append(e);inc[move(v,a)].append(e)
 masks=[set() for _ in edges];face=0
 for v in vertices:
  for a,b in combinations(range(3),2):
   es=[edges[v,a],edges[move(v,a),b],edges[move(v,b),a],edges[v,b]]
   for e in es:masks[e].add(face)
   face+=1
 labels=set();counts=[[0,0] for _ in range(face)]
 for v in vertices:
  for e,f in combinations(inc[v],2):
   s=frozenset(masks[e]^masks[f]);assert len(s)in(6,8) and s not in labels;labels.add(s)
   for p in s:counts[p][len(s)==8]+=1
 assert all(c==[24,8] for c in counts)
 assert all(len(masks[e]&masks[f])<=1 for e,f in combinations(range(len(edges)),2))
 out.append({'L':L,'distinct_pair_flux_labels':len(labels),'faces':face,'every_face_incidence':[24,8]})
assert (F(24,36)+F(8,64))/4==F(19,96)
print(json.dumps({'status':'PASS','geometry':out,'coefficient':'19/96','scope':'exact finite geometry only'},indent=2))
