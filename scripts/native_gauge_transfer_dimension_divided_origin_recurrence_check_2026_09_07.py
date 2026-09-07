#!/usr/bin/env python3
import time,os,signal
AUDIT_TIMEOUT_SEC=180
START=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import math,json,sys,resource,hashlib
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator,expm_multiply
checks=[]
def ck(name,value):
 if name in checks or not bool(value):raise AssertionError(name)
 checks.append(name)
rows=[];returns=[]
for beta in (128,512,2048):
 root=math.sqrt(beta);N=math.ceil(8*root)+1;size=N*N
 def action(v):
  x=np.asarray(v).reshape(N,N,-1);y=-beta*x.copy()
  y[1:]+=beta/6*x[:-1];y[:-1]+=beta/6*x[1:]
  y[:,1:]+=beta/6*x[:,:-1];y[:,:-1]+=beta/6*x[:,1:]
  y[1:,:-1]+=beta/6*x[:-1,1:];y[:-1,1:]+=beta/6*x[1:,:-1]
  return y.reshape(np.asarray(v).shape)
 G=LinearOperator((size,size),matvec=action,rmatvec=action,matmat=action,rmatmat=action,dtype=float)
 v=np.zeros(size);v[0]=1
 gv=action(v);ck(f'origin two live neighbors {beta}',np.count_nonzero(gv)==3);del gv
 out=expm_multiply(G,v,traceA=-beta*size)
 ck(f'finite nonnegative output {beta}',np.all(np.isfinite(out)) and out.min()>=-1e-14)
 ret=float(out[0]);ck(f'positive return {beta}',ret>0)
 rate=2*beta/3;theta=math.asinh(N/rate);tail=2*math.exp(-theta*N+rate*(math.cosh(theta)-1))
 ck(f'finite tail {beta}',math.isfinite(tail) and tail>0)
 returns.append(dict(beta=beta,box_side=N,killed_return=ret,entry_box_error_bound=tail,tail_over_return=tail/ret))
 r=math.floor(root);ends=((0,0),(0,1),(0,r),(1,r),(r,math.floor(3*root/4)),(r,r),(2*r,r))
 for p,q in ends:
  d=(p+1)*(q+1)*(p+q+2)//2;a=float(out[p*N+q]);m=a/(d*ret)
  x=(p+1)/root;y=(q+1)/root;Q=x*x+x*y+y*y
  leading=math.exp(-Q);corr=leading*(3-7*Q/4+Q*Q/4)/beta
  err0=m-leading;err1=m-leading-corr;ratio_box=(tail/ret+a*tail/ret**2)/d
  ck(f'finite row {beta} {p} {q}',all(math.isfinite(z) for z in (m,leading,corr,err0,err1,ratio_box)))
  if (p,q)==(0,0):ck(f'exact vacuum ratio {beta}',m==1.)
  if beta>=2048:ck(f'theorem diagnostic {p} {q}',abs(err1)+ratio_box<1710/beta**2)
  rows.append(dict(beta=beta,label=[p,q],dimension=d,native_dimension_divided=m,gaussian=leading,correction=corr,leading_residual=err0,corrected_residual=err1,ratio_box_error_bound=ratio_box,theorem_domain=beta>=2048))
 del out,v,G
ck('all frozen rows',len(rows)==21);ck('unique case keys',len({(r['beta'],tuple(r['label'])) for r in rows})==21)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
ck('RSS below180MiB',math.isfinite(rss) and 0<rss<180);ck('runtime below180seconds',time.monotonic()-START<180)
result=dict(status='PASS',checks=checks,rows=rows,returns=returns,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),runtime_input_files=[],seconds=time.monotonic()-START,rss_MiB=rss,scope='Frozen origin-column dimension-divided diagnostics. Floating expm and Chernoff evaluation uncertified; box error explicitly divided by return. No eigenvalue fit or theorem constant selection.')
if '--json' in sys.argv:print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS:',len(checks),'checks;21 origin, wall, nearwall and interior entries.')
 print('per_element: Actual native six-shift killed origin recurrence; dimensions computed exactly.')
 print('per_site: Beta128/512 controls and beta2048 theorem-domain diagnostic; vacuum ratio1.')
 print('per_mode: Every leading/corrected residual retained; box tail priced against tiny return.')
 print('per_block: Floating exponential and tail uncertified; no spectral fit or constant retuning.')
 print('lattice_wide: No runtime file inputs; source SHA '+result['source_sha256'])
 print("TOTAL: PASS="+str(len(checks))+" FAIL=0")
