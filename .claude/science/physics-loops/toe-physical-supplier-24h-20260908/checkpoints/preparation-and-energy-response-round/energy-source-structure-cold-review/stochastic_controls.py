import ast,json
from pathlib import Path
from types import SimpleNamespace
import numpy as np
p=Path('/private/tmp/toe-24h-probes-20260908/energy-source-structure');checks={}
def ck(k,v):
 assert v,k
 checks[k]=True
# Execute only actual pure functions, removing JIT decoration; no author top-level code.
t=ast.parse((p/'tilted_kernel.py').read_text());names=['branch_value','literal_O','resample'];nodes=[]
for f in t.body:
 if isinstance(f,ast.FunctionDef) and f.name in names:f.decorator_list=[];nodes.append(f)
ix=np.array([2,2,0]);ns={'np':np,'prod':SimpleNamespace(systematic_indices=lambda w:(ix,1.8))}
exec(compile(ast.Module(body=nodes,type_ignores=[]),'<actual-functions>','exec'),ns)
a=np.arange(12).reshape(3,4);c=np.arange(3);o=np.arange(18).reshape(3,6);anc=np.array([8,9,10]);z=ns['resample'](a,c,o,anc,np.zeros(3))
ck('resampling_joint_state_cache_ancestry',all(np.array_equal(g,x[ix]) for g,x in zip(z[:4],[a,c,o,anc])))
z[0][0,0]=-100;ck('resampling_copies',a[2,0]!=-100)
raw=np.load(p/'raw.npz');bits=((raw['states'][:,None]>>np.arange(24))&1).astype(np.uint8)
coeff=np.array([[(-1)**(i//12+(i//6)%2+(i//3)%2+[(i//12),(i//6)%2,(i//3)%2][a])/np.sqrt(8) if i%3==b else 0 for i in range(24)] for a in range(3) for b in range(3) if a!=b])
for k,state in enumerate(bits):
 oo=ns['literal_O'](state,coeff);assert np.max(abs(oo-raw['O'][k]))<1e-12
ck('actual_literal_all864',True)
# Actual ratio function, independently compare full covariance quadratic form.
t=ast.parse((p/'analyze_production.py').read_text());ns2={'np':np};nodes=[f for f in t.body if isinstance(f,ast.FunctionDef) and f.name in ('se','ratio')];exec(compile(ast.Module(body=nodes,type_ignores=[]),'<actual-ratio>','exec'),ns2)
B=np.array([2,3,5,7.]);T=np.array([1,2,2,4.]);r=ns2['ratio'](B,T);gradient=np.array([.5/T.mean(),-.5*B.mean()/T.mean()**2]);cov=np.cov(np.stack([B,T]),ddof=1)/4
ck('ratio_full_covariance',abs(r['SE']**2-gradient@cov@gradient)<1e-14)
ck('nonpositive_denominator',not ns2['ratio'](B,np.zeros(4))['valid'])
ck('replica_negative_retained',ns2['ratio'](B,np.array([-1,1,2,3.]))['valid'])
Path(__file__).with_name('STOCHASTIC_CONTROLS.json').write_text(json.dumps({'checks':checks,'count':len(checks),'scope':'Actual extracted functions; resampling index provider controlled independently, not a full trajectory replication'},indent=2)+'\n');print(checks)
