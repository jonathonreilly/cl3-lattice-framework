from pathlib import Path
from fractions import Fraction as F
import types,sys,json,hashlib
P=Path('/private/tmp/toe-24h-probes-20260908/native-minimal-first-action-append-design')
for name in ('interval','core'):
 m=types.ModuleType(name);sys.modules[name]=m;exec(compile((P/(name+'.py')).read_bytes(),str(P/(name+'.py')),'exec'),m.__dict__)
c=sys.modules['core'];iv=sys.modules['interval'];count=0
I=[[int(i==j) for j in range(7)] for i in range(7)];O=[[0]*7 for _ in range(7)];T=[[0]*7 for _ in range(7)]
for a,b in ((1,2),(3,4),(5,6)):O[a][b]=O[b][a]=1;T[0][a]=-1;T[a][0]=1;T[0][b]=1;T[b][0]=-1
N=[[I[i][j]+O[i][j] for j in range(7)] for i in range(7)]
def dot(u,M,v):return sum(u[i]*M[i][j]*v[j] for i in range(7) for j in range(7))
def ok(interval,x):
 global count
 if not interval[0]<=x*iv.S<=interval[1]:raise ValueError('containment')
 count+=1
for orbit,(aa,cc) in zip(c.ORBITS,(((1,2),(3,4)),((1,2),(3,5)),((1,3),(5,6)),((1,3),(2,4)),((1,3),(2,5)))):
 def d(ids):return [0]+[([1,-1,1,-1,1,-1][i-1] if i in ids else 0) for i in range(1,7)]
 old=[[1,0,0,0,0,0,0],d(aa),d(cc)];new=[d(aa),d(cc),d(range(1,7))]
 for k,u in enumerate(new):
  for v,x in enumerate(old):
   for sig in (-1,1):
    s=F(7,5);A=F(2,9);B=F(3,11);mu=F(12,5);D=(1-s*s*A)/6
    gm=[[sig*s*(A*N[i][j]-D*O[i][j])+D*T[i][j] for j in range(7)] for i in range(7)]
    jm=[[B*N[i][j]-(mu-s*s*B)*O[i][j]/6-sig*s*B*T[i][j]/6 for j in range(7)] for i in range(7)]
    g,j=c.cross(k,v,s,sig,A,B,mu,orbit,iv.rational(F(3,2)));ok(g,F(3,4)*dot(u,gm,x));ok(j,F(3,4)*dot(u,jm,x))
   g,j=c.insertion(k,v,F(2,5),mu,orbit);ok(g,0);ok(j,-mu*dot(u,T,x)/24 if v==0 else -F(2,5)*dot(u,N,x)/4+mu*dot(u,O,x)/24)
  for l,y in enumerate(new):
   g,j=c.self_entry(k,l,orbit);ok(g,F(dot(u,I,y),4));ok(j,0)
print(json.dumps({'status':'PASS','predicates':count,'native_inputs_loaded':False,'stream_calls':0,'method':'independent literal7x7 matrices; no core.bilinear or geometry'}))
