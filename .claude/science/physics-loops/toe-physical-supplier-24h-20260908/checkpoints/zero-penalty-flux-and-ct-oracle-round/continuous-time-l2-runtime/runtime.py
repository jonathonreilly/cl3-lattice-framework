"""Reviewed-source L2 runtime candidate. No top-level sampling or launch."""
import json, math, hashlib
from pathlib import Path
from fractions import Fraction
from conditional import Trajectory, Conditional, draw
from geometry_reference import Geometry
ORACLE=Path('/private/tmp/toe-24h-probes-20260908/continuous-time-l2-calibration-design')
NAMES=('mid_NF','mid_X','mid_X2','endpoint_h','hL_hR','mid_X_endpoint_h','time_average_NF','endpoint_overlap','physical_event_count','hamming_activity_per_time','electric_corner_intensity','plane_anisotropy')

class Variates:
 """Discrete choices exact for ideal bits; finite-grid times explicitly approximate."""
 def __init__(self,bits):self.bits=bits;self.bit_calls=0
 def randbelow(self,n):
  if type(n) is not int or n<=0:raise ValueError('integer total')
  k=n.bit_length()
  for _ in range(4096):
   self.bit_calls+=1;x=self.bits(k)
   if type(x) is not int or not 0<=x<1<<k:raise ValueError('bit source domain')
   if x<n:return x
  raise ValueError('whole-job integer rejection budget')
 def uniform(self):
  self.bit_calls+=1;x=self.bits(53)
  if type(x) is not int or not 0<=x<1<<53:raise ValueError('bit source domain')
  return x/(1<<53)
 def stream(self):
  while True:yield self.uniform()

def weighted_integer(weights,rng):
 if any(type(x) is not int or x<0 for x in weights):raise ValueError('integer weights')
 u=rng.randbelow(sum(weights));acc=0
 for i,w in enumerate(weights):
  acc+=w
  if u<acc:return i
 raise ValueError('integer CDF')

class Runtime:
 def __init__(self,oracle_dir=ORACLE):
  self.g=Geometry(2);base=Path(oracle_dir)
  self.raw=json.loads((base/'BACKWARD_POWERS.json').read_text());self.oracle=json.loads((base/'ORACLE.json').read_text())
  self.states=self.raw['states'];self.index={x:i for i,x in enumerate(self.states)}
  self.witnesses=[]
  for i in range(len(self.states)):
   j=i;word=[]
   while self.raw['parents'][j] is not None:
    word.append(self.raw['parent_face'][j]);j=self.raw['parents'][j]
   self.witnesses.append(list(reversed(word)))
  self.bindings={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (base/'BACKWARD_POWERS.json',base/'ORACLE.json')}
 def target(self,T):
  return next(r for r in self.oracle['targets'] if Fraction(r['T_total'])==Fraction(T))
 def canonical_witness(self,path):
  # Identical initial configuration and physical path. Only proof tape changes.
  out=Trajectory(self.g,path.initial,list(path.events),path.T,list(self.witnesses[self.index[path.initial]]));out.check();return out
 def seed(self,T):return Trajectory(self.g,self.g.seed,[],float(T),[])
 def stationary_truncated(self,T,rng):
  row=self.target(T);weights=[int(x) for x in row['count_weights_integer']]
  k=weighted_integer(weights,rng);h=self.raw['h'];i=weighted_integer(h[k],rng);initial=self.states[i];labels=[]
  for remaining in range(k,0,-1):
   x=self.states[i];choices=[(i,None,self.raw['diag'][i]*h[remaining-1][i])]
   for p in range(self.g.M):
    if self.g.legal(x,p):
     j=self.index[x^self.g.masks[p]];choices.append((j,p,20*h[remaining-1][j]))
   if sum(c[2] for c in choices)!=h[remaining][i]:raise ValueError('backward normalizer')
   i,p,_=choices[weighted_integer([c[2] for c in choices],rng)];labels.append(p)
  times=sorted(float(T)*rng.uniform() for _ in range(k))
  if any(not 0<t<float(T) for t in times) or any(a>=b for a,b in zip(times,times[1:])):raise ValueError('whole-job initializer time collision/boundary')
  events=[(t,p) for t,p in zip(times,labels) if p is not None]
  path=Trajectory(self.g,initial,events,float(T),list(self.witnesses[self.index[initial]]));path.check()
  return path,dict(auxiliary_count=k,physical_events=len(events),scope='ideal bounded-count law; finite-grid times are not within its TV bound')
 def block(self,path,p,rng,maxevents=4096,tol=1e-12):
  c=Conditional(path,p,.95);out,receipt=draw(c,rng.stream(),maxevents=maxevents,tol=tol)
  return self.canonical_witness(out),receipt
 def measure(self,path):
  path.check();g=self.g;x=path.initial;mid=x;integral=0.;last=0.;T=path.T
  for t,p in path.events:
   integral+=(t-last)*g.nf(x);x^=g.masks[p]
   if t<=T/2:mid=x
   last=t
  integral+=(T-last)*g.nf(x)
  NF=g.nf(mid);hL=-g.nf(path.initial)/20;hR=-g.nf(x)/20;E=(hL+hR)/2
  X=sum(sum((-1)**(sum(r)+r[a])*(2*((mid>>e)&1)-1) for e,(r,c) in enumerate(g.links) if c==b)**2 for a in range(3) for b in range(3) if a!=b)/32
  overlap=sum((2*((path.initial>>e)&1)-1)*(2*((x>>e)&1)-1) for e in range(g.E))/g.E
  corner=sum(sum(2*((mid>>e)&1)-1 for e,(r,c) in enumerate(g.links) if c==a)**2 for a in range(3))/256
  planes=[sum(g.legal(mid,p) for p in range(a*8,(a+1)*8)) for a in range(3)]
  aniso=(3*sum(v*v for v in planes)-NF*NF)/192
  values=[NF,X,X*X,E,hL*hR,X*E,integral/T,overlap,len(path.events),len(path.events)/(6*T),corner,aniso]
  if not all(math.isfinite(z) for z in values):raise ValueError('nonfinite physical measurement')
  return dict(zip(NAMES,values))
 def save(self,path,file):
  path.check();payload=dict(initial=hex(path.initial),events=[[t.hex(),p] for t,p in path.events],T=path.T.hex(),witness=path.witness)
  Path(file).write_text(json.dumps(payload,separators=(',',':'))+'\n')
 def load(self,file):
  z=json.loads(Path(file).read_text());path=Trajectory(self.g,int(z['initial'],16),[(float.fromhex(t),p) for t,p in z['events']],float.fromhex(z['T']),z['witness']);path.check();return path
