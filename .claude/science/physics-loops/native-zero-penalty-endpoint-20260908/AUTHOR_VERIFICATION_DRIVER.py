from pathlib import Path
import json,hashlib,subprocess,tempfile,shutil
w=Path('/private/tmp/toe-native-zero-penalty-endpoint-20260908');p=w/'.claude/science/physics-loops/native-zero-penalty-endpoint-20260908';name='scripts/native_zero_penalty_endpoint_2026_09_08.py';a=json.loads((w/'outputs/native_zero_penalty_endpoint_2026_09_08.json').read_text());paths=list(a['input_sha256'])+[name]
def clone(t):
 for n in paths:(t/n).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(w/n,t/n)
def run(t):return subprocess.run(['python3','-OO',str(t/name),'--json'],capture_output=True,text=True,timeout=180)
with tempfile.TemporaryDirectory(prefix='u0-isolated-') as d:
 t=Path(d);clone(t);r=run(t);(p/'ISOLATED.stdout').write_text(r.stdout);(p/'ISOLATED.stderr').write_text(r.stderr)
 if r.returncode:raise RuntimeError(r.stderr)
 if json.loads(r.stdout)['parts']['exact']['rows']!=a['parts']['exact']['rows']:raise RuntimeError('isolated scientific payload')
(p/'ISOLATED_CLOSURE.json').write_text(json.dumps({'paths':paths,'count':len(paths),'scientific_payload_equal':True},indent=2)+'\n')
logs=[]
for label,old,new in [('wrong_K_factor','G(0,-2*x);ik[b][a]=G(0,2*x)','G(0,-x);ik[b][a]=G(0,x)'),('odd_Gauss_domain','if n.bit_count()%2==0] # PARITY_DOMAIN','if n.bit_count()%2==1] # PARITY_DOMAIN'),('wrong_spectator_count','4*3**(k//2)','2*3**(k//2)')]:
 with tempfile.TemporaryDirectory(prefix='u0-mutant-') as d:
  t=Path(d);clone(t);f=t/'scripts/native_zero_penalty_endpoint_exact_2026_09_08.py';s=f.read_text()
  if old not in s:raise RuntimeError('mutation target')
  f.write_text(s.replace(old,new));r=run(t);(p/(label+'.stdout')).write_text(r.stdout);(p/(label+'.stderr')).write_text(r.stderr)
  if r.returncode==0:raise RuntimeError('surviving mutant')
  logs.append(dict(name=label,exit=r.returncode,old=old,new=new,failure=r.stderr.splitlines()[-1],sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
(p/'MUTATIONS.json').write_text(json.dumps(logs,indent=2)+'\n')
probe="import runpy,signal,sys;calls=[];signal.alarm=lambda n:calls.append(n);sys.argv=['p','--json'];runpy.run_path(%r,run_name='__main__');\nif calls!=[180]:raise RuntimeError(str(calls))"%str(w/name)
r=subprocess.run(['python3','-OO','-c',probe],capture_output=True,text=True,timeout=180)
if r.returncode:raise RuntimeError(r.stderr)
bad=subprocess.run(['python3','-OO',str(w/name),'--unknown'],capture_output=True,text=True,timeout=180)
if bad.returncode==0:raise RuntimeError('CLI')
(p/'WRAPPER_CONTROLS.json').write_text(json.dumps({'actual_alarm_calls':[180],'unknown_argument_exit':bad.returncode,'optimized':True},indent=2)+'\n');print(a['executed_predicates'],a['elapsed_seconds'],a['peak_rss_mib'])
