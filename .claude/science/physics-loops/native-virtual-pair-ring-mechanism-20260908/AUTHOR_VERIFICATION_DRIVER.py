from pathlib import Path
import ast,json,hashlib,shutil,subprocess,sys,tempfile,signal,runpy,contextlib,io
w=Path('/private/tmp/toe-native-virtual-pair-ring-mechanism-20260908');p=w/'.claude/science/physics-loops/native-virtual-pair-ring-mechanism-20260908'
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def inputs(f):
 for n in ast.parse(f.read_text()).body:
  if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in n.targets):return list(ast.literal_eval(n.value))
 return []
primary=w/'scripts/native_virtual_pair_ring_mechanism_2026_09_08.py';closure={str(primary.relative_to(w))};todo=[primary]
while todo:
 for name in inputs(todo.pop()):
  if name not in closure:
   closure.add(name)
   if name.endswith('.py'):todo.append(w/name)
iso=Path(tempfile.mkdtemp(prefix='virtual-pair-isolated-'))
for n in closure:(iso/n).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(w/n,iso/n)
r=subprocess.run([sys.executable,'-OO',str(iso/primary.relative_to(w)),'--json'],capture_output=True,text=True,timeout=180)
(p/'ISOLATED.stdout').write_text(r.stdout);(p/'ISOLATED.stderr').write_text(r.stderr)
if r.returncode:raise RuntimeError('isolated closure')
raw=json.loads(r.stdout);live=json.loads((w/'outputs/native_virtual_pair_ring_mechanism_2026_09_08.json').read_text())
omit={'seconds','rss_MiB','source_sha256','input_sha256','elapsed_seconds','peak_rss_mib'}
def science(x):
 if isinstance(x,dict):return {k:science(v) for k,v in x.items() if k not in omit}
 if isinstance(x,list):return [science(v) for v in x]
 return x
if science(raw)!=science(live):raise RuntimeError('isolated payload')
(p/'ISOLATED_CLOSURE.json').write_text(json.dumps(dict(files={n:sha(w/n) for n in sorted(closure)},exit_code=0,scientific_payload_equal=True),indent=2)+'\n')
receipt={}
for kind,folder,file in [('fourth','native-virtual-pair-induced-ring','RESULT.json'),('sixth_local','native-virtual-pair-sixth-diagonal','RESULT.json'),('sixth_global','native-virtual-pair-sixth-diagonal','FULL_RESULT.json'),('full_fourth','native-soft-charge-penalty-root','FULL_FOURTH_RESULT.json'),('full_sixth_local','native-soft-charge-penalty-root','RESULT.json')]:
 f=p/'originals'/folder/file
 if science(json.loads(f.read_text()))!=science(live['parts'][kind]):raise RuntimeError('original payload '+kind)
 receipt[kind]=dict(original_sha256=sha(f),scientific_payload_identical=True)
original=json.loads((p/'originals/native-virtual-ring-remainder-cold-review/CONTROL.json').read_text())
for k in ('constant_terms','sum','surviving_inner_words'):
 if original[k]!=live['parts']['remainder'][k]:raise RuntimeError('independent scalar mismatch')
(p/'PORT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
mutants=[('full_to_hard_support','full_sixth_global','states.append(m);ener[m]=sum(d*d for d in delta);full[m]=zz','if max(map(abs,delta))<=1:states.append(m);ener[m]=sum(d*d for d in delta);full[m]=zz'),('full_missing_phase','full_fourth','(-1)**((z&masks[e]).bit_count()) if native else 1','1 if native else 1'),('full_missing_feedback','full_sixth_global','sum(E[k]*psi[n-k][m] for k in range(1,n))','F(0)'),('native_to_bare_X','fourth','(-1)**((z&masks[e]).bit_count()) if native else 1','1 if native else 1'),('wrong_D4_denominator','fourth','den*=d','den*=2'),('missing_folded_cross','fourth','folded=F(1,4)','folded=F(0)'),('missing_sixth_phase','sixth_global','value*(-1)**((full[m]&masks[e]).bit_count())','value'),('missing_sixth_feedback','sixth_global','sum(E[k]*psi[n-k][m] for k in range(1,n))','F(0)'),('relaxed_sixth_support','sixth_global','max(map(abs,delta))<=1','max(map(abs,delta))<=2'),('wrong_remainder_tail','remainder','1/((1-r)**3*(1-2*r))','1/((1-r)**3*(1-r))')]
(p/'mutations').mkdir(exist_ok=True);records=[]
for name,kind,old,new in mutants:
 source=w/f'scripts/native_virtual_pair_{kind}_2026_09_08.py';text=source.read_text()
 if text.count(old)!=1:raise RuntimeError('mutation location '+name)
 f=iso/'scripts'/f'mutant_{name}.py';f.write_text(text.replace(old,new));r=subprocess.run([sys.executable,'-OO',str(f)],capture_output=True,text=True,timeout=180)
 shutil.copy2(f,p/'mutations'/f.name);(p/'mutations'/f'{name}.stdout').write_text(r.stdout);(p/'mutations'/f'{name}.stderr').write_text(r.stderr)
 if not r.returncode or 'RuntimeError' not in r.stderr:raise RuntimeError('not semantic failure '+name)
 records.append(dict(name=name,source_sha256=sha(source),mutant_sha256=sha(f),exit_code=r.returncode))
(p/'MUTATIONS.json').write_text(json.dumps(records,indent=2)+'\n')
calls=[];oldalarm=signal.alarm;signal.alarm=lambda n:calls.append(n)
try:
 for kind in ('fourth','sixth_local','sixth_global','remainder','full_fourth','full_sixth_local','full_sixth_global'):
  f=w/f'scripts/native_virtual_pair_{kind}_2026_09_08.py'
  if any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(f.read_text()))):raise RuntimeError('bare assert')
  with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(f))
finally:signal.alarm=oldalarm
if calls:raise RuntimeError('alarm reset')
bad=subprocess.run([sys.executable,'-OO',str(primary),'--unknown'],capture_output=True,text=True,timeout=180)
if bad.returncode!=2:raise RuntimeError('CLI')
(p/'WRAPPER_CONTROLS.json').write_text(json.dumps(dict(imported_alarm_calls=calls,bare_asserts=0,unknown_argument_exit=bad.returncode),indent=2)+'\n')
print(json.dumps(dict(predicates=live['executed_predicates'],mutants=len(records),closure=len(closure)),indent=2))
