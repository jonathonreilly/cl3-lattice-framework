from pathlib import Path
import ast,hashlib,json,shutil,subprocess,tempfile,sys
w=Path('/private/tmp/toe-native-global-charge-support-20260908');p=w/'.claude/science/physics-loops/native-global-charge-support-20260908'
def sha(x):return hashlib.sha256(x.read_bytes()).hexdigest()
primary=w/'scripts/native_global_charge_support_2026_09_08.py'
def paths(f):
 for n in ast.parse(f.read_text()).body:
  if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in n.targets):return list(ast.literal_eval(n.value))
 return []
closure={str(primary.relative_to(w))};todo=[primary]
while todo:
 for name in paths(todo.pop()):
  if name not in closure:
   closure.add(name)
   if name.endswith('.py'):todo.append(w/name)
iso=Path(tempfile.mkdtemp(prefix='global-charge-isolated-'))
for name in closure:(iso/name).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(w/name,iso/name)
r=subprocess.run([sys.executable,'-OO',str(iso/primary.relative_to(w)),'--json'],capture_output=True,text=True,timeout=180)
(p/'ISOLATED.stdout').write_text(r.stdout);(p/'ISOLATED.stderr').write_text(r.stderr)
if r.returncode:raise RuntimeError('isolated closure failed')
raw=json.loads(r.stdout);live=json.loads((w/'outputs/native_global_charge_support_2026_09_08.json').read_text())
def scientific(x):
 if isinstance(x,dict):return {k:scientific(v) for k,v in x.items() if k not in ('seconds','peak_MiB','source_sha256','elapsed_seconds','peak_rss_mib')}
 if isinstance(x,list):return [scientific(v) for v in x]
 return x
if scientific(raw)!=scientific(live):raise RuntimeError('isolated payload changed')
(p/'ISOLATED_CLOSURE.json').write_text(json.dumps(dict(files={n:sha(w/n) for n in sorted(closure)},exit_code=r.returncode,scientific_payload_equal=True,seconds=raw['elapsed_seconds'],rss=raw['peak_rss_mib']),indent=2)+'\n')
originals={'reachability':p/'originals/native-d2-reachability/RESULT.json','connectivity':p/'originals/native-d2-reachability/CONNECTIVITY_RESULT.json','exchange':p/'originals/native-global-charge-exchange/RESULT.json'}
receipt={}
for kind,f in originals.items():
 eq=scientific(json.loads(f.read_text()))==scientific(live['parts'][kind]);receipt[kind]=dict(original_sha256=sha(f),scientific_payload_identical=eq)
 if not eq:raise RuntimeError('original scientific payload changed '+kind)
(p/'PORT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
mutations=[('missing_parking_return','connectivity','if park is not None:hop(park,p,1)','if False:hop(park,p,1)'),('wrong_negative_cycle_direction','connectivity','(j+s*k)%len(C)','(j+k)%len(C)'),('missing_native_Z_strings','exchange','if nb<w:pa+=2*','if False:pa+=2*')]
(p/'mutations').mkdir(exist_ok=True);records=[]
for name,kind,old,new in mutations:
 source=w/f'scripts/native_global_charge_{kind}_2026_09_08.py';text=source.read_text()
 if text.count(old)!=1:raise RuntimeError('mutation location not unique')
 target=p/'mutations'/f'{name}.py';target.write_text(text.replace(old,new));run=subprocess.run([sys.executable,'-OO',str(target)],capture_output=True,text=True,timeout=180)
 (p/'mutations'/f'{name}.stdout').write_text(run.stdout);(p/'mutations'/f'{name}.stderr').write_text(run.stderr)
 if run.returncode==0:raise RuntimeError('semantic mutant survived '+name)
 records.append(dict(name=name,source_sha256=sha(source),mutant_sha256=sha(target),exit_code=run.returncode,actual_predicate_failure='RuntimeError' in run.stderr))
(p/'MUTATIONS.json').write_text(json.dumps(records,indent=2)+'\n')
# Strict CLI failure is separate from semantic failures.
bad=subprocess.run([sys.executable,'-OO',str(primary),'--unknown'],capture_output=True,text=True,timeout=180)
if bad.returncode!=2:raise RuntimeError('strict CLI failure')
(p/'CLI_CONTROL.json').write_text(json.dumps(dict(exit_code=bad.returncode,stderr=bad.stderr),indent=2)+'\n')
print(json.dumps(dict(closure=len(closure),predicate_total=raw['executed_assertions'],mutants_killed=len(records),port=receipt),indent=2))
