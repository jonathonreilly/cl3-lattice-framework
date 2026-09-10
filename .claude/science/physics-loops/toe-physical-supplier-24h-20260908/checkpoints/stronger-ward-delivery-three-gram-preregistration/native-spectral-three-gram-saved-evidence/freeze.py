from pathlib import Path
import json,hashlib
S=Path('/private/tmp/toe-24h-probes-20260908');P=S/'native-spectral-three-gram-saved-design';O=S/'native-degree10-spectral-residual-design';R=S/'native-spectral-residual-root-review';OUT=S/'native-spectral-residual-run-prospective'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def rec(p):return {'path':str(p),'sha256':sha(p)}
b0=json.loads((O/'BINDING.json').read_text());a=json.loads((R/'ROOT_ACCEPTANCE.json').read_text());spec={'acceptance':rec(R/'ROOT_ACCEPTANCE.json'),'receipt':rec(R/'RECEIPT.json'),'root_freeze':rec(R/'ROOT_FREEZE.json'),'worker':rec(OUT/'WORKER_COMPLETE.json'),'result':rec(OUT/'RESULT.json'),'binding':rec(O/'BINDING.json'),'worker_freeze':a['worker_freeze']}
b={'status':'NOTREADY_NEW_SAVED_THREE_GRAM','degree10':b0['degree10'],'spectral':spec};(P/'BINDING.json').write_text(json.dumps(b,indent=2)+'\n')
f0=json.loads((O/'RUNTIME_FREEZE.json').read_text());inputs=dict(f0['inputs'])
for folder in [O,R]:
 for p in folder.iterdir():
  if p.is_file():inputs[str(p)]=sha(p)
for name,h in a['output_hashes'].items():
 p=OUT/name;assert sha(p)==h;inputs[str(p)]=h
for folder in [S/'native-ward-dual-residual-stretch',S/'native-dual-residual-cold-review']:
 for p in folder.iterdir():
  if p.is_file():inputs[str(p)]=sha(p)
for p in P.iterdir():
 if p.is_file()and p.name!='RUNTIME_FREEZE.json':inputs[str(p)]=sha(p)
f={'execution_enabled':False,'interpreter':f0['interpreter'],'membership':sorted([p.name for p in P.iterdir()if p.name!='RUNTIME_FREEZE.json']+['RUNTIME_FREEZE.json']),'inputs':dict(sorted(inputs.items())),'readiness_inputs':dict(sorted(inputs.items())),'source_only_no_saved_values_parsed':True}
(P/'RUNTIME_FREEZE.json').write_text(json.dumps(f,indent=2)+'\n');print(json.dumps({'freeze':sha(P/'RUNTIME_FREEZE.json'),'binding':sha(P/'BINDING.json'),'proof':sha(P/'DERIVATION.md'),'pins':len(inputs)}))
