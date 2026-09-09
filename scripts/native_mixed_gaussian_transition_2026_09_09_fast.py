from fractions import Fraction as F
import json
q=F(9801,10000);g=1-q;n=0
def ck(x):
 global n
 if not x:raise ValueError('exact control')
 n+=1
ck(q**2048/g<F(1,10**15))
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]
I=[[F(1),F(0)],[F(0),F(1)]]
E=[[F(1,4),F(1,8)],[F(0),F(-1,4)]];P=E;S=I
for k in range(11):
 S=add(S,mm(P,S));P=mm(P,P)
 M=[[I[i][j]-E[i][j] for j in range(2)] for i in range(2)];MS=mm(M,S)
 ck(all(MS[i][j]==I[i][j]-P[i][j] for i in range(2) for j in range(2)))
ck(2**11==2048)
# Rational logarithm tail enclosure improves monotonically, no libm comparison.
z=F(1,3);prev=None
for m in (4,8,16,32):
 lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(m)),F(0));hi=lo+2*z**(2*m+1)/(F(2*m+1)*(1-z*z))
 if prev:ck(prev[0]<=lo<=hi<=prev[1])
 prev=(lo,hi)
print(json.dumps({'status':'PASS_SYNTHETIC_EXACT','predicates':n,'physical_calls':0,'doublings':11,'matrix_products':22}))
