"""Portable exact H8 control, adapted from preserved research source."""
AUDIT_TIMEOUT_SEC=180
import argparse, signal
if __name__=='__main__':
 signal.alarm(AUDIT_TIMEOUT_SEC)
 parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');parser.parse_args()
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,time,resource,sys,signal
start=time.monotonic();checks=0
root=Path(__file__).resolve().parents[1]
def req(v,m):
 global checks
 checks+=1
 if not v:raise RuntimeError(m)
out=[]
for L in [4,6]:
 vertices=list(product(range(L),repeat=3));index={v:i for i,v in enumerate(vertices)};ends=[];bits=[]
 for v in vertices:
  for axis in range(3):
   w=list(v);w[axis]=(w[axis]+1)%L;ends.append((index[v],index[tuple(w)]));bits.append(v[axis]%2)
 adjacency=[[] for _ in vertices]
 for e,(v,w) in enumerate(ends):adjacency[v].append((w,e));adjacency[w].append((v,e))
 # Iterative four-step neighbor-slot enumeration, rather than recursive path source.
 cycles={}
 for v in range(len(vertices)):
  for slots in product(range(6),repeat=4):
   trail=[v];es=[]
   for slot in slots:
    nxt,e=adjacency[trail[-1]][slot]
    if len(trail)>1 and nxt==trail[-2]:break
    trail.append(nxt);es.append(e)
   if len(es)==4 and trail[-1]==v:cycles.setdefault(tuple(sorted(es)),tuple(es))
 req(len(cycles)==(240 if L==4 else 648),'complete cycle count')
 snapshots=[];tapes=[];seen={tuple(bits)}
 for stage in range(3):
  req(all(sum(bits[e] for _,e in adj)==3 for adj in adjacency),'full ice')
  fl=0;prod_sum=0;walls=0
  for es in cycles.values():
   b=[bits[e] for e in es];d=sum(b[i]!=b[(i+1)%4] for i in range(4));walls+=d;fl+=d==4;prod_sum+=(-1)**sum(b)
  q=-F(209,28800)*walls+F(1769,216000)*prod_sum
  snapshots.append(dict(bits=bits.copy(),sha256=hashlib.sha256(bytes(bits)).hexdigest(),F=fl,Psum=prod_sum,domainwalls=walls,Q=str(q)))
  if stage<2:
   for es in cycles.values():
    b=[bits[e] for e in es]
    if not all(b[i]!=b[(i+1)%4] for i in range(4)):continue
    candidate=bits.copy()
    for e in es:candidate[e]^=1
    if tuple(candidate) in seen:continue
    req(all(sum(candidate[e] for _,e in adj)==3 for adj in adjacency),'legal flip preserves ice')
    tapes.append(dict(edge_ids=list(es),edge_endpoints=[ends[e] for e in es],before_bits=b));bits=candidate;seen.add(tuple(bits));break
   else:raise RuntimeError('no successor')
 f=[r['F'] for r in snapshots];q=[F(r['Q']) for r in snapshots]
 determinant=(f[1]-f[0])*(q[2]-q[0])-(f[2]-f[0])*(q[1]-q[0]);req(determinant!=0,'nonaffine exact determinant')
 original=next(r for r in json.loads((root/'outputs/native_eighth_global_2026_09_08.json').read_text())['results'] if r['L']==L)
 for i,r in enumerate(snapshots):req(r['sha256']==original['snapshots'][i]['seed_sha256'],'independent original-state hash match')
 out.append(dict(L=L,edge_order='coordinate vertex lexicographic then positive axis0,1,2',snapshots=snapshots,legal_flip_tapes=tapes,determinant=str(determinant)))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(time.monotonic()-start<180 and 0<rss<384,'resources')
r=dict(checks=checks,results=out,seconds=time.monotonic()-start,rss_mib=rss,reviewed_source_sha256=hashlib.sha256((root/'scripts/native_eighth_global_2026_09_08.py').read_bytes()).hexdigest())
(Path(__file__).resolve().parents[1]/'outputs/native_eighth_witness_2026_09_08.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(dict(checks=checks,seconds=r['seconds'],witnesses=[dict(L=x['L'],features=[(s['F'],s['Psum'],s['domainwalls']) for s in x['snapshots']],determinant=x['determinant'],tapes=x['legal_flip_tapes']) for x in out]),indent=2))
