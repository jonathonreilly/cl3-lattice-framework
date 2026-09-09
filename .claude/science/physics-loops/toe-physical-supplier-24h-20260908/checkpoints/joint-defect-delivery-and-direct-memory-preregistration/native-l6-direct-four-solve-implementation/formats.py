"""Lossless real NPY / interleaved little-endian complex binary bridge."""
import hashlib
from pathlib import Path

def export(np,source,target,phase='real',expected=1<<20):
 if phase not in ('real','i'):raise ValueError('phase')
 a=np.load(source,allow_pickle=False)
 if a.shape!=(expected,) or a.dtype!=np.dtype('float64') or not np.isfinite(a).all():raise ValueError('real NPY schema')
 target=Path(target)
 if target.exists():raise ValueError('fresh raw')
 with target.open('wb') as f:
  for lo in range(0,len(a),4096):
   x=a[lo:lo+4096];z=np.zeros((len(x),2),dtype='<f8');z[:,0 if phase=='real' else 1]=x;f.write(z.tobytes())
 return {'phase':phase,'entries':len(a),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}

def verify(np,source,raw,phase='real',expected=1<<20):
 if phase not in ('real','i'):raise ValueError('phase')
 a=np.load(source,allow_pickle=False)
 if a.shape!=(expected,) or a.dtype!=np.dtype('float64') or not np.isfinite(a).all():raise ValueError('NPY')
 if Path(raw).stat().st_size!=16*expected:raise ValueError('raw length')
 with open(raw,'rb') as f:
  for lo in range(0,len(a),4096):
   x=a[lo:lo+4096];z=np.frombuffer(f.read(16*len(x)),dtype='<u8').reshape(-1,2)
   if not np.array_equal(z[:,0 if phase=='real' else 1],x.astype('<f8',copy=False).view('<u8')) or np.any(z[:,1 if phase=='real' else 0]):raise ValueError('raw bit identity')
 return True
