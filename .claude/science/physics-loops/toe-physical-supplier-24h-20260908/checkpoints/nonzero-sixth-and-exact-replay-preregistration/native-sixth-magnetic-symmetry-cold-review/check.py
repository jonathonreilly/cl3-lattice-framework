from itertools import product,combinations
from pathlib import Path
import json,time,signal
signal.alarm(180);t=time.monotonic();V=list(product(range(4),repeat=3));I={v:i for i,v in enumerate(V)};K={}
for x in V:
 for d in range(3):
  y=list(x);y[d]=(y[d]+1)%4;i,j=sorted((I[x],I[tuple(y)]));s=-2*(-1)**sum(x[:d]);K[i,j]=s;K[j,i]=-s
class UF:
 def __init__(self,n):self.p=list(range(n));self.s=[1]*n;self.bad=set()
 def find(self,x):
  if self.p[x]!=x:
   p,s=self.find(self.p[x]);self.s[x]*=s;self.p[x]=p
  return self.p[x],self.s[x]
 def join(self,a,b,z):
  ra,sa=self.find(a);rb,sb=self.find(b)
  if ra==rb:
   if sa!=z*sb:self.bad.add(ra)
  else:
   bad=ra in self.bad or rb in self.bad;self.p[ra]=rb;self.s[ra]=z*sb*sa
   if bad:self.bad.add(rb)
pairs=[p for p in combinations(range(64),2) if (sum(V[p[0]])+sum(V[p[1]]))%2];idx={p:i for i,p in enumerate(pairs)};u=UF(len(pairs));checks=0
for kind,d in [('t',i) for i in range(3)]+[('r',i) for i in range(3)]+[('s',0),('s',1)]:
 f=[]
 for x in V:
  y=list(x)
  if kind=='t':y[d]=(y[d]+1)%4
  elif kind=='r':y[d]=-y[d]%4
  else:y[d],y[d+1]=y[d+1],y[d]
  f.append(I[tuple(y)])
 g=UF(64)
 for (a,b),v in K.items():g.join(a,b,K[f[a],f[b]]//v)
 if any(g.find(r)[0] in g.bad for r in range(64)):raise ValueError('inconsistent lift')
 signs=[g.find(i)[1] for i in range(64)]
 for (a,b),v in K.items():
  if K[f[a],f[b]]!=signs[a]*signs[b]*v:raise ValueError('covariance')
  checks+=1
 for k,(a,b) in enumerate(pairs):
  c,d=f[a],f[b];u.join(k,idx[tuple(sorted((c,d)))],signs[a]*signs[b]*(1 if c<d else -1));checks+=1
orbits={}
for k,(a,b) in enumerate(pairs):
 r,s=u.find(k);row=orbits.setdefault(r,dict(size=0,forced_zero=r in u.bad,distances=set()));row['size']+=1;row['distances'].add(sum(min(abs(x-y),4-abs(x-y)) for x,y in zip(V[a],V[b])))
rows=[dict(**{k:v for k,v in x.items() if k!='distances'},distances=sorted(x['distances'])) for x in orbits.values()]
if sorted((x['size'],x['forced_zero']) for x in rows)!=[(192,False),(192,True),(256,True),(384,True)]:raise ValueError(rows)
Path(__file__).with_name('RESULT.json').write_text(json.dumps(dict(checks=checks,orbits=rows,seconds=time.monotonic()-t),indent=2)+'\n')
