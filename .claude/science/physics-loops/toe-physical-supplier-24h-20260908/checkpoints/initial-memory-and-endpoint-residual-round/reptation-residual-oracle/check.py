import time,signal,resource,json,sys
start=time.monotonic();signal.alarm(180)
from itertools import product,combinations
from fractions import Fraction as F
from pathlib import Path
from decimal import Decimal,localcontext
L=2;rs=list(product(range(2),repeat=3));links=[(r,a) for r in rs for a in range(3)];ix={v:i for i,v in enumerate(links)};faces=[]
for a,b in combinations(range(3),2):
 for r in rs:
  ra=list(r);rb=list(r);ra[a]^=1;rb[b]^=1
  faces.append([ix[r,a],ix[tuple(ra),b],ix[tuple(rb),a],ix[r,b]])
def moves(x):
 out=[]
 for f in faces:
  z=[(x>>e)&1 for e in f]
  if z[0]==z[2] and z[1]==z[3] and z[0]!=z[1]:out.append(x^sum(1<<e for e in f))
 return out
seed=sum((r[a]%2)<<j for j,(r,a) in enumerate(links));states=[seed];indices={seed:0}
for x in states:
 for y in moves(x):
  if y not in indices:indices[y]=len(states);states.append(y)
adj=[[indices[y] for y in moves(x)] for x in states];nf=[len(y) for y in adj];modes=[]
for a in range(3):
 for b in range(3):
  if a==b:continue
  modes.append([sum((-1)**(sum(r)+r[a])*(2*((x>>j)&1)-1) for j,(r,pol) in enumerate(links) if pol==b) for x in states])
x32=[sum(o[i]**2 for o in modes) for i in range(len(states))]
checks=0
def req(c):
 global checks
 checks+=1
 if not c:raise RuntimeError('oracle identity')
req(len(states)==864 and sum(nf)==6912)
req(all(adj[i].count(j)==adj[j].count(i) for i in range(864) for j in set(adj[i])))
# terms: coefficient, left h exponent, right h exponent, middle NF exponent, middle X exponent
obs=[[(F(1),0,0,1,0)],[(F(1),0,0,0,1)],[(F(1,2),1,0,0,0),(F(1,2),0,1,0,0)],[(F(1),1,1,0,0)],[(F(1,2),1,0,0,1),(F(1,2),0,1,0,1)],[(F(1),0,0,0,2)]]
allrows=[]
for V in (F(19,20),F(1)):
 scale=480 if V!=1 else 24;off=20 if V!=1 else 1;diag=[scale-(19 if V!=1 else 1)*f for f in nf]
 def apply(v):return [diag[i]*v[i]+off*sum(v[j] for j in adj[i]) for i in range(864)]
 vec=[[f**a for f in nf] for a in range(3)];prev=0
 for n in (2,48,192):
  k=n//2
  for step in range(prev,k):vec=[apply(v) for v in vec]
  prev=k;z=sum(v*v for v in vec[0]);cache={}
  def moment(a,b,r,s):
   key=(a,b,r,s)
   if key not in cache:cache[key]=F(sum(vec[a][i]*vec[b][i]*nf[i]**r*x32[i]**s for i in range(864)),z*32**s)*(V-1)**(a+b)
   return cache[key]
  means=[sum(c*moment(a,b,r,s) for c,a,b,r,s in terms) for terms in obs]
  cross=[[sum(c*d*moment(a+aa,b+bb,r+rr,s+ss) for c,a,b,r,s in u for d,aa,bb,rr,ss in v) for v in obs] for u in obs]
  N,X,E,P,XE,X2=means;vh=P-E*E;vx=X2-X*X;corr=XE/X-E;D=F(4,8)*(V*N-E)/X
  psi=vec[0];rnum=F(0)
  for o in modes:
   op=[o[i]*psi[i] for i in range(864)]
   rnum+=F(sum(op[i]*(V*nf[i]*op[i]-sum(op[j] for j in adj[i])) for i in range(864)),32*z)-E*F(sum(v*v for v in op),32*z)
  R=rnum/X;req(R==D+corr);req(vh>=0 and vx>=0);req(corr*corr*X*X<=vh*vx)
  if V==1:req(E==P==XE==vh==corr==0 and D==R)
  row=dict(V=str(V),n=n,means=list(map(str,means)),cross=[[str(v) for v in rr] for rr in cross],VarH=str(vh),VarX=str(vx),correction=str(corr),D=str(D),R=str(R))
  with localcontext() as ctx:
   ctx.prec=24
   row['decimal']={key:str(Decimal(val.numerator)/Decimal(val.denominator)) for key,val in [('VarH',vh),('VarX',vx),('correction',corr),('D',D),('R',R),('E',E),('X',X)]}
  allrows.append(row)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);req(0<rss<384)
print(json.dumps(dict(checks=checks,states=864,directed_moves=sum(nf),variables=['NF','X1','Eavg','hLhR','X1Eavg','X1_squared'],rows=allrows,seconds=time.monotonic()-start,peak_MiB=rss),indent=2))
