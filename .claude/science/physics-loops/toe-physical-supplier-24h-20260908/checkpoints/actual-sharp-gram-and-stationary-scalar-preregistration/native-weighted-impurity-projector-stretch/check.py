from fractions import Fraction as F
import json
n=0
for j in range(-25,126):
    x=F(j,100)
    if min(abs(x),abs(x-1))<=F(1,4):
        e=min(abs(x),abs(x-1)); y=3*x*x-2*x*x*x
        near=0 if x<F(1,2) else 1
        if abs(y-near)>F(7,2)*e*e: raise RuntimeError('purification bound')
        n+=1
err=F(357,25)*F(1,128)+F(1,8)+429*F(4,25)**6+F(1,200)
if not err<F(1,4): raise RuntimeError('budget')
n+=1
if not 2*F(3,2)*F(29,40)-2*(F(29,40)**2+F(21,40)**2)>0: raise RuntimeError('ellipse monotonicity')
if not (F(3,2)-F(29,40))**2>0: raise RuntimeError('ellipse real square')
n+=2
print(json.dumps({'scope':'exact scalar purification, budget, ellipse positivity only; no physical matrix or integral','predicates':n,'quarter_budget':str(err),'quarter_budget_decimal':float(err)},indent=2))
