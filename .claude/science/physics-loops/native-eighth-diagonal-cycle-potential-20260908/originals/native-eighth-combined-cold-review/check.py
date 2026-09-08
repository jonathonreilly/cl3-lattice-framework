from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
import json
P=Path('/private/tmp/toe-24h-probes-20260908');rows=json.loads((P/'native-full-eighth-diagonal/RESULT.json').read_text())['rows'];tab={(r['shape'],tuple(r['bits'])):F(r['connected8']) for r in rows};parts={}
parts['one']=3*tab['one',(0,)]
for name,k in [('pair',2),('path3',3),('path4_unrestricted',4)]:
 shape='path4' if k==4 else name;parts[name]=sum(F(3,2)*__import__('math').prod(2 if a==b else 3 for a,b in zip(bits,bits[1:]))*tab[shape,bits] for bits in product((0,1),repeat=k))
for name,k in [('star3',3),('star4',4)]:parts[name]=sum(tab[name,tuple(sorted(bits,reverse=True))] for ids in combinations(range(6),k) for bits in [tuple((0,0,0,1,1,1)[i] for i in ids)])
parts['fork4']=F(0)
for b in (0,1):
 others=[0]*3+[1]*3;others.remove(b)
 for ids in combinations(range(5),2):
  leaves=sorted([others[i] for i in ids],reverse=True)
  for d in others:parts['fork4']+=3*tab['fork4',tuple(leaves+[b,d])]
expected=json.loads((P/'native-eighth-combined/RESULT.json').read_text());
for k,v in parts.items():
 if v!=F(expected['scalar_parts'][k]):raise RuntimeError('part '+k)
C=sum(parts.values())
if C!=F(3610233,16000):raise RuntimeError('scalar')
points=[(324,648,1296),(320,624,1304),(317,612,1310)]
q=[-F(209,28800)*d+F(1769,216000)*p for f,p,d in points]
det=(points[1][0]-points[0][0])*(q[2]-q[0])-(points[2][0]-points[0][0])*(q[1]-q[0])
if det!= -F(1769,9000):raise RuntimeError('determinant')
out=dict(parts={k:str(v) for k,v in parts.items()},C_tree=str(C),Q=[str(v) for v in q],determinant=str(det),scope='Exact independent arithmetic; supplied global witness triples still require state verification')
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
