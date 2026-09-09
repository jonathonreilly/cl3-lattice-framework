from fractions import Fraction as F
import json
low=F(2,9)*F(5439,160)*F(1,2**48)+F(1,6)*F(867,32)*F(1,2**64)
high=F(1,8)*F(9,64)**15*(1+F(18,64*33))
quad=F(6139)*F(4,25)**21
assert F(3112000,507)<6139
assert low+high+quad<F(2,10**13)
assert 18*21==378 and 4*378+2+58==1572
print(json.dumps({'scope':'exact rational analytic budget only; no nodes or native data','low':str(low),'high':str(high),'quadrature':str(quad),'sum':str(low+high+quad),'sum_decimal_display':float(low+high+quad),'nodes':378,'rank_bound':1572},indent=2))
