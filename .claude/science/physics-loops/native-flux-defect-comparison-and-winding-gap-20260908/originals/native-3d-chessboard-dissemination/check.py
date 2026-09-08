"""Exact geometry controls; no spectrum or reflection-energy inequality computation."""
import itertools,json,hashlib,time
from pathlib import Path
start=time.monotonic();count=0

def ck(c,label):
 global count
 count+=1
 if not c:raise RuntimeError(label)

verts=list(itertools.product(range(2),repeat=3))
edges=[(v,a) for v in verts for a in range(3) if v[a]==0]
tree=[];known={(0,0,0)}
while len(known)<8:
 for v,a in edges:
  w=list(v);w[a]=1;w=tuple(w)
  if (v in known)!=(w in known):tree.append((v,a));known.update((v,w))
free=[e for e in edges if e not in tree];ck(len(free)==5,'cube cycle rank')
rows=[];classes=set()
for bits in range(32):
 base={e:(-1 if e in free and bits>>free.index(e)&1 else 1) for e in edges}
 def bface(a,b,cval):
  c=3-a-b;v=[0,0,0];v[c]=cval;v=tuple(v)
  va=list(v);va[a]=1;vb=list(v);vb[b]=1
  return base[v,a]*base[tuple(va),b]*base[tuple(vb),a]*base[v,b]
 signature=tuple(bface(a,b,c) for a,b in ((0,1),(0,2),(1,2)) for c in (0,1));classes.add(signature)
 ck(__import__('math').prod(signature)==1,'cube compatibility')
 m=sum(x==1 for x in signature)
 for dims in ((4,4,4),(4,8,4),(8,8,8)):
  sites=list(itertools.product(*(range(L) for L in dims)))
  def shift(v,a):w=list(v);w[a]=(w[a]+1)%dims[a];return tuple(w)
  def fold(x):return (0,1,1,0)[x%4]
  def link(v,a,twist=True):
   block=[x//2 for x in v]
   if v[a]%2==0:
    w=[fold(x) for x in v];w[a]=0
    ans=(-1)**sum(block)*base[tuple(w),a]
   else:ans=(-1)**sum(block[a+1:])
   if twist and v[a]==dims[a]-1:ans*=(-1)**(dims[a]//4+1)
   return ans
  def face(v,a,b):return link(v,a)*link(shift(v,a),b)*link(shift(v,b),a)*link(v,b)
  defect=0
  for v in sites:
   for a,b in ((0,1),(0,2),(1,2)):
    got=face(v,a,b)
    expect=bface(a,b,fold(v[3-a-b])) if v[a]%2==v[b]%2==0 else -1
    ck(got==expect,'retained internal or canonical crossing face');defect+=got==1
   cube=1
   for a,b in ((0,1),(0,2),(1,2)):
    c=3-a-b;cube*=face(v,a,b)*face(shift(v,c),a,b)
   ck(cube==1,'full cube Bianchi')
  ck(defect==len(sites)//8*m,'disseminated defect multiplicity')
  for a,L in enumerate(dims):
   w=[0,0,0];hol=bare=1
   for i in range(L):w[a]=i;hol*=link(tuple(w),a);bare*=link(tuple(w),a,False)
   ck(hol==-1,'canonical real hopping winding');ck(bare==(-1)**(L//4),'untwisted period-four winding')
  rows.append({'class':bits,'dims':dims,'internal_defects':m,'defects':defect})
ck(len(classes)==32,'all cube gauge classes')
# Every elementary face belongs to exactly two of the eight shifted block partitions.
for dims in ((4,4,4),(4,8,4)):
 for v in itertools.product(*(range(L) for L in dims)):
  for a,b in ((0,1),(0,2),(1,2)):
   ck(sum(v[a]%2==s[a] and v[b]%2==s[b] for s in verts)==2,'eight-partition multiplicity')
ck((-1)**(8//4)!=-1,'seam omission is discriminating at L8')
result={'status':'PASS','predicates':count,'seconds':time.monotonic()-start,'classes':len(classes),'rows':rows,'scope':'exact compatible tiling/Bianchi/winding/counting; analytical energy inequality not numerically tested'}
print(json.dumps(result,indent=2))
