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
for i in range(4):cases.append(dict(cid=i,T=(.5,.5,2.,2.)[i],start=('constant','bounded','constant','bounded')[i],seed=202609340001+i,initialization_seconds=.01,io_seconds=.01,synthetic_output_seconds=.02,synthetic_rows=128,synthetic_batches=16,measurement_seconds=[.004]*4,interval_seconds=[.02]*4,case_seconds=.13,blocks=[dict(face=0,seconds=.0001)]*384,measurements=[dict(x=1.)]*4))
r=dict(runtime_load_seconds=.1,cases=cases);q=forecast.calculate(r,1.)
ck(abs(q['unallocated_outer_seconds_charged_each_chain']-.42)<1e-12)
ck(abs(q['arms'][0]['four_chain_shard']-(4*(.04+144*.004+128*.004+.42)+.1))<1e-12)
a=json.loads(json.dumps(r));a['cases'][0]['interval_seconds'][0]=float('nan');rejects(lambda:forecast.calculate(a,1.))
a=json.loads(json.dumps(r));a['cases'][0]['blocks'].pop();rejects(lambda:forecast.calculate(a,1.))
a=json.loads(json.dumps(r));del a['cases'][0]['measurement_seconds'];
try:forecast.calculate(a,1.)
except KeyError:ck(True)
else:raise ValueError('missing measurement accepted')
a=json.loads(json.dumps(r));a['cases'][0]['synthetic_rows']=4;rejects(lambda:forecast.calculate(a,1.))
# Old cadence formula must differ from the correct positive-measurement forecast.
old=4*(.02+144*.005+.5)+.1
ck(q['arms'][0]['four_chain_shard']>old)
ck(q['arms'][0]['measurement_count']==128 and q['arms'][0]['synthetic_output_seconds']==.02)
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
# Actual formula mutants, isolated source executions; no sampling.
source=(B/'forecast.py').read_text().split("if __name__")[0]
for name,old,new in [('omit_measurement','+128*measurement','+0*measurement'),('omit_serialization',"+c['synthetic_output_seconds']+(burn",'+0+(burn')]:
 changed=source.replace(old,new)
 if changed==source:raise ValueError('mutant target missing')
 ns={'__name__':'isolated_mutant'};exec(compile(changed,name,'exec'),ns)
 wrong=ns['calculate'](r,1.)
 ck(abs(wrong['arms'][0]['four_chain_shard']-q['arms'][0]['four_chain_shard'])>1e-8)
 (B/(name+'_mutant.py')).write_text(changed)
 (B/(name+'_RESULT.json')).write_text(json.dumps(dict(correct=q['arms'][0]['four_chain_shard'],mutant=wrong['arms'][0]['four_chain_shard'],expected_equality=False)))
print(json.dumps(dict(checks=N,scope='deterministic preflight/accounting only; no profile'),indent=2))
