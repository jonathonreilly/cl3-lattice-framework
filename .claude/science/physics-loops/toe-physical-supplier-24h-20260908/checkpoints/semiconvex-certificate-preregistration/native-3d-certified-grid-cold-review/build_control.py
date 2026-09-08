from pathlib import Path
import json,runpy
from independent import *
B=Path(__file__).parent.parent/'native-3d-certified-grid-design';build=runpy.run_path(str(B/'matrix.py'))['build'];cubes=json.loads((B/'CUBE_INPUTS.json').read_text());grid=[]
for x in (F(1,2),F(1),F(3,2)):grid.append(dict(q_hex=float(x).hex(),lower_numerator=x.numerator*100-1,upper_numerator=x.numerator*100+1,denominator=x.denominator*100))
n=0
for rep in (0,1,3,5,10,15):
 A,r=matrix(cubes['rows'][rep],grid);D,s=build(cubes['rows'][rep],grid);ck(r==s,'radius');n+=1
 for i in range(16):
  for j in range(16):ck(A[i][j]==z(D[i][j]),'literal tensor matrix');n+=1
print(json.dumps({'controls':n,'scope':'six exact rational-input matrix assemblies, no eigenvalues or physical grid'}))
