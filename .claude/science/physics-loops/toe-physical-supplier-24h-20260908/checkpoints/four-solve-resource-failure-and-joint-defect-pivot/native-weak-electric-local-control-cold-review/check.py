"""Independent literal incidence controls; no Hamiltonian evaluation."""
from itertools import product,combinations
from collections import Counter
from fractions import Fraction as F
import json
rows=[]
for dims in [(4,4,4),(6,6,6),(4,6,8)]:
 points=list(product(*(range(x) for x in dims)))
 def step(v,a,d=1):
  w=list(v);w[a]=(w[a]+d)%dims[a];return tuple(w)
 ef={};faces=[]
 for v in points:
  for a,b in combinations(range(3),2):
   edges={(v,a),(v,b),(step(v,a),b),(step(v,b),a)};idx=len(faces);faces.append(edges)
   for e in edges:ef.setdefault(e,set()).add(idx)
 census=Counter();perface=[Counter() for _ in faces]
 for v in points:
  incident=[(v,a) for a in range(3)]+[(step(v,a,-1),a) for a in range(3)]
  for e,f in combinations(incident,2):
   kind='opposite' if e[1]==f[1] else 'perpendicular';flipped=ef[e]^ef[f];expected=8 if kind=='opposite' else 6
   if len(flipped)!=expected:raise ValueError('touched faces')
   census[kind]+=1
   for i in flipped:perface[i][kind]+=1
 if any(x!=Counter(perpendicular=24,opposite=8) for x in perface):raise ValueError('perface')
 rows.append({'dims':dims,'faces':len(faces),'pairs':dict(census),'perface':[24,8],'max_touched':8})
for m in range(1,257):
 for d in range(1,min(m,8)+1):
  if (m-d+7)//8 < (m+7)//8-1:raise ValueError('ceiling induction')
# Commuting projectors reduced to their joint binary spectrum; exact off-block domination.
n=0
for m in range(1,9):
 for hit in range(1,1<<m):
  for defects in range(1<<m):
   q=int(defects==(1<<m)-1);qprime=int((defects^hit)==(1<<m)-1)
   untouched=((1<<m)-1)^hit;remaining=int(defects&untouched==untouched)
   if qprime*(1-q)>remaining:raise ValueError('projector domination')
   n+=1
print(json.dumps({'status':'PASS','geometry':rows,'binary_projector_controls':n,'induction_range':256,'physical_calls':0},indent=2))
