import sympy as S
from itertools import product,combinations
from pathlib import Path
import hashlib,json
c={}
def ck(k,p):
 if not p:raise AssertionError(k)
 c[k]=True
pairs=list(combinations(range(4),2));E={ij:int(ij==(0,1)) for ij in pairs}
sums=[E[(0,1)]+E[(2,3)],E[(0,2)]+E[(1,3)],E[(0,3)]+E[(1,2)]]
ck('interaction_complement_sums_violate_onebody',sums==[1,0,0])
e=[1,2,4,8];G={ij:sum(e[j] for j in ij) for ij in pairs}
ck('onebody_control_complement_sums',[G[(0,1)]+G[(2,3)],G[(0,2)]+G[(1,3)],G[(0,3)]+G[(1,2)]]==[15]*3)
basis=[x for x in product((0,1),repeat=4) if sum(x)%2==0]
A=S.Matrix([[1,*x] for x in basis]);b=S.Matrix([x[0]*x[1] for x in basis])
ck('no_affine_occupation_rewrite',A.rank()==5 and A.row_join(b).rank()==6)
a={(0,1):S.Rational(1,2),(0,3):S.Rational(1,2),(1,2):-S.Rational(1,2),(2,3):S.Rational(1,2)}
pl=lambda d:d.get((0,1),0)*d.get((2,3),0)-d.get((0,2),0)*d.get((1,3),0)+d.get((0,3),0)*d.get((1,2),0)
ck('input_Slater',pl(a)==0)
a[(0,1)]/=2
ck('filtered_pure_not_Slater',pl(a)==-S.Rational(1,8))
print(json.dumps({'checks':c,'count':len(c),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
