from pathlib import Path
import hashlib,json
w=Path('/private/tmp/toe-native-zero-penalty-endpoint-20260908');p=w/'.claude/science/physics-loops/native-zero-penalty-endpoint-20260908';d=Path(__file__).parent;n=0
read=lambda f:json.loads(f.read_text())
def need(c,s):
 global n
 if not c:raise RuntimeError(s)
 n+=1
f=read(p/'SOURCE_FREEZE.json')
for k,h in f.items():need(hashlib.sha256((w/k).read_bytes()).hexdigest()==h,k)
a=read(w/'outputs/native_zero_penalty_endpoint_2026_09_08.json');iso=json.loads((p/'ISOLATED.stdout').read_text())
for k,h in a['input_sha256'].items():need(hashlib.sha256((w/k).read_bytes()).hexdigest()==h,k)
need(a['input_sha256']==iso['input_sha256'],'isolated binding');need(a['parts']['exact']['rows']==iso['parts']['exact']['rows'],'isolated data');need(a['executed_predicates']==80,'80')
# Reconstruct moment sequences directly from reviewed analytic energy multisets.
for row in a['parts']['exact']['rows']:
 v=row['vertices'];flux=row['flux'];out=[]
 for k in range(len(row['moments'])):
  if k==0:value=1<<(v-1)
  elif k%2:value=0
  elif v==3:value=4*3**(k//2)
  elif flux==-1:value=8*2**k
  else:value=4*8**(k//2)
  need(str(value)==row['moments'][k],'spectral multiset moment')
for m in read(p/'MUTATIONS.json'):need(m['exit']!=0 and (p/(m['name']+'.stderr')).read_text().strip().endswith(m['failure']),m['name'])
(d/'RESULT.json').write_text(json.dumps({'checks':n,'scope':'read-only source/receipt/spectral multiset replay; no matrix or prior508 rerun'},indent=2)+'\n');files=[w/k for k in f]+[p/k for k in ['SOURCE_FREEZE.json','ISOLATED_CLOSURE.json','ISOLATED.stdout','MUTATIONS.json','WRAPPER_CONTROLS.json']];(d/'READ_HASHES.json').write_text(json.dumps({str(k):hashlib.sha256(k.read_bytes()).hexdigest() for k in files},indent=2)+'\n');print(n)
