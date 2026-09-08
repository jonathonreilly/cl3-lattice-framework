from fractions import Fraction as F
import json
# Quadratic field Q(sqrt2); direct 2x2 inverse, independent of alpha polynomial.
def q(a,b=0):return(F(a),F(b))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def mul(a,b):return(a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def div(a,b):return mul(a,(b[0]/(b[0]**2-2*b[1]**2),-b[1]/(b[0]**2-2*b[1]**2)))
def inverse(A):
 d=add(mul(A[0][0],A[1][1]),neg(mul(A[0][1],A[1][0])));return [[div(A[1][1],d),div(neg(A[0][1]),d)],[div(neg(A[1][0]),d),div(A[0][0],d)]]
def mv(A,v):return [add(mul(r[0],v[0]),mul(r[1],v[1])) for r in A]
rows=[]
for x in [F(0),F(-6),F(1),F(2)]:
 E=[[q(x+F(1,3)),q(0,F(1,3))],[q(0,F(1,3)),q(x+F(5,3))]]
 O=[[q(x+F(2,3)),q(0,-F(1,3))],[q(0,-F(1,3)),q(x+F(4,3))]]
 v=mv(inverse(E),[q(1),q(0)])
 # Six disjoint pairs: perpendicular components sum to -3 times C's.
 post=[mul(q(6),v[0]),mul(q(-3),v[1])]
 z=mv(inverse(O),post);alpha=mul(q(F(15,8*24)),z[0]);formula=F(15)*(6*x*x+18*x+14)/(8*24*(x*x+2*x+F(1,3))*(x*x+2*x+F(2,3)))
 if alpha!=q(formula):raise ValueError('formula')
 rows.append({'x':str(x),'alpha':str(alpha[0])})
if rows[0]['alpha']!='315/64' or rows[1]['alpha']!='2745/172864':raise ValueError('absolute')
b=2*F(315,64)**2*2/24
if b!=F(33075,8192):raise ValueError('sixth normalization')
print(json.dumps({'status':'PASS','direct_two_mode_cases':rows,'singleton_coefficient':str(b)},indent=2))
