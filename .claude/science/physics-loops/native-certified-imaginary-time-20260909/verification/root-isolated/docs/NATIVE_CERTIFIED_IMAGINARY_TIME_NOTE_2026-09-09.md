---
claim_id: native_uniform_reference_imaginary_time_chart
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
runner: scripts/native_certified_imaginary_time_2026_09_09.py
---
# Uniform reference chart for native impurity imaginary time

In the supplied infinite cubic pi-flux model, let D_A be the actual quadratic Hamiltonian relative to the reference vacuum after a selected pair of link flips. For every finite t>=0, its normalized evolution of the reference vacuum has real skew reference pairing Z_ref(t), and

 **||Z_ref(t)|| <= 99/100.**

This is an all-time analytical statement, not an executed native propagation. The model and CAR convention, finite relative energy, and stationary chart estimates are imported from the finite-excitation Ward and pair-vacuum-chart theorems. This note proves the uniform reference-chart improvement and states a separate exact-data positive-band approximation corollary. It computes neither a kernel nor alpha, and establishes no practical cost or roundoff bound.

## Precise imports

The parent pair-chart theorem supplies the real reference polar-frame matrix D=S−2ub^T, where S is bounded, positive and injective but gapless. The local vectors a=S^-1/2u and d=S^-1/2b exist and satisfy a^T d=1/3 and 2||a||||d||<=33/25. It also supplies a positive reference overlap for the actual impurity vacuum, a real stationary pairing of operator norm <=sqrt(347/349), and squared Hilbert–Schmidt norm <87. The finite-excitation Ward theorem identifies D_A with the actual reference-normal-ordered quadratic operator, including its finite reference-normal-ordering scalar c_A. The separate impurity-ground-energy shift is denoted E_A below; these two constants are not identified. These are load-bearing supplied-model results, not newly selected microscopic axioms.

The load-bearing canonical imports are [the pair-vacuum chart](NATIVE_PAIR_VACUUM_CHART_NOTE_2026-09-09.md) and [the finite-excitation Ward theorem](NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md). The exact research proofs and independent reviews are preserved in the paired inputs provenance directory; their historical prospective statements do not override this note's present analytical scope.

## Hamiltonian signs and invariant disk

Write f=(a_M+ib_M)/2 for the reference Majoranas (the subscript distinguishes them from the local weighted vectors). Set H=(D+D^T)/2 and K=−(D−D^T)/2. Ordered CAR expansion of i a_M^T D b_M/2 gives f†Hf+(f†Kf†+fK^Tf)/2, apart from the scalar. Consequently the vacuum-normalized Gaussian exponential has pairing equation

 Z′=−K−HZ−ZH−ZKZ, Z(0)=0.                         (1)

For H=mu I,K=kJ,Z=zJ the equation is z′=−k−2mu z+kz², fixing the creation sign.

The weighted bounds give H>=S/150. The normalized skew form has norm ||ad^T−da^T||<=33/50, so for real v,w,

 |v^TKw|<=99 sqrt(v^THv) sqrt(w^THw).               (2)

No inverse of H on the whole space or positive spectral gap is used. Let r=99/100, M=r²I+Z², and A=H+ZK. Direct differentiation yields

 M′=F−AM−MA^T,
 F=2r²H−2ZHZ−(1−r²)(KZ+ZK).                      (3)

For a0=v^THv and b0=(Zv)^TH(Zv), equation (2) proves

 v^TFv >=2r²a0+2b0−198(1−r²)sqrt(a0b0)
       >=[4r−198(1−r²)]sqrt(a0b0)>=0.

Indeed 2r−99(1−r²)=99/10000>0. This forcing is positive for every real skew Z, without assuming the disk. The variation-of-constants formula for (3) consists of positive congruences, starting from r²I. Hence M>=0 and ||Z||<=r throughout each local solution. Bounded H,K and this operator norm bound prevent finite-time blowup of the locally Lipschitz equation. The argument applies directly in infinite dimension.

## Trace ideal and identification with actual evolution

K has finite rank. On the disk,

 ||Z′||1 <=||K||1+(2||H||+r||K||)||Z||1.

