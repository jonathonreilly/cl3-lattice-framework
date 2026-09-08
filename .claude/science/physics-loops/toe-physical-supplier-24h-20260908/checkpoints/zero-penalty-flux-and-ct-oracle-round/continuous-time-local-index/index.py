"""Persistent AVL event roots; deterministic reference for index invariants."""
from dataclasses import dataclass
import heapq,math
from conditional_reference import Trajectory,orbit,normalize,matmul
import bridge
@dataclass(frozen=True)
class Node:
 e:tuple
 left:object=None
 right:object=None
 height:int=1
 size:int=1

def ht(n):return 0 if n is None else n.height
def sz(n):return 0 if n is None else n.size
def make(e,l=None,r=None):return Node(e,l,r,1+max(ht(l),ht(r)),1+sz(l)+sz(r))
def balance(n):
 if ht(n.left)-ht(n.right)>1:
  l=n.left
  if ht(l.right)>ht(l.left):
   q=l.right;l=make(q.e,make(l.e,l.left,q.left),q.right)
  return make(l.e,l.left,make(n.e,l.right,n.right))
 if ht(n.right)-ht(n.left)>1:
  r=n.right
  if ht(r.left)>ht(r.right):
   q=r.left;r=make(q.e,q.left,make(r.e,q.right,r.right))
  return make(r.e,make(n.e,n.left,r.left),r.right)
 return n
def key(e):return e[:2]
def insert(n,e):
 if n is None:return make(e)
 if key(e)==key(n.e):raise ValueError('duplicate event id/key')
 if key(e)<key(n.e):return balance(make(n.e,insert(n.left,e),n.right))
 return balance(make(n.e,n.left,insert(n.right,e)))
def delete(n,k):
 if n is None:raise ValueError('missing event')
 if k<key(n.e):return balance(make(n.e,delete(n.left,k),n.right))
 if k>key(n.e):return balance(make(n.e,n.left,delete(n.right,k)))
 if n.left is None:return n.right
 if n.right is None:return n.left
 q=n.right
 while q.left is not None:q=q.left
 return balance(make(q.e,n.left,delete(n.right,key(q.e))))
def events(n):
 if n is not None:
  yield from events(n.left);yield n.e;yield from events(n.right)
def before(n,t):
 if n is None:return 0
 if t<=n.e[0]:return before(n.left,t)
 return sz(n.left)+1+before(n.right,t)
def at_time(n,t):
 while n is not None:
  if t==n.e[0]:return True
  n=n.left if t<n.e[0] else n.right
 return False
def audit(n):
 if n is None:return 0,0
 hl,sl=audit(n.left);hr,sr=audit(n.right)
 if n.height!=1+max(hl,hr) or n.size!=1+sl+sr or abs(hl-hr)>1:raise ValueError('AVL metadata')
 return n.height,n.size

class Index:
 def __init__(self,path):
  path.check();self.g=path.g;self.initial=path.initial;self.T=path.T;self.witness=list(path.witness);self.global_root=None;self.edge={};self.face={};self.nextid=0
  for t,p in path.events:
   e=(t,self.nextid,p);self.nextid+=1;self.global_root=insert(self.global_root,e);self.face[p]=insert(self.face.get(p),e)
   for link in self.g.faces[p]:self.edge[link]=insert(self.edge.get(link),e)
 def bit(self,e,t):return ((self.initial>>e)&1)^(before(self.edge.get(e),t)%2)
 def state(self,t):return sum(self.bit(e,t)<<e for e in range(self.g.E))
 def local_events(self,U):
  merged=heapq.merge(*(events(self.edge.get(e)) for e in U),key=key);out=[];last=None;visits=0
  for ev in merged:
   visits+=1
   if key(ev)!=last:out.append(ev);last=key(ev)
  return out,visits
 def trajectory(self):return Trajectory(self.g,self.initial,[(t,p) for t,i,p in events(self.global_root)],self.T,list(self.witness))
 def splice(self,p,newtimes,initial_flip):
  if type(initial_flip) is not bool:raise ValueError('initial flip')
  validate_proposal(self,p,newtimes,initial_flip)
  old=list(events(self.face.get(p)));root=self.global_root;staged={e:self.edge.get(e) for e in self.g.faces[p]};face=None;nextid=self.nextid
  if initial_flip and not self.g.legal(self.initial,p):raise ValueError('illegal initial flip')
  for e in old:
   root=delete(root,key(e))
   for link in self.g.faces[p]:staged[link]=delete(staged[link],key(e))
  last=0.
  for t in newtimes:
   if not math.isfinite(t) or not last<t<self.T or at_time(root,t):raise ValueError('global event collision/domain')
   ev=(t,nextid,p);nextid+=1;root=insert(root,ev);face=insert(face,ev)
   for link in self.g.faces[p]:staged[link]=insert(staged[link],ev)
   last=t
  # All local legality and global collision checks precede atomic root commit.
  self.global_root=root;self.face[p]=face
  for link,r in staged.items():self.edge[link]=r
  self.nextid=nextid
  if initial_flip:self.initial^=self.g.masks[p];self.witness.append(p)
  return len(old),len(newtimes)

