import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys,pathlib,json,hashlib,importlib.util,ast
import numpy as np
sys.dont_write_bytecode=True
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908/reptation-propagated-l4');O=pathlib.Path(__file__).parent
f=json.loads((P/'PRODUCTION_FREEZE.json').read_text())
for n,h in f.items():
 if hashlib.sha256((P/n).read_bytes()).hexdigest()!=h:raise RuntimeError('binding')
s=importlib.util.spec_from_file_location('review_stats',P/'analyze.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
a=np.array([[50+.3*i,3+.01*i,4+.02*(i%5),-.3+.002*i,.12+.001*(i%3),-.8+.005*i,-1+.003*i,12+.04*i,20+.06*i] for i in range(16)])
def fun(x):
 N,S,T,E,H2,SE,TE,S2,T2=x;out=[]
 for q,z,ze,z2 in ((2,S,SE,S2),(4,T,TE,T2)):
  d=q*(.95*N-E)/(64*z);c=ze/z-E;out.extend([d,d+c,c,H2-E*E,z2-z*z])
 return np.array(out)
z=a.mean(0);J=np.empty((10,9))
for j in range(9):
 w=z.astype(complex);w[j]+=1e-25j;J[:,j]=fun(w).imag/1e-25
cov=J@np.cov(a,rowvar=False)@J.T/16;v=fun(z);actual=m.stats(a);vals=np.array([r[k] for r in actual['rows'] for k in ('D','R','correction','VarH','VarX')]);err=float(max(abs(v-vals)));ce=float(np.max(abs(cov-actual['estimator_covariance'])))
if err>1e-13 or ce>1e-13:raise RuntimeError('formula/cov')
# Actual producer vector expression retains all same-time terms, with independent supplied scalar values.
tree=ast.parse((P/'production.py').read_text());expr=next(n.value for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='v' for t in n.targets))
class A:nf=[4,7,9]
actualv=eval(compile(ast.Expression(expr),'actual_vector','eval'),{'a':A(),'x1':2.,'x2':3.,'hl':-.2,'hr':-.45,'e':-.325})
expected=[7,2,3,-.325,.09,-.65,-.975,4,9]
if max(abs(np.array(actualv)-expected))>1e-15:raise RuntimeError('producer vector')
# Wrong same-endpoint square and omitted covariance are deliberately distinguishable.
if abs((-.2)**2-expected[4])<1e-6 or max(abs(v[[1,6]]-v[[0,5]]))<1e-6:raise RuntimeError('adverse witness')
out={'freeze_sha':hashlib.sha256((P/'PRODUCTION_FREEZE.json').read_bytes()).hexdigest(),'bindings':f,'estimate_residual':err,'covariance_residual':ce,'actual_same_time_vector':actualv,'wrong_endpoint_square_distinguished':True,'omitted_correction_distinguished':True,'scope':'Deterministic algebra/AST controls, no production or micro.'}
(O/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='bindings'},indent=2))
