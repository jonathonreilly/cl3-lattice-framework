from pathlib import Path
import ast,hashlib,json,shutil,subprocess,tempfile,sys,runpy,contextlib,io,signal
w=Path('/private/tmp/toe-native-low-charge-u1-dictionary-20260908');p=w/'.claude/science/physics-loops/native-low-charge-u1-dictionary-20260908'
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def inputs(f):
 for n in ast.parse(f.read_text()).body:
  if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in n.targets):return list(ast.literal_eval(n.value))
 return []
primary=w/'scripts/native_low_charge_u1_dictionary_2026_09_08.py';closure={str(primary.relative_to(w))};todo=[primary]
while todo:
 for n in inputs(todo.pop()):
  if n not in closure:
   closure.add(n)
   if n.endswith('.py'):todo.append(w/n)
iso=Path(tempfile.mkdtemp(prefix='low-charge-u1-isolated-'))
for n in closure:(iso/n).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(w/n,iso/n)
r=subprocess.run([sys.executable,'-OO',str(iso/primary.relative_to(w)),'--json'],capture_output=True,text=True,timeout=180)
(p/'ISOLATED.stdout').write_text(r.stdout);(p/'ISOLATED.stderr').write_text(r.stderr)
if r.returncode:raise RuntimeError('isolated run failed')
new=json.loads(r.stdout);live=json.loads((w/'outputs/native_low_charge_u1_dictionary_2026_09_08.json').read_text())
omit={'seconds','rss_MiB','rss_mib','elapsed_seconds','peak_rss_mib','portable_seconds','portable_rss_mib','executed_predicates'}
def scientific(x):
 if isinstance(x,dict):return {k:scientific(v) for k,v in x.items() if k not in omit}
 if isinstance(x,list):return [scientific(v) for v in x]
 return x
if scientific(new)!=scientific(live):raise RuntimeError('isolated mismatch')
(p/'ISOLATED_CLOSURE.json').write_text(json.dumps(dict(files={n:sha(w/n) for n in sorted(closure)},scientific_payload_equal=True,exit_code=0),indent=2)+'\n')
receipt={}
for kind,folder,file in [('author','native-low-charge-u1-dictionary','RESULT.json'),('independent','native-low-charge-u1-cold-review','RESULT.json'),('absolute','native-low-charge-u1-dictionary','ABSOLUTE_PHASE_RESULT.json')]:
 f=p/'originals'/folder/file;eq=scientific(json.loads(f.read_text()))==scientific(live['parts'][kind])
 if not eq:raise RuntimeError('original payload mismatch '+kind)
 receipt[kind]=dict(original_sha256=sha(f),scientific_payload_identical=eq)
(p/'PORT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
mutants=[('missing_hole_minus','author','candidate = (2 + 2 * (a + b)) % 4','candidate = (2 * (a + b)) % 4'),('wrong_gauss_sign','domain','return div-(plus-minus)','return div+(plus-minus)'),('removed_no_double','domain','return plus*minus==0 and gauss(div,plus,minus)==0','return gauss(div,plus,minus)==0'),('wrong_absolute_basis_phase','absolute','sign != (-1) ** sum(I)','sign != (-1) ** (sum(I)-len(I)*(len(I)-1)//2)')]
(p/'mutations').mkdir(exist_ok=True);records=[]
for name,kind,old,newtext in mutants:
 source=w/f'scripts/native_low_charge_u1_{kind}_2026_09_08.py';text=source.read_text()
 if text.count(old)!=1:raise RuntimeError('mutation location ambiguous '+name)
 # Preserve repository-relative __file__ layout for the actual D4 seed dependency.
 target=iso/'scripts'/f'mutant_{name}.py';target.write_text(text.replace(old,newtext));run=subprocess.run([sys.executable,'-OO',str(target)],capture_output=True,text=True,timeout=180)
 shutil.copy2(target,p/'mutations'/target.name);(p/'mutations'/f'{name}.stdout').write_text(run.stdout);(p/'mutations'/f'{name}.stderr').write_text(run.stderr)
 if run.returncode==0 or 'RuntimeError' not in run.stderr:raise RuntimeError('mutation did not fail scientifically '+name)
 records.append(dict(name=name,source_sha256=sha(source),mutant_sha256=sha(target),exit_code=run.returncode))
(p/'MUTATIONS.json').write_text(json.dumps(records,indent=2)+'\n')
# Import execution cannot reset the primary absolute deadline. No bare assert may disappear under -OO.
calls=[];oldalarm=signal.alarm;signal.alarm=lambda n:calls.append(n)
try:
 for kind in ('author','independent','absolute','domain'):
  f=w/f'scripts/native_low_charge_u1_{kind}_2026_09_08.py'
  if any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(f.read_text()))):raise RuntimeError('bare assertion')
  with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(f))
finally:signal.alarm=oldalarm
if calls:raise RuntimeError('alarm reset')
bad=subprocess.run([sys.executable,'-OO',str(primary),'--unknown'],capture_output=True,text=True,timeout=180)
if bad.returncode!=2:raise RuntimeError('CLI control')
(p/'WRAPPER_CONTROLS.json').write_text(json.dumps(dict(imported_alarm_calls=calls,bare_asserts=0,unknown_argument_exit=bad.returncode),indent=2)+'\n')
print(json.dumps(dict(total=live['executed_predicates'],parts={k:v['executed_predicates'] for k,v in live['parts'].items()},closure=len(closure),mutants=len(records)),indent=2))
