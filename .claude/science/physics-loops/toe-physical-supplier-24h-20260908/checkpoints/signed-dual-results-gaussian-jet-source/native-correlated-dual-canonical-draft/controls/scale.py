# Exact synthetic checks only, no native data or implementation imports.
from fractions import Fraction as F
import json
add=lambda a,b:[x+y for x,y in zip(a,b)]
sc=lambda c,a:[c*x for x in a]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
mv=lambda M,a:[dot(row,a)for row in M]
H=[[F(2),F(1)],[F(1),F(3)]];J=[[F(0),F(2)],[F(-2),F(0)]]
U=[F(2),F(-1)];W=[F(3),F(1)];t=F(2,5);s=F(3,7);r=[F(1),F(2)];q=[F(-1),F(3)]
y=sc(s,add(W,sc(-t,mv(J,U))));z=sc(-t,U);c0=dot(r,W);c1=dot(r,mv(J,U));c2=dot(q,U);count=0
for l in map(F,[0,F(1,2),1,F(3,2),2]):
 a=add(add(W,sc(-l,mv(H,y))),sc(l,mv(J,z)));b=add(sc(-1,U),sc(-l,mv(H,z)))
 vs=[W,mv(H,W),mv(J,U),mv(H,mv(J,U))];co=[1,-l*s,-l*t,l*s*t]
 assert a==[sum(co[j]*vs[j][i]for j in range(4))for i in range(2)];count+=1
 assert b==add(sc(-1,U),sc(l*t,mv(H,U)));count+=1
 assert l*(dot(r,y)+dot(q,z))==l*(s*c0-s*t*c1-t*c2);count+=1
 G=[[dot(v,w)for w in vs]for v in vs];assert dot(a,a)==sum(co[i]*co[j]*G[i][j]for i in range(4)for j in range(4));count+=1
 if l not in [0,1]:
  wrong=[1,-l*s,-l*t,l*l*s*t];assert a!=[sum(wrong[j]*vs[j][i]for j in range(4))for i in range(2)];count+=1
assert 13*15*5*2==1950 and 3*15*5*2==450;count+=1
print(json.dumps({'checks':count,'status':'PASS','native_values':0}))
