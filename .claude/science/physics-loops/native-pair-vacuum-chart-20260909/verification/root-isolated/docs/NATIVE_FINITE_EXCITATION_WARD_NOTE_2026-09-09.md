---
claim_id: native_finite_excitation_ward_note_2026-09-09
claim_type: bounded_theorem
claim_scope: "Supplied infinite native Gaussian reference: bounded Ward identity, trace-class impurity polarization, polylogarithmic finite-excitation existence and uniform absolute-error Ward approximation."
upstream_dependencies:
  - native_infinite_star_node_reduction_note_2026-09-09
  - native_star_thermodynamic_limit_note_2026-09-09
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
  - native_zero_penalty_optimal_flux_dispersion_note_2026-09-08
runner: scripts/native_finite_excitation_ward_2026_09_09.py
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Finite-excitation approximation of the native Ward node target

**Status:** conditional-support. Independent source review passed at the frozen assembled proof; see the packet review history. Exact supporting controls are not an audit verdict.

Use the [infinite node and h/4 gap theorem](NATIVE_INFINITE_STAR_NODE_REDUCTION_NOTE_2026-09-09.md), [thermodynamic reference](NATIVE_STAR_THERMODYNAMIC_LIMIT_NOTE_2026-09-09.md), [full native dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), and [canonical dispersion](NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md). The model, Hamiltonian and pure Gaussian reference remain supplied. All new gap uses are infinite-volume; no finite-L threshold is inferred.

## Unified claim and quantitative example

For each actual two-link impurity, its stationary projector differs from the reference by a trace-class operator of norm below87. An explicit dyadic quadrature yields a rank-k operator approximating that difference with nuclear error eta and k=O(log²(1/eta)). Exact principal-angle truncation then supplies a parity-preserving finite-excitation approximation of the original vacuum in the impurity Fock representation, with error at most sqrt2 eta and at most floor((k+3)/2) fermion modes. Fully swapped modes are included. This is an existence statement about the exact principal-angle subspace, not a claim that quadrature columns already compute it.

The actual impurity Hamiltonian is DeltaEA+dGamma(omegaA), with DeltaEA identified with the parent determinant integral. Its unnormalized semigroup propagates the state error contractively. The bounded Ward identity reduces all node terms to two inverses and explicit CAR sources. With eta=2287839703834313821/4000000000000000000000000 and k2352, at most1177 fermion modes suffice for the initial state; applying one boundary CAR source adds at most one orbital. The full90-word STATE-COMPRESSION error is below0.0036/h², using delta=h/4 and ||WA||<4.6. This is not an alpha value or a complete algorithmic error: principal orbitals, source tails, energies, propagation and cross-impurity phases/moments must still be certified. No cost or memory claim follows.

The argument below consolidates the complete proof chain. The preserved source versions in the packet retain their original provisional-review wording and chronology; those quotations do not supply a final review disposition for this assembled note. References to source filenames below identify that preserved provenance.


## Proof block 1: Native shared-center zero-energy scattering identity


This is an analytical route, not a computation of alpha. Use the actual bipartite one-particle matrix K=[0,B;-B^T,0], with the center in the first sublattice. Write b for its row, and b_A for that row restricted to a subset A of its six incident bonds. Reversing exactly those bonds gives B_A=B-2 e_0 b_A^T. Here b_A is a column when it occurs without transpose.

On a cubic fully antiperiodic even torus the reference B is invertible. Centered magnetic cubic symmetries permute all six incident bonds and preserve the AP holonomies. Their gauge factors cancel in the products b_j(B^-1)_(j,0). Consequently those six products are equal. Their sum is (BB^-1)_(0,0)=1, so each is exactly 1/6. This argument requires the centered magnetic symmetry, not a bare coordinate permutation of the signed matrix.

For k=|A|, the determinant lemma gives

 det(B_A)/det(B)=1-k/3.

For k !=3, Sherman–Morrison gives

 B_A^-1=B^-1+[2/(1-k/3)] B^-1 e_0 b_A^T B^-1.

In particular a two-bond defect has determinant ratio 1/3 and inverse coefficient 6. Its four-bond complement has ratio -1/3; the full six-bond star has ratio -1. The skew determinant ratio for a pair is therefore 1/9 at zero spectral parameter, agreeing with the independent scalar Green-function pair-gap formula. This does not give the many-body resolvent matrix element: the latter depends on the complete excitation spectrum and its vacuum contractions.

The same identity has a useful infinite-volume interpretation. The inverse reference operator applied to a finitely supported source is square summable in three dimensions: its Dirac singularity is O(1/|k|), whose square is locally integrable. Let w_A=(B^T)^-1 b_A, using this Fourier inverse. Its center value is k/6 by the AP limit of the identity above. Let q be a generalized zero-energy white-sublattice Bloch solution, B^T q=0, with q_0=1. Then

 q_A=q+[2/(1-k/3)] w_A

