# Root independent finite-neighborhood and finite-carrier dynamics bound

This is a mathematical approximation theorem for a supplied cubic SU3 Hamiltonian. It retains nonlinear plaquette interactions and boundary charge sectors. Root and primary independently derived the face-chain estimate before exchanging refinements. Root's tail integration and mixed-state normalization refinements were prospectively frozen before calculations. No finite calculation supplies a continuum or physical clock conclusion.

## 1. Setting and geometric constants

Let Lambda be any finite set of links of the infinite cubic lattice, with any chosen subset of its elementary plaquettes. On its full tensor L²(SU3) link carrier take H_Lambda=sum_e K_e+v sum_p(1-J_p), K_e=-(3/(2a))Delta_e, a>0,v>=0, J_p=ReTr(U_p)/3. The sum of v per face is scalar and does not affect Heisenberg evolution. Use centered interactions Phi_p=-v J_p, norm<=v. Every link belongs to at most4 plaquettes, each of4 links.

Define the link metric by declaring two distinct links adjacent if they belong to a common elementary plaquette in the infinite lattice. A face has diameter1 in this metric. Let A be bounded with nonempty finite link support X. For integer r>=0, Omega=B_r(X) intersect Lambda, N=|Omega|. Include every chosen Lambda plaquette wholly inside Omega in H_Omega. Each adjacency step changes a link's tail coordinates by at most1 in each coordinate, so N<=3|X|(2r+1)^3. A face crossing Omega has distance at least r from X, since it contains an outside link of distance at least r+1 and its four links are mutually adjacent. At most4N faces cross; if F is the number of internal faces,4F<=4N, hence F<=N. The positive finite-region potential obeys0<=V_Omega<=M=2vF<=2vN.

## 2. Strong interaction picture and a conservative face-chain bound

The onsite K terms are unbounded but their tensor product unitary does not spread support. In a finite Lambda, conjugating each bounded Phi_p by the onsite unitary produces a strongly continuous, bounded, time-dependent interaction with the same support and norm. Strong Dyson integrals exist and define unitary propagation. They are not assumed norm differentiable on all bounded local inputs. This is the strong-topology setting treated in Nachtergaele and Sims, arXiv:1410.8174, especially Proposition2.1 and Lemma2.2; the elementary recursion below fixes the present finite-range constants rather than importing numerical velocities.

For the bounded interaction-picture dynamics and fixed bounded B supported on Y, put C_B(S,t)=sup_(A_S nonzero)||[tau_t(A_S),B]||/||A_S||. The Jacobi identity splits the derivative of this commutator into a selfadjoint commutator evolution (which preserves norm) and a forcing term. The strong variation-of-constants estimate then gives
 C_B(S,t)<=C_B(S,0)+2 sum_(p:p meets S) integral_0^|t| ||Phi_p(s)|| C_B(p,s) ds.
The same bound applies to two-time propagation. Endpoint onsite conjugations leave supports and norms unchanged and may be absorbed into A or B; hence the bound applies to the original dynamics.

Iterating this inequality yields chains of faces. The first face has weighted choice sum at most4v|S|; each subsequent face meeting a preceding4-link face has weighted choice sum at most16v. For disjoint X,Y, a chain contributing to the initial commutator must reach Y, so its number n of faces is at least d(X,Y). The initial commutator is bounded by2||B||. Time ordering supplies |t|^n/n!. A safe bound, after loosening the first factor, is
 ||[tau_t(A),B]||<=2||A||||B|| |X| Theta_d(32v|t|),
 Theta_d(z)=sum_(n>=d) z^n/n!, d=d(X,Y).
For d=0 the same upper bound is valid since |X|>=1. The iterated remainder vanishes by the factorial, uniformly in finite Lambda; no branching-volume norm is used. For z>=0, Theta_d(z)<=exp(e z-d), since1_(n>=d)<=exp(n-d). This gives the conservative32e v propagation coefficient; no optimal velocity is claimed. At v=0 and d>=1 the exact tail is zero.

## 3. Spatial truncation with an integrated tail

Decouple Omega and its complement by removing crossing plaquettes. The onsite operators are unchanged, and the difference of the two finite Hamiltonians is bounded. Duhamel in the strong interaction picture bounds the observable difference by the time integral of commutators with all crossing Phi_p. All crossing faces lie at distance at least r from X. Therefore, for T>=|t|,
 ||tau_t^Lambda(A)-tau_t^Omega(A)||
 <=2||A|| v |X| N_cross integral_0^T Theta_r(32vs) ds
 <=(||A|| |X| N/4) Theta_(r+1)(32vT).                 (S)
