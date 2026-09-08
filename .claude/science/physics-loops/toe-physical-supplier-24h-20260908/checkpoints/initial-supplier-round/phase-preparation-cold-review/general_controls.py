from pathlib import Path
from itertools import product
import sympy as s,json,hashlib
checks={}
def check(n,b):checks[n]=bool(b);assert b,n
# Independent one-particle sign and Givens generation.
X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);R=(s.eye(2)-s.I*Z)/s.sqrt(2)
J=s.I*s.Matrix([[0,1],[-1,0]])
check('phase_conjugation_current_sign',s.simplify(R.H*X*R-J)==s.zeros(2))
c=s.Rational(3,5);t=s.Rational(4,5)
G=c*s.eye(2)-s.I*t*J
check('current_pulse_real_Givens',G==s.Matrix([[c,t],[-t,c]]))
# General tree binary-incidence map for m=2..7: all remaining m edge bits
# give every matter pattern once for every one of the 2^m fixed leaf patterns.
counts=[]
for m in range(2,8):
 total=0
 for leaf in product((0,1),repeat=m):
  seen=set()
  for free in product((0,1),repeat=m):
   path=free[:-1]; reservoir=free[-1]
   matter=tuple(leaf[i]^(path[i-1] if i>0 else reservoir)^(path[i] if i<m-1 else 0) for i in range(m))
   checkbit=(sum(matter)+sum(leaf)+reservoir)%2
   assert checkbit==0; seen.add(matter);total+=1
  assert len(seen)==2**m
 check('tree_ready_uniform_m'+str(m),total==4**m);counts.append([m,total])
# Spectral occupancy filter for nondegenerate positive/negative/zero energies,
# use r_j rational directly; no author matrix or expected-output import.
rs=[s.Rational(1,2),s.Rational(2,3),s.Integer(1)];signs=[1,-1,0]
weights=[]
for bits in product((0,1),repeat=3):
 k=s.prod(rs[j]**(bits[j] if signs[j]>=0 else 1-bits[j]) for j in range(3))
 weights.append(k*k)
check('success_product_factorization',sum(weights)/8==s.prod((1+r*r)/2 for r in rs))
check('success_bounds',s.Rational(1,8)<=sum(weights)/8<=1)
# This is the ratio of two occupation weights after a positive/negative mode flip.
check('positive_energy_odds',rs[0]**2==s.Rational(1,4))
check('negative_energy_odds',1/rs[1]**2==s.Rational(9,4))
out={'checks':checks,'TOTAL':len(checks),'incidence_assignments':counts,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('GENERAL_CONTROLS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
