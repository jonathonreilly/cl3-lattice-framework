"""Independent literal source table reconstruction. No original data reader."""
import independent as I
from fractions import Fraction as F
SIGS=(('P','P',1,48),('P','P',2,12),('P','O',0,12),('O','P',0,12),('O','O',0,6))
def defects(kind):
 v={(0,1):I.c(0,2),(1,0):I.c(0,-2)}
 if kind=='inner':return {1:v,2:{(0,1):I.c(0,-2),(1,0):I.c(0,2),(1,2):I.c(-1),(2,1):I.c(-1)}}
 if kind=='nominal':return {1:{(0,2):I.c(0,2),(2,0):I.c(0,-2)},2:{(0,1):I.c(0,-2),(1,0):I.c(0,2),(0,3):I.c(-2),(3,0):I.c(-2)},3:v}
 raise ValueError('kind')
def factors(kind):
 if kind=='inner':return(2,2,4),[(0,(0,),1),(1,(0,),1),(2,(0,),1),(0,(0,1),-1),(2,(0,2),-1),(1,(0,1),-1)]
 if kind=='nominal':return(2,2,1,1),[(0,(0,),1),(1,(0,),1),(2,(0,),1),(0,(0,1),-1),(2,(0,2),-1),(3,(3,),2),(1,(0,3),-1)]
 raise ValueError('kind')
def build(radial,kind,left='P',right='P',opposite=1):
 if kind=='inner':mapping,shifts,limit=(0,1,1),(0,0,1),6;left=right;shared=2;opposite=2 if right=='O'else 0
 else:
  if (left,right,opposite)not in {(a,b,c)for a,b,c,_ in SIGS}:raise ValueError('signature')
  mapping,shifts,limit=(0,1,2,0),(0,0,0,1),4;shared=0
 if left not in ('P','O')or right not in ('P','O'):raise ValueError('class')
 def base(n,i,j,projected):
  if i==j==0:q=radial(n)
  elif (i==0)!=(j==0):q=I.ZERO
  else:
   same=2 if i==j else shared;o=(2 if(right if i==1 else left)=='O'else 0)if i==j else opposite
   q=I.mul(I.c(same-o),radial(n))
   if o:q=I.add(q,I.mul(I.c(F(o,6)),radial(n+2)))
  odd=I.ZERO if(i==0)==(j==0)else I.mul(I.c(0,F(-1 if i==0 else 1,3)),radial(n+1))
  if not projected:return q if n%2==0 else odd
  return I.scale(I.add(q,I.scale(odd,-1))if n%2==0 else I.add(odd,I.scale(q,-1)),F(1,2))
 def callback(projected):
  def get(n,i,j):
   if any(type(x)is not int for x in(n,i,j))or not 0<=n<=limit or not 0<=i<len(mapping)or not 0<=j<len(mapping):raise ValueError('table index')
   return I.checked(base(n+shifts[i]+shifts[j],mapping[i],mapping[j],projected))
  return get
 return callback(False),callback(True)
