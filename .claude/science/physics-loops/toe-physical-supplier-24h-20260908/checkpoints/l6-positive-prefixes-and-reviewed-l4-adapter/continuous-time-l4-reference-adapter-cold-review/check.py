from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as F
import sys,json,hashlib,math
sys.dont_write_bytecode=True;S=Path('/private/tmp/toe-24h-probes-20260908/continuous-time-l4-reference-adapter');sys.path.insert(0,str(S));from adapter import Adapter
from verified_path import Trajectory
O=Path(__file__).parent;n=0
def ck(x):
 global n;n+=1
 if not x:raise ValueError(n)
a=Adapter(4);vs=list(product(range(4),repeat=3));es=[(v,d) for v in vs for d in range(3)];index={e:i for i,e in enumerate(es)}
def step(v,d):w=list(v);w[d]=(w[d]+1)%4;return tuple(w)
faces=[(index[v,d],index[step(v,d),e],index[step(v,e),d],index[v,e]) for d,e in combinations(range(3),2) for v in vs]
def legal(x,p):return tuple((x>>e)&1 for e in faces[p]) in ((0,1,0,1),(1,0,1,0))
def nf(x):return sum(legal(x,p) for p in range(192))
x=sum((v[d]%2)<<i for i,(v,d) in enumerate(es));ck(x==a.g.seed)
events=[];states=[x]
for j in range(24):
 p=next(p for p in [(j*19+k)%192 for k in range(192)] if legal(x,p));x^=sum(1<<e for e in faces[p]);events.append((float(F(j+1,50)),p));states.append(x)
 for v in vs:ck(sum((x>>i)&1 for i,(w,d) in enumerate(es) if w==v or step(w,d)==v)==3)
path=Trajectory(a.g,states[0],events,.5,[]);ck(path.check()==x)
for x in states:
 expected=[]
 for h in (1,2):
  total=0
  for d in range(3):
   for e in range(3):
    if d==e:continue
    z=sum((1j)**(h*v[d])*(-1)**sum(v)*(2*((x>>i)&1)-1) for i,(v,b) in enumerate(es) if b==e)
    total+=int(z.real)**2+int(z.imag)**2
  expected.append(F(total,256))
 ck(a.sources(x)==expected)
v=a.measure(path);mid=states[12];ck(v['mid_NF']==nf(mid));ck(v['mid_X1']==float(a.sources(mid)[0]));ck(v['endpoint_h']==float(-F(nf(states[0])+nf(states[-1]),40)))
integral=F(0);last=F(0)
for k,(t,p) in enumerate(events):integral+=(F(t)-last)*nf(states[k]);last=F(t)
integral+=(F(1,2)-last)*nf(states[-1]);ck(abs(v['time_average_NF']-float(integral/F(1,2)))<1e-12)
ck(a.balance(v,.5)==.95*v['time_average_NF']-2*24-v['endpoint_h'])
# Public deletion must be blocked, not merely assignment.
for obj in (path,a.g):
 try:delattr(obj,'_sealed')
 except AttributeError:ck(True)
 else:raise ValueError('public deletion bypass')
for key in ('M','_sealed'):
 try:a.g.__dict__[key]=0
 except TypeError:ck(True)
 else:raise ValueError('public dictionary bypass')
(O/'RESULT.json').write_text(json.dumps(dict(checks=n,scope='literal192-edge geometry,24 deterministic legal events,complex sources and path boundary; no sampler draw'),indent=2)+'\n');print(n)