satisfies B_A^T q_A=0 and (q_A)_0=1/(1-k/3). For the actual pair, the center amplitude is exactly 3. All these statements concern generalized one-particle solutions; q is not an l2 CAR vector, and no bounded gamma(q) operator is asserted. The correction w_A is l2. The k=3 denominator is singular and this route must not be applied to it.

#### Why this has not yet proved the node sign

A Ward manipulation using q_A must retain its bounded correction 6w_A. The defect-adapted zero-mode functional is not the original vacuum annihilator. Dropping that correction would discard precisely additional local-source contractions of the kind present in the reviewed three-resolvent formula. The positivity of the on-center factor 3 therefore does not establish positivity of alpha.

There is also an exact many-body complement identity. Conjugation by gamma_0 flips every center-incident quadratic term and leaves all other terms unchanged, hence gamma_0 H_A gamma_0=H_(A^c), and likewise gamma_0 R_A gamma_0=R_(A^c), using the same reference energy. Thus R_C gamma_0 R_A=gamma_0 R_(C^c) R_A. In the 90-word sum C and A are disjoint pairs, so A is contained in the four-leg set C^c. The expression is an ordered product of two distinct inverses. It is not a positive quadratic form just because both negative resolvents have positive negatives.

The next genuinely discriminating identity would express the fully summed soft Ward correction together with the direct term as a squared norm or a positive scalar multiple of an impurity overlap. Neither the one-particle determinant identity nor the complement relation supplies that factorization. The negative disjoint-pair channel established separately makes discarding the correction unjustified.

#### Source and scope

Read actual NODE_REDUCTION.md, SOFT_LIMIT_AND_LAPLACE.md and UNIFORM_PAIR_GAP.md in native-infinite-star-node-stretch, together with the canonical bipartite convention carried by the 8063 thermodynamic-limit note. This derivation is independent algebra using that convention. It uses no finite-L4 extrapolation, no branch choice for a Gaussian determinant, no assumed positivity of a Laplace kernel, and no physical numerical evaluation. The newly reviewed h/6 gap can bound all inverse factors, but a norm bound cannot settle their signed sum.

## Proof block 2: Corrected zero-mode Ward identity with all tails retained


Use the actual native definitions and normalization in SOFT_LIMIT_AND_LAPLACE.md. Let w_A=(B^T)^-1 b_A for a two-link pair and set W_A=6 gamma(w_A). This is a bounded Hermitian CAR operator, unlike the generalized original node mode. The rank-one identity gives (w_A)_0=1/3, hence {W_A,gamma_0}=4.

The generalized corrected mode q+6w_A solves K_A(q+6w_A)=0. Its rigorous bounded consequence is

 [W_A,D_A]=-J_A,
 [W_A,R_A]=-R_A J_A R_A.                         (1)

One may establish the first equation directly on the finite-particle core using the linear CAR commutator: K_A w_A is finitely supported by the defining inverse equation. The result extends as a bounded commutator. It does not require forming gamma(q), an impurity vacuum, or a unitary implementing a change of vacuum. The second identity follows from the bounded inverse commutator, with R_A=-D_A^-1.

Substituting (1) into the already reviewed soft identity, and using {W_C,gamma_0}=4, gives the exact bounded formula

 8 alpha = sum_(A,C disjoint) [
  3 <R_C R_A>
 + (1/2)<R_C gamma_0 (W_A-W_C) R_A>
 - (1/2)<W_C R_C gamma_0 R_A>
 - (1/2)<R_C gamma_0 R_A W_A> ].                (2)

All brackets remain in the ORIGINAL canonical Gaussian vacuum. In particular the last two terms must not be removed by an impurity-annihilation assertion. The derivation is simple operator algebra: the two middle terms of the expanded commutators combine as W_C gamma_0+gamma_0 W_A=4+gamma_0(W_A-W_C). This is where the native factor3 appears, with its exact normalization.

This removes one inverse from each correction, replacing its local numerator by a bounded spatial tail. It is a sharper structural target than a bound using beta/delta cubed. It does not make the direct overlap positive: <R_C R_A> is an off-diagonal Gram entry, and the disjoint-pair sum is indefinite. Pair reversal makes the full sum real but does not cancel the (W_A-W_C) term; its adjoint is exactly the reversed-pair term.

#### Actual tail norms from the native scalar Green function

The pair-gap derivation defines A(0)=<e_0,(-K^2)^-1 e_0> and D(0)=1/(6h^2). Its normalized signed two-neighbor vector u has <u,(-K^2)^-1u>=A(0) for perpendicular pairs and D(0) for opposite pairs. Since ||b_A||=sqrt(2)h,

 ||w_P||^2=2h^2 A(0) <=17/30,
 ||w_O||^2=2h^2 D(0)=1/3.

Thus ||W_P||<=sqrt(102/5), and ||W_O||=sqrt12. These are real CAR vectors, so the operator norm equals their Euclidean norm. They use the actual Green-function bound, not a flat-spectrum L4 approximation. The difference vector has zero center component; its trivial norm bound is still at most the sum of the two norms.

For one ordered pair, the absolute value of the three correction terms in (2) is bounded by

 [ ||W_A-W_C|| + ||W_C|| + ||W_A|| ] /(2 delta^2)
 <= (||W_A||+||W_C||)/delta^2.

