"""Floating active/spectator candidate; no native calls on import."""
import math
import numpy as np
import plane,resolvent

def solve(omega,a,b,groups,rhs,sector,minimum_denominator=0.):
 omega=np.asarray(omega);a=np.asarray(a);b=np.asarray(b);n=len(omega)
 if any(v.dtype!=np.dtype('float64') or v.shape!=(n,) or not np.isfinite(v).all() for v in (omega,a,b)) or not 4<=n<=21:raise ValueError('coefficient schema')
 if sector not in (0,1) or not math.isfinite(minimum_denominator) or minimum_denominator<0:raise ValueError('sector/floor')
 if [i for g in groups for i in g]!=list(range(n)) or any(len(g)<2 for g in groups):raise ValueError('ordered blocks')
 if any(any(omega[j]!=omega[g[0]] or (j!=g[0] and a[j]!=0) for j in g) for g in groups):raise ValueError('block frequency/center')
 if not isinstance(rhs,np.ndarray) or rhs.dtype!=np.dtype('float64') or rhs.shape!=(1<<(n-1),) or not np.isfinite(rhs).all():raise ValueError('rhs')
 aligned=b.copy();rot=[];J=[]
 for g in groups:
  J.extend(g[:2]);p=g[1]
  for q in reversed(g[2:]):
   v=float(aligned[p]);w=float(aligned[q]);r=math.hypot(v,w)
   if r==0:continue
   c=v/r;s=w/r;aligned[p]=c*v+s*w;aligned[q]=-s*v+c*w;rot.append((p,q,math.atan2(s,c)))
 # Alignment is R; physical original operator=W_Rt H_aligned W_Rt^T.
 align=[]
 for p,q,t in reversed(rot):align.extend([(p,q,-t,'AA'),(p,q,t,'BB')])
 spectator=[i for i in range(n) if i not in J]
 if any(abs(aligned[i])>1e-12*max(1,float(np.max(np.abs(b)))) for i in spectator):raise ValueError('alignment residual')
 M=np.diag(omega[J])-2*np.outer(a[J],aligned[J]);rec=resolvent.prepare(M,float(np.sum(omega[J]))/2)
 active=[(J[p],J[q],t,k) for p,q,t,k in rec['planes']]
 x=rhs.copy()
 for p,q,t,k in reversed(align):plane.apply(x,n,sector,p,q,t,k,inverse=True)
 for p,q,t,k in reversed(active):plane.apply(x,n,sector,p,q,t,k,inverse=True)
 smallest=math.inf
 for lo in range(0,len(x),4096):
  ids=np.arange(lo,min(lo+4096,len(x)),dtype=np.uint64);bits=ids|((plane.parity(ids)^sector)<<(n-1));den=np.full(len(ids),rec['delta'])
  for j,s in zip(J,rec['sigma']):den=np.add(den,np.multiply((bits>>j)&1,s))
  for j in spectator:den=np.add(den,np.multiply((bits>>j)&1,omega[j]))
  if not np.isfinite(den).all() or np.any(den<=minimum_denominator):raise ValueError('denominator')
  smallest=min(smallest,float(np.min(den)));x[lo:lo+len(ids)]=x[lo:lo+len(ids)]/den
  if not np.isfinite(x[lo:lo+len(ids)]).all():raise ValueError('division')
 for p,q,t,k in active:plane.apply(x,n,sector,p,q,t,k)
 for p,q,t,k in align:plane.apply(x,n,sector,p,q,t,k)
 return x,{'active':J,'spectators':spectator,'alignment_givens':len(rot),'spin_passes':2*(len(align)+len(active)),'signed_sigma':rec['sigma'].tolist(),'minimum_denominator':smallest}
