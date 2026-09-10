from fractions import Fraction as F
from functools import lru_cache
import interval as I
import wick
from degree10 import ra,rm,rd,rn
P=I.point

def opadd(*xs):return[x for y in xs for x in y]
def term(word,c=1,phase=0):return[(tuple(word),wick.phase(c,phase))]
def opscale(x,c):return[(w,wick.cm(a,wick.phase(c)))for w,a in x]
def opmul(x,y):
 if len(x)*len(y)>400:raise ValueError('operator term cap')
 return[(a+b,wick.cm(ac,bc))for a,ac in x for b,bc in y]
def hermitian(x):return[(tuple(reversed(w)),wick.cj(c))for w,c in x]

def local_operators():
 # a,v,z,d,k,w =0,1,2,3,4,5
 O0=term(());O1=term((0,3),1,1)
 O2=opadd(term((),2),term((4,3),-1),term((0,1),-1))
 O3=opadd(opscale(O1,-2),term((0,4),2,1),term((3,1),1,1),term((2,3),-1,1),term((4,1),-2,1),term((0,5),-1,1))
 return[O0,O1,O2,O3],term((3,),2,1),opadd(term((1,),-2),term((0,),-8))

def evaluator(G):
 misses=products=0
 def cm(a,b):
  nonlocal products
  products+=1
  if products>200000:raise ValueError('complex product cap')
  return wick.cm(a,b)
 @lru_cache(maxsize=8192)
 def expect(word):
  nonlocal misses
  misses+=1
  if misses>8192 or len(word)>6:raise ValueError('Wick state/word cap')
  if not word:return wick.phase(1)
  if len(word)%2:return wick.ZERO
  val=wick.ZERO
  for j in range(1,len(word)):
   x=cm(G[word[0]][word[j]],expect(word[1:j]+word[j+1:]));val=wick.ca(val,x if j%2 else wick.cn(x))
  return val
 def mean(op):
  val=wick.ZERO
  for word,c in op:val=wick.ca(val,cm(c,expect(word)))
  return val
 def inner(x,y):return mean(opmul(hermitian(x),y))
 def counts():return {'wick_states':misses,'complex_products':products}
 return mean,inner,counts

def real_moment(value):
 if not value[1][0]<=0<=value[1][1]:raise ValueError('nonreal moment')
 return I.nonnegative(value[0])

def choose3(H,b):
 # Interval LDL proves positive leading Schur pivots; no midpoint PSD inference.
 A=[[x for x in row]for row in H];piv=[]
 for k in range(3):
  pivot=A[k][k]
  if pivot[0]<=0:raise ValueError('uncertified3x3 pivot')
  piv.append(pivot)
  for i in range(k+1,3):
   for j in range(i,3):A[i][j]=I.sub(A[i][j],I.div(I.mul(A[i][k],A[k][j]),pivot));A[j][i]=A[i][j]
 rows=[[I.mid(x)for x in row]+[I.mid(y)]for row,y in zip(H,b)]
 for k in range(3):
  v=rows[k][k]
  if v<=0:raise ValueError('midpoint pivot')
  rows[k]=[rd(x,v)for x in rows[k]]
  for i in range(3):
   if i!=k:
    c=rows[i][k];rows[i]=[ra(x,rn(rm(c,y)))for x,y in zip(rows[i],rows[k])]
 return[dyadic(row[3])for row in rows],piv

def dyadic(x):
 x=I.check(x)
 if abs(x)>2**32:raise ValueError('fixed coefficient magnitude cap')
 s=1<<128;n=(x.numerator*s)//x.denominator
 # Deterministic downward choice, not an assertion of optimizer closeness.
 return I.check(F(n,s))
