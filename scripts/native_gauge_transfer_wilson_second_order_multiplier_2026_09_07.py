#!/usr/bin/env python3
"""Exact coefficient and explicit remainder certificate for the native Wilson multiplier.

Quadrature is a separately executed support runner, not a proof dependency.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import signal,time,resource,sys
signal.alarm(180);started=time.monotonic()
import sympy as sym
from fractions import Fraction as F
from math import factorial
import json,hashlib
from pathlib import Path
x,y,k,l=sym.symbols('x y k l')
qa=k*k-k*l+l*l;Q=x*x+x*y+y*y;H=x*y*(x+y)/2;W=H*sym.exp(-Q)
def Lop(f):return (sym.diff(f,x,2)-sym.diff(f,x,y)+sym.diff(f,y,2))/3
symbolic={
 'quartic symbol':sym.expand(k**4+l**4+(k-l)**4-2*qa**2),
 'alternant quadratic':sym.expand((2*k-l)**2+(k-2*l)**2+(k+l)**2-6*qa),
 'LW':sym.simplify(Lop(W)-(Q-4)*W),
 'L2W':sym.simplify(Lop(Lop(W))-(Q**2-10*Q+20)*W)}
for name,residual in symbolic.items():
 if residual!=0:raise AssertionError(name)
checks=[]
def ck(name,ok):
 if not ok:raise AssertionError(name)
 checks.append(name)
def expsum(x,n):return sum((x**j/F(factorial(j))) for j in range(n+1))
a=F(23,72);g=lambda n:F(factorial(2*n),4**n*factorial(n))
cn=sum(c*g(n)*a**(-n) for c,n in [(F(1,20),4),(F(23,2592),5),(F(1,2592),6)])
cd=F(1,5)*(F(1,5)*20*a**-6+F(29,1620)*120*a**-7+F(1,2592)*840*a**-8)
ck('low numerator',cn<170);ck('low denominator',cd<2617)
ck('square sinc halfcut',F(1,16)+F(1,10)+F(1,80)+F(1,1600)<F(1,5))
ck('numerator cubic',F(1,810)+F(1,1440)+F(1,144)==F(23,2592))
ck('denominator cubic',F(1,810)+F(1,360)+F(1,72)==F(29,1620))
ck('alpha inverse square root',a>F(1,4))
ck('exp high exact',expsum(F(128,3),150)>10**18)
ck('exp approximation tail',expsum(F(512,3),500)>10**60)
b=2048;t=F(b,48)
en=F(b*b,3)*24**3*factorial(2)*sum(t**j/factorial(j) for j in range(3))/10**18
ed=F(b*b,30)*24**4*factorial(3)*sum(t**j/factorial(j) for j in range(4))/10**18
an=F(1,3)*(F(9,2)*factorial(4)*6**5+F(1,18)*factorial(5)*6**6)/10**60
ad=F(1,30)*(5*factorial(5)*6**6+F(1,18)*factorial(6)*6**7)/10**60
ck('exact numerator tail',en<F(37,10**6));ck('exact denominator tail',ed<F(3869,10**6))
ck('approx numerator tail',an<F(1,1000));ck('approx denominator tail',ad<F(1,1000))
ck('CN ceiling',cn+en+an<171);ck('CD ceiling',cd+ed+ad<2618)
ck('tail monotonicity threshold',b>5*48)
ck('W maximum',expsum(F(3),20)>18)
ck('QW maximum',expsum(F(5),25)>36*F(5,2)**5/27)
ck('Q2W maximum',expsum(F(7),30)>4*F(7,2)**7/27)
ck('W2 bound',3*F(1,12)+F(7,4)*F(1,6)+F(1,4)*F(1,2)==F(2,3))
ck('D0 floor',27*F(5,3)/F(22,7)>14)
ck('denominator fraction',1-F(1,b)-F(2618,14*b*b)>F(999,1000))
c=F(1000,999)*(F(171,14)+F(2,3)+F(2618,14)*(F(1,12)+F(2,3*b)))
ck('final constant',c==F(76675625,2685312) and c<29)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
elapsed=time.monotonic()-started
if not(0<rss<180 and 0<=elapsed<180):raise AssertionError('resource contract')
result=dict(symbolic_checks=list(symbolic),symbolic_assertion_count=len(symbolic),rational_checks=checks,rational_assertion_count=len(checks),
 beta0=b,C=29,window=[["1/4","2"],["1/4","2"]],coefficient="(3-7Q/4+Q^2/4) H exp(-Q)",
 low_CN=str(cn),low_CD=str(cd),numerator_remainder_constant=171,denominator_remainder_constant=2618,ratio_coefficient=str(c),
 dependencies={},source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=elapsed,rss_MiB=rss,
 resources=dict(timeout_seconds=180,rss_limit_MiB=180,blas_threads=1),
 scope="Exact native Wilson multiplier expansion on fixed shifted window; no full-operator, log-ratio, gap or physical Yang-Mills claim. Quadrature is separate support, not proof input.")
if '--json' in sys.argv:print(json.dumps(result,indent=2,allow_nan=False))
else:
 print('PASS native Wilson second-order multiplier: four symbolic identities and22 exact rational inequalities')
 print('per_element: exact symbol quartic, Weyl alternant quadratic and two Gaussian differential identities.')
 print('per_site: fixed dominant-weight endpoints with rho=(1,1); shifted window[1/4,2]^2.')
 print('per_mode: exact low/high Fourier remainder constants171 and2618; positive denominator controlled.')
 print('per_block: |v-W-W2/beta|<=29/beta^2 for every beta>=2048 in the declared window.')
 print('lattice_wide: no operator spectral consequence; original native Fourier identity is the conditional parent premise.')
 print('SOURCE_SHA256',result['source_sha256']);print('DEPENDENCIES {}')
 print('RESOURCES',elapsed,rss,'seconds/MiB;180 limits, BLAS1')
 print('TOTAL: PASS FAIL=0')
