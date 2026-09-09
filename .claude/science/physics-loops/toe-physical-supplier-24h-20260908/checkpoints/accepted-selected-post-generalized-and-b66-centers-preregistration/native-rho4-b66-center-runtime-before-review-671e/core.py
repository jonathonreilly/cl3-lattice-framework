"""NEW rho4/40-tail center, not an old B26 interval contraction. No I/O."""
from fractions import Fraction as F
from math import comb
BITS=256;S=1<<BITS;CAP=32768;EPS=F(1,2**64);A0=F(17,60);RESERVE=F(1,10**35)
def guard(x):
 x=F(x)
 if max(abs(x.numerator).bit_length(),x.denominator.bit_length())>CAP:raise ValueError('stored rational32768')
 return x
def box(x):
 if len(x)!=2:raise ValueError('two endpoints')
 a,b=map(guard,x)
 if a>b:raise ValueError('ordered box')
 return a,b
def mid(x):return guard(sum(x)/2)
def mul(x,y):
 z=[guard(a*b)for a in x for b in y];return min(z),max(z)
def inv(x):
 if x[0]<=0<=x[1]:raise ValueError('denominator does not separate')
 return guard(1/x[1]),guard(1/x[0])
def rounded(x):
 x=guard(x);n=x.numerator<<BITS
 if abs(n).bit_length()>CAP+BITS:raise ValueError('round transient')
 return guard(F(n//x.denominator,S))
def center(s,t,at,ass,aps,w):
 s=guard(s);t,at,ass,aps,w=map(box,(t,at,ass,aps,w))
 if not F(1,128)<=s<=16 or not 0<t[0]<=t[1]<=8 or not 0<w[0]<=w[1]:raise ValueError('fixed domain')
 a=(s*s,s*s);b=mul(t,t);di=inv((b[0]-a[0],b[1]-a[1]));ct=mul(b,di);cs=tuple(-v for v in reversed(mul(a,di)));h=mul((2*s,2*s),mul(b,mul(di,di)));hp=mul(a,di)
 # Exactly the centers whose errors were bounded by the accepted width ledger.
 g=guard(mid(ct)*mid(at)+mid(cs)*mid(ass));hh=guard(mid(h)*(mid(ass)-mid(at))+mid(hp)*mid(aps))
 return rounded(mid(w)*g),rounded(mid(w)*hh)
def moments(maximum):
 if type(maximum)is not int or not 0<=maximum<=40:raise ValueError('moment40 cap')
 a=[comb(2*n,n)for n in range(maximum+1)];out=[]
 for n in range(maximum+1):out.append(sum(comb(n,k)*comb(k,j)*a[j]*a[k-j]*a[n-k]for k in range(n+1)for j in range(k+1)))
 return out

def tail_centers(s,ass,aps,M):
 if len(M)!=41 or M[:3]!=[1,6,42]:raise ValueError('exact moments fixed40')
 s=guard(s);j=mid(box(ass));jp=mid(box(aps));g=hh=F(0)
 for n in range(40):
  old=j;j=guard(M[n]-s*s*j);jp=guard(-2*s*old-s*s*jp);d=(2*n+1)*8**(2*n+1)
  g=guard(g+F((-1)**n,d)*j);hh=guard(hh-F((-1)**n,d)*jp)
 rem=F(12**40,81*8**81)
 # Both positive remainders centered at half upper remainder, never at zero.
 return (rounded(g+rem/2),rounded(hh+rem/2))
def low_centers(s,ass,aps):
 s=guard(s);return rounded(EPS*mid(box(ass))-EPS**3*A0/(6*s*s)),rounded(-EPS*mid(box(aps))-EPS**3*A0/(3*s**3))
def finalize(centers,radii,pi_box):
 pl,pu=box(pi_box)
 if not F(157,50)<pl<=pu<4:raise ValueError('pi box')
 ans=[]
 for k in range(2):
  r=guard(radii[k]);c=guard(centers[k])
  if r<0:raise ValueError('radius')
  x=mul((c-r,c+r),(2/pu,2/pl));lo=rounded(x[0]);hi=-rounded(-x[1])
  ans.append((lo,hi)if k==0 else(-hi,-lo))
 return ans
