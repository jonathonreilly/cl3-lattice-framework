from fractions import Fraction as F
import json
low=F(357,25)*F(1,2**32)
quad=6139*F(4,25)**21
high=F(1,8)*F(9,64)*(1+F(18,320))
assert low+quad+high<F(19,1000)
e=F(8,10**6);b=1+e
metric=88*b*e/(1-e)
assert metric<F(71,100000)
assert 3*metric+F(1,10000)+F(1,100000)<F(224,100000)
remaining=F(11,500)-F(224,100000)-F(19,1000)
assert remaining>0 and remaining**2/2>F(1,10**9)
print(json.dumps({'status':'PASS','scope':'four exact source-budget checks only','checks':4,'tail_upper':str(low+quad+high),'metric_operator_upper':str(metric),'remaining_witness':str(remaining)}))
