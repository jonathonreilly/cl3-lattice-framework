# Finite artificial rational matrices only; no accepted inputs.
from fractions import Fraction as F
from math import factorial
import json
import core as C
n=4;zero=C.ZERO
J1={(0,0):C.c(2),(0,1):C.c(0,2),(1,0):C.c(0,-2)}
J2={(2,2):C.c(4),(0,2):C.c(0,2),(2,0):C.c(0,-2)}
J3={(3,3):C.c(-2),(0,3):C.c(-2),(3,0):C.c(-2)}
D=lambda power,i,j:C.c(int(power==0 and i==j))
# Four sources/four variables, noncommuting artificial Hermitian defects, h=0,P=I.
factors=[(0,(0,),1),(1,(0,),1),(2,(0,),1),(0,(0,2),-1),(2,(0,3),-1),(3,(1,),2),(1,(0,1),-1)]
Z=C.reconstruct((1,1,1,1),factors,{1:J1,2:J2,3:J3},D,D)
# det product exponential identity => branch-one square root exp(-2t-s+z+2w).
checks=0
for alpha,v in Z.items():
 expected=F(1)
 for k,x in zip(alpha,[-2,-1,1,2]):expected*=F(x**k,factorial(k))
 assert v==C.c(expected);checks+=1
# Literal center-reflection coefficient test with imaginary h*a column.
def mm(a,b):return [[sumc([C.mul(a[i][k],b[k][j])for k in range(len(b))])for j in range(len(b[0]))]for i in range(len(a))]
def sumc(v):
 z=zero
 for w in v:z=C.add(z,w)
 return z
def adj(a):return [[(a[j][i][0],-a[j][i][1])for j in range(len(a))]for i in range(len(a[0]))]
h=[[zero for _ in range(4)]for _ in range(4)]
for i,j,v in [(0,1,1),(1,0,-1),(2,3,2),(3,2,-2)]:h[i][j]=C.c(0,v)
a=[C.c(1),zero,zero,zero];d=[zero,C.c(1),C.c(1),zero];e=[zero,C.c(1),C.c(-1),zero];ha=[h[i][0]for i in range(4)];bank=[list(x)for x in zip(a,d,e,ha)]
j=[[zero for _ in range(4)]for _ in range(4)]
for (i,k),v in {(0,1):C.c(0,-2),(1,0):C.c(0,2),(0,3):C.c(-2),(3,0):C.c(-2)}.items():j[i][k]=v
actual=mm(mm(bank,j),adj(bank));v=[[C.scale(C.add(C.mul(a[i],d[k]),C.scale(C.mul(d[i],a[k]),-1)),F(2))for k in range(4)]for i in range(4)]
v=[[( -z[1],z[0])for z in row]for row in v]
R=[[C.c((-1 if i==0 else 1)if i==k else 0)for k in range(4)]for i in range(4)]
full=[[C.add(h[i][k],v[i][k])for k in range(4)]for i in range(4)];ref=mm(mm(R,full),R)
for i in range(4):
 for k in range(4):assert actual[i][k]==C.add(ref[i][k],C.scale(h[i][k],-1));checks+=1
j[0][3]=C.c(2);assert mm(mm(bank,j),adj(bank))!=actual;checks+=1
print(json.dumps({'status':'PASS_EXACT_SYNTHETIC','checks':checks,'native_inputs':0,'native_jets':0,'mask_tested':[1,1,1,1]}))
