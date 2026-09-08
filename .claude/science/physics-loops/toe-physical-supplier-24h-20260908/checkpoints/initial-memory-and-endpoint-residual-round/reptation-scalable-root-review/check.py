from pathlib import Path
import importlib.util,hashlib,time,json
import numpy as np
p=Path('/private/tmp/toe-24h-probes-20260908/reptation-scalable-core/core.py');s=importlib.util.spec_from_file_location('candidate',p);c=importlib.util.module_from_spec(s);s.loader.exec_module(c)
rng=np.random.default_rng(2026090801440);count=0;start=time.monotonic()
def nf(x,faces):
 # Algebraic alternate: legal exactly when consecutive bit signs all oppose.
 y=1-2*x[faces].astype(int)
 return int(np.all(y*np.roll(y,1,axis=1)==-1,axis=1).sum())
for L in [4,8,12]:
 faces,coef,seed=c.geometry(L,(1,2));affected=c.affected_faces(faces)
 for i in range(64):
  x=rng.integers(0,2,len(seed),dtype=np.uint8);base=nf(x,faces)
  for face in rng.choice(len(faces),16,replace=False):
   y=x.copy();y[faces[face]]^=1;actual=nf(y,faces);got=c.next_count(x,int(face),faces,affected,base)
   if actual!=got:raise RuntimeError((L,face,actual,got))
   # Independent support: predicates outside the exact shared-edge set unchanged.
   allids={j for j,f in enumerate(faces) if set(f)&set(faces[face])}
   if allids!=set(affected[face]):raise RuntimeError('dependency set')
   count+=2
out={'status':'PASS','checks':count,'seconds':time.monotonic()-start,'source_sha':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'Independent alternating-sign recount on arbitrary non-ice bitstrings and literal shared-edge incidence; complements author legal-state/event controls. No stochastic science or mixing test.'};r=Path(__file__).parent;(r/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
