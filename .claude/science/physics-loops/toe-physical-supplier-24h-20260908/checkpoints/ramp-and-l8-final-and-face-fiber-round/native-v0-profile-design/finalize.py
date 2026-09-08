import pathlib,json,hashlib,sys,importlib.util
import numpy as np
import profile as actual_profile
P=pathlib.Path(__file__).parent;B=P.parent
# Explicit old initializer finite equality, without importing its old local core implicitly.
spec=importlib.util.spec_from_file_location('oldcore',B/'native-v0-stage0/CORE_V095_ORIGINAL.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
g=dict(np=np,Path=old.Path,legal=old.legal,count=old.count,next_count=old.next_count);source=(P/'INITIALIZE_V095_ORIGINAL.py').read_text().replace('from core import Path,legal,count,next_count','');exec(compile(source,'preserved-old-initialize','exec'),g)
from initialize import initialize
for L in (2,4):
 a,im=initialize(L,24,np.random.default_rng(12345),.95,2);b,bm=g['initialize'](L,24,np.random.default_rng(12345),2)
 if not np.array_equal(a.labels,b.labels) or any(not np.array_equal(x,y) for x,y in zip(a.states,b.states)) or a.nf!=b.nf or any(not np.array_equal(x,y) for x,y in zip(a.O,b.O)):raise RuntimeError('old .95 initializer')
# Bind current running L8 closure, without modifying it.
live=B/'reptation-propagated-l8-design';f=json.loads((live/'PRODUCTION_FREEZE.json').read_text())
for n,h in f.items():
 if hashlib.sha256((live/n).read_bytes()).hexdigest()!=h:raise RuntimeError('live L8 changed '+n)
(P/'LIVE_V095_UNCHANGED.json').write_text(json.dumps(dict(freeze_sha=hashlib.sha256((live/'PRODUCTION_FREEZE.json').read_bytes()).hexdigest(),verified_entries=len(f),old_initializer_fixed_fixtures=2,scope='read-only hash verification; no L8 runtime mutation'),indent=2)+'\n')
import run_profile,forecast
from checkpoint import save,load
r=np.random.default_rng(321);save(P/"RUNTIME_CLOSURE_CHECKPOINT.npz",a,r,4,dict(stage="dependency closure only"));load(P/"RUNTIME_CLOSURE_CHECKPOINT.npz",expected=dict(L=4,n=24,V=.95))
files={}
for m in list(sys.modules.values()):
 q=getattr(m,'__file__',None)
 if q and pathlib.Path(q).is_file():files[str(pathlib.Path(q).resolve())]=hashlib.sha256(pathlib.Path(q).read_bytes()).hexdigest()
files[str(pathlib.Path(sys.executable).resolve())]=hashlib.sha256(pathlib.Path(sys.executable).resolve().read_bytes()).hexdigest()
(P/'RUNTIME.json').write_text(json.dumps(dict(python=sys.version,files=files,scope='actual imported/interpreter files; OS frameworks supplied; profile not executed'),indent=2)+'\n')
source_names=['core.py','observables.py','initialize.py','checkpoint.py','profile.py','run_profile.py','forecast.py','PROTOCOL.md','RUNTIME.json']
(P/'FINAL_FREEZE.json').write_text(json.dumps({n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in source_names},indent=2)+'\n');print(hashlib.sha256((P/'FINAL_FREEZE.json').read_bytes()).hexdigest())
