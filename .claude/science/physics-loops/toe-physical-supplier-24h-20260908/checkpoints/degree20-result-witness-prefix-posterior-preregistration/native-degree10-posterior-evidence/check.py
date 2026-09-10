from pathlib import Path
from fractions import Fraction as F
import types,json
P=Path('/private/tmp/toe-24h-probes-20260908/native-degree10-posterior-certificate-design/posterior.py');m=types.ModuleType('p');exec(compile(P.read_bytes(),str(P),'exec'),m.__dict__)
s={'P':['8','8'],'O':['8','8']};gate={'E':['0','0'],'F':['0','0'],'nominal':['2','2']};x=m.evaluate(s,{'P':'0','O':'0'},gate);assert x['a_squared_upper']==15 and x['b_squared_upper']==0 and x['error_upper']==0 and x['alpha_interval']==(F(1,4),F(1,4));checks=4
for q in [F(0),F(1,3),F(17),F(999,7)]:
 y=m.upper_root(q);assert y*y>=q and (y-F(1,2**256))**2<q if q else y==0;checks+=1
# Scalar polarization and both mixed decompositions on fixed real vectors.
for u in [-2,-1,1,2]:
 x=F(u);xh=F(1);v=F(2);vh=F(-1);E=abs(x-xh);Fv=abs(v-vh);a=abs(xh);b=abs(vh);chi=abs(x);psi=abs(v)
 error=6*(E*(a+chi)+min(E*b+chi*Fv,E*psi+a*Fv));truth=abs(6*(x*x-x*v-xh*xh+xh*vh));assert truth<=error;checks+=1
print(json.dumps({'status':'PASS','checks':checks,'scope':'synthetic scalar posterior algebra and exact upward roots; no saved events/values'}))
