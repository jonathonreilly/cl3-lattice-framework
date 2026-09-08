from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import runpy,json
B=Path(__file__).parent.parent/'native-3d-certified-grid-production';a=runpy.run_path(str(B/'aggregate.py'));trig=json.loads((B/'TRIG_INPUTS.json').read_text());cubes=json.loads((B/'CUBE_INPUTS.json').read_text());n=0
def ck(x):
 global n;n+=1
 if not x:raise ValueError(n)
seen=Counter((rep,i,j,k) for rep in (0,1,3,5,10,15) for block in range(4) for i in range(block*4,block*4+4) for j,k in product(range(16),repeat=2));ck(len(seen)==24576);ck(set(seen.values())=={1})
# Nonzero widths and a failed sign catch endpoint reversal/forced positivity.
d={r:(F(-2)+F(r,100),F(-2)+F(r,100)+F(1,10000)) for r in (0,1,3,5,10,15)};v=a['comparison'](d,cubes,trig);pi=F(trig['pi_upper_numerator'],trig['pi_denominator']);err=F(3,8192)*pi*pi
for c in v['costs']:
 r=c['rep'];m=cubes['rows'][r]['defects'];lo=d[r][0]-d[15][1]-err;hi=d[r][1]-d[15][0]+err
 ck(F(c['density_lower'])==lo);ck(F(c['density_upper'])==hi);ck(F(c['limiting_delta_lower'])==8*lo/m);ck(F(c['auxiliary_defect_coefficient_lower'])==2*lo/m);ck(F(c['native_half_objective_defect_coefficient_lower'])==lo/m);ck(c['strictly_positive']==(lo>0))
ck(v['all_five_positive'] is False);ck(F(v['common_density_lower'])==min(F(c['density_lower']) for c in v['costs']))
print(json.dumps({'checks':n,'scope':'independent full membership and rational interval/error/normalization/negative sign; no spectra'}))
