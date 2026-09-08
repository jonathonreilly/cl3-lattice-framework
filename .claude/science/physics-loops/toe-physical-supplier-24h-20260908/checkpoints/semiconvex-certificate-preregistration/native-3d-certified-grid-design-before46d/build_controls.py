from pathlib import Path
import json,math
from matrix import build
from forecast import calculate
p=Path(__file__).resolve().parent;c=json.loads((p/'CUBE_INPUTS.json').read_text());t=json.loads((p/'TRIG_INPUTS.json').read_text());checks=0
for row in c['rows']:
 D,r=build(row,[t['rows'][j] for j in (0,8,16)])
 if any(D[i][j]!=D[j][i].conjugate() for i in range(16) for j in range(16)):raise ValueError('Hermitian exact builder')
 if not 0<=r<1e-12 or any(D[i][i]!=6 for i in range(16)):raise ValueError('diagonal and input error')
 checks+=2
from itertools import product
rows=[dict(rep=q,index=j,build_seconds=.0001,eigh_seconds=.0001,certificate_seconds=.001,serialization_seconds=.0001) for q in (0,1,3,5,10,15) for j in product((0,8,16,24),(0,16),(0,16))]
z=calculate(dict(rows=rows),1.)
if z['grid_matrices']!=196608 or z['jobs']!=192:raise ValueError('grid coverage')
for field in ('certificate_seconds','serialization_seconds'):
 bad=[dict(x) for x in rows];bad[0][field]=0
 try:calculate(dict(rows=bad),1.)
 except ValueError:pass
 else:raise ValueError('missing timing accepted')
print(json.dumps(dict(controls=checks+3,scope='deterministic matrix assembly and synthetic forecast; no eigensolver')))
