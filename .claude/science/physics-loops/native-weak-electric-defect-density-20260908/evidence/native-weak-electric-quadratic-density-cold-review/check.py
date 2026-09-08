from itertools import product,combinations
import json
checks=0;rows=[]
def ck(x):
 global checks
 if not x:raise ValueError('count')
 checks+=1
for dims in [(4,4,4),(4,4,8),(4,8,8),(8,8,8)]:
 V=list(product(*(range(L) for L in dims)));idx={v:i for i,v in enumerate(V)};edges=[];inc=[[] for v in V]
 for v in V:
  for a in range(3):
   w=list(v);w[a]=(w[a]+1)%dims[a];e=len(edges);edges.append((idx[v],idx[tuple(w)],a));inc[idx[v]].append(e);inc[idx[tuple(w)]].append(e)
 faces=[]
 for v in V:
  for a,b in combinations(range(3),2):
   va=list(v);va[a]=(va[a]+1)%dims[a];vb=list(v);vb[b]=(vb[b]+1)%dims[b];faces.append({3*idx[v]+a,3*idx[v]+b,3*idx[tuple(va)]+b,3*idx[tuple(vb)]+a})
 edgefaces=[set() for e in edges]
 for f,es in enumerate(faces):
  for e in es:edgefaces[e].add(f)
 counts=[[0,0] for f in faces];types=[0,0]
 for es in inc:
  ck(len(es)==6)
  for a,b in combinations(es,2):
   typ=int(edges[a][2]==edges[b][2]);affected=edgefaces[a]^edgefaces[b];ck(len(affected)==(8 if typ else 6));types[typ]+=1
   for f in affected:counts[f][typ]+=1
 ck(types==[12*len(V),3*len(V)])
 for x in counts:ck(x==[24,8])
 rows.append({'dims':dims,'N':len(V),'pairs':types,'face_counts':[24,8]})
print(json.dumps({'status':'PASS','predicates':checks,'rows':rows},indent=2))
