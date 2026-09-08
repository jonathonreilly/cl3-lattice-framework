import math,json,time,resource,pathlib,signal,hashlib
from fractions import Fraction
import runtime,conditional,conditional_original
B=pathlib.Path(__file__).resolve().parent;N=0

def need(c,s):
 global N;N+=1
 if not c:raise ValueError(s)
class Preset:
 def __init__(self,ints,uniforms):self.ints=iter(ints);self.uniforms=iter(uniforms)
 def randbelow(self,n):
  x=next(self.ints)
  if not 0<=x<n:raise ValueError('fixed integer domain')
  return x
 def uniform(self):return next(self.uniforms)
 def stream(self):return self.uniforms

def main():
 r=runtime.Runtime();g=r.g
 # Literal bit rejection paths, including rejected all-one candidate.
 bits=iter([7,2]);v=runtime.Variates(lambda k:next(bits));need(v.randbelow(5)==2 and v.bit_calls==2,'integer rejection literal')
 bits=iter([0,(1<<53)-1]);v=runtime.Variates(lambda k:next(bits));need(v.uniform()==0 and v.uniform()==1-2**-53,'finite-grid endpoints')
 try:runtime.Variates(lambda k:(1<<k)-1).randbelow(5)
 except ValueError as e:need('rejection budget' in str(e),'whole rejection failure')
 else:raise ValueError('missing rejection budget')
 paths=[]
 for T in (.5,2.):
  row=r.target(T);h=r.raw['h'];w=[int(x) for x in row['count_weights_integer']]
  # Auxiliary count0, fixed seed index0: exact constant path.
  z,rec=r.stationary_truncated(T,Preset([0,0],[]));need(z.initial==g.seed and not z.events and rec['auxiliary_count']==0,'literal countzero')
  paths.append(z)
  # Count2; seed; first legal nonself option; final self option.
  koffset=sum(w[:2]);selfweight=r.raw['diag'][0]*h[1][0]
  z,rec=r.stationary_truncated(T,Preset([koffset,0,selfweight,0],[.2,.8]));p=next(p for p in range(g.M) if g.legal(g.seed,p))
  need(z.initial==g.seed and z.events==[(.2*T,p)] and rec['auxiliary_count']==2,'literal selected/self trajectory')
  paths.append(z)
  try:r.stationary_truncated(T,Preset([koffset,0,selfweight,0],[.2,.2]))
  except ValueError as e:need('collision' in str(e),'collision whole failure')
  else:raise ValueError('collision survived')
 # Every BFS state is reachable and all constant-path endpoint/time/count invariants.
 for i,x in enumerate(r.states):
  z=conditional.Trajectory(g,x,[],.5,r.witnesses[i]);z.check();m=r.measure(z)
  need(m['endpoint_overlap']==1 and m['physical_event_count']==0 and m['hamming_activity_per_time']==0,'constant physical events')
  need(m['time_average_NF']==m['mid_NF']==g.nf(x),'constant NF')
  need(m['endpoint_h']==-g.nf(x)/20 and m['hL_hR']==(-g.nf(x)/20)**2,'constant endpoint moments')
 # Actual initialized piecewise paths: direct two-interval readouts.
 for z in paths:
  m=r.measure(z);nf0=g.nf(z.initial);final=z.check();nf1=g.nf(final)
  expected=nf0 if not z.events else .2*nf0+.8*nf1
  need(abs(m['time_average_NF']-expected)<1e-12,'piecewise integral')
  need(m['mid_NF']==nf1 and m['endpoint_overlap']==(1 if not z.events else 2/3),'midpoint and endpoint physical state')
  r.save(z,B/'ROUNDTRIP.json');zz=r.load(B/'ROUNDTRIP.json')
  need(zz.events==z.events and zz.T==z.T and zz.initial==z.initial and r.measure(zz)==m,'lossless hex time roundtrip')
 # Changed lazy tape is exactly the original algorithm on these fixed finite tapes.
 tape=[((i*37)%997+.5)/997 for i in range(4096)]
 for z in paths:
  for p in range(g.M):
   co=conditional_original.Conditional(z,p,.95);old,ro=conditional_original.draw(co,tape,maxevents=4096)
   cn=conditional.Conditional(z,p,.95);new,rn=conditional.draw(cn,iter(tape),maxevents=4096)
   need(old.initial==new.initial and old.events==new.events and ro==rn,'fixed tape original match')
   clean=r.canonical_witness(new);need(clean.initial==new.initial and clean.events==new.events,'witness only proof change')
   need(r.measure(clean)==r.measure(new),'witness invariant observables')
 return dict(checks=N,deterministic_paths=len(paths),fixed_tape_blocks=len(paths)*g.M,source_bindings=r.bindings,scope='fixed supplied variates only; no stochastic cost/profile/calibration')
if __name__=='__main__':
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('180s deterministic cap')));signal.alarm(180);start=time.monotonic()
 out=main();out['seconds']=time.monotonic()-start;out['rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576
 if out['rss_mib']>384:raise ValueError('RSS cap')
 print(json.dumps(out,indent=2))
