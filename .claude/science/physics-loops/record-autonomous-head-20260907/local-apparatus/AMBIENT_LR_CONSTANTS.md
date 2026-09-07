# Explicit volume-uniform LR constants for native controlled whole hoppings

Independent derivation for the cubic lattice family. The ambient operator
construction is in ambient-generator-review.md; the notation delta_R matches
the primary localized-lift DERIVATION.md. No repository edits or transport
parameter changes were made.

## Geometry and local registers

Let original cubic vertices be v in Z^3, of valence at most6. Embed a vertex
at2v and the midpoint of edge(v,v+e_a) at2v+e_a. Let Gamma be these vertices
and midpoints, with the RESTRICTED AMBIENT l1 metric

    d(x,y)=|x-y|_1.

This is not asserted to be the shortest-path metric of an auxiliary adjacency
graph on Gamma. It is a valid metric on a subset of Z^3, which is all the LR
argument needs. Finite induced graphs, or finite restrictions of the infinite
interaction, obey the same bounds below.

At each midpoint place its native edge qubit and fuel qubit: local dimension4.
At each vertex place its supplied head qubit: local dimension2. A ready/sign
register or mathematical flag, if used, is colocated at the event seed and
changes local dimension rather than adding metric sites. A one-head initial
preparation is a supplied invariant sector, not a global projector in H.
The continuous battery is NOT smuggled into this local-register assertion.

For each original edge e=(u,v), let D_e be the midpoint set of all edges incident
to u or v. Then

    |D_e|<=11,     D_e subset ball_2(midpoint(e)),     diam(D_e)<=4.

The whole native h_e is supported in D_e, independently of neighbor-order
choices; q_e is colocated at midpoint(e), so q_e h_e has the same support bound.
A fixed midpoint(f) lies in D_e precisely when e shares an endpoint with f;
there are at most11 such e. These verify the proposed cardinality, diameter
and incidence constants in doubled coordinates.

A Record-only directed seed M_vw f_e Q_e,z uses at most3 metric sites: the two
head vertices and midpoint(e). The feedback seed includes
J_vw=T_e n_v(1-n_w), so its support S has at most13 sites: D_e and the two head
vertices. Both seed supports fit in ball_2(midpoint(e)); both have diameter at
most4. Their single-edge two-sign columns have norm at most1. No separate
factor is charged for two signs. The fixed numerical bound s=|S|<=13 is safe
for either case and is independent of lattice volume and particle number.

## Summable metric weight and convolution

Choose any mu>0 and

    F(r)=(1+r)^(-4),       F_mu(r)=exp(-mu r) F(r).

The l1 shell of radius n>=1 in Z^3 contains4n^2+2 sites. Therefore, writing

    Fbar = 4 zeta(2) - 8 zeta(3) + 6 zeta(4) - 1
         = 2.4572204443829833...,

we have ||F||_Gamma<=Fbar, uniformly in every finite volume. Indeed the complete
Z^3 sum is 1+sum_(n>=1)(4n^2+2)/(n+1)^4, and shifting n+1 gives the displayed
zeta expression exactly.

For any x,y,z, at least one of d(x,z),d(z,y) is >=d(x,y)/2. On that half of the
sum the corresponding F ratio is at most16. Splitting into the two halves and
using the triangle inequality for the exponential weight gives

    sum_z F_mu(d(x,z)) F_mu(d(z,y)) / F_mu(d(x,y))
       <=32 Fbar =: Cbar = 78.63105422025546... .

Thus C_mu<=Cbar, with no extensive site-count constant. The factor32 proposed
in the sketch is valid. No assumption of translation invariance of Gamma is
needed; bounding its sums by complete Z^3 suffices.

## Interaction norm: a refinement of the proposed bound

Split the ambient Hamiltonian as

    H = sum_midpoints Delta q_e + sum_e Phi(D_e),
    Phi(D_e)=q_e h_e,       ||Phi(D_e)||<=t.

If multiple labels share an actual support, combine their terms and bound the
norm by their norm sum. Treat Delta q_e as the on-site Hamiltonian in the LR
theorem. It need not enter J_mu. It commutes with every controlled hopping,
and its conjugation of fuel lowering is a local phase. That phase is retained
in the lift and in its truncation; it is not discarded from battery accounting.

For distinct midpoint sites x=midpoint(f),y=midpoint(g), the multiplicity of
whole-hopping supports containing both has these bounds:

| Ambient l1 distance | Maximum number of terms |
|---:|---:|
| 0 | 11 |
| 2 | 6 |
| 4 | 1 |
| greater than4 | 0 |

There are no nonzero odd-distance pairs because every midpoint has odd total
coordinate parity. For two edges sharing a vertex, every covering e is incident
to that vertex; an additional edge between the other endpoints would form a
triangle, impossible in the cubic graph. This gives6 at distance2. For disjoint
f,g, a covering e connects one endpoint of f to one endpoint of g. Two such
connections cannot share an endpoint (again a triangle); if two exist, the four
edges form a cubic square. Then f,g are opposite parallel square edges, whose
midpoints have distance2. At distance4 there can consequently be only one.
Terms involving a vertex/head site contribute zero to this interaction norm.

It follows directly that the Sims interaction norm is bounded by

    J_mu = sup_xy [sum_(Z containing x,y)||Phi(Z)||]/F_mu(d(x,y))
         <= t max{11, 6*3^4 exp(2mu), 5^4 exp(4mu)}
         = 625 t exp(4mu) =: Jbar_mu.

