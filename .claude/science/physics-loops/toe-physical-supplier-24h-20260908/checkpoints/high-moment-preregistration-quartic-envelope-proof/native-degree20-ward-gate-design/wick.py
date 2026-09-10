"""Finite six-vector interval Wick algebra. No data loader or native calls."""
from fractions import Fraction as F
from functools import lru_cache
import interval as I
from degree10 import ra,rm,rn
P=I.point
ZERO=(P(0),P(0))

def ca(a,b):return(I.add(a[0],b[0]),I.add(a[1],b[1]))
def cn(a):return(I.neg(a[0]),I.neg(a[1]))
def cm(a,b):return(I.sub(I.mul(a[0],b[0]),I.mul(a[1],b[1])),I.add(I.mul(a[0],b[1]),I.mul(a[1],b[0])))
def cj(a):return(a[0],I.neg(a[1]))
def phase(value,p=0):return(P(value),P(0))if p==0 else(P(0),P(value))

def table(c,nu,omega5,kind):
 if kind=='P':L2,L4,ed,ed3=12,84,I.scale(c,6),I.scale(nu,2)
 elif kind=='O':L2,L4,ed,ed3=14,108,I.scale(nu,F(1,3)),I.scale(omega5,F(1,3))
 else:raise ValueError('class')
 # labels0=a,1=v,2=z (white);3=d,4=k,5=w (black).
 white=[[1,-2,-6],[-2,L2,14],[-6,14,42]];black=[[2,2,-L2],[2,6,-14],[-L2,-14,L4]]
 cov=[[I.neg(c),I.scale(c,-3),I.scale(nu,F(1,3))],[ed,I.scale(nu,F(1,3)),I.neg(ed3)],[I.scale(nu,F(1,3)),nu,I.scale(omega5,F(-1,3))]]
 G=[[ZERO for _ in range(6)]for _ in range(6)]
 for i in range(3):
  for j in range(3):
   G[i][j]=(P(white[i][j]),P(0));G[i+3][j+3]=(P(black[i][j]),P(0))
   G[i][j+3]=(P(0),cov[i][j]);G[j+3][i]=(P(0),I.neg(cov[i][j]))
 return G

def sources(u,V):
 b=[((3,),phase(rm(2,u),1)),((0,),phase(V))]
 Db=[((1,),phase(rm(-2,u))),((0,),phase(rm(-4,u))),((4,),phase(V,1)),((3,),phase(rn(V),1))]
 D2b=[((5,),phase(rm(-2,u),1)),((0,3,1),phase(rm(-2,u),1)),((4,),phase(rm(-4,u),1)),((3,),phase(rm(4,u),1)),((2,),phase(rn(V))),((0,3,4),phase(rn(V))),((1,),phase(V)),((0,),phase(rm(2,V)))]
 return b,Db,D2b

def source_moments(G,source,emit):
 calls=0
 @lru_cache(maxsize=4096)
 def expect(word):
  nonlocal calls
  calls+=1
  if calls>4096 or len(word)>6 or any(type(i)is not int or not 0<=i<6 for i in word):raise ValueError('finite Wick cap')
  if not word:return phase(1)
  if len(word)%2:return ZERO
  result=ZERO
  for j in range(1,len(word)):
   term=cm(G[word[0]][word[j]],expect(word[1:j]+word[j+1:]))
   result=ca(result,term if j%2 else cn(term))
  return result
 def inner(x,y):
  result=ZERO
  for a,ac in x:
   for b,bc in y:result=ca(result,cm(cm(cj(ac),bc),expect(tuple(reversed(a))+b)))
  return result
 b,Db,D2b=source;values=[]
 for index,(x,y)in enumerate([(b,b),(b,Db),(Db,Db),(Db,D2b),(D2b,D2b)]):
  value=inner(x,y);emit('wick_moment_raw',{'index':index,'real':value[0],'imaginary':value[1],'cache_misses':calls})
  if not value[1][0]<=0<=value[1][1]:raise ValueError('nonreal source moment')
  values.append(I.nonnegative(value[0]))
 return values,calls
