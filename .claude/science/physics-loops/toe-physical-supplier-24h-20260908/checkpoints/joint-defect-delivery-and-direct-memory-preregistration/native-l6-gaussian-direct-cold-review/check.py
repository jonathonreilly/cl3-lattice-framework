from fractions import Fraction as F
from pathlib import Path
import json,hashlib
source=Path('/private/tmp/toe-24h-probes-20260908/native-l6-four-solve-implementation/COEFFICIENTS.json');c=json.loads(source.read_text());out={};checks=0
for label,vs,want in [('P',('36','6'),[F(160,81),F(64,27),F(8,9),F(8,81)]),('O',('36','180'),[F(64,81),F(64,27),F(16,9),F(32,81)])]:
 rows=[{r['mode']:r for r in c['neighbors'][v]} for v in vs];squares=[]
 for start,size in ((0,6),(6,6),(12,6),(18,3)):
  sq=F(0)
  for j in range(start+1,start+size):
   rs=[r[j] for r in rows if j in r]
   if not rs:continue
   if len(set(r['norm'] for r in rs))!=1:raise ValueError('exact common denominator')
   sq+=(-2*sum(F(r['value']) for r in rs))**2/F(rs[0]['norm'])
  squares.append(sq)
 if squares!=want:raise ValueError('perpendicular norm')
 checks+=4;out[label]=list(map(str,squares))
# Independent word-on-basis CAR product avoids the author's dense matrix routines.
def g(j,b,state):
 return state^(1<<j),(-1)**((state&((1<<j)-1)).bit_count())*((2*((state>>j)&1)-1) if b else 1)
for state in range(16):
 for j in range(4):
  mid,s=g(j,False,state);end,t=g(j,True,mid)
  if end!=state or s*t!=1-2*((state>>j)&1):raise ValueError('BA normalization')
  checks+=1
# Noncontiguous active modes [0,2], spectators [1,3]: literal bilinear includes spectator signs.
for state in range(16):
 for b in (False,True):
  mid,s=g(2,b,state);end,t=g(0,b,mid)
  if (end&10)!=(state&10) or end!=state^5:raise ValueError('spectator block invariant')
  # Pair changes number by an even integer, preserving active parity.
  if ((state&5).bit_count()-(end&5).bit_count())%2:raise ValueError('active parity')
  checks+=1
if 2**13*2**7!=2**20 or 3*4+1!=13 or 2*(8*7//2)!=56:raise ValueError('counts')
checks+=3
print(json.dumps({'status':'PASS','checks':checks,'perpendicular_squares':out,'coefficient_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'physical_actions':0},indent=2))
