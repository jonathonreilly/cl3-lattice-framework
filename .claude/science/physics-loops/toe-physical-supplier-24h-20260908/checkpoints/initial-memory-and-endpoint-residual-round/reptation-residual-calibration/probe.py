import os,sys,time,signal,resource,json,pathlib,hashlib
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
start=time.monotonic();signal.alarm(30);sys.dont_write_bytecode=True
import numpy as np
p=pathlib.Path(__file__).resolve().parent;sys.path.insert(0,str(p.parent/'detuned-reptation-l2'));import graph as g
oracle=[]
for n in [2,48,192]:
 psi=g.power(n//2);hp=g.H@psi;E=float(psi@hp);X=g.S;S=float(psi@(X*psi));NN=float(psi@(g.nf*psi));H2=float(hp@hp);XE=float((X*psi)@hp);X2=float(psi@(X*X*psi));D=.5*(.95*NN-E)/S;R=sum(float((g.O[:,j]*psi)@(g.H@(g.O[:,j]*psi))) for j in range(6))/S-E;corr=(XE-S*E)/S
 if abs(R-D-corr)>1e-12:raise RuntimeError('residual sign')
 varH=H2-E*E;varX=X2-S*S
 if abs(corr)>np.sqrt(max(0,varH)*varX)/S+1e-12:raise RuntimeError('oracle bound')
 oracle.append(dict(n=n,vector=[NN,S,E,H2,XE,X2],D=D,R=R,correction=corr,varH=varH,varX=varX))
n=48;path=[0]*(n+1);direction=1;rng=np.random.default_rng(202609170201);raw=[]
for _ in range(4096):
 old=path[-1] if direction==1 else path[0];second=path[1] if direction==1 else path[-2];u=rng.random()*(24+.05*g.nf[old]);f=int(u) if u<24 else -1;y=g.T[old,f] if f>=0 else -1;y=y if y>=0 else old;ok=rng.random()<min(1,g.b[old]/g.b[second])
 if ok:path=path[1:]+[int(y)] if direction==1 else [int(y)]+path[:-1]
 else:direction=-direction
 mid=path[n//2];hl=-.05*g.nf[path[0]];hr=-.05*g.nf[path[-1]];e=(hl+hr)/2;x=g.S[mid];raw.append([g.nf[mid],x,e,hl*hr,x*e,x*x])
raw=np.array(raw);np.savez_compressed(p/'MICRO_RAW.npz',vectors=raw);m=raw.mean(0);D=.5*(.95*m[0]-m[2])/m[1];correction=m[4]/m[1]-m[2];vh=m[3]-m[2]**2;vx=m[5]-m[1]**2
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if rss>=384 or time.monotonic()-start>=30:raise RuntimeError('resources')
print(json.dumps(dict(scope='nonequilibrated micro, not calibration',oracle=oracle,mean_vector=m.tolist(),covariance=np.cov(raw,rowvar=False).tolist(),D_plugin=D,R_plugin=D+correction,correction_plugin=correction,varH_plugin=vh,varX_plugin=vx,bound_plugin=None if vh<0 or vx<0 else np.sqrt(vh*vx)/m[1],seconds=time.monotonic()-start,rss_mib=rss),indent=2,allow_nan=False))