Even the opposite-pair norm is larger than the onsite coefficient3. Moreover no strictly positive lower bound for the direct disjoint Gram sum follows from the available gap. Consequently this rigorous estimate does not close a positivity proof, including with the improved h/6 gap. It does avoid the former extra inverse power, so it can improve an eventual certified approximation of the scalar target.

#### Precise remaining opportunity

A sign proof must control correlations between W_A Omega and R_C gamma_0 R_A Omega, not merely the tail norms. The actual reference Gaussian relation fixes W_A Omega as a one-particle vector; it does not annihilate it. A usable next identity would evaluate or bound these cross contractions jointly with the disjoint-pair Gram channels through the actual quadratic scattering data. Formula (2) narrows that task to two inverses and explicit l2 sources. No impurity-vacuum implementer or determinant square-root sign has been supplied or used. Alpha remains unevaluated.

## Proof block 3: Infinite pair impurities change the Fermi projector by a trace-class operator


A first-principles structural lemma for independent review. It uses the already reviewed infinite two-link determinant and Green bounds, not a finite-volume gap or an assumed active gap. It concerns the stationary one-particle spectral projector; a uniform low-rank description of the finite-time normalized quench is a separate obligation.

Let h0=iK and h_lambda=h0+lambda Delta h, 0<=lambda<=1, for either actual pair geometry. Let U have columns the center and the normalized signed neighbor sum. In hopping units h=2|t_hop|, ||Delta h||=beta=2sqrt(2)h and rank Delta h=2. The reviewed scalar Green bound is A(0)<=a/h², a=17/60. The opposite-pair entry B=D<=1/(6h²), and the perpendicular entry B=A. The center and neighbor sum have opposite bipartite parity, so their off-diagonal entry in U^dagger(h0²+s²)^-1 U vanishes. Hence

 ||(h0-is)^-1 U||_HS²=A(s)+B(s)<=2a/h²,
 ||U^dagger(h0-is)^-1 U||<=sqrt(a)/h.

The rank-two Birman-Schwinger determinant at coupling lambda is

 d_lambda(s)=(1-4lambda h²D(s))²+8lambda²h²s²A(s)B(s).

Since 0<=D(s)<=1/(6h²), d_lambda(s)>=(1-2lambda/3)²>=1/9. This is uniform in s>0 and along the entire coupling interpolation. For a two-by-two matrix M, ||M^-1||=||M||/|det M|. Thus the exact Woodbury matrix has norm at most

 9(1+beta sqrt(a)/h).

The resolvent difference is a product of two bare local resolvent columns, this bounded two-by-two matrix, and the rank-two coupling. Its trace norm is consequently bounded near s=0 by

 C0=2a beta*9(1+beta sqrt(a)/h)/h².

At s>=2beta, a Neumann estimate instead gives

 ||(h_lambda-is)^-1-(h0-is)^-1||_1<=4beta/s².

Both bounds are integrable in s. The sign-function resolvent integral therefore converges in trace norm for the difference, proving

 P_-(h_lambda)-P_-(h0) is trace class,
 ||P_-(h_lambda)-P_-(h0)||_1
 <=(1/pi) integral_0^infinity ||Delta R(is)||_1 ds.

There are no zero eigenvectors: at lambda=0 the Fourier symbol has no square-integrable zero mode; a zero eigenvector at nonzero lambda would satisfy the finite-rank zero-energy equation, whose limiting two-by-two matrix remains invertible by d_lambda(0)>=1/9. The local inverse columns exist in l² because A(0)<infinity. This also rules out that particular finite-rank zero-energy solution, without postulating a spectral gap.

For a completely explicit conservative bound use sqrt(a)<3/5, beta<3h, and split at s=6h. Then C0<1071/(25h), the high integral is <2, and pi>3 gives

 ||P_-(h_lambda)-P_-(h0)||_1<87.

This bound is intentionally coarse. It proves a finite excitation-sector change in a Schatten sense and makes the rank-tail inequality

 ||D-D_rank-r||_HS <= ||D||_1/sqrt(r+1)

available. At a small requested error that particular bound is not computationally useful. It does not prove a rapidly decaying numerical singular spectrum, a uniform rank for every finite-time quench, a nonzero reference overlap, or an affordable 384-MiB evaluation. Those must not be inferred merely from trace-class implementability folklore.

The argument also gives trace-norm continuity in lambda by dominated convergence. Any further use of a Fock implementability theorem or parity/index conclusion needs its assumptions stated separately; it is not an imported conclusion here. The result is a concrete reason to investigate excitation compression rather than retain the entire bath, while preserving the remaining quantitative rank bottleneck.

## Proof block 4: A polylogarithmic-rank approximation to the stationary impurity projector


New analytic refinement of TRACE_CLASS_IMPURITY_PROJECTOR, for independent review. No physical resolvent or quadrature was evaluated. This is a finite-rank existence/construction bound for the stationary projector, not a completed quench-state algorithm.

