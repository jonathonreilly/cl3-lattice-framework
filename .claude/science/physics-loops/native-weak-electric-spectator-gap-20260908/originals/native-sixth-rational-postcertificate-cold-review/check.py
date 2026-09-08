from pathlib import Path
from fractions import Fraction as F
import sys,json,signal,time,resource
signal.alarm(180);t=time.monotonic()
sys.path.insert(0,'/private/tmp/toe-24h-probes-20260908/native-sixth-rational-postcertificate')
import core
p=Path('/private/tmp/toe-24h-probes-20260908/native-zero-penalty-sixth-spectator-coefficient');m=core.ExactModel(json.loads((p/'FRAME_RESULT.json').read_text()),json.loads((p/'PREFIXES.json').read_text()));A=m.matrix(3);n=0
def ck(x):
 global n;n+=1
 if not x:raise ValueError(n)
for (i,j),v in A.items():ck(m.W[i]*v==m.W[j]*A.get((j,i),0))
x=([((i*7)%13)-6 for i in range(512)],32);parts=[([int(i==0) for i in range(512)],1),([i%2 for i in range(512)],64)]
r=[-sum(F(v[i],d) for v,d in parts)/2 for i in range(512)]
for (i,j),v in A.items():r[i]-=F(v,m.den)*F(x[0][j],x[1])
sq=sum(w*y*y for w,y in zip(m.W,r));tick=time.monotonic();bound=core.residual(m,A,x,parts);cost=time.monotonic()-tick
ck(bound*bound>=sq);ck((bound-F(1,10**50))**2<sq)
ck(sum(l*l/w for l,w in zip(m.ell,m.W))==6)
for q in (F(0),F(2),F(7,13),F(10**80,31)):
 u=core.upper_sqrt(q);ck(u*u>=q)
# Negative sign/metric omissions must change this exact witness.
ck(sum(y*y for y in r)!=sq)
ck(core.gap(m,3)==F(999997540876869429,1446265625000000000))
Path(__file__).with_name('RESULT.json').write_text(json.dumps(dict(checks=n,residual_seconds=cost,total_seconds=time.monotonic()-t,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576,scope='one arbitrary dyadic exact fixture, not physical candidate cost or full-prefix forecast'),indent=2)+'\n')
