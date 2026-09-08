from pathlib import Path
import sys,hashlib,json,io,contextlib,os
import numpy as np
def current():
 # Tiny deterministic import exercise only, not a cost fixture or coefficient.
 np.linalg.solve(np.eye(1),np.ones(1));b=io.BytesIO();np.savez(b,x=np.zeros((1,1)));np.load(io.BytesIO(b.getvalue()),allow_pickle=False).close()
 files={str(Path(sys.executable).resolve()):hashlib.sha256(Path(sys.executable).resolve().read_bytes()).hexdigest()}
 modules={}
 for name,m in sorted(sys.modules.items()):
  if name=='numpy' or name.startswith('numpy.'):
   for kind in ('__file__','__cached__'):
    f=getattr(m,kind,None)
    if f and Path(f).is_file():
     f=str(Path(f).resolve());files[f]=hashlib.sha256(Path(f).read_bytes()).hexdigest();modules[name+':'+kind]=f
 text=io.StringIO()
 with contextlib.redirect_stdout(text):np.show_config()
 libraries={}
 if sys.platform=='darwin':
  import ctypes
  dyld=ctypes.CDLL(None);dyld._dyld_image_count.restype=ctypes.c_uint32;dyld._dyld_get_image_name.argtypes=[ctypes.c_uint32];dyld._dyld_get_image_name.restype=ctypes.c_char_p
  for i in range(dyld._dyld_image_count()):
   f=dyld._dyld_get_image_name(i).decode()
   if any(t in f.lower() for t in ('numpy','openblas','accelerate','veclib')):
    libraries[f]=hashlib.sha256(Path(f).read_bytes()).hexdigest() if Path(f).is_file() else 'system_shared_cache_not_file'
 return {'files':files,'modules':modules,'libraries':libraries,'numpy_version':np.__version__,'python_version':sys.version,'optimization':sys.flags.optimize,'backend':text.getvalue()}
def verify(path):
 expected=json.loads(Path(path).read_text());actual=current()
 if actual!=expected:raise RuntimeError('runtime closure changed')
 return hashlib.sha256(Path(path).read_bytes()).hexdigest()
if __name__=='__main__':
 Path(__file__).with_name('RUNTIME.json').write_text(json.dumps(current(),indent=2)+'\n')
