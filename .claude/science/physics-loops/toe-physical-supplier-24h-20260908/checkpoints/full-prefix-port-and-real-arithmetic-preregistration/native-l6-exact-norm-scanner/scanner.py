"""Exact binary64 squared norms in units2^-2148; standard library only."""
import struct
DENOMINATOR_EXPONENT=2148

def square(bits):
 exponent=(bits>>52)&2047;fraction=bits&((1<<52)-1)
 if exponent==2047:raise ValueError('nonfinite binary64')
 if exponent==0:return fraction*fraction
 significand=(1<<52)|fraction
 return significand*significand << (2*(exponent-1))

def scan(path,modes,parity,chunk_entries=4096):
 if type(modes) is not int or not 1<=modes<=30 or type(parity) is not int or parity not in (0,1):raise ValueError('domain')
 count=1<<(modes-1);buckets=[0]*(modes+1);seen=0
 with open(path,'rb') as f:
  while True:
   data=f.read(16*chunk_entries)
   if not data:break
   if len(data)%16:raise ValueError('truncated complex pair')
   for real,imag in struct.iter_unpack('<QQ',data):
    if seen>=count:raise ValueError('extra entries')
    low=seen.bit_count();particles=low+(parity^(low&1))
    buckets[particles]+=square(real)+square(imag);seen+=1
 if seen!=count:raise ValueError('missing entries')
 return {'entries':seen,'parity':parity,'modes':modes,'denominator_exponent':2148,'squared_norm_numerator':str(sum(buckets)),'particle_numerators':list(map(str,buckets))}
