import pathlib,sys,hashlib,json,difflib
import reference,guarded,factory,checkpoint,measure,profile,run_profile,forecast,controls,finalize_outer
B=pathlib.Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
# Actual checkpoint reader exercised on the retained reduced fixture; no sampling.
checkpoint.load(factory.Geometry(2),B/'CONTROL_FILES'/'0',(2,4,0.))
parent=B.parent/'face-fiber-gibbs'
if sha(B/'reference.py')!=sha(parent/'core.py'):raise ValueError('reference changed')
(B/'NUMERIC_GUARD_DELTA.diff').write_text(''.join(difflib.unified_diff((B/'reference.py').read_text().splitlines(True),(B/'guarded.py').read_text().splitlines(True),fromfile='reference.py',tofile='guarded.py')))
l8=B.parent/'reptation-propagated-l8-design';f=json.loads((l8/'PRODUCTION_FREEZE.json').read_text())
for name,h in f.items():
 if sha(l8/name)!=h:raise ValueError('old L8 source changed '+name)
(B/'OLD_L8_UNCHANGED.json').write_text(json.dumps({'freeze':sha(l8/'PRODUCTION_FREEZE.json'),'entries_verified':len(f)},indent=2))
refs=[parent/'FINAL_FREEZE.json',parent/'core.py',B.parent/'face-fiber-gibbs-cold-review'/'REVIEW.md',B.parent/'face-fiber-diagnostic-design'/'DIAGNOSTIC_DESIGN.md']
(B/'SOURCE_BINDINGS.json').write_text(json.dumps({str(p):sha(p) for p in refs},indent=2))
paths={pathlib.Path(sys.executable).resolve()}
for m in list(sys.modules.values()):
 p=getattr(m,'__file__',None)
 if p and pathlib.Path(p).is_file():paths.add(pathlib.Path(p).resolve())
(B/'RUNTIME.json').write_text(json.dumps({'files':{str(p):sha(p) for p in sorted(paths)},'scope':'actual imported Python module/extension files and interpreter; no claim to freeze the OS'},indent=2))
files={str(p.relative_to(B)):sha(p) for p in sorted(B.rglob('*')) if p.is_file() and '__pycache__' not in str(p) and p!=B/'FINAL_FREEZE.json'}
(B/'FINAL_FREEZE.json').write_text(json.dumps({'files':files,'profile_launched':False},indent=2));print(sha(B/'FINAL_FREEZE.json'));print(len(paths))
