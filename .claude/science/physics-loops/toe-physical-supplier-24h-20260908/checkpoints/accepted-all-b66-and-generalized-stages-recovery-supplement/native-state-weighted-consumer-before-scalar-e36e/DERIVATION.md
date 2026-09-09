# Occupation-weighted propagation for finite-excitation Ward inputs

Status: new source-only conditional theorem. No native matrices, histories, scalar outputs or probes. The original uniform leakage exclusion is unchanged. This is a new sufficient certificate for specified inputs, not a weakening of the uniform1e-12 gate.

## 1. Review of the root one-body theorem

The root DERIVATION bound2c839 is mathematically sound under its stated isometric-domain premise. Duhamel sign, the two real-time signs, Poisson normalization and tail4||X||atan(t/S)/pi are correct for both operator and HS norms. Nonorthogonal B=G^-1J is G-skew and L=D+JG^-1J is exactly the residual Gram. The resolvent identity has a minus sign and denominator|Im z|. For unbounded H, each finite V column in D(H) suffices; the residual is bounded finite rank and finite evolution makes Duhamel legitimate. No positive-band assertion follows from this alone.

An initial vector outside the represented span introduces its projection error: for contractions T=e^-t|H| and U=V e^-t|A| V*, ||Tf-Uf|| <= ||(1-P)f|| + ||(T V-V e^-t|A|)V*f||. This is a separate initial-source gate. A pointwise small residual at time zero does not control its finite evolution.

## 2. Fock derivative: the useful stronger consumer bound

Let E be a finite-dimensional input one-particle space with orthonormal basis e_i, F an output one-particle Hilbert space, and T,U:E→F contractions. Let Gamma(T) denote the exterior-algebra second quantization, acting identically on the vacuum. It is a contraction, without any invertibility assumption. For any finite Fock vector Phi,

 Gamma(T)Phi-Gamma(U)Phi
 = integral_0^1 sum_i a†((T-U)e_i) Gamma(U+lambda(T-U)) a(e_i)Phi d lambda.

Proof: on a decomposable q-particle wedge, differentiate the q factors. Moving the annihilator through the wedge gives exactly the replacement-factor signs; linearity proves the formula. The convex interpolant is a contraction, so its second quantization has norm at most1. CAR gives ||a†(v)||=||v||. Consequently

 ||(Gamma(T)-Gamma(U))Phi||
 <= sum_i ||(T-U)e_i|| ||a(e_i)Phi||.                 (1)

For a unit vector write n_i=||a(e_i)Phi||². This is the explicitly occupation-weighted bound sum_i sqrt(n_i) e_i(error). Cauchy-Schwarz also yields ||T-U||_HS sqrt(<N>_Phi). Neither statement requires a normalized output, a determinant denominator, a positive overlap floor, or an entrywise coefficient precision gate. The usual q||T-U|| bound is another consequence of tensor telescoping; (1) can be substantially more useful for decaying occupations.

The theorem extends to an infinite input basis if the displayed series converges: truncate Phi in particle/mode number, apply the finite theorem, and use contractivity plus the summable bound. For implementation, finite truncation is simpler and its Fock norm error must be added explicitly.

## 3. Stationary Gaussian input and the reviewed trace-class premise

In the exact impurity stationary positive-energy Fock representation, take a finite paired-angle truncation of the reference vacuum:

 Phi=product_j(cos(theta_j)+sin(theta_j)a†(e_2j-1)a†(e_2j)) Omega_A,

with phases absorbed in the pair amplitudes and the chosen exact implementer lift. Each paired mode has occupation sin²(theta_j). Fully swapped single modes have occupation1 and are retained. In this natural basis

 sum_i sqrt(n_i)=2 sum_j sin(theta_j)+number_of_swapped_modes
               = (1/2)||P_A-P_0||_1

for the retained blocks, or <= that quantity when a tail is dropped. The factor follows from four singular values sin(theta) per paired block and two unit singular values per fully swapped mode in the particle-hole doubled projector. Thus the reviewed native trace-class bound<87 supplies a coefficient<43.5 multiplying the largest SPECIFIED MODE error, not the residual norm on an unrelated trial span. Keeping the actual individual occupations and errors is better. This uses the exact same PH multiplicity convention as the finite-excitation theorem; no new trace bound is computed here.

If an initial finite truncation Phi approximates the physical reference vector by epsilon0, contractivity adds epsilon0. Its phases must be inherited from the original principal-angle/Fock construction; arbitrary independently chosen stationary vacuum phases cannot be ignored in cross-impurity matrix elements.

## 4. Making the one-body approximation a legitimate Fock map

Actual stationary propagation is T_A(t)=exp(-t omega_A) on the impurity positive one-particle space. The root theorem can be applied to signed H_A with |H_A|, but the lifted compressed approximation may leave that positive space. Define U_A(t)=P_A^+ V exp(-t|V*H_AV|)V* restricted to the finite input space. This is a contraction into the correct output space. Since actual T_A(t) stays in P_A^+, projection cannot enlarge its vector error. Therefore (1) applies directly using the root one-body error bounds for each input column, plus any initial projection error.