For v>0, the integral identity follows term by term from the nonnegative series; for v=0 both sides vanish. The second inequality uses N_cross<=4N. The explicit exponential upper bound is (||A|| |X|N/4) exp(32e vT-r-1). Unlike the exact tail, that further upper bound need not vanish atv0. One may also take the minimum with2||A||. The constants depend on X,r,T and local v, not the total ambient volume.

Global initial correlations are allowed. Under the decoupled evolution, a local expectation depends only on rho_Omega, the reduced state on Omega. The operator norm error(S) holds for every global state; no product-state assumption enters spatial truncation.

## 4. Cutoff approximation from local form energy

Assume rho_Omega is a normal density matrix with finite energy E=Tr(rho_Omega H_Omega). On each link retain full Peter-Weyl blocks p+q<=R, with projector P_R; use their tensor product P on Omega and Q=1-P. The all-link kinetic threshold is g_R=[ceil(3(R+1)^2/4)+3(R+1)]/a. It gives H_Omega>=K_Omega>=g_R Q as forms. The local dimension is D_R=(R+2)^2(R+3)^2(R+1)(R+4)(3(R+2)^2+3(R+2)+2)/2880, so N ceil(log2D_R) qubits store the finite tensor carrier.

Let H_Omega,R=P H_Omega P on the finite carrier and p=Tr(P rho_Omega). Then1-p<=E/g_R. Purify rho_Omega with a reference that is not evolved. Full finite-region evolution preserves its form energy, so the Q component of the purified state has norm at mostsqrt(E/g_R) at every time. Because P K Q=0, the projected Duhamel forcing is only P V Q. Its norm is at most M. The block32 proof, on this arbitrary finite link set with M=2vF, gives
 ||psi(t)-exp(-itH_Omega,R)P psi|| <=(1+M T)sqrt(E/g_R).
The extension from operator to form domain uses spectral approximation and bounded V exactly as in block32. No finite-rank reference or special pure state is assumed.

For A_R=PAP and sigma=P rho_Omega P (trace p), the expectation difference between the normalized full vector and the unnormalized finite vector is at most2||A||(1+M T)sqrt(E/g_R). If p>0 and sigma is normalized to rho_R=sigma/p, this adds at most||A||(1-p): the finite unnormalized expectation has magnitude at most p||A||. Thus
 |Tr(rho_Omega tau_t^Omega(A))-Tr(rho_R tau_t^R(A_R))|
 <=||A||[2(1+M T)sqrt(E/g_R)+(1-p)]
 <=||A||[2(1+M T)sqrt(E/g_R)+E/g_R].                 (C)
The sufficient condition E/g_R<1 guarantees p>0. If the input is already prepared in P, p=1 and the normalization term vanishes. Otherwise success probability and preparation of rho_R remain an explicit resource premise; this is not a free deterministic encoder or a diamond-norm assertion.

Combining(S) and(C) gives the promised local-observable error bound, independent of total lattice size. If only a local kinetic energy-density bound Tr(rho K_e)<=epsilon_K is available, E<=N epsilon_K+2vF supplies a sufficient local energy budget. First choose r to control(S), then choose R to control(C) for that finite N and E. No claim of a uniform all-energy fixed-R approximation follows.

## 5. Boundary Gauss sectors cannot be discarded

A global physical state need not reduce to a local zero-boundary-charge singlet. On an actual four-link loop, the normalized physical state psi=Tr(U1 U2 U3^(-1) U4^(-1)) has a Schmidt decomposition across one link versus the remaining three:
 psi=(1/3) sum_(a,b=1)^3 [sqrt3 U1_ab] [sqrt3 (U2 U3^(-1) U4^(-1))_ba].
Haar orthogonality makes each displayed9-member set orthonormal. The single-link reduced density is therefore identity/9 on its fundamental Peter-Weyl matrix block. It commutes with the left and right gauge actions but has zero support on the constant single-link singlet. A forced local zero-charge projection would discard this valid global physical state with probability1.

Accordingly the neighborhood approximation uses the full local link tensor carrier and preserves its boundary representation sectors. P_R commutes with the exact gauge action; it does not project onto a boundary singlet. Interior constraints may be imposed where all incident links are retained. A gauge-invariant local observable may be used, but gauge invariance of a density operator must not be confused with support on invariant vectors.

## 6. Scope

This is an explicit finite-neighborhood, finite-storage approximation for local dynamics of a supplied lattice model and a specified finite-local-energy input. It neither compiles native qubit controls nor selects the Hamiltonian, time, couplings or measurements from the axioms. It does not identify the strong-coupling gapped sector, require a global spectral gap or take a spatial continuum limit. A thermodynamic dynamics claim would additionally use the Cauchy limit supplied by the same locality estimate; no exchange with an unpriced input-energy limit is assumed.
