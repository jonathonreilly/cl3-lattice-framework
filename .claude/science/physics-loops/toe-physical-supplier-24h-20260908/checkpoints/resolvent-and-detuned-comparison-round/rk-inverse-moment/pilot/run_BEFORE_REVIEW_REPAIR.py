import os,sys,time,signal,resource,json,argparse,hashlib
from pathlib import Path
from fractions import Fraction
p=Path(__file__).resolve().parent
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True
ap=argparse.ArgumentParser();ap.add_argument('--micro',action='store_true');ap.add_argument('--L',type=int,choices=[2,4],default=4);ap.add_argument('--burn',type=int,choices=[32,128],default=128);args=ap.parse_args();signal.alarm(30 if args.micro else 120);start=time.monotonic()
sys.path[:0]=[str(p.parent.parent/'detuned-energy-moment'),'/private/tmp/toe-physical-supplier-24h-20260908/scripts']
import numpy as np
import producer_original as prod
from kernel import collect,endpoint,observe,generate_lags
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice,vertex_degrees,electric_flux
L=4 if args.micro else args.L;M=3*L**3;g=prod.build_geometry(L);cr,ci,modes=prod.transverse_coefficients(L,(1,2));coeff=cr+1j*ci;initial=initial_ice(L).ravel();alphas=np.array([.25,.5,1.]);qs=M/(M+alphas);caps=[];bounds=[]
for a,q in zip(alphas,qs):
 k=int(np.ceil(np.log(a*.001)/np.log(q)))-1;aa=Fraction(str(a));qq=Fraction(M)/(M+aa)
 while qq**(k+1)/aa>Fraction(1,1000):k+=1
 while k>0 and qq**k/aa<=Fraction(1,1000):k-=1
 caps.append(k);bounds.append(float(qq**(k+1)/aa))
caps=np.array(caps,dtype=np.int64);n=128 if args.micro else 256;reps=1 if args.micro else 32
orig=[];products=[];lagsall=[];tails=[];seeds=[];snap=[]
for rep in range(reps):
 cid=900 if args.micro else (([2,4].index(L)*2+[32,128].index(args.burn))*32+rep)
 rng=np.random.default_rng(400000000+cid);U=rng.random((n,3));lags=generate_lags(U,qs)
 if not np.all(lags>=0):raise AssertionError('geometric support')
 o,y,states=collect(initial,g.plaquette_links,coeff,lags,caps,8 if args.micro else args.burn,cid)
 if not all(np.all(vertex_degrees(x)==3) and electric_flux(x)==(0,0,0) for x in states.reshape((-1,L,L,L,3))):raise AssertionError('source component postconditions')
 if not np.all(y[lags>caps]==0):raise AssertionError('clipped contribution')
 orig.append(o);products.append(y);lagsall.append(lags);tails.append(lags>caps);seeds.append(cid);snap.append(states)
out={'L':L,'burn':8 if args.micro else args.burn,'chains':reps,'origins_per_chain':n,'chain_ids':seeds,'alphas':alphas.tolist(),'q':qs.tolist(),'Kmax':caps.tolist(),'exact_rational_tail_comparison':True,'tail_bounds':bounds,'modes':modes,'clipped_counts':np.sum(tails,axis=(0,1)).tolist()}
if args.micro:
 state=snap[0][0];signed=0
 for x in snap[0][:8]:
  old=observe(x,coeff)
  for f,face in enumerate(g.plaquette_links):
   if prod.is_flippable(x,face):
    y=x.copy();y[face]^=1;actual=observe(y,coeff)-old;predicted=coeff[:,face]@(1.-2*x[face])
    if np.max(abs(actual-predicted))>1e-12:raise AssertionError('signed complex flip')
    signed+=len(coeff)
 if not np.array_equal(endpoint(state,g.plaquette_links,0,999),state):raise AssertionError('zero-step support')
 endpoint(state,g.plaquette_links,10000,999);observe(state,coeff)
 t=time.monotonic()
 for _ in range(20):endpoint(state,g.plaquette_links,10000,999)
 stepcost=(time.monotonic()-t)/200000
 t=time.monotonic()
 for _ in range(2000):observe(state,coeff)
 obscost=(time.monotonic()-t)/2000
 out.update(mode='micro_not_physics',signed_complex_cases=signed,proposal_seconds=stepcost,source_call_seconds=obscost,expected_proposal_cost_32chain_cell=8192*(8*M)*stepcost,expected_source_cost_32chain_cell=8192*4*obscost,hypothetical_16chain_cost=.5*(8192*(8*M)*stepcost+8192*4*obscost))
else:
 name=f'L{L}_b{args.burn}';np.savez_compressed(p/(name+'.npz'),origins=orig,products=products,lags=lagsall,clipped=tails);out['raw_file']=name+'.npz'
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);elapsed=time.monotonic()-start
if not 0<rss<384 or elapsed>(30 if args.micro else 120):raise RuntimeError('resource envelope')
out.update(seconds=elapsed,rss_mib=rss,run_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),kernel_sha256=hashlib.sha256((p/'kernel.py').read_bytes()).hexdigest());print(json.dumps(out,indent=2,allow_nan=False))
