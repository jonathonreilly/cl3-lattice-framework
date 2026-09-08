from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
ncheck=0
def req(x,m):
 global ncheck
 ncheck+=1
 if not x:raise RuntimeError(m)
def comps(n,l):
 if not l:
  if not n:yield()
  return
 for i in range(1,n+1):
  for t in comps(n-i,l-1):yield(i,)+t
f={};s={}
for n in range(1,15):
 value=F(0)
 for l in range(2,n+1):
  for c in comps(n,l):
   term=2*f[c[0]];p=c[0]
   for i in c[1:]:p+=i;term*=22*p*s[i]
   value+=term/factorial(l)
 for l in range(n):
  for c in comps(n-1,l):
   term=F(11);p=0
   for i in c:p+=i;term*=22*(1+p)*s[i]
   value+=term/factorial(l)
 f[n]=value;s[n]=4*value;req(value>0,'finite majorant')
m=154;rho=min(F(1),F(1,24*m*max(1,sum(s.values()))))
req(2*m*3*rho*sum(s.values())<=F(1,4),'analytic Lie disk')
req(5+1-4-9==-7,'old failure');req(13+1-4-9==1,'root vanishing');req(14+1-4-9==2,'native improved');req(6-4==2,'slow comparison')
# Exact two-sector witness: lower excited-sector terms cannot be discarded globally,
# yet they have no action on an initial ice vector. No dynamics oracle is used.
import sympy as sp
P=sp.diag(1,1,0,0);Q=sp.eye(4)-P;D=2*Q
X0=sp.zeros(4);X0[0,1]=X0[1,0]=1
X1=sp.zeros(4);X1[2,3]=X1[3,2]=1
Z0=sp.diag(1,-1,0,0);Z1=sp.diag(0,0,1,-1)
z=sp.Rational(1,10)
K=z*X1+z*z*(3*P+Z1)+z**3*Z1+z**4*(X0+5*P+X1)+z**5*X1+z**6*Z0
L=z**4*X0+z**6*Z0
req(D*K==K*D and D*L==L*D,'charge conservation');scalar=3*z*z+5*z**4
req((K-L)*P==scalar*P,'ice scalar equality');req(K-L!=scalar*sp.eye(4),'no global equality')
for n in range(1,7):req((K-scalar*sp.eye(4))**n*P==L**n*P,'restricted powers')
req((K-L)*Q!=sp.zeros(4),'fast excited-sector adverse')
result=dict(checks=ncheck,order=14,rho=str(rho),s={j:str(v) for j,v in s.items()},powers=dict(old=-7,order13=1,order14=2,slow=2),scope='Exact finite recursion and restricted-algebra controls; not simulation or proof by numerics of the natural-time theorem.')
Path(__file__).with_name('RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(ncheck)
