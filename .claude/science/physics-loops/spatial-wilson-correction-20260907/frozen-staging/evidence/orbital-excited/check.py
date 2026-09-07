import time,signal,json,hashlib,resource,sys,itertools,math
from fractions import Fraction as F
from pathlib import Path
start=time.monotonic();signal.alarm(180)
class Q:
 def __init__(self,r=0,s=0):
  if isinstance(r,Q): self.r,self.s=r.r,r.s
  else:self.r,self.s=F(r),F(s)
 def __add__(a,b):b=Q(b);return Q(a.r+b.r,a.s+b.s)
 __radd__=__add__
 def __neg__(a):return Q(-a.r,-a.s)
 def __sub__(a,b):return a+-Q(b)
 def __rsub__(a,b):return Q(b)+-a
 def __mul__(a,b):b=Q(b);return Q(a.r*b.r+55*a.s*b.s,a.r*b.s+a.s*b.r)
 __rmul__=__mul__
 def __truediv__(a,b):
  b=Q(b);v=b.r*b.r-55*b.s*b.s
  return a*Q(b.r/v,-b.s/v)
 def __rtruediv__(a,b):return Q(b)/a
 def __eq__(a,b):b=Q(b);return a.r==b.r and a.s==b.s
 def __bool__(a):return bool(a.r or a.s)
 def enc(a):return dict(rational=str(a.r),sqrt55=str(a.s),diagnostic=float(a.r)+math.sqrt(55)*float(a.s))
class Jet:
 # actual derivatives, not divided Taylor coefficients
 def __init__(self,v=0,a=0,b=0,ab=0):
  if isinstance(v,Jet):self.c=v.c
  else:self.c=tuple(Q(x) for x in (v,a,b,ab))
 def __add__(x,y):y=Jet(y);return Jet(*(a+b for a,b in zip(x.c,y.c)))
 __radd__=__add__
 def __neg__(x):return Jet(*(-a for a in x.c))
 def __sub__(x,y):return x+-Jet(y)
 def __rsub__(x,y):return Jet(y)+-x
 def __mul__(x,y):
  y=Jet(y);v,a,b,ab=x.c;w,c,d,cd=y.c
  return Jet(v*w,a*w+v*c,b*w+v*d,ab*w+a*d+b*c+v*cd)
 __rmul__=__mul__
 def __truediv__(x,y):return x*(Q(1)/y)
def inverse(m):
 n=len(m);a=[[Q(x) for x in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(m)]
 for k in range(n):
  i=next(i for i in range(k,n) if a[i][k]);a[k],a[i]=a[i],a[k];z=a[k][k];a[k]=[x/z for x in a[k]]
  for i in range(n):
   if i!=k:
    z=a[i][k];a[i]=[v-z*w for v,w in zip(a[i],a[k])]
 return [row[n:] for row in a]
checks=[]
def ck(s,b):assert b,s;checks.append(s)
# Integer vertices have axis0 in bit3, matching the declared coordinate convention.
edges=[(v,v^(1<<(3-a))) for v in range(16) for a in range(4) if not v&(1<<(3-a))]
tree=[0,20,12,4,23,15,2,3,6,7,8,10,11,17,19];chords=[e for e in range(32) if e not in tree]
def face(a,b,base):
 verts=[base,base^(1<<(3-a)),base^(1<<(3-a))^(1<<(3-b)),base^(1<<(3-b))]
 return [(edges.index((x,y)),1) if (x,y) in edges else (edges.index((y,x)),-1) for x,y in zip(verts,verts[1:]+verts[:1])]
words=[];weights=[]
for a,b in itertools.combinations(range(4),2):
 others=[i for i in range(4) if i not in (a,b)]
 for bits in itertools.product((0,1),repeat=2):
  base=sum(x<<(3-i) for i,x in zip(others,bits))
  if (a,b)==(0,1) and not base&2:continue
  words.append([(chords.index(e),sign) for e,sign in face(a,b,base) if e in chords]);weights.append(F(1) if b==3 else F(1,2))
source_words=[face(0,1,t) for t in (0,1)];source=[[(chords.index(e),sign) for e,sign in w if e in chords] for w in source_words];u,v=[x[0][0] for x in source]
ck('literal sources indices0,1 signsminus',source==[[(0,-1)],[(1,-1)]])
ck('17chords22faces and weighted17',len(chords)==17 and len(words)==22 and sum(weights)==17)
B=[[sum(s for e,s in w if e==i) for i in range(17)] for w in words]
H=[[sum(w*r[i]*r[j] for w,r in zip(weights,B))/3 for j in range(17)] for i in range(17)]
omega=Q(0,F(1,90));theta=23/(32+3*Q(0,1))
G0=inverse(H);G=inverse([[x+(omega if i==j and i in (u,v) else 0) for j,x in enumerate(row)] for i,row in enumerate(H)])
ck('source Gaussian covariance',[[G0[i][j] for j in (u,v)] for i in (u,v)]==[[Q(F(192,11)),Q(F(138,11))],[Q(F(138,11)),Q(F(192,11))]])
J=[[Jet(G[i][j],-2*G[i][u]*G[u][j],-2*G[i][v]*G[v][j],4*(G[i][u]*G[u][v]*G[v][j]+G[i][v]*G[v][u]*G[u][j])) for j in range(17)] for i in range(17)]
precision=[[Jet(H[i][j]+(omega if i==j and i in (u,v) else 0),2*int(i==j==u),2*int(i==j==v),0) for j in range(17)] for i in range(17)]
ck('inverse derivatives all289entries fourcomponents',all(sum((precision[i][k]*J[k][j] for k in range(17)),Jet()).c==Jet(int(i==j)).c for i in range(17) for j in range(17)))
ck('mixed polynomial jet lowcase',(Jet(2,3,5,7)*Jet(11,13,17,19)).c==tuple(map(Q,(22,59,89,231))))
# Coefficients generated from shared validated trace-word formulas, not result JSON.
cubic={};quartic={}
for w,wt in zip(words,weights):
 for tri in itertools.combinations(w,3):
  ids=[e for e,sgn in tri];par=(-1)**sum(ids[i]>ids[j] for i in range(3) for j in range(i+1,3));key=tuple(sorted(ids));cubic[key]=cubic.get(key,F())-wt*math.prod(sgn for e,sgn in tri)*par/6
 for counts in itertools.product(range(5),repeat=len(w)):
  if sum(counts)!=4:continue
  key=tuple(e for (e,sgn),n in zip(w,counts) for j in range(n));coef=-wt*F(math.prod(sgn**n for (e,sgn),n in zip(w,counts)),3*math.prod(math.factorial(n) for n in counts));quartic[key]=quartic.get(key,F())+coef
cubic={k:c for k,c in cubic.items() if c};quartic={k:c for k,c in quartic.items() if c}
def tr4(g,seq):
 a,b,c,d=seq
 return F(64,3)*(g[a][b]*g[c][d]+g[a][d]*g[b][c])-F(8,3)*g[a][c]*g[b][d]
def minor(g,I,J):
 total=0
 for p in itertools.permutations(range(3)):
  sign=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3));total+=sign*g[I[0]][J[p[0]]]*g[I[1]][J[p[1]]]*g[I[2]][J[p[2]]]
 return total
