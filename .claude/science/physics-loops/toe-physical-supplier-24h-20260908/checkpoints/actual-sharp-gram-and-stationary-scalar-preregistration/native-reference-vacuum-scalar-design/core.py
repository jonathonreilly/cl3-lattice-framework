"""Prospective exact interval scalar integration; no import-time evaluation."""
from fractions import Fraction as F
from math import factorial,comb
S=1<<192
def iv(a,b=None):
 a=F(a);b=a if b is None else F(b)
 if a>b:raise ValueError('reversed interval')
 return (F((a*S).__floor__(),S),F((b*S).__ceil__(),S))
def add(x,y):return iv(x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[1],-x[0])
def mul(x,y):
 z=[a*b for a in x for b in y];return iv(min(z),max(z))
def scale(x,a):return mul(x,iv(a))
def inv(x):
 if x[0]<=0<=x[1]:raise ValueError('zero divisor')
 return iv(1/x[1],1/x[0])
def moment(n):
 return sum(F(factorial(n),factorial(a)*factorial(b)*factorial(n-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b) for a in range(n+1) for b in range(n-a+1))
def pi_interval():
 def atan(q):
  v=sum((F((-1)**n,(2*n+1)*q**(2*n+1)) for n in range(48)),F(0));return iv(v,v+F(1,97*q**97))
 return add(scale(atan(5),16),scale(atan(239),-4))
def integrate(catalogue,gauss,save):
 if set(catalogue)!={f'{i:04d}.json' for i in range(746)}:raise ValueError('catalogue membership')
 rule=gauss['rule']
 if len(rule)!=12:raise ValueError('Gauss order')
 acc=iv(0);panels=[];n=2
 for j in range(-28,3):
  a=F(2)**j;c=3*a/2;half=a/2;piece=iv(0)
  for nodes,weights in rule:
   l,u=[c+half*F(z) for z in nodes];rl,ru=catalogue[f'{n:04d}.json'],catalogue[f'{n+1:04d}.json'];n+=2
   if F(rl['s'])!=l or F(ru['s'])!=u:raise ValueError('node binding')
   for row in (rl,ru):
    if row['terms']!=160 or row['status']!='CERTIFIED_TARGET':raise ValueError('oracle schema')
    if not 0<=F(row['A'][1])-F(row['A'][0])<=F(1,10**30):raise ValueError('oracle width')
   at=iv(F(ru['A'][0]),F(rl['A'][1]));t=iv(l,u)
   q=add(iv(1),neg(mul(mul(t,t),at)))
   piece=add(piece,mul(iv(*map(F,weights)),q))
  piece=scale(piece,half);acc=add(acc,piece);panels.append({'j':j,'integral':list(map(str,piece)),'cumulative':list(map(str,acc))});save({'status':'PARTIAL','panels':panels})
 if n!=746:raise ValueError('coverage')
 tail=iv(0)
 for k in range(16):tail=add(tail,iv(F((-1)**k)*moment(k+1)/((2*k+1)*8**(2*k+1))))
 remainder=F(12**17,33*8**33);radius=F(400,9)*F(4,25)**12
 integral=add(add(acc,tail),iv(-radius,radius+F(1,2**28)+remainder));mu=mul(scale(inv(pi_interval()),2),integral)
 result={'status':'CANDIDATE','mu':list(map(str,mu)),'cA':list(map(str,scale(mu,F(1,3)))),'width':str(mu[1]-mu[0]),'target':'1/1000000','panels':panels,'middle_radius':str(radius),'high_remainder':str(remainder),'oracle_calls':0,'new_physical_integral':True}
 save(result)
 if mu[0]<=0 or mu[1]-mu[0]>F(1,10**6):raise ValueError('fixed final gate')
 result['status']='CERTIFIED_TARGET';return result
