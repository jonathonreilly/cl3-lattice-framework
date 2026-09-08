import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import signal,time,resource,sys,json,hashlib
signal.alarm(30);start=time.monotonic()
import sympy as sp
from pathlib import Path
x=sp.symbols('x',real=True);N=4;checks=0
D=sp.diag(0,2);V=sp.Matrix([[0,1],[1,0]]);zero=sp.zeros(2)
def req(a,m):
 global checks
 checks+=1
 if not a:raise RuntimeError(m)
def clean(m):return m.applyfunc(sp.expand)
def pcomm(a,b):
 out={}
 for i,A in a.items():
  for j,B in b.items():
   if i+j<=N:out[i+j]=clean(out.get(i+j,zero)+A*B-B*A)
 return out
def transform(S,f,sign=1):
 out={0:D,1:f*V};term=out.copy()
 for k in range(1,N+1):
  term=pcomm(S,term)
  for j,A in term.items():out[j]=clean(out.get(j,zero)+A/sp.factorial(k))
 term={j+1:A.diff(x) for j,A in S.items() if j+1<=N}
 for k in range(N):
  for j,A in term.items():out[j]=clean(out.get(j,zero)+sign*sp.I*A/sp.factorial(k+1))
  term=pcomm(S,term)
 return out
def solve(f,sign=1):
 S={};K={}
 for n in range(1,N+1):
  F=transform(S,f,sign).get(n,zero);Sn=sp.zeros(2);Kn=sp.zeros(2)
  for a in range(2):
   for b in range(2):
    if a==b:Kn[a,b]=F[a,b]
    else:Sn[a,b]=F[a,b]/(D[a,a]-D[b,b])
  S[n]=clean(Sn);K[n]=clean(Kn)
 return S,K
base=sp.expand(x**N*(1-x)**N);f=sp.integrate(base,(x,0,x))/sp.integrate(base,(x,0,1))
S,K=solve(f);actual=transform(S,f);static,_=solve(sp.Integer(1))
for n in range(1,N+1):
 req(clean(S[n]+S[n].conjugate().T)==zero,'antihermitian')
 req(clean(actual[n]-K[n])==zero,'coefficient matches')
 req(clean(D*K[n]-K[n]*D)==zero,'D conservation')
 req(clean(actual[n]-actual[n].conjugate().T)==zero,'Hermitian moving generator')
 req(S[n].subs(x,0)==zero,'start identity')
 req(clean(S[n].subs(x,1)-static[n])==zero,'exact static endpoint')
wrong,_=solve(f,sign=-1);bad=transform(wrong,f,sign=1)
req(clean(D*bad[2]-bad[2]*D)!=zero,'wrong derivative sign adverse')
req(clean(K[2]-sp.diag(-f*f/2,f*f/2))==zero,'instantaneous second scalar')
base14=sp.expand(x**14*(1-x)**14);f14=sp.integrate(base14,(x,0,x))/sp.integrate(base14,(x,0,1))
req(f14.subs(x,0)==0 and f14.subs(x,1)==1,'normalized beta14')
for j in range(1,15):req(sp.diff(f14,x,j).subs(x,0)==0 and sp.diff(f14,x,j).subs(x,1)==0,'flat endpoint')
req((14+1)-1-9==5,'ramp backward cone exponent')
req((14+1)-4-9==2,'hold backward cone exponent')
req(6-4==2,'slow ring correction exponent')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(time.monotonic()-start<30 and rss<384,'resources')
print(json.dumps(dict(checks=checks,N=N,f=str(sp.expand(f)),first_generators={str(n):str(S[n]) for n in (1,2)},seconds=time.monotonic()-start,rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='exact symbolic finite controls; not an independent proof of uniform local many-body preparation'),indent=2))
