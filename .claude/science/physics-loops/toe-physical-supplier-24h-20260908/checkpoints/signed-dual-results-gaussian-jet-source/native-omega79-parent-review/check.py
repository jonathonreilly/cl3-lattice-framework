from pathlib import Path
from fractions import Fraction as F
import sys,types,json
P=Path('/private/tmp/toe-24h-probes-20260908/native-omega79-catalog-supplier-design');count=0
for name in ['interval','pi','compute','loader']:
 m=types.ModuleType(name);m.__file__=str(P/(name+'.py'));sys.modules[name]=m;exec(compile(Path(m.__file__).read_bytes(),m.__file__,'exec'),m.__dict__)
c=sys.modules['compute'];loader=sys.modules['loader']
def check(v):
 global count
 assert v;count+=1
for x in [1,4,9]:
 moments={k:F(x)**k for k in range(46)}
 for r in [3,4]:
  for t in [F(1,3),F(2),F(7)]:
   q,w,p=c.node_value({'t_interval':(t,t),'A_interval':(1/(x+t*t),1/(x+t*t)),'weight_interval':(F(1,7),F(1,7))},r,moments)
   exact=F(x)**(r+1)/(x+t*t);check(q[0]<=exact<=q[1] and w[0]<=exact/7<=w[1]);check(p[0]<=t**(2*r+2)/7<=p[1])
  z=c.tails(r,moments);sq={1:1,4:2,9:3}[x];v=F(sq,8)
  # Independent alternating arctan series: integral from8 to infinity.
  a=sum(((-1)**k*v**(2*k+1)/F(2*k+1)for k in range(42)),F(0));b=a+v**85/F(85);factor=F(x)**r*sq
  check(z['high_partial']<=factor*a<=factor*b<=z['high_partial']+z['high_remainder'])
  e=F(1,2**64);v=e/sq;lo=sum(((-1)**k*v**(2*k+1)/F(2*k+1)for k in range(6)),F(0));hi=lo+v**13/F(13)
  if F(1,x)<=F(17,60):check(z['low_interval'][0]<=factor*lo<=factor*hi<=z['low_interval'][1])
for n in [0,3,43,46,True,44.0]:
 try:c.moment(n)
 except ValueError:count+=1
 else:raise AssertionError('new moment index guard')
for bad in ['1/0','01','+1','1/2/3','1.0']:
 try:loader.scalar(bad)
 except (ValueError,ZeroDivisionError):count+=1
 else:raise AssertionError('canonical scalar guard')
print(json.dumps({'status':'PASS','checks':count,'native_moments_evaluated':0,'catalog_loads':0,'synthetic_point_masses':[1,4,9]}))
