from pathlib import Path
from fractions import Fraction
import json,hashlib,struct,importlib.util,tempfile
B=Path('/private/tmp/toe-24h-probes-20260908');C=B/'native-l6-exact-norm-scanner';R=B/'native-l6-exact-norm-scanner-root-review';R.mkdir(exist_ok=True);F='f6c9d9f95c0743742bf9eed816b1a75f192cd03b750d584d4736dbd3edba83b8';assert hashlib.sha256((C/'FREEZE.json').read_bytes()).hexdigest()==F
spec=importlib.util.spec_from_file_location('normscanner',C/'scanner.py');ns=importlib.util.module_from_spec(spec);spec.loader.exec_module(ns);checks=0
for exponent in range(2047):
 for mantissa in [0,1,(1<<52)-1]:
  bits=(exponent<<52)|mantissa;x=struct.unpack('<d',struct.pack('<Q',bits))[0];assert Fraction(ns.square(bits),1<<2148)==Fraction(x)**2;checks+=1
for modes in range(1,8):
 for parity in (0,1):
  count=1<<(modes-1);raw=b''.join(struct.pack('<dd',(i-3)/8,(5-i)/16) for i in range(count));expected=[Fraction(0)]*(modes+1)
  for i in range(count):
   low=[(i>>j)&1 for j in range(modes-1)];full=low+[ (parity-sum(low))%2 ];expected[sum(full)]+=Fraction(i-3,8)**2+Fraction(5-i,16)**2
  with tempfile.TemporaryDirectory(dir='/private/tmp') as td:
   q=Path(td)/'x';q.write_bytes(raw);j=ns.scan(q,modes,parity,3);assert [Fraction(int(a),1<<2148) for a in j['particle_numerators']]==expected;checks+=1
f=json.loads((C/'FREEZE.json').read_text())
for name,h in f['inputs'].items():assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==h
(R/'TOY_RESULT.json').write_text(json.dumps(dict(status='PASS',source_freeze=F,independent_small_predicates=checks,full_vector_scans=0,runtime_hashes=len(f['inputs'])),indent=2)+'\n')
(R/'REVIEW.md').write_text('''# Root independent exact scanner review and cost authorization — UNLAUNCHED

Read full final proof/scanner/driver/controls/protocol/runtime boundary. Normal binary64 exponent e yields integer significand2^(e-1) in2^-1074 units; square scaling2(e-1) is correct. Subnormal/zero and exponent2047reject correct. Compressed particle count includes implicit parity bit; exact length and finite data are checked. Full root toy sweep covers all2047 finite exponent fields at three mantissa boundaries and modes1..7both parities against independent Fraction/explicitbitlist arithmetic (6155predicates), no fullvector scan. All1880-ish actual input pins checked; actual count inTOY_RESULT. Finalf6c preservesc0e and resolves atmost4196bit wording plus loadedmodule/framework guard. OS sharedcache boundary explicit. Root did not author scanner or arithmetic proof.

One fixed2^20complex extreme-exponent fixture cost attempt,30seconds384MiB whole-tree cap after remotecheckpoint. The saved exactnorm belongs to that fixture; it is no physical residual. Source/runtime hash read, imports, fixturegeneration/write, exactscan, hash and serialization included. Strict-I-B, external /usr/bin/time -lp, processgroup watchdog29.5seconds and internal29alarm. Retain failure/partial, no retry. No fullscanner call has occurred. Future source/residual arithmetic errors and independent complete replay remain separate obligations.
''')
print(json.dumps(dict(checks=checks,pins=len(f['inputs']))))
