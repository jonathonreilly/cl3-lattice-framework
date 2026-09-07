import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import time,signal,resource,sys,json,hashlib,math
from fractions import Fraction as F
signal.alarm(180);start=time.monotonic()
import sympy as s
checks=[]
def ck(name,v):
 if name in checks or not bool(v):raise AssertionError(name)
 checks.append(name)
x,y,z1,z2=s.symbols('x y z1 z2',real=True);v=s.Matrix([x,y]);z=s.Matrix([z1,z2]);rho=s.Matrix([1,1]);s1=s.Matrix([[-1,0],[1,1]]);s2=s.Matrix([[1,1],[0,-1]])
group=[(s.eye(2),1),(s1,-1),(s2,-1),(s1*s2,1),(s2*s1,1),(s1*s2*s1,-1)]
ck('six distinct Weyl matrices',len({tuple(w) for w,sgn in group})==6)
a=z1*z1-z1*z2+z2*z2;Delta=(2*z1-z2)*(z1-2*z2)*(z1+z2)
for j,(w,sgn) in enumerate(group):
 ck('determinant sign '+str(j),w.det()==sgn)
 zz=w.T*z;ck('dual quadratic invariance '+str(j),s.expand(zz[0]**2-zz[0]*zz[1]+zz[1]**2-a)==0)
 for k in (0,1):
  mat=s.hessian(s.expand(s.Rational(4,3)*a-zz[k]**2),(z1,z2))/2
  ck('coordinate square domination '+str(j)+' '+str(k),mat[0,0]>=0 and mat[1,1]>=0 and mat.det()>=0)
A=sum(sgn*s.exp(-s.I*(z.T*w*v)[0]) for w,sgn in group)
for name,sub in [('xwall',{x:0}),('ywall',{y:0}),('thirdwall',{y:-x})]:ck(name,s.simplify(A.subs(sub))==0)
for n in range(4):
 term=s.expand(sum(sgn*(-s.I*(z.T*w*rho)[0])**n/s.factorial(n) for w,sgn in group))
 ck('small endpoint coefficient '+str(n),s.simplify(term-(-s.I*Delta if n==3 else 0))==0)
ck('divided alternant constant',F(16)**2/3<100)
ck('root squared sum',s.expand((2*z1-z2)**2+(z1-2*z2)**2+(z1+z2)**2-6*a)==0)
ck('symmetrized cubic integrand normalization',s.simplify(s.I*Delta*term/6-Delta**2/6)==0)
ck('missing symmetrization factor rejected',s.simplify(s.I*Delta*term-Delta**2/6)!=0)
ck('wrong cubic sign rejected',s.expand(-s.I*Delta-s.I*Delta)!=0)
alpha=F(23,72);cn=F(1,2)*(F(1,20)*math.factorial(5)/alpha**6+F(23,2592)*math.factorial(6)/alpha**7+F(1,2592)*math.factorial(7)/alpha**8)
def expsum(q,n):
 term=F(1);total=term
 for j in range(1,n+1):term*=q/j;total+=term
 return total
ck('exact tail exponential',expsum(F(128,3),60)>10**18)
ck('Gaussian tail exponential',expsum(F(512,3),180)>10**60)
b=F(2048);t=b/48
et=b*b*F(1,2)*24**4*math.factorial(3)*(1+t+t*t/2+t**3/6)/10**18
at=F(1,2)*(F(9,2)*math.factorial(5)*6**6+F(1,18)*math.factorial(6)*6**7)/10**60
ck('divided exact high tail',et<F(3,50));ck('divided approximation high tail',at<F(1,1000));ck('divided numerator ceiling',cn+et+at<21201)
ck('exp one elementary floor',expsum(F(1),4)>F(8,3));ck('global correction bound',3+F(21,32)+F(9,64)<4)
C=F(1000,999)*(F(21201,14)+4+F(2618,14)*(1+F(4,2048)))
ck('final wall uniform ceiling',C<1710)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not 0<rss<180 or time.monotonic()-start>=180:raise AssertionError('resources')
print(json.dumps({'scope':'Exact algebra/arithmetic supporting divided Weyl alternant and global shifted-label one-link multiplier, not multilink identification','checks':checks,'low_divided_numerator':str(cn),'exact_tail':str(et),'approx_tail':str(at),'ratio_coefficient':str(C),'beta0':2048,'C':1710,'source_sha256':hashlib.sha256(open(__file__,'rb').read()).hexdigest(),'seconds':time.monotonic()-start,'rss_MiB':rss},indent=2,allow_nan=False))
