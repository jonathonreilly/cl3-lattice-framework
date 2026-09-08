import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json
from pathlib import Path
from analysis_core import stats
p=Path(__file__).parent
# Fixed deterministic vectors, no simulated physics data.
a=np.array([[40+i/16,2+i/100,3-i/200,-2+i/1000,4+i/500,-4+i/300,-6+i/400,5+i/50,10+i/40] for i in range(16)])
z=stats(a);cov=np.array(z['estimator_covariance']);se=[r[k+'_SE'] for r in z['rows'] for k in ['D','R','correction','VarH','VarX']]
if not np.allclose(np.diag(cov),np.array(se)**2,rtol=1e-12,atol=1e-18):raise RuntimeError('covariance')
zero=a.copy();zero[:,1:3]=0;out=stats(zero)
if any(r['valid'] for r in out['rows']) or out['influence_labels']:raise RuntimeError('invalid denominator')
# Independently reconstruct gradient by complex-step of ten raw functions.
def fn(m):
 vals=[]
 for j,q in [(1,2-np.sqrt(2)),(2,2)]:
  S=m[j];D=q*(.95*m[0]-m[3])/(512*S);C=m[4+j]/S-m[3]
  vals += [D,D+C,C,m[4]-m[3]**2,m[6+j]-S*S]
 return np.array(vals)
m=a.mean(0);grad=np.array([np.imag(fn(m.astype(complex)+1e-25j*np.eye(9)[k]))/1e-25 for k in range(9)]).T
independent=(a-m)@grad.T
err=float(np.max(abs(independent-np.array(z['chain_influences']))))
if err>1e-14:raise RuntimeError('gradient')
(p/'ANALYSIS_CONTROLS.json').write_text(json.dumps(dict(gradient_max_error=err,covariance_diagonal=True,zero_denominators_explicit_invalid=True,not_production=True),indent=2)+'\n')
