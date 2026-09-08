from pathlib import Path
import ast,hashlib,json,subprocess,shutil,tempfile,os
w=Path('/private/tmp/toe-native-zero-penalty-optimal-flux-dispersion-20260908');p=w/'.claude/science/physics-loops/native-zero-penalty-optimal-flux-dispersion-20260908';main='scripts/native_zero_penalty_optimal_flux_dispersion_2026_09_08.py';flux='scripts/native_zero_penalty_optimal_flux_exact_2026_09_08.py';disp='scripts/native_zero_penalty_dispersion_exact_2026_09_08.py'
inputs=next(ast.literal_eval(x.value) for x in ast.parse((w/main).read_text()).body if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in x.targets));files=[main,*inputs];env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
r=subprocess.run(['python3','-OO',str(w/main)],capture_output=True,text=True,timeout=180,env=env);(p/'LIVE.stdout').write_text(r.stdout)
if r.returncode:raise RuntimeError(r.stderr)
root=Path(tempfile.mkdtemp(prefix='u0flux-isolated-'))
for f in files:(root/f).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(w/f,root/f)
r=subprocess.run(['python3','-OO',str(root/main),'--json'],capture_output=True,text=True,timeout=180,env=env);(p/'ISOLATED.stdout').write_text(r.stdout);(p/'ISOLATED.stderr').write_text(r.stderr)
if r.returncode:raise RuntimeError(r.stderr)
out=json.loads(r.stdout);origf=json.loads((p/'originals/native-zero-penalty-flux-selection-root/RESULT.json').read_text());origd=json.loads((p/'originals/native-zero-penalty-pi-dispersion/RESULT.json').read_text())
for key in ['partition_controls','torus_controls']:
 if out['parts']['flux'][key]!=origf[key]:raise RuntimeError('flux payload changed')
if out['parts']['dispersion']['rows']!=origd['rows']:raise RuntimeError('dispersion payload changed')
(p/'ISOLATED_CLOSURE.json').write_text(json.dumps({'files':files,'scientific_payload_equal':True,'sha256':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in files}},indent=2)+'\n')
mutants=[('partition',flux,'2**(vertices-2)*v','2**(vertices-1)*v','physical versus auxiliary partition'),('trivial_flux',flux,'(-1)**sum(u[:a])','1','all canonical basic cycle phases'),('seam',disp,'b=-tau[a] if r[a]==L[a]-1 else 1','b=tau[a] if r[a]==L[a]-1 else 1','literal canonical K')];records=[]
for name,f,old,new,expected in mutants:
 s=(root/f).read_text()
 if s.count(old)!=1:raise RuntimeError('mutation target '+name)
 (root/f).write_text(s.replace(old,new));m=subprocess.run(['python3','-OO',str(root/main),'--json'],capture_output=True,text=True,timeout=180,env=env)
 if m.returncode==0 or expected not in m.stderr:raise RuntimeError('surviving '+name)
 (p/(name+'.stdout')).write_text(m.stdout);(p/(name+'.stderr')).write_text(m.stderr);records.append({'name':name,'returncode':m.returncode,'expected':expected,'source_sha256':hashlib.sha256((root/f).read_bytes()).hexdigest()});(root/f).write_text(s)
(p/'MUTATIONS.json').write_text(json.dumps(records,indent=2)+'\n')
u=subprocess.run(['python3','-OO',str(root/main),'--unknown'],capture_output=True,text=True,env=env)
if u.returncode==0:raise RuntimeError('unknown CLI accepted')
code="import signal,runpy,sys; calls=[]; signal.alarm=lambda x:calls.append(x); sys.argv=[sys.argv[1],'--json']; runpy.run_path(sys.argv[0],run_name='__main__'); print('ALARMS',calls)"
a=subprocess.run(['python3','-OO','-c',code,str(root/main)],capture_output=True,text=True,timeout=180,env=env)
if a.returncode or not a.stdout.rstrip().endswith('ALARMS [180]'):raise RuntimeError('alarm scope')
(p/'WRAPPER_CONTROLS.json').write_text(json.dumps({'unknown_cli_rejected':True,'alarm_calls':[180],'json_parse':True},indent=2)+'\n')
(p/'PORT_RECEIPT.json').write_text(json.dumps({'live_count':7059,'flux_count':6962,'dispersion_count':97,'scientific_fields_unchanged':True,'helper_changes':'output dictionaries; standalone alarm guards; flux RSS platform conversion','independent_counts_archived_not_added':[6590,4660]},indent=2)+'\n')
shutil.copy2(__file__,p/'AUTHOR_VERIFICATION_DRIVER.py');freeze={f:hashlib.sha256((w/f).read_bytes()).hexdigest() for f in [*files,'outputs/native_zero_penalty_optimal_flux_dispersion_2026_09_08.json']};(p/'SOURCE_FREEZE.json').write_text(json.dumps(freeze,indent=2)+'\n');print(json.dumps(freeze,indent=2));shutil.rmtree(root)
