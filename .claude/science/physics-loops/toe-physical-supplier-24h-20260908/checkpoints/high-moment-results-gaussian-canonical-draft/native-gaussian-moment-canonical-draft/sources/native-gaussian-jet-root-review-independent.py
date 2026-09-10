"""Independent scalar endpoint and sparse-identity verifier; no producer imports."""
from math import factorial,comb
Q=1<<256;CAP=4096
class Invalid(ValueError):pass
def need(x,m):
 if not x:raise Invalid(m)
def bound(x):need(type(x)is int and abs(x).bit_length()<=CAP,'integer cap');return x
def ceildiv(n,d):
 q,r=divmod(n,d);return q+bool(r)
def real(n,d=1):return(bound(n*Q//d),bound(ceildiv(n*Q,d)))
def point(n,d=1):return(real(n,d),(0,0))
Z=((0,0),(0,0))
def plus(x,y):return(bound(x[0]+y[0]),bound(x[1]+y[1]))
def minus(x):return(-x[1],-x[0])
def times(x,y):
 a,b=x;c,d=y
 if a>=0:
  if c>=0:lo,hi=a*c,b*d
  elif d<=0:lo,hi=b*c,a*d
  else:lo,hi=b*c,b*d
 elif b<=0:
  if c>=0:lo,hi=a*d,b*c
  elif d<=0:lo,hi=b*d,a*c
  else:lo,hi=a*d,a*c
 else:
  if c>=0:lo,hi=a*d,b*d
  elif d<=0:lo,hi=b*c,a*c
  else:lo,hi=min(a*d,b*c),max(a*c,b*d)
 return bound(lo//Q),bound(ceildiv(hi,Q))
def add(x,y):return plus(x[0],y[0]),plus(x[1],y[1])
def neg(x):return minus(x[0]),minus(x[1])
def mul(x,y):return plus(times(x[0],y[0]),minus(times(x[1],y[1]))),plus(times(x[0],y[1]),times(x[1],y[0]))
def div(x,n):return tuple((bound(z[0]//n),bound(ceildiv(z[1],n)))for z in x)
def imag(n,d=1):return(0,0),real(n,d)
def put(m,k,v):
 if v!=Z:m[k]=add(m.get(k,Z),v)
def matrix_add(a,b):
 c=dict(a)
 for k,v in b.items():put(c,k,v)
 return c

def linear(n):
 a={}
 for left in range(n):
  right=n-1-left;v=-(-1)**right*comb(n-1,left)
  a[2*left,2*right+1]=imag(2*v,factorial(n));a[2*left+1,2*right]=imag(-2*v,factorial(n))
 return a

def operator_coefficients(D,emit):
 A={};nonlinear={};current={}
 for n in range(1,11):
  A[n]=matrix_add(linear(n),current);nonlinear[n]=current
  emit('operator_order',{'order':n,'linear_entries':len(linear(n)),'nonlinear_entries':len(current),'A':[[i,j,v]for(i,j),v in A[n].items()],'Q':[[i,j,v]for(i,j),v in current.items()]})
  if n==10:break
  numerator={}
  for(i,j),v in current.items():put(numerator,(i+2,j),v);put(numerator,(i,j+2),neg(v))
  for(i,j),v in A[n].items():
   power,source=divmod(j,2)
   for target in range(2):
    c=1-target;coefficient=imag(2 if target==0 else-2)
    put(numerator,(i,c),neg(mul(mul(v,D[power][source][target]),coefficient)))
  current={k:div(v,n+1)for k,v in numerator.items()}
 return A,nonlinear

def trace(a,B):
 out=Z
 for(i,j),v in a.items():out=add(out,mul(v,B[i//2+j//2][j%2][i%2]))
 return out

def product(a,b,B):
 out={}
 for(i,j),x in a.items():
  for(k,l),y in b.items():
   p=j//2+k//2;need(p<=8,'degree');put(out,(i,l),mul(mul(x,B[p][j%2][k%2]),y))
 return out

def high_logs(D,B,emit):
 A,N=operator_coefficients(D,emit);logs={n:div(trace(N[n],B),2)for n in range(7,11)};previous=A
 for factors in range(2,11):
  nextpower={}
  for n in range(factors,11):
   value={}
   for k in range(1,n-factors+2):value=matrix_add(value,product(A[k],previous[n-k],B))
   nextpower[n]=value
   if n>=7:
    term=div(trace(value,B),2*factors);term=term if factors%2 else neg(term);logs[n]=add(logs[n],term);emit('log_power',{'order':n,'factors':factors,'entries':len(value),'trace_contribution':term})
  previous=nextpower
 for n,v in logs.items():emit('log_coefficient',{'order':n,'value':v});need(v[1][0]<=0<=v[1][1],'real log')
 return logs

def scalar_high(accepted,high,emit):
 z={n:div(mul(point((-1)**n),x),factorial(n))for n,x in accepted.items()};logs={}
 for n in range(1,7):
  value=mul(point(n),z[n])
  for k in range(1,n):value=add(value,neg(mul(mul(point(k),logs[k]),z[n-k])))
  logs[n]=div(value,n)
 emit('lower_logs_from_accepted',{'orders':list(range(1,7)),'logs':logs});logs.update(high);new={}
 for n in range(7,11):
  value=Z
  for k in range(1,n+1):value=add(value,mul(mul(point(k),logs[k]),z[n-k]));emit('scalar_reconstruction_partial',{'order':n,'term':k,'sum':value})
  z[n]=div(value,n);new[n]=mul(point((-1)**n*factorial(n)),z[n]);emit('new_moment_raw',{'order':n,'value':new[n]});need(new[n][1][0]<=0<=new[n][1][1],'real moment')
 return new

def source_tables(M,kind):
 """M is authenticated outward-grid absolute radial data, not a supplier."""
 need(kind in('P','O'),'class');D={};B={}
 def pair(j):return mul(point(2),M[j])if kind=='P'else div(M[j+2],3)
 for j in range(9):
  if j%2==0:
   D[j]=[[M[j],Z],[Z,pair(j)]];cross=((0,0),div(M[j+1],6)[0]);B[j]=[[div(M[j],2),cross],[neg(cross),div(pair(j),2)]]
  else:
   cross=((0,0),div(M[j+1],3)[0]);D[j]=[[Z,neg(cross)],[cross,Z]];half=div(cross,2);B[j]=[[neg(div(M[j],2)),neg(half)],[half,neg(div(pair(j),2))]]
 return D,B

def normalize(x):
 # Preserve scalar types: bool cannot impersonate a dyadic endpoint or count.
 if type(x)is bool:return('BOOL',x)
 if type(x)is int:return('INT',x)
 if isinstance(x,(list,tuple)):return tuple(normalize(v)for v in x)
 if isinstance(x,dict):return tuple(sorted((str(k),normalize(v))for k,v in x.items()))
 return(type(x).__name__,x)
def compare(x,y,label):need(normalize(x)==normalize(y),label)
