from pathlib import Path
import json,hashlib
S=Path('/private/tmp/toe-24h-probes-20260908');P=S/'native-coarse-witness-continuation-design';O=S/'native-coarse-occupied-witness-runtime-design';R=S/'native-coarse-witness-root-review'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
f=json.loads((O/'FREEZE.json').read_text());a=json.loads((R/'FAILED_ACCEPTANCE.json').read_text());b=json.loads((O/'BINDING.json').read_text())
b['prefix']={'receipt':{'path':str(R/'FAILED_ACCEPTANCE.json'),'sha256':sha(R/'FAILED_ACCEPTANCE.json')},'worker_freeze':a['worker_freeze'],'root_freeze':a['root_freeze'],'output':str(S/'native-coarse-witness-run-prospective'),'outputs':a['outputs']}
(P/'BINDING.json').write_text(json.dumps(b,indent=2)+'\n')
inputs=dict(f['inputs'])
for x in (O/'FREEZE.json',R/'ROOT_FREEZE.json',R/'FAILED_ACCEPTANCE.json'):inputs[str(x)]=sha(x)
for name,h in a['outputs'].items():
 x=S/'native-coarse-witness-run-prospective'/name;assert sha(x)==h;inputs[str(x)]=h
Q=S/'native-witness-three-coefficient-stretch'
for x in Q.iterdir():
 if x.is_file():inputs[str(x)]=sha(x)
for x in P.iterdir():
 if x.is_file() and x.name!='FREEZE.json':inputs[str(x)]=sha(x)
f={'status':'NOT_READY_REVIEW_AND_PREREGISTRATION','interpreter':f['interpreter'],'membership':sorted(x.name for x in P.iterdir()if x.is_dir()or x.suffix in('.py','.pyc','.so','.dylib')),'inputs':dict(sorted(inputs.items())),'physical_calls_during_preparation':0}
(P/'FREEZE.json').write_text(json.dumps(f,indent=2)+'\n')
print(json.dumps({'freeze':sha(P/'FREEZE.json'),'pins':len(inputs)}))
