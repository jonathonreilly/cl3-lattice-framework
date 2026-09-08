from fractions import Fraction as F
from exact_certificate import certificate,sqrt_bounds
import json
D=[[0j]*16 for _ in range(16)];Q=[[0j]*16 for _ in range(16)]
for i in range(16):D[i][i]=i;Q[i][i]=1
r=certificate(D,Q,list(range(16)),0)
if F(r['eta']) or F(r['residual']) or F(r['eigenvalue_radius']):raise ValueError('exact diagonal certificate')
for x in (F(0),F(1),F(2),F(17,29)):
 a,b=sqrt_bounds(x)
 if not a*a<=x<=b*b:raise ValueError('outward square root')
wrong=[x.copy() for x in Q];wrong[0][0]=0
try:certificate(D,wrong,list(range(16)),0)
except ValueError as e:
 if 'Gram' not in str(e):raise
else:raise ValueError('bad Gram survived')
# A complex phase column remains exactly unitary and solves diagonal D.
Q[3][3]=1j
z=certificate(D,Q,list(range(16)),0)
if F(z['residual']) or F(z['eta']):raise ValueError('complex certificate')
# Deliberately wrong finite eigenvalues still get nonzero certified residual.
w=certificate(D,Q,[i+.25 for i in range(16)],0)
if F(w['residual'])<=0 or F(w['eigenvalue_radius'])<F(1,4):raise ValueError('wrong candidate residual')
print(json.dumps(dict(controls=8,scope='synthetic exact arithmetic only; no eigensolver')))
