#!/usr/bin/env python3
"""Actual full-torus quadrature support; not a certified integral enclosure."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import signal,time,resource,sys
signal.alarm(180);started=time.monotonic()
import numpy as np
from scipy.special import roots_legendre
import json,hashlib
from pathlib import Path
rows=[]
for beta in [128,256,512,1024]:
 p=int(np.floor(np.sqrt(beta)))-1;q=int(np.floor(1.5*np.sqrt(beta)))-1
 x=(p+1)/np.sqrt(beta);y=(q+1)/np.sqrt(beta)
 Q=x*x+x*y+y*y;W=x*y*(x+y)/2*np.exp(-Q);W2=(3-7*Q/4+Q*Q/4)*W
 estimates=[]
 for order in [256,384,512]:
  nodes,weights=roots_legendre(order);z=nodes*np.pi*np.sqrt(beta);wt=weights*np.pi*np.sqrt(beta)
  u=z[:,None];v=z[None,:];k=u/np.sqrt(beta);l=v/np.sqrt(beta)
  # Stable exact cosine deficit, not Taylor approximated.
  exponent=beta*(2/3)*(np.sin(k/2)**2+np.sin(l/2)**2+np.sin((k-l)/2)**2)
  alternant=8*beta**1.5*np.sin((2*k-l)/2)*np.sin((k-2*l)/2)*np.sin((k+l)/2)
  mass=np.exp(-exponent)*wt[:,None]*wt[None,:]
  N=float(np.sum(mass*alternant*np.sin(u*x+v*y))/(2*np.pi)**2)
  D=float(np.sum(mass*alternant**2)/(6*(2*np.pi)**2))
  if not(D>0 and np.isfinite(D) and np.isfinite(N)):raise AssertionError("nonfinite integral or denominator")
  value=N/D
  estimates.append(dict(order=order,N=N,D=D,value=value,scaled_first_correction=beta*(value-W),second_order_residual=beta**2*(value-W-W2/beta)))
 rows.append(dict(beta=beta,p=p,q=q,x=x,y=y,W=W,W2=W2,wrong_coefficient_without_denominator=W2-W,estimates=estimates))
for row in rows:
 if not(.25<=row['x']<=2 and .25<=row['y']<=2):raise AssertionError('window')
 estimates=row['estimates']
 if abs(estimates[-1]['value']-estimates[-2]['value'])>=2e-12:raise AssertionError('mesh convergence')
 for est in estimates:
  for value in est.values():
   if not np.isfinite(value):raise AssertionError('nonfinite support field')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);elapsed=time.monotonic()-started
if not(0<rss<180 and 0<=elapsed<180):raise AssertionError('resource contract')
result=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=rows,dependencies={},seconds=elapsed,rss_MiB=rss,
 resources=dict(timeout_seconds=180,rss_limit_MiB=180,blas_threads=1),scope='Actual full scaled torus numerical quadrature; convergence support not rigorous integral enclosure. Frozen beta128,256,512,1024 are diagnostics, not the theorem threshold2048.')
if '--json' in sys.argv:print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS actual native Wilson torus quadrature support')
 print('per_element: exact sine-symbol and Weyl-alternant integrands; no Gaussian replacement.')
 print('per_site: rho-shifted integer endpoints in the frozen compact window.')
 print('per_mode: positive denominator and all real integral/error fields retained on GL256/384/512.')
 print('per_block: four frozen beta128/256/512/1024 comparisons; coefficient unchanged and not fitted.')
 print('lattice_wide: numerical convergence only; no certified enclosure, theorem proof or spectral inference.')
 print('SOURCE_SHA256',result['source_sha256']);print('DEPENDENCIES {}')
 print('RESOURCES',elapsed,rss,'seconds/MiB;180 limits, BLAS1')
 print('TOTAL: PASS FAIL=0')
