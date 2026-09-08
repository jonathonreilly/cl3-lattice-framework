"""Short-trajectory deterministic CT conditional prototype; no RNG/launcher."""
import math
from dataclasses import dataclass
import bridge
from geometry_reference import Geometry

def product(x,y):
 z=x*y
 if not math.isfinite(z) or (x>0 and y>0 and z==0):raise ValueError('message product under/overflow')
 return z

def matmul(A,B):return [[sum(product(x,y) for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def normalize(A):
 s=max(z for row in A for z in row)
 if not math.isfinite(s) or s<=0:raise ValueError('zero/nonfinite matrix normalization')
 out=[[z/s for z in row] for row in A]
 if any(z>0 and v==0 for row,scaled in zip(A,out) for z,v in zip(row,scaled)):raise ValueError('matrix underflow')
 return out

def orbit(g,x,p):return sorted({x,x^g.masks[p]}) if g.legal(x,p) else [x]
def transfer(g,O,V,T,m=1.):
 if len(O)==1:return [[1.]]
 d=V*(g.nf(O[1])-g.nf(O[0]));logs=[[bridge.logE(d,m,T,i,j) for j in (0,1)] for i in (0,1)];shift=max(z for row in logs for z in row)
 A=[[0. if z==-math.inf else math.exp(z-shift) for z in row] for row in logs]
 if any(math.isfinite(z) and a==0 for row,aa in zip(logs,A) for z,a in zip(row,aa)):raise ValueError('transfer underflow')
 return A

from verified_path import Trajectory

class Conditional:
 def __init__(self,path,p,V):
  path.check()
  if type(p) is not int or not 0<=p<path.g.M or not math.isfinite(V) or V<0:raise ValueError('face/V')
  self.path=path;self.g=path.g;self.p=p;self.V=V;x=path.initial;self.orbits=[orbit(self.g,x,p)];self.retained=[]
  for t,q in path.events:
   x^=self.g.masks[q]
   if q!=p:self.retained.append((t,q));self.orbits.append(orbit(self.g,x,p))
  times=[0.]+[t for t,q in self.retained]+[path.T];self.durations=[b-a for a,b in zip(times,times[1:])]
  self.C=[]
  for i,(t,q) in enumerate(self.retained):
   self.C.append([[int(self.g.legal(x,q) and x^self.g.masks[q]==y) for y in self.orbits[i+1]] for x in self.orbits[i]])
  self.D=[transfer(self.g,O,V,t) for O,t in zip(self.orbits,self.durations)]
  self.h=[None]*len(self.D)
  for i in range(len(self.D)-1,-1,-1):
   future=[1.]*len(self.orbits[i]) if i==len(self.D)-1 else [sum(product(c,z) for c,z in zip(row,self.h[i+1])) for row in self.C[i]]
   h=[sum(product(x,y) for x,y in zip(row,future)) for row in self.D[i]];scale=max(h)
   if not math.isfinite(scale) or scale<=0:raise ValueError('zero conditional class')
   self.h[i]=[z/scale for z in h]
   if any(z>0 and v==0 for z,v in zip(h,self.h[i])):raise ValueError('message scaling underflow')
 def partition_signature(self):return (tuple(tuple(z) for z in self.orbits),tuple(self.retained))

class Tape:
 def __init__(self,values):self.values=iter(values);self.index=0
 def next(self):
  if self.index>=4096:raise ValueError('whole-block variate budget')
  try:x=next(self.values)
  except StopIteration:raise ValueError('supplied tape exhausted') from None
  self.index+=1
  if not math.isfinite(x) or not 0<=x<1:raise ValueError('variate domain')
  return x

def choose(weights,tape):
 total=sum(weights)
 if not math.isfinite(total) or total<=0 or any(not math.isfinite(z) or z<0 for z in weights):raise ValueError('conditional weights')
 target=tape.next()*total;s=0.
 for j,w in enumerate(weights):
  s+=w
  if target<s:return j
 raise ValueError('CDF rounding')

def interval_events(g,O,V,T,start,end,tape,maxevents,tol):
 if len(O)==1:
  if start!=end:raise ValueError('singleton endpoint')
  return [],0.
 d=V*(g.nf(O[1])-g.nf(O[0]));elapsed=0.;state=start;events=[];bracket_error_sum=0.
 while True:
  z=bridge.inverse_first(d,1.,T-elapsed,state,end,tape.next(),tol)
  if z['no_event']:return events,bracket_error_sum
  if len(events)>=maxevents:raise ValueError('whole-fixture event budget')
  lo,hi=z['bracket'];step=lo+(hi-lo)/2
  if not 0<step<T-elapsed:raise ValueError('zero/coincident endpoint event')
  nxt=elapsed+step
  if not elapsed<nxt<T:raise ValueError('event-time rounding')
  bracket_error_sum+=hi-lo;elapsed=nxt;events.append(elapsed);state=1-state

def draw(c,values,maxevents=64,tol=1e-12):
 if type(maxevents) is not int or maxevents<1:raise ValueError('event budget')
 tape=Tape(values);start=choose(c.h[0],tape);initial=c.orbits[0][start];events=[];base=0.;error=0.;newp=0
 for i,(D,O,T) in enumerate(zip(c.D,c.orbits,c.durations)):
  future=[1.]*len(O) if i==len(c.D)-1 else [sum(product(x,y) for x,y in zip(row,c.h[i+1])) for row in c.C[i]]
  end=choose([product(D[start][j],future[j]) for j in range(len(O))],tape)
  pe,err=interval_events(c.g,O,c.V,T,start,end,tape,maxevents-newp,tol);newp+=len(pe);error+=err
  events.extend((base+t,c.p) for t in pe);base+=T
  if i<len(c.C):
   nxt=choose([product(c.C[i][end][j],c.h[i+1][j]) for j in range(len(c.orbits[i+1]))],tape)
   events.append(c.retained[i]);start=nxt
 out=Trajectory.from_conditional(c.path,initial,events,c.p);out.check()
 if Conditional(out,c.p,c.V).partition_signature()!=c.partition_signature():raise ValueError('quotient changed')
 return out,dict(tape_used=tape.index,selected_events=newp,sum_local_bracket_widths=error,scope='ordinary floating inverse; width sum is not a rigorous global distribution error')

def strict_distant(g,p,q):
 dependency={e for f in g.affected[p] for e in g.faces[f]}
 return not dependency.intersection(g.faces[q])

def merged_pair(c,i):
 t,q=c.retained[i]
 if not strict_distant(c.g,c.p,q):raise ValueError('not strict distant')
 C=c.C[i]
 if any(sum(row)!=1 for row in C) or any(sum(col)!=1 for col in zip(*C)):raise ValueError('not bijective compatibility')
 return normalize(matmul(transfer(c.g,c.orbits[i],c.V,c.durations[i]+c.durations[i+1]),C))
