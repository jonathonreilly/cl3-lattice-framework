"""Real binary64 candidate only. No physical-sized execution on import."""
import math
import numpy as np

def parity(a):
 z=a.copy()
 for s in (32,16,8,4,2,1):z^=z>>s
 return z&1

def apply(x,modes,sector,p,q,theta,kind='AA',inverse=False,chunk=4096):
 if not isinstance(modes,int) or not 2<=modes<=32 or sector not in (0,1):raise ValueError('modes/parity')
 if not isinstance(p,int) or not isinstance(q,int) or not 0<=p<q<modes or kind not in ('AA','BB'):raise ValueError('plane')
 if not isinstance(chunk,int) or not 1<=chunk<=4096:raise ValueError('chunk')
 if not isinstance(x,np.ndarray) or x.dtype!=np.dtype('float64') or x.shape!=(1<<(modes-1),) or not x.flags.c_contiguous or not x.flags.writeable:raise ValueError('real contiguous writable vector')
 if not math.isfinite(theta):raise ValueError('angle')
 c=math.cos(theta/2);s=math.sin(theta/2)*(-1 if inverse else 1);top=modes-1;mask=(1<<p)-1;toggle=(1<<p)^((1<<q) if q<top else 0)
 for lo in range(0,len(x)//2,chunk):
  k=np.arange(lo,min(lo+chunk,len(x)//2),dtype=np.uint64)
  i=(k&mask)|((k>>p)<<(p+1));j=i^toggle
  bits=i|((parity(i)^sector)<<top)
  # Input-column action: right generator q, then p on toggled occupation.
  g=1-2*(parity(bits&((1<<q)-1))^parity((bits^(1<<q))&((1<<p)-1))).astype(np.int8)
  if kind=='BB':g=g*(2*((bits>>q)&1).astype(np.int8)-1)*(2*((bits>>p)&1).astype(np.int8)-1)
  a=x[i].copy();b=x[j].copy()
  if not np.isfinite(a).all() or not np.isfinite(b).all():raise ValueError('nonfinite input')
  if theta==0:continue
  sg=np.multiply(s,g);u=np.subtract(np.multiply(c,a),np.multiply(sg,b));v=np.add(np.multiply(c,b),np.multiply(sg,a))
  if not np.isfinite(u).all() or not np.isfinite(v).all():raise ValueError('nonfinite result')
  x[i]=u;x[j]=v
 return x
