"""Stdlib-only verified supervisor loader; readiness executes imports, never main."""
import sys,json,hashlib,types
from pathlib import Path
B=Path(__file__).resolve().parent
if not sys.flags.isolated or not sys.dont_write_bytecode or not sys.flags.no_site:raise ValueError('-I -B -S required')
if len(sys.argv)!=4 or sys.argv[1] not in ('readiness','run'):raise ValueError('bootstrap.py readiness|run AUTH OUTPUT')
r=json.loads((B/'RUNTIME.json').read_text());cfg=json.loads((B/'DESIGN.json').read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def loaded():
 for m in list(sys.modules.values()):
  p=getattr(m,'__file__',None)
  if p:
   p=str(Path(p).resolve())
   if p==str(B/'bootstrap.py'):continue
   if p not in r['inputs'] or sha(p)!=r['inputs'][p]:raise ValueError('loaded origin '+p)
if str(Path(sys.executable).resolve())!=r['interpreter']:raise ValueError('interpreter')
for p,h in r['inputs'].items():
 if sha(p)!=h:raise ValueError('runtime pin '+p)
for n,h in json.loads((B/'FREEZE.json').read_text())['files'].items():
 if sha(B/n)!=h:raise ValueError('bootstrap package pin '+n)
loaded();s=Path(cfg['supervisor_dir']);f=s/'FREEZE.json'
if sha(f)!=cfg['supervisor_freeze']:raise ValueError('supervisor freeze')
for n,h in json.loads(f.read_text())['files'].items():
 if sha(s/n)!=h:raise ValueError('supervisor input '+n)
source=(s/'supervise.py').read_bytes()
if hashlib.sha256(source).hexdigest()!=json.loads(f.read_text())['files']['supervise.py']:raise ValueError('supervisor bytes')
m=types.ModuleType('verified_supervisor');m.__file__=str(s/'supervise.py');exec(compile(source,m.__file__,'exec'),m.__dict__)
loaded()
if sys.argv[1]=='readiness':print(json.dumps({'status':'PASS','supervisor_startup_imports':True,'main_called':False,'physical_calls':0}));raise SystemExit
sys.argv=[m.__file__,sys.argv[2],sys.argv[3]]
try:m.main()
finally:loaded()
if sha(f)!=cfg['supervisor_freeze']:raise ValueError('post supervisor freeze')
