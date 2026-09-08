import importlib.util,numpy as np,json
from pathlib import Path
p=Path('/private/tmp/toe-24h-probes-20260908/rk-resolvent-size-ladder');spec=importlib.util.spec_from_file_location('authoranalysis',p/'analyze.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
rng=np.random.default_rng(919191);N=100+rng.normal(size=128);S=2+.1*rng.normal(size=(128,2));Y=.4+.01*rng.normal(size=(128,2,3));I=np.zeros_like(Y);r=m.summarize(N,S,Y,I,8)
X=np.column_stack([N,S,Y.reshape(128,6)]);mean=X.mean(0)
def f(x):
 vals=[]
 for h in range(2):
  q=4*np.sin(np.pi*(1 if h==0 else 2)/8)**2;a=q*x[0]/512/x[1+h]
  for j,k in enumerate((.25,.5,1)):
   al=k*q/2 if h==0 else k;rr=x[3+3*h+j]/(al*x[1+h]);vals.extend([a,rr,1/rr-al,(a+al)*rr])
 return np.array(vals)
J=np.zeros((24,9))
for j in range(9):
 dx=np.zeros(9);dx[j]=1e-5;J[:,j]=(f(mean+dx)-f(mean-dx))/2e-5
expected=(X-mean)@J.T;actual=np.array(r['influences']);error=float(np.max(abs(expected-actual)))
if error>1e-8:raise AssertionError('joint gradient')
if np.max(abs(np.cov(expected,rowvar=False)-r['influence_sample_covariance']))>1e-9:raise AssertionError('joint covariance')
Path(__file__).with_name('ANALYSIS_CONTROL.json').write_text(json.dumps(dict(all24_joint_gradients=True,cross_covariance=True,max_residual=error),indent=2)+'\n');print(error)
