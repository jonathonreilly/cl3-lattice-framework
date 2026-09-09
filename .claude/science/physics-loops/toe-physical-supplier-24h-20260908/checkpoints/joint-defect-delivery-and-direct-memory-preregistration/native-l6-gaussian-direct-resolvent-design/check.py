from fractions import Fraction as F
from pathlib import Path
import json,hashlib
N=4
I=[[F(i==j) for j in range(N)] for i in range(N)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def tr(a):return list(map(list,zip(*a)))
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,c):return [[c*x for x in r] for r in a]
def car(j,B=False):
 a=[[F(0)]*N for _ in range(N)]
 for n in range(N):a[n^(1<<j)][n]=F((-1)**((n&((1<<j)-1)).bit_count())*((2*((n>>j)&1)-1) if B else 1))
 return a
A=[car(j) for j in range(2)];B=[car(j,True) for j in range(2)];checks=0
for generators,sg in [(A,-1),(B,1)]:
 W=add(scale(I,F(3,5)),scale(mm(*generators),F(4,5)))
 want=add(scale(generators[0],F(-7,25)),scale(generators[1],sg*F(24,25)))
 if mm(mm(W,generators[0]),tr(W))!=want:raise ValueError('conjugation sign')
 if mm(W,tr(W))!=I:raise ValueError('orthogonal')
 checks+=2
WA=add(scale(I,F(3,5)),scale(mm(*A),F(4,5)));WB=add(scale(I,F(5,13)),scale(mm(*B),F(12,13)));W=mm(WA,WB)
sigma=[F(2),F(-3)];c=F(7);Hd=scale(I,c)
for j in range(2):Hd=add(Hd,scale(mm(B[j],A[j]),-sigma[j]/2))
Hp=scale(I,c)
for j in range(2):Hp=add(Hp,scale(mm(mm(mm(W,B[j]),tr(W)),mm(mm(W,A[j]),tr(W))),-sigma[j]/2))
if Hp!=mm(mm(W,Hd),tr(W)):raise ValueError('signed spectrum similarity')
checks+=1
for n in range(N):
 want=c-sum(sigma)/2+sum(sigma[j] for j in range(2) if n>>j&1)
 if Hd[n][n]!=want:raise ValueError('offset')
 checks+=1
p=Path(__file__).parent;(p/'CONTROL.json').write_text(json.dumps({'status':'PASS','exact_fraction_predicates':checks,'modes':2,'physical_arrays':0,'non_dyadic_rational_rotations':True},indent=2)+'\n');print(checks)