Write F(s)=(h_A-is)^-1-(h0-is)^-1 and P_A-P0=-(2pi)^-1 integral_0^infinity [F(s)+F(s)^dagger]ds. Each F(s) has rank at most two. The preceding lemma gives ||F(s)||_1<=C0 with C0<1071/(25h). Self-adjoint resolvent norms additionally give ||F(s)||_1<=2beta/s² for every s>0, without a Neumann assumption.

On a complex disk |z-c|<=c/2, the resolvent identity bounds each bare or perturbed local resolvent column by twice its value at c. Therefore F is analytic there with

 ||F(z)||_1<=M(c)=min(4C0,8beta/c²).

Use dyadic real intervals [s,2s], centered at c=3s/2. The Bernstein ellipse of parameter rho=5/2 has maximum distance (s/4)(rho+rho^-1)=29s/40<c/2 from the center. The standard Chebyshev contour bound follows directly from Cauchy's formula: the degree-(2p-1) polynomial tail is at most (10/3) M(c) rho^(-2p). Positive p-node Gauss-Legendre quadrature integrates that polynomial exactly and has weights summing to the interval length. Its error in trace norm is thus at most

 (20/3) s M(c) (4/25)^p.

This is an operator-valued polynomial approximation argument; no dimension factor or Fock expansion is used.

Choose intervals j=-Jlo,...,Jhi-1 with s=h*2^j. Summing s M(3s/2) over all integer j is less than

 4C0*h + (64/3) < 14452/75.

The first term bounds j<0 by a geometric sum; the second bounds j>=0 using beta<3h. Combining quadrature and both omitted tails, with pi>3, proves a Hermitian finite-rank Q approximating P_A-P0 with

 ||(P_A-P0)-Q||_1
 <= (357/25) 2^(-Jlo) + 2*2^(-Jhi) +429*(4/25)^p.       (1)

The rank of Q is at most 4p(Jlo+Jhi), because each quadrature node contributes F+F^dagger. All finite-rank columns can be represented through actual impurity/bare resolvent columns; their infinite-space Gram entries need their own certified local Green-function evaluation. Equation (1) does not provide those entries for free.

In particular this gives rank O(log²(1/epsilon)), rather than the algebraic rank tail from trace norm alone. The constants remain conservative. The companion exact arithmetic lists sufficient ranks for three fixed tolerances without computing any physical matrix.

A physical covariance can be recovered without assuming Q itself is a projector. Let A=P0+Q and round its spectrum at 1/2. The resulting projector Ptilde differs from the true P_A by at most twice the error in (1) in trace norm: spectral rounding minimizes trace-norm distance to the set of projections, and the triangle inequality applies. The change from P0 is confined to span(range Q, P0 range Q), of dimension at most twice rank Q. Particle-hole symmetry must be preserved in the represented quadrature and rounding. This observation is a finite excitation-carrier construction, not a license to ignore parity or the physical phase of a vacuum implementer.

For a long-time quench one must still transport this finite excitation representation, control state and phase errors, and compute all required Gram data. The stationary rank bound alone does not establish a uniform finite-time approximation or 384-MiB cost. It nevertheless replaces an unquantified compression hope by a checkable explicit rank/error relation.

## Proof block 5: Principal-angle construction and the finite-time graph obstruction


This extends the reviewed stationary trace-class result. It makes no finite-time compression claim without the chart assumptions stated below. All one-particle spaces use the particle-hole involution of the actual Majorana problem; Q and P obey conjugate(P)=1-P.

#### Explicit stationary Fock construction

The compact difference of projections admits a principal-angle decomposition: diagonalize the positive compact operator Q(1-P)Q on ran Q. For every eigenvalue s² strictly between0 and1 choose a normalized vector u in ran Q; its normalized partner in ran(1-Q) is obtained by applying (1-Q)P to u. The resulting two-dimensional plane has P matrix [[c²,cs],[cs,s²]], up to a removable phase, with c=sqrt(1-s²). Orthogonal spectral subspaces give orthogonal planes. Eigenvalue1 gives the finite-dimensional fully exchanged spaces. The common0/1 spaces are unchanged. This construction follows directly from P²=P and the spectral theorem for a compact positive operator.

Particle-hole conjugation pairs the nontrivial planes. More explicitly, on a finite nonexceptional block the annihilator equations have a skew-symmetric pairing matrix Z (the skew relation is the CAR anticommutator of two annihilators). Unitary congruence reduces Z to 2-by-2 skew blocks: choose a singular vector, pair it with its normalized skew-conjugate image, and repeat on the orthogonal complement. This proves the paired form used below, rather than assuming independent one-mode rotations. Compactness permits the same block construction countably. In Fock language a paired block uses two reference modes a,b and the normalized factor

 c + s a†b†

acting on their empty vacuum, with a phase on s if required. Its mean particle number is2s². The corresponding doubled one-particle projector difference has squared Hilbert–Schmidt norm4s². A fully exchanged reference mode contributes one particle and squared projector difference2; only finitely many can occur because the difference is compact and trace class. Treat these occupied modes first, using a fixed ordered creation product.

