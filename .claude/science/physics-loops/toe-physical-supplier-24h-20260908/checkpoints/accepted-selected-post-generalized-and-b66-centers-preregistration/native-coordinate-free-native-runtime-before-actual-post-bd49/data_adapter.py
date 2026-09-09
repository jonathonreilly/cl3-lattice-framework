"""Prospective sparse realclosed DATA adapter. Import performs no file I/O."""
import json,hashlib
from collections import OrderedDict
from fractions import Fraction as F
import interval as iv

def integer(x,lo,hi):
 if type(x)is not int or not lo<=x<hi:raise ValueError('literal integer label')
 return x
def key(x):
 if type(x)is not tuple or len(x)!=2:raise ValueError('coordinate tuple')
 return integer(x[0],0,402),integer(x[1],0,2)
def embed_original_flat(i):
 integer(i,0,798)
 return (i%399,i//399) # tuple first; DATA flat encoding would raw+402*gamma

def inflate(x,r):
 d=iv.rational(r)[1]
 return x[0]-d,x[1]+d

class NewIndex:
 """Only3q saved stream; accepted immutable path/hash must be externally bound."""
 def __init__(self,path,digest,limit=32):
  integer(limit,1,33);self.file=open(path,'rb');self.expected=digest;self.cache=OrderedDict();self.index={};self.limit=limit
  h=hashlib.sha256();total=0
  try:
   while True:
    pos=self.file.tell();line=self.file.readline()
    if not line:break
    h.update(line);r=json.loads(line);oi=integer(r['orbit_id'],0,5);a=integer(r['append_index'],399,402);typ=r['type']
    if typ=='bare_to_pole':
     n=integer(r['pole_id'],0,66);sig=r['sigma']
     if type(sig)is not int or sig not in(-1,1):raise ValueError('sigma')
     first=6*n+(0 if sig==-1 else 3);ids=list(range(first,first+3));k=(oi,a,first)
    elif typ=='bare_to_insertion':ids=[396,397,398];k=(oi,a,396)
    elif typ=='bare_self':ids=list(range(a,402));k=(oi,a,399)
    else:raise ValueError('row type')
    if k in self.index or [e[0] for e in r['entries']]!=ids:raise ValueError('membership/duplicate')
    for e in r['entries']:
     if len(e)!=5 or any(type(v)is not int for v in e) or e[1]>e[2] or e[3]>e[4]:raise ValueError('integer interval')
    total+=len(ids);self.index[k]=(pos,len(line),hashlib.sha256(line).hexdigest())
   if h.hexdigest()!=digest or len(self.index)!=2010 or total!=6015:raise ValueError('immutable census')
  except BaseException:self.file.close();raise
 def get(self,k,j):
  if k not in self.cache:
   pos,n,d=self.index[k];self.file.seek(pos);raw=self.file.read(n)
   if hashlib.sha256(raw).hexdigest()!=d:raise ValueError('changed row')
   self.cache[k]=tuple(tuple(e) for e in json.loads(raw)['entries'])
   while len(self.cache)>self.limit:self.cache.popitem(last=False)
  self.cache.move_to_end(k)
  for e in self.cache[k]:
   if e[0]==j:return(e[1],e[2]),(e[3],e[4])
  raise ValueError('missing entry')
 def verify(self):
  self.file.seek(0);h=hashlib.sha256()
  for b in iter(lambda:self.file.read(1048576),b''):h.update(b)
  if h.hexdigest()!=self.expected:raise ValueError('final descriptor hash')
 def close(self):self.file.close()

class Entries:
 def __init__(self,old,new,orbit_id,*,etaA,etaB,etac,etamu):
  self.oi=integer(orbit_id,0,5);self.old=old;self.new=new
  if old.oi!=self.oi:raise ValueError('same orbit')
  if not 0<=etaA<=F(1,10**30) or any(not 0<=x<=F(1,10**19) for x in(etaB,etac,etamu)):raise ValueError('physical radii')
  self.pg=2800*etaA;self.pj=176*etaB+etamu;self.ij=etac/2+etamu/4
 def raw(self,i,j):
  integer(i,0,402);integer(j,0,402)
  if i>=399 or j>=399:
   reverse=i<399 or (j>=399 and i>j)
   # New-old stored new first; new-new stored smaller first.
   if i>=399 and j<399:a,b=i,j;reverse=False
   elif j>=399 and i<399:a,b=j,i;reverse=True
   else:a,b=min(i,j),max(i,j);reverse=i>j
   if b<396:
    first=b-b%3;g,z=self.new.get((self.oi,a,first),b);g,z=inflate(g,self.pg),inflate(z,self.pj)
   elif b<399:
    g,z=self.new.get((self.oi,a,396),b)
    if not g[0]<=0<=g[1]:raise ValueError('bare-Ward G zero')
    g,z=iv.ZERO,inflate(z,self.ij)
   else:
    g,z=self.new.get((self.oi,a,399),b)
    if not z[0]<=0<=z[1]:raise ValueError('bare-bare J zero')
    z=iv.ZERO
   return g,iv.neg(z) if reverse else z
  if i>=396 and j>=396:return self.old.self_append(i-396,j-396)
  if i>=396:
   n,t=divmod(j,6);return self.old.append_pole(i-396,2*n+(t//3),t%3)
  if j>=396:
   g,z=self.raw(j,i);return g,iv.neg(z)
  ni,ti=divmod(i,6);nj,tj=divmod(j,6)
  return self.old.pole(2*ni+ti//3,2*nj+tj//3,ti%3,tj%3)
 def __call__(self,a,b):
  i,ga=key(a);j,gb=key(b);g,z=self.raw(i,j)
  # [F,Gamma F]^T[F,Gamma F]=[[G,J],[-J,G]].
  return g if ga==gb else(iv.neg(z) if ga else z)

def native(*args,**kwargs):raise ValueError('NOTREADY: first-action saved POST and actual source binder required')

def exact_midpoint_family(poles,alpha):
 """Exact rational coefficients of accepted F, NOT exact Gauss roots or pi."""
 if len(poles)!=66 or len(alpha)!=66:raise ValueError('fixed66 family')
 ss=[F(x) for x in poles];aa=[F(x) for x in alpha]
 if any(not F(1,128)<=x<=16 for x in ss) or any(not 0<x<=12 for x in aa):raise ValueError('family range')
 # rational() outward-rounds exact rationals to fixed192; core sqrt encloses
 # sqrt of THIS exact alpha. No uncertain quadrature parameter is substituted.
 return [iv.rational(x) for x in ss],[iv.rational(x) for x in aa]
