#!/usr/bin/env python3
"""Exact scalar and polynomial certificate for provisional Wilson W2 bounds."""
import sympy as s
from fractions import Fraction as F
from math import factorial,isqrt
import json,hashlib
from pathlib import Path
checks=[]
def ck(name,ok):
 if not ok:raise AssertionError(name)
 checks.append(name)
x,y,k,l=s.symbols('x y k l');a=k*k-k*l+l*l;Q=x*x+x*y+y*y;H=x*y*(x+y)/2;W=H*s.exp(-Q)
L=lambda f:(s.diff(f,x,2)-s.diff(f,x,y)+s.diff(f,y,2))/3
ck('quartic symbol',s.expand(k**4+l**4+(k-l)**4-2*a*a)==0)
ck('alternant quadratic',s.expand((2*k-l)**2+(k-2*l)**2+(k+l)**2-6*a)==0)
ck('LW',s.simplify(L(W)-(Q-4)*W)==0)
ck('L2W',s.simplify(L(L(W))-(Q*Q-10*Q+20)*W)==0)
ck('W2',s.simplify(W+s.Rational(3,4)*L(W)+L(L(W))/4-(3-s.Rational(7,4)*Q+Q*Q/4)*W)==0)
ck('denominator relative coefficient',F(180,36)-F(12,2)==-1)
ck('cosine remainder enlargement',F(1,810)<F(1,90))
ck('sinc product coefficient',(F(1,120)+F(1,72))*F(9,4)==F(1,20))
ck('squared sinc coefficient',F(1,16)+F(1,10)+F(1,40*16)+F(1,400*16**2)<F(1,5))
ck('low exponential domination',F(1,3)-F(1,576)>F(1,4))
ck('low numerator cubic',F(1,90)+F(1,11520)+F(1,144)<1)
ck('low denominator cubic',F(1,90)+F(1,2880)+F(1,72)<1)
ck('global torus constant',F(4,90)>F(1,24))
ck('polar constant',2*F(22,7)/F(5,3)<4)
CN=12*(600*(factorial(2)*24**3+factorial(4)*24**5)+3*(factorial(3)*24**4+factorial(5)*24**6)+(factorial(4)*24**5+factorial(6)*24**7))
CD=32*(600*factorial(5)*24**6+3*factorial(6)*24**7+factorial(7)*24**8)
beta0=isqrt(4*CD)+1;C=2*CN+960+256*CD
ck('CN',CN==41831183351808);ck('CD',CD==18510264831836160)
ck('beta0',beta0==272104869 and beta0**2>4*CD and beta0>=4)
ck('ratio constant',C==4738711459316761536)
# Exact low-domain r2 coefficient uses v=a/(4beta), |r|<=a²/(20beta²).
# No sampled inequality is used as an all-domain proof.
print(json.dumps(dict(checks=checks,CN=CN,CD=CD,beta0=beta0,C=C,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2))
