"""Source-only masked relative Gaussian jets; no native loader or dispatcher."""
from fractions import Fraction as F
from itertools import product
from math import factorial
from functools import lru_cache
import arithmetic as a
MASKS={'pair':(3,3,1),'reflected':(3,3,2)}
WORD_CAP=200000; MATRIX_CAP=576; COUNT_CAP=100000000

def indices(mask):return sorted(product(*(range(x+1)for x in mask)),key=lambda x:(sum(x),x))
def plus(x,y):return tuple(a+b for a,b in zip(x,y))
def minus(x,y):return tuple(a-b for a,b in zip(x,y))
def inside(x,mask):return all(0<=a<=b for a,b in zip(x,mask))
def coefficient(x):
 if max(abs(x.numerator).bit_length(),x.denominator.bit_length())>2048:raise a.Refused('formal coefficient cap')
 return x

def compose(P,Q,mask):
 R={}
 for u,A in P.items():
  for v,B in Q.items():
   w=plus(u,v)
   if not inside(w,mask):continue
   out=R.setdefault(w,{})
   for p,x in A.items():
    for q,y in B.items():out[p+q]=coefficient(out.get(p+q,F(0))+x*y)
   if sum(map(len,R.values()))>WORD_CAP:raise a.Refused('formal word cap')
 return {u:{w:x for w,x in v.items()if x}for u,v in R.items()}

def exponential(variable,degree,letters,scale=1):
 R={}
 for n in range(degree+1):
  alpha=tuple(n if i==variable else 0 for i in range(3))
  R[alpha]={w:F(scale**n,factorial(n))for w in product(letters,repeat=n)}
 return R

def words(kind):
 mask=MASKS[kind];R={}
 for alpha in indices(mask):
  if kind=='pair'and alpha[2]:continue
  R[alpha]={(0,)*sum(alpha):F(1,factorial(alpha[0])*factorial(alpha[1])*factorial(alpha[2]))}
 R=compose(R,exponential(0,3,(0,1),-1),mask)
 if kind=='pair':
  R=compose(R,exponential(2,1,(2,),2),mask)
 else:R=compose(R,exponential(2,2,(0,2),-1),mask)
 R=compose(R,exponential(1,3,(0,2 if kind=='pair'else 1),-1),mask)
 for alpha,row in R.items():
  if sum(alpha)and any(all(z==0 for z in w)for w in row):raise a.Refused('uncancelled free word')
 return R

def box(value):
 if type(value)is not tuple or len(value)!=2:raise a.Refused("complex box shape")
 for part in value:
  if type(part)is not tuple or len(part)!=2 or any(type(x)is not int or abs(x).bit_length()>a.CAP for x in part)or part[0]>part[1]:raise a.Refused("complex box endpoints")
 return value

def tick(c,n=1):
 c['complex_products']+=n
 if c['complex_products']>COUNT_CAP:raise a.Refused('operation cap')
def times(x,y,c):tick(c);return a.mul(x,y)
def addentry(M,key,x):
 a.accum(M,key,x)
 if len(M)>MATRIX_CAP:raise a.Refused('matrix cap')
def sum_matrix(A,B):
 R=dict(A)
 for k,x in B.items():addentry(R,k,x)
 return R

def factor(word,J,D,c):
 pos=[i for i,x in enumerate(word)if x]
 if not pos:raise a.Refused('pure word after cancellation')
 left=pos[0];right=len(word)-pos[-1]-1;M=dict(J[word[pos[0]]])
 for p,q in zip(pos,pos[1:]):
  gap=q-p-1;N={}
  for(i,j),x in M.items():
   for(k,l),y in J[word[q]].items():
    addentry(N,(i,l),times(times(x,D(gap,j,k),c),y,c))
  M=N
 return {(3*left+i,3*right+j):x for(i,j),x in M.items()}

def projected_product(A,C,B,limit,c):
 out={}
 for(i,j),x in A.items():
  for(k,l),y in C.items():
   degree=j//3+k//3
   if degree>limit:raise a.Refused('projected degree')
   addentry(out,(i,l),times(times(x,B(degree,j%3,k%3),c),y,c))
 return out

def trace(A,B,limit,c):
 z=a.ZERO
 for(i,j),x in A.items():
  degree=i//3+j//3
  if degree>limit:raise a.Refused('trace degree')
  z=a.add(z,times(x,B(degree,j%3,i%3),c))
 return z

def jet(kind,J,D,B,emit=lambda *_:None):
 """J: two sparse 3x3 Hermitian coefficient boxes; D/B: inert table callbacks."""
 if kind not in MASKS:raise a.Refused('kind')
 if set(J)!={1,2}:raise a.Refused('defect keys')
 for M in J.values():
  if not M or any(type(i)is not int or type(j)is not int or not 0<=i<3 or not 0<=j<3 for i,j in M):raise a.Refused('source indices')
 mask=MASKS[kind];limit=sum(mask)-2
 for M in J.values():
  for value in M.values():box(value)
 def checked_table(original):
  @lru_cache(None)
  def lookup(n,i,j):
   if type(n)is not int or not 0<=n<=limit or not 0<=i<3 or not 0<=j<3:raise a.Refused('source query bounds')
   return box(original(n,i,j))
  return lookup
 D=checked_table(D);B=checked_table(B);c={'complex_products':0};W=words(kind);A={};ell={};keys=indices(mask)[1:]
 for alpha in keys:
  full={};nonlinear={}
  for w,q in W[alpha].items():
   count=sum(x!=0 for x in w);M=factor(w,J,D,c);qbox=a.point(q.numerator,q.denominator)
   for key,x in M.items():
    y=times(qbox,x,c);addentry(full,key,y)
    if count>=2:addentry(nonlinear,key,y)
  if any(i//3+j//3>sum(alpha)-1 for i,j in full):raise a.Refused("operator support")
  A[alpha]=full
  # Never evaluate the linear trace at total degree >=2.
  ell[alpha]=a.divide(trace(full if sum(alpha)==1 else nonlinear,B,limit,c),2)
  emit('operator_coefficient',{'alpha':alpha,'entries':len(full),'nonlinear_entries':len(nonlinear),'trace':ell[alpha]})
 del W
 prev=A
 for m in range(2,sum(mask)+1):
  curr={}
  for alpha in keys:
   if sum(alpha)<m:continue
   M={}
   for beta in keys:
    gamma=minus(alpha,beta)
    if gamma in prev:M=sum_matrix(M,projected_product(A[beta],prev[gamma],B,limit,c))
   if any(i//3+j//3>sum(alpha)-m for i,j in M):raise a.Refused("log product support")
   curr[alpha]=M
   z=a.divide(trace(M,B,limit,c),2*m)
   ell[alpha]=a.add(ell[alpha],z if m%2 else a.neg(z))
  prev=curr
 Z={(0,0,0):a.point(1)}
 for alpha in keys:
  total=a.ZERO
  for beta in keys:
   gamma=minus(alpha,beta)
   if gamma in Z:total=a.add(total,times(a.point(sum(beta)),times(ell[beta],Z[gamma],c),c))
  Z[alpha]=a.divide(total,sum(alpha));emit('jet_coefficient',{'alpha':alpha,'value':Z[alpha]})
 return Z,c

def shifted_table(base):
 """(a,d,hd) source, exact endpoint shifts; no native scalar evaluation."""
 source=(0,1,1);shift=(0,0,1)
 def table(n,i,j):
  degree=n+shift[i]+shift[j]
  if degree>8:raise a.Refused('fundamental degree')
  return base(degree,source[i],source[j])
 return table
