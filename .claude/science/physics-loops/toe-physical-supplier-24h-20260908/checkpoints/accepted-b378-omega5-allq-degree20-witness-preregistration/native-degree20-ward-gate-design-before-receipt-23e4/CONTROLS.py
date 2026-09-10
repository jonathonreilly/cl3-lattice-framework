"""Only synthetic algebra. Never calls candidate(), table(), or any loader."""
from fractions import Fraction as F
import interval as I
import algebra as A
import wick

def run():
 n=0;P=I.point
 H=[[P(2 if i==j else 0)for j in range(3)]for i in range(3)]
 x,p=A.choose3(H,[P(1),P(2),P(3)]);assert x==[F(1,2),F(1),F(3,2)];n+=1
 for bad in [0,-1]:
  H[0][0]=P(bad)
  try:A.choose3(H,[P(1)]*3)
  except ValueError:n+=1
  else:raise AssertionError('singular/negative accepted')
 G=[[(P(int(i==j)),P(0))for j in range(6)]for i in range(6)]
 mean,inner,counts=A.evaluator(G)
 for word in [(0,1),(0,1,2),(2,1,2)]:
  op=A.term(word,2,1);value=inner(op,op);assert value==(P(4),P(0));n+=1
  assert A.hermitian(A.hermitian(op))==op;n+=1
 assert A.dyadic(F(-1,3))<=F(-1,3)<A.dyadic(F(-1,3))+F(1,2**128);n+=1
 try:A.dyadic(F(2**33))
 except ValueError:n+=1
 else:raise AssertionError('magnitude cap')
 return {'status':'PASS_SYNTHETIC_ONLY','checks':n,'native_calls':0}
if __name__=='__main__':print(run())
