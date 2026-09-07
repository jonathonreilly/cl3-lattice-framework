from fractions import Fraction as F
from math import factorial
import json,hashlib
from pathlib import Path
checks=[]
def ck(name,ok):
 if not ok:raise AssertionError(name)
 checks.append(name)
def expsum(x,n):return sum((x**j/F(factorial(j))) for j in range(n+1))
a=F(23,72);g=lambda n:F(factorial(2*n),4**n*factorial(n))
cn=sum(c*g(n)*a**(-n) for c,n in [(F(1,20),4),(F(23,2592),5),(F(1,2592),6)])
cd=F(1,5)*(F(1,5)*20*a**-6+F(29,1620)*120*a**-7+F(1,2592)*840*a**-8)
ck('low numerator',cn<170);ck('low denominator',cd<2617)
ck('square sinc halfcut',F(1,16)+F(1,10)+F(1,80)+F(1,1600)<F(1,5))
ck('numerator cubic',F(1,810)+F(1,1440)+F(1,144)==F(23,2592))
ck('denominator cubic',F(1,810)+F(1,360)+F(1,72)==F(29,1620))
ck('alpha inverse square root',a>F(1,4))
ck('exp high exact',expsum(F(128,3),150)>10**18)
ck('exp approximation tail',expsum(F(512,3),500)>10**60)
b=2048;t=F(b,48)
en=F(b*b,3)*24**3*factorial(2)*sum(t**j/factorial(j) for j in range(3))/10**18
ed=F(b*b,30)*24**4*factorial(3)*sum(t**j/factorial(j) for j in range(4))/10**18
an=F(1,3)*(F(9,2)*factorial(4)*6**5+F(1,18)*factorial(5)*6**6)/10**60
ad=F(1,30)*(5*factorial(5)*6**6+F(1,18)*factorial(6)*6**7)/10**60
ck('exact numerator tail',en<F(37,10**6));ck('exact denominator tail',ed<F(3869,10**6))
ck('approx numerator tail',an<F(1,1000));ck('approx denominator tail',ad<F(1,1000))
ck('CN ceiling',cn+en+an<171);ck('CD ceiling',cd+ed+ad<2618)
ck('tail monotonicity threshold',b>5*48)
ck('W maximum',expsum(F(3),20)>18)
ck('QW maximum',expsum(F(5),25)>36*F(5,2)**5/27)
ck('Q2W maximum',expsum(F(7),30)>4*F(7,2)**7/27)
ck('W2 bound',3*F(1,12)+F(7,4)*F(1,6)+F(1,4)*F(1,2)==F(2,3))
ck('D0 floor',27*F(5,3)/F(22,7)>14)
ck('denominator fraction',1-F(1,b)-F(2618,14*b*b)>F(999,1000))
c=F(1000,999)*(F(171,14)+F(2,3)+F(2618,14)*(F(1,12)+F(2,3*b)))
ck('final constant',c==F(76675625,2685312) and c<29)
print(json.dumps(dict(checks=checks,beta0=b,C=29,low_CN=str(cn),low_CD=str(cd),ratio_coefficient=str(c),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2))
