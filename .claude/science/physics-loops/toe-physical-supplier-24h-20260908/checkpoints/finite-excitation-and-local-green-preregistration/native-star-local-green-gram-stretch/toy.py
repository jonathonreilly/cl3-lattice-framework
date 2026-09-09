"""Exact non-integrating normalization controls only."""
from fractions import Fraction as F
import json
from core import roots,down,up,sin_bounds,atan_bounds,ranges_a,ranges_b

def run():
 checks=0
 def req(ok,msg):
  nonlocal checks
  if not ok:raise ValueError(msg)
  checks+=1
 for x in [F(0),F(1),F(2),F(9,4),F(17,31)]:
  a,b=roots(x);req(a*a<=x<=b*b,'root enclosure');req(b-a<=F(1,2**80),'root width')
 for x in [F(1,3),F(-1,3),F(2**43+1,2**44)]:req(down(x)<=x<=up(x),'directed round')
 lo,hi=sin_bounds(F(1,3));req(lo<=F(1,2)<=hi,'sine pi/6 normalization')
 x=F(1,5);twice=2*x/(1-x*x);four=2*twice/(1-twice*twice);req((four-F(1,239))/(1+four/F(239))==1,'Machin tangent')
 a=ranges_a(F(1,2),F(1,4),F(1,4));req(a[0][0]<=F(2,3)<=a[0][1],'A exact square');req(a[1][0]<=F(-20,27)<=a[1][1],'A derivative factor')
 b=ranges_b(F(2),F(1),F(1));req(b[0][0]<=F(1,5)<=b[0][1],'B normalization');req(b[1][0]<=F(-4,25)<=b[1][1],'B derivative')
 b=ranges_b(F(1),F(0),F(4));req(b[0][1]>=F(1,2),'interior B maximum')
 # Independent exact spectral divided difference, including negative-band restriction.
 for lam in [-3,-1,2,4]:
  r5=F(1,lam-5);r6=F(1,lam-6);req(r5*r6==(r5-r6)/F(5-6),'resolvent difference')
  req((int(lam<0)*r5)*r6==int(lam<0)*(r5-r6)/F(5-6),'projected difference')
 return {'status':'PASS','checks':checks,'physical_integrals':0}
if __name__=='__main__':print(json.dumps(run(),indent=2))
