from pathlib import Path
import ast,json,hashlib,tempfile,shutil,subprocess,sys,runpy,contextlib,io,signal
w=Path('/private/tmp/toe-native-local-ring-dynamics-20260908');p=w/'.claude/science/physics-loops/native-local-ring-dynamics-20260908';primary=w/'scripts/native_local_natural_ring_dynamics_2026_09_08.py'
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def inputs(f):
 for n in ast.parse(f.read_text()).body:
  if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='AUDIT_INPUT_PATHS' for x in n.targets):return list(ast.literal_eval(n.value))
 return []
closure={str(primary.relative_to(w))};todo=[primary]
while todo:
 for n in inputs(todo.pop()):
  if n not in closure:
   closure.add(n)
   if n.endswith('.py'):todo.append(w/n)
iso=Path(tempfile.mkdtemp(prefix='local-ring-isolated-'))
for n in closure:(iso/n).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(w/n,iso/n)
a=subprocess.run([sys.executable,'-OO',str(iso/primary.relative_to(w)),'--json'],capture_output=True,text=True,timeout=180)
(p/'ISOLATED.stdout').write_text(a.stdout);(p/'ISOLATED.stderr').write_text(a.stderr)
if a.returncode:raise RuntimeError('isolated closure')
raw=json.loads(a.stdout);live=json.loads((w/'outputs/native_local_natural_ring_dynamics_2026_09_08.json').read_text())
def science(x):
 if isinstance(x,dict):return {k:science(v) for k,v in x.items() if k not in ('seconds','rss_mib','elapsed_seconds','peak_rss_mib','source_sha256')}
 if isinstance(x,list):return [science(v) for v in x]
 return x
if science(raw)!=science(live):raise RuntimeError('isolated scientific mismatch')
original=json.loads((p/'originals/native-local-harmonics-root/RESULT.json').read_text())
if science(original)!=science(live['parts']['harmonics']):raise RuntimeError('harmonic payload changed')
(p/'PORT_RECEIPT.json').write_text(json.dumps(dict(harmonic_payload_unchanged=True,matrix='Declared adaptation from13 to14; original fourth fields agree, new complete coefficients retained.',matrix_fourth_matches_original=live['parts']['matrix']['ice_fourth']==json.loads((p/'originals/native-natural-ring-timescale-root/RESULT.json').read_text())['ice_fourth']),indent=2)+'\n')
mutations=[('wrong_homological_sign','matrix','value/(energy[a]-energy[b])','value/(energy[b]-energy[a])'),('missing_folded_term','matrix','p,F(2))','p,F(0))'),('wrong_harmonic_input_sign','harmonics','m=(1-2*x)*(ri+rj-5)','m=(2*x-1)*(ri+rj-5)'),('bare_X_instead_native','matrix','masks=(0,1,2,5)','masks=(0,0,0,0)')]
(p/'mutations').mkdir(exist_ok=True);rows=[]
for name,kind,old,new in mutations:
 src=w/f'scripts/native_local_ring_{kind}_2026_09_08.py';s=src.read_text()
 if s.count(old)!=1:raise RuntimeError('mutation site '+name)
 f=iso/'scripts'/('mutant_'+name+'.py');f.write_text(s.replace(old,new));a=subprocess.run([sys.executable,'-OO',str(f)],capture_output=True,text=True,timeout=180)
 shutil.copy2(f,p/'mutations'/f.name);(p/'mutations'/f'{name}.stdout').write_text(a.stdout);(p/'mutations'/f'{name}.stderr').write_text(a.stderr)
 if a.returncode==0 or 'RuntimeError' not in a.stderr:raise RuntimeError('surviving/invalid mutant '+name)
 rows.append(dict(name=name,source_sha256=sha(src),mutant_sha256=sha(f),exit_code=a.returncode,error=a.stderr.splitlines()[-1]))
(p/'MUTATIONS.json').write_text(json.dumps(rows,indent=2)+'\n')
calls=[];alarm=signal.alarm;signal.alarm=lambda n:calls.append(n)
try:
 for kind in ('matrix','harmonics','constants'):
  f=w/f'scripts/native_local_ring_{kind}_2026_09_08.py'
  if any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(f.read_text()))):raise RuntimeError('assert')
  with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(f))
finally:signal.alarm=alarm
if calls:raise RuntimeError('alarm reset')
a=subprocess.run([sys.executable,'-OO',str(primary),'--unknown'],capture_output=True,text=True,timeout=180)
if a.returncode!=2:raise RuntimeError('strict CLI')
(p/'WRAPPER_CONTROLS.json').write_text(json.dumps(dict(imported_alarm_calls=calls,bare_asserts=0,unknown_argument_exit=2),indent=2)+'\n')
(p/'ISOLATED_CLOSURE.json').write_text(json.dumps(dict(files={n:sha(w/n) for n in sorted(closure)},scientific_payload_equal=True,exit_code=0),indent=2)+'\n')
print(json.dumps(dict(predicates=live['executed_predicates'],mutants=len(rows),closure=len(closure)),indent=2))
