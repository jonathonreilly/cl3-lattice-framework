# Full schema fixture is synthetic; h0=0 abstract determinant, not native data.
import core as C,worker as W
from fractions import Fraction as F
from math import factorial
import json,copy
z=[F(1)]
for n in range(1,7):z.append(((F(2**n,factorial(n))if n%2==0 else F(0))-sum(z[k]*z[n-k]for k in range(1,n)))/2)
def arr(x):return [list(x[0]),list(x[1])]
D={str(j):[[arr(C.point(int(j==0 and a==b)))for b in range(2)]for a in range(2)]for j in range(9)};B={str(j):[[arr(C.point(int(j==0 and a==b==0)))for b in range(2)]for a in range(2)]for j in range(9)}
m={}
for n,x in enumerate(z):x*=(-1)**n*factorial(n);m[str(n)]=arr(C.point(x.numerator,x.denominator))
p={'first_order':7,'grid_bits':256,'units':'dimensionless_h1','classes':{k:{'D':D,'B':B,'accepted_m':m}for k in ['P','O']}};ev=[];r=W.compute(p,lambda s,d:ev.append((s,d)));assert len(r['rows'])==2;assert all(d['order']>=7 for s,d in ev if s in ['new_moment_raw','log_coefficient']);assert all('A'in d and 'Q'in d for s,d in ev if s=='operator_order');checks=3
for fn in [lambda p:p.update(first_order=True),lambda p:p['classes']['P']['accepted_m'].update({'0':arr(C.point(2))}),lambda p:p['classes']['P']['D']['0'][0][0].__setitem__(0,[1,0]),lambda p:p['classes']['P']['B']['0'][0][0].__setitem__(0,[True,C.S])]:
 q=copy.deepcopy(p);fn(q)
 try:W.validate(q)
 except ValueError:checks+=1
 else:raise AssertionError('invalid schema accepted')
print(json.dumps({'status':'PASS','checks':checks,'events':len(ev),'native_values':0,'fixture':'abstract nonnative two identical classes'}))
