"""Read-only runtime census; no eigensolver call."""
from pathlib import Path
import argparse,hashlib,json,os,resource,signal,time,sys,itertools,ctypes,subprocess,runpy
import numpy as np
import numpy.linalg
root=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
paths={Path(sys.executable).resolve()}
for module in list(sys.modules.values()):
 f=getattr(module,'__file__',None)
 if f:
  p=Path(f).resolve()
  if p.is_file() and p.suffix not in ('.pyc','.pyo'):paths.add(p)
# Bind the installed NumPy code/extensions, including lazy linalg imports.
np_root=Path(np.__file__).resolve().parent
for p in np_root.rglob('*'):
 if p.is_file() and p.suffix in ('.py','.so','.dylib'):paths.add(p.resolve())
lib=ctypes.CDLL(None)
lib._dyld_image_count.restype=ctypes.c_uint32
lib._dyld_get_image_name.argtypes=[ctypes.c_uint32];lib._dyld_get_image_name.restype=ctypes.c_char_p
images=[];excluded=[]
for i in range(lib._dyld_image_count()):
 name=lib._dyld_get_image_name(i).decode();p=Path(name)
 if name.startswith(('/System/','/usr/lib/')):
  excluded.append({'path':name,'reason':'macOS system image/shared cache outside file binding'})
 elif p.is_file():paths.add(p.resolve());images.append(name)
 else:excluded.append({'path':name,'reason':'dyld image lacks individually readable file'})
links={}
for p in sorted(paths):
 if p.suffix in ('.so','.dylib'):
  r=subprocess.run(['/usr/bin/otool','-L',str(p)],capture_output=True,text=True)
  if r.returncode:raise RuntimeError('otool failed: '+str(p))
  links[str(p)]=r.stdout
files={str(p):sha(p) for p in sorted(paths) if p!=Path(__file__).resolve()}
result={'status':'runtime-only census; no eigensolver call','interpreter':str(Path(sys.executable).resolve()),'python_version':sys.version,'numpy_version':np.__version__,'platform':os.uname()._asdict() if hasattr(os.uname(),'_asdict') else list(os.uname()),'files':files,'loaded_non_system_images':images,'excluded_system_images':excluded,'extension_linkage':links,'backend':'NumPy build reports macOS Accelerate; system Accelerate/BLAS/LAPACK dyld images are explicitly outside content hash coverage','scope':'All installed NumPy .py/.so/.dylib, imported file-backed modules and readable loaded non-system libraries. OS/shared-cache binaries and future changes there are not certified.'}
(root/'RUNTIME.json').write_text(json.dumps(result,indent=2)+'\n');print(len(files),len(excluded))
