from fractions import Fraction as F
import json
n=0;d=F(1,4)
for t in map(F,[1,2,4,8,16]):
 A=(t+2*d)/(d*d*t**3);B=-2/t**3-2*t*A;C=3/t**2+t*t*A
 for x in [d,F(1,2),t,F(19)]:
  left=A*x*x+B*x+C-1/(x*x);right=(x-d)*(x-t)**2*((t+2*d)*x+d*t)/(d*d*t**3*x*x)
  assert left==right and left>=0;n+=1
 # Independent single atom first/inner residual contractions.
 p0,p1,q=F(2,3),F(-1,5),F(1,7);x=F(3,2);c=[F(1),-p0,-p1]
 for j in range(3):
  rho=sum(c[i]*c[k]*x**(i+k+j)for i in range(3)for k in range(3));assert rho==(1-x*(p0+p1*x))**2*x**j;n+=1
  xi=x**j-2*q*x**(j+1)+q*q*x**(j+2);assert xi==(1-q*x)**2*x**j;n+=1
 # Negative coefficient upper direction: a spurious upper rho1 produces smaller bound.
 assert B<0 and B*F(2)<B*F(1);n+=1
print(json.dumps({'checks':n,'status':'PASS_EXACT_SYNTHETIC','native_values':0}))
