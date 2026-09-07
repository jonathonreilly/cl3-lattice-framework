from fractions import Fraction as F
from math import factorial
import json
n=30
exp5upper=sum(F(5)**j/factorial(j) for j in range(n+1))+(F(5)**(n+1)/factorial(n+1))/(1-F(5,n+2))
b=F(1,10**12);lower=F(1,12**5*81);perturb=3*149*24*b
checks={'exp5upper':exp5upper<149,'small_exponent':12*b<F(1,2),'perturbation_constant':perturb==F(10728,10**12),'strict_margin':lower>perturb,'fundamental_dimension_power':3**4==81}
assert all(checks.values())
print(json.dumps({'checks':checks,'offdiagonal_realpart_lower':str(lower-perturb),'temporal_coupling':str(b),'spatial_coupling':1},indent=2))
