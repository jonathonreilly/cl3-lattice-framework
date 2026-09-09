from fractions import Fraction as F
from pathlib import Path
import json,hashlib,signal,time,resource
signal.alarm(30);start=time.monotonic();base=Path('/private/tmp/toe-24h-probes-20260908');o=base/'native-sharp-common-gram-run-a1558';dest=Path(__file__).parent;checks=0

def req(x,s):
 global checks
 if not x:raise ValueError(s)
 checks+=1
Q=1<<48
def rd(l,h):return F((l*Q).__floor__(),Q),F((h*Q).__ceil__(),Q)
def plus(a,b):return rd(a[0]+b[0],a[1]+b[1])
def neg(a):return -a[1],-a[0]
def minus(a,b):return plus(a,neg(b))
def times(a,b):
 z=[x*y for x in a for y in b];return rd(min(z),max(z))
def div(a,b):
 req(not b[0]<=0<=b[1],'positive divisor');return times(a,rd(1/b[1],1/b[0]))
def total(xs):
 v=(F(0),F(0))
 for x in xs:v=plus(v,x)
 return v
def pair(x):return tuple(map(F,x))
try:
 data=json.loads((o/'GRAM_INTERVALS.json').read_text());G=[[pair(x) for x in row] for row in data['G']];J=[[pair(x) for x in row] for row in data['J']];res=json.loads((o/'RESULT.json').read_text());done=json.loads((o/'WORKER_COMPLETE.json').read_text())
 req(hashlib.sha256((o/'RESULT.json').read_bytes()).hexdigest()=='d3244c6f39bc072fd108f48039c6a703952f97b5680cf0d17c70d5aab9348518','fixed result')
 req(done['result_sha256']==hashlib.sha256((o/'RESULT.json').read_bytes()).hexdigest(),'result pin')
 for M,skew in ((G,False),(J,True)):
  req(len(M)==28 and all(len(r)==28 for r in M),'size')
  for i in range(28):
   for j in range(28):req(M[i][j]==(neg(M[j][i]) if skew else M[j][i]),'symmetry')
 alg=json.loads((o/'ALGEBRA.json').read_text());nulls=[]
 for s,sign in ((1,-1),(2,1),(2,-1)):
  label={(1,-1):1,(2,1):2,(2,-1):3}[s,sign];v=[0]*28;v[7*label]=-sign*s;v[0]+=1
  for ax in range(3):v[7*label+1+2*ax]+=1;v[7*label+2+2*ax]-=1;v[1+2*ax]-=1;v[2+2*ax]+=1
  nulls.append(v)
 req(nulls==alg['null_relations'],'literal null vectors')
 for v in nulls:
  for M in (G,J):
   for row in M:
    z=total(times(x,(F(c),F(c))) for x,c in zip(row,v));req(z[0]<=0<=z[1],'null containment')
 initial=total(G[i][i] for i in range(28));req(initial==pair(res['initial_trace']),'initial trace')
 for step,row in enumerate(res['rows']):
  tr=total(G[i][i] for i in range(28));req(tr==pair(row['residual_trace']),'trace replay');req(4*initial[1]*tr[1]==F(row['error_squared_upper_for_coefficient_norm_le_one']),'error replay')
  if step==len(res['rows'])-1:
   req(4*initial[1]*tr[1]<=F(1,4),'conditional target');req(res['status']=='CERTIFIED_MODEST_CONDITIONAL_OPERATOR_ERROR','status');break
  index=max(range(28),key=lambda k:(G[k][k][0],-k));req(index==row['next_index'] and G[index][index]==pair(row['next_pivot']),'selected pivot')
  req(G[index][index][0]>0,'used positive pivot');g=G[index];j=J[index];pivot=G[index][index];A=[[None]*28 for _ in range(28)];B=[[None]*28 for _ in range(28)]
  for a in range(28):
   for b in range(a,28):
    A[a][b]=A[b][a]=minus(G[a][b],div(plus(times(g[a],g[b]),times(j[a],j[b])),pivot))
    B[a][b]=minus(J[a][b],div(minus(times(g[a],j[b]),times(j[a],g[b])),pivot)) if a!=b else (F(0),F(0));B[b][a]=neg(B[a][b])
  for a in range(28):A[index][a]=A[a][index]=B[index][a]=B[a][index]=(F(0),F(0))
  G,J=A,B
 out={'status':'PASS','checks':checks,'seconds':time.monotonic()-start,'rss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'physical_calls':0,'result_sha256':hashlib.sha256((o/'RESULT.json').read_bytes()).hexdigest(),'scientific_status':res['status'],'last_residual_upper':res['rows'][-1]['residual_trace'][1],'last_error_squared':res['rows'][-1]['error_squared_upper_for_coefficient_norm_le_one']}
 (dest/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
except BaseException as e:(dest/'FAILURE.json').write_text(json.dumps({'error':repr(e),'checks':checks})+'\n');raise
