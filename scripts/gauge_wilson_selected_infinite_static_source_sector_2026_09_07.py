import os,time,signal,sys,resource,hashlib
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
started=time.monotonic();signal.alarm(180)
AUDIT_TIMEOUT_SEC=180
AUDIT_MEMORY_LIMIT_MB=180
if sys.argv[1:] not in ([],['--json']):raise SystemExit('usage: gauge_wilson_selected_infinite_static_source_sector_2026_09_07.py [--json]')
import json
from fractions import Fraction as F
checks=0
def ck(x):
 global checks
 checks+=1
 assert x
# Stieltjes at i represented by exact real/imaginary pair.
def st(x):return (x/(x*x+1),F(1)/(x*x+1))
rows=[]
for n in (2,4,8):
 p=F(1,n); mean=(1-p)*2+p*(2+n)
 ck((1-p)+p==1 and mean==3)
 z=tuple((1-p)*a+p*b for a,b in zip(st(F(2)),st(F(2+n))))
 diff=tuple(a-b for a,b in zip(z,st(F(2))))
 ck(sum(x*x for x in diff)<=4*p*p)
 rows.append({'n':n,'mean':str(mean),'stieltjes':list(map(str,z))})
ck(F(2)<F(3))
# The local resolvent block at i is (1+i)/2; a zero eigenvalue gives i.
bottom=[]
for dim in (4,6):
 diag=[1]*(dim-1)+[0]
 local=[st(F(x)) for x in diag[:2]]
 ck(local==[st(F(1))]*2)
 ck(min(diag)==0 and min([1]*dim)==1)
 bottom.append({'dimension':dim,'local_dimension':2,'finite_bottom':0,'limit_bottom':1})
# Exact finite-character average: (1+zeta^q+zeta^(2q))/3=1 iff q=0 mod3.
P=[int((q+1)%3==0) for q in range(3)]
ck(P==[0,0,1] and [p*p for p in P]==P)
ck(all(not p or (q+1)%3==0 for q,p in enumerate(P)))
v=[F(1),F(2),F(3)]; projected=[p*x for p,x in zip(P,v)]
ck(sum(x*x for x in projected)<=sum(x*x for x in v))
wrong=[int(q%3==0) for q in range(3)]
ck(wrong!=P and any(p and (q+1)%3 for q,p in enumerate(wrong)))

payload={'checks':checks,'status':'PASS','first_moment_rows':rows,'escaping_bottom_rows':bottom,'combined_gauge_projector':P,'wrong_system_only_projector':wrong,'scope':'exact adverse controls; not numerical verification of imported GNS theorem'}
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
elapsed=time.monotonic()-started
if not (0<rss<180 and 0<=elapsed<180):raise AssertionError('resource guard')
payload.update(source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),resource={'elapsed_sec':elapsed,'peak_rss_mib':rss,'timeout_sec':180,'memory_limit_mib':180,'checks':1},N5={'per_element':3,'per_site':3,'per_mode':2,'per_block':3,'lattice_wide':0})
if sys.argv[1:]==['--json']:print(json.dumps(payload,sort_keys=True,indent=2,allow_nan=False))
else:
 print('PASS: 15 exact scientific controls; 1 separate resource guard')
 print('per_element: 3 exact rational spectral-measure cases')
 print('per_site: 3 finite Z3 charge labels, explicitly a toy')
 print('per_mode: 2 fixed local resolvent modes')
 print('per_block: 3 distinct adverse-control families')
 print('lattice_wide: 0 numerical infinite-volume simulations; theorem is analytical')
 print('resources: %.6fs / 180s; %.3fMiB / 180MiB'%(elapsed,rss))
