"""UNLAUNCHED formula scaffold. No accepted scalar importer, CLI or runtime."""
from fractions import Fraction as F

def solve2(a,b,c,x,y):
    det=a*c-b*b
    if a<=0 or det<=0:raise ValueError('uncertified moment solve')
    return ((c*x-b*y)/det,(a*y-b*x)/det)
def quad(a,b,c,u,v):return a*u*u+2*b*u*v+c*v*v

def candidate(c,nu,kind,mode):
    # Exact rational synthetic/scaffold arithmetic ONLY; native use needs intervals.
    if type(c) is not F or type(nu) is not F:raise ValueError('rational inputs')
    if kind=='P':m3=10*c;m4=20+36*c*c-F(2,3)*c*nu;j1=16*c;j2=F(32);cross=F(2,3)*nu-20*c
    elif kind=='O':m3=4*c+nu/3;m4=22+F(4,3)*c*nu;j1=F(4,3)*nu-8*c;j2=F(40);cross=-8*c
    else:raise ValueError('class')
    if mode=='residual':p0,p1=solve2(F(2),m3,m4,c,F(2))
    elif mode=='variational':p0,p1=solve2(c,F(2),m3,F(1),c)
    else:raise ValueError('fixed mode')
    u,v=p0,4*p1
    s0=quad(F(8),2*c,F(1),u,v)
    s1=quad(j1,F(0),2*c,u,v)
    s2=quad(j2,cross,F(4),u,v)
    if s2<=0:raise ValueError('source denominator')
    q=s1/s2
    r2=1-2*(p0*c+2*p1)+2*p0*p0+2*p0*p1*m3+p1*p1*m4
    t2=s0-2*q*s1+q*q*s2
    if min(r2,t2,s0,s1)<0:raise ValueError('inconsistent exact moment premise')
    return dict(p0=p0,p1=p1,q=q,r2=r2,t2=t2)
def ordered_nominal(C,A,c):
    u,v=C['p0'],C['p1'];a,b,q=A['p0'],A['p1'],A['q']
    return u*a+c*(u*b+v*a)+q*(2*c*u*a+4*u*b+4*c*v*b)
