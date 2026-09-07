#!/usr/bin/env python3
"""Exact SU(3) two-source cubic cancellation support; analytic bounds separate."""
import time,signal,resource,sys,os,json,hashlib,math
from pathlib import Path
START=time.monotonic();signal.alarm(180)
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1';os.environ['MKL_NUM_THREADS']='1'
import sympy as s
I=s.I;r=s.sqrt(2)
T=[s.Matrix([[0,1,0],[1,0,0],[0,0,0]])/r,s.Matrix([[0,-I,0],[I,0,0],[0,0,0]])/r,s.diag(1,-1,0)/r,s.Matrix([[0,0,1],[0,0,0],[1,0,0]])/r,s.Matrix([[0,0,-I],[0,0,0],[I,0,0]])/r,s.Matrix([[0,0,0],[0,0,1],[0,1,0]])/r,s.Matrix([[0,0,0],[0,0,-I],[0,I,0]])/r,s.diag(1,1,-2)/s.sqrt(6)]
checks=[]
def check(n,b):
 if not b:raise AssertionError(n)
 checks.append(n)
check('trace orthonormal generators',all(s.trace(a*b)==int(i==j) for i,a in enumerate(T) for j,b in enumerate(T)))
f={}
for a,A in enumerate(T):
 for b,B in enumerate(T):
  for c,C in enumerate(T):
   z=s.simplify(s.trace((A*B-B*A)*C)/I)
   if z:f[a,b,c]=z
check('actual f squared norm48',sum(z*z for z in f.values())==48)
check('actual f fully alternating',all(f.get((b,a,c),0)==-z and f.get((a,c,b),0)==-z for (a,b,c),z in f.items()))
check('real Wilson cubic is f over2',all(s.simplify(s.re(-I*s.trace(A*B*C))-f.get((a,b,c),0)/2)==0 for a,A in enumerate(T) for b,B in enumerate(T) for c,C in enumerate(T)))
x=s.symbols('x0:8',real=True);y=s.symbols('y0:8',real=True)
a,b,c,d,e,g=s.symbols('a b c d e g',real=True)
means=[[a*x[k]+b*y[k] for k in range(8)],[c*x[k]+d*y[k] for k in range(8)],[e*x[k]+g*y[k] for k in range(8)]]
poly=s.expand(sum(z*means[0][i]*means[1][j]*means[2][k] for (i,j,k),z in f.items()))
check('two arbitrary retained source vectors cancel',poly==0)
one=s.expand(sum(z*x[i]*x[j]*x[k] for (i,j,k),z in f.items()))
check('one retained source vector cancels',one==0)
check('zero retained source means cancel',sum(z*0 for z in f.values())==0)
for pair in [(0,1),(0,2),(1,2)]:
 free=next(k for k in range(3) if k not in pair)
 vals=[]
 for k in range(8):
  total=0
  for j in range(8):
   ids=[0]*3;ids[free]=k;ids[pair[0]]=ids[pair[1]]=j;total+=f.get(tuple(ids),0)
  vals.append(s.simplify(total))
 check('isotropic covariance contraction '+str(pair),all(z==0 for z in vals))
three=f[0,1,2]
check('three independent source countercase nonzero',three==s.sqrt(2))
check('three source direct ordered cubic nonzero',s.simplify(-s.re(-I*s.trace(T[0]*T[1]*T[2]))/3+s.sqrt(2)/6)==0)
seconds=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not(math.isfinite(seconds) and math.isfinite(rss) and seconds<180 and rss<180):raise RuntimeError('180second/180MiB resource bound failed')
out=dict(status='PASS',per_tensor_checks=4,per_mean_checks=3,per_covariance_checks=3,per_adverse_checks=2,TOTAL=len(checks),checks=checks,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),f_nonzero_entries={str(k):str(v) for k,v in f.items()},f_squared_norm=48,two_source_polynomial=str(poly),one_source_polynomial=str(one),three_source_f=str(three),three_source_Wilson_cubic='-sqrt(2)/6',seconds=seconds,rss_MiB=rss,scope='Actual SU3 tensor and two-source conditional cubic algebra; cube geometry and weighted nonlinear HS proof are separate analytical imports.')
assert out['TOTAL']==sum(out[k] for k in ['per_tensor_checks','per_mean_checks','per_covariance_checks','per_adverse_checks'])
if '--json' in sys.argv:print(json.dumps(out,indent=2,allow_nan=False))
else:
 print('PASS: 12 exact SU(3) tensor, mean, covariance and adverse checks.')
 print('N5: Two arbitrary retained color vectors give identically zero conditional cubic.')
 print('N5: Zero and one retained source controls also vanish.')
 print('N5: Three independent retained vectors give f=sqrt(2), pinning the two-source hypothesis.')
 print('N5: This finite certificate does not prove nonlinear chart, tail or spectral bounds.')
 print('N5: No finite-beta onset, physical coupling selection or all-source-count theorem.')
 print('source_sha256='+out['source_sha256'])
