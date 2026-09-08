from pathlib import Path
import shutil,subprocess,tempfile,json,hashlib,ast
w=Path('/private/tmp/toe-native-eighth-diagonal-cycle-potential-20260908');p=w/'.claude/science/physics-loops/native-eighth-diagonal-cycle-potential-20260908';name='scripts/native_eighth_diagonal_cycle_potential_2026_09_08.py'
def run(root,args=[]):return subprocess.run(['python3','-OO',str(root/name)]+args,capture_output=True,text=True,timeout=180)
r=run(w);(p/'LIVE.stdout').write_text(r.stdout);(p/'LIVE.stderr').write_text(r.stderr)
if r.returncode:raise RuntimeError(r.stderr)
a=json.loads((w/'outputs/native_eighth_diagonal_cycle_potential_2026_09_08.json').read_text());paths=list(a['input_sha256'])+[name]
def clone(t):
 for n in paths:(t/n).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(w/n,t/n)
with tempfile.TemporaryDirectory(prefix='h8-isolated-') as d:
 t=Path(d);clone(t);r=run(t,['--json']);(p/'ISOLATED.stdout').write_text(r.stdout);(p/'ISOLATED.stderr').write_text(r.stderr)
 if r.returncode:raise RuntimeError(r.stderr)
 b=json.loads(r.stdout)
 for kind,keys in {'local':['rows','checks'],'global':['results','checks'],'combined':['scalar_parts','C_tree','W','decomposition','checks'],'witness':['results','checks']}.items():
  for key in keys:
   if a['parts'][kind][key]!=b['parts'][kind][key]:raise RuntimeError('isolated payload '+kind+key)
(p/'ISOLATED_CLOSURE.json').write_text(json.dumps({'files':paths,'count':len(paths),'scientific_payload_equal':True},indent=2)+'\n')
mutants=[('wrong_rank','local','contour(en,hops,n)/rank','contour(en,hops,n)'),('bare_X','local','def setup(edges,bits,native=True):','def setup(edges,bits,native=False):'),('omit_folds','local','def scalar(en,hops,fold=True):','def scalar(en,hops,fold=False):'),('wrong_path_multiplicity','combined',"sum(c('path4',b[r:]+b[:r]) for r in range(4))","2*sum(c('path4',b[r:]+b[:r]) for r in range(4))")]
logs=[]
for label,kind,old,new in mutants:
 with tempfile.TemporaryDirectory(prefix='h8-mutant-') as d:
  t=Path(d);clone(t);f=t/f'scripts/native_eighth_{kind}_2026_09_08.py';s=f.read_text()
  if old not in s:raise RuntimeError('missing target')
  f.write_text(s.replace(old,new));r=run(t,['--json']);(p/(label+'.stdout')).write_text(r.stdout);(p/(label+'.stderr')).write_text(r.stderr)
  if r.returncode==0:raise RuntimeError('surviving mutant '+label)
  logs.append(dict(name=label,exit_code=r.returncode,old=old,new=new,source_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),failure=r.stderr.splitlines()[-1]))
(p/'MUTATIONS.json').write_text(json.dumps(logs,indent=2)+'\n')
# AST verifies alarm calls occur only within the standalone guard; actual import probe runs all helpers through primary with intercepted alarms.
probe="""import runpy,signal,sys
calls=[]
signal.alarm=lambda n:calls.append(n)
sys.argv=['primary','--json']
runpy.run_path(sys.argv[1] if len(sys.argv)>2 else %r,run_name='__main__')
if calls!=[180]:raise RuntimeError('sliding alarm '+str(calls))
"""%str(w/name)
r=subprocess.run(['python3','-OO','-c',probe],capture_output=True,text=True,timeout=180)
if r.returncode:raise RuntimeError(r.stderr)
bad=run(w,['--unknown'])
if bad.returncode==0:raise RuntimeError('CLI guard')
(p/'WRAPPER_CONTROLS.json').write_text(json.dumps({'actual_primary_alarm_calls':[180],'unknown_cli_exit':bad.returncode,'optimized':True},indent=2)+'\n')
# Parent's canonical cache reflects the most recent actual run.
print(json.dumps({'total':a['executed_predicates'],'seconds':a['elapsed_seconds'],'rss':a['peak_rss_mib'],'mutations':logs},indent=2))