Thus the solution belongs to the trace ideal at every finite time. To make the identification constructive mathematically, choose increasing real finite-rank projections Pn and compress Hn=PnHPn, Kn=PnKPn. Their form inequality (2) and disk estimate are unchanged. Hn converges strongly with uniform bound; Kn converges in trace norm. On compact time intervals the limiting continuous trace-class trajectory makes (Hn−H)Z and Z(Hn−H) converge uniformly in trace norm. The integral equations and Gronwall prove Zn→Z in trace norm there. Gaussian exterior series and their Fredholm normalization therefore converge.

On each finite particle sector dGamma(Hn) converges in the semigroup sense to dGamma(H); positivity and density extend this to Fock space. Pair creation and annihilation for trace-class K are bounded operators, and Kn gives convergence in operator norm. Bounded-perturbation semigroup convergence identifies the limiting Gaussian vector with the actual quadratic evolution. The finite relative scalar affects normalization only; the positive reference anchor fixes phase. This proves the claimed reference pairing bound for the actual normalized state, rather than only for an abstract Riccati solution. It gives no rate for a discretized H or K.

## Separate positive-band constructive corollary

In the impurity frame let H_+ be the exact positive excitation operator, with spectrum in [0,6h], and Z_A the reference vacuum pairing in that frame. Exact evolution is

 Z_A(t)=e^-tH_+ Z_A e^-tH_+^T,
 log||e^-tD_A Omega0||=−tE_A+¼Tr log(I+Z_A(t)†Z_A(t))−¼Tr log(I+Z_A†Z_A).

Both propagators are contractions. This is a different chart from the primary theorem. It still needs the finite E_A to evaluate unnormalized kernels.

Let U contain the seven center/neighbor seeds and let W0 span exact P_+R0(z)U at finitely many poles. Since the impurity perturbation has range in U,

 h_A W0 subset W0+span(P_+U).

Therefore W_m=W0+span{h_A^jP_+U:0<=j<m} contains all degree-m polynomial images of W0 and has dimension at most dim W0+7m, per impurity. Exact positive-band membership is essential: uncontrolled negative-band leakage invalidates contraction estimates.

For an exact isometry V onto W_m (or an enlarged exact positive-band space containing all the required polynomial images), A=V†h_AV>=0 and R=(I−VV†)h_AV satisfy R†R=V†h_A²V−A². Duhamel bounds vector error by the integral of ||R e^-sA x|| and pairing Hilbert–Schmidt error by twice the integral of ||R e^-sA Z||HS. Initial truncation, frame uncertainty and arithmetic error must be added.

At t<=100/h, mapping [0,6h] to [-1,1] and using Bernstein ellipse rho=3/2 bounds the degree-m exponential tail by delta_m<=6e^25(2/3)^(m+1). The exact rational upper bound 6*3^25*(2/3)^129<10^-10 proves that degree128 suffices. For an initial pairing supported in W0, Galerkin polynomial equality on W0 then gives semigroup error <=2delta_128 and pairing error <=4delta_128||Z_A||HS<4*10^-9, with at most 896 added seed directions per impurity.

Any initial pairing tail outside W0 is a separate error. These last numbers describe only polynomial truncation under exact positive-band, Gram and moment data. They are not total achieved errors. For real pairings in a common positive-anchor frame, normalized Fock-vector error is at most ||Delta Z||HS/sqrt(2), from the Gaussian differential metric. Separately approximated vacua, phases and the scalar energy require their own bounds.

## Evidence and unresolved numerical obligations

The supporting runner checks exact synthetic 2/4-mode ordered CAR and Lyapunov algebra, the rational disk margin and degree128 budget, and explicit adverse comparisons. These are small finite supporting controls, not tests of native evolution. The theorem requires neither an eigensolver nor a physical oracle.

A future actual propagation must certify source/Gram data, positive-band or reference-frame approximation errors, scalar normalization and signed cross contractions. The disk does not yield a dimension-free vacuum determinant bound, a stable long-time numerical Lipschitz constant, or positive cross-impurity kernels. No phase closure or alpha value is claimed.
