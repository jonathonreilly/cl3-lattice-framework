from fractions import Fraction as F
from math import comb

def coefficient(n):
 if type(n) is not int or n<0:raise ValueError('nonnegative integer index')
 return comb(2*n,n)*sum(comb(n,k)**2*comb(2*k,k) for k in range(n+1))
def tails(s,m):
 if s<=0 or type(m) is not int or m<0:raise ValueError('domain')
 q=s*s+6;r=F(36)/(q*q);rm=r**m
 return rm/(q*(1-r)),2*s/(q*q)*rm*((2*m+1)/(1-r)+2*r/(1-r)**2)
def plan(s,target):
 if s<=0 or target<=0:raise ValueError('positive inputs')
 m=0
 while max(tails(s,m))>target:m+=1
 return m

def evaluate(s,target,progress=None):
 if s not in (F(1),F(2),F(1,2)) or target not in (F(1,10**6),F(1,10**12)):raise ValueError('fixed cases')
 m=plan(s,target);q=s*s+6;a=d=F(0);power=q
 for n in range(m):
  c=coefficient(n)
  if c>6**(2*n):raise ValueError('walk bound')
  a+=c/power;d+=2*s*(2*n+1)*c/(power*q);power*=q*q
  if progress and n%16==15:
   ta,td=tails(s,n+1)
   progress({'completed_terms':n+1,'planned_terms':m,'A_partial':str(a),'Aprime_partial':str(-d),'remaining_tails':[str(ta),str(td)],'A_bounds':[str(a),str(a+ta)],'Aprime_bounds':[str(-d-td),str(-d)]})
 ta,td=tails(s,m)
 return {'s':str(s),'target':str(target),'terms':m,'A':[str(a),str(a+ta)],'Aprime':[str(-d-td),str(-d)],'widths':[str(ta),str(td)],'status':'CERTIFIED_TARGET'}
