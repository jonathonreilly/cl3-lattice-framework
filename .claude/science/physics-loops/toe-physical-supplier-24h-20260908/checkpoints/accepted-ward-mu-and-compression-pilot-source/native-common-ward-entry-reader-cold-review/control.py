from pathlib import Path
from fractions import Fraction as F
from collections import OrderedDict
import tempfile,json,hashlib,types,sys
P=Path('/private/tmp/toe-24h-probes-20260908/native-common-ward-entry-reader')
for name in ('interval','reader'):
 m=types.ModuleType(name);sys.modules[name]=m;exec(compile((P/(name+'.py')).read_bytes(),str(P/(name+'.py')),'exec'),m.__dict__)
r=sys.modules['reader'];iv=sys.modules['interval'];count=0
class Dummy:
 def __init__(self,zero=False):self.calls=[];self.zero=zero
 def get(self,key,j):self.calls.append((key,j));return (iv.ZERO,iv.ZERO) if self.zero else (iv.rational(2),iv.rational(3))
c=Dummy();a=Dummy();e=r.Entries(c,a,(0,0,2),etaA=F(0),etaB=F(0),etac=F(0),etaa0=F(0),alpha_max=F(1))
assert e.pole(1,0,1,2)==(iv.rational(4),iv.rational(-6));count+=1
assert e.pole(1,0,2,0)==(iv.rational(2),iv.rational(-3)) and c.calls[-1]==(('cd',0),1);count+=1
assert e.append_pole(2,3,1)==(iv.rational(2),iv.rational(3)) and a.calls[-1]==((3,398,9),10);count+=1
z=Dummy(True);e=r.Entries(z,z,(0,0,1),etaA=F(1,10**30),etaB=F(1,10**19),etac=F(1,10**19),etaa0=F(1,10**30),alpha_max=F(12))
assert len(e.lab)==399 and sum(x[4]==2 for x in e.lab)==396 and sum(x[4]==1 for x in e.lab)==3;count+=1
for i,j in [(0,0),(0,1),(0,396),(396,0),(397,398)]:
 g,jj=e(i,j);assert g[0]<=0<=g[1] and jj[0]<=0<=jj[1];count+=1
# Tiny descriptor exercises actual lazy row hashing, immutable tuple LRU and final hash.
with tempfile.TemporaryDirectory() as td:
 p=Path(td)/'tiny';raw=(json.dumps({'entries':[[0,1,1,0,0]]})+'\n').encode();p.write_bytes(raw);x=r.Indexed.__new__(r.Indexed);x.file=p.open('rb');x.expected=hashlib.sha256(raw).hexdigest();x.cache=OrderedDict();x.limit=1;x.index={('toy',0):(0,len(raw),hashlib.sha256(raw).hexdigest())}
 assert x.get(('toy',0),0)==((1,1),(0,0));count+=1;x.verify();count+=1
 p.write_bytes(raw.replace(b'1',b'2'));assert x.get(('toy',0),0)==((1,1),(0,0));count+=1
 try:x.verify()
 except ValueError:count+=1
 else:raise ValueError('mutation not caught')
 x.cache.clear()
 try:x.get(('toy',0),0)
 except ValueError:count+=1
 else:raise ValueError('row mutation not caught')
 x.close()
 try:r.Indexed(p,hashlib.sha256(p.read_bytes()).hexdigest(),'cache')
 except (ValueError,KeyError):count+=1
 else:raise ValueError('partial index accepted')
print(json.dumps({'status':'PASS','tiny_predicates':count,'native_reader_calls':0,'full_mock_files':0,'scope':'dummy fetches and one-row descriptor only'}))
