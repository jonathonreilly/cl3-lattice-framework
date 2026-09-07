import time,signal,resource,sys,json,hashlib
from pathlib import Path
start=time.monotonic();signal.alarm(180)
import sympy as s
I=s.I;r=s.sqrt(2)
T=[s.Matrix([[0,1,0],[1,0,0],[0,0,0]])/r,s.Matrix([[0,-I,0],[I,0,0],[0,0,0]])/r,s.diag(1,-1,0)/r,s.Matrix([[0,0,1],[0,0,0],[1,0,0]])/r,s.Matrix([[0,0,-I],[0,0,0],[I,0,0]])/r,s.Matrix([[0,0,0],[0,0,1],[0,1,0]])/r,s.Matrix([[0,0,0],[0,0,-I],[0,I,0]])/r,s.diag(1,1,-2)/s.sqrt(6)]
checks=[]
def check(n,b):
 assert b,n;checks.append(n)
check('trace orthonormal',all(s.trace(a*b)==int(i==j) for i,a in enumerate(T) for j,b in enumerate(T)))
f={}
for i,a in enumerate(T):
 for j,b in enumerate(T):
  comm=a*b-b*a
  for k,c in enumerate(T):
   v=s.simplify(s.trace(comm*c)/I)
   if v:f[i,j,k]=v
check('f squared sum48',sum(v*v for v in f.values())==48)
check('f alternating',all(f.get((j,i,k),0)==-v and f.get((i,k,j),0)==-v for (i,j,k),v in f.items()))
check('quartic adjacent contraction64/3',s.simplify(sum(s.trace(a*a*b*b) for a in T for b in T))==s.Rational(64,3))
check('quartic crossed contraction-8/3',s.simplify(sum(s.trace(a*b*a*b) for a in T for b in T))==-s.Rational(8,3))
check('quartic nested contraction64/3',s.simplify(sum(s.trace(a*b*b*a) for a in T for b in T))==s.Rational(64,3))
A,B,C=T[:3];coef=s.re(-I*s.trace(A*B*C));check('ordered cubic direct matrix',s.simplify(-coef/3+f[0,1,2]/6)==0)
check('repeated cubic vanishes',all(s.re(-I*s.trace(a*a*b))==0 for a in T for b in T))
# Independent explicit epsilon Taylor product for a noncommuting four-factor plaquette.
e=s.symbols('e',real=True)
def exp4(A):return sum(((I*e)**n/s.factorial(n)*A**n for n in range(5)),s.zeros(3))
word=exp4(A)*exp4(B)*exp4(-C)*exp4(-A)
coeff3=s.expand(s.re(s.trace(word))).coeff(e,3)
# First/last A cancel cyclically in the trace; the remaining two-factor cubic is zero.
check('four factor ordered cubic cancellation',s.simplify(coeff3)==0)
# Haar Jacobian roots: log j(X)= -sum_positive_roots alpha(X)^2/12+O(X^4).
x,y=s.symbols('x y',real=True);roots=[x-y,2*x+y,x+2*y]
check('Haar quadratic trace factor',s.expand(sum(a*a for a in roots)/12-(x*x+y*y+(x+y)**2)/4)==0)
out=dict(status='PASS',TOTAL=len(checks),checks=checks,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-start,rss_MiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024))
assert out['seconds']<180 and out['rss_MiB']<180
print(json.dumps(out,indent=2))
