# Finite-link transporter algebra: root verification and sharper path estimate

2026-09-07 21:35UTC. The prospective contract predates the calculations. Root received native's completed-proof summary, including the stronger union-of-leakage path estimate, before writing this proof. This is an independently checked derivation of a shared argument, not a blind discovery. The finite-dimensional obstruction is consistent with known quantum-link constructions, which retain exact continuous gauge symmetry with nonunitary link operators.

## 1. A precise finite-dimensional obstruction

Let H be a finite nonzero Hilbert space and rho a continuous unitary representation of SU(3). Write D(g)=rho(g) tensor I_3. Suppose a unitary matrix of operators U on H tensor C^3 has exact endpoint covariance

 D(g) U D(g)^* = (I_H tensor g^{-1}) U.

This is the convention of the actual left pullback rho(g)f(V)=f(g^{-1}V). Using g rather than its inverse here with this same left representation would reverse the noncommutative group composition and is not an interchangeable convention. A one-parameter Cartan subgroup already suffices for the contradiction.

Take g(t)=exp(it T), where T=diag(1,-1,0), and rho(g(t))=exp(it L). Differentiate: with A=L tensor I_3 and B=I_H tensor T,

 [A,U]=-B U, so U A U^*=A+B.

Finite unitary similarity preserves the trace of the square. But A and B commute and Tr(T)=0, so

 Tr((A+B)^2)-Tr(A^2)=dim(H) Tr(T^2)=2dim(H)>0.

This contradicts unitarity. Equivalently the exponentiated similarity gives 3 chi_rho(g)=chi_rho(g) chi_fund(g) on this torus; chi_rho remains nonzero sufficiently close to identity whereas chi_fund(g(t))=1+2cos(t) differs from3. First trace alone would miss the contradiction because T is traceless.

This does not forbid finite quantum-link representations with nonunitary transporter matrices, exact finite gauge groups, approximate covariance, state-restricted approximation, or ancillary infinite-dimensional carriers. No TOE-wide impossibility statement follows.

## 2. Actual Peter–Weyl cutoff, not an abstract unilateral-shift analogy

Take H=L2(SU(3),normalized Haar). The full matrix U multiplies a color-valued wavefunction pointwise by V in SU(3), and is unitary. Let P_R retain complete Peter–Weyl summands (p,q) with p+q<=R, including both matrix-coefficient indices; extend P_R by color identity. On its range define C_R=P_R U P_R. Then

 D_R=I-C_R^* C_R=P_R U^*(I-P_R) U P_R >=0.

Fundamental multiplication has only summands (p+1,q), (p-1,q+1), (p,q-1), with inadmissible labels omitted. Thus it raises p+q by at most1. Consequently (I-P_R) U P_{R-1}=0. A positive operator vanishing on the interior is block-supported on the orthogonal top shell T_R=P_R-P_{R-1}. Since U is unitary,

 0<=D_R<=T_R tensor I_3.

The norm bound is sharp for every finite R, not merely bounded away from zero asymptotically. Let d_R=(R+1)(R+2)/2 and psi_R(V)=sqrt(d_R) V_11^R. Schur orthogonality gives norm1: this is the normalized highest matrix coefficient in Sym^R(C^3). For input psi_R tensor e_1, the three output components are sqrt(d_R) V_i1 V_11^R. Every component is a matrix coefficient of Sym^(R+1)(C^3), because all R+1 factors have the same input column and their output tensors may be symmetrized. No antisymmetric component survives. This lies entirely in the excluded (R+1,0) summand. Hence C_R(psi_R tensor e_1)=0 and D_R has eigenvalue1.

For R=0, all fundamental Haar means vanish and C_0=0 outright. The energy estimate below uses R>=1. Inverse link orientations have the same shell support by antifundamental fusion; a conjugate highest-column/row witness gives the analogous sharp defect.

