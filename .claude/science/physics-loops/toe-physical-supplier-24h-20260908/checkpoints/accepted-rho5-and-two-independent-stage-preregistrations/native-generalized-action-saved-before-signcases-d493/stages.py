"""Independent fixed-grid stage arithmetic, expressed through exact Fractions."""
from fractions import Fraction as Q
from math import isqrt
S=2**256;BITS=4096
class Incomplete(ValueError):pass

def integer(x):
 if type(x)is not int or abs(x).bit_length()>BITS:raise Incomplete('endpoint cap')
 return x

def pair(x):
 if not isinstance(x,(list,tuple))or len(x)!=2:raise Incomplete('pair')
 a,b=map(integer,x)
 if a>b:raise Incomplete('order')
 return a,b

def down(q):return q.numerator//q.denominator

def up(q):return -down(-q)

def point(q):
 q=Q(q)*S
 if q.denominator!=1:raise Incomplete('non-grid point')
 return pair((q.numerator,q.numerator))

def plus(a,b):
 a,b=pair(a),pair(b)
 return pair((a[0]+b[0],a[1]+b[1]))

def neg(a):a=pair(a);return -a[1],-a[0]

class Arithmetic:
 def __init__(self):self.count=0
 def mul(self,a,b):
  a,b=pair(a),pair(b);self.count+=1
  if self.count>1000000:raise Incomplete('multiplication count')
  # Fraction formula is independent of producer integer quotient code.
  products=[Q(x,S)*Q(y,S)for x in a for y in b]
  return pair((down(min(products)*S),up(max(products)*S)))
 def mm(self,a,b):
  n,k,m=len(a),len(b),len(b[0]);shape(a,n,k);shape(b,k,m)
  c=[[point(0)for _ in range(m)]for _ in range(n)]
  for j in range(m):
   for t in range(k):
    for i in range(n):c[i][j]=plus(c[i][j],self.mul(a[i][t],b[t][j]))
  return c

def shape(a,n,m):
 if not isinstance(a,(list,tuple))or len(a)!=n or any(len(r)!=m for r in a):raise Incomplete('shape')
 for row in a:
  for x in row:pair(x)

def transpose(a):return [list(row)for row in zip(*a)]

def norm(a):
 row=max(sum(max(abs(x),abs(y))for x,y in r)for r in a)
 col=max(sum(max(abs(x),abs(y))for x,y in r)for r in zip(*a))
 return Q(max(row,col),S)

def midpoint(a):return pair(((a[0]+a[1])//2,)*2)

def symmetric(a,skew=False):
 a=[[pair(x)for x in r]for r in a];n=len(a)
 for i in range(n):
  if skew:
   if not a[i][i][0]<=0<=a[i][i][1]:raise Incomplete('skew diagonal')
   a[i][i]=point(0)
  for j in range(i+1,n):
   other=neg(a[j][i])if skew else a[j][i]
   z=pair((max(a[i][j][0],other[0]),min(a[i][j][1],other[1])))
   a[i][j]=z;a[j][i]=neg(z)if skew else z
 return a

def sqrt_interval(a):
 lo,hi=pair(a)
 if lo<=0:raise Incomplete('positive sqrt')
 # Explicit integer square comparison of rational endpoint squares.
 low=isqrt(lo*S);high=isqrt(hi*S)
 if high*high<hi*S:high+=1
 return pair((low,high))

def certify(h,a,z,x,emit):
 n=len(h)
 if not 0<n<=48:raise Incomplete('dimension')
 for m in(h,a,z,x):shape(m,n,n)
 if any(h[i][j]!=h[j][i]or z[i][j]!=z[j][i]or a[i][j]!=neg(a[j][i])or x[i][j]!=x[j][i]or x[i][j][0]!=x[i][j][1]for i in range(n)for j in range(n)):raise Incomplete('symmetry')
 ar=Arithmetic();identity=[[point(i==j)for j in range(n)]for i in range(n)]
 error=[[plus(h[i][j],neg(identity[i][j]))for j in range(n)]for i in range(n)]
 e=norm(error);emit('frame_residual',{'e':e})
 if e>=1:return dict(status='INDETERMINATE_FRAME',e=e,terms=ar.count)
 lower_h=1-e;hx=ar.mm(h,x);res=[[plus(identity[i][j],neg(hx[i][j]))for j in range(n)]for i in range(n)]
 r=norm(res);epsilon=r/lower_h;anorm=norm(a);emit('inverse_residual',dict(r=r,a=lower_h,epsilon=epsilon,A_norm=anorm))
 axa=ar.mm(ar.mm(a,x),a);emit('AXA',axa)
 schur=[[plus(z[i][j],axa[i][j])for j in range(n)]for i in range(n)];emit('N_raw',schur)
 schur=symmetric(schur)
 center=[[Q(lo+hi,2*S)for lo,hi in row]for row in schur]
 radius=max(sum(Q(hi-lo,2*S)for lo,hi in row)for row in schur);q=radius+anorm**2*epsilon
 gersh=max(center[i][i]+sum(abs(center[i][j])for j in range(n)if j!=i)for i in range(n))
 emit('Schur_center',dict(N0=center,N_radius=q,upper_numerator=gersh+q))
 if gersh+q<0:raise Incomplete('negative PSD upper')
 upper=(gersh+q)/lower_h
 lower=max([Q(0)]+[max(Q(0),center[i][i]-q)/Q(h[i][i][1],S)for i in range(n)])
 if lower>upper:raise Incomplete('contradictory bounds')
 for v in(upper,lower,e,epsilon,radius,q):
  if max(abs(v.numerator).bit_length(),v.denominator.bit_length())>65536:raise Incomplete('scalar cap')
 ans=dict(status='CERTIFIED_GENERALIZED_LEAKAGE_BOUND',delta_squared_upper=upper,delta_squared_lower=lower,target_squared=Q(1,10**12),leakage_pass=upper<=Q(1,10**12),target_excluded=lower>Q(1,10**12),e=e,inverse_error=epsilon,matrix_radius=radius,combined_radius=q,terms=ar.count,entrywise_C_claim=False)
 emit('Schur_center',dict(N0=center,N_radius=q));emit('result',ans);return ans
