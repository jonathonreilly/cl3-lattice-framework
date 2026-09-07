import time,signal,os
AUDIT_TIMEOUT_SEC=180
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sympy as s
import json,hashlib,resource,sys
from pathlib import Path
checks=[]
def ck(name,v):
 assert name not in checks and bool(v),name
 checks.append(name)
u=s.symbols('u',real=True);k=s.symbols('k',positive=True);A=s.symbols('A',real=True);r=s.symbols('r',positive=True)
mean=lambda f:s.simplify(s.integrate(f,(u,-s.pi,s.pi))/(2*s.pi))
p=1+A*s.cos(u)
ck('harmonic mass',mean(p)==1);ck('harmonic concentration',mean(p*p)==1+A*A/2)
ck('harmonic energy',mean(s.diff(p,u)**2)==A*A/2)
bump=k*(1+s.cos(u))
ck('supported mass',mean(bump)/k==1);ck('supported concentration',s.simplify(mean(bump*bump)/k-3*k/2)==0)
ck('supported energy',s.simplify(mean((k*s.diff(bump,u))**2)/k-k**3/2)==0)
ck('supported second derivative L2',s.simplify(mean((k*k*s.diff(bump,u,2))**2)/k-k**5/2)==0)
ck('boundary value zero',bump.subs(u,s.pi)==0);ck('boundary derivative zero',s.diff(bump,u).subs(u,s.pi)==0)
low=(r-1)/r;high=4*r*r/27
ck('matching value',low.subs(r,s.Rational(3,2))==high.subs(r,s.Rational(3,2)))
ck('matching first derivative',s.diff(low,r).subs(r,s.Rational(3,2))==s.diff(high,r).subs(r,s.Rational(3,2)))
ck('high concentration stiffness',s.simplify((k*k/3).subs(k,2*r/3)-high)==0)
ck('harmonic beyond threshold infeasible',1-s.sqrt(2)<0)
ck('two bump derivative penalty',mean(s.diff(1+A*s.cos(2*u),u)**2)==4*mean(s.diff(p,u)**2))
ck('two bump same concentration',mean((1+A*s.cos(2*u))**2)==mean(p*p))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
assert 0<rss<180 and time.monotonic()-start<180
payload=dict(checks=checks,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-start,rss_MiB=rss,scope='Symbolic profile integrals and discriminators only; global minimizer proof is analytical and no primitive-derived variational law is claimed.')


if len(sys.argv)==2 and sys.argv[1]=='--json':
 print(json.dumps(payload,indent=2,allow_nan=False))
elif len(sys.argv)==1:
 print('PASS:',len(checks),'exact assertions')
 for level in ('per_element','per_site','per_mode','per_block','lattice_wide'):
  print(level+': conditional mathematical result; supplied inputs remain explicit')
 print('source_sha256:',payload['source_sha256'])
 print('TOTAL: PASS='+str(len(checks))+' FAIL=0')
else:
 raise SystemExit('usage: runner [--json]')
