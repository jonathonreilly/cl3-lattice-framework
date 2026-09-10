from fractions import Fraction as F
import json
n=0
def ck(x):
 global n
 assert x;n+=1
L=F(17,20);eps=F(1,10**30)
ck(76*1451*F(1,2**20)<F(1,2));ck(F(17,3)*L*2*76**2*1451<2**27)
ck(2*L*76<130);ck(L*L*76**2<4174);ck(F(16,3)*(130*2**32+4174)<2**42)
ck(F(378,3)*L*76<2**13);ck(F(17,3)*L<5);ck(17*L*153+1<2**12)
budget=2**27*eps+F(2**42+2**13,2**160)+F(5,2**80)+F(2**12,2**180);ck(budget<F(8,10**13))
# Exact single-atom rational algebra; no native values or moments.
for s,t in [(F(1,3),F(2)),(F(1),F(3)),(F(1,2),F(1,2))]:
 A=lambda x:1/(4+x*x);B=lambda x:2/(4+x*x);D=lambda x:(1-x*x*A(x))/6
 KA=1/((4+s*s)*(4+t*t));KB=2*KA;KD=(A(s)-t*t*KA)/6
 for sig in [-1,1]:
  for tau in [-1,1]:
   q=sig*s;r=tau*t
   if q+r:
    ck((B(t)-B(s))/(q+r)==(q-r)*KB)
    ck((r*B(t)+q*B(s))/(q+r)==B(s)+r*(q-r)*KB)
    ck((t*t*B(t)-s*s*B(s))/(q+r)==(r-q)*(B(s)-r*r*KB))
    ck((r*A(t)+q*A(s))/(q+r)==A(s)+r*(q-r)*KA)
    ck((r*D(t)+q*D(s))/(q+r)==D(s)+r*(q-r)*KD)
ck(32*(2+F(256,3)+F(16,3))<2966);ck(F(32,3)+F(1,3)==11)
ck(2+F(256,3)+F(1088,6)<269);ck(1024+F(1088*256,6)<47446)
print(json.dumps({'status':'PASS','predicates':n,'input_upper':str(budget),'native_calls':0},indent=2))
