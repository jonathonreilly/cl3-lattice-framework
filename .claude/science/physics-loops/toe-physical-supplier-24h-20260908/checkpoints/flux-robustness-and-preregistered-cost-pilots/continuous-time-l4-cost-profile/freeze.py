import sys,json,pathlib,hashlib,subprocess,signal,resource,time,random,os
import adapter,verified_path,geometry,geometry_reference,bridge,conditional,profile,forecast,preflight
B=pathlib.Path(__file__).resolve().parent;sha=preflight.sha
parent=B.parent/'continuous-time-l4-reference-adapter'
files={p.name:sha(p) for p in parent.iterdir() if p.is_file() and p.name in ['adapter.py','verified_path.py','geometry.py','geometry_reference.py','bridge.py','conditional.py']}
for name,h in files.items():
 if sha(B/name)!=h:raise ValueError('parent source changed')
refs={str(parent/name):h for name,h in files.items()}
for name in ['FREEZE.json','FINAL_FREEZE.json']:
 p=parent/name
 if p.exists():refs[str(p)]=sha(p)
(B/'SOURCE_BINDINGS.json').write_text(json.dumps(refs,indent=2)+'\n')
paths={pathlib.Path(sys.executable).resolve()}
for m in list(sys.modules.values()):
 p=getattr(m,'__file__',None)
 if p and pathlib.Path(p).is_file():paths.add(pathlib.Path(p).resolve())
(B/'RUNTIME.json').write_text(json.dumps(dict(files={str(p):sha(p) for p in sorted(paths)},scope='interpreter and loaded module files, not full system-library closure'),indent=2)+'\n')
(B/'FREEZE.json').write_text(json.dumps(dict(files={p.name:sha(p) for p in sorted(B.iterdir()) if p.is_file() and p.name!='FREEZE.json'},python_membership=sorted(p.name for p in B.glob('*.py')),launched=False),indent=2)+'\n')
print(sha(B/'FREEZE.json'))
