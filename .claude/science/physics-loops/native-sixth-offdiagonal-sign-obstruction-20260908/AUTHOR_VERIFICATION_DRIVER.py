from pathlib import Path
import json,hashlib,subprocess,shutil,tempfile
w=Path('/private/tmp/toe-native-sixth-offdiagonal-sign-obstruction-20260908');p=w/'.claude/science/physics-loops/native-sixth-offdiagonal-sign-obstruction-20260908';name='scripts/native_sixth_offdiagonal_sign_obstruction_2026_09_08.py'
a=json.loads((w/'outputs/native_sixth_offdiagonal_sign_obstruction_2026_09_08.json').read_text());paths=list(a['input_sha256'])+[name]
def clone(t):
 for n in paths:(t/n).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(w/n,t/n)
def run(t):return subprocess.run(['python3','-OO',str(t/name),'--json'],capture_output=True,text=True,timeout=180)
with tempfile.TemporaryDirectory(prefix='h6-isolated-') as d:
 t=Path(d);clone(t);r=run(t);(p/'ISOLATED.stdout').write_text(r.stdout);(p/'ISOLATED.stderr').write_text(r.stderr)
 if r.returncode:raise RuntimeError(r.stderr)
 b=json.loads(r.stdout)
 for kind,keys in {'coefficients':['rows','six_cycle_amplitude','permutation_weights'],'normalization':['HB2','HB4','M2','forward4','reverse4'],'l4':['witness'],'l6':['witness'],'seed_component':['seed_bits','loop_states','preparation_faces','preparation_edges','native_B_phases','effective_sign_product']}.items():
  for k in keys:
   if a['parts'][kind][k]!=b['parts'][kind][k]:raise RuntimeError('payload mismatch')
(p/'ISOLATED_CLOSURE.json').write_text(json.dumps({'paths':paths,'count':len(paths),'payload_equal':True},indent=2)+'\n')
mutants=[('missing_feedback','coefficients','rhs=plus(rhs,scale(mm(mm(chi[a],C),chi[b]),-1))','rhs=plus(rhs,scale(mm(mm(chi[a],C),chi[b]),0))'),('bare_X','coefficients','F((-1)**((mask&z).bit_count()))','F(1)'),('reverse_metric','normalization','correct=add(HB4,sc(comm,F(1,2)))','correct=add(HB4,sc(comm,F(-1,2)))'),('wrong_hexagon_sign','l6','product_sign=-s','product_sign=s'),('omit_preparation','seed_component','prep_tape=[prep]+([second_prep] if one_failed else [])','prep_tape=[prep]')]
logs=[]
for label,kind,old,new in mutants:
 with tempfile.TemporaryDirectory(prefix='h6-mutant-') as d:
  t=Path(d);clone(t);f=t/f'scripts/native_sixth_{kind}_2026_09_08.py';s=f.read_text()
  if old not in s:raise RuntimeError('missing mutation')
  f.write_text(s.replace(old,new,1));r=run(t)
  (p/(label+'.stdout')).write_text(r.stdout);(p/(label+'.stderr')).write_text(r.stderr)
  if r.returncode==0:raise RuntimeError('mutant survived '+label)
  logs.append(dict(name=label,old=old,new=new,exit=r.returncode,failure=r.stderr.splitlines()[-1],sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
(p/'MUTATIONS.json').write_text(json.dumps(logs,indent=2)+'\n')
probe="import runpy,signal,sys;calls=[];signal.alarm=lambda n:calls.append(n);sys.argv=['p','--json'];runpy.run_path(%r,run_name='__main__');\nif calls!=[180]:raise RuntimeError(str(calls))"%str(w/name)
r=subprocess.run(['python3','-OO','-c',probe],capture_output=True,text=True,timeout=180)
if r.returncode:raise RuntimeError(r.stderr)
bad=subprocess.run(['python3','-OO',str(w/name),'--unknown'],capture_output=True,text=True,timeout=180)
if bad.returncode==0:raise RuntimeError('CLI')
(p/'WRAPPER_CONTROLS.json').write_text(json.dumps({'actual_alarm_calls':[180],'unknown_arg_exit':bad.returncode,'optimized':True},indent=2)+'\n')
print(json.dumps(dict(count=a['executed_predicates'],seconds=a['elapsed_seconds'],rss=a['peak_rss_mib'],mutations=logs),indent=2))
