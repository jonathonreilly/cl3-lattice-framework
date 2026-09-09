from fractions import Fraction as F
import json
checks=0
def req(v):
 global checks
 if not v:raise ValueError('tiny proof identity')
 checks+=1
# Single-atom toy laws, no native scalar values or catalog.
for x in [F(1,3),F(2),F(12)]:
 for s,t in [(F(1),F(2)),(F(2),F(1)),(F(1),F(1001,1000))]:
  a=s*s;b=t*t;d=b-a;As=1/(x+a);At=1/(x+b);Ap=-2*s/(x+a)**2
  G=(b*At-a*As)/d;H=2*s*((As+s*Ap/2)*d-(b*At-a*As))/d**2
  req(G==x/((x+a)*(x+b)));req(H==2*s*x/((x+a)**2*(x+b)))
  App=-2/(x+a)**2+8*s*s/(x+a)**3
  req(As+s*Ap/2==x/(x+a)**2);req(-(3*Ap+s*App)/4==2*s*x/(x+a)**3)
  req(0<=As-G<=t*t/(s*s*x));req(0<=-Ap-H<=2*t*t/(s**3*x))
  # A high-tail identity with four terms.
  N=4;partial=sum((-1)**n*x**n/t**(2*n+2) for n in range(N))
  req(At-partial==x**N/(t**(2*N)*(x+t*t)))
req(F(16,3)*8*F(17,60)==F(544,45))
print(json.dumps({'status':'PASS','checks':checks,'scope':'single-atom rational identities only; no physical or saved scalar input'},indent=2))
