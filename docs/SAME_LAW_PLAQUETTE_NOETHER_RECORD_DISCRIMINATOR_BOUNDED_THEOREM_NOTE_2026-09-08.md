---
claim_type: bounded_theorem
actual_current_surface_status: conditional finite supplied-model result
claim_scope: Four-site square CAR and commuting hard-core hopping, exact current/transfer identities, and a supplied even pointer channel; no physical action, formation, calibration or time selection.
---
# One square hopping expression, current, and a supplied Record discriminator

**Date:** 2026-09-08
**Type:** bounded_theorem
**Status:** conditional finite construction; independent final review pending.
**Primary runner:** `scripts/admissibility_same_law_plaquette_noether_record_statistics_discriminator_2026_09_01.py`
**Runner cache:** `logs/runner-cache/admissibility_same_law_plaquette_noether_record_statistics_discriminator_2026_09_01.txt`

A two-particle occupation event can distinguish two supplied products even
when their one-particle hopping matrices agree. The distinction persists when
the same event feeds a supplied pointer channel. This note states the finite
result recovered from Block 44; it does not select the physical product.

## Premises and domain

The [current minimal memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the framework
boundary. It supplies none of the Hamiltonian, composite product, initial
state, time parameter, calibration, pointer channel or formation schedule
used below. No scalar additivity or old Record-cost premise is used.

Take four sites cyclically ordered 0,1,2,3, each with lowering matrix
`sigma_-`, and explicitly choose either CAR operators
`c_j=Z_0 ... Z_(j-1) sigma_-j` or commuting hard-core operators
`b_j=sigma_-j`. The composite carrier here is the supplied 16-dimensional
occupation space. The symbolic expression is common; its two matrices need
not be identical. This is not a product-independent compilation theorem.

Put `H0=-sum_edges(a_x^dag a_y+a_y^dag a_x)`, `H=t H0`, real t,
`n_x=a_x^dag a_x`, and `Q=sum_x n_x`. Use initial occupation `1010` and
opposite target `0101`. Real `z=t tau` is a dimensionless supplied cadence;
there is no physical clock assertion. At t=0 the transition is trivial; the
nontrivial witness below requires nonzero coupling and an allowed cadence.

The pointer is a separate, trivially graded two-label factor. Interpreting
its events as framework Records additionally supplies an actual formation
occurrence and a valid carrier/readout identification. It does not insert a
full readable M2 algebra into the same nontrivially graded matter site.
Relative trace weights require separate calibration to become physical
probabilities; the endpoint calculation alone supplies no general Born law.

## Exact finite statement and proof

1. Both products have the same local number matrices and one-particle square
   adjacency, with spectrum `{-2,0,0,2}` for H0. Their off-site algebras differ:
   CAR anticommutes and the hard-core operators commute. Direct multiplication
   gives `[H,Q]=0` for both.

2. Orient an edge x to y and replace its term by
   `-t(exp(-iA)a_y^dag a_x+exp(iA)a_x^dag a_y)`.
   Differentiation at zero gives `t J_xy`, where
   `J_xy=i(a_y^dag a_x-a_x^dag a_y)` and `J_yx=-J_xy`.
   Summing incident terms yields `i[H,n_x]+t sum_y J_xy=0` at all four sites.
   This is conservation accounting for the supplied action.

3. The eight dihedral square transformations act by ordinary site permutation
   for hard-core operators and the signed fermionic lift for CAR. They preserve
   H0, transform oriented currents correctly and preserve the unordered pair
   of opposite-corner events. Within the *offdiagonal nearest-neighbor
   quadratic hopping ansatz*, invariance forces a real uniform edge weight.
   This restricted ray leaves t free. Onsite `mu Q`, interactions and other
   ansatz extensions are not excluded; `mu Q` only changes a fixed-Q phase.
   All 24 Jordan-Wigner site orders give the same CAR dark-amplitude result.

4. On the Q=2 sector, use the six occupation indices `(3,5,6,9,10,12)`.
   Exact multiplication gives
   `Hc(Hc^2-4I)=0`, spectrum `{-2,-2,0,0,2,2}`, and
   `Hb(Hb^2-8I)=0`, spectrum `{-2sqrt(2),0,0,0,0,2sqrt(2)}`.
   Polynomial interpolation therefore gives, for every real z,
   `exp(-iz Hc)=I-i sin(2z)Hc/2+(cos(2z)-1)Hc^2/4`,
   with the corresponding replacements `2 -> 2sqrt(2)` and `4 -> 8` for Hb.
   The target entries of I,Hc,Hc^2 from the initial state vanish. Hence
   `A_CAR(z)=0` and `A_HCB(z)=(cos(2sqrt(2)z)-1)/2`.
   At `z*=pi/(2sqrt(2))`, the latter amplitude is -1. Its zeros occur at
   `z=k pi/sqrt(2)`, k integer. These are analytic identities, not fitted samples.

5. Along the hard-core evolution the four densities are
   `(cos^2(sqrt(2)z),sin^2(sqrt(2)z),cos^2(sqrt(2)z),sin^2(sqrt(2)z))`.
   Integrating oriented currents on `(01,12,23,30)` from 0 to z* gives
   `(1/2,-1/2,1/2,-1/2)` and density change `(-1,1,-1,1)`.
   Each vertex obeys integrated continuity. This does not make current a
   cause or a selector of Record formation.

6. The target projector `P=|0101><0101|` is identical in both products and
   commutes with matter parity. On Q=2 define
   `K0=(I-P) tensor |0>` and `K1=P tensor |1>`.
   Then `K0^dag K0+K1^dag K1=I`. The Choi matrix factors as
   `[vec K0,vec K1][vec K0,vec K1]^dag`, so the channel is completely positive;
   its factor Gram is diag(5,1). The pointer-one pullback is P.
   At z* its outputs have pointer weights `(1,0)` for CAR and `(0,1)` for
   hard-core evolution. The two-Kraus channel dephases across P and I-P.
   Pointer relabeling by a unitary permutation changes no weight.

7. For later generators `H_matter tensor I_pointer`, both pointer projectors
   commute with the generator and are fixed for all later times. This is
   conditional permanence under supplied decoupling. Pointer mixing or an
   overwriting interaction can invalidate it. The assertion does not supply
   a physical persistence dynamics or a formation rate.

## Evidence and limitations

The canonical runner executes these identities with exact SymPy algebra and
retains its 15 original check labels. It declares its current memo, all seven
actually read historical packet files and this note; source/header/input
hashes bind the genuine cache. Its explicit timeout is 120 seconds. The old
unbound 15/0 stdout and all 22 Block 44 packet bodies remain dated provenance.
A fresh runner total checks the listed finite predicates; it does not approve
historical portfolio claims or prove source completeness by itself.

The original 17 named mutation claims are historical. Some exercise actual
matrices (current signs, strings, edges, writer and pointer); others only set
an overclaim flag. In particular `born_without_calibration` and
`arbitrary_K_family_fixed` are wording/custody checks, not countermodels to
all possible calibration or response laws. Actual coefficient/source controls
are recorded separately in the correction evidence.

The result leaves action/product selection, physical functional I4,
preparation, physical time, writer/formation and decoupling unresolved.
Different graphs, interactions, detector dynamics and calibration rules remain
live. No independence count or universal no-go follows from that list. Prior
PRs and novelty assertions quoted in the dated packet are unverified context,
not suppliers for this self-contained finite proof. Neither the historical
BACKLOG_NO_PR instruction nor a historical TOE-score gate controls current
owner-authorized recovery. No axiom adoption, obligation retirement or audit
status is asserted here; formal audit remains deferred until a solid TOE.
