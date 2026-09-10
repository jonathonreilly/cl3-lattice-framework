"""Source-only saved component arithmetic. No file or native-data loader."""
from fractions import Fraction as F
from math import comb
Q=1<<192
RAD4={'cminus':F(544,45*4**52),'mu':F(128,3*4**52),'nu':F(256,4**52)}
RAD5={'cminus':F(85,6*5**52),'mu':F(50,5**52),'nu':F(300,5**52)}
def require(ok,msg):
 if not ok: raise ValueError(msg)
def box(v):
 require(type(v)in(tuple,list) and len(v)==2,'box shape')
 require(all(type(x)is F for x in v),'exact Fraction operands')
 require(all(max(abs(x.numerator).bit_length(),x.denominator.bit_length())<=32768 for x in v),'stored bit cap')
 require(v[0]<=v[1],'ordered box');return tuple(v)
def rounded(v):
 a,b=box(v);return F((a*Q).__floor__(),Q),F((b*Q).__ceil__(),Q)
def add(a,b):return rounded((a[0]+b[0],a[1]+b[1]))
def product(a,b):
 vals=[x*y for x in a for y in b];return rounded((min(vals),max(vals)))
def moment(n):
 # Independent coefficient convolution, executed only in a future certificate.
 require(type(n)is int and 0<=n<=41,'moment index')
 return F(sum(comb(n,a)*comb(n-a,b)*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b) for a in range(n+1)for b in range(n-a+1)))
def tail(kind):
 k={'cminus':0,'mu':1,'nu':2}[kind]
 return sum(((-1)**n*moment(n+k)/((2*n+1)*8**(2*n+1))for n in range(40)),F(0)),F(12**(40+k),81*8**81)
def low(kind,first=None):
 e=F(1,2**64);a0=F(17,60)
 if kind=='mu':return e-a0*e**3/3,e
 if kind=='nu':return 6*e-e**3/3,6*e-e**3/3+a0*e**5/5
 t,A=map(box,first);require(e<t[0]<=t[1]<2*e,'first node bracket')
 return e*A[0],e*(A[1]+3*t[1])
def finish(middle,lo,high,pi,radius):
 pl,pu=box(pi);require(3<pl<=pu<4,'pi bounds')
 t,rem=high;require(rem>=0,'positive tail')
 return product(add(add(box(middle),(t,t+rem)),(lo[0]-radius,lo[1]+radius)),(2/pu,2/pl))
def machin():
 def atan(q,n):
  v=sum((F((-1)**j,(2*j+1)*q**(2*j+1))for j in range(n)),F(0));e=F(1,(2*n+1)*q**(2*n+1));return v,v+e
 a,b=atan(5,32),atan(239,10);return 16*a[0]-4*b[1],16*a[1]-4*b[0]
def recertify(kind,panels,saved,pi,first=None,emit=lambda x:None):
 require(box(pi)==machin(),'independent Machin binding');require(kind in RAD5,'kind');require(len(panels)==67,'panel census')
 total=(F(0),F(0))
 for j,p in enumerate(panels):
  emit({'stage':'panel','index':j,'input':p})
  require(type(p['panel'])is int and p['panel']==j-64,'panel order')
  total=add(total,box(p['value']));require(total==box(p['cumulative']),'saved cumulative')
 hi=tail(kind);lo=low(kind,first)
 emit({'stage':'components','middle':total,'low':lo,'high':hi,'old_radius':RAD4[kind],'new_radius':RAD5[kind]})
 require(box(saved['middle'])==total and box(saved['low'])==lo,'middle/low binding')
 require(tuple(saved['high'])==hi and saved['radius']==RAD4[kind],'tail/old radius binding')
 old=finish(total,lo,hi,pi,RAD4[kind]);require(old==box(saved['interval']),'original interval arithmetic')
 new=finish(total,lo,hi,pi,RAD5[kind]);emit({'stage':'new_interval','interval':new})
 require(old[0]<=new[0]<=new[1]<=old[1],'nested recertification')
 return {'interval':new,'width':new[1]-new[0],'target':F(2,10**28),'target_met':new[1]-new[0]<=F(2,10**28),'original_interval':old,'oracle_calls':0,'node_integrands_recomputed':0}
def load_actual(*args,**kwargs):raise RuntimeError('NOT_READY: authenticated accepted-source adapter, review and new protocol required')
