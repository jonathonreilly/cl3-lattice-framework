import sympy as s,json,runpy,contextlib,io
from pathlib import Path
p=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(p/'physical_check.py'))
R=d['responses'][1];qs=s.symbols('q0:3',real=True);ls=s.symbols('l0:3',real=True)
# Direct three amplitude paths, derived independently of physical Pauli matrices.
amplitudes=[s.I*s.Rational(3,13)*s.exp(s.I*qs[0])-s.Rational(2352,40625)*s.exp(s.I*qs[1])+s.Rational(27648,40625)*s.exp(s.I*qs[2]),s.Rational(36,65)*s.exp(s.I*qs[0])-s.I*s.Rational(196,8125)*s.exp(s.I*qs[1])+s.I*s.Rational(2304,8125)*s.exp(s.I*qs[2]),-s.Rational(672,3125)*(s.exp(s.I*qs[1])+s.exp(s.I*qs[2]))]
probs=[s.expand(a*s.conjugate(a)) for a in amplitudes];at0={q:0 for q in qs};checks={}
def ck(k,b):checks[k]=bool(b);assert b,k
ck('all_sources_probability_complete',s.simplify(sum(probs))==1)
for i in range(3):
 for j in range(3):ck('amplitude_Response_'+str(i)+str(j),s.simplify(s.diff(probs[i],qs[j]).subs(at0))==R[i,j])
F=sum(s.exp(s.I*ls[i])*probs[i] for i in range(3))
for i in range(3):
 for j in range(3):ck('operational_mixed_derivative_'+str(i)+str(j),s.simplify(-s.I*s.diff(F,ls[i],qs[j]).subs({**at0,**{l:0 for l in ls}}))==R[i,j])
# Off-diagonal history functional is not uniquely determined by diagonal probabilities.
t=s.symbols('t',real=True);rowphase=[s.exp(s.I*t*qs[0]),1,1]
ck('history_phase_probabilities_identical',all(s.simplify((rowphase[i]*amplitudes[i])*s.conjugate(rowphase[i]*amplitudes[i])-probs[i])==0 for i in range(3)))
# At equal zero sources, a derivative in the forward source ONLY gains i t p0.
pzero=[s.simplify(z.subs(at0)) for z in probs]
ck('cross_source_phase_ambiguity_nonzero',pzero[0]>0)
C=s.Matrix([[1,0],[0,1],[-1,-1],[0,0]]);Rn=C.T*R*C
ck('neutral_curl_nonzero',Rn[1,0]-Rn[0,1]==s.Rational(497664,528125))
ck('symmetric_part_indefinite',((Rn+Rn.T)/2).det()<0)
print(json.dumps({'count':len(checks),'checks':checks,'probabilities_at_zero':[str(x) for x in pzero],'neutral_curl':str(Rn[1,0]-Rn[0,1]),'symmetric_part_determinant':str(((Rn+Rn.T)/2).det()),'offdiagonal_phase_derivative_difference':'i*t*'+str(pzero[0])},indent=2))
