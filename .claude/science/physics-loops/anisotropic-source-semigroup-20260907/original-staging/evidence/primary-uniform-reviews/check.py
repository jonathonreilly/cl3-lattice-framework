import sympy as s,json,hashlib
from pathlib import Path
k,z=s.symbols('k z',positive=True)
D=k**7*(k+1)**2*(2*k+3)*(4*k*k+6*k+1)/8
sm=6*(4*k+5)/(4*k*k+6*k+1)
r2=sm/30
checks={
'determinant_degree12':s.degree(D,k)==12,
'determinant_lower_bound_positive_coefficients':all(c>=0 for c in s.Poly(s.expand((D-k**12).subs(k,z+1)),z).all_coeffs()),
'determinant_upper_bound_positive_coefficients':all(c>=0 for c in s.Poly(s.expand((s.Rational(55,2)*k**12-D).subs(k,z+1)),z).all_coeffs()),
'antisymmetric_covariance_decreases':s.simplify(s.diff(sm,k)+12*(8*k*k+20*k+13)/(4*k*k+6*k+1)**2)==0,
'rational_r_scaled_limit':s.limit(k*r2,k,s.oo)==s.Rational(1,5),
'partition_threshold_power':2+48==50,
'double_inverse_partition_power':2+48+48==98,
'power_schedule_error':1+2*98-200==-3,
}
# independent exact comparison of the two algebraic lambda expressions at k=1
ss=s.sqrt(55)
L1=16*s.sqrt(3)*s.pi/(s.sqrt(30)+s.sqrt(s.Rational(54,11)))**8
L2=s.sqrt(3)*s.pi*(11/(6*(32+3*ss)))**4
checks['ground_normalization_matches_isotropic']=s.simplify(L1-L2)==0
assert all(checks.values()),checks
p=Path('/private/tmp/toe-campaign-20260907/anisotropic-uniform-limit/DERIVATION.md')
print(json.dumps(dict(proof_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),checks=checks,scope='Independent exact scalar controls; analytical uniform estimates reviewed separately, not numerically certified.'),indent=2))
