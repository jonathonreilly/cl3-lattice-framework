"""Zero-Gram orchestration only: loader and table constructors explicitly stubbed."""
import sys,tempfile,json
from pathlib import Path
from fractions import Fraction as F
P=Path('/private/tmp/toe-24h-probes-20260908/native-degree21-retained-runtime-design');sys.path.insert(0,str(P))
import worker,loader,tables,arithmetic as a
rows={m:{'p':{k:[F(0)]*3 for k in('P','O')},'old_q':{k:F(0)for k in('P','O')},'s0_s2':{k:[a.ZERO]*3 for k in('P','O')},'first_squared':{k:F(0)for k in('P','O')},'a_squared':(F(0),F(0)),'old_alpha':(F(-1),F(1))}for m in('residual','variational')}
def fake(b,emit):
 for s in('before_bound_inputs','authenticated_same_trial_inputs','authenticated_degree21_inputs'):emit(s,{})
 return {n:a.ZERO for n in range(11)},rows
loader.load=fake;tables.inner=lambda *_:(lambda *_:a.ZERO,lambda *_:a.ZERO);tables.nominal=tables.inner
with tempfile.TemporaryDirectory()as d:
 out=Path(d);worker.run({},out);r=json.loads((out/'RESULT.json').read_text());ev=[json.loads(x)for x in(out/'EVENTS.ndjson').read_text().splitlines()];assert r['jets']==7 and len(ev)==2386 and len(list(out.iterdir()))==13;assert all(x['intersection']==['0','0']for x in r['rows']);assert len([x for x in ev if x['stage']=='jet_start'])==7
 print(json.dumps({'status':'PASS_SYNTHETIC_ORCHESTRATION_ONLY','events':len(ev),'worker_files':13,'with_dispatch_files':15,'native_values':0,'stubbed':['loader.load','tables.inner','tables.nominal'],'real_core':True,'real_assembly':True},indent=2))
