"""Fixed192 sufficient scalable bound; source-only native interface disabled."""
from fractions import Fraction as F
import interval as iv
import coefficients as cf
Q=tuple((r,g) for r in(396,399,400,401) for g in(0,1))
def key(k):
 if type(k)is not tuple or len(k)!=2 or any(type(x)is not int for x in k) or not 0<=k[0]<402 or k[1]not in(0,1):raise ValueError('strict coordinate')
 return k
def sumv(xs):
 x=iv.ZERO
 for y in xs:x=cf.add(x,y)
 return x
def sq(x):
 cf.checked(x);lo=0 if x[0]<=0<=x[1] else min(x[0]*x[0],x[1]*x[1]);hi=max(x[0]*x[0],x[1]*x[1]);return cf.checked((lo//iv.S,-((-hi)//iv.S)))
def root(x):return cf.checked(iv.sqrt(x))
def upper(x):
 if x[1]<0:raise cf.Indeterminate('negative upper of positive quantity')
 return (0,x[1])
def intersection(a,b):
 z=max(a[0],b[0]),min(a[1],b[1])
 if z[0]>z[1]:raise cf.Indeterminate('empty PSD/symmetry intersection')
 return z
def raw_residual_bounds(diag,R):
 if len(diag)!=399:raise ValueError('saved half diagonal count')
 for x in diag:
  cf.checked(x)
  if x[0]<0:raise ValueError('negative saved diagonal')
 out={}
 for r,g in R:
  key((r,g))
  if r>=399:raise ValueError('original domain')
  if r<396:
   n,t=divmod(r,6);source=t%3;i=6*n+2*source;out[(r,g)]=(0,diag[i][1]+diag[i+1][1])
  else:out[(r,g)]=(0,diag[r][1])
 return out

def bound(columns,R,diag,entry,poles,alpha,persist,*,target=F(1,10**6)):
 """C must be authenticated ideal paired coefficients; caller supplies same F."""
 R=tuple(R);p=len(columns);s=len(R)
 if p>48 or p%2 or s>96 or len(set(R))!=s or len(poles)!=66 or len(alpha)!=66:raise ValueError('fixed shape/cap')
 for k in R:
  key(k)
  if k[0]>=399:raise ValueError('ORIGINAL domain')
 for col in columns:
  if not set(col)<=set(R):raise ValueError('coefficient support')
  for k,x in col.items():key(k);cf.checked(x)
  if any(x[1]-x[0]>cf.COEFFICIENT_WIDTH for x in col.values()) or sum(max(abs(v) for v in x) for x in col.values())>cf.MAGNITUDE*iv.S:raise cf.Indeterminate('coefficient width/l1')
 u=raw_residual_bounds(diag,R);persist({'stage':'residual_diagonals','u':[[*k,*v] for k,v in u.items()]});C=[[col.get(k,iv.ZERO) for col in columns] for k in R]
 M={}
 def get(a,b):
  pair=tuple(sorted((a,b)))
  if pair not in M:
   persist({'stage':'entry','row':a,'column':b});M[pair]=cf.checked(entry(a,b))
  return M[pair]
 MRQ=[[get(i,j) for j in Q] for i in R];MQQ=[[get(i,j) for j in Q] for i in Q]
 A=[[sumv(cf.mul(C[i][j],MRQ[i][a]) for i in range(s)) for a in range(8)] for j in range(p)]
 G=[[cf.sub(MQQ[a][b],sumv(cf.mul(A[j][a],A[j][b]) for j in range(p))) for b in range(8)] for a in range(8)]
 persist({'stage':'source_gram_raw','A':A,'G':G})
 for a in range(8):
  G[a][a]=intersection(G[a][a],upper(G[a][a]))
  for b in range(a):G[a][b]=G[b][a]=intersection(G[a][b],G[b][a])
 lam=[]
 for r,g in R:
  if r<396:
   n,t=divmod(r,6);ss=cf.checked(poles[n]);aa=cf.checked(alpha[n])
   if ss[0]<=0 or aa[0]<=0:raise ValueError('positive family')
   lam.append(cf.scaled(ss,-1 if t<3 else 1))
  else:lam.append(iv.ZERO)
 # Predeclared second candidate: dominant-coefficient row's Lambda midpoint,
 # rounded DOWN to2^-16, ties by lexicographic R key. Zero is always retained.
 z=[]
 for j in range(p):
  if not s:z.append(iv.ZERO);continue
  i=min(range(s),key=lambda i:(-abs(C[i][j][0]+C[i][j][1]),R[i]))
  val=F(lam[i][0]+lam[i][1],2*iv.S);val=F((val*2**16).__floor__(),2**16);z.append(iv.rational(val))
 candidates=[]
 for name,shift in(('zero',[iv.ZERO]*p),('dominant_diagonal',z)):
  X=[[cf.mul(cf.sub(lam[i],shift[j]),C[i][j]) for j in range(p)] for i in range(s)]
  persist({'stage':'free_X','candidate':name,'shift':shift,'X':X})
  a=sumv(cf.mul(root(u[R[i]]),root(upper(sumv(sq(x) for x in X[i])))) for i in range(s))
  persist({'stage':'free_bound','candidate':name,'shift':shift,'X':X,'a':a,'u':[[*k,*v] for k,v in u.items()]});candidates.append((name,a))
 a_upper=min(x[1][1] for x in candidates)
 # Free source map, same Gamma bit; rank-two impurity correction added later.
 Y0=[[iv.ZERO for _ in range(p)] for _ in range(8)];qi={k:i for i,k in enumerate(Q)}
 for i,(r,g) in enumerate(R):
  if r<396:
   n,t=divmod(r,6);dest=(396,399,400)[t%3];factor=cf.scaled(root(cf.checked(alpha[n])),-2)
  else:dest=(401,399,400)[r-396];factor=iv.ONE
  a=qi[(dest,g)]
  for j in range(p):Y0[a][j]=cf.add(Y0[a][j],cf.mul(factor,C[i][j]))
 results=[]
 for q in(399,400):
  Y=[row[:] for row in Y0];a0=qi[(396,0)];aq=qi[(q,0)]
  for j in range(p):Y[a0][j]=cf.add(Y[a0][j],cf.scaled(A[j][aq],8));Y[aq][j]=cf.sub(Y[aq][j],cf.scaled(A[j][a0],8))
  persist({'stage':'source_Y','impurity':q,'Y':Y})
  trace=sumv(cf.mul(cf.mul(Y[a][j],G[a][b]),Y[b][j]) for j in range(p) for a in range(8) for b in range(8))
  persist({'stage':'source_trace_raw','impurity':q,'Y':Y,'G':G,'trace':trace})
  b=root(upper(trace));delta=cf.checked((0,a_upper+b[1]));passed=F(delta[1],iv.S)<=target
  row={'impurity':q,'delta_upper_numerator':delta[1],'denominator':iv.S,'target':str(target),'pass':passed,'a_upper_numerator':a_upper,'b':b};persist({'stage':'bound_complete',**row});results.append(row)
 return {'status':'COMPLETE_SUFFICIENT_UPPER_BOUND','results':results,'queries':len(M),'midpoint_isometry_claim':False,'failure_is_no_go':False}

def native(*a,**k):raise ValueError('NOTREADY: no accepted24 history/DATA/runtime binder')
