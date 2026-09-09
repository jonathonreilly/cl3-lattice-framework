from pathlib import Path
from fractions import Fraction as F
import hashlib,json
S=Path(__file__).resolve().parents[1];P=S/'native-highprecision-b-contraction-design';O=S/'native-highprecision-b-contraction-before-accepted-binding-a9074';R=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=0
def check(x):
 global checks
 assert x;checks+=1
check(sha(P/'RUNTIME_FREEZE.json')=='06afde8d8e56f19a41b48657e0eeb5961d3dfa73f5a2882a71179d98f1fc237d')
f=json.loads((P/'RUNTIME_FREEZE.json').read_text());old=json.loads((O/'RUNTIME_FREEZE.json').read_text())
for n in f['membership']:check((P/n).read_bytes()==(O/n).read_bytes())
for p,h in f['inputs'].items():check(sha(Path(p))==h)
for p,h in old['inputs'].items():check(f['inputs'][p]==h)
b=json.loads((P/'BINDING.json').read_text());check(sha(P/'BINDING.json')==f['binding_sha256'])
check(b['shards']==[list(range(6*j,6*j+6)) for j in range(11)])
for name,count,freeze in [('a66',66,S/'native-stationary-pole-scalar-batch-design/FREEZE.json'),('catalog',3484,S/'native-highprecision-b-catalog-design/FREEZE.json')]:
 d=b[name];p=Path(d['directory']);acc=Path(d['acceptance_path']);check(sha(acc)==d['acceptance_sha256']);a=json.loads(acc.read_text());check(a['status'].startswith('ACCEPTED_'));check(sha(freeze)==d['source_freeze_sha256']==a['worker_freeze']);check(f['inputs'][str(freeze)]==sha(freeze))
 result=json.loads((p/'RESULT.json').read_text());check(sha(p/'RESULT.json')==d['result_sha256']==a['result_sha256']);check(len(result['rows'])==count)
 for row in result['rows']:
  raw=row['oracle'] if name=='a66' else json.loads((p/row['path']).read_text())
  if name=='catalog':check(f['inputs'][str(p/row['path'])]==sha(p/row['path'])==row['sha256'])
  for key,width in zip(('A','Aprime'),raw['widths']):
   lo,hi=map(F,raw[key]);check(0<=hi-lo==F(width)<=F(1,10**30))
check(f['status']=='ACCEPTED_INPUTS_BOUND_UNLAUNCHED' and f['global_cap_seconds']==1200)
(R/'RESULT.json').write_text(json.dumps({'status':'PASS','checks':checks,'physical_contractions':0,'scope':'Frozen binding delta and accepted saved scalar inputs only'},indent=2)+'\n')
print(checks)
