"""Tiny synthetic affine identities only; no native imports or data."""
from fractions import Fraction as F
import json
n=0
def check(x):
 global n
 if not x: raise AssertionError(n)
 n+=1
for b in (F(-3,2),F(0),F(7,3)):
 for old in (F(-2),F(1,7)):
  new=F(5,11);eta=F(1,100);a=F(3,13);rho=F(1,1000)
  lo=a+b*old-rho;hi=a+b*old+rho
  shift=b*(new-old);r=abs(b)*eta
  for x in (new-eta,new,new+eta):check(lo+shift-r<=a+b*x<=hi+shift+r)
# Changed midpoint invalidates naive shrink; overlap alone is not containment.
check(not -F(1,100)<=F(1)<=F(1,100))
check(max(F(0),F(1,2))<=min(F(1),F(3,2)) and not F(3,2)<=F(1))
# Coefficient interval and exact displacement, including negative displacement.
for delta in (F(-3),F(2)):
 B=(F(2),F(3));prod=sorted([x*delta for x in B]);eta=F(1,10)
 for b in (F(2),F(5,2),F(3)):
  for e in (-eta,eta):check(prod[0]-3*eta<=b*(delta+e)<=prod[1]+3*eta)
# Literal affine J formulas, independent symbolic substitution.
b=F(3,5);sig=-1;s=F(7,4);N=-2;O=-1;T=2;c=F(2,7);mu=F(8,3);B=F(1,6)
dc=F(1,101);dm=F(-1,103)
def ward(c):return b/F(2)*(B*F(T,6)+sig*((c-B)*N/s+s*B*F(O,6)))
def bare(mu):return b/F(2)*(B*N-(mu-s*s*B)*F(O,6)-sig*s*B*F(T,6))
check(ward(c+dc)-ward(c)==b*sig*N/(2*s)*dc)
check(bare(mu+dm)-bare(mu)==-b*O/F(12)*dm)
check((-N*(c+dc)/4+O*(mu+dm)/24)-(-N*c/4+O*mu/24)==-N*dc/4+O*dm/24)
check(5*104-15==505);check(5460*2*4*5==218400)
print(json.dumps({'status':'PASS_SYNTHETIC_AFFINE_CONTROLS','checks':n,'native_data_reads':0}))
