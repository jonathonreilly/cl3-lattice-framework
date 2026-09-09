"""New fixed Gauss21 rule. Import is inert; generation is unexecuted."""
from fractions import Fraction as F
N=21;BITS=224

def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
 z=[x*y for x in a for y in b];return min(z),max(z)
def scale(a,s):return mul(a,(s,s))
def poly(n,x):
 a=(F(1),F(1));b=x
 if n==0:return a
 for j in range(1,n):a,b=b,scale(add(scale(mul(x,b),2*j+1),scale(a,-j)),F(1,j+1))
 return b
def value(x):return poly(N,(x,x))[0]
def rule(progress):
 # Exact central root is supplied separately; positive grid scan avoids it.
 assert value(F(0))==0
 intervals=[];a=F(1,2048);fa=value(a)
 if fa==0:raise ValueError('unexpected grid root')
 for j in range(2,2049):
  b=F(j,2048);fb=value(b)
  if fb==0:raise ValueError('unexpected grid root')
  if fa*fb<0:intervals.append((a,b))
  a,fa=b,fb
 if len(intervals)!=10:raise ValueError('positive root census')
 positive=[]
 for index,(a,b) in enumerate(intervals):
  fa=value(a)
  for step in range(BITS+1):
   if b-a<=F(1,2**BITS):break
   c=(a+b)/2;fc=value(c)
   if fc==0:a=b=c;break
   if fa*fc<0:b=c
   else:a=c;fa=fc
  if b-a>F(1,2**BITS):raise ValueError('fixed bisection cap')
  positive.append((a,b));progress({'stage':'root','index':index,'bracket':[str(a),str(b)]})
 roots=[(-b,-a) for a,b in reversed(positive)]+[(F(0),F(0))]+positive
 out=[]
 for i,x in enumerate(roots):
  one=add((F(1),F(1)),scale(mul(x,x),-1))
  num=scale(add(poly(N-1,x),scale(mul(x,poly(N,x)),-1)),N)
  derivative=mul(num,(1/one[1],1/one[0]))
  if derivative[0]<=0<=derivative[1]:raise ValueError('derivative zero')
  sq=(min(v*v for v in derivative),max(v*v for v in derivative));den=mul(one,sq)
  w=(2/den[1],2/den[0])
  if w[0]<=0:raise ValueError('weight positivity')
  out.append((x,w))
 if not sum(w[0] for x,w in out)<=2<=sum(w[1] for x,w in out):raise ValueError('weight sum enclosure')
 return out

def generate(progress):
 out=[]
 r=rule(progress)
 for j in range(-16,2):
  a=F(4)**j
  for i,(x,w) in enumerate(r):
   s=tuple(a*(5+3*z)/2 for z in x);weight=tuple(3*a*z/2 for z in w)
   if s[1]-s[0]>F(1,2**160) or weight[1]-weight[0]>F(1,2**160):raise ValueError('mapped root/weight width')
   out.append({'id':len(out),'panel':j,'root':i,'s_interval':list(map(str,s)),'weight_interval':list(map(str,weight)),'s':str(sum(s)/2),'weight':str(sum(weight)/2)})
 if len(out)!=378:raise ValueError('node census')
 return out
