from pathlib import Path
import json,hashlib
w=Path('/private/tmp/toe-native-sixth-offdiagonal-sign-obstruction-20260908');b=Path('/private/tmp/toe-24h-probes-20260908');p=w/'.claude/science/physics-loops/native-sixth-offdiagonal-sign-obstruction-20260908';o=Path(__file__).parent;n=0
read=lambda p:json.loads(p.read_text())
def need(x,s):
 global n
 if not x:raise RuntimeError(s)
 n+=1
freeze=read(p/'SOURCE_FREEZE.json')
for f,h in freeze.items():need(hashlib.sha256((w/f).read_bytes()).hexdigest()==h,'freeze '+f)
a=read(w/'outputs/native_sixth_offdiagonal_sign_obstruction_2026_09_08.json');iso=json.loads((p/'ISOLATED.stdout').read_text())
for f,h in a['input_sha256'].items():need(hashlib.sha256((w/f).read_bytes()).hexdigest()==h,'input '+f)
refs={'coefficients':b/'native-full-sixth-offdiagonal/RESULT.json','normalization':b/'native-full-sixth-offdiagonal/NORMALIZATION_RESULT.json','l4':b/'native-sixth-sign-loop/RESULT.json','l6':b/'native-sixth-sign-loop/RESULT_L6.json'}
for kind,ref in refs.items():
 old=read(ref);cur=read(w/f'outputs/native_sixth_{kind}_2026_09_08.json')
 for key in old:
  if key in ('seconds','rss_mib'):continue
  need(old[key]==a['parts'][kind][key]==cur[key]==iso['parts'][kind][key],kind+key)
need(a['executed_predicates']==3682 and a['absolute_binding_predicates']==7,'count')
need(iso['input_sha256']==a['input_sha256'],'isolated final note binding')
for m in read(p/'MUTATIONS.json'):need(m['exit']!=0 and (p/(m['name']+'.stderr')).read_text().strip().endswith(m['failure']),m['name'])
(o/'RESULT.json').write_text(json.dumps({'checks':n,'scope':'source and recorded output replay; no physics rerun'},indent=2)+'\n')
files=[w/f for f in freeze]+[p/f for f in ['PORT_RECEIPT.json','ISOLATED_CLOSURE.json','ISOLATED.stdout','MUTATIONS.json','WRAPPER_CONTROLS.json','AUTHOR_VERIFICATION_DRIVER.py']]
(o/'READ_HASHES.json').write_text(json.dumps({str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in files},indent=2)+'\n');print(n)
