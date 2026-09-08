import json,time,signal
from pathlib import Path
import geometry as g
n=0
def ck(x,label):
 global n;n+=1
 if not x:raise RuntimeError(label)
def mul(a,b):
 out={}
 for (i,j),x in a.items():
  for (k,l),y in b.items():
   if k==j:out[i,l]=out.get((i,l),0)+x*y
 return {k:v for k,v in out.items() if v}
def run():
 data=g.inputs();ck(len(set(tuple(r['face_signs']) for r in data['rows']))==32,'gauge classes')
 reps=sorted(set(r['symmetry_representative'] for r in data['rows']));ck(len(reps)==6,'six cube symmetry classes')
 for row in data['rows']:
  ts=row['terms'];lookup={(i,j,d):s for i,j,d,s in ts}
  ck(len(ts)==len(lookup)==384,'actual directed edge count')
  for i,j,d,s in ts:
   ck(lookup[j,i,tuple(-x for x in d)]==s,'Laurent Hermiticity')
   ck(sum(g.V[i])%2!=sum(g.V[j])%2,'bipartite sign')
  ck(sum(1 for i,j,d,s in ts if any(d))==96,'wrapped directed bonds')
  ck(len({(i,j) for i,j,d,s in ts})==384,'no matrix-entry collision')
  h={(i,j):s for i,j,d,s in ts};h2=mul(h,h)
  ck(sum(h2.get((i,i),0) for i in range(64))==384,'unit-hop trace square')
  q=tuple(row['face_signs'])
  if q==(-1,)*6:
   ck(h2=={(i,i):6 for i in range(64)},'canonical cell Ksquare')
   # Wrong Bloch seam at k=pi in x must change this exact matrix identity.
   bad={(i,j):s*(-1)**d[0] for i,j,d,s in ts};ck(mul(bad,bad)!=h2,'seam-sensitive canonical square')
  if q==(1,)*6:ck(h2!={ (i,i):6 for i in range(64)},'free-cube is not canonical')
 for rep in reps:
  ids=[r['id'] for r in data['rows'] if r['symmetry_representative']==rep]
  ck(len(ids)==len(g.orbit(g.signature(rep))),'complete orbit multiplicity')
 return data,reps
if __name__=='__main__':
 signal.alarm(180);start=time.monotonic();data,reps=run();p=Path(__file__).resolve().parent
 (p/'INPUTS.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
 result={'status':'PASS','predicates':n,'seconds':time.monotonic()-start,'representatives':reps,'scope':'integer geometry and k=0 matrix products only; no eigensolver or integral'}
 (p/'GEOMETRY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
