import sys,time,signal,resource,json,hashlib,importlib.util
from pathlib import Path
signal.alarm(29);t=time.monotonic();P=Path(__file__).resolve().parent
if not sys.flags.isolated or len(sys.argv)!=3 or sys.argv[1] not in ('controls','solve'):raise ValueError('-I -B run.py controls|solve FRESH_EXTERNAL_OUTPUT')
out=Path(sys.argv[2]).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh external output')
f=json.loads((P/'FREEZE.json').read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
actual=sorted(str(x.relative_to(P)) for x in P.rglob('*') if x.is_file() and x.suffix in ('.py','.pyc','.so'))
if actual!=f['executable_membership']:raise ValueError('module membership')
for group,base in [('files',P),('runtime',None),('dependencies',None)]:
 for p,h in f[group].items():
  if sha(base/p if base else p)!=h:raise ValueError('pin '+p)
out.mkdir(parents=True)
def guard():
 if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise RuntimeError('RSS')
 if time.monotonic()-t>29:raise TimeoutError('29seconds')
try:
 spec=importlib.util.spec_from_file_location('vertex_core',P/'core.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c);control=c.controls();guard();result=dict(controls=control,mode=sys.argv[1],freeze=sha(P/'FREEZE.json'))
 if sys.argv[1]=='solve':
  e=[c.F(int(i==0)) for i in range(32)];x={};ys=[];timings=[]
  for pair in c.pairs:
   guard();start=time.monotonic();x[pair]=c.solve(c.matrix(c.mask(pair),0),e);timings.append(time.monotonic()-start)
  G=c.gamma(0)
  for pair in c.pairs:
   guard();start=time.monotonic();b=[sum(x[a][i] for a in c.pairs if not(set(a)&set(pair))) for i in range(32)];y=c.solve(c.matrix(c.mask(pair),1),c.mv(G,b));ys.append(y);timings.append(time.monotonic()-start)
  z=[sum(y[i] for y in ys)/48 for i in range(32)]
  weights={str(k):sum(c.W[1][i]*z[i]**2 for i,b in enumerate(c.bits[1]) if b.bit_count()==k) for k in (1,3,5)}
  total=sum(weights.values());multi=weights['3']+weights['5']
  result.update(coordinates=[str(q) for q in z],occupation_bits=c.bits[1],metric=[str(q) for q in c.W[1]],particle_weights={k:str(v) for k,v in weights.items()},total_weight=str(total),multiparticle_weight=str(multi),multiparticle_positive=multi>0,solve_seconds=timings,exact_residuals=30,normalization='chi=(1/48) S sum y_C at |t|=1; two negative resolvents cancel')
  (out/'SOLVE_VECTORS.json').write_text(json.dumps(dict(first={','.join(map(str,p)):list(map(str,v)) for p,v in x.items()},second=[list(map(str,y)) for y in ys]),indent=2)+'\n')
 guard();result.update(status='COMPLETE',seconds=time.monotonic()-t,rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
except BaseException as e:
 (out/'FAILURE.json').write_text(json.dumps(dict(error=repr(e),seconds=time.monotonic()-t))+'\n');raise
