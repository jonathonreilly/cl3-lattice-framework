import time,signal,os
AUDIT_TIMEOUT_SEC=180
START=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS']:os.environ[k]='1'
from fractions import Fraction as F
from itertools import permutations,product
import json,resource,sys,hashlib
neighbors=((1,2),(0,3),(0,3),(1,2));orders=list(permutations(range(4)));configs=list(product(range(6),repeat=4));checks=[]
def ck(n,v):
 if not v:raise AssertionError(n)
 checks.append(n)
def phi(a,b,w):return w[0] if a==b else w[1] if a//2==b//2 else w[2]
def prob(v,order,w):
 done=set();p=F(1)
 for x in order:
  adj=done.intersection(neighbors[x]);weights=[]
  for s in range(6):
   val=1
   for y in adj:val*=phi(s,v[y],w)
   weights.append(val)
  p*=F(weights[v[x]],sum(weights));done.add(x)
 return p
rows=[]
for w in [(3,1,2),(2,2,2)]:
 laws=[[prob(v,o,w) for v in configs] for o in orders]
 for i,law in enumerate(laws):ck(f'normalized {w} order{i}',sum(law)==1)
 mono=laws[orders.index((0,1,2,3))];other=laws[orders.index((0,2,1,3))]
 ck(f'monotone agreement {w}',mono==other)
 mix=[sum(vals,F(0))/24 for vals in zip(*laws)]
 ck(f'mixture normalized {w}',sum(mix)==1)
 diffs=[a-b for a,b in zip(mix,mono)];tv=sum(map(abs,diffs),F(0))/2
 ck(f'expected constant discriminator {w}',(tv==0)==(w==(2,2,2)))
 # Square reflection permutes orders and neighbors, tested on actual mixture entries.
 index={v:i for i,v in enumerate(configs)}
 ck(f'mixture square reflection {w}',all(mix[i]==mix[index[(v[1],v[0],v[3],v[2])]] for i,v in enumerate(configs)))
 rows.append({'weights':w,'orders':24,'configurations':1296,'mixture_vs_monotone_TV':str(tv),'different_configurations':sum(x!=0 for x in diffs),'first_difference':next(({'configuration':configs[i],'mixture':str(mix[i]),'monotone':str(mono[i])} for i,d in enumerate(diffs) if d),None)})
def support(contents):return set(contents) if contents and len(set(contents))==1 else set(range(6))
ck('old endpoints valid before append',0 in support([]) and 1 in support([]))
unsafe=[]
for t in range(6):
 bad=[end for end in (0,1) if end not in support([t])]
 ck(f'every center outcome unsafe {t}',bool(bad));unsafe.append({'center':t,'violated_endpoint_contents':bad})
ck('center local rule normalized full support',support([0,1])==set(range(6)))
# Nonempty support for every nearest-neighbor count pattern, without enumerating ordered duplicates.
count=0
for k in range(7):
 for c in product(range(6),repeat=k):
  assert support(c);count+=1
ck('adverse rule total on all six-neighbor menus',count==sum(6**k for k in range(7)))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
ck('resource',0<rss<180 and time.monotonic()-START<180)
payload={'checks':checks,'rows':rows,'adverse_path':unsafe,'full_domain_cases':count,'seconds':time.monotonic()-START,'rss_MiB':rss,'source_sha256':hashlib.sha256(open(__file__,'rb').read()).hexdigest()}


if len(sys.argv)==2 and sys.argv[1]=='--json':
 print(json.dumps(payload,indent=2,allow_nan=False))
elif len(sys.argv)==1:
 print('PASS:',len(checks),'exact assertions')
 for level in ('per_element','per_site','per_mode','per_block','lattice_wide'):
  print(level+': conditional mathematical result; supplied inputs remain explicit')
 print('source_sha256:',payload['source_sha256'])
 print('TOTAL: PASS='+str(len(checks))+' FAIL=0')
else:
 raise SystemExit('usage: runner [--json]')
