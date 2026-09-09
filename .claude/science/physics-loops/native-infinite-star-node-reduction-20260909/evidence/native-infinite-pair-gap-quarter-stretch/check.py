from fractions import Fraction as F
import json,math
opposite=F(3,8)*(F(4,7)+F(40,343));assert opposite>F(1,4)
a=F(17,60);w=[F(8,9),F(0),-(4*a/9+8*a*a),F(0),-4*a*a/9]
def mul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
p=[F(1)];low=F(0)
for n in range(1,13):p=mul(p,w);low+=sum(v/F(i+1) for i,v in enumerate(p))/n
low*=F(7,44);tail=F(0)
for j in range(16,320):
 a=F(j,16);b=F(j+1,16);tail+=F(7,44*16)*(24-8/a**2)/(b*b+7)**2
assert low+tail>F(1,4)
d=F(1,4);T=100;beta=3;term=F(1);exp_lower=term
for n in range(1,161):term*=d*T/n;exp_lower+=term
err=F(90,8)*(2/d**2+beta*T/d**2+2*beta/d**3)/exp_lower;assert err<F(1,10**6)
print(json.dumps({'opposite_lower':str(opposite),'perpendicular_low':str(low),'perpendicular_tail':str(tail),'tail_intervals':304,'both_exceed_quarter':True,'laplace_tail_upper':str(err),'laplace_tail_less_1e_minus_6':True,'physical_runs':0},indent=2))
