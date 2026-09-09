from pathlib import Path
from fractions import Fraction as F
import runpy,struct,tempfile,json
P=Path(__file__).parent;ns=runpy.run_path(str(P/'scanner.py'));patterns=[0,1,2,(1<<52)-1,1<<52,(1023<<52),(2046<<52)|((1<<52)-1),1<<63,(1<<63)|1];count=0
for bits in patterns:
 x=struct.unpack('<d',struct.pack('<Q',bits))[0]
 if F(ns['square'](bits),1<<2148)!=F(x)**2:raise ValueError('exact square')
 count+=1
for p in (0,1):
 with tempfile.TemporaryDirectory() as tmp:
  q=Path(tmp)/'x.bin';vals=[(patterns[i%len(patterns)],patterns[-1-i%len(patterns)]) for i in range(16)];q.write_bytes(b''.join(struct.pack('<QQ',a,b) for a,b in vals));z=ns['scan'](q,5,p,3);b=[F(0)]*6
  for i,(a,c) in enumerate(vals):
   n=i.bit_count();n+=p^(n&1);b[n]+=sum(F(struct.unpack('<d',struct.pack('<Q',x))[0])**2 for x in (a,c))
  if [F(int(x),1<<2148) for x in z['particle_numerators']]!=b:raise ValueError('particle buckets')
  count+=1
for bad in (2047<<52,(2047<<52)|1):
 try:ns['square'](bad)
 except ValueError:count+=1
 else:raise ValueError('nonfinite accepted')
# Actual arithmetic mutant drops normal hidden bit.
mut=dict(ns);exec(compile((P/'scanner.py').read_text().replace('significand=(1<<52)|fraction','significand=fraction'),'mutant','exec'),mut)
if mut['square'](1023<<52)==ns['square'](1023<<52):raise ValueError('mutant survives')
print(json.dumps({'exact_checks':count,'hidden_bit_mutant_killed':True,'full_vector_scan':False}))
