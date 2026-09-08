from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import json,time,signal,resource,sys,hashlib
signal.alarm(180);start=time.monotonic()
shapes={'one':[(0,1)],'pair':[(0,1),(1,2)],'disjoint':[(0,1),(2,3)],'star':[(0,1),(0,2),(0,3)],'path':[(0,1),(1,2),(2,3)],'pair_edge':[(0,1),(1,2),(3,4)]}
def energy_series(edges,bits):
 k=len(edges);N=1<<k
 energies=[sum(sum((1-2*bits[e]) for e in range(k) if z>>e&1 and v in edges[e])**2 for v in range(6)) for z in range(N)]
 assert energies[0]==0 and all(energies[1:])
 masks=[sum(1<<f for f in range(e) if set(edges[f])&set(edges[e])) for e in range(k)]
 def V(x):return [sum((-1)**((masks[e]&z).bit_count())*x[z^(1<<e)] for e in range(k)) for z in range(N)]
 psi=[[F(z==0) for z in range(N)]];E=[F(0)]
 for n in range(1,7):
  t=V(psi[-1]);E.append(t[0]);psi.append([F(0)]+[(-t[z]+sum(E[j]*psi[n-j][z] for j in range(1,n)))/energies[z] for z in range(1,N)])
 return E,energies
rows=[]
for name,edges in shapes.items():
 for bits in product((0,1),repeat=len(edges)):
  E,levels=energy_series(edges,bits);connected=F(0)
  for n in range(1,len(edges)+1):
   for ids in combinations(range(len(edges)),n):
    connected+=(-1)**(len(edges)-n)*energy_series([edges[e] for e in ids],[bits[e] for e in ids])[0][6]
  rows.append({'shape':name,'bits':bits,'E':list(map(str,E)),'D':levels,'connected6':str(connected)})
assert time.monotonic()-start<180
out={'rows':rows,'seconds':time.monotonic()-start,'rss_MiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
for r in rows:print(r['shape'],r['bits'],r['E'][4],r['E'][6],r['connected6'])
# Independent resolvent ring sum with full charge spectrum and incident native signs.
from itertools import permutations
ringedges=[(0,1),(1,2),(2,3),(3,0)]
for native in (True,False):
 total=F(0)
 for word in permutations(range(4)):
  active=set();phase=1;den=1
  for k,e in enumerate(word):
   if native:phase*=(-1)**sum(f>e and bool(set(ringedges[f])&set(ringedges[e])) for f in active)
   active.symmetric_difference_update({e})
   if k<3:den*=sum(sum((1-2*(f%2)) for f in active if v in ringedges[f])**2 for v in range(4))
  total-=F(phase,den)
 assert total==(F(1,2) if native else F(-5,2))
# Prospective exact analytic table comparison, including new D6 and D10 paths.
for r in rows:
 name=r['shape'];bits=r['bits'];E=list(map(F,r['E']))
 if name=='path':
  D=2+4*sum(bits[i]==bits[i+1] for i in (0,1))
  assert E[6]==-(F(35)+F(2,D))/32
 if name in ('one','pair','star'):
  k={'one':1,'pair':2,'star':3}[name];assert E[4]==F(k*k,8) and E[6]==-F(k**3,16)
counts={0:0,1:0,2:0}
for middle in (0,1):
 patterns=[b for b in product((0,1),repeat=5) if sum(b)+middle==3]
 for l in patterns:
  for r in patterns:
   local={0:0,1:0,2:0}
   for x in l:
    for y in r:local[(x==middle)+(y==middle)]+=1
   assert local=={0:9,1:12,2:4}
coefficient=-(F(3,16)+F(45,8)+F(60,8)+3*(F(9*3,16)+F(12,6)+F(4*13,80)))
assert coefficient==-F(1053,40)
Path(__file__).with_name('SUPPLEMENT.json').write_text(json.dumps({'full_carrier_sixth_per_vertex':str(coefficient),'path_counts_per_middle_edge':{'D2':9,'D6':12,'D10':4},'native_ring':'1/2','bare_X_mutant':'-5/2','analytic_table_checks':len(rows)},indent=2)+'\n')
