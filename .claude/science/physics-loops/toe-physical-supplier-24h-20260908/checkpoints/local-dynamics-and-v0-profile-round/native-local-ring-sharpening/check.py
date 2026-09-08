from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json,time
start=time.monotonic();checks=0
def req(x,m):
 global checks
 checks+=1
 if not x:raise RuntimeError(m)
def comps(n,l):
 if l==0:
  if n==0:yield()
  return
 for i in range(1,n+1):
  for t in comps(n-i,l-1):yield(i,)+t
f={};s={}
for n in range(1,6):
 v=F(0)
 for l in range(2,n+1):
  for c in comps(n,l):
   t=2*f[c[0]];p=c[0]
   for i in c[1:]:p+=i;t*=22*p*s[i]
   v+=t/factorial(l)
 for l in range(n):
  for c in comps(n-1,l):
   t=F(11);p=0
   for i in c:p+=i;t*=22*(1+p)*s[i]
   v+=t/factorial(l)
 f[n]=v;s[n]=4*v;req(v>0,'positive')
def poly(x):return sum(F(5,4)**j*s[j]*x**j for j in range(1,6))
Q=2**80;lo=0;hi=Q
while lo<hi:
 mid=(lo+hi+1)//2
 if poly(F(mid,Q))<=F(1,440):lo=mid
 else:hi=mid-1
rho=F(lo,Q);req(rho>0,'nonzero grid');req(poly(rho)<=F(1,440),'safe');req(poly(F(lo+1,Q))>F(1,440),'maximal grid');req(rho<=1,'disk')
M=2*(F(990,49)+F(55,4));C=2*M/rho**6
old=json.loads(Path('/private/tmp/toe-24h-probes-20260908/native-local-ring-truncation-cold-proof/RESULT.json').read_text())
for j in range(1,6):req(s[j]<=F(old['s'][str(j)]),'majorant improvement')
req(rho>F(old['rho']),'radius improvement');req(C<F(old['C_R']),'remainder improvement')
# Rational exponential majorants: exp(t)<=1/(1-t) for0<=t<1.
req(F(1,1-F(1,5))==F(5,4),'support exponential bound');req(18/(1-F(6,55))==F(990,49),'D weight');req(11/(1-F(1,5))==F(55,4),'V weight')
# Retaining rho powers matters; linearized radius is far smaller.
linear=F(1,440*sum(F(5,4)**j*s[j] for j in range(1,6)));req(rho>linear,'power retention')
r=dict(checks=checks,f={j:str(v) for j,v in f.items()},s={j:str(v) for j,v in s.items()},rho=str(rho),rho_decimal=float(rho),grid_numerator=lo,grid_denominator=Q,polynomial_at_rho=str(poly(rho)),M=str(M),C_R=str(C),C_R_decimal=float(C),regime_gamma_over_U=float(rho/2),old_radius=float(F(old['rho'])),old_C_R_order10=len(str(F(old['C_R']).numerator))-len(str(F(old['C_R']).denominator)),seconds=time.monotonic()-start)
Path(__file__).with_name('RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k not in ('C_R','polynomial_at_rho')},indent=2))
