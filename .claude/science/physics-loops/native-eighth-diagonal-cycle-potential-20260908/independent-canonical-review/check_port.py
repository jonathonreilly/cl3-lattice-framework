from pathlib import Path
import json,hashlib,difflib
w=Path('/private/tmp/toe-native-eighth-diagonal-cycle-potential-20260908'); p=w/'.claude/science/physics-loops/native-eighth-diagonal-cycle-potential-20260908'; out=Path(__file__).parent
checks=[]
def req(x,s):
 if not x: raise RuntimeError(s)
 checks.append(s)
def read(p): return json.loads(p.read_text())
freeze=read(p/'SOURCE_FREEZE.json')
for n,h in freeze.items():req(hashlib.sha256((w/n).read_bytes()).hexdigest()==h,'freeze '+n)
a=read(w/'outputs/native_eighth_diagonal_cycle_potential_2026_09_08.json');iso=json.loads((p/'ISOLATED.stdout').read_text())
for n,h in a['input_sha256'].items():req(hashlib.sha256((w/n).read_bytes()).hexdigest()==h,'input '+n)
keys={'local':['rows','checks'],'global':['results','checks'],'combined':['scalar_parts','C_tree','W','decomposition','checks'],'witness':['results','checks']}
orig={'local':'native-full-eighth-diagonal','global':'native-eighth-global-reduction-root','combined':'native-eighth-combined','witness':'native-eighth-global-witness'}
for k,ks in keys.items():
 old=read(p/'originals'/orig[k]/'RESULT.json'); live=read(w/f'outputs/native_eighth_{k}_2026_09_08.json')
 for key in ks:
  req(old[key]==a['parts'][k][key]==iso['parts'][k][key]==live[key],k+' preserved '+key)
 s=p/'originals'/orig[k]/'check.py';t=w/f'scripts/native_eighth_{k}_2026_09_08.py'
 if s.exists():(out/f'{k}.diff').write_text(''.join(difflib.unified_diff(s.read_text().splitlines(True),t.read_text().splitlines(True))))
req(a['executed_predicates']==542264,'total');req(a['absolute_binding_predicates']==7,'absolute bindings')
req(a['parts']['combined']['input_sha256']==hashlib.sha256((w/'outputs/native_eighth_local_2026_09_08.json').read_bytes()).hexdigest(),'fresh local hash')
for m in read(p/'MUTATIONS.json'):
 req(m['exit_code']!=0 and (p/(m['name']+'.stderr')).read_text().strip().endswith(m['failure']), 'mutation '+m['name'])
files=[w/n for n in freeze]+[p/n for n in ['SOURCE_FREEZE.json','PORT_RECEIPT.json','ISOLATED_CLOSURE.json','MUTATIONS.json','WRAPPER_CONTROLS.json','AUTHOR_VERIFICATION_DRIVER.py','ISOLATED.stdout','ISOLATED.stderr']]
(out/'READ_HASHES.json').write_text(json.dumps({str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in files},indent=2)+'\n')
(out/'RESULT.json').write_text(json.dumps({'checks':len(checks),'predicates':checks,'scope':'Read-only source and actual-output replay; no physics rerun'},indent=2)+'\n')
print(len(checks))
