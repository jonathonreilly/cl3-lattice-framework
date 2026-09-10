from fractions import Fraction as F
import json
from core import source_triple,cross,local_gamma
pairs=[((1,2),(3,4)),((1,2),(3,5)),((1,3),(5,6)),((1,3),(2,4)),((1,3),(2,5))]
roots=[F(1),F(2),F(3)];mu=sum(roots)/3
A=lambda s:sum(1/(x*x+s*s)for x in roots)/3
B=lambda s:sum(x/(x*x+s*s)for x in roots)/3
# Literal independent dense entry formula; no coefficient decomposition used.
def entry(i,j,s,sign,gamma):
 identity=int(i==j);op=int(i*j>0 and (i-1)//2==(j-1)//2 and i!=j);skew=(-(-1)**(j+1)if i==0<j else((-1)**(i+1)if j==0<i else0));a=A(s);b=B(s);d=(1-s*s*a)/6
 return (-b*identity-(1+s*s/6)*b*op+sign*s*b*skew/6)if gamma else(sign*s*(a*identity+(a-d)*op)+d*skew)
n=0;s,t=F(1),F(4)
for pa,pc in pairs:
 sources=[[1,0,0,0,0,0,0]]+[[0]+[int(j in p)*(-1)**(j+1)for j in range(1,7)]for p in [pa,pc]]
 for x in sources:
  for y in sources:
   d=source_triple(x,y)
   for sig in [-1,1]:
    for tau in [-1,1]:
     for gamma in [0,1]:
      dense=sum(x[i]*y[j]*(entry(i,j,t,tau,gamma)-entry(i,j,s,-sig,gamma))*(1 if gamma==0 else-1)/(sig*s+tau*t)for i in range(7)for j in range(7))
      assert dense==cross(s,sig,t,tau,A(s),B(s),A(t),B(t),gamma,d);n+=1
# Full local opposite-site Gamma overlap includes the non-cancelling constant.
x=[0,0,1,0,0,0,0];y=[0,1,0,0,0,0,0];d=source_triple(x,y)
for sig in [-1,1]:
 direct=sum(q*(1-q*q/6)/(q*q+s*s)for q in roots)/3
 assert local_gamma(s,sig,A(s),B(s),mu,d)==direct;n+=1
 assert direct!=(1+s*s/6)*B(s);n+=1
try:cross(s,1,s,-1,A(s),B(s),A(s),B(s),0,(1,0,0))
except ValueError:n+=1
else:raise AssertionError('confluence silently accepted')
print(json.dumps({'status':'PASS_SYNTHETIC_DENSE_EQUIVALENCE','checks':n,'native_values':0,'native_calls':0}))
