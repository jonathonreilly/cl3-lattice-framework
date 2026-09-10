from fractions import Fraction as F
from math import factorial,comb
from interval import add,mul,neg
from pi import pi_bounds

def moment(n):
 if type(n)is not int or n not in(44,45):raise ValueError('only missing M44/M45')
 return sum((F(factorial(n),factorial(a)*factorial(b)*factorial(n-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b)for a in range(n+1)for b in range(n-a+1)),F(0))
def node_value(node,r,m):
 if r not in(3,4):raise ValueError('fixed exponent')
 tt=mul(node['t_interval'],node['t_interval']);power=(F(1),F(1));q=(F(0),F(0))
 for j in range(r+1):
  term=mul((m[r-j],m[r-j]),power);q=add(q,neg(term)if j%2 else term);power=mul(power,tt)
 correction=mul(power,node['A_interval']);q=add(q,neg(correction)if(r+1)%2 else correction)
 return q,mul(node['weight_interval'],q),mul(node['weight_interval'],power)
def tails(r,m,progress=lambda *args:None):
 terms=[]
 for n in range(40):
  terms.append(F((-1)**n)*m[n+r+1]/((2*n+1)*8**(2*n+1)));progress('tail_term',{'r':r,'term_index':n,'terms':terms,'cumulative':sum(terms,F(0))})
 eps=F(1,2**64);low=sum((F((-1)**j)*m[r-j]*eps**(2*j+1)/(2*j+1)for j in range(r+1)),F(0));width=F(17,60)*eps**(2*r+3)/(2*r+3)
 lowbox=(low-width,low)if(r+1)%2 else(low,low+width)
 return {'r':r,'high_terms':terms,'high_partial':sum(terms,F(0)),'high_remainder':m[r+41]/(81*8**81),'low_interval':lowbox,'quadrature_radius':F(136,3)*m[r]/4**52,'tail_terms':40}
def finish(total,tail):
 radius=tail['quadrature_radius'];low=tail['low_interval'];high=(tail['high_partial'],tail['high_partial']+tail['high_remainder']);pl,pu=pi_bounds()
 return mul(add(add(total,high),(low[0]-radius,low[1]+radius)),(2/pu,2/pl)),(pl,pu)
