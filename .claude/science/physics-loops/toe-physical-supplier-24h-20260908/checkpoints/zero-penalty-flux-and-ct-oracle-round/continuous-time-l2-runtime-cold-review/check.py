import sys,json,hashlib,math,time,resource
from pathlib import Path
from fractions import Fraction
B=Path('/private/tmp/toe-24h-probes-20260908/continuous-time-l2-runtime');sys.path.insert(0,str(B))
import runtime
n=0
def ck(c):
 global n;n+=1
 if not c:raise ValueError(n)
t=time.monotonic();r=runtime.Runtime();g=r.g
for f,h in json.loads((B/'FINAL_FREEZE.json').read_text()).items():ck(hashlib.sha256((B/f).read_bytes()).hexdigest()==h)
for x,w in zip(r.states,r.witnesses):
 p=runtime.Trajectory(g,x,[],.5,w);z=r.measure(p)
 spins=[2*((x>>i)&1)-1 for i in range(24)]
 # Literal Fourier factor i*pi and staggered parity, separate channel accumulation.
 S=0
 for a in range(3):
  for b in range(3):
   if a==b:continue
   amp=sum(spins[e]*complex(math.cos(math.pi*rr[a]),math.sin(math.pi*rr[a]))*(-1)**sum(rr) for e,(rr,c) in enumerate(g.links) if c==b)/math.sqrt(32)
   S+=abs(amp)**2
 ck(abs(S-z['mid_X'])<1e-13)
 ck(z['mid_X_endpoint_h']==z['mid_X']*z['endpoint_h'])
 ck(z['mid_X2']==z['mid_X']**2)
# Independently sum all rows of B, exact first two backward recurrences.
for i,x in enumerate(r.states):
 js=[r.index[x^g.masks[p]] for p in range(24) if g.legal(x,p)]
 ck(r.raw['h'][1][i]==480+g.nf(x))
 ck(r.raw['h'][2][i]==(480-19*g.nf(x))*r.raw['h'][1][i]+20*sum(r.raw['h'][1][j] for j in js))
class Pick:
 def __init__(self,u):self.u=u
 def randbelow(self,n):return self.u
for weights in ([0,2,0,3],[1],[3,1,8]):
 outcomes=[runtime.weighted_integer(weights,Pick(i)) for i in range(sum(weights))]
 ck([outcomes.count(i) for i in range(len(weights))]==weights)
# Midpoint convention and a nonconstant integral independently from literal states.
p=next(p for p in range(24) if g.legal(g.seed,p));y=g.seed^g.masks[p]
z=runtime.Trajectory(g,g.seed,[(.25,p)],.5,[]);m=r.measure(z)
ck(m['mid_NF']==g.nf(y));ck(m['time_average_NF']==(g.nf(y)+g.nf(g.seed))/2)
# All finite-tape exhaustion is a failure, never recycled.
try:r.block(r.seed(.5),p,type('R',(),{'stream':lambda self:iter([])})())
except ValueError:ck(True)
else:ck(False)
print(json.dumps(dict(checks=n,seconds=time.monotonic()-t,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576),indent=2))
