import os,sys,time,signal,resource,json,hashlib
from pathlib import Path
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
sys.dont_write_bytecode=True;p=Path(__file__).resolve().parent;os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');signal.alarm(180);start=time.monotonic()
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
from itertools import product,combinations
L=2;vol=8;M=24;sites=list(product(range(2),repeat=3));links=[(r,a) for r in sites for a in range(3)];idx={x:i for i,x in enumerate(links)}
faces=[]
for a,b in combinations(range(3),2):
 for r in sites:
  ra=list(r);rb=list(r);ra[a]^=1;rb[b]^=1
  faces.append([idx[r,a],idx[tuple(ra),b],idx[tuple(rb),a],idx[r,b]])
x0=sum(1<<i for i,(r,a) in enumerate(links) if r[a]);states=[x0];lookup={x0:0};rr=[];cc=[]
for x in states:
 for f in faces:
  z=[(x>>i)&1 for i in f]
  if z[0]==z[2] and z[1]==z[3] and z[0]!=z[1]:
   y=x^sum(1<<i for i in f)
   if y not in lookup:lookup[y]=len(states);states.append(y)
   rr.append(lookup[y]);cc.append(lookup[x])
checks={}
def ck(k,b):
 if not bool(b):raise AssertionError(k)
 checks[k]=True
n=len(states);ck('actual_component',n==864 and len(rr)==6912)
A=sparse.coo_matrix((np.ones(len(rr)),(rr,cc)),shape=(n,n)).tocsr();nf=np.asarray(A.sum(0)).ravel();N=sparse.diags(nf);I=sparse.eye(n,format='csr')
bits=((np.array(states)[:,None]>>np.arange(24))&1).astype(np.uint8)
coeff=np.array([[(-1)**r[a]/np.sqrt(vol) if d==b else 0 for r,d in links] for a in range(3) for b in range(3) if a!=b]);O=(bits-.5)@coeff.T;X=np.sum(O*O,axis=1);bound=3*vol/2
ck('source_bound',np.max(X)<=bound+1e-13 and np.min(X)>=0)
sys.path.insert(0,'/private/tmp/toe-physical-supplier-24h-20260908/scripts')
from spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03 import build_geometry
sys.path.insert(0,str(p.parent/'detuned-energy-moment'))
import producer_original as prod
cr,ci,modes=prod.transverse_coefficients(2,(1,));ck('geometry_literal',np.array_equal(build_geometry(2).plaquette_links,faces));ck('source_actual_producer',np.max(abs(prod.evaluate_observables(bits,cr,ci)-O))<1e-12)
wrongcoeff=np.array([[(-1)**r[a]/np.sqrt(vol) if d==b else 0 for r,d in links] for a in range(3) for b in range(3) if a!=b]);wrongX=np.sum(((bits-.5)@wrongcoeff.T)**2,axis=1);ck('wrong_stagger_detected',np.max(abs(wrongX-X))>1)
rows=[];data={};windowrows=[]
r0=np.zeros(n);r0[0]=1
RK=I-(N-A)/M
for _ in range(20*M):r0=RK@r0
for V in [.95,1.]:
 for lam in [-.02,-.01,-.005,0.,.005,.01,.02]:
  shift=abs(lam)*bound;H=V*N-A+sparse.diags(lam*X);G=I-(H-shift*I)/M
  branch=1+((1-V)*nf+shift-lam*X)/M
  P=A@sparse.diags(1/(M*branch))+sparse.diags(1-nf/(M*branch))
  delta=(P@sparse.diags(branch)-G).tocsr();res=0 if not delta.nnz else np.max(abs(delta.data))
  ck(f'kernel_{V}_{lam}',res<1e-13 and min(branch)>=1-1e-13 and min(P.data)>=-1e-13 and max(abs(np.asarray(P.sum(0)).ravel()-1))<1e-13)
  e,u=eigsh(H,k=1,which='SA',tol=1e-13,v0=1+np.arange(n)/n);E=float(e[0]);psi=u[:,0]*np.sign(u[:,0].sum());ck(f'eigen_{V}_{lam}',min(psi)>0 and np.linalg.norm(H@psi-E*psi)<1e-10)
  mixed=float(psi@((V-1)*nf+lam*X)/psi.sum());pureX=float(psi**2@X);mixedX=float(psi@X/psi.sum());shifted=1-float(np.sum(G@psi)/sum(psi));shifted*=M
  ck(f'energy_restore_{V}_{lam}',abs(mixed-E)<1e-10 and abs(shifted+shift-E)<1e-10)
  r=r0.copy();window=[]
  for sweep in range(80):
   for _ in range(M):r=G@r;r/=sum(r)
   if sweep>=40:window.append(float(r@((V-1)*nf+lam*X)))
  row={'V':V,'lambda':lam,'shift':shift,'E':E,'shifted_E':shifted,'mixed_energy':mixed,'pure_X':pureX,'mixed_X':mixedX,'pure_O_means':((psi**2)@O).tolist(),'kernel_max_residual':float(res),'branch_range':[float(min(branch)),float(max(branch))],'window_energy':float(np.mean(window)),'window_error':float(np.mean(window)-E)}
  rows.append(row);data[V,lam]=(E,psi,pureX)
