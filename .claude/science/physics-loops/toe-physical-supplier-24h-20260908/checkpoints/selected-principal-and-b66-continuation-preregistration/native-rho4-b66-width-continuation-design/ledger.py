"""Pure width formulas only. No loader, CLI, moment evaluator or integral center."""
from fractions import Fraction as F
from caps import guard,tree,pole
A0=F(17,60);EPS=F(1,2**64);N=40
TARGETS=(F(2,10**28),F(2,10**27))
def box(x):
 if not isinstance(x,(tuple,list)) or len(x)!=2 or any(type(y)is not F for y in x) or x[0]>x[1]:raise ValueError('Fraction interval')
 return tuple(x)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[1],-x[0]
def mul(x,y):
 z=[a*b for a in x for b in y];return min(z),max(z)
def inv(x):
 if x[0]<=0<=x[1]:raise ValueError('denominator does not separate')
 return F(1)/x[1],F(1)/x[0]
def const(x):return x,x
def mr(x):return (x[0]+x[1])/2,(x[1]-x[0])/2
def product_radius(c,x):
 cm,cr=mr(c);xm,xr=mr(x)
 return max(abs(c[0]),abs(c[1]))*xr+cr*abs(xm)
def node(s,t,at,ass,aps,w):
 if type(s)is not F or not F(1,128)<=s<=16:raise ValueError('exact fixed pole domain')
 t,at,ass,aps,w=map(box,(t,at,ass,aps,w))
 if not 0<t[0]<=t[1]<=8 or not 0<w[0]<=w[1]:raise ValueError('node/weight positivity')
 a=const(s*s);b=mul(t,t);d=add(b,neg(a));di=inv(d)
 ct=mul(b,di);cs=neg(mul(a,di));h=mul(const(2*s),mul(b,mul(di,di)));hp=mul(a,di)
 rg=product_radius(ct,at)+product_radius(cs,ass)
 rh=product_radius(h,ass)+product_radius(neg(h),at)+product_radius(hp,aps)
 _,wr=mr(w)
 return (w[1]*rg+wr*A0,w[1]*rh+wr*3),{'denominator_lower_abs':min(abs(d[0]),abs(d[1])),'node_radii':(rg,rh)}
def amplification(s):
 if type(s)is not F or not F(1,128)<=s<=16:raise ValueError('pole')
 pole(s)
 k=kp=F(0)
 for n in range(N):
  den=(2*n+1)*8**(2*n+1)
  term=guard(s**(2*n+2)/den);termp=guard((2*n+2)*s**(2*n+1)/den)
  k=guard(k+term);kp=guard(kp+termp)
 return k,kp

def total(s,ass,aps,node_radii):
 ass,aps=box(ass),box(aps);_,ea=mr(ass);_,ep=mr(aps);k,kp=amplification(s)
 low=(EPS*ea+EPS**3*A0/(6*s*s),EPS*ep+EPS**3*A0/(3*s**3))
 high=(k*ea,kp*ea+k*ep);rem=F(12**40,81*8**81);quad=128*F(1,4**52)
 widths=tuple(F(200,157)*(node_radii[i]+low[i]+high[i]+rem/2+quad+F(1,10**35))+F(1,10**35)for i in range(2))
 tree((low,high,widths))
 return {'widths':widths,'passes':tuple(widths[i]<=TARGETS[i]for i in range(2)),'high_input_radii':high,'low_radii':low,'scope':'prospective error only; no integral value'}
