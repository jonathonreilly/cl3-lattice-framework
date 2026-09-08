import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import time,signal,resource,json,importlib.util
signal.alarm(180);start=time.monotonic()
import numpy as np
from scipy.linalg import eigh
p='/private/tmp/toe-physical-supplier-24h-20260908/scripts/spin_half_cartesian_plaquette_source_2026_09_07.py'
spec=importlib.util.spec_from_file_location('source_geometry',p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
links,faces,states,arcs=mod.component();rows,cols,_,_=arcs.T;N=len(states);M=24
A=np.zeros((N,N));np.add.at(A,(rows,cols),1);counts=A.sum(1)
O=np.array([sum((-1)**sum(r)*(((s>>i)&1)-.5)*(-1)**r[0]/np.sqrt(8) for i,(r,a) in enumerate(links) if a==1) for s in states])
out=[]
for V in [1.,.95]:
 H=np.diag(V*counts)-A;e,U=eigh(H);psi=U[:,0];psi*=np.sign(psi.sum());q=1-e/M;rat=q/q[0]
 assert abs(O@psi**2)<1e-11
 amp=U.T@(O*psi);weights=amp**2;weights/=weights.sum();support=np.flatnonzero(weights>1e-10)
 pure=np.array([weights@(rat**(M*t)) for t in range(17)])
 fits=lambda c:{str((a,b)):float((M-e[0])*(1-np.exp(np.polyfit(np.arange(a,b+1),np.log(c[a:b+1]),1)[0]/M))) if np.min(c[a:b+1])>0 else None for a,b in [(2,6),(8,14)]}
 entry={'V':V,'ground':float(e[0]),'supported_gap':float(e[support[0]]-e[0]),'first_level_weight':float(weights[abs(e-e[support[0]])<1e-9].sum()),'spectral_variance':float(weights@(e-e[0])**2-(weights@(e-e[0]))**2),'pure_curve':pure.tolist(),'pure_fits':fits(pure),'forward':{}}
 for F in [0,1,2,6,12,20]:
  left=U@((U.T@np.ones(N))*rat**(M*F)); coeff=(U.T@(left*O))*amp; c=np.array([coeff@(rat**(M*t))/coeff.sum() for t in range(17)])
  entry['forward'][str(F)]={'curve':c.tolist(),'max_absolute_bias':float(max(abs(c-pure))),'fits':fits(c),'negative_spectral_coefficients':int(np.sum(coeff< -1e-11))}
  G=np.eye(N)-H/M;vec=O*psi
  for _ in range(M):vec=G@vec/q[0]
  assert abs((left*O)@vec/coeff.sum()-c[1])<1e-10
 if V==1:assert max(v['max_absolute_bias'] for v in entry['forward'].values())<1e-10
 out.append(entry)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if __import__('sys').platform=='darwin' else 1024)
assert 0<rss<180
print(json.dumps({'states':N,'directed_moves':len(arcs),'rows':out,'seconds':time.monotonic()-start,'rss_mib':rss},indent=2,allow_nan=False))
