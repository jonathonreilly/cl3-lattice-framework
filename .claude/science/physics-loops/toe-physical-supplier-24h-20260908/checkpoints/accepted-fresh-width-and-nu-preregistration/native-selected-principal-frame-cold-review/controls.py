from fractions import Fraction as F
import json
def mm(a,b):return [[sum(x*y for x,y in zip(r,c))for c in zip(*b)]for r in a]
def tr(a):return list(map(list,zip(*a)))
I=[[F(i==j)for j in range(4)]for i in range(4)];checks=0
for a in (F(-2),F(1,3),F(7)):
 for b in (F(1,10),F(2)):
  S=[[1,0,a,0],[0,1,0,a],[0,0,b,0],[0,0,0,b]];inv=[[1,0,-a/b,0],[0,1,0,-a/b],[0,0,1/b,0],[0,0,0,1/b]]
  for d in (F(-1,7),F(1,8)):
   U=[[1,d,0,0],[0,1,0,0],[0,0,1,d],[0,0,0,1]];ui=[[1,-d,0,0],[0,1,0,0],[0,0,1,-d],[0,0,0,1]];T=mm(inv,U);G=mm(tr(S),S);assert mm(mm(tr(T),G),T)==mm(tr(U),U);assert mm(mm(S,T),ui)==I;checks+=2
# Phi norm identity and safe rational bound for small symmetric fixtures.
for a,b,c in ((F(1),F(2),F(3)),(F(-2),F(1,7),F(0))):
 assert a*a/4+b*b+c*c/4<=(a*a+2*b*b+c*c)/2;checks+=1
assert 4*24**2==2304 and 5*2304==11520;checks+=1
print(json.dumps({'status':'PASS_EXACT_TRIANGULAR_GAUGE','checks':checks,'native_calls':0}))
