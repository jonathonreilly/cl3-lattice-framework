from fractions import Fraction as F
import json
checks=0
for X in(F(1),F(3),F(12)):
 for t in(F(1,2),F(8)):
  for k in(0,1):
   for n in(2,4):
    part=sum(((-1)**j*X**(j+k)/t**(2*j+2)for j in range(n)),F(0));rem=X**(n+k)/(t**(2*n)*(X+t*t));assert part+rem==X**k/(X+t*t)and rem>=0;checks+=1
 # Synthetic monotone Lipschitz A(t)=1/(X+t²), L=3 valid X>=1.
 eps=F(1,16);node=F(3,32);low=eps/(X+node*node);high=eps*(1/(X+node*node)+3*node)
 assert low<=eps/(X+eps*eps)<=eps/X<=high;checks+=1
assert F(16,3)*8*F(17,60)==F(544,45);checks+=1
assert F(16,3)*8==F(128,3);checks+=1
assert 1742*7+134+40<12500;checks+=1
print(json.dumps({'status':'PASS_TINY_ALTERNATIVE_IDENTITIES','checks':checks,'catalog_calls':0,'moment41_calls':0}))
