"""Independent saved matrix certificate; no producer imports or input loader."""
from fractions import Fraction as F
from math import isqrt
Q=2**256
CAP=32768
class BoundExceeded(ValueError):pass
def integer(v):
 if type(v)is not int or v.bit_length()>CAP:raise BoundExceeded('integer cap')
 return v
def rational(x):
 x=F(x);integer(x.numerator);integer(x.denominator);return x
def require(v,m):
 if not v:raise ValueError(m)
def transpose(a):return [list(c)for c in zip(*a)]
def multiply(a,b):
 require(len(a)>0 and len(b)>0 and all(len(r)==len(b)for r in a),'product shape')
 ans=[[0]*len(b[0])for _ in a]
 for k in range(len(b)):
  for i in range(len(a)):
   for j in range(len(b[0])):ans[i][j]=integer(ans[i][j]+integer(a[i][k]*b[k][j]))
 return ans
def normceil(a,den):
 total=0
 for row in a:
  for x in row:total=integer(total+integer(x*x))
 numerator=integer(total*Q**2);denominator=integer(den**2)
 n=isqrt(numerator//denominator)
 if n*n*denominator!=numerator:n+=1
 return rational(F(n,Q))
def seed(i,g):
 require(type(i)is int and 0<=i<399,'seed index')
 if i>=396:return {(i,g):F(1)}
 pole,kind=divmod(i,6);axis=kind//2
 first=F((1 if kind%2==0 else -1)*(1 if axis==0 else -1),2)
 return {(6*pole+axis,g):first,(6*pole+axis+3,g):F(1,2)}
def reconstruct(ids,entries):
 require(len(ids)==24 and len(set(ids))==24,'24 unique')
 cols=[seed(i,g)for i in ids for g in (0,1)]
 labels=sorted({x for c in cols for x in c});embedding=[[c.get(x,F())for c in cols]for x in labels]
 boxes={}
 require(len(entries)==300,'300 entries')
 z=0
 for a in range(24):
  for b in range(a,24):
   d=entries[z];z+=1;require(type(d['a'])is int and type(d['b'])is int and (d['a'],d['b'])==(a,b),'entry order')
   g,j=d['g'],d['j']
   for v in (g,j):require(len(v)==2 and all(type(x)is int for x in v) and v[0]<=v[1],'entry interval')
   if a==b:require(j[0]<=0<=j[1],'zero skew diagonal');j=[0,0]
   for x,y,v in ((2*a,2*b,g),(2*a+1,2*b+1,g),(2*a,2*b+1,j),(2*a+1,2*b,[-j[1],-j[0]])):
    boxes[x,y]=v;boxes[y,x]=v
 c=[[F(sum(boxes[i,j]),2**193)for j in range(48)]for i in range(48)]
 r=[[F(boxes[i,j][1]-boxes[i,j][0],2**193)for j in range(48)]for i in range(48)]
 return c,r,labels,embedding

def certificate(c,r,t,embedding,save):
 n=len(t);require(0<n<=48 and 0<len(embedding)<=96,'dimensions')
 for a in (c,r,t,embedding):
  require(all(len(row)==n for row in a),'row shape')
  for row in a:
   for x in row:rational(x)
 require(len(c)==len(r)==n,'square')
 require(all(t[i][i]>0 and all(t[i][j]==0 for j in range(i))for i in range(n)),'positive upper')
 require(all(c[i][j]==c[j][i] and r[i][j]==r[j][i] and r[i][j]>=0 for i in range(n)for j in range(n)),'symmetric')
 cc=[];rr=[]
 for i in range(n):
  cr=[];rad=[]
  for j in range(n):
   low=(c[i][j]-r[i][j])*Q;high=(c[i][j]+r[i][j])*Q
   lo=low.numerator//low.denominator;hi=-((-high.numerator)//high.denominator)
   mid=integer((lo+hi)//2);cr.append(mid);rad.append(integer(max(mid-lo,hi-mid)))
  cc.append(cr);rr.append(rad)
 def grid(a):
  ans=[]
  for row in a:
   z=[]
   for x in row:
    v=x*Q;require(v.denominator==1,'exact grid');z.append(integer(v.numerator))
   ans.append(z)
  return ans
 ti,ei=grid(t),grid(embedding)
 save('dyadic_inputs',dict(Gcenter=cc,radius=rr,T=ti,E=ei,scale=Q))
 # Different association from producer T^T (C T).
 h=multiply(multiply(transpose(ti),cc),ti)
 save('H_integer',dict(H=h,denominator=Q**3))
 defect=[[integer(h[i][j]-Q**3*(i==j))for j in range(n)]for i in range(n)]
 eta,tn=normceil(rr,Q),normceil(ti,Q)
 e=rational(normceil(defect,Q**3)+eta*tn**2)
 save('error',dict(e=e,eta=eta,Tnorm_upper=tn))
 if e>=1:return dict(status='INDETERMINATE_RESIDUAL',e=e)
 et=multiply(ei,ti);radius=rational(normceil(et,Q**2)*e/(1-e)**2)
 center=[[F(v,Q**2)for v in row]for row in et]
 save('coefficient_box',dict(center=center,radius=radius))
 l1=rational(max(sum((abs(row[j])+radius for row in center),F())for j in range(n)))
 return dict(status='CERTIFIED_ENCLOSURE',center=center,radius=radius,e=e,width_pass=2*radius<=F(1,2**39),l1_pass=l1<=2**40)
