#!/usr/bin/env python3
"""Fixed two-endpoint killed native walk diagnostic; floating expm is not certified."""
import time, os, signal
START=time.monotonic(); signal.alarm(180)
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'): os.environ[key]='1'
import sys,json,hashlib,resource,math
from pathlib import Path
import numpy as np
from scipy.sparse import diags,kron,eye
from scipy.sparse.linalg import expm_multiply, LinearOperator
CHECKS=0
def check(v):
 global CHECKS
 CHECKS+=1
 if not v: raise AssertionError((CHECKS, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
def finite(x):
 check(bool(np.all(np.isfinite(x))))
s1=np.array([[-1,0],[1,1]]);s2=np.array([[1,1],[0,-1]])
group=((np.eye(2,dtype=int),1),(s1,-1),(s2,-1),(s1@s2,1),(s2@s1,1),(s1@s2@s1,-1))
rows=[]
for beta in (128,512,2048):
 root=math.sqrt(beta);p=(math.floor(root),math.floor(3*root/4));N=max(p)+math.ceil(6*root)+1
 size=N*N
 def action(v):
  a=np.asarray(v).reshape(N,N,-1); b=-beta*a.copy()
  b[1:]+=beta/6*a[:-1];b[:-1]+=beta/6*a[1:]
  b[:,1:]+=beta/6*a[:,:-1];b[:,:-1]+=beta/6*a[:,1:]
  b[1:,:-1]+=beta/6*a[:-1,1:];b[:-1,1:]+=beta/6*a[1:,:-1]
  return b.reshape(np.asarray(v).shape)
 G=LinearOperator((size,size),matvec=action,rmatvec=action,matmat=action,rmatmat=action,dtype=float)
 probe=np.zeros(size);probe[(N//2)*N+N//2]=1;gp=action(probe)
 check(np.count_nonzero(gp)==7);check(abs(float(gp.sum()))<1e-12)
 del probe,gp
 v=np.zeros(N*N);v[p[0]*N+p[1]]=1
 ends=((0,0),(0,p[1]),(p[0],0),p,(p[0]+math.floor(root/2),p[1]),(2*p[0],2*p[1]))
 for t in (.5,1.):
  out=expm_multiply(t*G,v,traceA=-beta*t*N*N);finite(out);check(float(out.min())>=-1e-14);check(float(out.sum())<=1+1e-12)
  rate=2*beta*t/3;bounds=[]
  for start in p:
   d=N-start;theta=math.asinh(d/rate);bounds.append(math.exp(-theta*d+rate*(math.cosh(theta)-1)))
  trunc=sum(bounds);finite(trunc)
  for q in ends:
   x=(np.asarray(p)+1)/root;y=(np.asarray(q)+1)/root
   leading=0.; correction=0.
   for w,sign in group:
    z=y-w@x;r=(z[0]**2+z[0]*z[1]+z[1]**2)/t
    term=sign*math.sqrt(3)/(2*math.pi*t)*math.exp(-r)
    leading+=term;correction+=term*(r*r-4*r+2)/(4*beta*t)
   actual=float(beta*out[q[0]*N+q[1]]);err0=actual-leading;err1=actual-leading-correction
   finite([actual,leading,correction,err0,err1]);check(actual>=-1e-12)
   if beta>=2048:check(abs(err1)+beta*trunc<18/beta**2)
   rows.append(dict(beta=beta,time=t,source=list(p),endpoint=list(q),box_side=N,native_scaled_entry=actual,gaussian=leading,second_order_correction=correction,leading_residual=err0,corrected_residual=err1,beta_squared_corrected_residual=beta**2*err1,entry_truncation_upper_bound=trunc,scaled_entry_truncation_upper_bound=beta*trunc,theorem_domain=beta>=2048))
 del G,v,out
check(len(rows)==36);check(len({(r["beta"],r["time"],tuple(r["source"]),tuple(r["endpoint"])) for r in rows})==36)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
finite(rss);check(rss<180);check(time.monotonic()-START<180)
result=dict(status='PASS',checks=CHECKS,rows=rows,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),runtime_input_files=[],seconds=time.monotonic()-START,rss_MiB=rss,scope='36 frozen two-endpoint entries. Floating expm_multiply is uncertified; the Chernoff inequality addresses box truncation only and its floating asinh/cosh/exp evaluations are not certified enclosures. Beta128/512 are outside theorem domain; no fitted constant or spectral conclusion.')
if '--json' in sys.argv: print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS: native six-neighbor killed recurrence, 36 frozen entries;',CHECKS,'checks')
 print('per_element: actual six-shift killed generator and adjoint; 36 frozen kernel entries, 119 actual checks.')
 print('per_site: shifted nonorigin sources, wall/interior endpoints; beta128/512/2048, t=.5/1; all signed residuals retained in --json.')
 print('per_mode: analytic box-exit Chernoff inequality; floating asinh/cosh/exp evaluation and expm_multiply are not certified enclosures.')
 print('per_block: beta2048 is the theorem-domain diagnostic; smaller beta are controls, no improvement filter or fitted constant.')
 print('lattice_wide: not executed; finite boxes only, no spectral conclusion; source SHA '+result['source_sha256'])
 for row in rows: print('KERNEL_ROW',json.dumps(row,sort_keys=True,allow_nan=False))
 print('RESOURCES',result['seconds'],result['rss_MiB'],'seconds/MiB; limits180/180; BLAS1')
