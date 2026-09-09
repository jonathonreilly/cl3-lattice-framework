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
 if len(history)>24:raise ValueError('twenty-four-pair source-design cap')
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
