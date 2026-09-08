import json,pathlib,numpy as np
from analyze import values_grad
p=pathlib.Path(__file__).resolve().parent;m=np.array(json.loads((p/'MICRO.json').read_text())['oracle'][0]['vector']);v,J=values_grad(m);err=0
for i in range(6):
 d=np.zeros(6);d[i]=1e-5;fd=(values_grad(m+d)[0]-values_grad(m-d)[0])/2e-5;err=max(err,float(np.max(abs(fd-J[:,i]))))
if err>1e-8:raise RuntimeError('Jacobian')
bad=m.copy();bad[3]=bad[2]**2-.1
if values_grad(bad)[0][3]>=0:raise RuntimeError('negative variance lost')
try:values_grad(np.array([1,0,0,0,0,0]))
except ValueError:pass
else:raise RuntimeError('zero S')
(p/'CONTROLS.json').write_text(json.dumps(dict(Jacobian_maxerror=err,negative_variance_preserved=True,zero_denominator_rejected=True,scope='deterministic interface checks, no stochastic production'),indent=2)+'\n')
