from pathlib import Path
from fractions import Fraction as F
import runpy,struct,json,tempfile
p=Path(__file__).parent;r=runpy.run_path(str(p/'replay.py'));count=0
# Exact independent Fraction normalization, including exponent extremes.
values=[0.,-0.,1.,-1.,1.5,float.fromhex('0x0.0000000000001p-1022'),float.fromhex('0x0.fffffffffffffp-1022'),float.fromhex('0x1p-1022'),float.fromhex('0x1.fffffffffffffp+1023')]
for x in values:
 if F(r['exact_square'](x),1<<2148)!=F(x)**2:raise ValueError('square')
 count+=1
with tempfile.TemporaryDirectory(dir=p) as d:
 path=Path(d)/'tiny.bin'
 for modes in range(1,6):
  n=1<<(modes-1);z=[(values[i%len(values)],values[(i+3)%len(values)]) for i in range(n)];path.write_bytes(b''.join(struct.pack('<dd',a,b) for a,b in z))
  for parity in (0,1):
   got=r['scan'](path,modes,parity,3);expected=[F(0)]*(modes+1)
   states=[b for b in range(1<<modes) if b.bit_count()%2==parity];lookup={b&((1<<(modes-1))-1):b.bit_count() for b in states}
   for i,(a,b) in enumerate(z):expected[lookup[i]]+=F(a)**2+F(b)**2
   if [F(int(x),1<<2148) for x in got['particle_numerators']]!=expected:raise ValueError('buckets')
   count+=1
 for raw in [b'0',b'\0'*32,struct.pack('<dd',float('nan'),0),struct.pack('<dd',float('inf'),0)]:
  path.write_bytes(raw)
  try:r['scan'](path,1,0)
  except ValueError:count+=1
  else:raise ValueError('malformed survived')
 for modes,parity,chunk in [(True,0,1),(1,2,1),(1,0,0)]:
  try:r['scan'](path,modes,parity,chunk)
  except ValueError:count+=1
  else:raise ValueError('domain survived')
print(json.dumps({'status':'PASS','predicates':count,'maximum_fixture_entries':16,'author_imports':False,'full_scans':0}))
