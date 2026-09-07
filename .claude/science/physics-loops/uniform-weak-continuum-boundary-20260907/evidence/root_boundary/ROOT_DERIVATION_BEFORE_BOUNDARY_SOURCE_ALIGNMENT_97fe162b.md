# Root uniform-clustering boundary for a continuum field route

This is a conditional scaling obstruction for a precisely specified field class. It is not a theorem that every continuum limit is impossible. The prospective route was shared with native before independent proof work. Spatial mesh length ell is a new supplied interpretation of cell coordinates and is distinct from the kinetic/time parameter a. The result does not select either quantity from the axioms.

## Uniform input and its model dependence

Take the selected infinite-volume ground state omega_u of the fixed compact SU3 interaction used in blocks36/39. Choose a closed weak-coupling interval0<=u<=u_* strictly inside one common convergence window, u=av. The marked-cluster construction can be run with one fixed activity majorant throughout this interval. Yarotsky0412040 Theorem1(3) and Section2 supply constants C>=1 and mu>0, depending only on fixed geometry and this chosen window, such that bounded local operators A,B satisfy

 |omega_u(AB)-omega_u(A)omega_u(B)|
 <= C^(|S_A|+|S_B|) exp[-mu d(S_A,S_B)] ||A||||B||.       (1)

Here S_A,S_B are cell supports and d is their lattice distance; changing between the source's equivalent fixed-range graph metric and nearest-neighbor cell distance only changes the positive constantmu. This is an explicit imported clustering theorem, not a numerical fit. Primary source: https://arxiv.org/pdf/math-ph/0412040 . Uniformity follows by choosing the time step, norm majorant and cluster smallness once for the whole smaller interval, as in the block36 construction. A separate theorem's bare assertion of analyticity at each u would not establish uniformity by itself.

Multiplying the Hamiltonian by a>0 does not change its ground state. In scaled form aH depends only on u, so allowing a=a_ell cannot by itself change the equal-time ground correlation bound while u_ell remains in this interval. This does not identify a with a spatial lattice spacing or give a physical light speed.

## Point-field version

Assign spatial position ell z to cell z in Z3. For each ell down to0 choose bounded operators A_ell,B_ell supported in neighborhoods of at mostm cells and of lattice radius at mostR around anchor cells z_ell,w_ell, with m,R fixed. Suppose their physical anchors converge to distinct points X,Y; write r=|X-Y|>0. For all sufficiently small ell, their physical anchor distance is at leastr/2, so

 d(S_A,S_B)>=r/(2ell)-2R

up to a fixed geometry factor already absorbable into mu. If the anchors approximate X,Y with O(ell) error, the sharper r/ell-O(1) bound is available, but unnecessary.

Assume ||A_ell||<=M_A ell^(-p), ||B_ell||<=M_B ell^(-q) for fixed finite nonnegativep,q and constantsM_A,M_B. Then(1) gives

 |connected_ell(A,B)|
 <= C^(2m) M_A M_B exp(2mu R) ell^(-p-q) exp[-mu r/(2ell)].       (2)

For every finite N, ell^(-N) times the right side tends to0. Indeed with t=1/ell, any t^k exp(-ct) tends to0 for c>0, as follows for example from an exponential-series lower bound of degree greater thank. Thus every possible continuum limit of these connected two-point functions vanishes at distinct spatial points. Constants added to the fields do not change their connected correlator; subtracting a nonzero local mean does not evade(2).

The same argument allows more general subexponential normalization if log(||A_ell||||B_ell||)=o(1/ell), with bounded support size. Polynomial normalization is a useful concrete sufficient condition, not an assertion that all conceivable fields obey it.

## Separated smearing supports

Let F_ell=sum_i alpha_i,ell A_i,ell and G_ell=sum_j beta_j,ell B_j,ell be finite sums of bounded local operators. Each summand has at mostm cells and radiusR. Suppose the two families' physical anchor sets are separated by a fixed r>0. Require polynomial weighted norm budgets

 sum_i |alpha_i,ell| ||A_i,ell|| <= M_F ell^(-p_F),
 sum_j |beta_j,ell| ||B_j,ell|| <= M_G ell^(-p_G).

No fixed number of summands is needed; ordinary finite mesh smearings fit if their coefficients and local field norms give these budgets. Applying(1) to each pair and using bilinearity and the triangle inequality yields

 |omega(F_ell G_ell)-omega(F_ell)omega(G_ell)|
 <= C^(2m) exp(2mu R) M_F M_G ell^(-p_F-p_G) exp[-mu r/ell],       (3)

again allowing an inessential fixed metric factor inmu. The sum is estimated term by term rather than treating its entire macroscopic support as one mark; the latter would introduce an avoidable support-volume prefactor. Separated continuum smearings in this class therefore have zero connected limit, if their limits exist.

## Precise consequence and exclusions

A proposed continuum field construction with nonzero connected equal-time two-point functions at separated points or separated smearing supports cannot simultaneously satisfy all of the following: u_ell stays in one fixed uniformly controlled weak interval; the fields are built from the stated bounded local fixed-radius lattice operators; their weighted norms grow only polynomially (or suitably subexponentially); and physical separation is interpreted by ell times cell coordinates with ell->0. At least one premise must change.

This does not prove existence of any continuum limit, control contact terms, fix field dimensions, forbid unbounded fields outside the norm hypothesis, or exclude growing-support/nonlocal observables. Large Wilson loops of fixed physical size have growing lattice support and require their own analysis. It does not prove that leaving this weak interval produces a continuum theory, locate a transition or derive a physical coupling. The failure of a uniform convergence certificate near a boundary is not itself evidence of a phase transition.

The strategic implication is specific: the uniformly controlled strong-electric phase established by the campaign cannot furnish the desired nontrivial separated local correlations through an ordinary polynomially normalized fixed-neighborhood field construction alone. A continuum-focused campaign must establish a different scaling regime, justify a different field class, or derive why the axioms select a route outside these assumptions. The present conditional gap and static-charge results remain useful model checks, but do not by themselves close that bridge.

## No unsupported speed identification

The finite-dynamics locality estimate gives an upper propagation bound; its constant is not a measured signal speed. This note makes no continuum light-cone or mass-velocity identification from that coefficient. The equal-time correlation argument already proves the stated obstruction without conflating a and ell or assuming saturation of a Lieb–Robinson estimate.
