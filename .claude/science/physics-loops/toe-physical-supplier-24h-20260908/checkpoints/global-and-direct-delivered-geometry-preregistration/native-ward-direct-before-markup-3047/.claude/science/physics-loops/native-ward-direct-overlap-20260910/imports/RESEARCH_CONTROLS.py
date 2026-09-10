from fractions import Fraction as F
from itertools import combinations
import json
pairs=list(combinations(range(6),2));n=15
T=[[F(not(set(a)&set(b))) for b in pairs] for a in pairs]
B=[[F(i in a)-F(1,3) for i in range(6)] for a in pairs]
E0=[[F(1,15) for _ in pairs] for _ in pairs]
E1=[[sum(B[i][k]*B[j][k] for k in range(6))/4 for j in range(n)]for i in range(n)]
E2=[[F(i==j)-E0[i][j]-E1[i][j] for j in range(n)]for i in range(n)]
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B)))for j in range(len(B[0]))]for i in range(len(A))]
checks=0
def ok(x):
 global checks
 if not x:raise AssertionError('exact control')
 checks+=1
for E,rank,lam in zip((E0,E1,E2),(1,5,9),(6,-3,1)):
 ok(mul(E,E)==E);ok(sum(E[i][i] for i in range(n))==rank);ok(mul(T,E)==[[lam*v for v in r]for r in E])
for E,Fm in ((E0,E1),(E0,E2),(E1,E2)):ok(all(v==0 for row in mul(E,Fm)for v in row))
ok(sum(sum(row) for row in T)==90)
# Opposite labels=(0,1),(2,3),(4,5); all other labels perpendicular.
z=[[F(2 if a in ((0,1),(2,3),(4,5)) else 7)] for a in pairs]
ok(all(row==[0] for row in mul(E1,z)))
# Generic rational Hilbert-valued x,p: exact square completion, no native vectors.
x=[[F((i+2)*(j+1)%7-3) for j in range(3)]for i in range(n)]
p=[[F((i+3)*(j+4)%11-5,3) for j in range(3)]for i in range(n)]
y=[[x[i][j]-p[i][j]/2 for j in range(3)]for i in range(n)]
def dot(x,y):return sum(a*b for r,s in zip(x,y) for a,b in zip(r,s))
lhs=dot(x,mul(T,x))-dot(x,mul(T,p));rhs=sum(lam*(dot(mul(E,y),mul(E,y))-dot(mul(E,p),mul(E,p))/4)for E,lam in zip((E0,E1,E2),(6,-3,1)))
ok(lhs==rhs)
c=F(49,60);m=(26-4*c+c**3)/(26*c-4)
ok(m==F(5028049,3722400));ok(m>F(4,3));ok(135*m*m-180*m==F(326063949601,102638976000));ok(135*m*m-180*m>3)
ok(c*c>F(2,3));ok(26*F(1,4)-4>0);ok(24+2*c<26)
print(json.dumps({'status':'PASS','checks':checks,'scope':'finite pair-space identities, arbitrary synthetic vectors and rational moment bounds only','native_kernel_calls':0}))
