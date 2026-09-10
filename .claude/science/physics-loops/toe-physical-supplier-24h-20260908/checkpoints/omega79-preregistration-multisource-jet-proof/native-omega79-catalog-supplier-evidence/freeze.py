from pathlib import Path
import json,hashlib
S=Path('/private/tmp/toe-24h-probes-20260908');P=S/'native-omega79-catalog-supplier-design';O=S/'native-omega5-catalog-supplier-runtime-design';R=S/'native-omega5-root-review';OUT=S/'native-omega5-catalog-supplier-run-prospective'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb')as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def rec(p):return {'path':str(p),'sha256':sha(p)}
b=json.loads((O/'BINDING.json').read_text());b['status']='NOTREADY_NEW_OMEGA79';b['omega5']={k:rec(p)for k,p in {'acceptance':R/'ROOT_ACCEPTANCE.json','root':R/'ROOT_FREEZE.json','receipt':R/'RECEIPT.json','worker':OUT/'WORKER_COMPLETE.json','result':OUT/'RESULT.json','tail':OUT/'TAIL.json','binding':O/'BINDING.json'}.items()};b['omega5']['worker_freeze']=sha(O/'RUNTIME_FREEZE.json');(P/'BINDING.json').write_text(json.dumps(b,indent=2)+'\n')
f0=json.loads((O/'RUNTIME_FREEZE.json').read_text());inputs=dict(f0['inputs'])
for folder in [O,R,OUT,S/'native-gaussian-jet-degree-cold-review',S/'native-gaussian-moment-jet-cold-review']:
 for p in folder.rglob('*'):
  if p.is_file():inputs[str(p)]=sha(p)
for p in P.iterdir():
 if p.is_file()and p.name!='RUNTIME_FREEZE.json':inputs[str(p)]=sha(p)
f={'execution_enabled':False,'interpreter':f0['interpreter'],'membership':sorted([p.name for p in P.iterdir()if p.name!='RUNTIME_FREEZE.json']+['RUNTIME_FREEZE.json']),'inputs':dict(sorted(inputs.items())),'readiness_inputs':dict(sorted(inputs.items())),'source_only_no_scientific_values_loaded':True}
(P/'RUNTIME_FREEZE.json').write_text(json.dumps(f,indent=2)+'\n');print(json.dumps({'freeze':sha(P/'RUNTIME_FREEZE.json'),'binding':sha(P/'BINDING.json'),'proof':sha(P/'DERIVATION.md'),'pins':len(inputs),'interpreter':f['interpreter']}))
