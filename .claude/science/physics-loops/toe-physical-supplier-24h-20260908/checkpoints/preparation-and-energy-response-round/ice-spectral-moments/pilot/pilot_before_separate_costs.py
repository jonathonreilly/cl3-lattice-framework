import os,sys,time,signal,resource,json,argparse,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
for k in['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(P/'numba-cache');sys.dont_write_bytecode=True
ap=argparse.ArgumentParser();ap.add_argument('--L',type=int,choices=[2,4],default=2);ap.add_argument('--burn',type=int,choices=[32,128],default=32);ap.add_argument('--micro',action='store_true');args=ap.parse_args();signal.alarm(30 if args.micro else 120);start=time.monotonic()
sys.path.insert(0,'/private/tmp/toe-physical-supplier-24h-20260908/scripts')
import numpy as np
from numba import njit
from spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03 import build_geometry,is_flippable
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice,vertex_degrees,electric_flux

def coefficients(L):
 modes=[];rows=[];planes=[];scales=[];orient=[(0,1),(0,2),(1,2)]
 for h in ([1]if L==2 else[1,2]):
  for a in range(3):
   for b in range(3):
    if a==b:continue
    modes.append((h,a,b));row=np.zeros(3*L**3,dtype=np.complex128)
    for r in np.ndindex(L,L,L):row[np.ravel_multi_index((*r,b),(L,L,L,3))]=(-1)**sum(r)*np.exp(2j*np.pi*h*r[a]/L)/np.sqrt(L**3)
    rows.append(row);planes.append(orient.index(tuple(sorted((a,b)))));scales.append(4*np.sin(np.pi*h/L)**2/(2*L**3))
 return np.array(rows),np.array(planes),np.array(scales),modes

@njit(cache=True)
def measurements(state,faces,coeff,planes,scales):
 modes=coeff.shape[0];M=len(faces);O=np.zeros(modes,np.complex128);LO=np.zeros(modes,np.complex128);counts=np.zeros(3,np.int64)
 for m in range(modes):
  for i in range(len(state)):O[m]+=coeff[m,i]*(float(state[i])-.5)
 for f in range(M):
  if is_flippable(state,faces[f]):
   counts[f//(M//3)]+=1
   for m in range(modes):
    delta=0j
    for i in faces[f]:delta+=coeff[m,i]*(1.-2.*state[i])
    LO[m]-=delta
 result=np.empty((modes,4))
 for m in range(modes):result[m,0]=O[m].real;result[m,1]=O[m].imag;result[m,2]=(O[m].real**2+O[m].imag**2);result[m,3]=scales[m]*counts[planes[m]]
 return result,np.abs(LO)**2,counts

@njit(cache=True)
def chain(initial,faces,coeff,planes,scales,burn,samples,seed):
 np.random.seed(seed);state=initial.copy();M=len(faces);values=np.empty((samples,coeff.shape[0],5));counts=np.empty((samples,3),np.int64);snaps=np.empty((min(samples,64),len(state)),np.uint8)
 for sweep in range(burn+samples):
  for step in range(M):
   f=np.random.randint(M)
   if is_flippable(state,faces[f]):
    for i in faces[f]:state[i]^=np.uint8(1)
  if sweep>=burn:
   j=sweep-burn;x,y,c=measurements(state,faces,coeff,planes,scales)
   values[j,:,:4]=x;values[j,:,4]=y;counts[j]=c
   if j<len(snaps):snaps[j]=state
 return values,counts,state,snaps

@njit(cache=True)
def numerator_methods(states,faces,coeff,planes,scales,choices,method):
 result=np.zeros((len(states),coeff.shape[0]));M=len(faces)
 for j in range(len(states)):
  state=states[j]
  if method==2:
   counts=np.zeros(3,np.int64)
   for f in range(M):
    if is_flippable(state,faces[f]):counts[f//(M//3)]+=1
   for m in range(coeff.shape[0]):result[j,m]=scales[m]*counts[planes[m]]
  else:
   for slot in range(M if method==0 else 1):
    f=slot if method==0 else choices[j]
    if is_flippable(state,faces[f]):
     for m in range(coeff.shape[0]):
      z=0j
      for i in faces[f]:z+=coeff[m,i]*(1.-2.*state[i])
      result[j,m]+=(z.real*z.real+z.imag*z.imag)*(.5 if method==0 else M*.5)
 return result

G=build_geometry(args.L);coeff,planes,scales,modes=coefficients(args.L);initial=initial_ice(args.L).ravel()
if args.micro:
 data=np.load(P.parent.parent/'ice-estimator-calibration/exact_data.npz');states=((data['states'][:,None]>>np.arange(24))&1).astype(np.uint8)
 assert args.L==2
 vals=[]
 for x in states:
  v,z,c=measurements(x,G.plaquette_links,coeff,planes,scales);vals.append(np.column_stack((v,z)))
 vals=np.array(vals)
 assert np.max(abs(vals[:,:,2].mean(0)-5/12))<1e-12
 assert np.max(abs(vals[:,:,3].mean(0)/vals[:,:,2].mean(0)-8/5))<1e-12
 assert np.max(abs(vals[:,:,4].mean(0)/vals[:,:,2].mean(0)-16/5))<1e-12
 # Literal signed changes and LO on every L2 state/move and all modes.
 updates=0
 for x in states:
  O=coeff@(x.astype(float)-.5);sumdelta=np.zeros(len(modes),complex)
  for links in G.plaquette_links:
   if is_flippable(x,links):
    y=x.copy();y[links]^=1;actual=coeff@(y.astype(float)-.5)-O;pred=coeff[:,links]@(1.-2*x[links]);assert max(abs(actual-pred))<1e-13;sumdelta+=actual;updates+=len(modes)
  _,sq,_=measurements(x,G.plaquette_links,coeff,planes,scales);assert max(abs(sq-abs(sumdelta)**2))<1e-12
 chain(initial,G.plaquette_links,coeff,planes,scales,2,4,1400000)
 choices=np.zeros(len(states),np.int64)
 for method in range(3):numerator_methods(states,G.plaquette_links,coeff,planes,scales,choices,method)
 direct=numerator_methods(states,G.plaquette_links,coeff,planes,scales,choices,0);count=numerator_methods(states,G.plaquette_links,coeff,planes,scales,choices,2);assert max(abs(direct-count).ravel())<1e-12
 out={'micro':True,'states':864,'signed_update_cases':updates,'exact_S':5/12,'exact_mu1':8/5,'exact_mu2':16/5,'all_mode_checks':True}
else:
 vals=[];counts=[];snaps=[];seeds=[]
 for r in range(32):
  seed=1400000+args.L*100000+args.burn*100+r;seeds.append(seed)
  v,c,last,ss=chain(initial,G.plaquette_links,coeff,planes,scales,args.burn,256,seed);vals.append(v);counts.append(c);snaps.append(ss)
  cube=last.reshape(args.L,args.L,args.L,3);assert np.all(vertex_degrees(cube)==3) and electric_flux(cube)==(0,0,0)
 vals=np.array(vals);snapshots=np.concatenate(snaps);rng=np.random.default_rng(991000+args.L*1000+args.burn);choices=rng.integers(len(G.plaquette_links),size=len(snapshots))
 signed_cases=0
 for state in snapshots[:16]:
  O=coeff@(state.astype(float)-.5);summed=np.zeros(len(modes),complex)
  for links in G.plaquette_links:
   if is_flippable(state,links):
    flipped=state.copy();flipped[links]^=1
    actual=coeff@(flipped.astype(float)-.5)-O
    predicted=coeff[:,links]@(1.-2*state[links])
    assert np.max(abs(actual-predicted))<1e-12
    summed+=actual;signed_cases+=len(modes)
  _,sq,_=measurements(state,G.plaquette_links,coeff,planes,scales)
  assert np.max(abs(sq-abs(summed)**2))<1e-10
 timing={};numerators={} 
 for method in range(3):
  z=numerator_methods(snapshots,G.plaquette_links,coeff,planes,scales,choices,method)
  t=time.monotonic()
  for _ in range(20):z=numerator_methods(snapshots,G.plaquette_links,coeff,planes,scales,choices,method)
  timing[str(method)]=(time.monotonic()-t)/(20*len(snapshots));numerators[str(method)]=z
 assert np.max(abs(numerators['0']-numerators['2']))<1e-12
 name=f'L{args.L}_b{args.burn}';np.savez_compressed(P/(name+'.npz'),values=vals,counts=np.array(counts),snapshots=snapshots,one_face_numerator=numerators['1'],all_face_numerator=numerators['0'])
 out={'L':args.L,'burn':args.burn,'modes':modes,'seeds':seeds,'chains':32,'samples_per_chain':256,'timing_seconds_per_snapshot':timing,'signed_visited_move_cases':signed_cases,'snapshot_count':len(snapshots),'raw_file':name+'.npz'}
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin'else 1024);assert 0<rss<384
out.update(seconds=time.monotonic()-start,rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());print(json.dumps(out,indent=2,allow_nan=False))
