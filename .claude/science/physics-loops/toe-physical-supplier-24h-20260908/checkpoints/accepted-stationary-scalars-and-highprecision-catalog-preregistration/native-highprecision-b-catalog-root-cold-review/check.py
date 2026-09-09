from pathlib import Path
import types,sys,json,hashlib,time,textwrap,math
P=Path('/private/tmp/toe-24h-probes-20260908/native-highprecision-b-catalog-design');R=P.parent/'native-highprecision-b-catalog-root-review';OUT=P.parent/'native-highprecision-b-catalog-root-cold-review/SYNTHETIC_OUTPUT'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def require(x,m):
 if not x:raise ValueError(m)
# Stub only the actual oracle; use unchanged actual pilot and actual geometry.
stub=types.ModuleType('elliptic');stub.oracle=lambda s:{'s':str(s),'A':['1','1'],'Aprime':['-1','-1'],'widths':['0','0'],'status':'CERTIFIED_TARGET','terms':160,'derivative_side':'ordinary'};sys.modules['elliptic']=stub
m=types.ModuleType('pilot');m.__file__=str(P/'pilot.py');exec(compile((P/'pilot.py').read_bytes(),m.__file__,'exec'),m.__dict__)
t=time.monotonic();m.run(OUT);elapsed=time.monotonic()-t
PF=sha(P/'FREEZE.json');(OUT/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE','freeze_sha256':PF,'result_sha256':sha(OUT/'RESULT.json'),'seconds':elapsed+1,'rss_bytes':1}))
s=(R/'run_once.py').read_text();start=s.index('  pins(); result=');end=s.index('\n  pins()\n  require(0<done',start);block=textwrap.dedent(s[start:end]).replace('pins(); result=','result=',1)
env=dict(P=P,O=OUT,PF=PF,sha=sha,json=json,math=math,Path=Path,require=require);exec(compile(block,'ACTUAL_ACCEPTANCE_BLOCK','exec'),env)
# Actual acceptance expression must reject missing raw seconds, preserving fixture.
f=OUT/'ORACLES/0000.json';raw=json.loads(f.read_text());saved=f.read_bytes();raw.pop('seconds');f.write_text(json.dumps(raw));result=json.loads((OUT/'RESULT.json').read_text());result['rows'][0]['sha256']=sha(f);orig=(OUT/'RESULT.json').read_bytes();(OUT/'RESULT.json').write_text(json.dumps(result));done=json.loads((OUT/'WORKER_COMPLETE.json').read_text());done['result_sha256']=sha(OUT/'RESULT.json');(OUT/'WORKER_COMPLETE.json').write_text(json.dumps(done))
failed=False
try:exec(compile(block,'MISSING_SECONDS_ADVERSE','exec'),env)
except (KeyError,ValueError):failed=True
require(failed,'missing seconds accepted');f.write_bytes(saved);(OUT/'RESULT.json').write_bytes(orig)
print(json.dumps({'status':'PASS_ACTUAL_PILOT_SYNTHETIC_SCHEMA','rows':3484,'oracle_calls':0,'actual_acceptance_source':sha(R/'run_once.py'),'actual_pilot_source':sha(P/'pilot.py'),'adverse_missing_seconds_rejected':True,'scope':'synthetic output only; worker completion is a fixture, not physical evidence'}))
