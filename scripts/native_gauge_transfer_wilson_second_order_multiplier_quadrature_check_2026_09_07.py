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
# Finite diagnostic separation, not the beta>=2048 theorem or an error enclosure.
# The competing coefficients differ by exactly W: quarter-W acceptance leaves
# a three-quarter-W exclusion margin. These margins are not fitted theorem constants.
COEFFICIENT_MARGIN=0.25
D0=27*np.sqrt(3)/np.pi
comparison_checks=[]
def ck(name,ok):
 if not ok:raise AssertionError(name)
 comparison_checks.append(name)
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
  denominator_first_error=beta*(D/D0-1)+1
  coefficient_error=(beta*(value-W)-W2)/W
  alternative_error=(beta*(value-W)-(W2-W))/W
  # GL256 is retained as a coarse diagnostic; acceptance uses the original
  # mesh-converged GL384/512 pair, without changing any quadrature order.
  if order in (384,512):
   ck(f'denominator first correction beta{beta} GL{order}',abs(denominator_first_error)<COEFFICIENT_MARGIN)
   ck(f'normalized coefficient beta{beta} GL{order}',abs(coefficient_error)<COEFFICIENT_MARGIN)
   ck(f'alternative excluded beta{beta} GL{order}',abs(alternative_error)>1-COEFFICIENT_MARGIN)
  estimates.append(dict(coefficient_acceptance_checked=order in (384,512),denominator_first_error=denominator_first_error,relative_coefficient_error=coefficient_error,relative_alternative_error=alternative_error,order=order,N=N,D=D,value=value,scaled_first_correction=beta*(value-W),second_order_residual=beta**2*(value-W-W2/beta)))
 rows.append(dict(beta=beta,p=p,q=q,x=x,y=y,W=W,W2=W2,wrong_coefficient_without_denominator=W2-W,estimates=estimates))
for row in rows:
 ck(f"actual shifted endpoint beta{row['beta']}",abs(row['x']*np.sqrt(row['beta'])-row['p']-1)<1e-12 and abs(row['y']*np.sqrt(row['beta'])-row['q']-1)<1e-12)
 if not(.25<=row['x']<=2 and .25<=row['y']<=2):raise AssertionError('window')
 estimates=row['estimates']
 if abs(estimates[-1]['value']-estimates[-2]['value'])>=2e-12:raise AssertionError('mesh convergence')
 for est in estimates:
  for value in est.values():
   if not np.isfinite(value):raise AssertionError('nonfinite support field')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);elapsed=time.monotonic()-started
if not(0<rss<180 and 0<=elapsed<180):raise AssertionError('resource contract')
result=dict(finite_comparison_assertion_count=len(comparison_checks),finite_comparison_checks=comparison_checks,coefficient_margin=COEFFICIENT_MARGIN,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=rows,dependencies={},seconds=elapsed,rss_MiB=rss,
 resources=dict(timeout_seconds=180,rss_limit_MiB=180,blas_threads=1),scope='Actual full scaled torus numerical quadrature; convergence support not rigorous integral enclosure. Frozen beta128,256,512,1024 are diagnostics, not the theorem threshold2048.')
if '--json' in sys.argv:print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS actual native Wilson torus quadrature support')
 print('RESULT '+json.dumps(result,sort_keys=True,allow_nan=False))
 print('per_element: exact sine-symbol and Weyl-alternant integrands; no Gaussian replacement.')
 print('per_site: rho-shifted integer endpoints in the frozen compact window.')
 print('per_mode: denominator -1 correction and quarter-W coefficient comparisons checked on converged GL384/512; GL256 retained as coarse diagnostic.')
 print('per_block: four frozen beta128/256/512/1024 cases; actual values and 28 finite comparison assertions retained; coefficient unchanged.')
 print('lattice_wide: numerical convergence only; no certified enclosure, theorem proof or spectral inference.')
 print('SOURCE_SHA256',result['source_sha256']);print('DEPENDENCIES {}')
 print('RESOURCES',elapsed,rss,'seconds/MiB;180 limits, BLAS1')
 print('TOTAL: PASS FAIL=0')
