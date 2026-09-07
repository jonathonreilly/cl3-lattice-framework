#!/usr/bin/env python3
"""Fixed two-endpoint killed native walk diagnostic; floating expm is not certified."""
import time, os, signal
START=time.monotonic(); signal.alarm(180)
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'): os.environ[key]='1'
import sys,json,hashlib,resource,math
from pathlib import Path
import numpy as np
from scipy.sparse import diags,kron,eye
from scipy.sparse.linalg import expm_multiply
CHECKS=0
def check(v):
 global CHECKS
 CHECKS+=1
 if not v: raise AssertionError(CHECKS)
def finite(x):
 check(bool(np.all(np.isfinite(x))))
s1=np.array([[-1,0],[1,1]]);s2=np.array([[1,1],[0,-1]])
group=((np.eye(2,dtype=int),1),(s1,-1),(s2,-1),(s1@s2,1),(s2@s1,1),(s1@s2@s1,-1))
rows=[]
for beta in (128,512,2048):
 root=math.sqrt(beta);p=(math.floor(root),math.floor(3*root/4));N=max(p)+math.ceil(6*root)+1
 up=diags(np.ones(N-1),1,shape=(N,N),format='csr');ident=eye(N,format='csr')
 J=(kron(up,ident)+kron(ident,up)+kron(up,up.T)).tocsr();J=(J+J.T)/6
 G=beta*(J-eye(N*N,format='csr'))
 check((G-G.T).nnz==0);check(float(np.max(np.asarray(J.sum(axis=0))))<=1.000000000000001)
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
 del G,J,v,out,up,ident
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
finite(rss);check(rss<180);check(time.monotonic()-START<180)
result=dict(status='PASS',checks=CHECKS,rows=rows,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),runtime_input_files=[],seconds=time.monotonic()-START,rss_MiB=rss,scope='36 frozen two-endpoint entries. Floating expm_multiply is uncertified; Chernoff bound addresses box truncation only. Beta128/512 are outside theorem domain; no fitted constant or spectral conclusion.')
if '--json' in sys.argv: print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS: native six-neighbor killed recurrence, 36 frozen entries;',CHECKS,'checks')
 print('N5: shifted nonorigin sources, wall and interior endpoints; beta128/512/2048, t=.5/1.')
 print('N5: leading and corrected residuals retained in --json; no improvement filter.')
 print('N5: finite-box Chernoff truncation bound; floating exponential remains uncertified.')
 print('N5: beta2048 is the theorem-domain diagnostic; smaller beta are controls.')
 print('N5: no spectral fit or theorem-constant adjustment; source SHA '+result['source_sha256'])
