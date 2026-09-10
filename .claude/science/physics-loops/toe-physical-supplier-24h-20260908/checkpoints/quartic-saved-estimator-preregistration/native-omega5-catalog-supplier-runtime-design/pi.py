from fractions import Fraction as F

def atan_bounds(x,n):
 total=sum(((-1)**k*x**(2*k+1)/F(2*k+1)for k in range(n)),F(0));rem=x**(2*n+1)/F(2*n+1)
 return(total,total+rem)if n%2==0 else(total-rem,total)
def pi_bounds():
 a,b=atan_bounds(F(1,5),32),atan_bounds(F(1,239),10)
 return 16*a[0]-4*b[1],16*a[1]-4*b[0]
