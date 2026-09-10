"""Independent non-native 3x3 system and Clifford dagger controls only."""
import sys
sys.path.insert(0,'/private/tmp/toe-24h-probes-20260908/native-degree20-ward-gate-design')
import algebra as a,interval as i
from fractions import Fraction as F
H=[[2,1,0],[1,3,1],[0,1,2]];sol=[F(1),F(-2),F(3)];rhs=[sum(F(x)*v for x,v in zip(row,sol))for row in H]
x,p=a.choose3([[i.point(v)for v in row]for row in H],[i.point(v)for v in rhs]);assert x==sol and all(v[0]>0 for v in p)
# Independent Jordan-Wigner-free scalar CAR identity: anticommuting unit generators.
G=[[(i.point(int(j==k)),i.point(0))for k in range(6)]for j in range(6)]
mean,inner,counts=a.evaluator(G)
for w in [(0,1),(0,1,2),(1,2,1)]:
 op=a.term(w,3,1);assert inner(op,op)==(i.point(9),i.point(0));assert a.hermitian(a.hermitian(op))==op
# Non-Hermitian representative must not silently lose its adjoint.
op=a.term((0,1));assert mean(a.opmul(op,op))[0]==i.point(-1);assert inner(op,op)[0]==i.point(1)
print({'scope':'synthetic only, no tables/candidate/loader calls','predicates':9,'passed':True})
