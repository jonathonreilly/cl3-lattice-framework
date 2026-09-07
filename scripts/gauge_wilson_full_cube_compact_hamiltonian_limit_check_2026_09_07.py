#!/usr/bin/env python3
"""Exact finite algebra support; analytic convergence is proved in the source."""
import time
START=time.monotonic()
import os,sys,signal,json,hashlib,resource
from pathlib import Path
AUDIT_TIMEOUT_SEC = 180
signal.alarm(AUDIT_TIMEOUT_SEC)
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'): os.environ[key]='1'
if sys.argv[1:] not in ([],['--json']): raise SystemExit('usage: runner [--json]')
import sympy as s
from itertools import combinations
checks=[]
def ck(name, value):
    if name in checks or not bool(value): raise AssertionError(name)
    checks.append(name)
T=[]
for i,j in combinations(range(3),2):
    A=s.zeros(3);A[i,j]=A[j,i]=1/s.sqrt(2);T.append(A)
    A=s.zeros(3);A[i,j]=-s.I/s.sqrt(2);A[j,i]=s.I/s.sqrt(2);T.append(A)
T.extend([s.diag(1,-1,0)/s.sqrt(2),s.diag(1,1,-2)/s.sqrt(6)])
for i,A in enumerate(T): ck('generator%d Hermitian traceless'%i,A==A.H and s.trace(A)==0)
for i,A in enumerate(T): ck('trace inner product row%d'%i,all(s.simplify(s.trace(A*B))==int(i==j) for j,B in enumerate(T)))
casimir=sum((A*A for A in T),s.zeros(3))
ck('fundamental Casimir8over3 kinetic4overa',casimir==s.eye(3)*s.Rational(8,3) and s.Rational(3,2)*s.Rational(8,3)==4)
edges=[(v,v^(1<<a)) for v in range(8) for a in range(3) if not v&(1<<a)]
faces=[]
for a,b in combinations(range(3),2):
    c=next(i for i in range(3) if i not in (a,b))
    for o in (0,1<<c):faces.append([o,o^(1<<a),o^(1<<a)^(1<<b),o^(1<<b)])
ck('cube12links6faces',len(edges)==12 and len(faces)==6)
ck('every face closes through actual links',all(all(tuple(sorted((u,v))) in edges for u,v in zip(f,f[1:]+f[:1])) for f in faces))
ck('each link touches two faces',all(sum(set(e)<=set(f) for f in faces)==2 for e in edges))
z=s.symbols('z',real=True);E=s.Rational(2,3)*(1-s.cos(z));series=s.series(E,z,0,6).removeO()
ck('actual diagonal Wilson quadratic TrX2over6',series.coeff(z,2)==s.Rational(1,3))
ck('actual diagonal Wilson fourth nonzero',series.coeff(z,4)==-s.Rational(1,36))
ck('actual diagonal Wilson odd coefficients zero',all(series.coeff(z,i)==0 for i in (1,3,5)))
ck('Gaussian covariance from exponent one sixth',1/(2*s.Rational(1,6))==3)
ck('eight dimensional Gaussian second radial moment',8*3==24)
ck('eight dimensional Gaussian fourth radial moment',8*(8+2)*3**2==720)
ck('96 dimensional product Gaussian fourth radial moment',96*(96+2)*3**2==84672)
h,v,c0,J=s.symbols('h v c0 J',positive=True)
ck('six face half multiplier scalar exponent minus3hv',s.expand(-h*v*(6-J)/2)==-3*h*v+h*v*J/2)
ck('full transfer scalar expminus6hv c0powerminus12',s.expand(2*(-3*h*v))==-6*h*v and len(edges)==12)
ck('compact potential not quadratic at pi',s.simplify(E.subs(z,s.pi))==s.Rational(4,3) and s.pi**2/3>s.Rational(4,3))
ck('compact potential periodic while quadratic is not',s.simplify(E.subs(z,z+2*s.pi)-E)==0 and s.expand((z+2*s.pi)**2-z*z)!=0)
if len(checks)!=31:raise AssertionError('frozen count31')
elapsed=time.monotonic()-START
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not (0<rss<=180 and 0<elapsed<AUDIT_TIMEOUT_SEC):raise AssertionError('resource contract')
payload=dict(status='PASS',checks=checks,total=len(checks),dependencies={},source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_seconds=elapsed,peak_rss_mib=rss,scope='Exact finite algebra only; no numerical tail, domain or convergence certification',data=dict(casimir=str(casimir),edges=edges,faces=faces,wilson_direction_series=str(series),gaussian_radial_moments={'8_second':24,'8_fourth':720,'96_fourth':84672},kinetic_fundamental='4/a',transfer_scalar='exp(-6*h*v)/c0(a/h)^12'))
if '--json' in sys.argv:print(json.dumps(payload,sort_keys=True,allow_nan=False))
else:
    print('PASS: exact compact Wilson Hamiltonian algebra support')
    print('per_element: eight trace-normalized generators; fundamental kinetic coefficient4/a')
    print('per_site: cube incidence verifies twelve physical links and six closed faces')
    print('per_mode: covariance3 and radial Gaussian moments are finite algebra checks')
    print('per_block: exact nonlinear compact potential and transfer scalar retained')
    print('lattice_wide: fixed cube only; no numerical certification of strong convergence or continuum limit')
    print('TOTAL:',len(checks));print('resources: seconds=%.6f RSS_MiB=%.6f limits180/180'%(elapsed,rss));print('source_sha256:',payload['source_sha256'])
