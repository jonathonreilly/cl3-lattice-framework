from pathlib import Path
import ast,hashlib,json,subprocess,shutil,tempfile,os
w=Path('/private/tmp/toe-native-leading-ring-stoquastic-gauge-20260908');p=w/'.claude/science/physics-loops/native-leading-ring-stoquastic-gauge-20260908';main='scripts/native_leading_ring_stoquastic_gauge_2026_09_08.py';helper='scripts/native_leading_ring_stoquastic_gauge_exact_2026_09_08.py'
tree=ast.parse((w/main).read_text());inputs=next(ast.literal_eval(x.value) for x in tree.body if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in x.targets));files=[main,*inputs]
root=Path(tempfile.mkdtemp(prefix='leading-ring-isolated-'));env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
for f in files:
 (root/f).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(w/f,root/f)
r=subprocess.run(['python3','-OO',str(root/main),'--json'],capture_output=True,text=True,timeout=180,env=env);(p/'ISOLATED.stdout').write_text(r.stdout);(p/'ISOLATED.stderr').write_text(r.stderr)
if r.returncode:raise RuntimeError(r.stderr)
out=json.loads(r.stdout);orig=json.loads((p/'originals/native-leading-ring-stoquastic-gauge/RESULT.json').read_text());live=json.loads((w/'outputs/native_leading_ring_stoquastic_gauge_2026_09_08.json').read_text())
if out['parts']['exact']['results']!=orig['results'] or live['parts']['exact']['results']!=orig['results']:raise RuntimeError('raw scientific payload changed')
(p/'ISOLATED_CLOSURE.json').write_text(json.dumps({'files':files,'sha256':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in files},'scientific_payload_equal':True,'returncode':r.returncode},indent=2)+'\n')
s=(root/helper).read_text();old='return d(x)*(-1)**((linear&x).bit_count())'
if s.count(old)!=1:raise RuntimeError('mutation target')
(root/helper).write_text(s.replace(old,'return d(x)'))
m=subprocess.run(['python3','-OO',str(root/main),'--json'],capture_output=True,text=True,timeout=180,env=env)
if m.returncode==0 or 'actual full native transition' not in m.stderr:raise RuntimeError('mutant not discriminated')
(p/'MUTANT.stdout').write_text(m.stdout);(p/'MUTANT.stderr').write_text(m.stderr);(p/'MUTATIONS.json').write_text(json.dumps({'name':'omit linear background in actual phase transformation','returncode':m.returncode,'expected_failure':'actual full native transition','source_sha256':hashlib.sha256((root/helper).read_bytes()).hexdigest()},indent=2)+'\n');(root/helper).write_text(s)
u=subprocess.run(['python3','-OO',str(root/main),'--unknown'],capture_output=True,text=True,env=env)
if u.returncode==0:raise RuntimeError('unknown CLI accepted')
code="import signal,runpy,sys; calls=[]; signal.alarm=lambda x:calls.append(x); sys.argv=[sys.argv[1],'--json']; runpy.run_path(sys.argv[0],run_name='__main__'); print('ALARMS',calls)"
a=subprocess.run(['python3','-OO','-c',code,str(root/main)],capture_output=True,text=True,env=env,timeout=180)
if a.returncode or not a.stdout.rstrip().endswith('ALARMS [180]'):raise RuntimeError('alarm scope')
(p/'WRAPPER_CONTROLS.json').write_text(json.dumps({'unknown_cli_rejected':True,'alarm_calls':[180],'json_parse':True},indent=2)+'\n')
(p/'PORT_RECEIPT.json').write_text(json.dumps({'original_count':6253,'live_count':6253,'scientific_results_unchanged':True,'helper_delta':'standalone alarm guard and output-only wrapper; no scientific body edits','reviewer_805_archived_not_added':True},indent=2)+'\n')
shutil.copy2(__file__,p/'AUTHOR_VERIFICATION_DRIVER.py')
freeze={f:hashlib.sha256((w/f).read_bytes()).hexdigest() for f in [*files,'outputs/native_leading_ring_stoquastic_gauge_2026_09_08.json']};(p/'SOURCE_FREEZE.json').write_text(json.dumps(freeze,indent=2)+'\n');print(json.dumps(freeze,indent=2));shutil.rmtree(root)
