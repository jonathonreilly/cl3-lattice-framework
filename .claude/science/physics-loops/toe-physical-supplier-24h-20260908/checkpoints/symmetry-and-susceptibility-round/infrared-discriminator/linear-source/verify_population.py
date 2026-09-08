from producer import *
import runpy,contextlib,io
from scipy import sparse
from scipy.sparse.linalg import eigsh
import kernel as scalar
import population_kernel as pk
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path('/private/tmp/toe-24h-probes-20260908/detuned-energy-moment/check.py')
g=prod.build_geometry(2);cr,ci,mo=prod.transverse_coefficients(2,(1,));co=cr[:1].copy();checks={}
def ck(k,v):
 if not bool(v):raise AssertionError(k)
 checks[k]=True
maxerr=0.;count=0
for i,x in enumerate(d['states']):
 s=np.array([(x>>j)&1 for j in range(24)],dtype=np.uint8);o=pk.literal_O(s,co);nf=prod.count_flippable(s,g.plaquette_links)
 for xi in GRID:
  ck0=pk.branch_value(nf,pk.source_norm(o),-.05,xi,abs(xi)*np.sqrt(8)/2,24)
  maxerr=max(maxerr,abs(ck0-scalar.branch(nf,o[0],.95,xi,8)))
 for f in range(24):
  if prod.is_flippable(s,g.plaquette_links[f]):
   ss=s.copy();oo=o.copy();nn=pk.flip_cached(ss,nf,oo,f,co,g.plaquette_links,g.affected_plaquettes,g.affected_counts)
   y,F,b=scalar.step(x,o[0],f,0.,d['faces'],co[0],nf,.95,.01,8)
   if sum(int(z)<<j for j,z in enumerate(ss))!=y or nn!=d['nf'][d['lookup'][y]]:raise AssertionError('elementary flip/count')
   maxerr=max(maxerr,abs(oo[0]-F));count+=1
ck('all_elementary_6912',count==6912 and maxerr<1e-12)
# Actual resampling cache alignment, all descendant slots.
ss=np.array([[(x>>j)&1 for j in range(24)] for x in d['states'][:128]],dtype=np.uint8);ct=np.array([prod.count_flippable(s,g.plaquette_links) for s in ss]);ob=np.array([pk.literal_O(s,co) for s in ss]);anc=np.arange(128,dtype=np.int32)
a,b,c,e,ess=pk.resample(ss,ct,ob,anc,np.linspace(-2,2,128))
ck('resampling_alignment',np.array_equal(a,ss[e]) and np.array_equal(b,ct[e]) and np.array_equal(c,ob[e]))
A,N=d['A'],d['N'];I=sparse.eye(864);r0=np.zeros(864);r0[0]=1;RK=I-(N-A)/24
for _ in range(20*24):r0=RK@r0
rows=[]
for xi in GRID:
 F=d['O'][0];H=.95*N-A+sparse.diags(xi*F);G=I-(H-abs(xi)*np.sqrt(8)/2*I)/24;E=eigsh(H,k=1,which='SA',tol=1e-13,v0=1+np.arange(864)/864)[0][0];r=r0.copy();window=[]
 for j in range(80):
  for _ in range(24):r=G@r;r/=sum(r)
  if j>=40:window.append(float(r@(-.05*d['nf']+xi*F)))
 rows.append(dict(xi=xi,E=float(E),window=float(np.mean(window)),error=float(np.mean(window)-E)))
ck('tilted_window_energy',max(abs(x['error']) for x in rows)<1e-10)
errs={x['xi']:x['error'] for x in rows};curv={str(h):-(errs[h]+errs[-h]-2*errs[0])/h**2 for h in [.01,.005,.0025]};ck('tilted_window_curvature',max(abs(x) for x in curv.values())<1e-5)
print(json.dumps(dict(checks=checks,elementary_pairs=count,max_residual=maxerr,windows=rows,curvature_window_errors=curv,seconds=time.monotonic()-start),indent=2))
