import sys,json
sys.dont_write_bytecode=True
from fractions import Fraction as F
from math import factorial
import independent as I
count=0
intervals=[(a,b)for a in range(-3,4)for b in range(a,4)]
for a in intervals:
 for b in intervals:
  x=I.times(a,b);v=[p*q for p in a for q in b];assert x==(min(v)//I.Q,I.ceildiv(max(v),I.Q));count+=1
D={j:[[I.Z,I.Z],[I.Z,I.Z]]for j in range(9)};B={j:[[I.Z,I.Z],[I.Z,I.Z]]for j in range(9)};D[0]=[[I.point(1),I.Z],[I.Z,I.point(1)]];B[0]=[[I.point(1),I.Z],[I.Z,I.Z]]
# Independent scalar square-root convolution: Z²=cosh(2t).
z={0:F(1)}
for n in range(1,11):
 c=F(2**n,factorial(n))if n%2==0 else F(0);z[n]=(c-sum(z[k]*z[n-k]for k in range(1,n)))/2
accepted={n:I.point(((-1)**n*factorial(n)*z[n]).numerator,((-1)**n*factorial(n)*z[n]).denominator)for n in range(7)}
e=[];logs=I.high_logs(D,B,lambda s,v:e.append((s,v)));new=I.scalar_high(accepted,logs,lambda s,v:e.append((s,v)))
for n,v in new.items():
 truth=(-1)**n*factorial(n)*z[n];assert F(v[0][0],I.Q)<=truth<=F(v[0][1],I.Q);count+=1
print(json.dumps({'status':'PASS','predicates':count,'synthetic_stages':len(e),'native_values':0}))