def dependency(g,p):return {e for q in g.affected[p] for e in g.faces[q]}
def dnf(g,x,p):return sum(int(g.legal(x^g.masks[p],q))-int(g.legal(x,q)) for q in g.affected[p])
def local_transfer(g,O,p,V,T):
 if len(O)==1:return [[1.]]
 d=V*sum(int(g.legal(O[1],q))-int(g.legal(O[0],q)) for q in g.affected[p]);logs=[[bridge.logE(d,1.,T,i,j) for j in (0,1)] for i in (0,1)];s=max(z for row in logs for z in row)
 out=[[math.exp(z-s) for z in row] for row in logs]
 if any(z>0 and not math.isfinite(z) for row in out for z in row) or any(v==0 for row in out for v in row):raise ValueError('local transfer underflow')
 return out
def local_messages(index,p,V):
 g=index.g
 if type(p) is not int or not 0<=p<g.M or not math.isfinite(V) or V<0:raise ValueError('local face/V')
 U=dependency(g,p);mask=sum(1<<e for e in U);x=index.initial&mask;orbits=[orbit(g,x,p)];retained=[];es,visits=index.local_events(U)
 for t,i,q in es:
  x^=g.masks[q]&mask
  if q!=p:retained.append((t,q));orbits.append(orbit(g,x,p))
 C=[]
 for i,(t,q) in enumerate(retained):
  if set(g.faces[q]).isdisjoint(g.faces[p]):C.append([[int((a^(g.masks[q]&mask))==b) for b in orbits[i+1]] for a in orbits[i]])
  else:C.append([[int(g.legal(a,q) and a^g.masks[q]==b) for b in orbits[i+1]] for a in orbits[i]])
 times=[0.]+[t for t,q in retained]+[index.T];D=[local_transfer(g,O,p,V,b-a) for O,a,b in zip(orbits,times,times[1:])]
 total=D[0]
 for i,c in enumerate(C):total=normalize(matmul(matmul(total,c),D[i+1]))
 return dict(total=normalize(total),local_event_count=len(es),index_entry_visits=visits,retained=retained,orbits=orbits,U=U)

def integral_delta(index,p,newtimes,initial_flip):
 g=index.g;U=dependency(g,p);mask=sum(1<<e for e in U);x=index.initial&mask;delta=initial_flip;es,_=index.local_events(U)
 timeline={}
 for t,i,q in es:timeline.setdefault(t,[]).append(('old',q))
 for t in newtimes:timeline.setdefault(t,[]).append(('new',p))
 total=0.;last=0.
 for t,items in sorted(timeline.items()):
  total+=(t-last)*(dnf(g,x,p) if delta else 0)
  for kind,q in items:
   if kind=='old':
    x^=g.masks[q]&mask
    if q==p:delta=not delta
   else:delta=not delta
  last=t
 total+=(index.T-last)*(dnf(g,x,p) if delta else 0)
 return total


def validate_proposal(index,p,newtimes,initial_flip):
 g=index.g
 if type(p) is not int or not 0<=p<g.M or type(initial_flip) is not bool:raise ValueError('proposal domain')
 if initial_flip and not g.legal(index.initial,p):raise ValueError('initial orbit')
 U=dependency(g,p);mask=sum(1<<e for e in U);x=(index.initial^(g.masks[p] if initial_flip else 0))&mask
 old,_=index.local_events(U);retained=[(t,q) for t,i,q in old if q!=p]
 previous=0.
 for t in newtimes:
  if not math.isfinite(t) or not previous<t<index.T:raise ValueError('new event time')
  previous=t
 timeline=sorted(retained+[(t,p) for t in newtimes]);last=-1.
 for t,q in timeline:
  if t==last:raise ValueError('local event collision')
  if (q==p or not set(g.faces[q]).isdisjoint(g.faces[p])) and not g.legal(x,q):raise ValueError('local retained/proposed legality')
  x^=g.masks[q]&mask;last=t
 return True
