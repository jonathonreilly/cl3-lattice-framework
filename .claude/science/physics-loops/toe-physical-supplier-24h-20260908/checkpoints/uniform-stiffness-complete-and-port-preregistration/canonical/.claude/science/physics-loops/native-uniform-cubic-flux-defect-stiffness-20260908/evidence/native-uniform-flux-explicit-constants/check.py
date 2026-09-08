from fractions import Fraction as F
import json,math
from pathlib import Path
# Deterministic rational checks, independent of any density data.
loss=F(4*3*10,8*32**2)+F(4*7,10*200)
assert F(3,50)-loss >= F(3,100)
target=48**24*31*4096
lower=sum((F(105**k,math.factorial(k)) for k in range(201)),F(0))
assert lower>target
# Wrong factor: dropping native auxiliary half doubles the advertised coefficient.
assert F(3,100)/8==F(3,800)
assert 2*14000*F(3,800)==105
out={'conditional_only':True,'density_premise_not_tested':True,'thermal_lower':str(F(3,50)-loss),'claimed_lower':'3/100','native_coefficient_over_h':'3/800','exp105_taylor_terms':201,'exp105_lower_numerator':str(lower.numerator),'exp105_lower_denominator':str(lower.denominator),'target':str(target),'exp_bound_pass':lower>target}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if 'numerator' not in k and 'denominator' not in k}))
