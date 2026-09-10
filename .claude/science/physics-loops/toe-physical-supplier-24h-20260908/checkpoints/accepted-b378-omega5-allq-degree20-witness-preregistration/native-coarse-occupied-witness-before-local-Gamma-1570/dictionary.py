"""Literal seven-star real rephased overlap matrices; pure scalar algebra."""
from fractions import Fraction as F
from functools import lru_cache
from interval import add,mul,neg,const,inv

def sub(a,b):return add(a,neg(b))
def scale(a,x):return mul(a,const(x))
I=[[int(i==j) for j in range(7)] for i in range(7)]
O=[[int(i>0 and j>0 and (i-1)//2==(j-1)//2 and i!=j) for j in range(7)] for i in range(7)]
T=[[0]*7 for _ in range(7)]
for j in range(1,7):T[0][j]=-((-1)**(j+1));T[j][0]=-T[0][j]
N=[[I[i][j]+O[i][j] for j in range(7)] for i in range(7)]
@lru_cache(maxsize=900)
def pole(s,sigma,A,B):
 s=const(F(s));ss=mul(s,s);d=scale(sub(const(1),mul(ss,A)),F(1,6))
 C=[];L=[]
 for i in range(7):
  cr=[];lr=[]
  for j in range(7):
   cr.append(add(scale(mul(s,add(scale(A,I[i][j]),scale(sub(A,d),O[i][j]))),sigma),scale(d,T[i][j])))
   lr.append(add(add(scale(B,-I[i][j]),scale(mul(add(const(1),scale(ss,F(1,6))),B),-O[i][j])),scale(mul(s,B),F(sigma*T[i][j],6))))
  C.append(cr);L.append(lr)
 return C,L

def local_append(source,c,mu):
 # source is e0 for bare center, or signed neighbor d for Ward.
 if source==[1,0,0,0,0,0,0]:
  g=[const(F(int(v==0),2)) for v in range(7)]
  j=[scale(mu,F(T[0][v],12)) for v in range(7)]
 else:
  tk=[sum(source[k]*T[k][v] for k in range(7)) for v in range(7)]
  nk=[sum(source[k]*N[k][v] for k in range(7)) for v in range(7)]
  ok=[sum(source[k]*O[k][v] for k in range(7)) for v in range(7)]
  g=[const(F(x,12)) for x in tk]
  j=[scale(sub(scale(mu,F(ok[v],6)),scale(c,nk[v])),F(1,2)) for v in range(7)]
 return g,j
