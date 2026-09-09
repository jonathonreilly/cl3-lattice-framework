"""Immutable indexed saved-data API. Import performs no I/O or entry evaluation."""
import hashlib,json
from collections import OrderedDict
from fractions import Fraction as F
import interval as iv
ORBITS=((1,1,0),(1,0,0),(0,1,0),(0,0,2),(0,0,1))
TYPES=('cc','cd','P','O','cross')

def labels(augmented=True):
 x=tuple(('pole',n,s,e,2) for n in range(66) for s in range(3) for e in(-1,1))
 return x+tuple(('append',0,s,1,1) for s in range(3)) if augmented else x

def inflate(x,r):
 d=iv.rational(r)[1];return x[0]-d,x[1]+d

class Indexed:
 def __init__(self,path,digest,mode,limit=32):
  if mode not in('cache','append') or not 1<=limit<=32:raise ValueError('index mode/LRU')
  self.file=open(path,'rb');self.expected=digest;self.mode=mode;self.limit=limit;self.cache=OrderedDict();self.index={};h=hashlib.sha256();counts=0
  try:
   while True:
    pos=self.file.tell();line=self.file.readline()
    if not line:break
    h.update(line);r=json.loads(line)
    if mode=='cache':
     typ,i=r['type'],r['i']
     if typ not in TYPES or not 0<=i<132:raise ValueError('cache label')
     key=(typ,i);ids=list(range(0 if typ=='cd' else i,132))
    else:
     oi,i=r['orbit_id'],r['append_index']
     if not 0<=oi<5 or not 396<=i<399:raise ValueError('append label')
     if r['type']=='append_to_pole':
      n,sig=r['pole_id'],r['sigma']
      if not 0<=n<66 or sig not in(-1,1):raise ValueError('append pole')
      first=n*6+(0 if sig==-1 else 3);key=(oi,i,first);ids=list(range(first,first+3))
     elif r['type']=='append_self':key=(oi,i,396);ids=list(range(i,399))
     else:raise ValueError('append type')
    if key in self.index or [x[0] for x in r['entries']]!=ids:raise ValueError('duplicate/membership')
    for e in r['entries']:
     if len(e)!=5 or any(type(x)is not int for x in e) or e[1]>e[2] or e[3]>e[4]:raise ValueError('integer interval')
    counts+=len(ids);self.index[key]=(pos,len(line),hashlib.sha256(line).hexdigest())
   if h.hexdigest()!=digest or len(self.index)!=(660 if mode=='cache' else 1995) or counts!=(52536 if mode=='cache' else 5970):raise ValueError('saved hash/census')
  except BaseException:self.file.close();raise
 def row(self,key):
  if key in self.cache:self.cache.move_to_end(key);return self.cache[key]
  pos,size,digest=self.index[key];self.file.seek(pos);raw=self.file.read(size)
  if hashlib.sha256(raw).hexdigest()!=digest:raise ValueError('changed indexed bytes')
  values=tuple(tuple(e) for e in json.loads(raw)['entries']);self.cache[key]=values
  while len(self.cache)>self.limit:self.cache.popitem(last=False)
  return values
 def get(self,key,j):
  for e in self.row(key):
   if e[0]==j:return (e[1],e[2]),(e[3],e[4])
  raise ValueError('missing indexed entry')
 def verify(self):
  self.file.seek(0);h=hashlib.sha256()
  for block in iter(lambda:self.file.read(1048576),b''):h.update(block)
  if h.hexdigest()!=self.expected:raise ValueError('final immutable hash')
 def close(self):self.file.close()

class Entries:
 def __init__(self,cache,append,orbit,*,etaA,etaB,etac,etaa0,alpha_max):
  if tuple(orbit) not in ORBITS:raise ValueError('orbit')
  if not 0<=etaA<=F(1,10**30) or not 0<=etaB<=F(1,10**19) or not 0<=etac<=F(1,10**19) or not 0<=etaa0<=F(1,10**30) or not 0<alpha_max<=12:raise ValueError('actual radius gates')
  self.cache,self.append,self.orbit=cache,append,tuple(orbit);self.oi=ORBITS.index(self.orbit);self.lab=labels(append is not None)
  self.eg=alpha_max*2**24*etaA;self.ej=alpha_max*10136*etaB;self.ag=176*etaA;self.aj=514*etaB+512*etac;self.aa=etaa0/2
 def pole(self,i,j,a,b):
  oa,oc,k=self.orbit;reverse=False;factor=1
  if a==b:typ='cc' if a==0 else('O' if(oa if a==1 else oc) else'P')
  elif a==0:typ='cd'
  elif b==0:typ='cd';i,j=j,i;reverse=True
  else:
   if not k:return iv.ZERO,iv.ZERO
   typ='cross';factor=k
  if typ!='cd' and i>j:i,j=j,i;reverse=not reverse
  g,z=self.cache.get((typ,i),j)
  if reverse:z=iv.neg(z)
  # General l1<=2 inflation is applied ONCE, after k2 selector multiplication.
  return inflate(iv.scale(g,factor),self.eg),inflate(iv.scale(z,factor),self.ej)
 def append_pole(self,a,i,v):
  raw=(i//2)*6+(0 if i%2==0 else 3)+v;first=raw-raw%3
  g,z=self.append.get((self.oi,396+a,first),raw);return inflate(g,self.ag),inflate(z,self.aj)
 def self_append(self,a,b):
  if a>b:a,b=b,a
  g,z=self.append.get((self.oi,396+a,396),396+b)
  if not z[0]<=0<=z[1]:raise ValueError('append exact J zero')
  return inflate(g,self.aa if a and b else F(0)),iv.ZERO
 def __call__(self,i,j):
  if not 0<=i<len(self.lab) or not 0<=j<len(self.lab):raise ValueError('entry index')
  x,y=self.lab[i],self.lab[j]
  def terms(l):
   kind,n,s,eta,_=l
   if kind=='append':return ((None,s,F(1)),)
   chi=1 if s==0 else-1
   return ((2*n+1,s,F(1,2)),(2*n,s,F(-eta*chi,2)))
  g=z=iv.ZERO
  for pi,a,ca in terms(x):
   for pj,b,cb in terms(y):
    if pi is None and pj is None:gg,jj=self.self_append(a,b)
    elif pi is None:gg,jj=self.append_pole(a,pj,b)
    elif pj is None:gg,jj=self.append_pole(b,pi,a);jj=iv.neg(jj)
    else:gg,jj=self.pole(pi,pj,a,b)
    g=iv.add(g,iv.scale(gg,ca*cb));z=iv.add(z,iv.scale(jj,ca*cb))
  if x[3]!=y[3]:
   if not g[0]<=0<=g[1]:raise ValueError('chiral G inconsistency')
   g=iv.ZERO
  if x[3]==y[3]:
   if not z[0]<=0<=z[1]:raise ValueError('chiral J inconsistency')
   z=iv.ZERO
  return g,z
