from fractions import Fraction as F
from interval_base import sin_bounds,roots,down,up

def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
 z=[x*y for x in a for y in b];return min(z),max(z)
def scale(a,b):return mul(a,(b,b))
def poly(n,x):
 a=(F(1),F(1));b=x
 if n==0:return a
 for j in range(1,n):a,b=b,scale(add(scale(mul(x,b),2*j+1),scale(a,-j)),F(1,j+1))
 return b
def val(n,x):return poly(n,(x,x))[0]
def gauss(n):
 brackets=[];a=F(-1);fa=val(n,a)
 for j in range(1,4097):
  b=F(-1)+F(j,2048);fb=val(n,b)
  if fb==0:raise ValueError('grid root requires separate contract')
  if fa*fb<0:brackets.append((a,b))
  a,fa=b,fb
 if len(brackets)!=n:raise ValueError('root completeness')
 out=[]
 for a,b in brackets:
  fa=val(n,a)
  while b-a>F(1,2**160):
   c=(a+b)/2;fc=val(n,c)
   if fc==0:a=b=c;break
   if fa*fc<0:b=c
   else:a=c;fa=fc
  x=(a,b);one=add((1,1),scale(mul(x,x),-1))
  numerator=scale(add(poly(n-1,x),scale(mul(x,poly(n,x)),-1)),n)
  derivative=mul(numerator,(1/one[1],1/one[0]))
  sq=mul(derivative,derivative)
  if derivative[0]<=0<=derivative[1]:raise ValueError('derivative zero enclosure')
  # squaring interval must not retain a negative cross endpoint
  sq=(min(derivative[0]**2,derivative[1]**2),max(derivative[0]**2,derivative[1]**2))
  den=mul(one,sq);out.append((x,(2/den[1],2/den[0])))
 return out

def run_case(s,target,progress=None):
 if s not in (F(1),F(2)):raise ValueError('fixed s')
 N=8 if s==1 else 4;p=2
 while F(32,s*s)*F(1,4**p)>target/4:p+=2
 rule=gauss(p);nodes=[]
 for panel in range(N):
  for (a,b),weight in rule:
   u=((a+1)/2+panel)/N;v=((b+1)/2+panel)/N
   lo=sin_bounds(u)[0];hi=sin_bounds(v)[1]
   nodes.append(((4*lo*lo,4*hi*hi),scale(weight,F(1,2*N))))
 lower=upper=F(0)
 for i,(x,wx) in enumerate(nodes):
  for y,wy in nodes:
   a=(s*s+x[0]+y[0],s*s+x[1]+y[1]);rlo=roots(a[0]*(a[0]+4))[0];rhi=roots(a[1]*(a[1]+4))[1]
   ww=mul(wx,wy);lower+=down(ww[0]/rhi,64);upper+=up(ww[1]/rlo,64)
  if progress:progress({'completed_rows':i+1,'rows':len(nodes)})
 err=F(32,s*s)*F(1,4**p);lower-=err;upper+=err
 return {'s':str(s),'target':str(target),'N':N,'p':p,'bounds':[str(lower),str(upper)],'width':str(upper-lower),'status':'CERTIFIED_TARGET' if upper-lower<=target else 'INDETERMINATE','evaluations':len(nodes)**2}
