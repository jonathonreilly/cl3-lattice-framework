import sys,types,json
from fractions import Fraction as F
from pathlib import Path
p=Path(sys.argv[1]);m=types.ModuleType('tested');exec(compile(p.read_bytes(),str(p),'exec'),m.__dict__)
count=0
def test(b):
 global count
 count+=1
 if not b:raise ValueError('test '+str(count))
def contains(i,x):return i.lo<=x<=i.hi
# Exact ambient pure covariance, synthetic dyadic vectors.
Y=[[F((i*7+j*3+i*j)%11-5,4) for j in range(5)] for i in range(6)]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def gamma(a):return [(-a[i+1] if i%2==0 else a[i-1]) for i in range(len(a))]
v=list(map(list,zip(*Y)));G=[[m.Iv(dot(a,b)) for b in v] for a in v];J=[[m.Iv(dot(a,gamma(b))) for b in v] for a in v]
i=0;r=dot(v[i],v[i]);a=v[i];b=gamma(a)
w=[[x-dot(z,a)*aa/r-dot(z,b)*bb/r for x,aa,bb in zip(z,a,b)] for z in v]
Gn,Jn=m.pivot(G,J,i)
for k in range(5):
 for l in range(5):test(contains(Gn[k][l],dot(w[k],w[l])));test(contains(Jn[k][l],dot(w[k],gamma(w[l]))))
# Independent scalar dual-number differentiation of non-native moments.
class D:
 def __init__(self,x,d=0):self.x=F(x);self.d=F(d)
 def __add__(self,b):
  if not isinstance(b,D):b=D(b)
  return D(self.x+b.x,self.d+b.d)
 __radd__=__add__
 def __neg__(self):return D(-self.x,-self.d)
 def __sub__(self,b):return self+-b if isinstance(b,D) else self+D(-b)
 def __rsub__(self,b):return D(b)+-self
 def __mul__(self,b):
  if not isinstance(b,D):b=D(b)
  return D(self.x*b.x,self.d*b.x+self.x*b.d)
 __rmul__=__mul__
 def __truediv__(self,b):
  if not isinstance(b,D):b=D(b)
  return D(self.x/b.x,(self.d*b.x-self.x*b.d)/(b.x*b.x))
 def __rtruediv__(self,b):return D(b)/self
N,O,T=m.operators();data={};ind={}
for s in (1,2):
 z=D(s,1);A=1/(4+z*z);B=2/(4+z*z);dd=(1-z*z*A)/6
 data[s]=tuple(m.Iv(x) for x in (A.x,A.d,B.x,B.d))
 for sig in (1,-1):
  C=[[sig*z*(A*N[a][b]-dd*O[a][b])+dd*T[a][b] for b in range(7)] for a in range(7)]
  L=[[-B*N[a][b]-z*z*B*O[a][b]/6+sig*z*B*T[a][b]/6 for b in range(7)] for a in range(7)]
  ind[s,sig]=C,L
G,J=m.assemble(data)
for i in range(28):
 s,sig=m.LABELS[i//7];a=i%7
 for j in range(i,28):
  t,tau=m.LABELS[j//7];b=j%7;den=sig*s+tau*t
  if den:
   g=(ind[t,tau][0][a][b].x-ind[s,-sig][0][a][b].x)/den
   q=-(ind[t,tau][1][a][b].x-ind[s,-sig][1][a][b].x)/den
  else:g=ind[t,tau][0][a][b].d/tau;q=-ind[t,tau][1][a][b].d/tau
  test(contains(G[i][j],g));test(contains(J[i][j],q))
# Interval failure branch is actual production routine, no Gram assembly.
z=[[m.Iv(-1,1)]];status,rows,initial=m.compress(z,[[m.Iv(0)]],lambda _:None)
test(status=='INDETERMINATE_POSITIVE_PIVOT')
print(json.dumps({'status':'PASS','predicates':count,'scope':'synthetic rational vectors and dual-number moment functions; no physical inputs'}))