For infinitely many paired blocks the finite products converge in Fock norm: choose each c>=0, and the inner product between products cut at m and n is product_(j=m+1..n)c_j. Since sum s_j² is finite, the tail products approach1. This proves the Cauchy property and gives a normalized vector in the original Fock space. Its finite-mode correlations have precisely covariance P, so it is the required pure quasifree state. No external implementability theorem is needed for this construction.

The particle count follows by monotone convergence of finite-mode number operators:

 <N>=number of fully occupied exceptional modes +2 sum_j s_j²
     =(1/2)||P-Q||HS² <=(1/2)||P-Q||1 <87/2.

This explains the particle-hole factor explicitly. The vacuum overlap is zero if a fully occupied exceptional mode occurs. If no such mode occurs, the product of cosines is strictly positive because the squared sines are summable. A uniform lower bound on that product has not been proved by the trace bound alone.

#### Relative parity along the coupling path

Parity cannot be read from the integer index of arbitrary complex projections alone. Here it is the parity of the number of fully occupied exceptional reference modes; paired rotations create two particles. The constructed quasifree vacuum is unique up to phase. Near any fixed polarization, sufficiently close projections in operator norm have no exchanged modes relative to each other and can be joined by the paired-rotation construction above. Their vacuum vectors therefore have the same parity. The trace-norm-continuous lambda path is operator-norm continuous and its compact parameter interval can be covered by finitely many such neighborhoods. Starting at lambda0 with the even reference vacuum proves even relative parity at every lambda. Fully exchanged modes relative to the original reference may occur, but their total parity is even. Their occurrence can make the original-reference overlap vanish without breaking implementability or continuity.

#### Finite-time graph evolution: what follows and what does not

Let P_A be the stationary negative spectral projection of h_A, and write h_A=(-omega_minus) direct-sum omega_plus on its negative/positive spaces, with both omega nonnegative and bounded. If the initial subspace ran Q is a graph over the entire ran P_A of a bounded operator Z0, its imaginary-time evolution is a graph with

 Z_tau=exp(-tau omega_plus) Z0 exp(-tau omega_minus).

Indeed evolving a vector (x,Z0x) gives (exp(tau omega_minus)x,exp(-tau omega_plus)Z0x), and the first component can be used as the new coordinate. This proves contraction of every Schatten norm of Z, including HS and nuclear norms, uniformly in tau. A graph truncation at singular rank r has tail bounded by its nuclear norm divided by sqrt(r+1) in HS norm. Orthogonal graph-projector reconstruction, rather than raw matrix truncation, keeps a physical covariance.

Trace class of Q-P_A alone does not bound ||Z0||1 uniformly: its singular values are tan(theta), while the projector estimate controls sin(theta). Angles arbitrarily close to pi/2 can make the graph norm arbitrarily large. A fully exchanged block prevents this chart entirely.

There is nevertheless a precise finite-exception statement at the INITIAL time. Pick an explicit eta in(0,1). At most ||Q-P_A||1/eta <87/eta one-particle singular directions have sin(theta)>eta. On the complementary principal-angle tail,

 sum tan(theta) <= (1/sqrt(1-eta²)) sum sin(theta),

with the consistent doubled multiplicities. Thus this initial tail has a controlled nuclear graph norm. This is an algebraic split, not yet a uniform dynamical split.

The obstruction is that the exceptional principal-angle subspace generally does not reduce omega_plus or omega_minus. Imaginary-time contractions mix its directions with the nominal tail. Removing its initial finite-dimensional span does not yield an autonomous graph equation on the remaining complement. One can retain the evolved exceptional columns exactly, but their changing orientation and orthogonalization against the graph require quantitative conditioning bounds. Neither trace class nor the stationary excitation estimate supplies those bounds. Conversely, if an additional finite-dimensional reducing exceptional subspace exists, the graph contraction argument applies to its invariant complement and gives a uniform tail bound without a global reference-overlap lower bound. No such reducing subspace is supplied for the actual gapless native bath.

A potentially implementable route is a moving finite-column chart: propagate the exceptional columns and a trace-class graph tail, then certify their Gram matrix and chart transitions. Its required new certificate is a lower singular-value bound for the evolving finite-column representation (or an overlap-free Grassmann error analysis). Simply asserting that finite exceptional modes stay separate would be incorrect. This identifies the remaining quantitative obligation without assuming a vacuum overlap, active spectral gap, or affordable rank.

## Proof block 6: Identifying the scalar impurity energy in the implemented Fock dynamics


Use h0=iK0, hA=h0+V, V=i Delta K, with the actual finite-rank self-dual impurity and P0=P_-(h0), PA=P_-(hA). The trace-class projector difference and its continuous coupling path were proved in TRACE_CLASS_IMPURITY_PROJECTOR.md (5654417a); no spectral gap at the Dirac node is assumed. The previous principal-angle construction supplies the impurity vacuum OmegaA in the original Fock space. Throughout, H0 is normal ordered relative to Omega0, with reference energy zero, and BA is the physical quadratic impurity, including its fixed normal-ordering constant.

