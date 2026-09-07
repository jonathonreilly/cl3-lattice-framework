from fractions import Fraction as F
from math import factorial
import json,hashlib
from pathlib import Path
checks=[]
def ck(name,ok):
 if name in checks or not ok:raise AssertionError(name)
 checks.append(name)
low2=F(4,35)**2*F(2,3)**5
ck('low radial integral ceiling squared',low2<F(1,24)**2)
ck('sqrt6 ceiling squared',6<F(5,2)**2)
ck('sqrt3 ceiling squared',3<F(7,4)**2)
exp6=sum(F(6)**j/factorial(j) for j in range(17))
ck('positive Taylor lower bound exp6',exp6>400)
moment=36*factorial(1)+15*factorial(2)+2*factorial(3)+F(1,12)*factorial(4)
ck('high polynomial moment',moment==80)
ck('high radial ceiling',F(20)*F(5,2)/400==F(1,8))
J=F(7,324)*(F(1,24)+F(1,8));mu=F(2,243)
ck('weighted trace ceiling',J==F(7,1944))
ck('Perron moment upper bound',-1+J/mu==F(-9,16))
ck('absolute insertion upper bound',F(-9,16)*mu==F(-1,216))
ck('pointwise polynomial minimum',F(7,2)*(F(7,2)-7)/4==F(-49,16))
print(json.dumps(dict(checks=checks,relative_lower_bound='-49/16',relative_upper_bound='-9/16',absolute_upper_bound='-1/216',exp6_partial_sum=str(exp6),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact scalar arithmetic supporting the analytical positive-operator/heat-kernel proof; no floating Perron data used'),indent=2,allow_nan=False))
