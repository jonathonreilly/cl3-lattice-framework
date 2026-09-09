from fractions import Fraction as F
import arithmetic as a,json
n=0
for X in (F(1,2),F(3)):
 for s,t in ((F(1,2),F(2)),(F(3),F(1))):
  A=1/(X+t*t);As=1/(X+s*s);Ap=-2*s/(X+s*s)**2;w=F(2,5)
  g,h=a.weighted(s,(t,t),(A,A),(As,As),(Ap,Ap),(w,w));eg=w*X/((X+s*s)*(X+t*t));eh=2*s*eg/(X+s*s)
  assert 0<=eg-g<F(1,a.Q)and 0<=eh-h<F(1,a.Q);n+=1
  assert not 0<=eh+h<F(1,a.Q);n+=1
for x in ('01','1/1','1.0'):
 try:a.fraction(x)
 except ValueError:n+=1
 else:raise AssertionError('noncanonical')
print(json.dumps({'synthetic_checks':n,'native_calls':0,'moment_calls':0}))
