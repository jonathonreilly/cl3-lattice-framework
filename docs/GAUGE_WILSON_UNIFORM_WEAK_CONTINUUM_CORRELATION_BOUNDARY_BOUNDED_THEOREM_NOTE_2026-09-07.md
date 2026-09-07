---
claim_id: gauge_wilson_uniform_weak_continuum_correlation_boundary_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
bodyType: bounded_theorem
runner: scripts/gauge_wilson_uniform_weak_scaling_controls_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07
  - gauge_wilson_electric_dominated_volume_uniform_gap_bounded_theorem_note_2026-09-07
  - gauge_wilson_local_observable_finite_region_pw_approximation_bounded_theorem_note_2026-09-07
  - gauge_wilson_selected_infinite_static_source_sector_bounded_theorem_note_2026-09-07
claim_scope: "Uniform imported weak-window clustering excludes specified polynomially normalized separated local correlations; actual u=0 Haar plaquettes nevertheless admit nonzero Gaussian contact finite-dimensional distributions. Conditional gap/LR scale comparison only."
---

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

In one uniformly controlled weak-electric-coupling window, bounded fixed-neighborhood lattice fields with polynomial norm renormalization have connected ground correlations vanishing faster than every power of spatial spacing at distinct physical points. The same holds for separated smearing families with polynomial total weighted norms. This is a conditional boundary for that field construction, not a prohibition of all continuum limits.

The distinction is sharp inside the supplied model: at exactly u=av=0, disjoint actual Haar plaquette traces with central-limit normalization converge in finite-dimensional distributions to nonzero Gaussian contact statistics. No tightness or convergence in a topology of random distributions, dynamics or propagating quantum field is claimed. A separate scale comparison uses an LR upper parameter and a gap lower bound without identifying either with a measured signal speed.

The [compact Hamiltonian source](GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md) fixes the supplied model. The [uniform gap source](GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md) and [locality source](GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md) supply the two bounds used only in the conditional scale comparison. The [selected GNS source](GAUGE_WILSON_SELECTED_INFINITE_STATIC_SOURCE_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-07.md) fixes the consistent whole-range neutral representation; no periodic/empty-boundary state identification is assumed. The direct clustering import is Yarotsky0411042 equation16, explicitly described below.

The [scaling helper](../scripts/gauge_wilson_uniform_weak_scaling_controls_2026_09_07.py) performs18 exact degree, norm-budget and clock-ratio controls. The [contact helper](../scripts/gauge_wilson_haar_contact_fdd_controls_2026_09_07.py) performs13 exact actual-plaquette and Taylor-constant controls. These are not numerical convergence validations or computations of a physical coupling threshold. The [durable packet](../.claude/science/physics-loops/uniform-weak-continuum-boundary-20260907/PROOF_REVIEW.md) preserves complete independent proofs, original source-alignment/FDD wording, exact corrections, reviews and raw outputs.

The following main derivation is retained in full, followed by the complete independent contact proof with explicit constants. The main contact construction uses spacing2 in a unit box; the independent version uses spacing3 and compactly supported tests on all of R³. Both use their corresponding coarse mesh in the normalization and prove the same type of FDD sharpness result. Shared candidate exposure preceded independently frozen proofs; no blind-discovery claim is made. Root's separately reviewed optional third/fourth moment and finite-mesh skew formula remain evidence, not an additional canonical claim or fitted result.

# A precise continuum-correlation boundary inside a uniform weak-electric window

2026-09-07. Prospective contract preceded this proof. Root exposed the proposed exponential-versus-polynomial argument; no completed root proof has been read. This is an elementary scaling consequence of explicit imported clustering, not a new generic clustering theorem or a prohibition of all continuum limits.

## 1. One consistent supplied model and a uniform window

Take the compact SU3 cubic-link Hamiltonian already specified in the campaign, with a>0, v>=0, u=av, all fixed elementary plaquettes, and full link Hilbert spaces. The parameter a is a supplied kinetic/temporal-scaling parameter, not spatial spacing. Spatial spacing ell>0 is introduced independently as an embedding of the unchanged combinatorial lattice into Euclidean space. Parameters a_ell,v_ell may vary, but assume 0<=u_ell<=u_* in ONE sufficiently small fixed window.

Use the selected neutral ground state from the fixed whole-range finite restrictions of Yarotsky0411042 Theorem2. Section2 equation16 gives exponential connected correlations for this same state; its constants can be chosen uniformly by fixing the activity/decay parameter first and choosing u_* below the corresponding smallness threshold. In outgoing-cell scaled units the onsite operator h_z=(a/4)K_cell,z is independent of a, while the centered perturbation has norm at most3u/4. Hence arbitrary variation of a does not change this uniform ground-state bound. Explicit primary source: https://arxiv.org/pdf/math-ph/0411042 , equation16 and its Section2 convention that the decay parameter can be fixed by uniformly small perturbation norm.

