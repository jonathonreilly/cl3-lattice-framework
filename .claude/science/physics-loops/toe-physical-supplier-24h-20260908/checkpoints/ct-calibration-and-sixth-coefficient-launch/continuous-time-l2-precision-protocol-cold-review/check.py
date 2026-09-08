import json,hashlib,sys,math
from pathlib import Path
B=Path('/private/tmp/toe-24h-probes-20260908/continuous-time-l2-precision-followup'); O=Path(__file__).resolve().parent
sys.dont_write_bytecode=True;sys.path.insert(0,str(B));import analyze,config
n=0
def ck(x):
 global n;n+=1
 if not x:raise ValueError(n)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
f=json.loads((B/'FINAL_FREEZE.json').read_text())
for p,h in f['files'].items():ck(sha(B/p)==h)
for p,h in json.loads((B/'RUNTIME.json').read_text())['files'].items():ck(sha(Path(p))==h)
for p,h in json.loads((B/'SOURCE_BINDINGS.json').read_text()).items():ck(sha(Path(p))==h)
for name in ('runtime.py','conditional.py','bridge.py','geometry_reference.py'):ck((B/name).read_bytes()==(B.parent/'continuous-time-l2-calibration'/name).read_bytes())
F=json.loads((B/'FORECAST.json').read_text());groups=[]
for a in range(4):
 rows=[r for r in F['all_32_input_timings'] if r['arm']//2==a];ck(len(rows)==8)
 vals=[r['seconds']*320/(128+(16 if r['arm']%2==0 else 64)) for r in rows]
 for r,v in zip(rows,vals):ck(abs(r['scaled']-v)<1e-12)
 groups.append(1.5*max(vals)+2)
ck(abs(sum(groups)*16+30+180.930914-F['forecast_total_seconds'])<1e-10)
ck(max(groups)==F['forecast_max_shard_seconds'])
# Rank-one synthetic chain variation gives analytic covariance; no sampler invocation.
m=[10.,2.,5.,-.5,.3,-.8,10.,.2,4.,1.,.1,.1];v=[.01*(j+1) for j in range(12)]
rows=[[x+(i-31.5)*y for x,y in zip(m,v)] for i in range(64)];s=analyze.stats(rows)
var=64*65/12
for i in range(12):
 for j in range(12):ck(abs(s['mean_covariance'][i][j]-var*v[i]*v[j]/64)<1e-12)
for j,g in enumerate(analyze.gradients(m)):
 z=sum(x*y for x,y in zip(g,v));ck(abs(s['derived_covariance'][j][j]-var*z*z/64)<1e-12)
ck(len({config.seed(a,c) for a in range(4) for c in range(64)})==256)
ck(not {config.seed(a,c) for a in range(4) for c in range(64)} & {202609350000+1000*a+c for a in range(8) for c in range(16)})
result=dict(checks=n,freeze=sha(B/'FINAL_FREEZE.json'),forecast=F['forecast_total_seconds'],max_shard=max(groups),scope='deterministic hash, covariance, seed and price checks; no sampling')
(O/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(O/'READ_HASHES.json').write_text(json.dumps({str(B/p):sha(B/p) for p in f['files']},indent=2)+'\n');print(json.dumps(result))
