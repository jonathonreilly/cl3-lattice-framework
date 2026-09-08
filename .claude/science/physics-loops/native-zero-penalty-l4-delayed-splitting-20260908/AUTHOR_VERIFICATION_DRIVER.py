from pathlib import Path
import ast,hashlib,json,subprocess,shutil,tempfile,os
w=Path('/private/tmp/toe-native-zero-penalty-l4-delayed-splitting-20260908');p=w/'.claude/science/physics-loops/native-zero-penalty-l4-delayed-splitting-20260908';main='scripts/native_zero_penalty_l4_delayed_splitting_2026_09_08.py'
inputs=next(ast.literal_eval(x.value) for x in ast.parse((w/main).read_text()).body if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in x.targets));files=[main,*inputs];env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1');root=Path(tempfile.mkdtemp(prefix='delayed-isolated-'))
for f in files:(root/f).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(w/f,root/f)
r=subprocess.run(['python3','-OO',str(root/main),'--json'],capture_output=True,text=True,timeout=180,env=env);(p/'ISOLATED.stdout').write_text(r.stdout);(p/'ISOLATED.stderr').write_text(r.stderr)
if r.returncode:raise RuntimeError(r.stderr)
out=json.loads(r.stdout)
for key,name,fields in [('electric','native-zero-penalty-first-order-electric',['rows']),('spectator','native-zero-penalty-spectator-lifting',['five_pair_matching','six_pairs','non_scalar_even_masks']),('isolation','native-zero-penalty-l4-isolation',['fixtures'])]:
 old=json.loads((p/'originals'/name/'RESULT.json').read_text())
 for f in fields:
  if old[f]!=out['parts'][key][f]:raise RuntimeError('payload '+key)
(p/'ISOLATED_CLOSURE.json').write_text(json.dumps({'files':files,'scientific_payload_equal':True,'sha256':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in files}},indent=2)+'\n')
mutants=[('odd_active_projection','spectator',[('B=mm(A,P)','B=A')],'odd-cut active parity exclusion'),('incorrect_flux_scope','electric',[('cuts[m]&occ','cuts.get(m,0)&occ'),('for m in pairterms if m in cuts','for m in pairterms')],'K4 scalar E/2'),('winding_omission','isolation',[('for a in range(3):\n for v in vs:','for a in range(0):\n for v in vs:')],'noncanonical basic flux')];records=[]
for name,key,changes,expected in mutants:
 f=f'scripts/native_zero_penalty_{key}_exact_2026_09_08.py';s=(root/f).read_text();bad=s
 for old,new in changes:
  if bad.count(old)!=1:raise RuntimeError('mutationtarget '+name)
  bad=bad.replace(old,new)
 (root/f).write_text(bad);m=subprocess.run(['python3','-OO',str(root/main),'--json'],capture_output=True,text=True,timeout=180,env=env);(p/(name+'.stdout')).write_text(m.stdout);(p/(name+'.stderr')).write_text(m.stderr)
 if m.returncode==0 or expected not in m.stderr:raise RuntimeError('mutant '+name+' '+m.stderr)
 records.append({'name':name,'returncode':m.returncode,'expected':expected,'source_sha256':hashlib.sha256(bad.encode()).hexdigest()});(root/f).write_text(s)
(p/'MUTATIONS.json').write_text(json.dumps(records,indent=2)+'\n')
u=subprocess.run(['python3','-OO',str(root/main),'--unknown'],capture_output=True,text=True,env=env)
if u.returncode==0:raise RuntimeError('unknowncli')
code="import signal,runpy,sys; calls=[]; signal.alarm=lambda x:calls.append(x); sys.argv=[sys.argv[1],'--json']; runpy.run_path(sys.argv[0],run_name='__main__'); print('ALARMS',calls)"
a=subprocess.run(['python3','-OO','-c',code,str(root/main)],capture_output=True,text=True,env=env,timeout=180)
if a.returncode or not a.stdout.rstrip().endswith('ALARMS [180]'):raise RuntimeError('alarm')
(p/'WRAPPER_CONTROLS.json').write_text(json.dumps({'unknown_cli_rejected':True,'alarm_calls':[180],'json_parse':True},indent=2)+'\n')
(p/'PORT_RECEIPT.json').write_text(json.dumps({'live_count':93564,'parts':[964,87509,5091],'scientific_fields_unchanged':True,'helper_changes':'output dictionaries, standalone alarm guards, platform RSS; no science edits'},indent=2)+'\n');shutil.copy2(__file__,p/'AUTHOR_VERIFICATION_DRIVER.py')
freeze={f:hashlib.sha256((w/f).read_bytes()).hexdigest() for f in [*files,'outputs/native_zero_penalty_l4_delayed_splitting_2026_09_08.json']};(p/'SOURCE_FREEZE.json').write_text(json.dumps(freeze,indent=2)+'\n');print(json.dumps(freeze,indent=2));shutil.rmtree(root)