Thus there are fixed C>=1 and mu>0 such that for bounded local operators supported on finite cell sets I,J,

 |omega_ell(AB)−omega_ell(A)omega_ell(B)|
 <= C^(|I|+|J|) ||A|| ||B|| exp(−mu dist(I,J)).       (1)

The distance is a fixed lattice metric, with fixed geometric conversion to Euclidean cell positions. For the usual nearest-neighbor metric it dominates Euclidean separation of cell centers. Any fixed-range metric changes mu by a constant only.

Independently, Yarotsky0412040 Theorem1(3)/Section2 supplies the analogous result for its periodic-selected ground state after the four-cell classical-block applicability map. https://arxiv.org/pdf/math-ph/0412040 . That is a separate version. No identification of two boundary-selected representations is required here: use0411042 directly when combining(1) with the reviewed gap/GNS model. Neither pointwise analyticity in u nor a family of nonuniform clustering estimates suffices for the theorem below.

## 2. Fixed-support fields at positive physical separation

Let A_ell,B_ell have at most m_A,m_B cells of support, lying within fixed lattice radii D_A,D_B of cell centers x_ell,y_ell. Suppose their physical centers ell x_ell,ell y_ell approach different points at Euclidean separation r>0. For sufficiently small ell,

 dist(I_ell,J_ell)>= r/(2ell)−D_A−D_B.

If ||A_ell||<=K_A ell^(−p) and ||B_ell||<=K_B ell^(−q), with fixed finite p,q>=0, (1) implies

 |connected(A_ell,B_ell)| <= K ell^(−p−q) exp(−mu r/(2ell)).       (2)

For every fixed M>=0 the right side is o(ell^M). Indeed setting s=1/ell reduces the logarithm to (p+q+M)log s−(mu r/2)s, which tends to minus infinity. Multiplicative field renormalizations of polynomial growth are included in the norm hypothesis. Subtracting scalar counterterms does not affect the connected correlation; the hypothesis may instead be imposed on chosen representatives modulo scalars.

This rules out a nonzero separated-point connected limit for this specified class under the uniform-window hypothesis. It does not bound truly unbounded local operators merely from their formal names or low-state moments. Operator-norm control, or a separate replacement theorem, is necessary.

## 3. Separated smearing sums

Let A_ell(f)=Σ_i alpha_(ell,i) A_(ell,i) and B_ell(g)=Σ_j beta_(ell,j) B_(ell,j), finite sums at every ell. Assume each constituent obeys the same uniform support-size/radius and polynomial norm bounds, and all physical centers in the first sum remain separated by r>0 from all centers in the second. Suppose Σ_i|alpha_(ell,i)|<=K_f ell^(−s) and Σ_j|beta_(ell,j)|<=K_g ell^(−t). Bilinearity and the triangle inequality give

 |connected(A_ell(f),B_ell(g))|
 <= K' ell^(−p−q−s−t) exp(−mu r/(2ell))=o(ell^M)

for every M. The number of summands need not be separately bounded: their total absolute weights are what is priced. Ordinary compact-support Riemann sums have polynomial counts and satisfy this condition. We do NOT apply C^(support volume) to the union of all smearing sites, which would discard the useful estimate.

The hypothesis requires two positively separated physical support regions. It says nothing about overlapping smearing regions, coincident-point singularities or distributions supported on the diagonal. More generally the same proof works if the logarithm of all norm/coefficient/support-prefactor costs is o(ell^−1) and the physical support radii shrink to zero; no such broader condition is silently assumed for macroscopic Wilson loops or volume-supported observables.

## 4. An actual contact-limit adverse to an overbroad no-go

At u=0 the neutral ground is product Haar. Choose N=n³ disjoint elementary xy plaquettes anchored at (2i,2j,2k), 0<=i,j,k<n, and set ell=1/(2n). Their physical anchors are(i/n,j/n,k/n) in the unit box. Their link sets are disjoint. Let J_k=ReTr(U_plaquette,k)/3. Haar orthogonality and fundamental center charge give omega(J_k)=0 and omega(J_k²)=1/18. The variables X_k=sqrt18 J_k are independent, centered, bounded by sqrt18, and have variance1.

