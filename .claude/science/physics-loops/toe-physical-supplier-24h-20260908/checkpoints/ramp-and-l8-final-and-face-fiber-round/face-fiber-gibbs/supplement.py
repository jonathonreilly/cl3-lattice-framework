import json,itertools,time,resource,sys,signal
from fractions import Fraction as F
import core
from check import w,enumerated,literal_nf
checks=0
def need(c,msg):
 global checks
 checks+=1
 if not c:raise ValueError(msg)
def main():
 g=core.Geometry(2);seen={g.seed};queue=[g.seed]
 for x in queue:
  for f in g.faces:
   if tuple((x>>e)&1 for e in f) in ((1,0,1,0),(0,1,0,1)):
    y=x^sum(1<<e for e in f)
    if y not in seen:seen.add(y);queue.append(y)
 need(len(seen)==864,'literal component size')
 for x in queue:
  need(g.nf(x)==literal_nf(g,x),'all component Nf');g.validate(x)
  need(g.flux(x)==g.flux(g.seed),'all component flux')
  for p in range(g.M):
   if g.legal(x,p):
    y=x^g.masks[p];need(y in seen,'move component');need(g.changed_nf(x,p,g.nf(x))==literal_nf(g,y),'all move cache')
    need(g.weight(x,y,g.nf(x),F(19,20))==w(g,x,y,F(19,20)),'multiplicity')
 l=core.Geometry(4);x=l.seed;walk=[x]
 for i in range(64):
  ps=[p for p in range(l.M) if l.legal(x,p)];p=ps[(17*i+3)%len(ps)];y=x^l.masks[p]
  need(l.changed_nf(x,p,l.nf(x))==literal_nf(l,y),'L4 Nf');l.validate(y);need(l.flux(y)==l.flux(l.seed),'L4 flux');x=y;walk.append(x)
 path=core.PackedPath(l,walk,F(19,20))
 allowed=0;zeros=0
 for p in range(l.M):
  O,N,T=path.fiber(p)
  for i,matrix in enumerate(T):
   for a,row in enumerate(matrix):
    for b,t in enumerate(row):
     need(t==w(l,O[i][a],O[i+1][b],F(19,20)),'L4 literal matrix')
     if t:
      allowed+=1
      old=walk[i]^walk[i+1];new=O[i][a]^O[i+1][b]
      if old!=l.masks[p]:need(new==old,'other-face bond fixed by support')
     else:zeros+=1
 # Alias cancellation on a genuine fiber with fixed slices.
 states=queue[:1]
 # Find a legal two-step path whose p orbit is singleton at one slice and double at another.
 fixture=None
 for x in queue:
  for q in range(g.M):
   if g.legal(x,q):
    y=x^g.masks[q]
    for p in range(g.M):
     if g.legal(x,p)!=g.legal(y,p):fixture=([x,y,x],p);break
    if fixture:break
  if fixture:break
 need(fixture is not None,'mixed orbit fixture')
 xs,p=fixture;O,m=enumerated(g,xs,p,F(19,20));aliases=[z if len(z)==2 else z*2 for z in O];raw={}
 for ys in itertools.product(*aliases):
  mass=w(g,ys[0],ys[1],F(19,20))*w(g,ys[1],ys[2],F(19,20));raw[ys]=raw.get(ys,F(0))+mass
 raw={k:v for k,v in raw.items() if v};Z=sum(raw.values())
 need({k:v/Z for k,v in raw.items()}==m,'uniform singleton aliases harmless')
 return dict(checks=checks,component=len(seen),L4_allowed_entries=allowed,L4_zero_entries=zeros,alias_control='uniform singleton duplication cancels after pushforward; not a bias mutant')
if __name__=='__main__':
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError()));signal.alarm(180);t=time.monotonic();r=main();r['elapsed']=time.monotonic()-t;r['rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);need(r['rss_mib']<384,'RSS');r['checks']=checks;print(json.dumps(r,indent=2))
