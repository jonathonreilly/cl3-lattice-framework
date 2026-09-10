"""Independent directed256 reference reconstruction, no producer imports or native loader.
Complex values are pairs of integer endpoint intervals. Source tables supplied explicitly.
This interval reference has no native input loader or runtime.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
LIMIT=20000
GRID=1<<256
CAP=4096
ZERO=((0,0),(0,0));ONE=((GRID,GRID),(0,0))
def ceildiv(n,d):return -((-n)//d)
def real(q):
 q=F(q);return q.numerator*GRID//q.denominator,ceildiv(q.numerator*GRID,q.denominator)
def c(x=0,y=0):return real(x),real(y)
def checked(z):
 for v in z:
  if len(v)!=2 or any(type(x)is not int or abs(x).bit_length()>CAP for x in v)or v[0]>v[1]:raise ValueError('endpoint cap/order')
 return z
def ra(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[1],-x[0]
def product_bounds(x,y):
 a,b=x;d,e=y
 if a>=0:
  lo,hi=(a*d,b*e)if d>=0 else((b*d,a*e)if e<=0 else(b*d,b*e))
 elif b<=0:
  lo,hi=(a*e,b*d)if d>=0 else((b*e,a*d)if e<=0 else(a*e,a*d))
 else:
  lo,hi=(a*e,b*e)if d>=0 else((b*d,a*d)if e<=0 else(min(a*e,b*d),max(a*d,b*e)))
 return lo//GRID,ceildiv(hi,GRID)
def add(x,y):return checked((ra(x[0],y[0]),ra(x[1],y[1])))
def mul(x,y):
 return checked((ra(product_bounds(x[0],y[0]),neg(product_bounds(x[1],y[1]))),ra(product_bounds(x[0],y[1]),product_bounds(x[1],y[0]))))
def scale(x,q):
 q=F(q)
 def r(v):
  lo,hi=(v[0]*q.numerator,v[1]*q.numerator)if q>=0 else(v[1]*q.numerator,v[0]*q.numerator)
  return lo//q.denominator,ceildiv(hi,q.denominator)
 return checked((r(x[0]),r(x[1])))
def put(d,k,v):
 z=add(d.get(k,ZERO),v)
 if v!=ZERO:d[k]=z
 if len(d)>LIMIT:raise ValueError('bounded dictionary')
def indices(mask):return sorted(product(*(range(v+1)for v in mask)),key=lambda a:(sum(a),a))
def poly_product(a,b,mask):
 out={}
 for x,aa in a.items():
  for y,bb in b.items():
   z=tuple(i+j for i,j in zip(x,y))
   if any(i>j for i,j in zip(z,mask)):continue
   d=out.setdefault(z,{})
   for w,v in aa.items():
    for u,q in bb.items():
     key=w+u;d[key]=d.get(key,F(0))+v*q
     if not d[key]:del d[key]
   if sum(map(len,out.values()))>LIMIT:raise ValueError('word cap')
 return out
def words(mask,factors):
 """Ordered factors (variable, letters, scale); letter0 is free h."""
 zero=(0,)*len(mask);out={zero:{():F(1)}}
 for variable,letters,s in factors:
  f={}
  for n in range(mask[variable]+1):
   alpha=tuple(n if j==variable else 0 for j in range(len(mask)))
   f[alpha]={w:F(s**n,factorial(n))for w in product(letters,repeat=n)}
  out=poly_product(out,f,mask)
 return out

def operator(word,J,D):
 loc=[i for i,v in enumerate(word)if v]
 if not loc:raise ValueError('uncancelled pure h')
 M=dict(J[word[loc[0]]])
 for p,q in zip(loc,loc[1:]):
  nxt={}
  for (i,j),v in M.items():
   for (k,l),w in J[word[q]].items():put(nxt,(i,l),mul(mul(v,D(q-p-1,j,k)),w))
  M=nxt
 return {(loc[0],i,len(word)-1-loc[-1],j):v for(i,j),v in M.items()}
def multiply(A,B,projected):
 out={}
 for (p,i,q,j),v in A.items():
  for (r,k,s,l),w in B.items():put(out,(p,i,s,l),mul(mul(v,projected(q+r,j,k)),w))
 return out
def trace(A,P):
 z=ZERO
 for (p,i,q,j),v in A.items():z=add(z,mul(v,P(p+q,j,i)))
 return z
def reconstruct(mask,factors,J,D,P,emit=lambda *_:None):
 """Independent exact reference path; scalar source truth remains external."""
 W=words(mask,factors);keys=indices(mask);zero=keys[0];A={};ell={}
 for alpha in keys[1:]:
  full={};nonlinear={};linear={}
  for word,q in W.get(alpha,{}).items():
   m=sum(v!=0 for v in word)
   if m==0:raise ValueError('free cancellation')
   if m==1:linear[(next(v for v in word if v),len(word)-1)]=linear.get((next(v for v in word if v),len(word)-1),F(0))+q
   for k,v in operator(word,J,D).items():
    put(full,k,mul(c(q),v))
    if m>=2:put(nonlinear,k,mul(c(q),v))
  if sum(alpha)>=2 and any(linear.values()):raise ValueError('one-defect trace premise')
  A[alpha]=full;emit('operator_matrices',{'alpha':alpha,'A':full,'Q':nonlinear});ell[alpha]=scale(trace(full if sum(alpha)==1 else nonlinear,P),F(1,2));emit('operator_coefficient',{'alpha':alpha,'entries':len(full),'nonlinear_entries':len(nonlinear),'trace':ell[alpha]})
 previous=A
 for degree in range(2,sum(mask)+1):
  current={}
  for alpha in keys[1:]:
   out={}
   for beta,B in A.items():
    gamma=tuple(x-y for x,y in zip(alpha,beta))
    if gamma not in previous:continue
    for k,v in multiply(B,previous[gamma],P).items():put(out,k,v)
   if sum(alpha)>=degree:
    current[alpha]=out;emit('log_power_matrix',{'alpha':alpha,'factors':degree,'matrix':out});signed=scale(trace(out,P),F((-1)**(degree+1),2*degree));ell[alpha]=add(ell[alpha],signed);emit('log_power_trace',{'alpha':alpha,'factors':degree,'signed_trace':signed})
  previous=current
 for alpha in keys[1:]:emit('log_coefficient',{'alpha':alpha,'value':ell[alpha]})
 Z={zero:ONE}
 for alpha in keys[1:]:
  total=ZERO
  for beta,L in ell.items():
   gamma=tuple(x-y for x,y in zip(alpha,beta))
   if gamma in Z:total=add(total,scale(mul(L,Z[gamma]),sum(beta)))
  Z[alpha]=scale(total,F(1,sum(alpha)));emit('jet_coefficient',{'alpha':alpha,'value':Z[alpha]})
 return Z
