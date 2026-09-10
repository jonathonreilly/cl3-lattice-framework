"""Exact synthetic cone/polynomial constants, no native inputs."""
from fractions import Fraction as F
import json
n=0
def check(v):
 global n
 if not v:raise ValueError(n)
 n+=1
c,A,B=F(3,2),F(13,10),F(6,5);d=c*c-A*A
check(c-A==F(1,5));check(d==F(14,25));check(B*B/d==F(18,7));check((1-F(18,7))/(1+F(18,7))==F(-11,25))
for u in(F(-1),F(-13,15),F(-1,2),F(0),F(1,2),F(1)):
 x=c+A*u;v2=B*B*(1-u*u)
 check(x*x-d*(1-u*u)==(A+c*u)**2);check(v2<=F(18,7)*x*x)
for X in(F(0),F(1,3),F(2)):
 for r in(F(0),F(11,25),F(3)):
  left=X*X+r*r-F(22,25)*X*r
  check(left==(r-F(11,25)*X)**2+F(504,625)*X*X);check(left>=F(16,25)*X*X)
check(F(504,625)>=F(64,81)) # optional tighter rational9/8 majorant
for M,R in[(F(17,48),F(85,6)),(F(5,4),F(50)),(F(15,2),F(300)),(F(15,4),F(150))]:check(40*M==R)
ratio=F(64,75)*F(5,4)**52;check(ratio>90000)
print(json.dumps({'status':'PASS_EXACT_SYNTHETIC_CONSTANTS','checks':n,'catalog_loads':0,'node_loads':0,'scalar_output_loads':0}))
