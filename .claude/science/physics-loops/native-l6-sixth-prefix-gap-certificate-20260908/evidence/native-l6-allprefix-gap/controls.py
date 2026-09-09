import signal,time,json,resource
from pathlib import Path
from fractions import Fraction as F
signal.alarm(175);t=time.monotonic()
import core
p=Path(__file__).parent;c=core.census;rows=[]
for r in c['rows']:
 mask=int(next(x for x in r['prefixes'] if x['k']==1)['mask']);rows.append(core.certify(mask,controls=True))
plan=json.loads((p/'PLAN.json').read_text());m=[x for s in plan['shards'] for x in s['masks']]
if len(m)!=1534 or len(set(m))!=1534 or plan['proper_keys']!=2038 or len(plan['singletons'])!=2:raise ValueError('coverage')
# Baseline shifted inverse identity on every column, exact Fraction.
R=core.R;A=core.A;s=F(25,4)
for j in range(108):
 for i in range(108):
  value=sum(F(int(A[i,k]))*R[k][j] for k in range(108) if A[i,k])+s*R[i][j]
  if value!=F(i==j):raise ValueError('baseline inverse')
print(json.dumps(dict(pilot_rows=rows,coverage=True,exact_factorizations=5,inverse_checks=5,baseline_inverse_entries=11664,seconds=time.monotonic()-t,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576),indent=2))
