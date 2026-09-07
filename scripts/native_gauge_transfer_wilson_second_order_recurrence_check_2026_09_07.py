import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import signal,time,resource,sys,math,json,hashlib,gc
from fractions import Fraction as F
signal.alarm(180);start=time.monotonic();AUDIT_TIMEOUT_SEC=180
import numpy as np
from scipy.sparse import coo_matrix,eye
from scipy.sparse.linalg import expm_multiply
checks=0
def ck(v):
 global checks
 checks+=1
 if not v:raise AssertionError(checks)
def tail_cert(beta,R,theta):
 term=F(1);cs=term
 for n in range(1,21):term*=theta**2/F((2*n-1)*(2*n));cs+=term
 first=term*theta**2/F(41*42);cs+=first/(1-theta**2/F(41*42))
 A=theta*R-F(2*beta,3)*(cs-1);ck(A>0)
 term=F(1);lower=term
 for n in range(1,101):term*=A/n;lower+=term
 ck(lower>2*10**30)
 return {'rational_theta':str(theta),'cosh_terms_through_power':40,'cosh_geometric_remainder':True,'exponential_lower_terms':100,'certified_kernel_tail_upper':'1e-30'}
moves=[(1,0),(-1,1),(0,-1),(0,1),(1,-1),(-1,0)]
grid=[(.5,.5),(1.,1.),(1.5,.5),(.5,1.5),(2.,1.),(2.,2.)];cases=[]
for beta,R,theta in [(128,128,F(1)),(256,192,F(9,10)),(512,256,F(2,3))]:
 cert=tail_cert(beta,R,theta)
 rr=[];cc=[]
 for p in range(R):
  for q in range(R):
   j=p*R+q
   for dp,dq in moves:
    a=p+dp;b=q+dq
    if 0<=a<R and 0<=b<R:rr.append(a*R+b);cc.append(j)
 J=coo_matrix((np.full(len(rr),1/6),(rr,cc)),shape=(R*R,R*R)).tocsr();del rr,cc;gc.collect()
 ck((J-J.T).nnz==0);ck(np.all(J.data==1/6));ck(J[:,0].nnz==2)
 A=J-eye(R*R,format='csr');v=np.zeros(R*R);v[0]=1
 k=expm_multiply(beta*A,v,traceA=-beta*R*R)
 ck(np.all(np.isfinite(k)));ck(k.min()>=-1e-14);ck(0<k.sum()<=1+1e-12);ck(k[0]>0)
 rows=[]
 for xn,yn in grid:
  p=math.floor(xn*math.sqrt(beta))-1;q=math.floor(yn*math.sqrt(beta))-1;ck(0<=p<R and 0<=q<R)
  x=(p+1)/math.sqrt(beta);y=(q+1)/math.sqrt(beta);Q=x*x+x*y+y*y;W=x*y*(x+y)/2*math.exp(-Q);W2=(3-7*Q/4+Q*Q/4)*W
  val=beta**-1.5*k[p*R+q]/k[0]
  # Certified entry-tail with floating denominator scale; NOT a total numerical error bound.
  ratio_tail_scale=beta**-1.5*1e-30/k[0]*(1+k[p*R+q]/k[0])
  rows.append({'p':p,'q':q,'x':x,'y':y,'kernel_entry':float(k[p*R+q]),'kernel_return':float(k[0]),'v':float(val),'W':W,'W2':W2,'leading_residual':float(val-W),'second_order_residual':float(val-W-W2/beta),'scaled_second_order_residual':float(beta**2*(val-W-W2/beta)),'conditional_truncation_ratio_scale':float(ratio_tail_scale)})
 opt=math.asinh(3*R/(2*beta));optlog=math.log(2)-opt*R+(2*beta/3)*(math.cosh(opt)-1)
 cases.append({'beta':beta,'R':R,'dimension':R*R,'J_nnz':J.nnz,'survival_mass':float(k.sum()),'return_scaled_beta4':float(beta**4*k[0]),'analytic_certificate':cert,'optimized_tail_log_numeric_only':optlog,'rows':rows})
 del J,A,v,k;gc.collect()
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);ck(0<rss<180);ck(time.monotonic()-start<180)
payload={'scope':'Independent killed six-neighbor recurrence falsifier; analytic truncation certificate but floating expm not interval-certified; beta values below refined theorem threshold','checks':checks,'cases':cases,'source_sha256':hashlib.sha256(open(__file__,'rb').read()).hexdigest(),'seconds':time.monotonic()-start,'rss_MiB':rss,'dependencies':{},'resources':{'timeout_seconds':180,'rss_limit_MiB':180,'blas_threads':1}}
if '--json' in sys.argv:print(json.dumps(payload,indent=2,allow_nan=False))
else:
 print('PASS native killed-recurrence falsifier:47 actual checks,3 frozen cases,18 rows')
 for case in cases:
  print('BETA',case['beta'],'R',case['R'],'return_scaled_beta4',case['return_scaled_beta4'])
  for row in case['rows']:print('GRID',row['p'],row['q'],'beta2_residual',row['scaled_second_order_residual'])
 print('per_element: actual six-neighbor1/6 killed walk, native coefficients without Gaussian fitting')
 print('per_site:18 frozen grid labels at their actual shifted coordinates')
 print('per_mode: three finite sparse squares with analytic first-exit kernel tail<1e-30')
 print('per_block: beta128/256/512 below2048 theorem threshold; floating exponential not interval-certified')
 print('lattice_wide: checked and not executed -- no finite-packet spectrum or physical Wilson/gap claim')
 print('SOURCE_SHA256',payload['source_sha256'])
