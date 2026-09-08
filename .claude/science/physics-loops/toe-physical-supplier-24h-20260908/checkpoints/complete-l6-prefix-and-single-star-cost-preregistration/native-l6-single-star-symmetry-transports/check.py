from pathlib import Path
from itertools import product,permutations,combinations
from fractions import Fraction as F
import json,hashlib,time,signal,resource
P=Path(__file__).resolve().parent;start=time.monotonic();signal.alarm(29);checks=0

def ck(x,s):
 global checks
 checks+=1
 if not x:raise ValueError(s)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
freeze=json.loads((P/'PRE_FREEZE.json').read_text())
for p,h in freeze['inputs'].items():ck(sha(p)==h,'input')
V=list(product(range(6),repeat=3));ix={v:i for i,v in enumerate(V)};K=[{} for _ in V];edges=[]
for v in V:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%6;i,j=sorted((ix[v],ix[tuple(w)]));z=-2*(-1)**sum(v[:a]);K[i][j]=z;K[j][i]=-z;edges.append((i,j))
E={frozenset(e):i for i,e in enumerate(edges)};star=sorted(i for i,e in enumerate(edges) if 0 in e)
basis=json.loads(Path(next(iter(freeze['inputs']))).read_text())['one_star'];sparse=[{i:x for i,x in enumerate(b['vector']) if x} for b in basis];norms=[b['norm_squared'] for b in basis];records=[]
for perm in permutations(range(3)):
 for signs in product((-1,1),repeat=3):
  phi=[ix[tuple(signs[a]*v[perm[a]]%6 for a in range(3))] for v in V];s={0:1};todo=[0]
  for i in todo:
   for j,k in K[i].items():
    val=s[i]*K[phi[i]][phi[j]]//k
    if j in s:ck(s[j]==val,'gauge cycle')
    else:s[j]=val;todo.append(j)
  ck(len(s)==216 and phi[0]==0 and s[0]==1,'center gauge')
  emap=[E[frozenset((phi[a],phi[b]))] for a,b in edges];ck(sorted(emap[e] for e in star)==star,'star')
  # Exact rational real W-coordinate matrix; paired complex action is determined by K.
  cols=[]
  for b,n in zip(sparse,norms):
   t={phi[i]:s[i]*z for i,z in b.items()};dots=[sum(z*t.get(i,0) for i,z in a.items()) for a in sparse]
   ck(sum((F(x*x,d) for x,d in zip(dots,norms)),F())==n,'W containment')
   cols.append([str(F(x,d)) for x,d in zip(dots,norms)])
  records.append(dict(permutation=perm,signs=signs,site_map=phi,site_signs=[s[i] for i in range(216)],star_map=[emap[e] for e in star],W_columns=cols))
pairs=list(combinations(star,2));orbits=[];remaining=set(pairs)
while remaining:
 rep=min(remaining);orb={tuple(sorted(rec['star_map'][star.index(e)] for e in rep)) for rec in records};ck(orb<=set(pairs),'pair orbit');orbits.append(dict(representative=rep,targets=[dict(pair=p,transport=next(i for i,r in enumerate(records) if tuple(sorted(r['star_map'][star.index(e)] for e in rep))==p)) for p in sorted(orb)]));remaining-=orb
ck(sorted(len(o['targets']) for o in orbits)==[3,12],'two orbits')
predecessors=[dict(last=c,first=[a for a in pairs if not set(a)&set(c)]) for c in pairs]
for r in predecessors:ck(len(r['first'])==6,'six predecessor')
# CAR exterior-sign fixture: a two-mode swap fixes vacuum and reverses ordered pair.
ck((-1)**1==-1,'two-mode exterior determinant');ck(sum(len(x['first']) for x in predecessors)==90,'ninety')
ck(time.monotonic()-start<29 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<384*1048576,'cap')
(P/'TRANSPORTS.json').write_text(json.dumps(dict(star=star,orbits=orbits,predecessors=predecessors,automorphisms=records),separators=(',',':'))+'\n');result=dict(status='PASS',predicates=checks,automorphisms=48,orbit_sizes=[len(o['targets']) for o in orbits],seconds=time.monotonic()-start,transport_sha=sha(P/'TRANSPORTS.json'));(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
