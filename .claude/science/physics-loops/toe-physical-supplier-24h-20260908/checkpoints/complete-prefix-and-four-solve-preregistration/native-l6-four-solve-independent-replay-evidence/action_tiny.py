import sys,importlib.util,json
from pathlib import Path
P=Path('/private/tmp/toe-24h-probes-20260908/native-l6-four-solve-independent-replay')
for name in ('envelope','transport','fp_guard','validate_coefficients','review'):
 s=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m)
import review as r
import numpy as np
# Full 16-dimensional literal CAR matrices, independently assembled.
def mat(j,kind):
 out=np.zeros((16,16))
 for b in range(16):out[b^(1<<j),b]=(-1)**((b&((1<<j)-1)).bit_count())*(2*((b>>j)&1)-1 if kind=='B' else 1)
 return out
center=[(0,.5),(3,.25)];neigh={1:[(1,.5),(2,-.25)],2:[(2,.75)]};freq=[1.,2.,3.,4.];B=sum(c*mat(j,'B') for j,c in center);H=np.diag([sum(freq[j] for j in range(4) if b>>j&1) for b in range(16)])
for v,k in [(1,-2),(2,-2)]:H+=k*B@sum(c*mat(j,'A') for j,c in neigh[v])
for p in (0,1):
 ids=[i|(((i.bit_count()&1)^p)<<3) for i in range(8)];x=np.array([(i-2)/16 for i in range(8)])
 r.same(r.action(x,p,center,neigh,[(1,-2),(2,-2)],freq),H[np.ix_(ids,ids)]@x)
print(json.dumps({'status':'PASS','full_literal_CAR_action_parities':2,'largest_vector':16,'physical_calls':0}))
