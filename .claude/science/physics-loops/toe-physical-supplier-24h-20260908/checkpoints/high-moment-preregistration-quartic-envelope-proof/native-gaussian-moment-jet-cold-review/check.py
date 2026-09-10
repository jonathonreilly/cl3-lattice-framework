from fractions import Fraction as F
from math import factorial
import json
n=0
for v in [F(-3,2),F(2,3),F(0)]:
 N=9;G=[F(0)]+[(-v)**k/factorial(k)for k in range(1,N+1)];R=[F(1)];ell=[F(0)];Z=[F(1)]
 for k in range(1,N+1):
  R.append(-sum(G[j]*R[k-j]for j in range(1,k+1)))
  ell.append(sum((k-j)*R[j]*G[k-j]for j in range(k))/(2*k))
  Z.append(sum(j*ell[j]*Z[k-j]for j in range(1,k+1))/k)
  assert Z[k]==(-v/2)**k/factorial(k);n+=1
print(json.dumps({'status':'PASS','independent_commuting_jet_checks':n,'native_values_loaded':0}))
