"""Sparse192 coefficient and signed-action design. No native loader/import work."""
from fractions import Fraction as F
import interval as iv
BITS=320
MAGNITUDE=2**40
COEFFICIENT_WIDTH=iv.S//2**39 # midpoint radius <=2^-40
class Indeterminate(ValueError):pass

def checked(x):
 if len(x)!=2 or any(type(t)is not int for t in x) or x[0]>x[1]:raise ValueError('integer interval')
 if max(abs(t).bit_length() for t in x)>BITS:raise Indeterminate('endpoint bit cap320')
 return tuple(x)
def add(x,y):return checked(iv.add(x,y))
def mul(x,y):return checked(iv.mul(x,y))
def neg(x):return checked(iv.neg(x))
def sub(x,y):return add(x,neg(y))
def div(x,y):
 checked(y)
 if y[0]<=0:raise Indeterminate('pivot denominator not strictly positive')
 return checked(iv.div(x,y))
def scaled(x,t):return checked(iv.scale(x,t))
def put(v,key,x):
 if not isinstance(key,tuple) or len(key)!=2 or type(key[0])is not int or not 0<=key[0]<402 or key[1] not in (0,1):raise ValueError('coordinate')
 x=checked(x)
 if x!=iv.ZERO:v[key]=x
 else:v.pop(key,None)
def gamma(v):
 out={}
 for (r,g),x in v.items():put(out,(r,1-g),neg(x) if g else x)
 return out

def combine(v,w,t):
 out=dict(v)
 for key,x in w.items():put(out,key,add(out.get(key,iv.ZERO),mul(x,t)))
 return out

def seed(index):
 if type(index)is not int or not 0<=index<399:raise ValueError('half label')
 if index>=396:return {(index,0):iv.ONE}
 n,rest=divmod(index,6);source,par=divmod(rest,2);eta=(-1,1)[par];chi=1 if source==0 else -1
 return {(6*n+3+source,0):iv.rational(F(1,2)),(6*n+source,0):iv.rational(F(-eta*chi,2))}

def coefficients(history,persist,*,seed_map=None,label_count=399):
 """History must be authenticated exact physical rows externally. No row replay."""
 if len(history)>4:raise ValueError('four-pair cap')
 native=seed_map is None;getseed=seed if native else lambda i:seed_map[i]
 beta=[];columns=[];indices=[];R=set()
 for h,row in enumerate(history):
  i=row['index'];persist({'stage':'coefficient','pair':h,'index':i})
  if type(i)is not int or not 0<=i<label_count or i in indices:raise ValueError('selected index')
  if len(row['g'])!=label_count or len(row['j'])!=label_count:raise ValueError('history row length')
  r=checked(row['r'])
  if r[0]<=0:raise Indeterminate('nonpositive pivot lower bound')
  s={key:checked(x) for key,x in getseed(i).items()}
  if native and any(key[0]>=399 for key in s):raise ValueError('original F domain')
  R.update(s);R.update(gamma(s));v=s
  for a,old in enumerate(history[:h]):
   rr=checked(old['r']);g=checked(old['g'][i]);j=checked(old['j'][i])
   v=combine(v,beta[a],neg(div(g,rr)));v=combine(v,gamma(beta[a]),div(j,rr))
  if not set(v)<=R or len(R)>4*(h+1):raise ValueError('sparse recurrence support')
  magnitude=sum(max(abs(x[0]),abs(x[1])) for x in v.values())
  if magnitude>MAGNITUDE*iv.S:raise Indeterminate('beta l1 exceeds2^40')
  c={key:div(x,checked(iv.sqrt(r))) for key,x in v.items()}
  maxwidth=max((x[1]-x[0] for x in c.values()),default=0)
  cmag=sum(max(abs(x[0]),abs(x[1])) for x in c.values())
  persist({'stage':'coefficient_enclosed','pair':h,'beta':encode(v),'column':encode(c),'maximum_width':maxwidth,'l1_upper_numerator':cmag})
  if maxwidth>COEFFICIENT_WIDTH or cmag>MAGNITUDE*iv.S:raise Indeterminate('coefficient conditioning: width or l1')
  beta.append(v);columns.extend((c,gamma(c)));indices.append(i)
 return columns,tuple(sorted(R))

def encode(v):return [[r,g,*x] for (r,g),x in sorted(v.items())]
Q=((396,0),(399,0),(400,0),(401,0),(396,1),(399,1),(400,1),(401,1))

