from pathlib import Path
import runpy,numpy as np,json
check=runpy.run_path(str(Path(__file__).with_name('guard.py')))['check'];original=np.multiply;rows=[]
for mode in ('simulated_FTZ','simulated_DAZ'):
 def changed(a,b):
  if mode=='simulated_DAZ':
   a=a.copy();b=b.copy();a[(np.abs(a)>0)&(np.abs(a)<np.finfo(float).tiny)]=0;b[(np.abs(b)>0)&(np.abs(b)<np.finfo(float).tiny)]=0
  z=original(a,b)
  if mode=='simulated_FTZ':z[(np.abs(z)>0)&(np.abs(z)<np.finfo(float).tiny)]=0
  return z
 try:
  np.multiply=changed
  try:check()
  except RuntimeError as e:rows.append({'mode':mode,'caught':str(e)})
  else:raise ValueError('adverse survived')
 finally:np.multiply=original
print(json.dumps({'status':'PASS','simulated_python_ufunc_corruptions':rows,'hardware_environment_changed':False},indent=2))
