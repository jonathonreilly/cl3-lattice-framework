from fractions import Fraction as F
from checker import certificate,normceil,seed
q=2**256;events=[]
a=certificate([[F(1),F(0)],[F(0),F(1)]],[[F(0)]*2 for _ in range(2)],[[F(1),F(0)],[F(0),F(1)]],[[F(1),F(0)],[F(0),F(1)]],lambda s,d:events.append((s,d)))
assert a['radius']==0 and a['width_pass'] and a['l1_pass']
assert normceil([[3,4]],1)==5
assert seed(0,0)=={(0,0):F(1,2),(3,0):F(1,2)}
assert seed(3,1)=={(1,1):F(1,2),(4,1):F(1,2)}
assert seed(398,1)=={(398,1):F(1)}
try:certificate([[F(1)]],[[F(0)]],[[F(-1)]],[[F(1)]],lambda *_:None)
except ValueError:pass
else:raise AssertionError('negative candidate')
print('{"status":"PASS","tiny_cases":6,"native_inputs":0}')
