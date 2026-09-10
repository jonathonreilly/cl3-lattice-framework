"""Inert degree-filtered dyadic Gaussian log jets. No native loader or CLI."""
from math import comb,factorial
BITS=256;S=1<<BITS;CAP=4096;NMAX=10
ZERO=((0,0),(0,0))
class Refused(ValueError):pass

def bounded(v):
 if type(v)is not int or abs(v).bit_length()>CAP:raise Refused('stored integer cap')
 return v

def ri(n,d=1):
 if type(n)is not int or type(d)is not int or d<=0:raise Refused('exact rational input')
 if max(abs(n).bit_length(),d.bit_length())>CAP-BITS:raise Refused('input transient cap')
 return bounded(n*S//d),bounded(-((-n*S)//d))
def point(n,d=1):return ri(n,d),(0,0)
def imaginary(n,d=1):return(0,0),ri(n,d)
def ra(a,b):return bounded(a[0]+b[0]),bounded(a[1]+b[1])
def rn(a):return -a[1],-a[0]
def rm(a,b):
 z=[x*y for x in a for y in b];return bounded(min(z)//S),bounded(-((-max(z))//S))
def rd(a,n):
 if type(n)is not int or not 0<n<=factorial(NMAX)*2:raise Refused('fixed integer divisor')
 return bounded(a[0]//n),bounded(-((-a[1])//n))
def add(a,b):return ra(a[0],b[0]),ra(a[1],b[1])
def neg(a):return rn(a[0]),rn(a[1])
def mul(a,b):return ra(rm(a[0],b[0]),rn(rm(a[1],b[1]))),ra(rm(a[0],b[1]),rm(a[1],b[0]))
def divide(a,n):return rd(a[0],n),rd(a[1],n)
def accum(D,key,value):
 if value!=ZERO:D[key]=add(D.get(key,ZERO),value)

def linear(n):
 out={};den=factorial(n)
 for p in range(n):
  q=n-1-p;c=-((-1)**q)*comb(n-1,p)
  out[2*p,2*q+1]=imaginary(2*c,den);out[2*p+1,2*q]=imaginary(-2*c,den)
 return out

def addition(A,B):
 out=dict(A)
 for key,v in B.items():accum(out,key,v)
 return out

def build_A(N,D,emit):
 As={};Qs={};Q={};mults=0
 for n in range(1,N+1):
  L=linear(n);As[n]=addition(L,Q);Qs[n]=Q;emit('operator_order',{'order':n,'linear_entries':len(L),'nonlinear_entries':len(Q)})
  if n==N:break
  nxt={}
  for(i,j),x in Q.items():accum(nxt,(i+2,j),x);accum(nxt,(i,j+2),neg(x))
  # -(L+Q) V. Ordinary contraction degree is <=n-1<=N-2.
  for(i,j),x in As[n].items():
   power,a=divmod(j,2)
   for b in range(2):
    gram=D(power,a,b)
    for c in range(2):
     if b==c:continue
     J=imaginary(2 if b==0 else-2);accum(nxt,(i,c),neg(mul(mul(x,gram),J)));mults+=2
  Q={key:divide(x,n+1)for key,x in nxt.items()}
  if any(i//2+j//2>n-1 for i,j in Q):raise Refused('nonlinear degree invariant')
 return As,Qs,mults

def product(A,C,B,N,counters):
 out={}
 for(i,j),x in A.items():
  for(k,l),y in C.items():
   power=j//2+k//2
   if power>N-2:raise Refused('projected source degree')
   v=mul(mul(x,B(power,j%2,k%2)),y);accum(out,(i,l),v);counters['complex_products']+=2
 return out

def trace(A,B,N,counters):
 z=ZERO
 for(i,j),x in A.items():
  power=i//2+j//2
  if power>N-2:raise Refused('trace degree')
  z=add(z,mul(x,B(power,j%2,i%2)));counters['complex_products']+=1
 return z

def logjet(N,D,B,emit=lambda *_:None,first_order=1):
 if type(N)is not int or not 2<=N<=NMAX:raise Refused('order2..10')
 if first_order not in (1,7)or first_order>N:raise Refused('output order')
 counters={'complex_products':0};As,Qs,counters['operator_products']=build_A(N,D,emit);ell={}
 # Linear sector is never passed to trace for n>=2.
 if first_order==1:ell[1]=divide(trace(As[1],B,N,counters),2)
 for n in range(max(2,first_order),N+1):ell[n]=divide(trace(Qs[n],B,N,counters),2)
 del Qs
 prev=As
 for m in range(2,N+1):
  curr={}
  for n in range(m,N+1):
   C={}
   for k in range(1,n-m+2):C=addition(C,product(As[k],prev[n-k],B,N,counters))
   if any(i//2+j//2>n-m for i,j in C):raise Refused('product degree invariant')
   curr[n]=C
   if n<first_order:continue
   v=divide(trace(C,B,N,counters),2*m);ell[n]=add(ell[n],v if m%2 else neg(v));emit('log_power',{'order':n,'factors':m,'entries':len(C),'trace_contribution':v if m%2 else neg(v)})
  prev=curr
 for n,x in ell.items():
  emit('log_coefficient',{'order':n,'value':x})
  if not x[1][0]<=0<=x[1][1]:raise Refused('nonreal log coefficient')
 return ell,counters

def scalar_exp(ell,N,accepted_low=None):
 # Optional accepted Z0..Z6 are reused, not recomputed as new native moments.
 low={}if accepted_low is None else dict(accepted_low);Z={0:point(1)};Z.update(low)
 for n in range(1,N+1):
  if n in low:continue
  total=ZERO
  for k in range(1,n+1):total=add(total,mul(mul(point(k),ell[k]),Z[n-k]))
  Z[n]=divide(total,n)
 return Z

def lower_logs(accepted_Z):
 N=max(accepted_Z);out={}
 if set(accepted_Z)!=set(range(N+1)):raise Refused('consecutive accepted coefficients')
 for n in range(1,N+1):
  v=mul(point(n),accepted_Z[n])
  for k in range(1,n):v=add(v,neg(mul(mul(point(k),out[k]),accepted_Z[n-k])))
  out[n]=divide(v,n)
 return out


def high_moments(ell_high,accepted_m):
 if set(accepted_m)!=set(range(7))or set(ell_high)!={7,8,9,10}:raise Refused('fixed lower/high moment split')
 low={n:divide(mul(point((-1)**n),x),factorial(n))for n,x in accepted_m.items()}
 ell={**lower_logs(low),**ell_high};Z=scalar_exp(ell,10,low)
 return {n:mul(point((-1)**n*factorial(n)),Z[n])for n in range(7,11)}
