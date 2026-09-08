import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import itertools,json,time,signal,resource,sys
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
signal.alarm(180);start=time.monotonic();count=0
def req(x,m):
 global count
 count+=1
 if not x:raise RuntimeError(m)
def comps(total,length,bound):
 if length==0:
  if total==0:yield ()
  return
 for i in range(1,min(total,bound)+1):
  for rest in comps(total-i,length-1,bound):yield(i,)+rest
f={};s={}
for n in range(1,6):
 v=F(0)
 for l in range(2,n+1):
  for c in comps(n,l,n-1):
   t=F(18);p=0
   for i in c:p+=i;t*=2*(6+11*p)*s[i]
   v+=t/F(sp.factorial(l))
 for l in range(n):
  for c in comps(n-1,l,n-1):
   t=F(11);p=0
   for i in c:p+=i;t*=22*(1+p)*s[i]
   v+=t/F(sp.factorial(l))
 f[n]=v;s[n]=4*v;req(v>0,'positive recursive majorant')
rho=F(1,440*3**55*max(1,sum(s.values())));M=2*(18*3**6+11*3**11)
req(110*3**55*rho*sum(s.values())<=F(1,4),'Lie radius')
req(sum(F(1,2)**n for n in range(6,80))<2*F(1,2)**6,'Cauchy tail')
# Actual three-edge full-carrier forest, fixed exterior alternating ice.
ends=[(0,1),(1,2),(2,3)];bits=[0,1,0];ener=[]
for z in range(8):
 delta=[0]*4
 for e,(a,b) in enumerate(ends):
  if z>>e&1:delta[a]+=1-2*bits[e];delta[b]+=1-2*bits[e]
 ener.append(sum(d*d for d in delta))
D=sp.diag(*ener);V=sp.zeros(8)
for z in range(8):
 for e in range(3):V[z^(1<<e),z]=(-1)**((z&(1<<(e-1))).bit_count()) if e else 1
req(V==V.T,'native Hermitian');req(ener.count(0)==1,'unique forest ice')
Z=sp.diag(*[(-1)**z.bit_count() for z in range(8)]);req(Z*V*Z==-V,'bit parity')
zero=sp.zeros(8)
def comm(a,b):
 out={}
 for i,A in a.items():
  for j,B in b.items():
   if i+j<=5:out[i+j]=out.get(i+j,zero)+A*B-B*A
 return out
def transform(S):
 out={0:D,1:V};term=out.copy()
 for l in range(1,6):
  term=comm(S,term)
  for n,A in term.items():out[n]=out.get(n,zero)+A/sp.factorial(l)
 return out
S={};ks={}
for n in range(1,6):
 Fn=transform(S).get(n,zero);Sn=sp.zeros(8);Kn=sp.zeros(8)
 for a in range(8):
  for b in range(8):
   if ener[a]!=ener[b]:Sn[a,b]=Fn[a,b]/(ener[a]-ener[b])
   else:Kn[a,b]=Fn[a,b]
 req(Sn.T==-Sn,'anti-Hermitian inverse');req(Sn*D-D*Sn==Kn-Fn,'homological sign');S[n]=Sn;ks[n]=Kn
actual=transform(S)
for n in range(1,6):req(actual[n]==ks[n],'exact transformed coefficient');req(D*ks[n]==ks[n]*D,'D conservation');req(Z*S[n]*Z==(-1)**n*S[n],'generator grading')
req([ks[n][0,0] for n in (1,3,5)]==[0,0,0],'odd ice');req(ks[2][0,0]==-sp.Rational(3,2),'ice second');req(ks[4][0,0]==sp.Rational(7,8),'ice fourth canonical')
wrong=transform({1:-S[1]})[1];req(D*wrong!=wrong*D,'opposite inverse sign adverse')
req(0<resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)<384 and time.monotonic()-start<180,'resource cap')
out=dict(checks=count,f={k:str(v) for k,v in f.items()},s={k:str(v) for k,v in s.items()},rho=str(rho),M=M,C_R=str(2*M/rho**6),forest_D=ener,ice_coefficients={k:str(v[0,0]) for k,v in ks.items()},seconds=time.monotonic()-start,scope='Exact finite algebra/majorant controls, not numerical validation of infinite-volume dynamics or a useful coupling onset.')
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(count)