def correction(g,half=True):
 e4=sum(c*tr4(g,s) for s,c in quartic.items());e32=48*sum(c*d*minor(g,I,J) for I,c in cubic.items() for J,d in cubic.items());haar=-2*sum(g[i][i] for i in range(17));halfsource=(g[u][u]+g[v][v]) if half else 0
 return dict(E4=e4,E3_squared=e32,Haar=haar,halfsource=halfsource,total=e32/2-e4+haar+halfsource)
ck('single covariance tracefour',tr4([[Q(3)]],(0,0,0,0))==360)
parts=correction(J);K,Ka,Kb,Kab=parts['total'].c
La=-8*G[u][u];Lb=-8*G[v][v];Lab=16*G[u][v]*G[u][v]
den=16+4*omega*(La+Lb)+omega*omega*(La*Lb+Lab)
ck('Mehler excited norm4 theta_squared',den==4*theta*theta)
ck('source exchange jet derivatives',Ka==Kb)
ratio=((4*omega+omega*omega*Lb)*Ka+(4*omega+omega*omega*La)*Kb+omega*omega*Kab)/den
z=correction(G0,False)['total'];k0=K-z;k1=k0+ratio
# Independent lowcase Wick: one scalar-color covariance determinant polynomial multilinearity.
ck('determinant lowcase',minor([[Q(2),Q(0),Q(0)],[Q(0),Q(3),Q(0)],[Q(0),Q(0),Q(5)]],(0,1,2),(0,1,2))==30)
def enc(x):
 if isinstance(x,Q):return x.enc()
 if isinstance(x,Jet):return dict(zip(['value','a','b','ab'],map(enc,x.c)))
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 return x
out=dict(status='PASS',checks=checks,TOTAL=len(checks),tree=tree,chords=chords,source=source,words=words,weights=list(map(str,weights)),cubic={str(k):str(c) for k,c in cubic.items()},quartic={str(k):str(c) for k,c in quartic.items()},parts=enc(parts),Gamma_log_derivatives=enc(dict(a=La,b=Lb,ab=Lab)),excited_Gamma_ratio=enc(den),theta=enc(theta),Z1=enc(z),k0=enc(k0),k1=enc(k1),first_top_ratio_relative_correction=enc(ratio),seconds=time.monotonic()-start,rss_MiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),shared_input_sha256=hashlib.sha256(Path('/private/tmp/toe-autonomous-native-ladder-20260907/cube-first-correction/check.py').read_bytes()).hexdigest(),scope='Conditional exact Wick differential coefficient; actual HS expansion and isolated branch justification are separate prerequisites; shared color contractions declared.')
assert out['seconds']<180 and 0<out['rss_MiB']<180
print(json.dumps(out,indent=2,allow_nan=False))
