import os,sys,json,hashlib,itertools,time,signal
from pathlib import Path
for v in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[v]='1'
os.environ['NUMBA_CACHE_DIR']='/private/tmp/toe-24h-probes-20260908/complex-source-l4-root-review/numba-cache'
sys.path[:0]=['/private/tmp/toe-physical-supplier-24h-20260908/scripts','/private/tmp/toe-24h-probes-20260908/complex-source-l4','/private/tmp/toe-24h-probes-20260908/detuned-energy-moment']
import numpy as np
import kernel,producer_original as prod
signal.alarm(180);t=time.monotonic();checks=0
L=4;vol=L**3
coords=list(itertools.product(range(L),repeat=3))
index=lambda r,a:3*((r[0]%L)*L*L+(r[1]%L)*L+r[2]%L)+a
modes=[(a,b) for a in range(3) for b in range(3) if a!=b]
faces=[]
for r in coords:
 for a,b in ((0,1),(0,2),(1,2)):
  ra=list(r);ra[a]+=1;rb=list(r);rb[b]+=1
  faces.append([index(r,a),index(ra,b),index(rb,a),index(r,b)])
g=prod.build_geometry(L)
# Compare geometry as unordered geometric faces; preserve producer ordering for actual function.
if sorted(map(sorted,faces))!=sorted(map(sorted,g.plaquette_links.tolist())):raise ValueError('geometry')
def nf(state):
 bits=state[g.plaquette_links]
 return int(np.sum((bits[:,0]==bits[:,2])&(bits[:,1]==bits[:,3])&(bits[:,0]!=bits[:,1])))
rng=np.random.default_rng(5500001)
state=np.array([r[a]%2 for r in coords for a in range(3)],dtype=np.uint8)
cr,ci,labels=prod.transverse_coefficients(L,(1,2))
for h in (1,2):
 c=np.zeros((6,3*vol),complex)
 for m,(a,b) in enumerate(modes):
  for r in coords:c[m,index(r,b)]=(-1)**sum(r)*np.exp(2j*np.pi*h*r[a]/L)/np.sqrt(vol)
 coeff=np.vstack((c.real,c.imag));sl=slice(6*(h-1),6*h)
 if np.max(abs(c-(cr[sl]+1j*ci[sl])))>1e-14:raise ValueError('literal coefficient')
 for step in range(35):
  bits=state[g.plaquette_links];legal=np.flatnonzero((bits[:,0]==bits[:,2])&(bits[:,1]==bits[:,3])&(bits[:,0]!=bits[:,1]))
  f=int(rng.choice(legal));before=state.copy();observed=kernel.literal_O(state,coeff);count=nf(state)
  after_count=kernel.flip_cached(state,count,observed,f,coeff,g.plaquette_links,g.affected_plaquettes,g.affected_counts)
  manual=before.copy();manual[g.plaquette_links[f]]^=1
  direct=c@(manual.astype(float)-.5)
  if not np.array_equal(state,manual) or after_count!=nf(manual) or np.max(abs(observed[:6]+1j*observed[6:]-direct))>1e-13:raise ValueError('actual flip')
  x=float(np.vdot(direct,direct).real)
  if abs(kernel.source_norm(observed)-x)>1e-13:raise ValueError('norm')
  for V in (1.,.95):
   for lam in (-.02,-.01,.0,.01,.02):
    shift=96*abs(lam);b=kernel.branch_value(after_count,x,V-1,lam,shift,192)
    diag=b-after_count/192
    if b<1-1e-13 or abs(diag-(1-(V*after_count+lam*x-shift)/192))>1e-13:raise ValueError('G diagonal')
    if abs(b*(1/(192*b))-1/192)>1e-15:raise ValueError('G offdiagonal')
  checks+=1
out={'status':'PASS','independent_coordinate_coefficients':2304,'actual_legal_flips':checks,'seconds':time.monotonic()-t,'kernel_sha256':hashlib.sha256(Path(kernel.__file__).read_bytes()).hexdigest(),'scope':'actual functions, literal coordinates and binary updates; no stochastic accuracy assertion'}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
