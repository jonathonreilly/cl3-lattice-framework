from pathlib import Path
import types,json,tempfile,hashlib
b=Path('/private/tmp/toe-24h-probes-20260908/native-global-projector-coefficient-runtime-design')
e=b.with_name('native-global-projector-coefficient-runtime-evidence')
mods={}
for name in ('binder','worker'):
 m=types.ModuleType(name);m.__file__=str(b/(name+'.py'));exec(compile(Path(m.__file__).read_bytes(),m.__file__,'exec'),m.__dict__);mods[name]=m
n=0
def ok(x):
 global n
 if not x:raise AssertionError('synthetic control')
 n+=1
for x in (True,'01','1/0','2/2','1.0'):
 try:mods['binder'].scalar(x)
 except ValueError:ok(True)
 else:ok(False)
ok(str(mods['binder'].scalar('-2/3'))=='-2/3')
try:mods['binder'].load({'status':'PENDING'},lambda *a:None)
except ValueError:ok(True)
else:ok(False)
# Only one synthetic start event, then injected binder failure. No core imported/called.
out=Path(tempfile.mkdtemp(prefix='synthetic-',dir=e))
fake=types.SimpleNamespace(load=lambda *a:(_ for _ in ()).throw(ValueError('synthetic refused input')))
try:mods['worker'].run(out,{'identity':'SYNTHETIC'},None,fake,lambda:None)
except ValueError:ok(True)
else:ok(False)
fail=json.loads((out/'FAILURE.json').read_text());partial=json.loads((out/'PARTIAL.json').read_text());ev=[json.loads(l)for l in(out/'EVENTS.ndjson').read_text().splitlines()]
ok(fail['events']==partial['events']==1 and fail['coefficient_blocks']==0)
ok(ev==[{'seq':0,'stage':'start','payload':{'scope':'NEW_A_ONLY_PHYSICAL_COLUMN_COEFFICIENTS','acquisition_binding':'SYNTHETIC'}}])
print(json.dumps({'status':'PASS','checks':n,'native_oracle_calls':0,'accepted_loads':0,'coefficient_assemblies':0,'scope':'canonical parser, pending binder refusal and one-event failure retention'}))
