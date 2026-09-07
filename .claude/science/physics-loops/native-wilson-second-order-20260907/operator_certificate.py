"""Exact scalar certificate accompanying an analytical operator proof.

Does not compute spectra or certify infinite-dimensional lemmas numerically.
"""
from fractions import Fraction as F
import json,hashlib
from pathlib import Path
checks=[]
def ck(name,statement):
 if name in checks:raise AssertionError('duplicate check '+name)
 if not statement:raise AssertionError(name)
 checks.append(name)
beta0=2048
ck('exponential geometric remainder domain',F(3,beta0)<1)
extra=F(9,24)/(1-F(3,beta0))
ck('exact saddle exponential remainder coefficient',extra==F(768,2045))
c=29+extra
ck('same-lattice shifted saddle remainder below30',c<30)
insert=(F(1,2)+7*F(1,6))/4
ck('global insertion multiplier norm ceiling',insert==F(5,12))
ratio=F(1000,999)*(F(171,14)+F(2,3)+F(2618,14)*(F(1,12)+F(2,3*beta0)))
ck('imported refined ratio arithmetic',ratio==F(76675625,2685312) and ratio<29)
ck('denominator strictly positive fraction',1-F(1,beta0)-F(2618,14*beta0**2)>F(999,1000))
factor=lambda q:q*(q-7)/4
ck('negative multiplier factor at Q3',factor(F(3))==-3)
ck('positive multiplier factor at Q12',factor(F(12))==15)
ck('two multiplier factors not constant',factor(F(3))!=factor(F(12)))
result=dict(checks=checks,beta0=beta0,global_multiplier_C=29,shifted_saddle_remainder_C=str(c),insertion_norm_ceiling=str(insert),ratio_scalar=str(ratio),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact rational margins only; contraction, dense range, compact sandwich and isolated-eigenvalue perturbation are proved analytically, not inferred from this certificate.')
print(json.dumps(result,indent=2,allow_nan=False))