#### Domains and generator comparison

In the explicit paired product, the reference excitation count is a finite exceptional integer plus twice a sum of independent Bernoulli variables with summable parameters sin²(theta_j). Its second moment is finite: the variance is at most twice the mean contribution from paired modes, and the squared mean is finite. Hence OmegaA lies in Dom N. Since h0 is bounded, the free many-body generator satisfies ||H0 psi||<=||h0|| ||N psi|| on Dom N; thus OmegaA lies in Dom H0. The finite-rank quadratic BA is bounded, so it does not change this domain conclusion.

The impurity Fock construction gives a strongly continuous quadratic dynamics generated by dGamma(omegaA), with vacuum energy zero and omegaA the positive one-particle excitation operator. Transport this dynamics to the original Fock representation using the explicitly constructed polarization change. Both its generator and H0+BA implement exactly the same CAR automorphisms, as follows from their quadratic commutators with the bounded Majorana fields. Their unitary groups therefore differ by a scalar character: their quotient commutes with every CAR operator, and the vacuum Fock representation is irreducible. Strong continuity and the group property give a real scalar c with

 H0+BA = c I + dGamma(omegaA)                    (1)

in the transported representation. This argument compares self-adjoint generators via their unitary groups; it does not subtract two unbounded operators on an unspecified core. OmegaA is in the physical domain by the preceding count bound and is the transported zero-energy vacuum, so c=<OmegaA,(H0+BA)OmegaA>.

#### Trace formula with the physical constant

For a finite-mode quadratic Majorana form H=(i/4)gamma^T K gamma, the covariance contraction is (1/2)Tr(hP), with h=iK and P=(I+iGamma)/2; Tr h=0. Finite-rank compression and the trace-class difference extend the reference-subtracted expression to the present problem:

 c=(1/2)Tr[h0(PA-P0)+V PA].                    (2)

All terms here are trace class. In particular VPA is finite rank, and h0 is bounded. Equation(2) retains the impurity constant fixed by the actual quadratic Hamiltonian, not a freely chosen zero of energy.

Set SA=sign(hA), S0=sign(h0); zero eigenvectors have already been excluded. Since PA=(I-SA)/2,

 |hA|-|h0|=V SA+h0(SA-S0)

is trace class. Also Tr V=0 for the imaginary antisymmetric finite-rank native perturbation. Substitution into(2) now gives

 c=-(1/4)Tr(|hA|-|h0|).                         (3)

This is a relative trace, not a difference of two infinite traces. The factor1/4 is the full Majorana/Nambu one-particle convention; it is not divided again by a parity or spectator multiplicity.

#### Equality with the native determinant integral

Let h_lambda=h0+lambda V. Differentiate the sign-resolvent integral directly. The derivative of its resolvent is -R_lambda V R_lambda. Near zero each perturbed local column is uniformly bounded by the bare local columns and the Woodbury inverse; at infinity the derivative is O(s^-2) in trace norm. These are uniform integrable bounds along lambda. Thus P_lambda is trace-norm differentiable, with derivative obtained under the sign integral. Differentiating P_lambda²=P_lambda shows that P_lambda' is off-diagonal relative to P_lambda. Since h_lambda commutes with P_lambda, cyclicity gives Tr(h_lambda P_lambda')=0. Therefore the already well-defined energy expression satisfies

 c_lambda'=(1/2)Tr(V P_lambda).

This direct argument avoids any unproved trace-norm endpoint convergence of regularized absolute-value differences. Integrate from lambda0, where c0=0.

The finite-rank determinant d_lambda(s)=det[(s-K_lambda)(s-K0)^-1] is positive on s>0 and at least1/9 on the full coupling interval. Jacobi's derivative gives its lambda derivative as the finite-rank resolvent trace. Pairing spectral parameters +is and -is and integrating gives

 Tr(|hA|-|h0|)=(2/pi) integral_0^infinity log d_1(s) ds,

and therefore

 c=-(1/(2pi)) integral_0^infinity log d_1(s) ds = Delta E_A. (4)

For completeness, the interchange can be taken first on epsilon<=s<=R and lambda in[0,1]. Near zero the actual local resolvent compression and the inverse Woodbury bound uniformly bound the lambda derivative of log d; at infinity its potentially1/s term is Tr V=0 and the remainder is O(s^-2), uniformly in lambda. These are integrable envelopes, so epsilon->0 and R->infinity commute with the lambda integral. The normalization also follows directly from a conjugate spectral pair: integral log[(s²+a²)/(s²+b²)]ds=pi(a-b), while that pair contributes2(a-b) to the absolute-value trace.

Consequently the already certified INFINITE impurity energy lower bound applies to the scalar in(1). This closes the normalization needed for e^-tau DA=e^-tau DeltaEA Gamma(e^-tau omegaA), and hence the uniform absolute-error compression estimates. No finite-volume version of the infinite lower bound, reference-overlap positivity, determinant square-root phase, or physical numerical evaluation is inferred.

#### Dependency record

