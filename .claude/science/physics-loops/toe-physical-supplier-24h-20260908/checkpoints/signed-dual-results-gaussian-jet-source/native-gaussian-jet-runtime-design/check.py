"""Independent exact2x2 relative determinant coefficients; no native moments."""
from fractions import Fraction as F
import core as C
import json
from math import factorial
z=(F(0),F(0));one=(F(1),F(0))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scale(a,b):return a[0]*b,a[1]*b
def mm(a,b):return[[add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j]))for j in range(2)]for i in range(2)]
def ma(a,b,sign=1):return[[add(a[i][j],scale(b[i][j],sign))for j in range(2)]for i in range(2)]
def ms(a,k):return[[scale(x,k)for x in row]for row in a]
H=[[(F(-1),F(0)),z],[z,(F(2),F(0))]];V=[[z,(F(0),F(2))],[(F(0),F(-2)),z]];HA=ma(H,V);U=[[[one,z],[z,one]]]
for n in range(10):U.append(ms(ma(mm(H,U[-1]),mm(U[-1],HA),-1),F(1,n+1)))
# det(I-P+PU)=U00; solve Z²=U00 directly, bypassing log/finite-rank code.
Z=[F(1)]
for n in range(1,11):
 assert U[n][0][0][1]==0
 Z.append((U[n][0][0][0]-sum(Z[k]*Z[n-k]for k in range(1,n)))/2)
queries=[]
def D(j,a,b):
 assert 0<=j<=8;queries.append(('D',j));return C.point((-1 if a==0 else 2)**j if a==b else 0)
def B(j,a,b):
 assert 0<=j<=8;queries.append(('B',j));return C.point((-1)**j if a==b==0 else 0)
ell,counters=C.logjet(10,D,B);boxes=C.scalar_exp(ell,10);checks=0
for n,v in enumerate(Z):assert F(boxes[n][0][0],C.S)<=v<=F(boxes[n][0][1],C.S);assert boxes[n][1][0]<=0<=boxes[n][1][1];checks+=1
low={n:C.point(v.numerator,v.denominator)for n,v in enumerate(Z[:7])};hi,c2=C.logjet(10,D,B,first_order=7);assert set(hi)=={7,8,9,10};joined={**C.lower_logs(low),**hi};got=C.scalar_exp(joined,10,low)
for n in range(7,11):assert F(got[n][0][0],C.S)<=Z[n]<=F(got[n][0][1],C.S);checks+=1
accepted={}
for n in range(7):
 v=(-1)**n*factorial(n)*Z[n];accepted[n]=C.point(v.numerator,v.denominator)
new=C.high_moments(hi,accepted)
for n in range(7,11):
 v=(-1)**n*factorial(n)*Z[n];assert F(new[n][0][0],C.S)<=v<=F(new[n][0][1],C.S);checks+=1
for fn in [lambda:C.logjet(11,D,B),lambda:C.bounded(1<<4096),lambda:C.logjet(10,D,B,first_order=6)]:
 try:fn()
 except C.Refused:checks+=1
 else:raise AssertionError('missing cap')
assert max(j for _,j in queries)==8;checks+=1
print(json.dumps({'status':'PASS','checks':checks,'native_values':False,'direct_finite_dimension':2,'order':10,'max_source_power':8,'complex_operation_counters':counters,'interval_widths_claimed':False},indent=2))
