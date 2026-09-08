from pathlib import Path
import json,hashlib,time,signal,resource
signal.alarm(30);t=time.monotonic();P=Path(__file__).parent;S=P.parent/'native-sixth-magnetic-symmetry-root/RESULT.json';source=json.loads(S.read_text());gens=source['generators'];seen=set();orbits=[]
for root in range(4096):
 if root in seen:continue
 val={root:1};todo=[root];bad=False
 while todo:
  x=todo.pop();i,j=divmod(x,64)
  for g in gens:
   f=g['permutation'];sign=g['gauge'];y=f[i]*64+f[j];z=val[x]*sign[i]*sign[j]
   if y in val:
    if val[y]!=z:bad=True
   else:val[y]=z;todo.append(y)
 seen.update(val);orbits.append(dict(root=divmod(root,64),size=len(val),forced_zero=bad,values={str(k):v for k,v in val.items()}))
if len(seen)!=4096:raise ValueError('coverage')
if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise ValueError('RSS')
r=dict(status='COMPLETE',source_sha=hashlib.sha256(S.read_bytes()).hexdigest(),dimension=sum(not x['forced_zero'] for x in orbits),orbits=orbits,seconds=time.monotonic()-t)
(P/'COMMUTANT.json').write_text(json.dumps(r,indent=2)+'\n');print(dict(dimension=r['dimension'],orbits=[{k:v for k,v in x.items() if k!='values'} for x in orbits],seconds=r['seconds']))
