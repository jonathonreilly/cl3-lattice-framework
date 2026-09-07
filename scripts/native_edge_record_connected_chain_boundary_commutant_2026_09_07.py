import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import time,signal,resource,sys,itertools,json,hashlib
from fractions import Fraction as F
signal.alarm(180);start=time.monotonic();AUDIT_TIMEOUT_SEC=180;N=6;I='I'*N;checks=0
def ck(x):
 global checks
 checks+=1
 if not x:raise AssertionError(checks)
def word(items):
 a=list(I)
 for k,v in items:a[k]=v
 return ''.join(a)
def mul(a,b):
 out=[];phase=1
 for x,y in zip(a,b):
  if x=='I':out.append(y)
  elif y=='I':out.append(x)
  elif x==y:out.append('I')
  else:out.append(({'X','Y','Z'}-{x,y}).pop());phase*=1j if (x,y) in [('X','Y'),('Y','Z'),('Z','X')] else -1j
 return ''.join(out),phase
def add(d,k,v):
 d[k]=d.get(k,F(0))+v
 if not d[k]:del d[k]
def comm(a,b):
 out={}
 for x,c in a.items():
  for y,d in b.items():
   z,phase=mul(x,y)
   if phase.imag:add(out,z,c*d*int(phase.imag))
 return out
HB={I:F(2),word([(4,'Z')]):F(-1,2),word([(5,'Z')]):F(-1)}
def hop(j):return {word([(j,a),(j+1,a)]):F(1,2) for a in 'XY'}
def total(cut=None):
 H=dict(HB)
 for j in range(3):
  if j!=cut:
   for k,v in hop(j).items():add(H,k,v)
 return H
def solve(m,cut=None):
 basis=[a+'I'*(4-m)+b for a in map(''.join,itertools.product('IXYZ',repeat=m)) if sum(x in 'XY' for x in a)%2==0 for b in map(''.join,itertools.product('IXYZ',repeat=2))]
 H=total(cut);rows={}
 for col,x in enumerate(basis):
  for k,v in comm({x:F(1)},H).items():rows.setdefault(k,{})[col]=v
 piv={}
 for row in rows.values():
  row=dict(row)
  while row:
   p=min(row)
   if p not in piv:
    v=row[p];piv[p]={k:x/v for k,x in row.items()};break
   v=row[p]
   for k,x in piv[p].items():add(row,k,-v*x)
 gens=[]
 for free in range(len(basis)):
  if free in piv:continue
  vec={free:F(1)}
  for p,row in sorted(piv.items(),reverse=True):
   v=-sum((x*vec.get(k,0) for k,x in row.items() if k!=p),F(0))
   if v:vec[p]=v
  gen={basis[k]:v for k,v in vec.items()};ck(not comm(gen,H));gens.append(gen)
 identmatter=all(all(k[:4]=='IIII' for k in g) for g in gens)
 if cut is None and m<4:ck(len(gens)==4);ck(identmatter)
 return {'m':m,'cut_edge':cut,'columns':len(basis),'rank':len(piv),'nullity':len(gens),'all_identity_matter':identmatter,'basis':[{k:str(v) for k,v in g.items()} for g in gens]}
results=[solve(m) for m in (1,2,3,4)]
# Declared severed boundary contrasts for each proper segment.
results += [solve(m,m-1) for m in (1,2,3)]
for a,b in itertools.product((0,1),repeat=2):
 op={I:F(1,4),word([(4,'Z')]):F((-1)**a,4),word([(5,'Z')]):F((-1)**b,4),word([(4,'Z'),(5,'Z')]):F((-1)**(a+b),4)}
 ck(not comm(op,total()))
ck(bool(comm(hop(0),total())))
ck(not comm(hop(0),total(1)))
Hmatter={k:v for k,v in total().items() if k not in HB};ck(not comm(Hmatter,total()))
ck(any(not r['all_identity_matter'] for r in results if r['cut_edge'] is not None))
for r in results:r['basis_sha256']=hashlib.sha256(json.dumps(r['basis'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);ck(0<rss<180);ck(time.monotonic()-start<180)
payload={'scope':'FullFock fourmode connected fixedhopping chain, evenCAR properprefix operators plus fourlevel finitebattery; no fuel switching or fixedinput claim','checks':checks,'results':results,'source_sha256':hashlib.sha256(open(__file__,'rb').read()).hexdigest(),'seconds':time.monotonic()-start,'rss_MiB':rss,'dependencies':{},'resources':{'timeout_seconds':180,'rss_limit_MiB':180,'blas_threads':1}}
if '--json' in sys.argv:print(json.dumps(payload,indent=2,allow_nan=False))
else:
 print('PASS connected-chain boundary commutants:',checks,'actual exact assertion calls')
 for row in results:print('PREFIX',row['m'],'CUT',row['cut_edge'],'rank',row['rank'],'nullity',row['nullity'],'basis_sha256',row['basis_sha256'])
 print('per_element: exact full Pauli commutator equations, battery projectors and nonzero hopping control')
 print('per_site: four fixed chain sites; proper prefixes1,2,3 and each severed contrast')
 print('per_mode: fullFock evenCAR operators with finite fourlevel battery; no fixedN compression')
 print('per_block: all exact nullspace bases and fullsupport contrast, source and basis hashes')
 print('lattice_wide: checked and not executed -- no arbitrarygraph/fuelswitch theorem or radius-error lower bound')
 print('SOURCE_SHA256',payload['source_sha256'])
