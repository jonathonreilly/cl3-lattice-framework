import numpy as np
import graph as g

def powers(n):
 out=[np.ones(len(g.nf))];scales=[]
 for _ in range(n):
  x=g.G@out[-1];scale=float(np.max(x));out.append(x/scale);scales.append(scale)
 return np.asarray(out),np.asarray(scales)
def draw(p,rng):
 p=np.asarray(p,float);p=p/p.sum();cdf=np.cumsum(p);cdf[-1]=1.
 return int(np.searchsorted(cdf,rng.random(),side='right'))
def initialize(n,rng,psi):
 path=np.empty(n+1,int);path[0]=draw(psi[n],rng)
 for k in range(n):
  old=path[k];remaining=n-k
  # Distinct legal face labels plus ONE aggregate self; sums recover G even with duplicate endpoints.
  targets=np.r_[g.T[old],old];weights=np.r_[np.where(g.T[old]>=0,1/24,0),1-.95*g.nf[old]/24]
  weights[:24]*=psi[remaining-1,np.maximum(g.T[old],0)];weights[24]*=psi[remaining-1,old]
  path[k+1]=targets[draw(weights,rng)]
 return path
