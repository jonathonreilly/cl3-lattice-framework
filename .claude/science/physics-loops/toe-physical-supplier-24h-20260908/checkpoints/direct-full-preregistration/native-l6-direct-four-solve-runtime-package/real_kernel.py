import numpy as np
MODES=21
TOP=MODES-1
SIZE=1<<TOP
CHUNK=1<<15

def parity(a):
 x=a.copy()
 for shift in (16,8,4,2,1):x^=x>>shift
 return x&1

def linear(x,p,coeff,kind):
 out=np.zeros(SIZE,dtype=np.float64)
 for lo in range(0,SIZE,CHUNK):
  ids=np.arange(lo,min(lo+CHUNK,SIZE),dtype=np.uint32);bits=ids|((parity(ids)^p)<<TOP)
  for j,c in coeff:
   signs=1-2*parity(bits&((1<<j)-1)).astype(np.int8)
   if kind=='B':signs*=2*((bits>>j)&1).astype(np.int8)-1
   term=np.multiply(x[ids],c);term=np.multiply(term,signs)
   if not np.isfinite(term).all():raise ValueError('linear product nonfinite')
   target=ids^(1<<j) if j<TOP else ids
   updated=np.add(out[target],term)
   if not np.isfinite(updated).all():raise ValueError('linear sum nonfinite')
   out[target]=updated
 return out

def action(x,p,center,neighbors,pair,frequencies):
 out=np.empty(SIZE)
 for lo in range(0,SIZE,CHUNK):
  ids=np.arange(lo,min(lo+CHUNK,SIZE),dtype=np.uint32);bits=ids|((parity(ids)^p)<<TOP);diag=np.zeros(len(ids))
  for j,omega in enumerate(frequencies):diag=np.add(diag,np.multiply(((bits>>j)&1),omega))
  out[ids]=np.multiply(diag,x[ids])
  if not np.isfinite(out[ids]).all():raise ValueError('diagonal nonfinite')
 for v,k in pair:
  tmp=linear(x,p,neighbors[v],'A');term=linear(tmp,1-p,center,'B');term=np.multiply(term,k)
  if not np.isfinite(term).all():raise ValueError('pair nonfinite')
  out=np.add(out,term)
  if not np.isfinite(out).all():raise ValueError('action nonfinite')
 return out