# Shift and branch counterexamples, without pretending symmetric differentiation necessarily detects a cusp.
q=next(r for r in rows if r['V']==.95 and r['lambda']==.02);ck('omitted_restoration_detected',abs(q['shifted_E']-q['E'])>.2)
V=.95;lam=.02;branch=1+((1-V)*nf+abs(lam)*bound-lam*X)/M;old=1+(1-V)*nf/M
ck('old_unsourced_branch_detected',max(abs(branch-old))>.001)
ck('transition_only_wrong',max(abs(branch-1))>.01)
ck('unshifted_acceptance_invalid',min(1-X/M)<1 and max(1/(1-X/M))>1)
ck('mixed_pure_not_identical',abs(data[.95,0.][2]-next(r['mixed_X'] for r in rows if r['V']==.95 and r['lambda']==0))>1e-3)
stencils=[]
for V in [.95,1.]:
 E,psi,target=data[V,0.]
 for h in [.02,.01,.005]:
  plus=data[V,h][0];minus=data[V,-h][0];d=(plus-minus)/(2*h);lo=(plus-E)/h;hi=(E-minus)/h
  ck(f'concavity_{V}_{h}',lo-1e-9<=target<=hi+1e-9)
  stencils.append({'V':V,'h':h,'derivative':d,'pure_X':target,'error':d-target,'concavity_interval':[lo,hi]})
# Simultaneous energy responses at lambda0: V derivative uses fixedh.02, source derivative retains all declared h.
Es=[]
for V in [.93,.97]:Es.append(float(eigsh(V*N-A,k=1,which='SA',tol=1e-13,v0=1+np.arange(n)/n)[0][0]))
E,psi,T=data[.95,0.];B=float(psi@(A@psi));Bh=.95*(Es[1]-Es[0])/.04-E
moments=[{'source_h':r['h'],'moment_two_response':.5*Bh/r['derivative'],'pure_moment':.5*B/T,'error':.5*Bh/r['derivative']-.5*B/T} for r in stencils if r['V']==.95]
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);ck('resource',rss<384 and time.monotonic()-start<180)
out={'checks':checks,'count':len(checks),'states':n,'directed_geometric_moves':len(rr),'X_range':[float(min(X)),float(max(X))],'X_global_bound':bound,'rows':rows,'stencils':stencils,'two_response_moments':moments,'seconds':time.monotonic()-start,'rss_mib':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
np.savez_compressed(p/'raw.npz',states=states,faces=faces,rows=rr,columns=cc,nf=nf,O=O,X=X)
(p/'RESULT.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(out,indent=2,allow_nan=False))
