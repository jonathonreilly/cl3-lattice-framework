#!/usr/bin/env python3
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'): os.environ[k]='1'
import signal,time,resource,sys
signal.alarm(180)
started=time.monotonic()
import numpy as np
from scipy.linalg import expm,eigvalsh
import json,hashlib
from pathlib import Path
edges=[(0,1),(1,2),(2,3),(3,4),(4,5)]
weights=[np.sqrt(2)/3,-1,1,1,-np.sqrt(3)/4]
terms=[]
for (a,b),w in zip(edges,weights):
 x=np.zeros((6,6));x[a,b]=x[b,a]=w;terms.append(x)
h=sum(terms[i] for i in (0,1,3,4)); seed=terms[2]
cuts=[[],[1,3],[0,1,3],[0,1,3,4]]
times=[0,1/32,1/16,1/8,1/4,1/2,1,2]
rows=[]
for cut in cuts:
 hr=sum((terms[i] for i in cut),np.zeros((6,6)))
 omitted=[i for i in (0,1,3,4) if i not in cut]
 # Distances in remaining graph to an endpoint of an omitted hopping.
 dist={2:0,3:0};front=[2,3]
 while front:
  a=front.pop(0)
  for i in (0,1,3,4):
   u,v=edges[i]
   if a in (u,v):
    b=v if a==u else u
    if b not in dist:dist[b]=dist[a]+1;front.append(b)
 m=1+min((min(dist[a],dist[b]) for i in omitted for a,b in [edges[i]]),default=999)
 for tau in times:
  E=expm(-1j*h*tau)@expm(1j*(h+seed)*tau)
  R=expm(-1j*hr*tau)@expm(1j*(hr+seed)*tau)
  z=np.linalg.eigvals(E.conj().T@R)
  products=np.ones(1,dtype=complex)
  for val in z:products=np.concatenate([products,products*val])
  echo=float(np.max(np.abs(1-products)))
  ext=h-hr;G=R.conj().T@ext@R-ext
  lam=eigvalsh(G)
  drift=float(max(sum(lam[lam>0]),-sum(lam[lam<0])))
  def tail(n,x):
   # Positive recurrence avoids cancellation near zero.
   import math
   term=x**n/math.factorial(n);s=term
   for k in range(n+1,300):
    term*=x/k;s+=term
    if term<1e-18*max(s,1e-300):break
   return s
  # Chain d=2 and t=max|weight|=1, source-code all Fock bound.
  eb=0. if not omitted else min(2.,4*tail(m+1,2*abs(tau)))
  gb=0. if not omitted else min(4*tail(m,2*abs(tau)),8*abs(tau))
  assert all(np.isfinite(v) for v in (echo,drift,eb,gb))
  assert echo<=eb+3e-13 and drift<=gb+3e-13
  rows.append(dict(cut=cut,tau=tau,m=None if not omitted else m,echo_norm=echo,energy_drift_norm=drift,echo_bound=eb,energy_bound=gb))
result=dict(method='6x6 one-particle exterior spectral identities; all 64 occupation subsets via eigenvalue products; no Fock matrices',rows=rows,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
elapsed=time.monotonic()-started
assert rss<180 and elapsed<180
result.update(dependencies={},resources=dict(timeout_seconds=180,rss_limit_MiB=180,blas_threads=1),seconds=elapsed,rss_MiB=rss)
if '--json' in sys.argv:
 print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS independent exterior-spectral quench witness: 32 cut/time rows satisfy echo and energy-defect bounds.')
 print('per_element: six eigenvalues generate all 64 exterior subset products and all-N Hermitian subset sums.')
 print('per_site: six chain modes, five weighted edges and the central seed are explicit; no ambient native-code matrix is simulated.')
 print('per_mode: only 6x6 one-particle exponentials and spectra are used; no full-Fock matrix or primary imports.')
 print('per_block: four whole-hop truncations at eight Fourier times; actual locality orders 1,2,2,infinity are checked.')
 print('lattice_wide: not executed; this finite CAR witness does not simulate a cube device or a local Markov bath.')
 print('SOURCE_SHA256',result['source_sha256'])
 print('DEPENDENCIES {}')
 print('RESOURCES',json.dumps(dict(seconds=elapsed,rss_MiB=rss,**result['resources']),sort_keys=True))
 print('TOTAL: PASS FAIL=0')
