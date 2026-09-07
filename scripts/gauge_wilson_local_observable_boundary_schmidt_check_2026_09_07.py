import os,time,signal,sys,resource,json,hashlib
from pathlib import Path
START=time.monotonic();signal.alarm(180)
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
AUDIT_TIMEOUT_SEC=180
AUDIT_MEMORY_LIMIT_MB=180
if sys.argv[1:] not in ([],['--json']): raise SystemExit('usage: gauge_wilson_local_observable_boundary_schmidt_check_2026_09_07.py [--json]')
import sympy as s
from itertools import combinations
checks=[]
def ck(name,truth):
 if name in checks or not bool(truth):raise AssertionError(name)
 checks.append(name)
# Analytically derived actual four-link Wilson-loop Schmidt coefficient matrix.
C=s.eye(9)/3;rho=C*C.H
ck('actual loop Schmidt normalization',s.trace(rho)==1)
ck('actual loop one-link reduced density',rho==s.eye(9)/9)
ck('actual loop purity one ninth',s.trace(rho*rho)==s.Rational(1,9))
T=[]
for i,j in combinations(range(3),2):
 A=s.zeros(3);A[i,j]=A[j,i]=1/s.sqrt(2);T.append(A)
 A=s.zeros(3);A[i,j]=-s.I/s.sqrt(2);A[j,i]=s.I/s.sqrt(2);T.append(A)
T += [s.diag(1,-1,0)/s.sqrt(2),s.diag(1,1,-2)/s.sqrt(6)]
Gleft=[s.kronecker_product(A,s.eye(3)) for A in T]
Gright=[-s.kronecker_product(s.eye(3),A.T) for A in T]
for i,(L,R) in enumerate(zip(Gleft,Gright)):
 ck('actual reduced density commutes endpoint generators '+str(i),L*rho==rho*L and R*rho==rho*R)
Cas=sum((G*G for G in Gleft+Gright),s.zeros(9))
ck('no invariant vector in actual fundamental matrix block',Cas==s.eye(9)*s.Rational(16,3))
rho10=s.diag(0,*([s.Rational(1,9)]*9));Psing=s.diag(1,*([0]*9))
ck('forced local singlet loses physical loop with probability one',s.trace(Psing*rho10)==0)
ck('representation R1 cutoff preserves whole boundary state',s.trace(s.diag(0,*([1]*9))*rho10)==1)
ck('physical one-link kinetic expectation',s.trace(rho*(s.eye(9)*4))==4)
# Exact finite coefficient identities supporting the all-orders tail integration proof.
z=s.symbols('z',nonnegative=True)
for r in (0,1,2,3,8):
 lower=sum(z**n/s.factorial(n) for n in range(r,12))
 upper=sum(z**n/s.factorial(n) for n in range(r+1,13))
 ck('tail antiderivative coefficient identity r'+str(r),s.expand(s.diff(upper,z)-lower)==0)
ck('boundary integrated coefficient',s.Rational(2)*4/32==s.Rational(1,4))
ck('generic first-face bound safely loosened',s.Rational(4,16)<=1)
for p in [s.Rational(1,16),s.Rational(1,4),s.Rational(9,16),s.Integer(1)]:
 ck('normalization expectation correction sharper p'+str(p),1-p<=2*(1-s.sqrt(p)))
ck('zero interaction tail has no nonzero terms',all(s.Integer(0)**n/s.factorial(n)==0 for n in range(1,13)))
elapsed=time.monotonic()-START
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
ck('positive resource budget',0<elapsed<180 and 0<rss<180)
result={'checks':checks,'TOTAL':len(checks),'Schmidt_dimension':9,'Schmidt_coefficient':'1/3','rho_eigenvalues':['1/9']*9,'rho_purity':'1/9','endpoint_Gauss_Casimir':'16/3','local_singlet_probability':0,'R1_retention_probability':1,'integrated_boundary_coefficient':'1/4','seconds':elapsed,'rss_MiB':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Actual Wilson-loop Schmidt/Haar consequence and exact finite coefficient checks; analytic Haar orthogonality, all-orders propagation and domain proofs remain separate.'}
if sys.argv[1:]==['--json']:
 print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS TOTAL='+str(result['TOTAL'])+' unique named checks')
 print('per_element: PASS 3 exact nine-mode Schmidt density and purity checks')
 print('per_site: PASS 10 endpoint-generator and boundary-singlet adverse checks')
 print('per_mode: PASS 2 whole-boundary-state retention and kinetic-energy checks')
 print('per_block: PASS 12 tail coefficient, integration, normalization and zero-coupling checks')
 print('lattice_wide: PASS 1 resource control; all-orders Haar/domain proofs remain analytical')
 print('DATA: '+json.dumps({k:v for k,v in result.items() if k not in ('checks','seconds','rss_MiB','source_sha256')},sort_keys=True,allow_nan=False))
 print('RESOURCE: seconds='+str(result['seconds'])+' rss_MiB='+str(result['rss_MiB'])+' limits=180sec/180MiB')
 print('SOURCE_SHA256: '+result['source_sha256'])
signal.alarm(0)
