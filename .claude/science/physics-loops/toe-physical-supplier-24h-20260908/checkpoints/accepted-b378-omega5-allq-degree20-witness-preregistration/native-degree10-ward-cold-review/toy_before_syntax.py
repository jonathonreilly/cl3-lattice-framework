from fractions import Fraction as F
# Exact complex pairs; synthetic formal Wick contractions, not native covariance values.
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def mul(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(x,a):return(x[0]*a,x[1]*a)
n=0
for c,nu in [(F(4,5),F(15)),(F(7,9),F(14))]:
 for kind in ('P','O'):
  ed=6*c if kind=='P' else nu/3;v2=F(12 if kind=='P' else 14)
  dots={('a','a'):F(1),('d','d'):F(2),('k','k'):F(6),('v','v'):v2,('k','d'):F(2),('a','v'):F(-2)}
  kap={('a','d'):-c,('a','k'):-3*c,('d','v'):-ed,('v','k'):nu/3}
  def cov(a,b):return(dots.get((a,b),dots.get((b,a),F(0))),kap.get((a,b),-kap.get((b,a),F(0))))
  def wick(w):
   if not w:return(F(1),F(0))
   z=(F(0),F(0))
   for j in range(1,len(w)):z=add(z,scale(mul(cov(w[0],w[j]),wick(w[1:j]+w[j+1:])),(-1)**(j-1)))
   return z
  # A=gamma(k)gamma(d)+gamma(a)gamma(v), [H,B]=-A.
  aa=(F(0),F(0))
  for x in [('k','d'),('a','v')]:
   for y in [('k','d'),('a','v')]:aa=add(aa,wick(x+y))
  m4=4-aa[0];assert aa[1]==0
  assert m4==(20+36*c*c-F(2,3)*c*nu if kind=='P' else22+F(4,3)*c*nu);n+=1
  cross=F(0)
  for x,b in [('v',F(-2)),('a',F(-4))]:
   for y,e in [('k',F(1)),('d',F(-1))]:cross-=b*e*cov(x,y)[1]
  assert cross==(2*nu/3-20*c if kind=='P' else -8*c);n+=1
print({'synthetic_formal_Wick_predicates':n,'native_evaluations':0})
