from fractions import Fraction as F
from math import factorial
import json
b=F(2048);t=F(1,2);alpha=F(23,72)*t
low=F(1,10)*(6*t/(810*alpha**4)+24*t*t/(2592*alpha**5))
exp21=sum(F(64,3)**j/factorial(j) for j in range(81))
exp32=sum(F(32)**j/factorial(j) for j in range(81))
exact_tail=b*b*F(48,10)/10**9
approx_tail=b*b*F(6,10)*(F(7,6)+b/144+2/b)/10**12
checks={'prefactor_pi22over7':F(22,7)**2<F(32,3),'low_lt_14over5':low<F(14,5),'exp64over3_gt_billion':exp21>10**9,'exp32_gt_trillion':exp32>10**12,'exact_tail_lt_21over1000':exact_tail<F(21,1000),'approx_tail_lt_1over1000':approx_tail<F(1,1000),'total_lt3':F(14,5)+F(21,1000)+F(1,1000)<3,'reflection_constant':6*3==18,'cut_inside_torus':F(2,3)<9,'tail_monotonic_threshold':b>288}
assert all(checks.values())
print(json.dumps({'checks':checks,'low_bound':str(low),'exact_tail_bound':str(exact_tail),'approx_tail_bound':str(approx_tail),'beta0':2048,'uniform_reflected_constant':18},indent=2))
