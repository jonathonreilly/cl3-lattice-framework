import itertools,json
from collections import defaultdict
# Independent ordered-word Clifford reduction, integer complex arithmetic only.
def norm(word):
 sign=1;w=list(word)
 for j in range(1,len(w)):
  k=j
  while k and w[k]<w[k-1]:w[k],w[k-1]=w[k-1],w[k];sign=-sign;k-=1
 out=[]
 for x,g in itertools.groupby(w):
  if len(list(g))%2:out.append(x)
 return tuple(out),sign
def add(*polys):
 d=defaultdict(complex)
 for p in polys:
  for w,c in p.items():d[w]+=c
 return {w:c for w,c in d.items() if c}
def scale(p,c):return {w:v*c for w,v in p.items() if v*c}
def mul(p,q):
 d=defaultdict(complex)
 for w,c in p.items():
  for v,e in q.items():z,s=norm(w+v);d[z]+=s*c*e
 return {w:c for w,c in d.items() if c}
g=[{(i,):1} for i in range(6)]
# Three blocks with distinct strengths; first two couple a to d through shared center.
K={(1,0):1,(3,0):1,(5,0):2,(0,1):-1,(0,3):-1,(0,5):-2,(2,4):3,(4,2):-3}
def act(p):
 d={}
 for word,c in p.items():
  for j,x in enumerate(word):
   for (y,z),v in K.items():
    if z==x:
     w,s=norm(word[:j]+(y,)+word[j+1:]);d=add(d,{w:1j*c*v*s})
 return d
def kp(p):return scale(act(p),-1j)
a=g[0];d=add(g[1],g[3]);k=kp(a);v=kp(d);z=kp(k);w=kp(v);B=scale(mul(a,d),1j)
def D(p):return add(act(p),mul(B,p))
n=0
for u,V in [(1,0),(0,1),(2,-3),(-5,7)]:
 b=add(scale(d,2j*u),scale(a,V))
 db=add(scale(add(scale(v,-2),scale(a,-4)),u),scale(add(k,scale(d,-1)),1j*V))
 d2=add(scale(add(scale(w,-2),scale(mul(mul(a,d),v),-2),scale(k,-4),scale(d,4)),1j*u),scale(add(scale(z,-1),scale(mul(mul(a,d),k),-1),v,scale(a,2)),V))
 assert D(b)==db;assert D(db)==d2;n+=2
# Independent constant-term convolution of X=6-sum(z_i+z_i^-1).
p={(0,0,0):1};X={(0,0,0):6}
for axis in range(3):
 for s in [-1,1]:q=[0]*3;q[axis]=s;X[tuple(q)]=-1
for target in [6,42,324]:
 q=defaultdict(int)
 for a,c in p.items():
  for b,d in X.items():q[tuple(x+y for x,y in zip(a,b))]+=c*d
 p=q;assert p[(0,0,0)]==target;n+=1
pairs=list(itertools.combinations(range(6),2));edges=[(a,c) for a in pairs for c in pairs if not set(a)&set(c)]
assert len(edges)==90;n+=1
print(json.dumps({'status':'PASS','checks':n,'scope':'independent six-generator Clifford word reduction and exact Laurent walk counts; no physical values'},indent=2))
