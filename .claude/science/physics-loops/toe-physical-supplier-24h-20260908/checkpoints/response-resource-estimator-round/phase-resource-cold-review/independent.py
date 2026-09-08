import sympy as s,json
ck={}
def c(n,b):ck[n]=bool(b);assert b,n
Y=s.Matrix([[0,-s.I],[s.I,0]]);I=s.eye(2)
# Independent odd-dimensional imaginary-H Gibbs fixture: energies +/-1,+/-2,0 at beta log2.
rho=s.diag((s.Rational(5,4)*I-s.Rational(3,4)*Y)*s.Rational(4,31),(s.Rational(17,8)*I-s.Rational(15,8)*Y)*s.Rational(4,31),s.Rational(4,31))
c('density_normalized',s.trace(rho)==1)
c('conjugate_product',rho*s.conjugate(rho)==s.Rational(16,961)*s.eye(5))
rootF=s.Rational(20,31);ig=s.Rational(11,62)
c('root_not_squared_fidelity',ig==(1-rootF)/2 and ig!=(1-rootF**2)/2)
blocks=[(s.Rational(10,31),s.Rational(3,5)),(s.Rational(17,31),s.Rational(15,17))]
average=0
for j,(w,y) in enumerate(blocks):
 a=s.sqrt((1+s.sqrt(1-y*y))/2);b=y/(2*a)
 v=s.Matrix([a,-s.I*b]);u=s.Matrix([b,-s.I*a]);mix=(v*v.H+u*u.H)/2
 c('ensemble_block'+str(j),s.simplify(mix-(I-y*Y)/2)==s.zeros(2))
 average+=w*b*b
c('achieving_flag_ensemble',s.simplify(average)==ig)
# A different exact complete real instrument, checked via pure quadratic form.
psi=s.Matrix([s.Rational(3,5),4*s.I/5]);Ks=[s.diag(s.Rational(3,5),s.Rational(5,13)),s.diag(s.Rational(4,5),s.Rational(12,13))]
c('real_instrument_complete',sum([K.T*K for K in Ks],s.zeros(2))==I)
def weighted_ig(v):return s.simplify(((v.H*v)[0]-s.Abs((v.T*v)[0]))/2)
c('strong_monotonicity_exact',sum(weighted_ig(K*psi) for K in Ks)<=weighted_ig(psi))
# Exact finite angle: cos theta=4/5,sin theta=3/5, theta<pi/4.
U=s.diag(s.Rational(4,5)-3*s.I/5,s.Rational(4,5)+3*s.I/5);plus=s.ones(2,1)/s.sqrt(2)
c('single_pulse_saturates_angle',weighted_ig(U*plus)==s.Rational(9,25))
# Branch scalar phases cannot change conditional density, but can change coherent flag state.
u=U*plus;v=plus;flag=s.Matrix.vstack(u,v)/s.sqrt(2);changed=s.Matrix.vstack(s.I*u,v)/s.sqrt(2)
c('classical_branch_phase_invariance',(s.I*u)*(s.I*u).H==u*u.H)
c('coherent_recombination_not_gauge',flag*flag.H!=changed*changed.H)
eta=s.Rational(1,100)
c('expected_square_adverse',eta/2>(eta*s.Rational(22,7)/4)**2)
# Source dimer constants, separately rational arithmetic.
z=s.Rational(1156,225);c('dimer_target',s.simplify((1-4/z)/2)==s.Rational(32,289))
c('dimer_success_weight',s.Rational(289,625)*s.Rational(32,289)==s.Rational(32,625))
print(json.dumps({'count':len(ck),'checks':ck,'odd_dimension_Ig':str(ig),'root_fidelity':str(rootF)},indent=2))
