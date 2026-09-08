from pathlib import Path
from itertools import product
import sys,json,hashlib,math
B=Path('/private/tmp/toe-24h-probes-20260908/continuous-time-face-conditional');sys.path.insert(0,str(B));import conditional as c
n=0
def need(x,m):
 global n
 if not x:raise RuntimeError(m)
 n+=1
freeze=json.loads((B/'FINAL_FREEZE.json').read_text())
for f,h in freeze['files'].items():need(hashlib.sha256((B/f).read_bytes()).hexdigest()==h,'freeze '+f)
def E(O,V,t,g):
 if len(O)==1:return [[math.exp(-V*g.nf(O[0])*t)]]
 u=V*g.nf(O[0]);v=V*g.nf(O[1]);d=v-u;r=math.sqrt(d*d+4);s=math.sinh(r*t/2);co=math.cosh(r*t/2);f=math.exp(-(u+v)*t/2)
 return [[f*(co+d/r*s),f*2/r*s],[f*2/r*s,f*(co-d/r*s)]]
for L in [2,4]:
 g=c.Geometry(L);qs=[p for p in range(g.M) if g.legal(g.seed,p)]
 for q in qs[:2]:
  path=c.Trajectory(g,g.seed,[(.17,q)],.4,[])
  for p in [0,1,g.M//3]:
   x=c.Conditional(path,p,.73);Ds=[E(O,.73,t,g) for O,t in zip(x.orbits,x.durations)];h=[1.]*len(x.orbits[-1])
   for i in range(len(Ds)-1,-1,-1):
    if i<len(x.C):h=[sum(a*b for a,b in zip(row,h)) for row in x.C[i]]
    h=[sum(a*b for a,b in zip(row,h)) for row in Ds[i]]
   need(all(abs(a/sum(h)-b/sum(x.h[0]))<1e-12 for a,b in zip(h,x.h[0])),'independent boundary marginal')
   before=(path.initial,list(path.events),list(path.witness));out,r=c.draw(x,[.68]*200)
   need(c.Conditional(out,p,.73).partition_signature()==x.partition_signature(),'output partition')
   need((path.initial,path.events,path.witness)==before,'input unchanged')
   try:c.draw(x,[])
   except ValueError:need((path.initial,path.events,path.witness)==before,'failure atomic input')
   else:raise RuntimeError('empty tape accepted')
O=Path(__file__).parent;(O/'RESULT.json').write_text(json.dumps({'checks':n,'scope':'fixed inputs and tapes only, direct hyperbolic boundary weights; no RNG'},indent=2)+'\n');(O/'READ_HASHES.json').write_text(json.dumps({str(B/f):h for f,h in freeze['files'].items()},indent=2)+'\n');print(n)
