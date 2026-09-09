"""Fixed exact return-series and rational logarithm lower bound. No spectral run."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json,signal,time
signal.alarm(30);start=time.monotonic();N=100;fac=[factorial(i) for i in range(2*N+1)];s=F(1)
for n in range(1,N+1):
 count=0
 for a in range(n+1):
  for b in range(n-a+1):
   c=n-a-b;count+=fac[2*n]//(fac[a]**2*fac[b]**2*fac[c]**2)
 s+=F(count,6**(2*n))
if not s<F(3,2):raise ValueError('return partial bound')
a=F(17,60);z=[F(8,9),F(0),-(4*a/9+8*a*a),F(0),-4*a*a/9]
def mul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
power=[F(1)];integral=F(0)
for n in range(1,13):
 power=mul(power,z);integral+=sum(v/F(i+1) for i,v in enumerate(power))/n
lower=F(7,44)*integral
if not lower>F(1,6):raise ValueError('gap comparison')
print(json.dumps({'return_cutoff':N,'return_partial_exact':str(s),'return_partial_less_than':'3/2','tail_upper':'1/5','A0_upper':'17/60','log_terms':12,'gap_lower_exact':str(lower),'gap_lower_exceeds_1_6':True,'seconds':time.monotonic()-start,'physical_runs':0},indent=2))
