"""Independent Fraction endpoint evaluation, quantized outward after each primitive."""
from fractions import Fraction as F
from math import isqrt
S=1<<192
Z=(0,0)
def demand(x,m):
 if not x:raise ValueError(m)
def box(x):
 demand(len(x)==2 and all(type(v)is int for v in x) and x[0]<=x[1],'interval');return tuple(x)
def roundq(x):return x.numerator//x.denominator,-((-x.numerator)//x.denominator)
def q(x):a,b=roundq(F(x)*S);return a,b
def op(a,b,which):
 a=box(a);b=box(b)
 if which=='div':demand(b[0]>0,'positive divisor')
 vals=[{'mul':lambda:F(x*y,S),'div':lambda:F(x*S,y),'add':lambda:F(x+y)}[which]() for x in a for y in b]
 return roundq(min(vals))[0],roundq(max(vals))[1]
def plus(a,b):return op(a,b,'add')
def times(a,b):return op(a,b,'mul')
def divide(a,b):return op(a,b,'div')
def minus(a):return -a[1],-a[0]
def scale(a,c):return times(a,q(c))
def root(a):
 demand(a[0]>=0,'sqrt');l=isqrt(a[0]*S);u=isqrt(a[1]*S);return l,u+(u*u<a[1]*S)
def intersect(a,b):c=max(a[0],b[0]),min(a[1],b[1]);demand(c[0]<=c[1],'empty intersection');return c
def acc(v,k,x):
 v[k]=plus(v.get(k,Z),x)
 if v[k]==Z:del v[k]
def gamma(v):return {(r,1-g):minus(x) if g else x for (r,g),x in v.items()}
def encode(v):return [[*k,*v[k]] for k in sorted(v)]
def combine(v,w,t):
 v=dict(v)
 for k,x in w.items():acc(v,k,times(x,t))
 return v
def seed(i):
 if i>=396:return {(i,0):q(1)}
 n,z=divmod(i,6);a,p=divmod(z,2);eta=2*p-1;chi=1 if a==0 else -1
 return {(6*n+3+a,0):q(F(1,2)),(6*n+a,0):q(F(-eta*chi,2))}
def coefficients(hist,emit):
 bet=[];cols=[];R=set()
 for h,row in enumerate(hist):
  i=row['index'];v=seed(i);R.update(v);R.update(gamma(v));emit('coefficient',{'pair':h,'index':i})
  for j,old in enumerate(hist[:h]):
   v=combine(v,bet[j],minus(divide(old['g'][i],old['r'])));v=combine(v,gamma(bet[j]),divide(old['j'][i],old['r']))
  c={k:divide(x,root(row['r'])) for k,x in v.items()};width=max((x[1]-x[0] for x in c.values()),default=0);mag=sum(max(map(abs,x)) for x in c.values())
  emit('coefficient_enclosed',{'pair':h,'beta':encode(v),'column':encode(c),'maximum_width':width,'l1_upper_numerator':mag})
  demand(width<=S//2**39 and mag<=2**40*S,'conditioning');bet.append(v);cols.extend((c,gamma(c)))
 return cols,tuple(sorted(R))
def inner(v,w,M):
 t=Z
 for i,x in v.items():
  for j,y in w.items():t=plus(t,times(times(x,M[i,j]),y))
 return t
def images(cols,M,poles,alpha,imp):
 out=[]
 for c in cols:
  v={}
  for (r,g),x in c.items():
   demand(r<399,'original F domain')
   if r<396:
    n,t=divmod(r,6);a=t%3;acc(v,(r,g),scale(times(x,q(poles[n])),-1 if t<3 else 1));acc(v,((396,399,400)[a],g),scale(times(x,root(q(alpha[n]))),-2))
   else:acc(v,((401,399,400)[r-396],g),x)
  v=combine(v,{(396,0):q(1)},scale(inner({(imp,0):q(1)},c,M),8));v=combine(v,{(imp,0):q(1)},scale(inner({(396,0):q(1)},c,M),-8));out.append(v)
 return out
def action(cols,M,poles,alpha,imp,emit):
 bs=images(cols,M,poles,alpha,imp);n=len(cols);T=[[inner(c,b,M) for b in bs] for c in cols];emit('T_raw',{'impurity_bare_index':imp,'T':T})
 for i in range(n):
  T[i][i]=intersect(T[i][i],Z)
  for j in range(i+1,n):T[i][j]=intersect(T[i][j],minus(T[j][i]));T[j][i]=minus(T[i][j])
 G=[[inner(a,b,M) for b in bs] for a in bs];emit('G_action',{'impurity_bare_index':imp,'G':G});L=[]
 for i in range(n):
  row=[]
  for j in range(n):
   t=Z
   for a in range(n):t=plus(t,times(T[i][a],T[a][j]))
   row.append(plus(G[i][j],t))
  L.append(row)
 emit('L_raw',{'impurity_bare_index':imp,'L':L})
 for i in range(n):
  L[i][i]=intersect(L[i][i],(0,max(0,L[i][i][1])))
  for j in range(i+1,n):L[i][j]=L[j][i]=intersect(L[i][j],L[j][i])
 bound=max(sum(max(map(abs,x)) for x in row) for row in L)
 return {'impurity_bare_index':imp,'T':T,'G':G,'L':L,'delta_squared_upper_numerator':bound,'denominator':S,'leakage_target':'1/1000000','leakage_pass':F(bound,S)<=F(1,10**12),'columns':[encode(c) for c in cols],'action_columns':[encode(b) for b in bs]}
