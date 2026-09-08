from itertools import product,combinations
from collections import Counter
from pathlib import Path
import json
rows=[]
for L in (2,4):
 vertices=list(product(range(L),repeat=3));edges=[(v,a) for v in vertices for a in range(3)];index={e:i for i,e in enumerate(edges)}
 def shift(v,a):
  z=list(v);z[a]=(z[a]+1)%L;return tuple(z)
 faces=[]
 for a,b in combinations(range(3),2):
  for v in vertices:
   f=(index[v,a],index[shift(v,a),b],index[shift(v,b),a],index[v,b])
   if len(set(f))!=4:raise RuntimeError('degenerate face')
   faces.append(f)
 masks=[sum(1<<e for e in f) for f in faces];multiplicity=Counter(masks)
 if len(faces)!=3*L**3 or len(multiplicity)!=len(faces):raise RuntimeError('mask collision')
 rows.append(dict(L=L,edges=len(edges),faces=len(faces),distinct_masks=len(multiplicity),max_mask_multiplicity=max(multiplicity.values()),face_edges=faces))
Path(__file__).with_name('RESULT.json').write_text(json.dumps({'no_author_imports':True,'rows':rows},indent=2)+'\n');print([(r['L'],r['edges'],r['faces'],r['distinct_masks']) for r in rows])
