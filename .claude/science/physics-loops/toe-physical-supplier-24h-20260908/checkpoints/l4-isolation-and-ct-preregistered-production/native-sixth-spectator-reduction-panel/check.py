from itertools import product,combinations
from fractions import Fraction as F
from pathlib import Path
import json,time
st=time.monotonic();n=0
def need(c,m):
 global n
 n+=1
 if not c:raise RuntimeError(m)
vs=list(product(range(4),repeat=3));ix={v:i for i,v in enumerate(vs)};ed=[];K={}
for r in vs:
 for a in range(3):
  s=list(r);s[a]=(s[a]+1)%4;s=tuple(s);i,j=sorted((ix[r],ix[s]));ed.append((i,j));z=(-1)**sum(r[:a]);K[i,j]=-2*z;K[j,i]=2*z
v,w=0,16;boundary=[e for e,(i,j) in enumerate(ed) if (i in (v,w))!=(j in (v,w))];B=set(boundary);S=set(sum(([i,j] for e in boundary for i,j in [ed[e]]),[]));S|={v,w}
bridges=[e for e,(i,j) in enumerate(ed) if e not in B and i in S and j in S and ((i in {v}|{u for f in B for u in ed[f] if v in ed[f]}) != (j in {v}|{u for f in B for u in ed[f] if v in ed[f]}))]
need(len(boundary)==10 and len(S)==12 and len(bridges)==6,'six bridge supports')
# Exact rank of columns E_S and K E_S using an independent row echelon algorithm.
cols=[]
for s in sorted(S):cols.append([F(i==s) for i in range(64)]);cols.append([F(K.get((i,s),0)) for i in range(64)])
rows=[list(z) for z in zip(*cols)];rank=0
for c in range(len(cols)):
 pivot=next((i for i in range(rank,64) if rows[i][c]),None)
 if pivot is None:continue
 rows[rank],rows[pivot]=rows[pivot],rows[rank];z=rows[rank][c];rows[rank]=[a/z for a in rows[rank]]
 for i in range(rank+1,64):
  z=rows[i][c]
  if z:rows[i]=[a-z*b for a,b in zip(rows[i],rows[rank])]
 rank+=1
need(rank==20,'common rank twenty')
adj=[[] for _ in vs]
for e,(i,j) in enumerate(ed):adj[i].append((j,e));adj[j].append((i,e))
def cut(mask):
 values={0:0};todo=[0]
 for i in todo:
  for j,e in adj[i]:
   z=values[i]^((mask>>e)&1)
   if j in values:
    if values[j]!=z:return None
   else:values[j]=z;todo.append(j)
 return sum(values.values())
results=[]
for bridge in bridges:
 labels=boundary+[bridge];pairs=[(a,b) for a,b in combinations(range(11),2) if set(ed[labels[a]])&set(ed[labels[b]])];seen={(0,0)};front=[(0,0)];counts={(0,0):1};odd=[]
 for mask,c in front:
  for a,b in pairs:
   mm=mask;cc=c;valid=True
   for q in (a,b):
    if q==10:
     cc+=1
     if cc>2:valid=False
    else:
     if mm>>q&1:valid=False
     mm|=1<<q
   if not valid:continue
   dst=(mm,cc)
   if dst not in seen:seen.add(dst);front.append(dst)
 # Count paths in topological degree order; each insertion operator is unique.
 for mask,c in sorted(seen,key=lambda z:z[0].bit_count()+z[1]):
  if (mask,c)==(0,0):continue
  total=0
  for a,b in pairs:
   mm=mask;cc=c;valid=True
   for q in (a,b):
    if q==10:cc-=1;valid &=cc>=0
    else:valid &=bool(mm>>q&1);mm &=~(1<<q)
   if valid:total+=counts.get((mm,cc),0)
  counts[mask,c]=total
  Fmask=sum(1<<boundary[q] for q in range(10) if mask>>q&1)^((1<<bridge) if c%2 else 0);size=cut(Fmask);degree=(mask.bit_count()+c)//2
  if degree<6:
   need(Fmask!=0,'no zero-toggle proper prefix')
   if size is not None:need(size%2==1,'only odd-cut proper prefix');odd.append((mask,c,size))
 need(cut(sum(1<<e for e in B)) in (2,62),'final adjacent cut')
 results.append({'bridge':bridge,'endpoints':ed[bridge],'reachable_states':len(seen),'ordered_words':counts.get((1023,2),0),'odd_cut_prefixes':len(odd)})
need(sum(z['ordered_words'] for z in results)==194400,'complete candidate count')
Path(__file__).with_name('RESULT.json').write_text(json.dumps({'checks':n,'rank':rank,'S':sorted(S),'boundary':boundary,'bridges':results,'seconds':time.monotonic()-st},indent=2)+'\n')
