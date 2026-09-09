"""Generic real floating candidate; no physical call on import."""
import math
import numpy as np
import plane

def givens(O,kind):
 n=len(O);a=O.copy();steps=[]
 if kind not in ('AA','BB') or O.shape!=(n,n) or not np.isfinite(O).all():raise ValueError('orthogonal shape')
 for p in range(n-1):
  for q in range(n-1,p,-1):
   x=float(a[p,p]);y=float(a[q,p]);r=math.hypot(x,y)
   if r==0:continue
   c=x/r;s=y/r;rp=a[p].copy();rq=a[q].copy();a[p]=c*rp+s*rq;a[q]=-s*rp+c*rq
   theta=math.atan2(s,c);steps.append((p,q,-theta if kind=='AA' else theta,kind))
 if np.max(np.abs(a-np.eye(n)))>1e-10:raise ValueError('not SO / elimination')
 # O=L1^T...Lk^T. Vector operations execute rightmost first.
 return list(reversed(steps))

def prepare(M,constant):
 M=np.asarray(M)
 if M.dtype!=np.dtype('float64') or M.ndim!=2 or M.shape[0]!=M.shape[1] or not 2<=len(M)<=21 or not np.isfinite(M).all() or not math.isfinite(constant):raise ValueError('matrix')
 U,s,VT=np.linalg.svd(M);V=VT.T.copy();U=U.copy();s=s.copy()
 du=float(np.linalg.det(U));dv=float(np.linalg.det(V))
 if abs(abs(du)-1)>1e-10 or abs(abs(dv)-1)>1e-10:raise ValueError('SVD orientation')
 su=1 if du>0 else -1;sv=1 if dv>0 else -1;U[:,-1]*=su;V[:,-1]*=sv;s[-1]*=su*sv
 error=float(np.max(np.abs((U*s)@V.T-M)))
 if not math.isfinite(error) or error>1e-10*max(1,float(np.max(np.abs(M)))):raise ValueError('SVD reconstruction')
 return {'sigma':s,'delta':float(constant)-float(np.sum(s))/2,'planes':givens(U,'BB')+givens(V,'AA'),'matrix_error':error,'orientation':(su,sv)}

def solve(M,constant,rhs,sector,minimum_denominator=0.):
 if sector not in (0,1) or not math.isfinite(minimum_denominator) or minimum_denominator<0:raise ValueError('sector/denominator floor')
 n=len(M)
 if not isinstance(rhs,np.ndarray) or rhs.dtype!=np.dtype('float64') or rhs.shape!=(1<<(n-1),) or not np.isfinite(rhs).all():raise ValueError('rhs')
 rec=prepare(M,constant);x=rhs.copy()
 for p,q,theta,kind in reversed(rec['planes']):plane.apply(x,n,sector,p,q,theta,kind,inverse=True)
 smallest=math.inf
 for lo in range(0,len(x),4096):
  ids=np.arange(lo,min(lo+4096,len(x)),dtype=np.uint64);bits=ids|((plane.parity(ids)^sector)<<(n-1));den=np.full(len(ids),rec['delta'])
  for j,s in enumerate(rec['sigma']):den=np.add(den,np.multiply((bits>>j)&1,s))
  if not np.isfinite(den).all() or np.any(den<=minimum_denominator):raise ValueError('nonpositive/small denominator')
  smallest=min(smallest,float(np.min(den)));x[lo:lo+len(ids)]=np.divide(x[lo:lo+len(ids)],den)
  if not np.isfinite(x[lo:lo+len(ids)]).all():raise ValueError('division overflow')
 for p,q,theta,kind in rec['planes']:plane.apply(x,n,sector,p,q,theta,kind)
 return x,{'delta':rec['delta'],'signed_sigma':rec['sigma'].tolist(),'planes':rec['planes'],'minimum_denominator':smallest,'matrix_reconstruction_error':rec['matrix_error'],'orientation':rec['orientation']}
