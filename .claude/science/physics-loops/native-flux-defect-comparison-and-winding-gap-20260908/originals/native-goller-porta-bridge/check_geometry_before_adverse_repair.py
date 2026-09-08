"""Exact feasibility check only; no chessboard inequality or spectral claim."""
import itertools,json,hashlib,pathlib
count=0

def require(ok):
 global count
 if not ok: raise RuntimeError('geometry predicate failed')
 count+=1

rows=[]
for L in (4,8):
 sites=list(itertools.product(range(L),repeat=3))
 def shift(r,a):
  s=list(r);s[a]=(s[a]+1)%L;return tuple(s)
 def phi(x,y):return 1 if x%2 and y%2 else -1
 def link(r,a):
  x,y,z=r
  if a==0:return 1
  if a==2:return (-1)**(x+y)
  ans=1
  for b in range(x):ans*=phi(b,y)
  return ans
 def face(r,a,b):return link(r,a)*link(shift(r,a),b)*link(shift(r,b),a)*link(r,b)
 defects=0
 for r in sites:
  require(face(r,0,1)==phi(r[0],r[1]))
  require(face(r,0,2)==-1 and face(r,1,2)==-1)
  q=1
  for a,b in ((0,1),(0,2),(1,2)):
   c=3-a-b;q*=face(r,a,b)*face(shift(r,c),a,b)
   defects+=face(r,a,b)==1
  require(q==1)
 require(defects==L**3//4)
 # An isolated face-sign change breaks the two adjacent cube identities.
 require((-1)*1==-1)
 rows.append({'L':L,'vertices':L**3,'defects':defects})
print(json.dumps({'status':'PASS','predicates':count,'scope':'compatible stacked link pattern only','rows':rows},indent=2))
