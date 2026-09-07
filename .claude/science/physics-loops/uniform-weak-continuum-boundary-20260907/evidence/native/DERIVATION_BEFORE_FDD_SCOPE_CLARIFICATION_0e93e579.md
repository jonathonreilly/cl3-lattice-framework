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

For a continuous test function f on the unit box put F_n(f)=n^(−3/2)Σ_k f(k/n)X_k. Its variance is n^(−3)Σ_k f(k/n)², tending to integral f²; for f=1 it is exactly1 at every n. The total coefficient l1 norm is at most n^(3/2)||f||_infinity, polynomial. Separated support regions have zero covariance already at finite n. There is therefore no contradiction with Sections2–3.

One can verify the full commuting Gaussian contact limit without a spectral fit: for coefficients a_(n,k)=n^(−3/2)f(k/n), boundedness and centering give omega(exp(it a X))=1−t²a²/2+O(|a|³), uniformly in k. Here max|a| tends to zero, Σa² tends to integral f² and Σ|a|³ tends to zero. Independence then gives the characteristic-function limit exp[−t² integral f²/2]. Applying the same argument to linear combinations of finitely many f gives the Gaussian white-noise finite-dimensional distributions with covariance integral fg. This is a commuting equal-time random-distribution limit inside the actual u=0 model, not a relativistic quantum field theory or a claim about its dynamics.

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
