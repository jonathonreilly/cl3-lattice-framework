import arithmetic as a
from fractions import Fraction as F
checks=0
for x in (F(-7,3),F(0),F(2,5)):
 for y in (F(1,7),F(3)):
  for fun,v in ((a.times,x*y),(a.divide,x/y),(a.plus,x+y)):
   z=fun(a.q(x),a.q(y));assert F(z[0],a.S)<=v<=F(z[1],a.S);checks+=1
for x in (F(0),F(2),F(9,4)):
 z=a.root(a.q(x));assert F(z[0],a.S)**2<=x<=F(z[1],a.S)**2;checks+=1
v={(3,0):a.q(2),(4,1):a.q(-3)};assert a.gamma(a.gamma(v))=={k:a.minus(x) for k,x in v.items()};checks+=1
for f in (lambda:a.divide(a.q(1),a.q(0)),lambda:a.intersect(a.q(0),a.q(1))):
 try:f()
 except ValueError:checks+=1
 else:raise AssertionError('negative control')
print({'status':'PASS_TINY_RATIONAL_ONLY','checks':checks,'native_calls':0})