def free(v,poles,alpha):
 out={}
 def accumulate(key,x):put(out,key,add(out.get(key,iv.ZERO),x))
 for (r,g),x in v.items():
  if r>=399:raise ValueError('action domain restricted to ORIGINAL F')
  if r<396:
   n,t=divmod(r,6);sigma=-1 if t<3 else 1;source=t%3
   s=checked(poles[n]);a=checked(alpha[n])
   if s[0]<=0 or a[0]<=0:raise ValueError('positive physical pole/alpha enclosure')
   accumulate((r,g),scaled(mul(x,s),sigma))
   target=(396,399,400)[source]
   accumulate((target,g),scaled(mul(x,checked(iv.sqrt(a))),-2))
  else:accumulate(((401,399,400)[r-396],g),x)
 return out

def dotM(v,w,M):
 total=iv.ZERO
 for i,x in v.items():
  for j,y in w.items():total=add(total,mul(mul(x,M[i,j]),y))
 return total

def intersect(x,y):
 z=(max(x[0],y[0]),min(x[1],y[1]))
 if z[0]>z[1]:raise Indeterminate('empty proved symmetry/PSD intersection')
 return z

def action(columns,R,entry,poles,alpha,persist,*,leakage_target=F(1,10**6)):
 """entry returns SAME physical DATA Gram interval; midpoint isometry not used."""
 if len(columns)>8 or len(R)>16 or any(k[0]>=399 for k in R):raise ValueError('original sparse support')
 if any(not set(c)<=set(R) for c in columns):raise ValueError('column support')
 if len(poles)!=66 or len(alpha)!=66:raise ValueError('physical scalar enclosure census')
 U=tuple(sorted(set(R)|set(Q)))
 if len(U)>24:raise ValueError('U support')
 M={}
 for a,i in enumerate(U):
  for j in U[a:]:
   persist({'stage':'data_entry','row':i,'column':j});x=checked(entry(i,j));M[i,j]=M[j,i]=x
 persist({'stage':'principal_gram_complete','U':U,'entries':[[*i,*j,*M[i,j]] for a,i in enumerate(U) for j in U[a:]]})
 allresults=[]
 for qraw in (399,400):
  images=[]
  for c in columns:
   b=free(c,poles,alpha)
   u=dotM({(qraw,0):iv.ONE},c,M);v=dotM({(396,0):iv.ONE},c,M)
   b=combine(b,{(396,0):iv.ONE},scaled(u,8));b=combine(b,{(qraw,0):iv.ONE},scaled(v,-8))
   if not set(b)<=set(U):raise ValueError('first action support')
   images.append(b)
  m=len(columns);T=[[dotM(c,b,M) for b in images] for c in columns]
  # T represents K, not H. Exact skew symmetry permits these intersections.
  for i in range(m):
   T[i][i]=intersect(T[i][i],iv.ZERO)
   for j in range(i+1,m):
    z=intersect(T[i][j],neg(T[j][i]));T[i][j]=z;T[j][i]=neg(z)
  G=[[dotM(a,b,M) for b in images] for a in images]
  L=[[add(G[i][j],sum_iv(mul(T[i][a],T[a][j]) for a in range(m))) for j in range(m)] for i in range(m)]
  for i in range(m):
   L[i][i]=intersect(L[i][i],(0,max(0,L[i][i][1])))
   for j in range(i+1,m):L[i][j]=L[j][i]=intersect(L[i][j],L[j][i])
  bound=max((sum(max(abs(x[0]),abs(x[1])) for x in row) for row in L),default=0)
  row={'impurity_bare_index':qraw,'T':T,'L':L,'delta_squared_upper_numerator':bound,'denominator':iv.S,'leakage_target':str(leakage_target),'leakage_pass':F(bound,iv.S)<=leakage_target**2,'columns':[encode(c) for c in columns],'action_columns':[encode(b) for b in images]}
  persist({'stage':'action_enclosed',**row});allresults.append(row)
 return {'status':'COMPLETE_CONDITIONAL_ACTION_ENCLOSURE','R':R,'U':U,'results':allresults,'midpoint_isometry_claim':False}

def sum_iv(xs):
 total=iv.ZERO
 for x in xs:total=add(total,x)
 return total

def native(*args,**kwargs):raise ValueError('NOTREADY: no authenticated physical history/DATA/scalar loader')
