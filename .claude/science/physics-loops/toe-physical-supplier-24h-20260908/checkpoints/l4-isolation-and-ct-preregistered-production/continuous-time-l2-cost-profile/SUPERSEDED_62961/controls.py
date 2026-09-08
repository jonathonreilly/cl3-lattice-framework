import json,tempfile,shutil,time,hashlib
from pathlib import Path
import runtime,forecast,preflight
B=Path(__file__).parent;N=0
def ck(c):
 global N;N+=1
 if not c:raise ValueError(N)
def rejects(f):
 try:f()
 except (ValueError,FileNotFoundError):ck(True)
 else:raise ValueError('mutant accepted')
for name in ('conditional.py','bridge.py','geometry_reference.py'):
 ck((B/name).read_bytes()==(B.parent/'continuous-time-l2-runtime'/name).read_bytes())
with tempfile.TemporaryDirectory() as z:
 p=Path(z);(p/'BACKWARD_POWERS.json').write_text('not json');rejects(lambda:runtime.Runtime(p))
cases=[]
for i in range(4):cases.append(dict(cid=i,T=(.5,.5,2.,2.)[i],start=('constant','bounded','constant','bounded')[i],seed=202609340001+i,initialization_seconds=.01,io_seconds=.01,interval_seconds=[.02]*4,case_seconds=.11,blocks=[dict(face=0,seconds=.0001)]*384,measurements=[dict(x=1.)]*4))
r=dict(runtime_load_seconds=.1,cases=cases);q=forecast.calculate(r,1.)
ck(abs(q['unallocated_outer_seconds_charged_each_chain']-.5)<1e-12)
ck(abs(q['arms'][0]['four_chain_shard']-(4*(.02+144*.005+.5)+.1))<1e-12)
a=json.loads(json.dumps(r));a['cases'][0]['interval_seconds'][0]=float('nan');rejects(lambda:forecast.calculate(a,1.))
a=json.loads(json.dumps(r));a['cases'][0]['blocks'].pop();rejects(lambda:forecast.calculate(a,1.))
# Full membership and file-pin mutants in isolated source copies, not author inputs.
with tempfile.TemporaryDirectory() as z:
 p=Path(z)
 for f in B.glob('*'):
  if f.is_file():shutil.copyfile(f,p/f.name)
 # A synthetic manifest tests exact implementation; runtime closure is empty here.
 (p/'RUNTIME.json').write_text('{"files":{}}')
 manifest=dict(files={'runtime.py':preflight.sha(p/'runtime.py')},executable_membership=sorted(f.name for f in p.iterdir() if f.suffix in ('.py','.sh')))
 (p/'FINAL_FREEZE.json').write_text(json.dumps(manifest));preflight.verify(p);ck(True)
 (p/'extra.py').write_text('');rejects(lambda:preflight.verify(p));(p/'extra.py').unlink()
 (p/'runtime.py').write_text('changed');rejects(lambda:preflight.verify(p))
print(json.dumps(dict(checks=N,scope='deterministic preflight/accounting only; no profile'),indent=2))
