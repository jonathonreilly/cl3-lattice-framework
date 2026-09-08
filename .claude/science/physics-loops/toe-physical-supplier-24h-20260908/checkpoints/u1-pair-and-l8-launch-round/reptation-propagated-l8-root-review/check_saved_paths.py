from pathlib import Path
from itertools import product,combinations
import json,numpy as np,time,hashlib
start=time.monotonic();root=Path('/private/tmp/toe-24h-probes-20260908/reptation-propagated-l8-design');rows=[]
for L in (2,4,8):
 file=root/f'CONTROL_L{L}.npz'
 with np.load(file,allow_pickle=False) as data:
  meta=json.loads(str(data['metadata']));labels=data['labels'].copy();states=data['states'].copy()
 sites=list(product(range(L),repeat=3));links=[(r,a) for r in sites for a in range(3)];idx={e:k for k,e in enumerate(links)};faces=[]
 for a,b in combinations(range(3),2):
  for r in sites:
   ra=list(r);rb=list(r);ra[a]=(ra[a]+1)%L;rb[b]=(rb[b]+1)%L
   faces.append([idx[r,a],idx[tuple(ra),b],idx[tuple(rb),a],idx[r,b]])
 x=sum(int(bit)<<i for i,bit in enumerate(states[0]));middle=None;flips=0
 for j in range(meta['n']):
  face=int(labels[(meta['head']+j)%meta['n']])
  if face>=0:
   e=faces[face];b=[(x>>k)&1 for k in e]
   if b[0]!=b[2] or b[1]!=b[3] or b[0]==b[1]:raise RuntimeError('illegal saved path edge')
   x^=sum(1<<k for k in e);flips+=1
  if j+1==meta['n']//2:middle=x
 expected=[sum(int(bit)<<i for i,bit in enumerate(s)) for s in states]
 if middle!=expected[1] or x!=expected[2]:raise RuntimeError('path versus endpoint cache')
 # Direct degree calculation of three saved configurations, not an author helper.
 ids={r:i for i,r in enumerate(sites)}
 for state in states:
  deg=[0]*len(sites)
  for k,(r,a) in enumerate(links):
   q=list(r);q[a]=(q[a]+1)%L;deg[ids[r]]+=int(state[k]);deg[ids[tuple(q)]]+=int(state[k])
  if any(d!=3 for d in deg):raise RuntimeError('ice constraint')
 rows.append({'L':L,'n':meta['n'],'legal_saved_flips':flips,'midpoint_and_right_exact':True,'all_saved_degrees_three':True,'source_sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
result={'rows':rows,'seconds':time.monotonic()-start,'scope':'Independent full saved-label path reconstruction, no author code imported; no physics production.'}
Path(__file__).with_name('SAVED_PATH_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
