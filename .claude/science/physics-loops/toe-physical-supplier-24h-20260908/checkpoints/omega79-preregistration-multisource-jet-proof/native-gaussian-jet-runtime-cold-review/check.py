# Independent abstract h0=0 determinant fixture; not a native vacuum model.
import pathlib,importlib.util,json
from fractions import Fraction as F
from math import factorial
p=pathlib.Path('/private/tmp/toe-24h-probes-20260908/native-gaussian-jet-runtime-design/core.py');sp=importlib.util.spec_from_file_location('jet',p);C=importlib.util.module_from_spec(sp);sp.loader.exec_module(C)
queries=[]
def D(j,a,b):queries.append(('D',j));return C.point(int(j==0 and a==b))
def B(j,a,b):queries.append(('B',j));return C.point(int(j==0 and a==b==0))
# det(I-P+P exp(-tV))=cosh(2t). Compute square root via scalar squaring.
z=[F(1)]
for n in range(1,11):z.append(((F(2**n,factorial(n))if n%2==0 else F(0))-sum(z[k]*z[n-k]for k in range(1,n)))/2)
ev=[];ell,counters=C.logjet(10,D,B,lambda s,d:ev.append((s,d)),first_order=7);accepted={n:C.point(((-1)**n*factorial(n)*z[n]).numerator,((-1)**n*factorial(n)*z[n]).denominator)for n in range(7)};got=C.high_moments(ell,accepted);checks=0
for n in range(7,11):v=(-1)**n*factorial(n)*z[n];assert F(got[n][0][0],C.S)<=v<=F(got[n][0][1],C.S);checks+=1
assert all(d['order']>=7 for s,d in ev if s=='log_coefficient');assert all(j<=8 for _,j in queries);checks+=2
# Independent combinatorial upper counts, no actual physical support construction.
A=lambda n:2*n*n
M=lambda n,m:A(n)if m==1 else 2*(n-m+1)*(n-m+2)
assert sum(2*A(k)*M(n-k,m-1)for m in range(2,11)for n in range(m,11)for k in range(1,n-m+2))==141240;checks+=1
assert counters['complex_products']<=141240+2642 and counters['operator_products']<=2280;checks+=1
print(json.dumps({'checks':checks,'native_calls':0,'abstract_degenerate_h0_only':True}))
