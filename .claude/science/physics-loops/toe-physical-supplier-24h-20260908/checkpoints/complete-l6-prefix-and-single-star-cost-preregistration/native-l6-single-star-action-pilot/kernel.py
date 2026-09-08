"""Fixed-order NumPy elementwise candidate arithmetic; NOT interval certified."""
import numpy as np
import math
MODES=21
TOP=MODES-1
SIZE=1<<TOP
CHUNK=1<<15

def parity(a):
 x=a.copy()
 for shift in (16,8,4,2,1):x^=x>>shift
 return x&1

def gamma(x,source_parity,coeff):
 out=np.zeros(SIZE,dtype=np.complex128)
 for lo in range(0,SIZE,CHUNK):
  ids=np.arange(lo,min(lo+CHUNK,SIZE),dtype=np.uint32)
  bits=ids|((parity(ids)^source_parity)<<TOP)
  for j,(a,b) in enumerate(coeff):
   sign=1-2*parity(bits&((1<<j)-1)).astype(np.int8)
   occupied=((bits>>j)&1).astype(np.int8)
   target=ids^(1<<j) if j<TOP else ids
   out[target]+=sign*(a+1j*b*(2*occupied-1))*x[ids]
 return out

def action(x,coefficients,edges,pair,lambdas):
 out=np.empty(SIZE,dtype=np.complex128)
 for lo in range(0,SIZE,CHUNK):
  ids=np.arange(lo,min(lo+CHUNK,SIZE),dtype=np.uint32);bits=ids|(parity(ids)<<TOP);diag=np.zeros(len(ids))
  for j,lam in enumerate(lambdas):diag+=math.sqrt(lam)*((bits>>j)&1)
  out[ids]=diag*x[ids]
 for e in pair:
  i,j,k=edges[e]
  tmp=gamma(x,0,coefficients[j]);term=gamma(tmp,1,coefficients[i])
  out+=(-1j*k)*term
 return out