For a real continuous test function f on the unit box put F_n(f)=n^(−3/2)Σ_k f(k/n)X_k. Its variance is n^(−3)Σ_k f(k/n)², tending to integral f²; for f=1 it is exactly1 at every n. The total coefficient l1 norm is at most n^(3/2)||f||_infinity, polynomial. Separated support regions have zero covariance already at finite n. There is therefore no contradiction with Sections2–3.

One can verify the full commuting Gaussian contact limit without a spectral fit: for coefficients a_(n,k)=n^(−3/2)f(k/n), boundedness and centering give omega(exp(it a X))=1−t²a²/2+O(|a|³), uniformly in k. Here max|a| tends to zero, Σa² tends to integral f² and Σ|a|³ tends to zero. Independence then gives the characteristic-function limit exp[−t² integral f²/2]. Applying the same argument to linear combinations of finitely many f gives the Gaussian white-noise finite-dimensional distributions with covariance integral fg. This is a commuting equal-time finite-dimensional distribution limit inside the actual u=0 model. No tightness or convergence in a topology of random distributions, relativistic quantum field theory, or dynamical limit is asserted.

Thus a statement that uniform weak coupling forbids EVERY nontrivial continuum limit would be false. The theorem excludes nonzero off-diagonal connected correlations for the stated renormalized local field class while allowing nontrivial contact data.

## 5. Independent gap and propagation-scale comparison

Use a common smaller weak window in which the reviewed34 gap bound and35 Lieb–Robinson estimate both apply. Introduce laboratory time tau=b_ell t, with arbitrary supplied b_ell>0. Its Hamiltonian is H_lab=H/b_ell. Write g_ell for its actual neutral excitation gap. The theorem gives only

 g_ell >= G_ell:=2/(a_ell b_ell).

It does not give an upper bound on g_ell. The35 link metric joins links in one elementary plaquette; their midpoint Euclidean separation is at most ell. Consequently its exponential commutator estimate has a valid physical-velocity upper parameter

 V_ell:=32e ell v_ell/b_ell=32e ell u_ell/(a_ell b_ell).

This is a Lieb–Robinson UPPER parameter, not an observed group velocity or an actual speed equality. The ratio of this upper parameter to the gap lower bound is exactly

 V_ell/G_ell=16e ell u_ell <=16e u_* ell.          (3)

Two carefully conditional consequences follow. First, if the ACTUAL rescaled gap is additionally bounded above by a finite M, then G_ell<=M and V_ell<=16e u_* M ell tends to zero. For fixed physical separation and fixed finite laboratory time, the same polynomially norm-bounded local commutators consequently vanish faster than every power: their LR exponent is at most −r/(2ell)+O(1). This conclusion uses the extra upper bound on the actual gap; the34 lower bound alone does not supply it.

Second, for this LR upper parameter even to remain at least some fixed V_0>0, (3) forces G_ell>=V_0/(16e u_* ell), hence a diverging actual gap lower bound. Equivalently, a demonstrably nonzero propagation speed bounded by this LR parameter could not coexist with a bounded gap in this uniformly weak scaling window. We do not infer such a speed from the estimate itself. If a_ell b_ell stays bounded below, V_ell already tends to zero directly. If a_ell b_ell is of order ell, the LR upper parameter may stay finite while the gap lower diverges; no contradiction occurs.

No equation a_ell=ell has been introduced. Clock rescaling changes both quantities together and cannot change ratio(3). Energy shifts by the vacuum scalar do not alter the gap; more elaborate sector-dependent subtractions or changed dynamics are outside this simple rescaling statement.

## 6. Exact conclusion and next residual

The exclusion is conditional and narrow: in one uniform sufficiently weak-electric window, fixed-size bounded local fields with polynomial renormalization cannot produce a nonzero separated-point connected ground correlator, including separated polynomial-l1 smearings. It leaves contact limits, unbounded fields lacking norm control, sufficiently non-polynomial renormalizations, growing physical supports, and regimes where clustering constants cease to be uniform outside the claim. Approaching a parameter boundary matters only if uniform constants are actually lost; merely renaming a coupling as near-threshold is not an exception.

The supplied fixed-lattice model could seek a different separated-point continuum limit only by changing at least one proved hypothesis, for example leaving the uniform weak window or identifying a different admissible field/support scaling and proving its estimates. No claim that doing so succeeds is made. Physical coupling selection, actual propagation, relativistic scaling and continuum identification remain separate mathematical/physical tasks. The prior-art exponential-clustering input and elementary exponential-versus-polynomial inference are explicitly credited; no all-protocol or universal continuum no-go is asserted.


# Independent contact proof with explicit remainder constants

# Exact Haar contact-limit sharpness example