The simpler11*625*t*exp(4mu) bound would also be valid, but loses a factor11.
The refined bound is uniform over graph boundaries and missing edges because
these only remove possible incidences. A finite patch enumeration independently
checked the multiplicities {distance0:11, distance2:6, distance4:1}; the proof
above is the volume-uniform argument.

If one insists on putting Delta q_e into Phi instead of the on-site part, a
safe alternative is J_mu<=max{11t+Delta,625t exp(4mu)}. Keeping it on-site is
both sharper and directly supported by the theorem's setup. No particle count,
fixed-N Hilbert dimension or total number of sites appears in these estimates.

## Imported LR theorem and its substitution

The only imported theorem here is Sims, Section3, equations18–22: bounded
interactions with a summable convolution weight have a disjoint-support bound
with time factor (exp(2 J_mu C_mu |tau|)-1)/C_mu and spatial sum of F_mu. On-site
Hamiltonians are separate in its setup. [Sims, Lieb-Robinson Bounds and
Quasi-locality for the Dynamics of Many-Body Quantum Systems](https://arxiv.org/pdf/1011.4540).

For disjoint supports, this time factor is nondecreasing in each positive J,C.
Thus using the upper bounds Jbar_mu,Cbar is justified jointly, including the
inverse C prefactor; one must not independently lower that prefactor without
also controlling the time factor. Bound the spatial sum by
Fbar min(|X|,|Y|) exp(-mu d(X,Y)). Define

    v_mu = 2 Jbar_mu Cbar / mu
         = 1250 Cbar t exp(4mu)/mu.

Then the following convenient, intentionally loose corollary is valid uniformly:

    ||[tau_tau(A_X),O_Y]||
       <= (2 ||A_X|| ||O_Y|| Fbar / Cbar)
          min(|X|,|Y|) exp[-mu(d(X,Y)-v_mu |tau|)].

Its constants depend only on mu, the lattice geometry and the hopping bound t.
Colocated finite registers do not change the bound. No useful small numerical
velocity or favorable finite radius is claimed from these loose constants.

## Explicit boundary sum and delta_R

Use the SAME neighborhood convention as the localized-lift derivation:

    B_R(S)={x in Gamma : d(x,S)<=R},       integer R>=4.

Retain exactly whole-hopping interactions supported inside B_R(S), together
with its on-site fuel terms and the supplied local seed/register. All omitted
interactions fully outside commute with the truncated evolved seed. Let
boundary(R) be omitted interactions crossing this boundary, and
b_R=sum_boundary ||Phi(Z)||.

For a crossing D_f, every point lies within2 of its midpoint m_f. Hence

    R-2 < d(m_f,S) <= R+2.

The center therefore belongs to the union, over s in S, of the four integer
shells n=R-1,R,R+1,R+2 about s. There is one interaction label per midpoint.
Bounding those midpoint shells by complete Z^3 shells yields

    b_R <= t s sum_(n=R-1)^(R+2) (4n^2+2)
        = t s (16R^2+16R+32) =: bbar_R.

The union bound may count a midpoint more than once, which is harmless. On-site
fuel terms never cross a boundary and contribute nothing to b_R. Each crossing
interaction also obeys d(S,D_f)>=R-4. These statements hold near a finite-volume
boundary as well, where fewer interactions can cross.

For a norm-one-or-less bare column W and its coherently truncated evolution,
write delta_R(tau)=||W(tau)-W_R(tau)||. Duhamel integration of the preceding LR
bound, with interaction diameter a=4, gives, for t>0,

    Cbar_R = 2 s Fbar bbar_R / (Cbar mu v_mu)
           = t s^2(16R^2+16R+32)/(16 mu v_mu),

    delta_R(tau)
       <= min{2,
              Cbar_R exp[-mu(R-4)] (exp(mu v_mu |tau|)-1)}
       <= min{2, Cbar_R exp[-mu(R-4-v_mu |tau|)]}.

This is the requested explicit volume-uniform substitution into the primary
delta_R notation. Cbar_R grows quadratically in R; it has not been hidden in a
radius-independent constant. For t=0 there are only local fuel phases and the
truncated/full seed evolutions agree exactly. For a jump multiplied by
sqrt(gamma), multiply the operator-error bound by sqrt(gamma); the frozen
construction has gamma=1.

A seed-centered ball about midpoint(e), rather than the distance-to-support ball
used here, permits dropping one factor s from bbar_R but changes the separation
in the exponent to at least R-6. Those conventions must not be mixed.

## Flags and limitations

The common ambient controlled-fuel H already realizes the lift fiber as ordinary
conjugation of a local seed, so no source/target history projector or additional
Hamiltonian flag is needed for this LR step. A degenerate output register at
midpoint(e) does not alter H. If the alternative single-event flag construction
is used, group the modified seed-edge term: (I-P_flag)h_e or
(q_e-P_flag)h_e has norm<=t and the same support. The stated constants therefore
survive that particular grouping; arbitrary added flag couplings would require
their own norm contribution.

These are ambient Hamiltonian and single-event fiber bounds. They do not prove
an error bound for the full occupation-dependent GKSL semigroup merely by
summing event-channel estimates. The exact global energy lift still uses all
Fourier times; locality follows only after a justified cutoff/tail argument in
the specified fixed-battery norm. Correlated retained-battery inputs, cap leakage,
full rather than truncated energy conservation, bath construction and entropy
remain separate obligations. Whole-hopping truncation preserves native N, but
neither the hopping support nor the feedback seed is one-site or nearest-neighbor
in the claimed sense. Head/fuel roles, placement and preparation remain supplied;
no covariant one-site admissibility or lattice-wide formation/renewal closure is
inferred from these constants.
