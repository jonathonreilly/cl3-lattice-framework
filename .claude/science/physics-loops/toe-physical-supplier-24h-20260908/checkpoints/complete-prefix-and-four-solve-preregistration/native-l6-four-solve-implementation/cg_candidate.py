"""Unlaunched candidate generator. Injected certifier must return exact Fraction rho."""
from fractions import Fraction as F

def solve(np,apply,b,certify,save_checkpoint,stage):
 if stage not in ('first','second'):raise ValueError('stage')
 threshold=F(1,10**10) if stage=='first' else F(1,10**9)
 x=np.zeros_like(b);r=b.copy();p=r.copy();rr=np.dot(r,r)
 for iteration in range(1,257):
  ap=apply(p);den=np.dot(p,ap)
  if not np.isfinite(den) or den<=0 or not np.isfinite(rr):raise ValueError('CG candidate breakdown')
  alpha=rr/den;x=np.add(x,np.multiply(alpha,p));r=np.subtract(r,np.multiply(alpha,ap));new=np.dot(r,r)
  if not np.isfinite(x).all() or not np.isfinite(r).all() or not np.isfinite(new):raise ValueError('CG candidate nonfinite')
  if iteration%16==0:
   cert=certify(x);save_checkpoint(iteration,x,cert)
   if not isinstance(cert['rho'],F):raise ValueError('exact external certificate required')
   if cert['rho']<=threshold:return x,cert,iteration
  if rr==0:raise ValueError('recursive zero before certified checkpoint')
  p=np.add(r,np.multiply(new/rr,p));rr=new
 raise RuntimeError('fixed256 cap: residual target not met')
