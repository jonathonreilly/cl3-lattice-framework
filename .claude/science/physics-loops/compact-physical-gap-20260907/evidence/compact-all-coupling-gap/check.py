import os,time,signal
START=time.monotonic();signal.alarm(180)
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sympy as s,json,math,hashlib,resource,sys
checks=[]
def ck(n,b):
 if n in checks or not bool(b):raise AssertionError(n)
 checks.append(n)
# Fixed degree12 Taylor polynomial; every omitted term is positive.
exp4lower=sum(s.Rational(4)**j/s.factorial(j) for j in range(13))
ck('rational Taylor lower bound exp4 exceeds54',exp4lower>54)
first=s.Rational(18,54);f2=s.Rational(192,54**2);ratio=s.Rational(4,3)*s.Rational(5,4)**6/54
ck('fundamental contribution conservative one third',first==s.Rational(1,3))
ck('tail successive ratio below one tenth',ratio<s.Rational(1,10))
tail=f2/(1-s.Rational(1,10));total=first+tail
ck('absolute nonconstant heat series below one half',total<s.Rational(1,2))
ck('tail below 74 thousandths',tail<s.Rational(74,1000))
p,q,m=s.symbols('p q m',integer=True,nonnegative=True)
E=p*p+q*q+p*q+3*(p+q)
ck('energy lower bound all m at least2 identity',s.expand(E-4*(p+q)-(s.Rational(3,4)*(p+q)**2-(p+q)+(p-q)**2/4))==0)
ck('dimension arithmetic mean bound identity',s.expand((p+q+2)**2/4-(p+1)*(q+1)-(p-q)**2/4)==0)
ck('m tail exact first term',s.Rational(3)*4**6/(64*54**2)==f2)
lo=s.Rational(1,2)**12;hi=s.Rational(3,2)**12
ck('product kernel ratio3 power12',hi/lo==3**12)
ck('weighted Poincare ratio square', (hi/lo)**-2==s.Rational(1,3**24))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
ck('positive resource budget',0<rss<180 and time.monotonic()-START<180)
print(json.dumps(dict(checks=checks,TOTAL=len(checks),Taylor_degree=12,exp4_rational_lower=str(exp4lower),first_bound=str(first),tail_first=str(f2),tail_ratio_bound=str(ratio),tail_bound=str(tail),total_nonconstant_bound=str(total),half_margin=str(s.Rational(1,2)-total),product_kernel_lower=str(lo),product_kernel_upper=str(hi),ground_ratio_prefactor=str(hi/lo),gap_prefactor=str(s.Rational(16,3**24)),seconds=time.monotonic()-START,rss_MiB=rss,source_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(),scope='Exact rational scalar checks; all-label tail monotonicity and operator-domain proof are analytic, not sampled.'),indent=2))
