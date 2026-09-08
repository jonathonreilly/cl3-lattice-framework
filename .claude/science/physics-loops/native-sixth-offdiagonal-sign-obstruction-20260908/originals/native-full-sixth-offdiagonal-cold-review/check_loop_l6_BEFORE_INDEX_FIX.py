from pathlib import Path
from itertools import product
import json,hashlib
B=Path('/private/tmp/toe-24h-probes-20260908/native-sixth-sign-loop');r=json.loads((B/'RESULT_L6.json').read_text())['witness']; vs=list(product(range(6),repeat=3));ix={v:i for i,v in enumerate(vs)};edges=[]
for v in vs:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%6;edges.append((ix[v],ix[tuple(w)]))
n=0
def need(x,m):
 global n
 if not x:raise RuntimeError(m)
 n+=1
states=r['states'];cycles=r['faces']+[r['six_cycle']];phases=[]
for row in states:
 need(len(row)==648 and all(type(b)==int and b in (0,1) for b in row),'bits')
 for v in range(216):need(sum(row[e] for e,ab in enumerate(edges) if v in ab)==3,'degree')
for j,cy in enumerate(cycles):
 row=states[j].copy(); vertices=[v for e in cy for v in edges[e]]
 need(len(set(cy))==len(cy) and all(vertices.count(v)==2 for v in set(vertices)),'cycle incidence')
 for v in set(vertices):need(sum(row[e] for e in cy if v in edges[e])==1,'alternating')
 phase=1
 for e in cy:
  # Later incident edge phase is the reverse-order gauge, independent of delivered earlier masks.
  phase*=(-1)**sum(row[f] for f in range(e+1,648) if set(edges[e])&set(edges[f]));row[e]^=1
 need(row==states[(j+1)%6],'full endpoint');phases.append(phase)
need(-phases[0]*phases[1]*phases[2]*phases[3]==-1,'effective closed sign')
Path(__file__).with_name('LOOP_L6_RESULT.json').write_text(json.dumps({'checks':n,'reverse_order_native_phases':phases,'closed_effective_sign':-1,'source_result_sha256':hashlib.sha256((B/'RESULT_L6.json').read_bytes()).hexdigest()},indent=2)+'\n');print(n,phases)
