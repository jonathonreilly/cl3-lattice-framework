from fractions import Fraction as F
from core import certificate
q=lambda A:[[F(x) for x in r]for r in A]
E=q([[1,0],[0,1]]);z=q([[0,0],[0,0]]);T=q([[1,-2],[0,2]]);G=q([[1,1],[1,F(5,4)]])
r=certificate(G,z,T,E);assert r['e']==0 and r['entry_radius']==0 and r['C0']==T
assert certificate(G,q([[1,0],[0,1]]),T,E)['status']=='INDETERMINATE_RESIDUAL'
try:certificate(G,z,q([[1,0],[1,1]]),E)
except ValueError:pass
else:raise AssertionError('lower triangle')
r=certificate(q([[1,0],[0,1]]),z,q([[1,F(1,100)],[0,1]]),E);assert r['entry_radius']>F(1,100) and not r['width_pass']
print('PASS four tiny certificate controls; no physical inputs')
