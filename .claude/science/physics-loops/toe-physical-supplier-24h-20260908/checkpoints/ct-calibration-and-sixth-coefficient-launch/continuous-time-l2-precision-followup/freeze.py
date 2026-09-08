import pathlib,sys,json,hashlib,signal,subprocess,random,resource,tempfile,copy
import runtime,conditional,bridge,geometry_reference,config,preflight,producer,analyze,launch
B=pathlib.Path(__file__).resolve().parent;sha=preflight.sha
cost=B.parent/'continuous-time-l2-cost-profile'
for name in ('runtime.py','conditional.py','bridge.py','geometry_reference.py'):
 if sha(B/name)!=sha(cost/name):raise ValueError('reviewed runtime changed')
refs=[cost/'FINAL_FREEZE.json',B.parent/'continuous-time-l2-calibration/FINAL_FREEZE.json',B.parent/'continuous-time-l2-calibration-design/FINAL_FREEZE.json',runtime.ORACLE/'BACKWARD_POWERS.json',runtime.ORACLE/'ORACLE.json',runtime.ORACLE/'SUPPLEMENT_RESULT.json']
(B/'SOURCE_BINDINGS.json').write_text(json.dumps({str(p):sha(p) for p in refs},indent=2))
paths={pathlib.Path(sys.executable).resolve(),*(p.resolve() for p in refs[3:])}
for m in list(sys.modules.values()):
 p=getattr(m,'__file__',None)
 if p and pathlib.Path(p).is_file():paths.add(pathlib.Path(p).resolve())
(B/'RUNTIME.json').write_text(json.dumps(dict(files={str(p):sha(p) for p in sorted(paths)},scope='actual imported module/extension files plus interpreter and oracle inputs; OS not frozen'),indent=2))
files={p.name:sha(p) for p in sorted(B.iterdir()) if p.is_file() and p.name!='FINAL_FREEZE.json'}
(B/'FINAL_FREEZE.json').write_text(json.dumps(dict(files=files,python_membership=sorted(p.name for p in B.glob('*.py')),launched=False),indent=2))
print(sha(B/'FINAL_FREEZE.json'));print(len(paths))
