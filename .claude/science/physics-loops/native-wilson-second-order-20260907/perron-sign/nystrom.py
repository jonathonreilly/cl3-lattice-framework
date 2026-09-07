import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.linalg import eigh
from numpy.polynomial.legendre import leggauss
import time,signal,resource,sys,json,hashlib
signal.alarm(180);start=time.monotonic()
s1=np.array([[-1,0],[1,1]]);s2=np.array([[1,1],[0,-1]]);group=[(np.eye(2,dtype=int),1),(s1,-1),(s2,-1),(s1@s2,1),(s2@s1,1),(s1@s2@s1,-1)]
Q=lambda x:x[...,0]**2+x[...,0]*x[...,1]+x[...,1]**2
rows=[]
for n in (12,20,28):
 z,w=leggauss(n);z=(z+1)*2.5;w=w*2.5
 xx,yy=np.meshgrid(z,z,indexing='ij');pts=np.column_stack([xx.ravel(),yy.ravel()]);weights=np.outer(w,w).ravel();q=Q(pts);H=pts[:,0]*pts[:,1]*(pts[:,0]+pts[:,1])/2;W=H*np.exp(-q)
 kernel=np.zeros((n*n,n*n))
 for refl,sign in group:
  diff=pts[None,:,:]-(pts@refl.T)[:,None,:];kernel+=sign*np.exp(-Q(diff))
 kernel*=np.sqrt(3)/(2*np.pi)
 symerr=float(np.max(abs(kernel-kernel.T)));assert symerr<1e-12
 d=np.sqrt(weights*W);B=d[:,None]*kernel*d[None,:]
 eig,v=eigh(B,subset_by_index=[n*n-2,n*n-1]);u=v[:,-1];u*=np.sign(np.sum(u));moment=float(np.sum(u*u*q*(q-7)/4))
 rows.append(dict(n=n,points=n*n,mu0=float(eig[-1]),mu1=float(eig[-2]),gap=float(eig[-1]-eig[-2]),correction_moment=moment,mass_Q_gt7=float(np.sum(u[q>7]**2)),min_kernel=float(kernel.min()),symmetry_error=symerr,trace=float(np.trace(B))))
 del diff,kernel,B,v
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);assert rss<180
print(json.dumps(dict(rows=rows,seconds=time.monotonic()-start,rss_MiB=rss,source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),scope='Uncertified fixed-grid diagnostics; no sign theorem from floating matrices'),indent=2,allow_nan=False))
