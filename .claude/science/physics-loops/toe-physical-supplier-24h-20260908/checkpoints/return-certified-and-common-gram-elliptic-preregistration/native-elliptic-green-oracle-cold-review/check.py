from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,hashlib,types
P=Path(__file__).resolve().parent;B=P.parent;A=B/'native-elliptic-green-oracle-stretch'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1<<20),b''):h.update(block)
 return h.hexdigest()
f=json.loads((A/'FREEZE.json').read_text());bad=[]
for p,h in f['inputs'].items():
 if sha(Path(p))!=h:bad.append(p)
if bad:raise ValueError(bad)
if sorted(p.name for p in A.iterdir() if p.is_dir() or p.suffix in ('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
c=types.ModuleType('reviewed_arithmetic');exec(compile((A/'core.py').read_bytes(),str(A/'core.py'),'exec'),c.__dict__)
n=0
def test(b):
 global n
 n+=1
 if not b:raise ValueError('control '+str(n))
for lo,hi in [(F(0),F(1,3)),(F(1,7),F(13,7)),(F(4),F(4)),(F(1,10**40),F(1,10**39))]:
 a,b=c.sqrt((lo,hi));test(a*a<=lo);test(b*b>=hi);test(b-a>=0)
for lo,hi in [(F(-7,3),F(-1,5)),(F(1,7),F(9,4))]:
 a,b=c.inv((lo,hi));test(a<=1/hi);test(b>=1/lo)
# Tail logic independently checked on synthetic elliptic parameters, neither oracle nor native s.
for N in (6,96):
 for z in (F(1,7),F(1,3),F(1,2)):
  r=z**N/(1-z);dr=N*z**(N-1)/(1-z)+z**N/(1-z)**2
  tail=sum(F(comb(2*k,k)**2,16**k)*z**k for k in range(N,N+24))
  dtail=sum(k*F(comb(2*k,k)**2,16**k)*z**(k-1) for k in range(N,N+24))
  test(0<tail<=r);test(0<dtail<=dr)
  for slope in (F(-3,2),F(2,3)):
   enc=c.mul((F(0),dr),(slope,slope));test(enc[0]<=slope*dtail<=enc[1]);test(slope*dtail!=0)
# Copied comparison data are exactly the completed return-series result.
test(sha(A/'RETURN_BASELINE.json')==sha(B/'native-green-return-series-run-4ec20/RESULT.json'))
result={'status':'PASS','synthetic_predicates':n,'source_runtime_pins_verified':len(f['inputs']),'freeze':sha(A/'FREEZE.json'),'physical_oracle_calls':0,'physical_gram_calls':0,'scope':'exact interval primitives and generic series-tail finite subseries; full tail validity is analytical'}
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
