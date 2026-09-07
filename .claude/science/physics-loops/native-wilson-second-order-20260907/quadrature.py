import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
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
  assert D>0 and np.isfinite(N)
  value=N/D
  estimates.append(dict(order=order,N=N,D=D,value=value,scaled_first_correction=beta*(value-W),second_order_residual=beta**2*(value-W-W2/beta)))
 rows.append(dict(beta=beta,p=p,q=q,x=x,y=y,W=W,W2=W2,wrong_coefficient_without_denominator=W2-W,estimates=estimates))
print(json.dumps(dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=rows,scope='Actual full scaled torus numerical quadrature; convergence support not rigorous integral enclosure.'),indent=2,allow_nan=False))
