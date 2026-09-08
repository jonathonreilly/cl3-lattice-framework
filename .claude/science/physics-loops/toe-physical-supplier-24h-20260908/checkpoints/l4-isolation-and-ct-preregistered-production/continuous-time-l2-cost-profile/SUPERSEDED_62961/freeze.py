import sys,json,hashlib,pathlib,random,signal,resource,time,tempfile,shutil,difflib
import runtime,conditional,bridge,geometry_reference,profile,forecast,preflight
B=pathlib.Path(__file__).resolve().parent
sha=preflight.sha
parent=B.parent/'continuous-time-l2-runtime'
(B/'RUNTIME_DELTA.diff').write_text(''.join(difflib.unified_diff((parent/'runtime.py').read_text().splitlines(True),(B/'runtime.py').read_text().splitlines(True),fromfile='frozen8d2/runtime.py',tofile='pinned/runtime.py')))
refs=[parent/'FINAL_FREEZE.json',B.parent/'continuous-time-l2-runtime-cold-review'/'REVIEW.md',runtime.ORACLE/'ORACLE.json',runtime.ORACLE/'BACKWARD_POWERS.json']
(B/'SOURCE_BINDINGS.json').write_text(json.dumps({str(p):sha(p) for p in refs},indent=2))
paths={pathlib.Path(sys.executable).resolve(),*(p.resolve() for p in refs[-2:])}
for m in list(sys.modules.values()):
 p=getattr(m,'__file__',None)
 if p and pathlib.Path(p).is_file():paths.add(pathlib.Path(p).resolve())
(B/'RUNTIME.json').write_text(json.dumps(dict(files={str(p):sha(p) for p in sorted(paths)},scope='loaded module files, interpreter and two external oracle files; OS/shared-library closure not claimed'),indent=2))
files={p.name:sha(p) for p in sorted(B.iterdir()) if p.is_file() and p.name!='FINAL_FREEZE.json'}
(B/'FINAL_FREEZE.json').write_text(json.dumps(dict(files=files,executable_membership=sorted(p.name for p in B.iterdir() if p.suffix in ('.py','.sh')),launched=False),indent=2))
print(sha(B/'FINAL_FREEZE.json'));print(len(paths))
