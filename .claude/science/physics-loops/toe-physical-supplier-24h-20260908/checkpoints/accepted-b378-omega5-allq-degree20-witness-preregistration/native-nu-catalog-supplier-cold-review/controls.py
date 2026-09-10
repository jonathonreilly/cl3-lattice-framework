from fractions import Fraction as F
from math import factorial,comb
import json
checks=0
def req(x):
 global checks
 if not x:raise ValueError('independent budget predicate')
 checks+=1
# Separate multinomial enumeration: only small exact moments, no catalog.
for k,expected in [(0,1),(1,6),(2,42),(3,324)]:
 v=sum(F(factorial(k),factorial(a)*factorial(b)*factorial(k-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(k-a-b),k-a-b) for a in range(k+1) for b in range(k-a+1))
 req(v==expected)
req(F(3,2)**2-F(17,16)**2-F(15,16)**2==F(31,128))
# Geometric expansion identities at rational toy X,t. Not physical data.
for x in [F(0),F(1,3),F(12)]:
 t=F(8);partial=sum((-1)**n*x**(n+2)/t**(2*n+2) for n in range(40));req(x*x/(x+t*t)-partial==x**42/(t**80*(x+t*t)))
quad=F(4)*8*6*F(1,4**52)/F(3,4)
req(quad==256*F(1,4**52))
node=4096*F(3,10**30)+600*F(1,2**140)
mid=9*node+1742*7*F(1,10**38)+F(1,10**45)
high=F(12**42,81*8**81);low=F(17,300*2**320)
width=F(100,157)*(2*quad+mid+high+low)+F(1,10**35)
req(node<F(2,10**26));req(mid<F(2,10**25));req(width<F(2,10**19));req(width<F(71,10**27))
# Reuse ellipse constants.
req(F(16,3)*8*F(17,60)==F(544,45));req(F(16,3)*8==F(128,3));req(F(16,3)*8*3==128)
print(json.dumps({'status':'PASS','checks':checks,'nu_full_width_upper':str(width),'scope':'exact tiny algebra and predata rational budgets; no catalog or oracle'},indent=2))
