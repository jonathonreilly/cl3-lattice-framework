from fractions import Fraction as F
from math import factorial,comb
from interval import add,mul,neg
from pi import pi_bounds

def moment(n):
 return sum((F(factorial(n),factorial(a)*factorial(b)*factorial(n-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b)for a in range(n+1)for b in range(n-a+1)),F(0))
def node_value(node):
 tt=mul(node['t_interval'],node['t_interval']);t4=mul(tt,tt);t6=mul(t4,tt)
 q=add(add(add((F(42),F(42)),neg(mul((F(6),F(6)),tt))),t4),neg(mul(t6,node['A_interval'])))
 return q,mul(node['weight_interval'],q),mul(node['weight_interval'],t6)
def tails():
 moments={k:moment(k)for k in range(3,44)};terms=[F((-1)**n)*moments[n+3]/((2*n+1)*8**(2*n+1))for n in range(40)]
 high=sum(terms,F(0));rem=moments[43]/(81*8**81);eps=F(1,2**64);low=42*eps-2*eps**3+eps**5/5;width=F(17,60)*eps**7/7
 return {'moments':moments,'high_terms':terms,'high_partial':high,'high_remainder':rem,'low_interval':(low-width,low),'quadrature_radius':F(1904,4**52),'tail_terms':40}
def finish(total,tail):
 radius=tail['quadrature_radius'];low=tail['low_interval'];high=(tail['high_partial'],tail['high_partial']+tail['high_remainder']);pl,pu=pi_bounds()
 ans=mul(add(add(total,high),(low[0]-radius,low[1]+radius)),(2/pu,2/pl))
 return ans,(pl,pu)
