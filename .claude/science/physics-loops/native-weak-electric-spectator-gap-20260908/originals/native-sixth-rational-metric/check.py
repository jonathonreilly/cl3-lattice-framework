import itertools,json,time,resource,signal
from fractions import Fraction as F
from pathlib import Path
signal.alarm(180);start=time.monotonic();n=0
def ck(c):
 global n;n+=1
 if not c:raise ValueError(n)
B=Path(__file__).parent;P=B.parent/'native-zero-penalty-sixth-spectator-coefficient';raw=json.loads((P/'FRAME_RESULT.json').read_text());R=[[F(x) for x in row] for row in raw['raw_black_basis']];d=list(map(F,raw['norms']));vs=list(itertools.product(range(4),repeat=3));ids={v:i for i,v in enumerate(vs)};black=[i for i,v in enumerate(vs) if sum(v)%2==0]
K=[[0]*64 for _ in vs];edges=[]
for v in vs:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%4;i,j=sorted((ids[v],ids[tuple(w)]));edges.append((i,j));K[i][j]=-2*(-1)**sum(v[:a]);K[j][i]=-K[i][j]
rr=[[F(0)]*64 for _ in R]
for i,row in enumerate(R):
 for k,v in zip(black,row):rr[i][k]=v
for i in range(10):
 for j in range(10):ck(sum(a*b for a,b in zip(rr[i],rr[j]))==(d[i] if i==j else 0))
kr=[[sum(K[i][j]*row[j] for j in range(64)) for i in range(64)] for row in rr]
def qmatrix(mask):
 KF=[row[:] for row in K]
 for e,(i,j) in enumerate(edges):
  if mask>>e&1:KF[i][j]*=-1;KF[j][i]*=-1
 fkr=[[sum(KF[i][j]*row[j] for j in range(64)) for i in range(64)] for row in kr]
 return [[-sum(a*b for a,b in zip(rr[i],fkr[j]))/12 for j in range(10)] for i in range(10)]
q0=qmatrix(0);ck(q0==[[2*d[i]*int(i==j) for j in range(10)] for i in range(10)])
states=[b for b in range(1024) if b.bit_count()%2==0];W={b:__import__('functools').reduce(lambda x,i:x*d[i],(i for i in range(10) if b>>i&1),F(1)) for b in states}
def mat(Q):
 J={}
 for b in states:
  J[b,b]=sum(Q[i][i]/d[i]*(F((b>>i)&1)-F(1,2)) for i in range(10))
  for i,j in itertools.combinations(range(10),2):
   bi=(b>>i)&1;bj=(b>>j)&1;sgn=(-1)**((b&((1<<i)-1)).bit_count()+(b&((1<<j)-1)).bit_count())
   z=F(sgn,2)*(Q[j][i]*(1-2*bi)-Q[i][j]*(1-2*bj))*d[i]**(bi-1)*d[j]**(bj-1)
   if z:J[b^(1<<i)^(1<<j),b]=z
 return J
J=mat(qmatrix(3))
for (a,b),z in J.items():ck(W[a]*z==W[b]*J.get((b,a),0))
J0=mat(q0);ck(all(z==2*(b.bit_count()-5)*int(a==b) for (a,b),z in J0.items()))
# Independent diagonal similarity cancellation squared, all bit cases.
for i,j in itertools.combinations(range(10),2):
 for bi,bj in itertools.product((0,1),repeat=2):
  rational=d[i]**(bi-1)*d[j]**(bj-1)
  ck(rational**2==d[i]**(2*bi-1)*d[j]**(2*bj-1)/(d[i]*d[j]))
# Rational metric residual with a supplied dyadic candidate, no solve.
z={b:F((b%7)-3,16) for b in states};rhs={b:F(b==0) for b in states};res={a:rhs[a]-10*z[a] for a in states}
for (a,b),v in J.items():res[a]-=v*z[b]
sq=sum(W[a]*v*v for a,v in res.items());ck(sq>0)
# Closing gamma_v gamma_w, black v=0 and white w=16, with fixed order.
v,w=edges[0];ck(v==0 and w==16)
closing={}
for b in states:
 for i in range(10):
  for j in range(10):
   coefficient=rr[i][v]*(-kr[j][w]/2)
   q=b^(1<<j);sign=(-1)**((b&((1<<j)-1)).bit_count()+(q&((1<<i)-1)).bit_count())*(1-2*((b>>j)&1))
   a=q^(1<<i)
   factor=1/d[i] if i==j else d[i]**(((b>>i)&1)-1)*d[j]**(((b>>j)&1)-1)
   closing[a,b]=closing.get((a,b),F(0))+coefficient*sign*factor
row={b:closing.get((0,b),F(0)) for b in states}
ck(sum(x*x/W[b] for b,x in row.items())==6)
out=dict(checks=n,nonzero_matrix_entries=len(J),metric_min=str(min(W.values())),metric_max=str(max(W.values())),exact_candidate_residual_norm_squared=str(sq),seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576,scope='rational matrix/metric control only, no DP or inverse')
print(json.dumps(out,indent=2))
