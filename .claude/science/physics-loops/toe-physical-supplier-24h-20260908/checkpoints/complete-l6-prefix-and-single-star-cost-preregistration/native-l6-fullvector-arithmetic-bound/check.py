"""Scalar arithmetic controls only; no physical vector or operator action."""
from fractions import Fraction as F
from math import isfinite,ldexp
import json,signal,resource,time

def main():
 signal.alarm(29);start=time.monotonic();u=F(1,2**53);zeta=F(1,2**1075);m=21
 gam=lambda n:n*u/(1-n*u)
 beta=gam(m)+2*gam(2)*(1+gam(m));tau=8*m*zeta/(1-u)**(m+2)
 cases=[];underflow_mutant=0
 for case in range(9):
  coeff=[];xs=[]
  for j in range(m):
   if case==8:c=(.5,0.);x=(ldexp(1.,-1074) if j==0 else 0.,0.)
   else:
    c=(ldexp((-1.)**(j+case)*(j+1),-6-case),ldexp((j%3)-1.,-7))
    x=(ldexp((-1.)**j*(2*j+1),case-8),ldexp((j%5)-2.,-9-case))
   coeff.append(c);xs.append(x)
  re=im=0.;er=ei=F(0);majorant=F(0)
  for (a,b),(c,d) in zip(coeff,xs):
   p=a*c;q=b*d;r=a*d;s=b*c
   if not all(map(isfinite,(p,q,r,s))):raise ValueError('intermediate')
   real=p-q;imag=r+s;re=re+real;im=im+imag
   if not all(map(isfinite,(real,imag,re,im))):raise ValueError('finite')
   a,b,c,d=map(F,(a,b,c,d));er+=a*c-b*d;ei+=a*d+b*c;majorant+=(abs(a)+abs(b))*(abs(c)+abs(d))
  error2=(F(re)-er)**2+(F(im)-ei)**2;radius=beta*majorant+tau
  if error2>radius*radius:raise ValueError('complex bound')
  underflow_mutant+=error2>(beta*majorant)**2
  cases.append({'case':case,'error_squared':str(error2),'bounded':True})
 if underflow_mutant==0:raise ValueError('underflow adverse did not discriminate')
 if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise ValueError('RSS')
 print(json.dumps({'status':'PASS','scalar_cases':9,'omit_underflow_term_failures':underflow_mutant,'beta_exact':str(beta),'scope':'nonphysical scalar21-term controls; no physical Γ action','seconds':time.monotonic()-start},indent=2))
if __name__=='__main__':main()
