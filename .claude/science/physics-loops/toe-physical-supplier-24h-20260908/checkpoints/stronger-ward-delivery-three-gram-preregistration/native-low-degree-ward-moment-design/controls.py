import json
import core as c
from fractions import Fraction as F
n=0

def check(v):
    global n
    if not v:raise AssertionError(n)
    n+=1
c.reset();g=[c.gamma(i) for i in range(4)]
P=c.imag(c.mul(g[0],g[1]));Q=c.imag(c.mul(g[2],g[3]))
H=c.add(c.scale(c.ONE,3),P,c.scale(Q,2))
K={0:{1:F(-2)},1:{0:F(2)},2:{3:F(-4)},3:{2:F(4)}}
density=c.mul(c.add(c.ONE,c.scale(P,-1)),c.add(c.ONE,c.scale(Q,-1)))
expect=c.wick_expectation(lambda i,j:F((i,j) in [(0,1),(2,3)]))
def literal(x):
    y=c.mul(density,x)
    return (y.get((0,0),F(0)),y.get((0,1),F(0)))
for mask in range(16):
    x={(mask,0):F(1)}
    check(expect(x)==literal(x))
    explicit=c.add(c.mul(H,x),c.scale(c.mul(x,H),-1))
    check(c.advance(x,K,{})==explicit)
check(c.advance(g[0],K,{})!=c.scale(c.imag(g[1]),2))
check(c.dagger(c.imag(g[0]))==c.scale(c.imag(g[0]),-1))
check(c.dagger(c.mul(g[0],g[1]))==c.scale(c.mul(g[0],g[1]),-1))
B=c.add(c.scale(c.ONE,2),c.scale(c.imag(c.mul(g[0],g[2])),F(1,3)))
D=c.add(H,B);p=[F(1,2),F(-1,10),F(1,100)]
u=c.polynomial(p,c.ONE,K,B)
direct={};power=c.ONE
for a in p:
    direct=c.add(direct,c.scale(power,a));power=c.mul(D,power)
check(c.norm2(c.add(u,c.scale(direct,-1)),expect)==0)
# Exact one-mode inverse checks with a genuine positive gap, no native data.
H1=c.add(c.ONE,P);B1=c.add(c.scale(c.ONE,2),c.scale(P,F(1,3)))
D1=c.add(H1,B1);inv=c.add(c.scale(c.ONE,F(27,65)),c.scale(P,F(-12,65)))
check(c.mul(D1,inv)==c.ONE)
J=c.add(c.mul(g[0],B1),c.scale(c.mul(B1,g[0]),-1))
row=c.pair_vectors({0:{1:F(-2)},1:{0:F(2)}},B1,J,[F(1,3)],[F(1,3)])
x=c.scale(inv,-1);v=c.mul(c.mul(inv,J),inv)
# delta=5/3, ||J||=2/3. Squared bounds are rational, no sqrt required.
r2=c.norm2(row['r'],expect);t2=c.norm2(row['t'],expect)
ex2=c.norm2(c.add(x,c.scale(row['x'],-1)),expect)
ev2=c.norm2(c.add(v,c.scale(row['v'],-1)),expect)
check(ex2<=r2/F(5,3)**2)
check(ev2<=2*((F(2,3)**2)*r2/F(5,3)**2+t2)/F(5,3)**2)
check(c.norm2(c.add(c.mul(D1,row['v']),c.scale(c.mul(J,c.scale(row['x'],-1)),-1)),expect)==t2)
# Degree-zero best residual based only on the native *symbolic* c upper bound.
check(1-F(49,60)**2/2==F(4799,7200))
check(6*15*16*F(4799,7200)>160)
# Exact Clifford identity behind the degree-zero source collapse.
d=c.add(g[1],g[2]);BB=c.imag(c.mul(g[0],d));JJ=c.scale(c.imag(d),2)
check(c.mul(BB,JJ)==c.scale(g[0],-4))
check(c.mul(c.mul(c.dagger(JJ),BB),JJ)==c.scale(BB,-8))
cc=F(49,60);pmax=cc/2;qmax=cc/2
check(90*pmax*pmax*(1+2*cc*qmax)<26)
check(6*15*16*F(4799,7200)>959)
# Independent nonnative occupied two-bond Wick check of the fourth-moment identity.
d=c.add(c.scale(g[1],-1),g[3]);BB=c.imag(c.mul(g[0],d))
commHB=c.advance(BB,K,{})
# mu_a=2, e_d=6, ||Ka||²=4, ||Kd||²=20, c=1, a K|h|d=-4.
check(c.norm2(commHB,expect)==4*2+20-2*2**2+2*2*6+2*1*(-4))
JJ=c.scale(c.imag(d),2);DJ=c.advance(JJ,K,BB)
check(c.norm2(DJ,expect)==64)
check(c.inner(JJ,DJ,expect)==(F(16),F(0)))
check(c.inner(JJ,c.advance(g[0],K,BB),expect)==(F(0),F(0)))
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','checks':n,'counts':c.COUNT,'native_evaluations':0},indent=2))
