import os,sys,time,signal,resource,json,argparse,hashlib
from pathlib import Path
from fractions import Fraction as F
p=Path(__file__).resolve().parent
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'cache');sys.dont_write_bytecode=True
ap=argparse.ArgumentParser();ap.add_argument('--L',type=int,choices=[8,16],required=True);ap.add_argument('--burn',type=int,choices=[32,128],default=32);ap.add_argument('--shard',type=int,choices=range(4),default=0);ap.add_argument('--profile',action='store_true');a=ap.parse_args();signal.alarm(30 if a.profile else 900);start=time.monotonic()
sys.path[:0]=[str(p.parent/'rk-inverse-moment/pilot'),str(p.parent/'detuned-energy-moment'),'/private/tmp/toe-physical-supplier-24h-20260908/scripts']
import numpy as np
from numba import njit
import producer_original as prod
from kernel import endpoint,observe,generate_lags
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice,vertex_degrees,electric_flux
@njit(cache=True)
def chain(initial,faces,coeff,lags,caps,burn,cid):
 n=len(lags);o=np.empty((n,len(coeff)),np.complex128);y=np.zeros((n,6,len(coeff)),np.complex128);nf=np.zeros(n,np.int64);snap=np.empty((n,len(initial)),np.uint8)
 state=endpoint(initial,faces,burn*len(faces),500000000+cid)
 for i in range(n):
  state=endpoint(state,faces,len(faces),600000000+1000*cid+i);snap[i]=state;o[i]=observe(state,coeff)
  for face in faces:nf[i]+=prod.is_flippable(state,face)
  for j in range(6):
   if lags[i,j]<=caps[j]:y[i,j]=np.conjugate(o[i])*observe(endpoint(state,faces,lags[i,j],700000000+1000*cid+6*i+j),coeff)
 return o,y,nf,snap
L=a.L;M=3*L**3;g=prod.build_geometry(L);cr,ci,modes=prod.transverse_coefficients(L,(1,L//4));coeff=cr+1j*ci;initial=initial_ice(L).ravel()
t=time.monotonic();alphas=np.array([k*2*np.sin(np.pi/L)**2 for k in [.25,.5,1]]+[.25,.5,1]);caps=[];cert=[]
assert F(482921,240000)>2
for alpha in alphas:
 aa=F(float(alpha));n=0
 while F(1,2**n)/aa>F(1,1000):n+=1
 z=(M+aa)/aa*F(7*n,10);kp=(z.numerator+z.denominator-1)//z.denominator
 caps.append(kp-1);cert.append(dict(n=n,alpha_num=aa.numerator,alpha_den=aa.denominator,bound=float(F(1,2**n)/aa)))
caps=np.array(caps,np.int64);cap_seconds=time.monotonic()-t;qs=M/(M+alphas)
if a.profile and L==16:
 prior=json.loads((p/'PROFILE_L8.json').read_text());ratio=(3*16**3*(1+sum(1/np.array([k*2*np.sin(np.pi/16)**2 for k in [.25,.5,1]]+[.25,.5,1]))))/(M/8*(1+sum(1/np.array([k*2*np.sin(np.pi/8)**2 for k in [.25,.5,1]]+[.25,.5,1]))))
 if 5*prior['hot_seconds']*ratio>=20:raise RuntimeError('L16 forecast gate failed')
# Warm compilation explicitly excluded from hot timing, retained in total.
t=time.monotonic();chain(initial,g.plaquette_links,coeff,np.zeros((1,6),np.int64),caps,0,90000);warm=time.monotonic()-t
outdir=p/(f'profile_L{L}' if a.profile else f'L{L}_b{a.burn}_shard{a.shard}');outdir.mkdir(exist_ok=False)
rows=[];hot=time.monotonic()
for rep in range(1 if a.profile else 32):
 cid=20000+([8,16].index(L)*2+[32,128].index(a.burn))*128+a.shard*32+rep
 if a.profile:cid=90000+L
 lags=generate_lags(np.random.default_rng(800000000+cid).random((8 if a.profile else 64,6)),qs)
 t=time.monotonic();o,y,nf,snap=chain(initial,g.plaquette_links,coeff,lags,caps,8 if a.profile else a.burn,cid);compute=time.monotonic()-t
 t=time.monotonic()
 assert np.isfinite(o).all() and np.isfinite(y).all() and np.all(y[lags>caps]==0)
 for state in snap:
  assert np.all(vertex_degrees(state.reshape(L,L,L,3))==3) and electric_flux(state.reshape(L,L,L,3))==(0,0,0)
 validation=time.monotonic()-t;t=time.monotonic();fn=outdir/f'chain{cid}.npz';np.savez_compressed(fn,origins=o,products=y,Nf=nf,lags=lags,clipped=lags>caps)
 rows.append(dict(cid=cid,compute=compute,validation=validation,compression=time.monotonic()-t,sha=hashlib.sha256(fn.read_bytes()).hexdigest()));del snap,o,y,nf,lags
hot=time.monotonic()-hot;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);assert rss<384
result=dict(L=L,profile=a.profile,burn=8 if a.profile else a.burn,shard=a.shard,modes=modes,alphas=alphas.tolist(),caps=caps.tolist(),certificates=cert,cap_seconds=cap_seconds,warm_seconds=warm,hot_seconds=hot,total_seconds=time.monotonic()-start,rss_mib=rss,rows=rows,source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
print(json.dumps(result,indent=2))
