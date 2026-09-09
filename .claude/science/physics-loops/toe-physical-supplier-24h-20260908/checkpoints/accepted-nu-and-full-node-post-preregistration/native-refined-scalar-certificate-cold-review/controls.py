from fractions import Fraction as F
n=0
for x in (F(1),F(3),F(12)):
 for s in (F(1,8),F(1),F(4)):
  a=s*s;As=1/(x+a);Ap=-2*s/(x+a)**2;App=-2/(x+a)**2+8*a/(x+a)**3
  assert As+s*Ap/2==x/(x+a)**2;n+=1
  assert -(3*Ap+s*App)/4==2*s*x/(x+a)**3;n+=1
  for t in (F(1,3),F(2),F(8)):
   b=t*t;d=b-a;At=1/(x+b)
   assert (b*At-a*As)/d==x/((x+a)*(x+b));n+=1
   assert 2*s*((As+s*Ap/2)*d-(b*At-a*As))/d**2==2*s*x/((x+a)**2*(x+b));n+=1
   assert 0<=As-x/((x+a)*(x+b))<=b/(x*a);n+=1
   assert 0<=-Ap-2*s*x/((x+a)**2*(x+b))<=2*b/(x*s**3);n+=1
print(n,'exact identities/low-tail predicates PASS; no data')
