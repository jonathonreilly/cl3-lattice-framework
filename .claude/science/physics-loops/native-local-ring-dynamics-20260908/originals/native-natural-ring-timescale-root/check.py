from fractions import Fraction as F
import json,math,time,resource,sys,hashlib
from pathlib import Path
import signal
signal.alarm(30)
start=time.monotonic();checks=0
N=16;order=13
def req(v,m):
 global checks
 checks+=1
 if not v:raise RuntimeError(m)
def add(a,b,scale=F(1)):
 c=a.copy()
 for k,v in b.items():
  c[k]=c.get(k,F(0))+scale*v
  if c[k]==0:del c[k]
 return c
def mul(a,b):
 c={};rows={}
 for (k,j),v in b.items():rows.setdefault(k,[]).append((j,v))
 for (i,k),u in a.items():
  for j,v in rows.get(k,[]):c[(i,j)]=c.get((i,j),F(0))+u*v
 return {k:v for k,v in c.items() if v}
def pcomm(a,b):
 c=[{} for _ in range(order+1)]
 for n in range(order+1):
  for i in range(n+1):c[n]=add(c[n],add(mul(a[i],b[n-i]),mul(b[n-i],a[i]),F(-1)))
 return c
def transformed(s,h):
 out=[d.copy() for d in h];term=h
 for k in range(1,order+1):
  term=pcomm(s,term)
  for n in range(order+1):out[n]=add(out[n],term[n],F(1,math.factorial(k)))
 return out
bits=(0,1,0,1);inc=((0,3),(0,1),(1,2),(2,3));masks=(0,1,2,5)
energy=[]
for m in range(N):
 delta=[(bits[e]^(m>>e&1))-bits[e] for e in range(4)]
 energy.append(sum((delta[a]+delta[b])**2 for a,b in inc))
ice=[m for m,d in enumerate(energy) if d==0];req(ice==[0,15],'rank two ice')
d={(i,i):F(e) for i,e in enumerate(energy) if e};v={}
for m in range(N):
 for e in range(4):v[(m^(1<<e),m)]=F((-1)**((m&masks[e]).bit_count()))
h=[d,v]+[{} for _ in range(order-1)];s=[{} for _ in range(order+1)];coeff=[]
for j in range(1,order+1):
 r=transformed(s,h)[j]
 s[j]={(a,b):value/(energy[a]-energy[b]) for (a,b),value in r.items() if energy[a]!=energy[b]}
 req(all(s[j].get((b,a),F(0))==-value for (a,b),value in s[j].items()),'antihermitian generator')
 full=transformed(s,h)
 for n in range(1,j+1):req(all(energy[a]==energy[b] for a,b in full[n]),'all D-offdiagonal cancelled')
 coeff.append(full[j])
def restrict(a):return {(i,j):value for (i,j),value in a.items() if i in ice and j in ice}
p={(i,i):F(1) for i in ice};r={(i,i):F(1,e) for i,e in enumerate(energy) if e}
second=mul(mul(mul(p,v),r),mul(v,p));req(restrict(coeff[1])=={k:-val for k,val in second.items()},'second resolvent coefficient')
word=p
for mat in (v,r,v,r,v,r,v,p):word=mul(word,mat)
reference=add({k:-val for k,val in word.items()},p,F(2))
req(restrict(coeff[3])==reference,'fourth folded resolvent coefficient')
for j in range(0,order,2):req(restrict(coeff[j])=={},'odd ice vanishes')
req(restrict(coeff[3])!={k:-val for k,val in word.items()},'missing folded actual negative control')
swrong=[{} for _ in range(order+1)];swrong[1]={k:-val for k,val in s[1].items()};wrong=transformed(swrong,h)
req(any(energy[a]!=energy[b] for a,b in wrong[1]),'wrong inverse sign actual negative control')
# Exact coefficient recursion for the independent conservative root norm constants.
def exppoly(poly,n):
 out=[F(0)]*(n+1);out[0]=F(1)
 for k in range(1,n+1):out[k]=sum(F(j)*poly[j]*out[k-j] for j in range(1,k+1))/k
 return out
ss=[];rr=[]
for j in range(1,order+1):
 poly=[F(0)]*(j+1)
 for i,si in enumerate(ss,1):poly[i]=112*j*si
 exp=exppoly(poly,j);rj=2916*exp[j]+216513*exp[j-1];rr.append(rj);ss.append(4*rj)
 req(rj>0 and ss[-1]>0,'positive finite majorant')
radius=min(F(1),F(1,224)/sum(ss));M=2*(2916+216513)
req(sum(ss[j-1]*radius**j for j in range(1,order+1))<=F(1,224),'Lie convergence radius')
req(2*M/radius**14>0,'positive Cauchy constant')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
req(time.monotonic()-start<30 and rss<384,'resources')
print(json.dumps(dict(checks=checks,ice=ice,ice_fourth={str(k):str(val) for k,val in reference.items()},r_majorants=list(map(str,rr)),s_majorants=list(map(str,ss)),radius=str(radius),radius_approx=float(radius),M=M,log10_C=math.log10(2*M)-14*math.log10(float(radius)),seconds=time.monotonic()-start,rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2))
