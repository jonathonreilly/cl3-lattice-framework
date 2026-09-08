from pathlib import Path
from itertools import product,combinations
import json,hashlib
B=Path('/private/tmp/toe-24h-probes-20260908/native-seed-component-sign-loop');r=json.loads((B/'RESULT.json').read_text());vs=list(product(range(6),repeat=3));ix={v:i for i,v in enumerate(vs)};edges=[];labels=[]
def shift(v,a):z=list(v);z[a]=(z[a]+1)%6;return tuple(z)
for v in vs:
 for a in range(3):edges.append((ix[v],ix[shift(v,a)]));labels.append((v,a))
index={x:i for i,x in enumerate(labels)};faces=[]
for a,b in combinations(range(3),2):
 for v in vs:faces.append([index[v,a],index[shift(v,a),b],index[shift(v,b),a],index[v,b]])
n=0
def need(x,m):
 global n
 if not x:raise RuntimeError(m)
 n+=1
def verify(row):
 need(len(row)==648 and all(type(x)==int and x in (0,1) for x in row),'binary')
 for v in range(216):need(sum(row[e] for e,ab in enumerate(edges) if v in ab)==3,'degree')
def flip(row,cy):
 endpoints=[v for e in cy for v in edges[e]]
 need(len(cy)==len(set(cy)) and all(endpoints.count(v)==2 for v in set(endpoints)),'simple cycle')
 for v in set(endpoints):need(sum(row[e] for e in cy if v in edges[e])==1,'alternating')
 out=row.copy();phase=1
 for e in cy:
  phase*=(-1)**sum(out[f] for f in range(e+1,648) if set(edges[e])&set(edges[f]));out[e]^=1
 verify(out);return out,phase
seed=[v[a]%2 for v,a in labels];need(seed==r['seed_bits'],'literal seed');verify(seed);x=seed
for p,es in zip(r['preparation_faces'],r['preparation_edges']):need(faces[p]==es,'prep face coordinates');x,_=flip(x,es)
need(x==r['loop_states'][0],'prep full endpoint');phases=[]
for i,(p,es) in enumerate(zip(r['face_order'],r['face_edges'])):
 need(faces[p]==es,'loop face coordinates');x,s=flip(x,es);need(x==r['loop_states'][i+1],'full loop state');phases.append(s)
x,s=flip(x,r['six_cycle']);phases.append(s);need(x==r['loop_states'][0],'full closure');need(-phases[0]*phases[1]*phases[2]*phases[3]==-1,'effective negative loop')
for es in r['preparation_edges']+r['face_edges']+[r['six_cycle']]:
 for e in es:need(all(abs(vs[edges[e][0]][a]-vs[edges[e][1]][a])<=1 for a in range(3)),'no seam')
out={'checks':n,'native_reverse_order_phases':phases,'effective_product':-1,'method':'literal coordinate labels, all degrees and reversed native edge ordering; no author imports or search'};Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(n,phases)
