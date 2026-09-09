import sys,json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'native-highprecision-b-contraction-design'
if not(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):raise ValueError('strict flags')
f=json.loads((P/'RUNTIME_FREEZE.json').read_text());b=json.loads((R/'ROOT_BINDING.json').read_text());sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
if sha(P/'RUNTIME_FREEZE.json')!=b['worker_freeze'] or sha(P/'BINDING.json')!=b['binding_sha256']:raise ValueError('summary input binding')
p=P/'summarize.py';data=p.read_bytes()
if hashlib.sha256(data).hexdigest()!=f['inputs'][str(p)]:raise ValueError('summary source bytes')
sys.argv=[str(p),sys.argv[1],b['worker_freeze'],b['binding_sha256'],sys.argv[2]];exec(compile(data,str(p),'exec'),{'__name__':'__main__','__file__':str(p)})
for m in list(sys.modules.values()):
 p=getattr(m,'__file__',None)
 if p and Path(p).resolve()!=Path(__file__).resolve():
  p=str(Path(p).resolve())
  if p not in f['inputs'] or sha(p)!=f['inputs'][p]:raise ValueError('summary loaded origin '+p)
