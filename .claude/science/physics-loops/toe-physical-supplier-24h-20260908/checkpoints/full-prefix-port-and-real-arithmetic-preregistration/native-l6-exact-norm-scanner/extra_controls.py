from pathlib import Path
from fractions import Fraction as F
import runpy,tempfile,struct,json
P=Path(__file__).parent;s=runpy.run_path(str(P/'scanner.py'));checks=0
for e in (0,1,2,1022,1023,1024,2045,2046):
 for frac in (0,1,(1<<52)-1):
  bits=(e<<52)|frac;x=struct.unpack('<d',struct.pack('<Q',bits))[0]
  if F(s['square'](bits),1<<2148)!=F(x)**2:raise ValueError('transition')
  checks+=1
with tempfile.TemporaryDirectory() as d:
 q=Path(d)/'x';valid=struct.pack('<dddd',1,0,2,0)
 for name,data in [('missing',valid[:16]),('extra',valid+valid[:16]),('truncated',valid[:-1])]:
  q.write_bytes(data)
  try:s['scan'](q,2,0)
  except ValueError:checks+=1
  else:raise ValueError('length '+name)
 q.write_bytes(valid);a=s['scan'](q,2,0);b=s['scan'](q,2,1)
 if a['particle_numerators']==b['particle_numerators']:raise ValueError('parity mutant')
 checks+=1
print(json.dumps({'extra_exact_checks':checks,'full_scan':False}))
