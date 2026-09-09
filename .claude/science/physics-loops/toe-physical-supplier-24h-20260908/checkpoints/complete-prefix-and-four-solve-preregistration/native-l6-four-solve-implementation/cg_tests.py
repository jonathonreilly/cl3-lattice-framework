from pathlib import Path
from fractions import Fraction as F
import numpy as np,json
from cg_candidate import solve
from envelope import root_upper
P=Path(__file__).parent;diag=np.arange(1,65,dtype=float);b=np.ones(64);checkpoints=[]
def actual(x):
 # Exact dyadic candidate versus exact integer diagonal/source, independent of recursive r.
 sq=sum((F(1)-F(int(d))*F(float(v)))**2 for d,v in zip(diag,x));return {'rho':root_upper(sq),'exact_residual_squared':str(sq)}
x,c,it=solve(np,lambda v:diag*v,b,actual,lambda i,x,c:checkpoints.append(i),'first')
err=sum((F(float(v))-F(1,int(d)))**2 for d,v in zip(diag,x))
if err>c['rho']**2 or it not in (16,32,48,64) or checkpoints!=list(range(16,it+1,16)):raise ValueError('true error/schedule')
failures=[]
for name,apply,cert in [('negative',lambda v:-v,actual),('recursive_zero',lambda v:v,actual),('cap',lambda v:np.geomspace(1,1e6,64)*v,lambda x:{'rho':F(1)})]:
 try:solve(np,apply,b,cert,lambda *a:None,'first')
 except (ValueError,RuntimeError) as e:failures.append({'case':name,'error':str(e)})
 else:raise ValueError('missing failure '+name)
if '256' not in failures[-1]['error']:raise ValueError('did not reach iteration cap')
print(json.dumps({'status':'PASS','dimension':64,'success_iteration':it,'checkpoints':checkpoints,'exact_error_squared':str(err),'failures':failures,'native_actions':0},indent=2))
