import pathlib,hashlib,json,subprocess,importlib.util,sys,numpy as np
P=pathlib.Path(__file__).parent
spec=importlib.util.spec_from_file_location('old',P/'CORE_V095_ORIGINAL.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
from core import Path
class Tape:
 def __init__(self,u):self.u=iter(u)
 def random(self):return next(self.u)
count=0
for L in (2,4):
 a=Path(L,8,.95);b=old.Path(L,8)
 for t in range(512):
  u=[((37*t+11)%509+.5)/509,((173*t+3)%503+.5)/503]
  if a.step(Tape(u))!=b.step(Tape(u)):raise RuntimeError('old .95 event')
  if a.head!=b.head or a.direction!=b.direction or not np.array_equal(a.labels,b.labels):raise RuntimeError('old .95 ring')
  for k in range(3):
   if not np.array_equal(a.states[k],b.states[k]) or a.nf[k]!=b.nf[k] or not np.array_equal(a.O[k],b.O[k]):raise RuntimeError('old .95 cache')
  count+=1
results=[];source=(P/'core.py').read_text()
for name,old,new in [('fixed_delta','.delta=1-self.V','.delta=.05'),('missing_extra_self','len(self.faces)+self.delta*self.nf[old]','len(self.faces)')]:
 if source.count(old)!=1:raise RuntimeError('mutation unique')
 d=P/'mutants'/name;d.mkdir(parents=True,exist_ok=True);(d/'core.py').write_text(source.replace(old,new));(d/'check.py').write_text((P/'check.py').read_text());r=subprocess.run([sys.executable,'-OO',str(d/'check.py')],capture_output=True,text=True,timeout=180);(d/'stdout').write_text(r.stdout);(d/'stderr').write_text(r.stderr)
 if r.returncode==0 or 'literal decision' not in r.stderr:raise RuntimeError(('mutation not killed mathematically',name,r.returncode,r.stderr))
 results.append(dict(name=name,exit=r.returncode,error=r.stderr))
(P/'SUPPLEMENT_RESULT.json').write_text(json.dumps(dict(old_v095_exact_event_cache_comparisons=count,qualification='fixed finite tape agreement; 1-.95 and literal .05 differ in binary rounding, no all-RNG bitwise equivalence claim',mutants=results),indent=2)+'\n')
print(count,[(r['name'],r['exit']) for r in results])
