import itertools,json,pathlib
import numpy as np
from analyze import stats
checks=0
for n in [2,4,6]:
 for tape in itertools.product([0,1],repeat=10):
  tags=list(range(n+1));d=1;u=lo=hi=0
  for ok in tape:
   if ok:
    tags=tags[1:]+[None] if d==1 else [None]+tags[:-1];u+=d;lo=min(lo,u);hi=max(hi,u)
   else:d=-d
   if (tags[n//2] is not None)!=(hi<=u+n//2<=n+lo):raise RuntimeError('tag identity')
   checks+=1
# Synthetic16chain covariance diagonal and negativeVarH remain signed.
a=np.tile([50.,3.,4.,-.25,.02,-.7,-.9,12.,20.],(16,1));a[:,0]+=np.linspace(-1,1,16);x=stats(a)
if any(r['VarH']>=0 or r['bound_plugin'] is not None for r in x['rows']):raise RuntimeError('variance clipping')
c=np.array(x['estimator_covariance']);se=[x['rows'][h-1][name+'_SE'] for h,name in x['influence_labels']]
if not np.allclose(np.diag(c),np.array(se)**2,atol=1e-20):raise RuntimeError('covariance factor')
pathlib.Path(__file__).with_name('CONTROLS.json').write_text(json.dumps(dict(tag_steps=checks,negative_variance_preserved=True,covariance_diagonal=True,scope='deterministic controls, no production'),indent=2)+'\n')
