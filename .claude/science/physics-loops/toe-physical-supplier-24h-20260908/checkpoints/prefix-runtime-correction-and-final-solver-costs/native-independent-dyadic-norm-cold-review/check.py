import runpy,struct,json,hashlib,tempfile,subprocess
from pathlib import Path
from fractions import Fraction as F
s=Path('/private/tmp/toe-24h-probes-20260908/native-independent-dyadic-norm-replay');out=Path(__file__).parent
r=runpy.run_path(str(s/'replay.py'));count=0
# Independent integer-bit decoding, contrasting the reviewed float-ratio path.
words=[0,1,0xfffffffffffff,0x10000000000000,0x3ff0000000000000,0x3ff123456789abcd,0x7fefffffffffffff]
for w in words+[w|(1<<63) for w in words]:
 x=struct.unpack('<d',struct.pack('<Q',w))[0];e=(w>>52)&2047;m=w&((1<<52)-1)
 if e:m|=1<<52
 shift=0 if e==0 else 2*(e-1)
 if r['exact_square'](x)!=(m*m<<shift):raise ValueError('independent bit square')
 count+=1
with tempfile.TemporaryDirectory(dir=out) as td:
 p=Path(td)/'x';raw=b''.join(struct.pack('<dd',i-3,(i+1)/8) for i in range(8));p.write_bytes(raw)
 for parity in [0,1]:
  z=r['scan'](p,4,parity,2);sums=[F(0)]*5
  for full in range(16):
   if bin(full).count('1')%2==parity:
    i=full&7;sums[bin(full).count('1')]+=F(i-3)**2+F(i+1,8)**2
  if [F(int(x),1<<2148) for x in z['particle_numerators']]!=sums:raise ValueError('parity')
  if z['input_sha256']!=hashlib.sha256(raw).hexdigest():raise ValueError('hash')
  count+=2
 result={'predicates':count,'max_entries':8,'status':'PASS','full_scans':0}
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'READ_HASHES.json').write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in s.iterdir() if p.is_file()},indent=2)+'\n')
print(result)
