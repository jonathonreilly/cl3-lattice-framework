from pathlib import Path
import runpy,json,math,hashlib
import numpy as np
p=Path(__file__).parent;q=p.parent/'native-l6-adapted-fock-transports';t=runpy.run_path(str(q/'transport.py'));count=0;wrong=0
# Independent two-mode exterior enumeration with additional low spectators.
for index in range(48):
 E,T,det=t['blocks'](index);R=np.array([[float(a)+float(b)*math.sqrt(3) for a,b in row] for row in E]);U=np.zeros((4,4));U[0,0]=1;U[1:3,1:3]=R;U[3,3]=det
 for low in (1,2,4):
  for parity in (0,1):
   n=1<<low;x=np.array([complex(i-3,(i%3)-1) for i in range(2*n)]);expect=np.zeros_like(x)
   for b in range(2*n):
    high=parity^(b.bit_count()%2);local=((b>>low)&1)|(high<<1);rest=b&(n-1)
    for target in range(4):
     if U[target,local]:
      a=rest|((target&1)<<low)
      if (target>>1)!=(parity^(a.bit_count()%2)):raise ValueError('parity')
      expect[a]+=U[target,local]*x[b]
   got=x.copy();t['_last_eg'](got,low,parity,R,det)
   if np.max(abs(got-expect))>1e-12:raise ValueError('top compressed')
   count+=1
   if det==-1:
    bad=x.copy();t['_last_eg'](bad,low,parity,R,1);wrong+=np.max(abs(bad-expect))>1e-12
if wrong==0:raise ValueError('mutant')
(p/'RESULT.json').write_text(json.dumps({'actual_tiny_top_checks':count,'missing_determinant_mismatches':int(wrong),'physical_apply_calls':0},indent=2)+'\n')
