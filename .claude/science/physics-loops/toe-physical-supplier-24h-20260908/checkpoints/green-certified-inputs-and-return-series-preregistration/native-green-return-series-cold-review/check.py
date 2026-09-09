from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,hashlib
P=Path('/private/tmp/toe-24h-probes-20260908/native-green-return-series-stretch');O=Path(__file__).resolve().parent
checks=0
# Independent literal walk recursion, not physical resolvent coefficients summed at s.
walk={(0,0,0):1};count=[]
for length in range(9):
 if length%2==0:
  n=length//2;c=comb(2*n,n)*sum(comb(n,k)**2*comb(2*k,k) for k in range(n+1))
  if walk.get((0,0,0),0)!=c:raise ValueError('walk count')
  count.append(c);checks+=1
 nxt={}
 for x,v in walk.items():
  for axis in range(3):
   for sign in [-1,1]:
    y=list(x);y[axis]+=sign;y=tuple(y);nxt[y]=nxt.get(y,0)+v
 walk=nxt
# Independent finite geometric differentiation formula checks minimal planned m.
rows=json.loads((P/'TOY_RESULT.json').read_text())['plans']
for row in rows:
 s=F(row['s']);q=s*s+6;r=36/q**2;m=row['terms'];target=F(row['target'])
 def tail(k):
  a=r**k/q/(1-r)
  d=2*s/q**2*r**k*((2*k+1)-(2*k-1)*r)/(1-r)**2
  return max(a,d)
 if not tail(m)<=target<tail(m-1):raise ValueError('minimal plan')
 checks+=2
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
f=json.loads((P/'FREEZE.json').read_text())
for p,v in f['inputs'].items():
 if h(Path(p))!=v:raise ValueError(p)
(O/'RESULT.json').write_text(json.dumps({'status':'PASS','predicates':checks,'walk_counts':count,'physical_series_evaluations':0,'plans':rows},indent=2)+'\n')
(O/'READ_HASHES.json').write_text(json.dumps(dict(f['inputs'], **{str(P/'FREEZE.json'):h(P/'FREEZE.json')}),indent=2)+'\n')
print('PASS',checks)
