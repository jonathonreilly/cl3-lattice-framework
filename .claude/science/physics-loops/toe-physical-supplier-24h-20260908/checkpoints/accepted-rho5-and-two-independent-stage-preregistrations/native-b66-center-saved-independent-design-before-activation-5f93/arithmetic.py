"""Independent exact-rational checks; no producer imports or I/O."""
from fractions import Fraction as F
from math import factorial,comb
Q=2**256;CAP=32768

def fraction(x):
 if type(x)is not str or len(x)>20000:raise ValueError('canonical scalar string')
 a=F(x)
 if str(a)!=x or max(abs(a.numerator).bit_length(),a.denominator.bit_length())>CAP:raise ValueError('canonical bounded fraction')
 return a

def vector(xs):
 if type(xs)is not list or len(xs)!=2:raise ValueError('two components')
 return tuple(map(fraction,xs))

def interval(xs):
 if type(xs)is not list or len(xs)!=2:raise ValueError('pair')
 a,b=map(fraction,xs)
 if a>b:raise ValueError('order')
 return a,b

def fl(x):
 n=x.numerator*Q;d=x.denominator;q,r=divmod(n,d);return F(q,Q)
def ceil(x):return-fl(-x)
def mid(x):return (x[0]+x[1])/2
def times(x,y):
 products=[a*b for a in x for b in y];return min(products),max(products)
def weighted(s,t,A,As,Ap,w):
 """Whole-box coefficients first, exact midpoint products second."""
 a=s*s;b=(t[0]*t[0],t[1]*t[1]);d=(b[0]-a,b[1]-a)
 if not 0<t[0]<=t[1]<=8 or d[0]<=0<=d[1]:raise ValueError('separated positive t')
 inverse=(1/d[1],1/d[0]);ct=times(b,inverse);cs0=times((a,a),inverse);cs=(-cs0[1],-cs0[0])
 inv2=times(inverse,inverse);h=times((2*s,2*s),times(b,inv2));hp=times((a,a),inverse)
 g=mid(w)*(mid(ct)*mid(A)+mid(cs)*mid(As))
 hval=mid(w)*(mid(h)*(mid(As)-mid(A))+mid(hp)*mid(Ap))
 for x in(g,hval):
  if max(abs(x.numerator).bit_length(),x.denominator.bit_length())>CAP:raise ValueError('exact center cap')
 return fl(g),fl(hval)
def moments():
 return [F(sum(factorial(n)//(factorial(i)*factorial(j)*factorial(n-i-j))*comb(2*i,i)*comb(2*j,j)*comb(2*(n-i-j),n-i-j)for i in range(n+1)for j in range(n-i+1)))for n in range(41)]
def tails(s,As,Ap,M):
 a=mid(As);ap=mid(Ap)
 # Explicit polynomials; no recurrence shared with the producer.
 def poly(k):return sum(((-s*s)**j*M[k-1-j]for j in range(k)),F(0))+(-s*s)**k*a
 def derivative(k):return sum((2*j*(-1)**j*s**(2*j-1)*M[k-1-j]for j in range(1,k)),F(0))+2*k*(-1)**k*s**(2*k-1)*a+(-s*s)**k*ap
 sums=[F(0),F(0)]
 for k in range(1,41):
  factor=F((-1)**(k-1),(2*k-1)*8**(2*k-1));sums[0]+=factor*poly(k);sums[1]-=factor*derivative(k)
 rem=F(12**40,81*8**81);e=F(1,2**64);c=F(17,60)
 return (fl(e*a-e**3*c/(6*s*s)),fl(-e*ap-e**3*c/(3*s**3))),tuple(fl(x+rem/2)for x in sums)
def pi():
 def arctan(q,n):
  a=sum((F((-1)**j,(2*j+1)*q**(2*j+1))for j in range(n)),F(0));return a,a+F(1,(2*n+1)*q**(2*n+1))
 a,b=arctan(5,32),arctan(239,10);return 16*a[0]-4*b[1],16*a[1]-4*b[0]
def final(c,r,p):
 ans=[]
 for k in range(2):
  v=times((c[k]-r[k],c[k]+r[k]),(2/p[1],2/p[0]));lo,hi=fl(v[0]),ceil(v[1]);ans.append((lo,hi)if k==0 else(-hi,-lo))
 return ans
