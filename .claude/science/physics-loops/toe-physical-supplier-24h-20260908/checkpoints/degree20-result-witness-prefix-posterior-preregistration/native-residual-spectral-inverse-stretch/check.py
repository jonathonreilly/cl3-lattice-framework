from fractions import Fraction as F
import json
n=0
for d in [F(1,4),F(1),F(3,2)]:
 for t in [d+1,d+2,d+5]:
  A=(t+2*d)/(d*d*t**3)
  def Q(x):return(3*t-2*x)/t**3+A*(x-t)**2
  assert Q(d)==1/d**2 and Q(t)==1/t**2;n+=2
  assert -2/t**3+2*A*(t-t)==-2/t**3;n+=1
  for x in [d,(d+t)/2,t,t+1,10*t]:
   rhs=(x-d)*(x-t)**2*((t+2*d)*x+d*t)/(d*d*t**3*x*x);assert Q(x)-1/x**2==rhs and rhs>=0;n+=1
# Independent finite atomic spectral moment contraction for first/inner residuals.
lam=[F(1,4),F(1),F(4)];weights=[F(1,5),F(1,2),F(3,10)];p0,p1,q=F(2,3),F(-1,7),F(3,5)
m=[sum(w*x**j for w,x in zip(weights,lam))for j in range(7)];coef=[F(1),-p0,-p1]
for j in range(3):
 rho=sum(coef[a]*coef[b]*m[a+b+j]for a in range(3)for b in range(3));direct=sum(w*(1-p0*x-p1*x*x)**2*x**j for w,x in zip(weights,lam));assert rho==direct;n+=1
s=[sum(w*(p0+p1*x)**2*x**j for w,x in zip(weights,lam))for j in range(5)]
for j in range(3):assert s[j]-2*q*s[j+1]+q*q*s[j+2]==sum(w*(p0+p1*x)**2*(1-q*x)**2*x**j for w,x in zip(weights,lam));n+=1
print(json.dumps({'status':'PASS_SYNTHETIC_SPECTRAL_ALGEBRA','checks':n,'native_values':0,'fixed_tau_family':[1,2,4,8,16]}))