This is an exact mathematical construction, not an assertion that P_A^+ is numerically available for free. Either its projected columns and cross-Grams must be independently certified, or a separate projector approximation error must be added. Omitting this projection and calling the result an impurity Fock state would be a gauge/domain error. The original24 selected span may fail to approximate the required natural-angle modes: nothing in this theorem asserts otherwise. The finite-excitation existence rank1177 is not an achieved24-mode representation or a feasible cost claim.

On finite inputs the resulting states are exterior-algebra polynomials in propagated columns. Their overlaps can be computed from cross-Gram minors with phases fixed by the original exterior lift; singular output Gram matrices are allowed. No artificial Gram inverse is required for this unnormalized representation. Actual cross-Gram and arithmetic certificates remain necessary.

## 5. CAR insertions and actual Ward-word structure

For a bounded CAR linear field L and any input basis mode,

 a(e_i)L Phi = -L a(e_i)Phi + {a(e_i),L}Phi.

Therefore ||a_i L Phi|| <= ||L|| ||a_i Phi|| + |{a_i,L}| ||Phi||. The coefficient vector of the anticommutators has l2 norm bounded by the creation part of L. Substitution in (1) gives

 error(L Phi) <= ||L|| sum_i e_i(error)||a_i Phi||
                 + ||T-U||_HS ||creation_coeff(L)||_2 ||Phi||.       (2)

Iterating this exact inequality covers every finite product of local CAR insertions and the bounded Ward linear field (its certified norm can be inserted, e.g.4.6 in the established normalization). It does not assume an l1 bound for arbitrary coefficient vectors. The new finite input space must include the projected creation/annihilation directions of those fields; omitted directions get separate initial-source errors. Finite-degree insertions do not require a global normalized Gaussian determinant to use (2).

Switching impurity species changes the stationary representation. Applying (1)/(2) separately at each stage requires the actual upstream state represented or approximated in that stage's Fock space with certified phase and truncation error. The existing mixed-vacuum theorem supplies an abstract interface, not its numerical realization. Thus no claim is made that the90 Ward terms reduce automatically to the current24 columns.

## 6. Resolvent and observable errors without normalization

With the already identified scalar energy c_A and D_A=c_A+dGamma(omega_A), a unit input with finite approximation error epsilon0 has unnormalized semigroup error at most

 e^-t c_A [epsilon0 + sum_i sqrt(n_i) e_i(t)]

for the same exact scalar and stationary vacuum. A scalar approximation adds t|delta c| exp(-t min(c,chat)) times the input norm. Integrating in t gives a resolvent-on-input error provided c_A>=delta>0; no many-body gap beyond the existing delta premise is introduced. The bound is epsilon0/delta + integral_0^infinity e^-delta t sum_i sqrt(n_i)e_i(t)dt, plus the scalar term |delta c|/min(c,chat)^2. If the approximate finite state has norm<=1, no overlap division appears.

For a concrete Ward word with m resolvents and bounded insertions B_j, telescope from the input side. At each replacement use the certified error for THAT exact or already-approximated incoming vector; bound the remaining exact factors by product_j||B_j|| delta^{-(remaining resolvents)}. Sum over the actual signed word coefficients in absolute value. This is a complete error rule once the finite inputs and their errors are supplied. It does not exploit cancellations or infer alpha's sign.

A particularly concrete alternative is to certify ||R(A-z)^-1 X|| directly from the residual Gram for the specified rational source bank. This avoids a uniform leakage bound and avoids certifying a whole reduced time orbit. Turning finitely many such certificates into exp(-t|H|) still requires a declared rational approximation/remainder. For Ward resolvents of D_A, a one-body complex-resolvent certificate alone is not a many-body resolvent certificate; the Fock/Laplace steps above supply the missing interface.

## 7. What this resolves and does not

The downstream sufficient condition can be occupation-weighted mode propagation plus explicit finite-state/projection/scalar errors. There is no requirement to make every C entry narrower than an unrelated cutoff or to overcome the observed large uniform leakage. However actual weighted residuals may also be large. No native mode, occupation, leakage value, Gaussian overlap or observable was evaluated. This is a new conditional method whose next numerical prerequisites are explicit, not an achieved physical result.

## 8. Interface to the parallel commuting-majorant construction

Let w_i=||a_i Phi|| and M=sum_i w_i. Weighted Cauchy gives sum_i w_i e_i <=sqrt(M)*sqrt(sum_i w_i e_i²). For projected input coordinates c_i, use the positive finite covariance D_w=sum_i w_i c_i c_i*. This avoids selecting numerical square roots of w_i. A certified commuting residual majorant W>=L with B*W+WB=0 gives weighted residual sum_i w_i ||R exp(tB)c_i||² <=Tr(W D_w), for either time sign. The initial projection defect contributes sum_i w_i||(1-P)e_i||². The root's HS Poisson estimate applies to the abstract column matrix with columns sqrt(w_i)c_i; these products can be evaluated entirely as traces against D_w.

This supplies a concrete occupation-weighted finite objective rather than a uniform leakage gate. W and D_w remain actual certificates to acquire. James independently develops the exact polynomial commuting majorant; its proof/source is not silently imported as an already reviewed numerical result. The natural paired-mode w_i and their projection covariance remain missing numerical inputs, so the current24 result is neither sufficient nor refuted for this new objective.

The supporting38 exact toy predicates check the two-mode exterior derivative and occupation-weighted inequality for rational contraction matrices. They validate algebraic controls, not the infinite Fock proof or native occupation data.
