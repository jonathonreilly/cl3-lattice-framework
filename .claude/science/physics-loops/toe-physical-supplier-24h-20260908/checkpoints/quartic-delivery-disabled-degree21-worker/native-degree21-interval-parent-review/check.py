import importlib.util,itertools,math,signal,json,resource
from fractions import Fraction as F
from pathlib import Path
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in()).throw(TimeoutError('10-second synthetic cap')));signal.alarm(10)
p=Path('/private/tmp/toe-24h-probes-20260908/native-degree21-independent-interval-core/core.py');s=importlib.util.spec_from_file_location('reviewed_core',p);C=importlib.util.module_from_spec(s);s.loader.exec_module(C)
mask=(2,2,1,1);zero=(0,)*4;keys=C.indices(mask)
X=[[0j,1+0j],[1+0j,0j]];Y=[[0j,-1j],[1j,0j]];I=[[1+0j,0j],[0j,1+0j]]
def mm(a,b):return[[sum(a[i][k]*b[k][j]for k in range(2))for j in range(2)]for i in range(2)]
def add(a,b):return[[a[i][j]+b[i][j]for j in range(2)]for i in range(2)]
def scale(a,z):return[[v*z for v in r]for r in a]
poly={zero:I}
for variable,A in enumerate([X,Y,X,Y]):
 factor={};power=I
 for n in range(mask[variable]+1):
  a=tuple(n if i==variable else 0 for i in range(4));factor[a]=scale(power,1/math.factorial(n));power=mm(power,A)
 nxt={}
 for a,M in poly.items():
  for b,N in factor.items():
   k=tuple(x+y for x,y in zip(a,b))
   if all(v<=cap for v,cap in zip(k,mask)):nxt[k]=add(nxt.get(k,[[0j]*2 for _ in range(2)]),mm(M,N))
 poly=nxt
# P=diag(1,0), so determinant(I+P(U-I))=U00. Exact dyadic coefficient sqrt uses Z^2=U00, independently of trace-log recurrence.
Z={zero:1+0j}
for a in keys[1:]:
 t=0j
 for b,z in Z.items():
  c=tuple(x-y for x,y in zip(a,b))
  if b!=zero and c!=zero and c in Z:t+=z*Z[c]
 Z[a]=(poly[a][0][0]-t)/2
J={1:{(i,j):C.c(v.real,v.imag)for i,r in enumerate(X)for j,v in enumerate(r)if v},2:{(i,j):C.c(v.real,v.imag)for i,r in enumerate(Y)for j,v in enumerate(r)if v}}
def box(q):
 x=C.c(q);return((x[0][0]-1,x[0][1]+1),(x[1][0]-1,x[1][1]+1))
def ordinary(n,i,j):return box(i==j)if n==0 else C.ZERO
def projected(n,i,j):return box(i==j==0)if n==0 else C.ZERO
out=C.reconstruct(mask,[(0,(1,),1),(1,(2,),1),(2,(1,),1),(3,(2,),1)],J,ordinary,projected)
for a,z in Z.items():
 v=out[a]
 assert F(v[0][0],C.GRID)<=F(z.real)<=F(v[0][1],C.GRID)
 assert F(v[1][0],C.GRID)<=F(z.imag)<=F(v[1][1],C.GRID)
assert Z[(1,1,0,0)]==.5j and Z[(2,2,0,0)]==3/16
assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<128*1048576
print(json.dumps({'status':'PASS_NONCOMMUTING_SYNTHETIC_ONLY','coefficients':len(Z),'rank_one_projected_fixture':True,'native_values':0,'independent_expected_path':'explicit ordered matrix product, determinant U00 and square-root convolution'}))
