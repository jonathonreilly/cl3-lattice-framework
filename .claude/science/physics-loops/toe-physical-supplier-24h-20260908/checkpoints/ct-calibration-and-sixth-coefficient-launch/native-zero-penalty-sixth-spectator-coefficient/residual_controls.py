from fractions import Fraction as F
import json,hashlib
from pathlib import Path
import solver_core as c
A=c.np.array([[2.,1.],[1.,3.]]);b=c.np.array([.5,-.25]);target=(F(-7,20),F(1,5));rows=[]
for x in (c.np.zeros(2),c.np.array([-.35,.2]),c.np.array([10.,-7.])):
 e,r=c.residual_certificate(A,0.,x,b,0.,1.)
 sq=sum((F.from_float(float(a))-z)**2 for a,z in zip(x,target))
 if sq>F.from_float(e)**2:raise RuntimeError('bound misses exact solution')
 rows.append({'x':x.tolist(),'error_bound':e,'exact_squared_error':str(sq)})
print(json.dumps({'PASS':True,'rows':rows,'scope':'Exact rational a posteriori controls, including deliberately inaccurate solves','solver_sha256':hashlib.sha256(Path(c.__file__).read_bytes()).hexdigest()},indent=2))
