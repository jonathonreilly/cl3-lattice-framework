from pathlib import Path
import json,hashlib
s=Path('/private/tmp/toe-24h-probes-20260908/native-l6-spin-plane-candidate');d=Path(__file__).parent;count=0
for m in range(2,9):
 for sector in [0,1]:
  for p in range(m):
   for q in range(p+1,m):
    seen=[]
    for k in range(1<<(m-2)):
     mask=(1<<p)-1;i=(k&mask)|((k>>p)<<(p+1));j=i^(1<<p)^((1<<q) if q<m-1 else 0);seen.extend([i,j]);bits=i|(((i.bit_count()&1)^sector)<<(m-1))
     for kind in ['AA','BB']:
      b=bits;g=1
      for v in [q,p]:
       g*=(-1)**((b&((1<<v)-1)).bit_count())
       if kind=='BB':g*=2*((b>>v)&1)-1
       b^=1<<v
      nq=(bits&((1<<q)-1)).bit_count();np=((bits^(1<<q))&((1<<p)-1)).bit_count();candidate=(-1)**(nq+np)
      if kind=='BB':candidate*= (2*((bits>>q)&1)-1)*(2*((bits>>p)&1)-1)
      if g!=candidate or (b&((1<<(m-1))-1))!=j:raise ValueError('CAR')
      count+=1
    if sorted(seen)!=list(range(1<<(m-1))):raise ValueError('partition')
f=json.loads((s/'FREEZE.json').read_text())
if not all(hashlib.sha256((s/n).read_bytes()).hexdigest()==h for n,h in f['files'].items()):raise ValueError('freeze')
(d/'CONTROL.json').write_text(json.dumps({'status':'PASS','literal_sign_cases':count,'max_modes':8,'no_arrays':True},indent=2)+'\n');print(count)
