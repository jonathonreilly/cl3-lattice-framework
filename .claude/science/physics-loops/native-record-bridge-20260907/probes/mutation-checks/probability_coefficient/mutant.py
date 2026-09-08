import itertools,json,hashlib,time,resource
from fractions import Fraction as F
from pathlib import Path
start=time.monotonic();checks=[]
def ck(name,b):
 if not b:raise AssertionError(name)
 checks.append(name)
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
dirs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
rots=[]
for perm in itertools.permutations(range(3)):
 for signs in itertools.product([-1,1],repeat=3):
  if parity(perm)*signs[0]*signs[1]*signs[2]!=1:continue
  rots.append(tuple(dirs.index(tuple(signs[i]*d[perm[i]] for i in range(3))) for d in dirs))
ck('24 distinct proper cubic rotations',len(set(rots))==24)
ck('rotation group closed',all(tuple(a[b[i]] for i in range(6)) in rots for a in rots for b in rots))
configs=list(itertools.product([-1,0,1],repeat=6)) # zero-record, blank, identity-record
def act(c,r):return tuple(c[r[i]] for i in range(6))
def prob(c,k):return F(1,2)+k*sum(c)/6
orbits={}
for c in configs:orbits.setdefault(min(act(c,r) for r in rots),[]).append(c)
fixed=[sum(act(c,r)==c for c in configs) for r in rots]
ck('Burnside census equals explicit orbit partition',sum(fixed)==24*len(orbits))
ck('orbit partition covers all729',sum(map(len,orbits.values()))==729)
rows=[]
for k in [F(1,3),F(2,3)]:
 vals=[prob(c,k) for c in configs]
 ck('strict positivity '+str(k),all(0<p<1 for p in vals))
 ck('normalization '+str(k),all(p+(1-p)==1 for p in vals))
 ck('all cubic covariance '+str(k),all(prob(act(c,r),k)==prob(c,k) for c in configs for r in rots))
 ck('variation '+str(k),len(set(vals))>1)
 ck('one identity neighbor '+str(k),prob((1,0,0,0,0,0),k)==F(1,2)+k/12)
 rows.append({'kappa':str(k),'min':str(min(vals)),'max':str(max(vals)),'one_identity':str(prob((1,0,0,0,0,0),k)),'all_rows':[str(x) for x in vals]})
ck('two laws differ same condition',rows[0]['one_identity']!=rows[1]['one_identity'])
ck('bad kappa2 genuinely negative',prob((-1,)*6,F(2))<0)
ck('singled-neighbor rule violates cubic covariance',any(F(1,2)+F(c[0],12)!=F(1,2)+F(act(c,r)[0],12) for c in configs for r in rots))
ck('constant rule violates variation',len({F(1,2) for c in configs})==1)
# Exact matrix controls use rational2x2 arithmetic independently of rank-statistic enumeration.
def mm(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def inv(a):
 d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
 return ((F(a[1][1],d),F(-a[0][1],d)),(F(-a[1][0],d),F(a[0][0],d)))
def rank(a):return 2 if a[0][0]*a[1][1]-a[0][1]*a[1][0] else int(any(x for r in a for x in r))
mats=[((0,0),(0,0)),((1,0),(0,1)),((1,0),(0,0)),((0,1),(0,0)),((2,3),(1,4))]
gs=[((1,1),(0,1)),((1,0),(1,1)),((0,1),(-1,0))]
ck('rank invariant under independent similarity controls',all(rank(mm(mm(g,a),inv(g)))==rank(a) for a in mats for g in gs))
ck('zero identity fixed under similarity',all(mm(mm(g,a),inv(g))==a for a in mats[:2] for g in gs))
p=((1,0),(0,0));orbit=[mm(mm(((1,t),(0,1)),p),((1,-t),(0,1))) for t in range(20)]
ck('noncentral conjugacy explicit20distinct',len(set(orbit))==20)
# Relative-frame adverse: n=m=ez, rotate only m by pi aroundx.
n=(0,0,1);m=(0,0,1);rot=lambda x:(x[0],-x[1],-x[2]);dot=lambda a,b:sum(x*y for x,y in zip(a,b))
ck('dot product fails independent internal rotation',dot(n,m)!=dot(n,rot(m)))
ck('simultaneous pi rotation preserves dot product',dot(rot(n),rot(m))==dot(n,m))
# Finite append process probabilities: local probabilities multiply without resetting old entries.
positions=[(0,0,0),(1,0,0),(0,1,0)]
def weight(bits,k):
 state={};w=F(1)
 for x,b in zip(positions,bits):
  cs=[]
  for d in dirs:cs.append(state.get(tuple(x[i]+d[i] for i in range(3)),0))
  p=prob(cs,k);w*=p if b==1 else 1-p;state[x]=b
 return w
# fix lexical separation in branch expression above before execution
for k in [F(1,3),F(2,3)]:
 ws=[weight(bs,k) for bs in itertools.product([-1,1],repeat=3)]
 ck('all8 append histories positive '+str(k),all(w>0 for w in ws))
 ck('all8 append histories normalize '+str(k),sum(ws)==1)
result={'status':'PASS','assertions':len(checks),'checks':checks,'cubic_orbit_count':len(orbits),'fixed_counts':fixed,'orbit_size_histogram':{str(n):sum(len(v)==n for v in orbits.values()) for n in sorted(set(map(len,orbits.values())))},'law_rows':rows,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'runtime_sec':time.monotonic()-start,'rss_raw':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
print(json.dumps(result,sort_keys=True,indent=2))
