from fractions import Fraction as F
from itertools import product
import json,hashlib
from pathlib import Path
checks={}
def check(k,p):
 if not p:raise AssertionError(k)
 checks[k]=True
for m in range(2,6):
 edges=[(j,j+1) for j in range(m-1)]+[(j,m+j) for j in range(m)]+[(0,2*m)]
 byleaf={}
 for bits in product((0,1),repeat=2*m):
  occ=tuple(sum(bits[k] for k,e in enumerate(edges) if j in e)%2 for j in range(2*m+1))
  key=occ[m:2*m];byleaf.setdefault(key,[]).append(occ)
 check(f'm{m}_all_ready_choices',len(byleaf)==2**m)
 check(f'm{m}_uniform_full_matter',all(len(rows)==2**m and len({x[:m] for x in rows})==2**m for rows in byleaf.values()))
 check(f'm{m}_reservoir_parity',all(x[-1]==sum(x[:-1])%2 for rows in byleaf.values() for x in rows))
# beta=2log2, energies integral. All factors exact; covers zero and repeated modes.
for label,eps in [('zero',(0,0)),('odd_zero',(-1,0,1)),('degenerate',(-1,-1,1,1))]:
 vals=[];pref=F(2)**sum(min(e,0) for e in eps)
 for occ in product((0,1),repeat=len(eps)):
  leaf=F(1)
  for e,n in zip(eps,occ):leaf*=F(2)**(-abs(e)*(n if e>=0 else 1-n))
  target=pref*F(2)**(-sum(e*n for e,n in zip(eps,occ)))
  check(label+'_operator_'+''.join(map(str,occ)),leaf==target)
  vals.append(leaf*leaf)
 pred=F(1)
 for e in eps:pred*=(1+F(4)**(-abs(e)))/2
 check(label+'_trace_probability',sum(vals)/2**len(eps)==pred)
 check(label+'_contraction',max(vals)<=1)
print(json.dumps({'checks':checks,'count':len(checks),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'New exact incidence and modal zero/degeneracy support, not a rerun of 197 author checks.'},indent=2))