**Type:** bounded_theorem, conditional on the supplied u=0 compact-link product Haar ground, spatial mesh and field normalization. Root exposed the candidate before the prospective contract. This proof froze before reading native40. No generic central limit theorem is imported.

At u=0 the neutral ground of the electric Hamiltonian is the product constant, so link variables under its expectation are independent normalized SU(3) Haar variables. For each k in Z3 take the positively oriented xy elementary plaquette based at fine-lattice vertex3k. Its four link variables are disjoint from those of every other chosen plaquette: projected unit-square coordinate intervals at distinct multiples of3 do not overlap in an edge, and different z layers also have distinct links. Its holonomy U_k is Haar, because a product of independent Haar matrices and their inverses is Haar. The holonomies are independent as functions of disjoint independent link sets.

Put J_k=ReTr(U_k)/3 and X_k=sqrt18 J_k. The fundamental Haar character chi satisfies integral chi=0, integral chi^2=0 and integral |chi|^2=1. The first follows from nontriviality, the second also follows from multiplication by the SU3 center, and the last is Schur orthogonality. Thus E J=0 and E J^2=(0+2+0)/36=1/18. Consequently E X=0, E X^2=1 and |X|<=B=sqrt18. These are actual plaquette multiplication observables in the electric ground, not abstract independent spins substituted for the model.

Give fine links mesh ell=h/3. The chosen plaquette anchors then have physical positions hk. For real f in C_c(R3), define the finite random variable

 Phi_h(f)=h^(3/2) sum_(k in Z3) f(hk) X_k.

Only finitely many terms are nonzero. They commute as multiplication observables. For any finite family f_1,...,f_m and real t_1,...,t_m set g=sum_j t_j f_j. The joint characteristic function equals the characteristic function of Phi_h(g).

## Explicit Taylor-product proof

Write phi(z)=E exp(i z X), z real. Taylor's integral remainder gives

 |phi(z)-1+z^2/2| <= B |z|^3/6,

because E|X|^3<=B E X^2=B. If |z|<=1/(2B), put w=phi(z)-1. Then |w|<=z^2(1/2+1/12)<=z^2<=1/72. The power-series logarithm about1 is therefore defined, with

 |log(1+w)-w| <= |w|^2/[2(1-|w|)] <= |w|^2 <= z^4.

It follows that

 |log phi(z)+z^2/2| <= (B/6+1/(2B))|z|^3 = (7B/36)|z|^3 <= (B/4)|z|^3.

For sufficiently small h, every z_k=h^(3/2)g(hk) satisfies the threshold. Independence gives an exact product, so summing these small-argument logarithms gives a logarithm of the product and

 |sum_k log phi(z_k) + (h^3/2)sum_k g(hk)^2|
 <= (B/4) h^(9/2) sum_k |g(hk)|^3 = O_g(h^(3/2)).

The last estimate uses a fixed compact box containing supp g: its number of mesh points is at most C_g h^-3 for0<h<=1, while ||g||_infinity is finite. The Riemann sum h^3 sum g(hk)^2 tends to integral g^2. Exponentiation therefore yields the joint limiting characteristic function

 exp[-(1/2) integral_(R3) (sum_j t_j f_j(x))^2 dx].

This is the finite-dimensional centered Gaussian white-noise characteristic functional. A degenerate covariance matrix is allowed if the test functions are linearly dependent. In particular

 Cov(Phi_h(f),Phi_h(g))=h^3 sum_k f(hk)g(hk) -> integral f g.

For disjoint test-function supports the finite covariance is already zero. This gives a nonzero contact/statistical limit while every separated-support connected covariance vanishes.

The O(h^(3/2)) bound is for the logarithmic product error relative to its discrete quadratic form. For arbitrary continuous compactly supported f no O(h^(3/2)) rate is asserted for the Riemann-sum-to-integral error. Only convergence of that latter error is needed. This distinction prevents a false quantitative CLT rate from being attached to arbitrary continuous test functions.

## Scope

The construction is at exactly u=0 with supplied ell=h/3, disjoint plaquette sampling and central-limit normalization. It is a rigorous finite-dimensional distribution limit, not a claim of convergence in a chosen random-distribution topology, a dynamical field, a propagating QFT, physical stochastic noise, or an interacting continuum limit. The Gaussian characteristic function does not supply a time evolution. It demonstrates why a separated-correlation obstruction must retain its contact-term exclusion.

Disjoint links are a sufficient independence criterion. Distinct plaquettes alone do not justify applying that criterion; no converse dependence assertion about all overlapping plaquettes is made. Repeating the identical plaquette is an explicit adverse case: the two resulting X variables have covariance1 rather than0.
