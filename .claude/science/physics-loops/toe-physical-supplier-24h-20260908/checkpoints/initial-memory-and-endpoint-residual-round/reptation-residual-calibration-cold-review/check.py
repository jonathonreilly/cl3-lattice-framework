import ast, pathlib, hashlib, json, importlib.util, sys
import numpy as np
sys.dont_write_bytecode=True
p=pathlib.Path('/private/tmp/toe-24h-probes-20260908/reptation-residual-calibration')
spec=importlib.util.spec_from_file_location('reviewed_analyzer',p/'analyze.py');a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
f=json.loads((p/'PRODUCTION_FREEZE.json').read_text())
for n,h in f.items():
 if hashlib.sha256((p/n).read_bytes()).hexdigest()!=h:raise RuntimeError('freeze')
m=np.array(next(x for x in json.loads((p/'MICRO.json').read_text())['oracle'] if x['n']==2)['vector'])
v,J=a.values_grad(m)
N,S,E,H2,XE,X2=m
expected=np.array([(.95*N-E)/(2*S),(.95*N-E)/(2*S)+XE/S-E,XE/S-E,H2-E*E,X2-S*S])
if not np.allclose(v,expected,rtol=0,atol=1e-14):raise RuntimeError('formula')
errs=[]
for j in range(6):
 z=m.astype(complex);z[j]+=1e-25j
 # independent analytic expression evaluated with complex step
 N,S,E,H2,XE,X2=z
 w=np.array([(.95*N-E)/(2*S),(.95*N-E)/(2*S)+XE/S-E,XE/S-E,H2-E*E,X2-S*S])
 errs.append(float(np.max(abs(w.imag/1e-25-J[:,j]))))
if max(errs)>1e-12:raise RuntimeError('Jacobian')
bad=m.copy();bad[3]=bad[2]**2-.1
if a.values_grad(bad)[0][3]>=0:raise RuntimeError('signed variance')
try:a.values_grad(np.array([1,0,0,0,0,0]))
except ValueError:pass
else:raise RuntimeError('zero S')
# Execute exactly the actual footer hash expression, with production's imports, without its sampling loop.
tree=ast.parse((p/'production.py').read_text());expr=next(n for n in ast.walk(tree) if isinstance(n,ast.keyword) and n.arg=='source_sha').value
env={'hashlib':hashlib,'pathlib':pathlib,'__file__':str(p/'production.py')}
try:eval(compile(ast.Expression(expr),'actual_source_hash_footer','eval'),env)
except NameError as e:footer={'status':'BLOCKER','error':str(e)}
else:footer={'status':'PASS'}
out={'freeze_sha':hashlib.sha256((p/'PRODUCTION_FREEZE.json').read_bytes()).hexdigest(),'bound_files':f,'formula_max_error':float(max(abs(v-expected))),'complex_step_Jacobian_max_error':max(errs),'signed_variance_retained':True,'zero_S_rejected':True,'actual_footer':footer,'scope':'No production or micro; actual footer AST evaluated independently of sampling.'}
pathlib.Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
