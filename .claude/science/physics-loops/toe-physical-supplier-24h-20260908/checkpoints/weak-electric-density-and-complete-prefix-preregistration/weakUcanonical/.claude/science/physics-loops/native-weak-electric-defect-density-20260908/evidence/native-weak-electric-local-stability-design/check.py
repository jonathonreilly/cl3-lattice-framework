from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
values=[]
for bits in product((0,1),repeat=6):
 z=[1-2*b for b in bits]
 d=(sum(bits)-3)**2
 expansion=F(3,2)+F(1,2)*sum(z[i]*z[j] for i in range(6) for j in range(i+1,6))
 if d!=expansion or not 0<=d<=9:raise ValueError('electric expansion')
 values.append(d)
if F(3,2)/F(3,800)!=400 or F(3)/F(3,800)!=800:raise ValueError('units')
# Wrong omitted constant is discriminated on every local state.
wrong=sum(F(d)!=F(d)-F(3,2) for d in values)
Path(__file__).with_name('RESULT.json').write_text(json.dumps({'local_states':64,'electric_min':min(values),'electric_max':max(values),'wrong_constant_mismatches':wrong,'ground_coefficient':400,'thermal_coefficient':800,'physical_solve':False},indent=2)+'\n')
