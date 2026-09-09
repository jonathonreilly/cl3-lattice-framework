from fractions import Fraction as F
from pathlib import Path
import types,sys,json,time,signal,resource
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('29s exact cap')));signal.alarm(29)
start=time.monotonic();checks=0
p=Path(__file__).parent/'lazy.py';m=types.ModuleType('reviewed_lazy');exec(compile(p.read_bytes(),str(p),'exec'),m.__dict__)
def ck(x):
 global checks
 if not x:raise ValueError('exact compression control')
 checks+=1

def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,c):return [[x*c for x in r] for r in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def structures(n):
 g=[[F(0)]*n for _ in range(n)];s=eye(n)
 for i in range(0,n,2):g[i+1][i]=1;g[i][i+1]=-1;s[i+1][i+1]=-1
 return g,s
Gm,Sm=structures(8);I=eye(8);Y=eye(8)
for i in range(8):Y[(i+2)%8][i]=F(i+1,13)
for r in Y:r.append(F(0))
Y[0][8]=1 # explicitly appended central synthetic insertion
eta=[(-1)**i for i in range(8)]+[1];G0=mm(tr(Y),Y);J0=mm(mm(tr(Y),Gm),Y)
history,diagonal=m.paired_steps([G0[i][i] for i in range(9)],lambda i:(G0[i],J0[i]),eta,4)
Pi=[[F(0)]*8 for _ in range(8)];adverse=0
for h in history:
 residual=mm(sub(I,Pi),Y);x=[[r[h['i']]] for r in residual];gx=mm(Gm,x);r=mm(tr(x),x)[0][0]
 ck(r==h['r']);pair=scale(add(mm(x,tr(x)),mm(gx,tr(gx))),1/r);Pi=add(Pi,pair)
 ck(mm(Pi,Pi)==Pi);ck(tr(Pi)==Pi);ck(mm(Pi,Gm)==mm(Gm,Pi));ck(mm(Pi,Sm)==mm(Sm,Pi))
 ry=mm(sub(I,Pi),Y);g=mm(tr(ry),ry);j=mm(mm(tr(ry),Gm),ry)
 ck([g[i][i] for i in range(9)]==h['diagonal_after']);ck(sum(g[i][i] for i in range(9))==h['trace_after'])
 prevg=mm(tr(residual),residual);prevj=mm(mm(tr(residual),Gm),residual)
 goodg=sub(prevg,scale(add(mm([[x] for x in h['g']],[h['g']]),mm([[x] for x in h['j']],[h['j']])),1/r))
 goodj=sub(prevj,scale(sub(mm([[x] for x in h['g']],[h['j']]),mm([[x] for x in h['j']],[h['g']])),1/r))
 ck(g==goodg);ck(j==goodj)
 badg=sub(prevg,scale(mm([[x] for x in h['g']],[h['g']]),1/r));badj=add(prevj,scale(sub(mm([[x] for x in h['g']],[h['j']]),mm([[x] for x in h['j']],[h['g']])),1/r))
 adverse+=int(badg!=g)+int(badj!=j)
 ck(mm(tr([[F(i==0)] for i in range(8)]),mm(sub(I,Pi),[[F(i==0)] for i in range(8)]))[0][0]==g[8][8])
ck(all(x==0 for x in diagonal));ck(adverse>0)
# Unsplit pair is not chiral invariant; blindly normalized quadruple is not a projection.
g,s=structures(4);x=[[F(2)],[F(0)],[F(0)],[F(1)]];gx=mm(g,x);sx=mm(s,x);gsx=mm(g,sx);r=F(5)
pair=scale(add(mm(x,tr(x)),mm(gx,tr(gx))),1/r)
ck(mm(pair,s)!=mm(s,pair))
quad=scale(add(add(mm(x,tr(x)),mm(gx,tr(gx))),add(mm(sx,tr(sx)),mm(gsx,tr(gsx)))),1/r)
ck(mm(quad,quad)!=quad)
pplus=scale(add(x,sx),F(1,2));pminus=scale(sub(x,sx),F(1,2));proper=[[F(0)]*4 for _ in range(4)]
for v in (pplus,pminus):
 gv=mm(g,v);rr=mm(tr(v),v)[0][0];proper=add(proper,scale(add(mm(v,tr(v)),mm(gv,tr(gv))),1/rr))
ck(proper==eye(4))
# Actual trace norm for diagonal weighted independent two-mode skew blocks.
w=[F(i+1,10) for i in range(8)];T=sum(x*x for x in w)
for removed in range(5):
 residual=sum(x*x for x in w[2*removed:])
 for c in ([F(1),F(-1,2),F(1,3),F(-1,4)],[F(-1,3),F(1,4),F(-1),F(1,2)]):
  norm=2*sum(abs(c[j]*w[2*j]*w[2*j+1]) for j in range(removed,4));ck(norm*norm<=4*T*residual)
# Explicit singular-Gram extension intertwines BOTH structures.
g6,s6=structures(6);g4,s4=structures(4);V=[r[:4] for r in eye(6)]
ck(mm(g6,V)==mm(V,g4));ck(mm(s6,V)==mm(V,s4))
ck(mm(tr(V),V)==eye(4))
d0=scale(eye(4),0);d1=scale(eye(4),0)
for i,v in enumerate([F(2),F(2),F(0),F(0)]):d0[i][i]=v
for i,v in enumerate([F(2),F(2),F(1,2),F(1,2)]):d1[i][i]=v
f0=mm(V,d0);f1=mm(V,d1);delta=sub(f1,f0)
ck(sum(x*x for row in delta for x in row)==F(1,2))
ck(sum(x*x for row in delta for x in row)<=2*4*F(1,8))
for f in (f0,f1):ck(mm(g6,f)==mm(f,g4));ck(mm(s6,f)==mm(f,s4))
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;ck(seconds<30 and rss<384*1048576)
print(json.dumps({'status':'PASS','predicates':checks,'paired_steps':len(history),'direct_wrong_update_discriminations':adverse,'seconds':seconds,'rss_bytes':rss,'physical_calls':0,'scope':'synthetic ambient projections, lazy row recurrence, chiral counterexample, two exact S1 block tests and simultaneous intertwiner'},indent=2))