With K=-3 Delta/(2a), the energy of summand(p,q) is [p^2+q^2+pq+3p+3q]/a. On p+q=R the smallest value is

 e_R=[ceil(3R^2/4)+3R]/a = g_(R-1).

Thus T_R<=K/e_R in quadratic-form order. A normalized retained state with finite kinetic expectation E has expectation of D_R at most E/e_R, capped by1. Worst-case operator-norm unitarity fails at every R while fixed-energy leakage tends to zero like R^-2 in probability. These statements coexist because the norm-one witness moves to increasing energy.

## 3. Distinct-link products and the stronger total-energy budget

Let e_1,...,e_L be distinct links along an oriented simple path. Each full transporter U_e acts on that link and the shared color C^3; factors for different links need not commute because their color matrices need not commute. However the color-identity cutoff P_e commutes with EVERY other-link transporter U_f and cutoff P_f. Let P=product_e P_e and W=U_eL ... U_e1. On retained input psi=P psi,

 C_eL ... C_e1 psi=P W psi.

The product of unitaries W has norm1. The unnormalized compressed error is exactly ||(I-P)W psi||. Since the commuting projections obey I-P<=sum_e(I-P_e),

 ||(W-PW)psi||^2 <= sum_e ||(I-P_e)W psi||^2.

For a fixed e, move I-P_e past the factors to its left and remove those factors by unitarity. The factors to its right preserve P_e and commute with the color-identity shell T_e, even for arbitrary initial entanglement. The single-link defect inequality therefore gives

 ||(I-P_e)W psi||^2 <= <psi,T_e psi>.

Summing yields the sharper bound

 ||(W-C_eL...C_e1)psi|| <= sqrt(sum_e <T_e>)
 <= sqrt(E_path/e_R),

where E_path=<psi,sum_e K_e psi>. A per-link assumption <K_e><=E_link instead gives sqrt(L E_link/e_R). The weaker telescoping bound sqrt(L E_path/e_R) from the initial candidate is valid but unnecessary. Reference-system entanglement causes no change: all projectors and kinetic forms are tensored by the reference identity.

If all path links initially lie in their interiors P_(R-1), every shell expectation vanishes and path action is EXACT. If a link is visited repeatedly, moving projections cannot reduce the expression to P W P in this way; that case needs a separate estimate depending on repeated visits and is outside this result.

## 4. State normalization and what this does not buy

Let q=||P W psi||^2. Orthogonality gives ||W psi-P W psi||=sqrt(1-q), with 1-q<=E_path/e_R. For q>0 the normalized compressed state eta=P W psi/sqrt(q) has overlap <W psi,eta>=sqrt(q), and therefore

 ||W psi-eta||^2=2(1-sqrt(q))<=2(1-q).

The pure-state trace distance with the one-half convention is exactly sqrt(1-q). These are mathematical comparisons; implementing nonunitary compression still requires an appropriate channel or dilation and, if interpreted as postselection, success probability q must be priced. The sufficient bound E_path<e_R ensures q>0; it is not necessary.

Most importantly, norm approximation does not control an unbounded kinetic-energy expectation. These estimates cannot alone transplant the exact full-unitary path trial's energy upper bound from block38 to finite qubit hardware. Such a transfer needs a form-energy estimate or an independently computed finite trial. The supplied Hamiltonian and state preparation also remain imports, not consequences of the four lattice axioms.

## Primary literature already consulted

Chandrasekharan and Wiese, Quantum Link Models: A Discrete Approach to Gauge Theories, https://arxiv.org/abs/hep-lat/9609042 . Wiese, From Quantum Link Models to D-Theory: A Resource Efficient Framework for the Quantum Simulation and Computation of Gauge Theories, https://arxiv.org/abs/2107.09335 . These motivate the known finite-gauge/nonunitary-link distinction; the explicit cutoff shell and path bounds above are proved here for the supplied actual Peter–Weyl construction rather than imported from an abstract claim about all encodings.
