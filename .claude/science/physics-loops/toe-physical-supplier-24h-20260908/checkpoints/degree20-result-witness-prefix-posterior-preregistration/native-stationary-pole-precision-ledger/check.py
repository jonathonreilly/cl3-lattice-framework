from pathlib import Path
from fractions import Fraction as F
import json
r=json.loads(Path('/private/tmp/toe-24h-probes-20260908/native-stationary-pole-scalar-batch-design/POLES.json').read_text())['rows']
lo=[F(x['s_interval'][0]) for x in r];hi=[F(x['s_interval'][1]) for x in r]
k=lambda s:4*(1+s*s/6+s/6)
d=lambda s:4*(s/3+F(1,6))
b=max(k(s)+d(s) for s in hi);checks=0
for i in range(66):
 for j in range(66):
  b=max(b,(k(hi[i])+k(hi[j]))/(lo[i]+lo[j]));checks+=1
  if i!=j:
   den=max(lo[i]-hi[j],lo[j]-hi[i])
   if den<=0:raise ValueError('stationary pole collision')
   b=max(b,(k(hi[i])+k(hi[j]))/den);checks+=1
c=F(35,6)*max(F(x['weight'][1]) for x in r);a=c*264*b
limit=min(F(1,10**6)/1056,F(9,10**6)/(4*318*1056))/a
if not F(1,10**19)<limit:raise ValueError('B sufficient radius')
analytic=F(2,3)*(2*F(400,27)*F(4,25)**26+F(1,3*2**64)+F(12**26,53*8**53))
if not analytic<F(2,10**19):raise ValueError('proposed analytic budget')
checks+=2
print(json.dumps({'scope':'geometry and error-bound arithmetic only; no physical integrals','predicates':checks,'entry_multiplier_upper':str(b),'Cmax_upper':str(c),'Gram_error_multiplier':str(a),'sufficient_eta_upper':str(limit),'sufficient_eta_decimal':float(limit),'proposed_p26_analytic_width':str(analytic),'proposed_p26_analytic_width_decimal':float(analytic),'proposed_catalog_calls':3484,'forecast_seconds':10+3*3484*.01228104199981317},indent=2))
