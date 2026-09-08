import os,sys,time,signal,json,resource,hashlib
from pathlib import Path
from fractions import Fraction
p=Path(__file__).resolve().parent
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'cache');sys.dont_write_bytecode=True
signal.alarm(30);t=time.monotonic()
sys.path[:0]=[str(p.parent/'rk-inverse-moment/pilot'),str(p.parent/'detuned-energy-moment'),'/private/tmp/toe-physical-supplier-24h-20260908/scripts']
import numpy as np
import producer_original as prod
from kernel import endpoint,observe,generate_lags
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice,vertex_degrees,electric_flux
L=8;M=3*L**3;hs=[1,L//4];g=prod.build_geometry(L);cr,ci,modes=prod.transverse_coefficients(L,tuple(hs));coeff=cr+1j*ci
alphas=np.array([k*(4*np.sin(np.pi*h/L)**2)/2 for h in hs for k in [.25,.5,1.]])
qs=M/(M+alphas);caps=[];bounds=[]
for a,q in zip(alphas,qs):
 aa=Fraction(float(a));qq=Fraction(M)/(M+aa);k=int(np.ceil(np.log(a*.001)/np.log(q)))-1
 while qq**(k+1)/aa>Fraction(1,1000):k+=1
 while k>0 and qq**k/aa<=Fraction(1,1000):k-=1
 caps.append(k);bounds.append(float(qq**(k+1)/aa))
cid=10000;lags=generate_lags(np.random.default_rng(800000000+cid).random((8,6)),qs)
state=endpoint(initial_ice(L).ravel(),g.plaquette_links,8*M,500000000+cid)
orig=[];ys=[];nf=[];snap=[];stepcounts=8*M
for i in range(8):
 state=endpoint(state,g.plaquette_links,M,600000000+1000*cid+i);stepcounts+=M
 assert np.all(vertex_degrees(state.reshape(L,L,L,3))==3) and electric_flux(state.reshape(L,L,L,3))==(0,0,0)
 o=observe(state,coeff);orig.append(o);snap.append(state.copy());nf.append(sum(prod.is_flippable(state,f) for f in g.plaquette_links));y=np.zeros((6,len(coeff)),complex)
 for j in range(6):
  if lags[i,j]<=caps[j]:
   other=endpoint(state,g.plaquette_links,int(lags[i,j]),700000000+1000*cid+6*i+j);stepcounts+=int(lags[i,j]);y[j]=np.conjugate(o)*observe(other,coeff)
 ys.append(y)
# independent literal complex signed update on one snapshot
signed=0
for face in g.plaquette_links:
 if prod.is_flippable(state,face):
  z=state.copy();z[face]^=1
  assert np.max(abs(observe(z,coeff)-observe(state,coeff)-coeff[:,face]@(1.-2*state[face])))<1e-11
  signed+=len(coeff)
np.savez_compressed(p/'MICRO_RAW.npz',origins=orig,products=ys,Nf=nf,lags=lags,snapshots=snap)
elapsed=time.monotonic()-t;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
assert elapsed<30 and rss<384
out=dict(L=L,mode='micro_only',seconds=elapsed,rss_mib=rss,alphas=alphas.tolist(),caps=caps,tail_bounds=bounds,steps=stepcounts,signed_cases=signed,clipped=np.sum(lags>np.array(caps),axis=0).tolist(),source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
print(json.dumps(out,indent=2))
