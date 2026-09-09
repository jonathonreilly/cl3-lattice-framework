"""Real ndarray exact scan adapter, unprofiled; no import-time scan."""
import struct
from fractions import Fraction as F
from exact_square import square
from envelope import root_upper

def scan(np,x,parity):
 if x.shape!=(1<<20,) or x.dtype!=np.dtype('float64') or parity not in (0,1):raise ValueError('real norm domain')
 buckets=[0]*22;index=0
 for lo in range(0,len(x),4096):
  for (bits,) in struct.iter_unpack('<Q',x[lo:lo+4096].astype('<f8',copy=False).tobytes()):
   k=index.bit_count();k+=parity^(k&1);buckets[k]+=square(bits);index+=1
 total=F(sum(buckets),1<<2148)
 return root_upper(total),buckets
