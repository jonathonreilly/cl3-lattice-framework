"""Validate saved exact basis; actual missing-vector containment mutant."""
from pathlib import Path
from fractions import Fraction as F
import json,signal,time,resource
signal.alarm(180);t=time.monotonic();p=Path(__file__).resolve().parent
r=json.loads((p/'RESULT.json').read_text());bases=json.loads((p/'BASES.json').read_text());out=[]
for c in r['cases']:
 b=bases[c['name']];support=c['endpoints']
 if any(sum((F(z['vector'][v]**2,z['norm_squared']) for z in b),F(0))!=1 for v in support):raise ValueError('retained containment')
 removed=next(i for i,z in enumerate(b) if any(z['vector'][v] for v in support));mut=b[:removed]+b[removed+1:]
 failed=[v for v in support if sum((F(z['vector'][v]**2,z['norm_squared']) for z in mut),F(0))!=1]
 if not failed:raise ValueError('actual omitted basis mutant survived')
 out.append(dict(case=c['name'],removed_basis_index=removed,failed_endpoints=failed))
print(json.dumps(dict(actual_missing_vector_mutants=out,seconds=time.monotonic()-t,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576),indent=2))
