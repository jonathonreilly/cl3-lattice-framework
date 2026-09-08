from fractions import Fraction as F
import itertools,json
from pathlib import Path
shapes={'star':[(0,1),(0,2),(0,3)],'path':[(0,1),(1,2),(2,3)],'pair_plus_edge':[(0,1),(1,2),(3,4)],'disjoint':[(0,1),(2,3),(4,5)]}
out={}
for name,edges in shapes.items():
 row={}
 for bits in itertools.product((0,1),repeat=3):
  total=F(0)
  for word in sorted(set(itertools.permutations((0,0,1,1,2,2)))):
   active=set();sgn=1;den=1;ok=True
   for k,e in enumerate(word):
    sgn*=(-1)**sum(f>e and bool(set(edges[e])&set(edges[f])) for f in active)
    active.symmetric_difference_update({e})
    if k<5:
     q=[sum((1-2*bits[f]) for f in active if v in edges[f]) for v in range(6)]
     d=sum(x*x for x in q)
     if not d or max(map(abs,q))>1:ok=False;break
     den*=d
   if ok:total+=F(sgn,den)
  row[''.join(map(str,bits))]=str(total)
 out[name]=row
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
# Exhaustive repeated-edge4+2 words; store separately without replacing triple evidence.
pairs={}
for incident in (False,True):
 edges=[(0,1),(1,2) if incident else (2,3)]
 for bits in itertools.product((0,1),repeat=2):
  total=F(0)
  for word in set(itertools.permutations((0,0,0,0,1,1))):
   active=set();sgn=1;den=1;ok=True
   for k,e in enumerate(word):
    sgn*=(-1)**sum(f>e and incident for f in active);active.symmetric_difference_update({e})
    if k<5:
     q=[sum(1-2*bits[f] for f in active if v in edges[f]) for v in range(4)];d=sum(x*x for x in q)
     if not d or max(map(abs,q))>1:ok=False;break
     den*=d
   if ok:total+=F(sgn,den)
  assert total==(0 if incident else F(1,32))
  pairs[str((incident,bits))]=str(total)
for name,row in out.items():
 for bits,value in row.items():
  expected=F(0) if name=='star' else F(1,32) if name=='path' and bits in ('010','101') else F(0) if name=='path' else F(1,16) if name=='pair_plus_edge' else F(9,32)
  assert F(value)==expected
# Ice endpoint choices: for each middle bit, each endpoint has3 opposite external bits.
counts=[]
for middle in (0,1):
 choices=[b for b in itertools.product((0,1),repeat=5) if sum(b)+middle==3]
 for left in choices:
  for right in choices:
   count=sum(x!=middle for x in left)*sum(x!=middle for x in right)
   assert count==9;counts.append(count)
Path(__file__).with_name('PAIR_AND_COUNT_RESULT.json').write_text(json.dumps({'pairs':pairs,'ice_endpoint_cases':len(counts),'alternating_paths_per_middle_edge':9},indent=2)+'\n')
