import os,sys,json,contextlib,io,runpy
from pathlib import Path
p=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(p/'check.py'))
import numpy as np
from itertools import product,combinations
states=d['states'];rows=np.array(d['rows']);cols=np.array(d['cols']);fids=np.array(d['faceids']);L=d['L'];planes=list(combinations(range(3),2));links=[(r,a)for r in product(range(2),repeat=3)for a in range(3)];n=len(states);calls=0
for a in range(3):
 for b in range(3):
  if a==b:continue
  O=np.array([sum((-1)**(sum(r)+r[a])*(((int(x)>>i)&1)-.5)/np.sqrt(8)for i,(r,c)in enumerate(links)if c==b)for x in states])
  expected=np.array([.5 if set(planes[int(fi)//8])=={a,b}else0 for fi in fids]);actual=(O[cols]-O[rows])**2
  assert max(abs(actual-expected))<1e-14;calls+=len(actual)
  local=np.bincount(rows,weights=actual,minlength=n)/2;nf=np.bincount(rows,weights=(expected!=0),minlength=n)
  assert max(abs(local-nf/4))<1e-14
  assert abs(np.mean(O*(L@O))-np.mean(local))<1e-14
  # Full double commutator on uniform RK vector, not a fitted derivative.
  Omat=np.diag(O);H=L.toarray();double=2*Omat@H@Omat-Omat@Omat@H-H@Omat@Omat
  assert abs(np.ones(n)@double@np.ones(n)/(2*n)-np.mean(local))<1e-12
print(json.dumps({'directed_update_cases':calls,'modes':6,'plane_count_and_double_commutator_checks':12,'status':'PASS'},indent=2))
