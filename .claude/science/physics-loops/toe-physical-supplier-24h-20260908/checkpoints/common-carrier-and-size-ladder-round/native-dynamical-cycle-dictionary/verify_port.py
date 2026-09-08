from pathlib import Path
import subprocess,json,hashlib,sys
w=Path('/private/tmp/toe-native-dynamical-cycle-dictionary-20260908');p=w/'.claude/science/physics-loops/native-dynamical-cycle-dictionary-20260908';ev=p/'evidence'
def clean(x):
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k not in ('seconds','source_sha256')}
 if isinstance(x,list):return [clean(v) for v in x]
 return x
live=json.loads((w/'outputs/native_dynamical_cycle_dictionary_2026_09_08.json').read_text())
refs={'author':ev/'native-dynamical-cycle-dictionary/RESULT.json','independent':ev/'native-common-carrier-cold-review/DICTIONARY_RESULT.json','exchange':ev/'native-common-carrier-cold-review/RESULT.json'}
receipt={}
for key,path in refs.items():
 original=json.loads(path.read_text());same=clean(original)==clean(live['parts'][key])
 if not same:raise RuntimeError('changed physics '+key)
 receipt[key]={'scientific_payload_identical':True,'original_result_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
(p/'PORT_RECEIPT.json').write_text(json.dumps({'normalization_only':['seconds','source_sha256'],'parts':receipt},indent=2)+'\n')
mutdir=ev/'actual-mutations';mutdir.mkdir(exist_ok=True)
s=(w/'scripts/native_dynamical_cycle_dictionary_author_2026_09_08.py').read_text()
changes={'omit_basis_phase':('phase[x]=phase[y]*b/a','phase[x]=1'), 'omit_cycle_factor':('na*=1j**len(cycle);ga*=1j**len(cycle)','na*=1;ga*=1j**len(cycle)')}
results={}
for name,(old,new) in changes.items():
 if s.count(old)!=1:raise RuntimeError('mutation target '+name)
 path=mutdir/(name+'.py');path.write_text(s.replace(old,new))
 proc=subprocess.run([sys.executable,'-O',str(path),'--json'],capture_output=True,text=True,timeout=180)
 (mutdir/(name+'.stdout')).write_text(proc.stdout);(mutdir/(name+'.stderr')).write_text(proc.stderr)
 if proc.returncode==0:raise RuntimeError('mutant survived '+name)
 results[name]={'returncode':proc.returncode,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'last_error':proc.stderr.splitlines()[-1]}
(p/'MUTATIONS.json').write_text(json.dumps(results,indent=2)+'\n')
script=w/'scripts/native_dynamical_cycle_dictionary_2026_09_08.py'
proc=subprocess.run([sys.executable,str(script),'--json'],capture_output=True,text=True,timeout=180)
if proc.returncode:raise RuntimeError(proc.stderr)
parsed=json.loads(proc.stdout);(ev/'canonical-pure-json.txt').write_text(proc.stdout)
proc2=subprocess.run([sys.executable,str(script),'--unexpected'],capture_output=True,text=True,timeout=180)
if proc2.returncode!=2:raise RuntimeError('strict CLI')
(ev/'strict-cli.stderr').write_text(proc2.stderr)
(p/'INTERFACE_CHECKS.json').write_text(json.dumps({'pure_json_status':parsed['status'],'strict_unknown_arg_exit':proc2.returncode,'scientific_assertions':parsed['executed_assertions']},indent=2)+'\n')
print(json.dumps({'port':receipt,'mutations':results},indent=2))