Load-bearing inputs: the actual native quadratic/CAR convention and finite-rank impurity; trace-class and coupling-continuity proof5654417a; the source-bound independent review041748c1; the explicit principal-angle/Fock product extension21400ab0; and the native pair determinant integral/Green bounds in native-infinite-star-node-stretch/UNIFORM_PAIR_GAP.md. The new argument is the domain, scalar-generator and relative-energy bridge. It introduces no altered Hamiltonian or new gap premise.

## Proof block 7: Uniform absolute-error quench compression without an overlap denominator


#### Initial approximation in the stationary impurity Fock space

Use the explicit principal-angle construction from FOCK_AND_QUENCH_EXTENSION.md, now expressing the original vacuum Omega in the impurity-vacuum representation. Projection symmetry gives the same trace bound L=87 in either direction. Retain every fully occupied exceptional mode (there are fewer than L), and order the remaining paired angles by decreasing s_j=sin(theta_j). Their doubled projection trace contributions are4s_j, so in particular sum s_j<=L is a conservative bound independent of conventions about counting pairs.

Let Omega_r retain the first r paired creation factors and all fully occupied exceptional modes, replacing every other paired factor by its empty factor. It is normalized and finite-excitation, with at most2r+L occupied-mode capacity. Fix its phase through the explicit ordered paired product, so

 <Omega_r,Omega>=product_(j>r) sqrt(1-s_j²)>=0.

This is an overlap with the APPROXIMATED ORIGINAL STATE, not a presumed nonzero overlap between the two vacua. All angle-pi/2 exceptions have been retained, so none are discarded in this product. The omitted paired factors have even parity and therefore the truncation preserves relative parity.

From descending order, s_(r+1)<=L/(r+1), and

 sum_(j>r) s_j² <= L²/(r+1).

Using product sqrt(1-x_j)>=1-sum x_j whenever the latter is positive (otherwise use the trivial nonnegative bound) gives

 ||Omega-Omega_r||²=2[1-product_(j>r)sqrt(1-s_j²)]
 <=2 sum_(j>r)s_j² <=2L²/(r+1).                 (1)

Thus r+1>=2L²/epsilon² guarantees initial Fock error at most epsilon. This is constructive mathematically, but the coarse constant makes it unsuitable as a claim of affordable rank. The actual singular tail could improve it only after certification. No root determinant branch is chosen numerically in this argument; phase is fixed by the paired-product construction or an equivalent continuous lift.

#### Uniform unnormalized propagation

In the impurity representation the actual quadratic Hamiltonian has

 D_A=Delta E_A+dGamma(omega_A), omega_A>=0,

with its scalar impurity ground-energy difference retained. Its implemented constant must be the actual normal-ordering energy, not an arbitrary scalar from one-particle diagonalization. The reviewed positive impurity energy bound gives Delta E_A>=delta. Therefore

 ||exp(-tau D_A)(Omega-Omega_r)|| <=exp(-delta tau) epsilon. (2)

There is no conditioning factor and no division by a reference overlap or evolved norm. Finite excitation number is preserved: each occupied orbital is propagated by the one-particle contraction exp(-tau omega_A), and a k-particle wedge is propagated by its k-fold exterior power. The vectors need not remain orthonormal. Their wedge/product representation and Gram determinants can be retained without normalization. Orthogonalizing them is an implementation choice whose errors must be certified, not a condition for the mathematical bound.

For the overlap kernel with normalized initial approximants independently constructed for A and C,

 |<E_C(t)Omega,E_A(s)Omega>-<E_C(t)Omega_rC,E_A(s)Omega_rA>|
 <=exp[-delta(t+s)](epsilon_C+epsilon_A).        (3)

The two impurity representations must be compared through their physical common CAR/Fock representation, including relative lift phases. Formula (3) does not compute that comparison for free. It isolates an overlap-free error budget. Analogous bounded-insertion estimates cost the insertion norm when the approximated vectors are directly on its two sides. The complete node's internal insertion integrals still require the corresponding source-state approximation/propagation, and are not automatically covered by merely evaluating (3).

#### Why normalization cannot have the same bound

A two-level even-sector counterexample is sufficient. Let D=diag(delta,delta+g), g>0, and psi_epsilon=epsilon|0>+sqrt(1-epsilon²)|2>, while phi=|2>. Their initial distance tends to zero with epsilon. At large time the normalized evolution of psi_epsilon tends to |0>, but that of phi remains |2>; their distance tends to sqrt2. Absolute unnormalized evolution obeys (2) throughout. Thus an error bound for normalized states independent of their surviving norm is false, even for a positive gapped quadratic two-mode model. This does not obstruct the unnormalized kernel route.

#### Concrete remaining inputs

The route genuinely eliminates the earlier need to isolate an invariant exceptional subspace or bound a normalized moving-chart Gram matrix. It needs certified impurity principal-angle tails and their orbitals, a phase-consistent map into the common representation, the scalar Delta E_A, and a certified one-particle contraction on the retained finite orbital set. The stationary projector trace bound proves existence but its universal rank estimate is very large: L87 gives r+1>=15138/epsilon². No physical computation, affordable-rank claim, or alpha-sign inference is made. A controlled low-rank approximation to the actual stationary projector and its energy is now a precise alternative to finite-time normalized chart compression.

