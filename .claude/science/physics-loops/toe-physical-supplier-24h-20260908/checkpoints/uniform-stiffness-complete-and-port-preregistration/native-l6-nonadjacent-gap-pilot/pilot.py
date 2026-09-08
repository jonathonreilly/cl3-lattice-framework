import sys,signal,time,json,resource,importlib.util
from pathlib import Path
signal.alarm(29);start=time.monotonic();P=Path(__file__).resolve().parent
if len(sys.argv)!=2:raise ValueError('one fresh output directory required')
out=Path(sys.argv[1]).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh external output only')
def load(name):
 spec=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
v=load('verify');freeze,f=v.verify();out.mkdir(parents=True);rows=[]
def guard():
 if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise RuntimeError('RSS384MiB')
 if time.monotonic()-start>29:raise TimeoutError('29s')
try:
 t=time.monotonic();core=load('core');baseline=time.monotonic()-t
 import numpy as np
 if str(Path(np.__file__).resolve())!=f['numpy_origin'] or np.__version__!=f['numpy_version']:raise ValueError('numpy origin')
 for m in tuple(sys.modules.values()):
  name=getattr(m,'__file__',None)
  if name and str(Path(name).resolve()).startswith(f['numpy_root']):
   p=str(Path(name).resolve())
   if p not in f['runtime']:raise ValueError('unbound numpy module '+p)
 guard();t=time.monotonic()
 # Exact shifted baseline inverse residual, sparse integer baseline times rational R.
 for i in range(108):
  nz=[(k,int(core.A[i,k])) for k in range(108) if core.A[i,k]]
  for j in range(108):
   x=sum(a*core.R[k][j] for k,a in nz)+core.s*core.R[i][j]
   if x!=int(i==j):raise ValueError('baseline inverse residual')
 baseline_control=time.monotonic()-t;plan=json.loads((P/'PLAN.json').read_text())
 for index,c in enumerate(plan['cases']):
  guard();t=time.monotonic();r=core.certify(int(c['mask']),c['white_center'],controls=True)
  if r['positive']!=(core.F(r['gap_lower'])>0):raise ValueError('exact positivity')
  r.update(case=index,name=c['name'],order=c['order'],seconds=time.monotonic()-t);rows.append(r)
  (out/f'case_{index:02d}.json').write_text(json.dumps(r,indent=2)+'\n')
 singleton_lower=2*core.lowerroot(3)
 if not 0<singleton_lower or singleton_lower**2>12:raise ValueError('singleton rational bound')
 guard();(out/'RESULT.json').write_text(json.dumps(dict(status='COMPLETE',freeze=freeze,rows=rows,baseline_seconds=baseline,baseline_control_seconds=baseline_control,singletons=plan['singletons'],singleton_lower=str(singleton_lower),seconds=time.monotonic()-start,rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,scope='fixed25-case cost pilot; not complete4986-prefix certification'),indent=2)+'\n')
except BaseException as e:
 (out/'FAILURE.json').write_text(json.dumps(dict(error=repr(e),rows=rows,seconds=time.monotonic()-start),indent=2)+'\n');raise
