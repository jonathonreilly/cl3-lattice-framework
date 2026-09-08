"""Synthetic arithmetic only: no profile or timing data."""
import json,math
from forecast import price
n=0
def need(c):
 global n
 n+=1
 if not c:raise ValueError('accounting predicate')
p=dict(accounted_case_seconds=8.,cases=[dict(base_16chain_16sweep_seconds_before_unallocated=100.),dict(base_16chain_16sweep_seconds_before_unallocated=200.)])
r=price(p,10.)
need(r['unallocated_profile_seconds']==2.)
need(r['cases'][0]['hypothetical_16chain_16sweep_seconds']==132.)
need(r['cases'][1]['hypothetical_16chain_16sweep_seconds']==232.)
need(all(x['unallocated_seconds_charged_per_hypothetical_chain']==2 for x in r['cases']))
need(price(p,8.)['unallocated_profile_seconds']==0.)
need(price(p,7.99)['unallocated_profile_seconds']==0.)
for t in [float('nan'),float('inf'),-1.,0.,7.]:
 try:price(p,t)
 except ValueError:need(True)
 else:need(False)
print(json.dumps(dict(checks=n,scope='synthetic formula controls only; no measured timing'),indent=2))
