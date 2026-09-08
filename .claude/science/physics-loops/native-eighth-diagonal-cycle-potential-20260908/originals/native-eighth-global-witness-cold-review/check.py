from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as F
import json,hashlib
p=Path('/private/tmp/toe-24h-probes-20260908/native-eighth-global-witness');raw=json.loads((p/'RESULT.json').read_text());checks=0

def req(v):
 global checks
 checks+=1
 if not v:raise RuntimeError('literal witness')
outputs=[]
for r in raw['results']:
 L=r['L'];N=L**3;coords=list(product(range(L),repeat=3));idx={v:i for i,v in enumerate(coords)}
 def sh(v,a,k=1):w=list(v);w[a]=(w[a]+k)%L;return tuple(w)
 def edge(v,a):return 3*idx[v]+a
 ends=[(idx[v],idx[sh(v,a)]) for v in coords for a in range(3)]
 cycles=[]
 for a,b in combinations(range(3),2):
  for v in coords:cycles.append((edge(v,a),edge(sh(v,a),b),edge(sh(v,b),a),edge(v,b)))
 if L==4:
  for a in range(3):
   for v in coords:
    if v[a]==0:cycles.append(tuple(edge(sh(v,a,k),a) for k in range(4)))
 req(len({frozenset(c) for c in cycles})==len(cycles)==(240 if L==4 else 648));features=[]
 for z in r['snapshots']:
  bits=z['bits'];req(len(bits)==3*N and all(type(x)is int and x in (0,1) for x in bits));req(hashlib.sha256(bytes(bits)).hexdigest()==z['sha256'])
  for v in coords:req(sum(bits[edge(v,a)]+bits[edge(sh(v,a,-1),a)] for a in range(3))==3)
  walls=fl=ps=0
  for c in cycles:
   b=[bits[e] for e in c];d=sum(b[i]!=b[(i+1)%4] for i in range(4));walls+=d;fl+=d==4;ps+=(-1)**sum(b)
  req((fl,ps,walls)==(z['F'],z['Psum'],z['domainwalls']));q=-F(209,28800)*walls+F(1769,216000)*ps;req(q==F(z['Q']));features.append((fl,ps,walls,q))
 for j,t in enumerate(r['legal_flip_tapes']):
  ids=t['edge_ids'];req(frozenset(ids) in {frozenset(c) for c in cycles});req([list(ends[e]) for e in ids]==t['edge_endpoints']);bits=r['snapshots'][j]['bits'];b=[bits[e] for e in ids];req(b==t['before_bits'] and all(b[i]!=b[(i+1)%4] for i in range(4)));new=bits.copy()
  for e in ids:new[e]^=1
  req(new==r['snapshots'][j+1]['bits'])
 det=(features[1][0]-features[0][0])*(features[2][3]-features[0][3])-(features[2][0]-features[0][0])*(features[1][3]-features[0][3]);req(det==F(r['determinant'])!=0);outputs.append(dict(L=L,features=[list(x[:3]) for x in features],determinant=str(det)))
result=dict(checks=checks,results=outputs,scope='Independent delivered-bit replay using literal plaquettes plus straight winding cycles; no author import or sampling');Path(__file__).with_name('RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