## Proof block 8: Raw nuclear approximation to uniform unnormalized Ward accuracy


Inputs: LOW_RANK_PROJECTOR_CERTIFICATE.md source943237a3cabc4346fd8c7d9191833e77ea14a4dda249195b632eb92f86aa062a, independently reviewed in native-impurity-lowrank-cold-review/REVIEW.md; the explicit Fock product and bounded Ward identities in this campaign. This is a mathematical combination, not a numerical extraction of principal angles.

Suppose D=P_A-P0 has a rank-k approximation Q with ||D-Q||1<=eta<1. Best rank-k approximation in nuclear norm gives sum_(j>k)s_j(D)<=eta. This can be proved by compressing onto the orthogonal complement of the k-dimensional output of Q and using the singular-value variational principle. No rounding of P0+Q is needed for this inference.

Choose canonical particle-hole principal blocks ordered by decreasing angle and retain every block intersecting the first k singular directions. A paired creation block has four singular directions with common value sin(theta), and uses two fermion modes. A fully swapped mode has two singular directions of value1 and uses one mode. Within a degenerate eigenspace choose these canonical blocks first; there is no need to retain the entire accidental spectral degeneracy. Completing the final intersected block adds at most three directions. Thus the retained one-particle dimension is at most k+3, and its fermion-mode count is at most floor((k+3)/2). For k2352 the safe bound is1177 fermion modes. All swapped modes are retained because any omitted singular value1 would contradict eta<1. This is a principal-angle carrier, distinct from the quadrature-column carrier and not a recipe for obtaining its basis cheaply.

The omitted paired angles obey 4 sum_tail sin(theta)<=eta, in particular sum_tail sin(theta)<=eta. Therefore sum_tail sin²(theta)<=eta² and the explicit product construction gives the safe bound

 ||Omega-Omega_r||<=sqrt(2)eta = epsilon.         (1)

(The multiplicity4 permits a stronger constant, but no downstream estimate here uses it.) Parity is preserved, and phase is fixed by the original-state product overlap, not by a possibly zero impurity-vacuum overlap. The rank and error are theoretical consequences of the raw Q certificate; they do not claim that Q's singular vectors themselves are the exact principal vectors of D.

#### All terms of the two-inverse Ward observable

Use the independently rederived identity

 8alpha=sum_disjoint [3<RC RA> +1/2<RC gamma0(WA-WC)RA>
 -1/2<WC RC gamma0 RA> -1/2<RC gamma0 RA WA>].

For each impurity choose a normalized Omega_rA satisfying (1). Propagate Omega_rA under its exact DA. For the left boundary term also propagate WC Omega_rC under DC; for the right boundary term propagate WA Omega_rA under DA. These odd source states differ from the exact ones by at most ||WA||epsilon_A. Applying a single linear CAR field to a finite-mode state adds at most one additional orbital to its excitation carrier; an annihilation term changes coefficients but does not require an infinite set of new orbitals. All such sources are propagated unnormalized.

Semigroup contraction and integration give, for one ordered pair, a total Ward error at most

 delta^-2 [3 + (||WA-WC||+||WA||+||WC||)/2]
             (epsilon_A+epsilon_C)
 <=delta^-2(3+||WA||+||WC||)(epsilon_A+epsilon_C).

This uses ||gamma0||=1 and normalized original/approximant vacua; source norms are bounded by the relevant W norm. With ||WA||,||WC||<=4.6, epsilon_A,epsilon_C<=sqrt2 eta, the full90-word alpha error is at most

 (90/8) * (61/5) * (2sqrt2 eta) /delta².        (2)

No inverse-cube error appears. This is only the state-compression error: errors in scalar impurity energies, orbital propagation, principal-angle extraction, W tails, and common-representation overlaps must be added separately. The bound can use whichever impurity gap has actually been certified; it does not infer a finite-volume gap from an infinite one.

At eta=2287839703834313821/4000000000000000000000000 and k2352, formula(1) is below8.1e-7. The rank increases only through the reviewed polylogarithmic quadrature choice as eta decreases. Thus there is a rigorous polylogarithmic EXISTENCE bound for a finite-excitation approximation with uniform unnormalized propagation error. It is not a polynomial-time or384MiB representation: a generic state on1177 fermion modes would be enormous. A Gaussian/wedge representation, certified angle extraction, and phase-consistent cross-impurity evaluation remain essential computational obligations. No physical matrix, spectrum, or quench was evaluated here.

## Supporting evidence and limitations

The paired stdlib runner checks rational constants, actual noncommutative Ward expansion, principal-angle tail/fidelity examples and finite scalar-energy normalization. Wrong Ward onsite coefficient and wrong scalar-energy factor are actual algebraic adverse controls. These finite controls do not prove the infinite spectral theorem, implementability or convergence arguments; those are supplied in the proof above and require independent source review. No physical spectra, resolvents, quench or alpha evaluation are run.
