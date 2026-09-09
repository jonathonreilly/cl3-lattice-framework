from fractions import Fraction as F
import json
# Fixed shell weights define a finitely additive set readout, with no annular collapse.
a={(1,0,0)};b={(2,0,0),(3,0,0)}
w=lambda x:F(sum(t*t for t in x)+1,7)
W=lambda s:sum((w(x) for x in s),F(0))
# Identity convolution is local, translation covariant, cubic covariant and linear.
rho={(0,0,0):F(2),(1,0,0):F(3)}
eta={(0,0,0):F(-1),(0,1,0):F(4)}
add=lambda x,y:{k:x.get(k,F(0))+y.get(k,F(0)) for k in x.keys()|y.keys()}
K=lambda x:dict(x)
assert W(a|b)==W(a)+W(b)
assert len({w(x) for x in a|b})==3
assert K(add(rho,eta))==add(K(rho),K(eta))
assert K({(0,0,0):F(1)}).get((2,0,0),F(0))==0
print(json.dumps({'additivity':str(W(a|b)),'three_shell_weights':[str(w((n,0,0))) for n in (1,2,3)],'identity_response_linear':True,'unit_source_response_at_distance_two':'0','scope':'finite counterexamples to claimed implications; no physical model identification'},indent=2))
