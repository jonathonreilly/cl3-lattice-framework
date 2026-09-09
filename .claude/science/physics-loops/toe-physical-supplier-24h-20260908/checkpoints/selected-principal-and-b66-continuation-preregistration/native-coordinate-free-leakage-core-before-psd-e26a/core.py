"""Fixed256 interval leakage certificate. No native loader/candidate/runtime."""
from fractions import Fraction as F
BITS=256;S=1<<BITS;CAP=4096;MAX_TERMS=1000000
class Refused(ValueError):pass
class Arithmetic:
 def __init__(self):self.terms=0
 def check(self,x):
  if len(x)!=2 or any(type(v)is not int or abs(v).bit_length()>CAP for v in x)or x[0]>x[1]:raise Refused('4096bit ordered endpoints')
  return tuple(x)
 def add(self,a,b):return self.check((a[0]+b[0],a[1]+b[1]))
 def neg(self,a):return(-a[1],-a[0])
 def mul(self,a,b):
  self.terms+=1
  if self.terms>MAX_TERMS:raise Refused('fixed multiplication cap')
  z=[x*y for x in a for y in b];return self.check((min(z)//S,-((-max(z))//S)))
 def mm(self,A,B):
  out=[]
  for row in A:
   r=[]
   for col in zip(*B):
    z=(0,0)
    for x,y in zip(row,col):z=self.add(z,self.mul(x,y))
    r.append(z)
   out.append(r)
  return out
 def norm(self,A):
  rows=max(sum(max(map(abs,x))for x in row)for row in A);cols=max(sum(max(map(abs,x))for x in row)for row in zip(*A));return F(max(rows,cols),S)
def exact(x):
 x=F(x);v=x*S
 if v.denominator!=1:raise Refused('candidate must be exact dyadic')
 return(v.numerator,v.numerator)
def certify(H,A,Z,X,persist=lambda stage,data:None):
 target_squared=F(1,10**12) # h=1; physical scaling belongs to the authenticated adapter.
 ar=Arithmetic();n=len(H)
 if not 0<n<=48 or any(len(M)!=n or any(len(row)!=n for row in M)for M in(H,A,Z,X)):raise Refused('dimension')
 H,A,Z,X=[[[ar.check(x)for x in row]for row in M]for M in(H,A,Z,X)]
 for i in range(n):
  for j in range(n):
   if H[i][j]!=H[j][i]or Z[i][j]!=Z[j][i]or A[i][j]!=ar.neg(A[j][i]):raise Refused('proved symmetric/skew enclosure required')
   if X[i][j]!=X[j][i]or X[i][j][0]!=X[i][j][1]:raise Refused('exact symmetric X')
 I=[[exact(i==j)for j in range(n)]for i in range(n)]
 E=[[ar.add(H[i][j],ar.neg(I[i][j]))for j in range(n)]for i in range(n)];e=ar.norm(E);persist('frame_residual',{'e':e})
 if e>=1:return {'status':'INDETERMINATE_FRAME','e':e,'terms':ar.terms}
 a=1-e;HX=ar.mm(H,X);R=[[ar.add(I[i][j],ar.neg(HX[i][j]))for j in range(n)]for i in range(n)];r=ar.norm(R);epsilon=r/a;b=ar.norm(A);persist('inverse_residual',{'r':r,'a':a,'epsilon':epsilon,'A_norm':b})
 AXA=ar.mm(ar.mm(A,X),A);N=[[ar.add(Z[i][j],AXA[i][j])for j in range(n)]for i in range(n)]
 # Intersect only exact transpose equality; no uncertain PSD clipping.
 for i in range(n):
  for j in range(i+1,n):
   z=(max(N[i][j][0],N[j][i][0]),min(N[i][j][1],N[j][i][1]));z=ar.check(z);N[i][j]=N[j][i]=z
 centers=[[F(x[0]+x[1],2*S)for x in row]for row in N];z=max(sum(F(x[1]-x[0],2*S)for x in row)for row in N);q=z+b*b*epsilon
 upper0=max(centers[i][i]+sum(abs(centers[i][j])for j in range(n)if j!=i)for i in range(n));upper=max(F(0),upper0+q)/a
 lower=max([F(0)]+[max(F(0),centers[i][i]-q)/F(H[i][i][1],S)for i in range(n)])
 for scalar in (upper,lower,e,epsilon,z,q):
  if max(abs(scalar.numerator).bit_length(),scalar.denominator.bit_length())>65536:raise Refused('scalar certificate bit cap')
 result={'status':'CERTIFIED_GENERALIZED_LEAKAGE_BOUND','delta_squared_upper':upper,'delta_squared_lower':lower,'target_squared':F(target_squared),'leakage_pass':upper<=target_squared,'target_excluded':lower>target_squared,'e':e,'inverse_error':epsilon,'matrix_radius':z,'combined_radius':q,'terms':ar.terms,'entrywise_C_claim':False}
 persist('Schur_center',{'N0':centers,'N_radius':q});persist('result',result);return result
