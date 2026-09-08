import sys,json,runpy,contextlib,io,time,resource
from pathlib import Path
from fractions import Fraction as F
B=Path(__file__).parent;P=B.parent/'native-zero-penalty-sixth-spectator-coefficient';sys.path.insert(0,str(P));import solver_core as c
start=time.monotonic();n=0
def ck(v):
 global n;n+=1
 if not v:raise ValueError(n)
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(B.parent/'native-sixth-rational-metric/check.py'))
m=c.Model(json.loads((P/'PREFIXES.json').read_text()));ck(m.norms==d['d'])
A,ae=m.matrix(3);states=d['states'];W=d['W'];J=d['J'];ell=d['row']
# Exact radical comparisons using squared rational bounds, no numerical sqrt.
def contains(num,rad,z,err):
 lo=F.from_float(float(z))-F.from_float(float(err));hi=F.from_float(float(z))+F.from_float(float(err))
 if num==0:return lo<=0<=hi
 if num<0:return contains(-num,rad,-float(z),err)
 return hi>=0 and hi*hi>=num*num*rad and (lo<=0 or lo*lo<=num*num*rad)
for ia,a in enumerate(states):
 for ib,b in enumerate(states):
  q=J.get((a,b),F(0))+10*(a==b)
  ck(contains(q,6*W[a]/W[b],A[ia,ib],ae))
for ib,b in enumerate(states):ck(contains(-ell[b],1/(6*W[b]),m.close[ib],m.close_error))
x=c.np.zeros(512);x[0]=1;zero=c.np.zeros(512);error,res=c.residual_certificate(A,ae,x,zero,0.,m.gap(3))
sq=6*sum(W[a]*(J.get((a,0),F(0))+10*(a==0))**2 for a in states)
ck(F.from_float(res)**2>=sq);ck(error>=1)
print(json.dumps(dict(checks=n,seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576,scope='one actual matrix/closing enclosure vs independent rational metric; no coefficient solve'),indent=2))
