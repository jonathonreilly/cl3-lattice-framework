from fractions import Fraction as F
from math import factorial
import json
q0=F(2,3)
low_squared=(F(4,35)**2)*q0**5
moment=sum(c*factorial(k) for k,c in [(1,F(36)),(2,F(15)),(3,F(2)),(4,F(1,12))])
taylor=sum(F(6)**k/factorial(k) for k in range(17))
checks={'low':low_squared<F(1,24)**2,'moment':moment==80,'exp6':taylor>400,'trace':F(7,324)*(F(1,24)+F(1,8))==F(7,1944),'ratio':-1+F(7,1944)/F(2,243)==F(-9,16),'absolute':F(-9,16)*F(2,243)==F(-1,216),'trial_coefficient':F(1,16)*F(1,27)*F(2,3)**4*18==F(2,243)}
assert all(checks.values())
print(json.dumps({'checks':checks,'exp6_partial_sum':str(taylor),'low_squared':str(low_squared)},indent=2))
