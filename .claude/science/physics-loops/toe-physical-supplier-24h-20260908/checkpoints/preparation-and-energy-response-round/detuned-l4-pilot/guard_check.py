import ast,json,hashlib
from pathlib import Path
import numpy as np
from types import SimpleNamespace
p=Path(__file__).resolve().parent;s=(p/'pilot.py').read_text();tree=ast.parse(s)
f=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='validate')
ns={'np':np,'prod':SimpleNamespace(count_flippable=lambda x,y:0),'g':SimpleNamespace(plaquette_links=None),'L':4,'vertex_degrees':lambda x:np.array([3]),'electric_flux':lambda x:(0,0,0)}
exec(compile(ast.Module(body=[f],type_ignores=[]),'actual_validate','exec',optimize=2),ns)
a=np.zeros((1,192),dtype=np.uint8);c=np.zeros(1);checks={}
for name,state,counts in [('binary',np.full((1,192),2,dtype=np.uint8),c),('count',a,np.ones(1))]:
 try:ns['validate'](state,counts)
 except AssertionError:checks[name]=True
 else:raise RuntimeError(name)
ns['vertex_degrees']=lambda x:np.array([2])
try:ns['validate'](a,c)
except AssertionError:checks['Gauss']=True
else:raise RuntimeError('Gauss')
ns['vertex_degrees']=lambda x:np.array([3]);ns['electric_flux']=lambda x:(1,0,0)
try:ns['validate'](a,c)
except AssertionError:checks['flux']=True
else:raise RuntimeError('flux')
guard=next(n for n in ast.walk(tree) if isinstance(n,ast.If) and any(isinstance(r,ast.Raise) and isinstance(r.exc,ast.Call) and r.exc.args and isinstance(r.exc.args[0],ast.Constant) and r.exc.args[0].value=='imaginary C0' for r in n.body))
try:exec(compile(ast.Module(body=[guard],type_ignores=[]),'actual_imag_guard','exec',optimize=2),{'np':np,'raw':np.array([1j])})
except AssertionError:checks['imaginary']=True
else:raise RuntimeError('imaginary')
print(json.dumps({'checks':checks,'count':len(checks),'actual_source_sha256':hashlib.sha256((p/'pilot.py').read_bytes()).hexdigest(),'scope':'Actual extracted failure guards compiled with optimize2; no stochastic run.'},indent=2))
