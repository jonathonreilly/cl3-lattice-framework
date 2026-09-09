---
claim_id: admissibility_exterior_character_jr_r3_q2_symmetric_action_crossing_top_spin_bounded_theorem_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R3_Q2_SYMMETRIC_ACTION_CROSSING_TOP_SPIN_BOUNDED_THEOREM_NOTE_2026-08-29.md
claim_type: bounded_theorem
title: Exact symmetric action/crossing highest-spin coefficients on a supplied r=3, q=2 Haar carrier
claim_scope: "For each of the three fine-plaquette placements in the supplied r=3, q=2 two-cell original-link geometry, derive the unique highest-spin coefficient of the complete two-order local response B C_c+C B after transport to the physical residual packet. For the two placements disjoint from the neighboring eight-link loop, the one-layer coefficient is r_1^8(r_n^4+r_(n+1)^4). For the boundary placement sharing h3, the top-coupled coefficient is r_1^7(r_n^3 r_(n+1)+r_(n+1)^3 r_(n+2)). Both terms strictly reinforce for the supplied finite-positive multiplier family. The corresponding pure-placement all-layer products are exact formal selected-packet coefficients. Mixed-placement words, powers of the actual coarse-to-residual response, the full action exponential, invariant closure, and global minimal memory are not classified."
depends_on:
  - minimal_axioms
dependency_roles:
  minimal_axioms: "framework boundary only; the supplied finite model and its used lemmas are explicit below"
actual_current_surface_status: conditional-support
conditional_surface_status: "exact complete-two-order highest-spin reinforcement on each fixed local action placement of the supplied physical-J3/Q stack"
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_jr_r3_q2_physical_q_action_crossing_tower_no_go_note_2026-08-29
target_blocker_text: "test the complete symmetric BC_c+CB branch and multiple action placements for cancellation or reinforcement of the unique top-spin branch"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
proposal_allowed: false
proposal_allowed_reason: "The exact coefficient theorem uses the explicit supplied action, central crossing, and Haar J3/Q model below; it does not select these physically or classify mixed placement words or a physical invariant carrier."
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
axiom_or_primitive_edits: 0
runner: scripts/admissibility_exterior_character_jr_r3_q2_symmetric_action_crossing_top_spin_2026_08_29.py
independent_checker: scripts/admissibility_exterior_character_jr_r3_q2_symmetric_action_crossing_top_spin_independent_2026_08_29.py
date: 2026-08-29
claim_type_reason: "exact O(3) fusion, conditional Haar, original-link representation census, and the supplied symmetric-step plus-sign identity determine the unique highest-spin coefficient on three fixed placements"
next_trace_action: "Enumerate mixed-placement top channels of the summed action and determine which remain distinct after physical conditional Haar; keep the response-domain and full-exponential boundaries explicit."
---

# The two action/crossing orders reinforce the local highest-spin branch

**Status:** `conditional-support`

Type: bounded_theorem

**Actual current surface:** `conditional-support`. The coefficient calculation
is exact on the supplied finite action/crossing/Haar-`J_3/Q` model defined
below. The broader historical parent claims are not accepted dependencies.
Formal audit is deferred; this correction assigns no effective audit status.
The historical term “physical Q” means the conditional-Haar projector of this
supplied model throughout this note; no physical projector or state selection
is derived from the minimal axioms.

## Exact target

**Target claim.** For each fixed fine-plaquette placement in the supplied
`r=3, q=2` two-cell geometry, compute the unique highest-spin coefficient of
both terms in the parent response `B C_c+C B`, with physical conditional-Haar
`Q` and one central multiplier per original link representation, and decide
whether those two coefficients cancel or add.

The answer is addition. On both disjoint placements the coefficient from spin
`n` to spin `n+1` is

```text
s_n^D=r_1^8(r_n^4+r_(n+1)^4).                     (1)
```

On the boundary placement sharing the rung `h3` with the neighboring merged
loop, the coupled coefficient is

```text
s_n^S=r_1^7[r_n^3 r_(n+1)+r_(n+1)^3 r_(n+2)].    (2)
```

The normalized multipliers supplied for every finite positive exterior
coupling are strictly positive. Therefore the two orders reinforce at every
finite layer on all three fixed placements. The result has only the domains
proved below; it does not accept or widen the
historical ordered Block247 carrier conclusion.

## Obligation graph

| Obligation | Disposition | Evidence |
|---|---|---|
| identify the two typed operator orders and their relative sign | proved for the supplied symmetric step | lemma T below |
| transport the coarse crossing without changing operator order | proved for the supplied central convolution | lemma T below |
| apply physical `Q`, rather than a static tensor projector | proved on the selected top channel from lemma H and exclusive-path orthogonality | equations (5)--(6) below |
| reconstruct the original-link multiplicities | proved here | equations (7)--(10) and both runners |
| prove top fusion multiplicity one | proved here | exact `O(3)` character product and independent maximal-torus extraction |
| decide the relative sign of the two top paths | proved here | equations (11)--(14) |
| exclude cancellation on the supplied multiplier domain | proved here | strict positivity in equation (15) |
| classify mixed plaquette words and the full physical response carrier | not part of this target | strongest missing lemma stated below |

The graph is acyclic: the top coefficient is derived from the supplied operator
identity proved below, the independently reconstructed link labels, and ordinary compact-
group representation algebra. No step assumes the target coefficient.

## Supplied model and used premises

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) give the framework boundary;
they do not select this action, Haar measure, coarse map, crossing kernel, or
physical time. We supply `G=O(3)` on the 19 oriented links in equations (7)--(8),
with normalized independent Haar measure and the usual vertex gauge action.
Take the gauge-invariant subspace of `L2(G^19)`. The coarse map retains
`h0,h3,h6` and the products of each three-link rail segment, deleting the
internal rungs `h1,h2,h4,h5`.
The coarse space has the pushed-forward product Haar measure. Its pullback
`J_3` is an isometry because a product of independent Haar variables is Haar;
coarse gauge-invariant functions pull back to fine gauge-invariant functions.
Set `Q=J_3 J_3*`. This specifies a finite graph and an infinite compact-group
function space, not a finite-dimensional truncation or a physical selection.

The four former parent notes and all original PR versions are preserved in the
[historical recovery inventory](../.claude/science/physics-loops/symmetric-crossing-7803-correction-20260909/HISTORY.md).
Only the definitions and lemmas stated here are used. No temporal limit,
semigroup obstruction, broad adjacent-product theorem, or linear-carrier no-go
from those parents is accepted by this packet.

### H. Conditional Haar on the required channels

At fixed coarse data the deleted internal rungs `h1,h2` remain independent
normalized Haar. Every nontrivial irrep matrix has zero Haar integral: the
integral intertwines with the trivial representation, so its image would be
an invariant vector, which an irreducible nontrivial representation lacks.
Every selected top network below has a nontrivial label on an internal rung;
all coarse pullbacks are independent of that rung. Integrating it proves
orthogonality to every coarse function, hence `Q g_n^i=0` for `n>=1`.
The raised top network has label `n+1` there and is likewise killed by `Q`.
This includes the shared placement because `h2` remains exclusive to `p2`.

For the disjoint product characters this also determines every lower branch.
At fixed coarse data, varying the internal rung in `p0` or `p1` makes that
plaquette Haar, while `chi_V(C1)` is unchanged. Thus
`Q[chi_(ell,p)(p_i) chi_V(C1)]` is zero except for `(ell,p)=(0,+)`, when it is
`chi_V(C1)`. The determinant `(0,-)` remains nontrivial and is not removed
by residual subtraction. Equivalently, in plaquette fiber coordinates choose
`W0,W1` Haar and set `W2=delta0 W0^-1 W1^-1`; each proper single plaquette
has Haar marginal. No assertion about arbitrary history spaces is required.

### T. Central transport and the relative plus sign

Supply identical real inversion-symmetric central convolution on each original
link, with scalar irrep multipliers `r_(ell,p)`. Centrality gives independent
multipliers on each link representation, respects vertex gauge invariance, and
makes convolution self-adjoint. On a retained product of three rail links,
convolving the three factors induces the threefold convolution of their
kernels: move the intermediate increments past the existing link variables;
conjugation preserves each increment law because it is central. On a retained
rung the induced kernel is unchanged. Therefore crossing maps coarse pullbacks
to coarse pullbacks. Write the resulting coarse operator as `C_c`; then
`C J_3=J_3 C_c`. Self-adjointness also preserves the orthogonal complement,
so `[C,Q]=0`. No closure of the induced kernel within a one-parameter family
is needed.

Supply a bounded real gauge-invariant multiplication operator `V_f` and the
symmetric step `S(lambda)=exp(-epsilon lambda V_f/2) C exp(-epsilon lambda V_f/2)`.
On this finite compact graph boundedness justifies differentiation in norm.
For any isometry `J=J_3`, direct minus staged compression is exactly
`D(lambda)=J* S(lambda)^2 J-(J* S(lambda)J)^2=J* S(lambda)(I-Q)S(lambda)J`.
Since `(I-Q)CJ=0`, its residual derivative is

```text
L = (I-Q) S'(0) J
  = -(epsilon/2)[(I-Q)V_f J C_c + C(I-Q)V_f J]
  = -(epsilon/2)(B C_c+C B),       B=(I-Q)V_f J.
```

This proves the plus sign by differentiating the two multiplier halves.
Self-adjointness also gives `D(lambda)=K(lambda)*K(lambda)` with
`K(lambda)=(I-Q)S(lambda)J`, so its quadratic coefficient is `L*L`.
For the selected defining-vector component, set
`V_f=sum_i alpha_i M_(chi_V(p_i))`; linearity isolates each `B_i`.
This supplies the typed response used here, without asserting that its
coarse-to-residual map is composable with itself or is physical time evolution.

### P. A supplied family with strictly positive multipliers

Positivity of a density alone does not imply positive Fourier multipliers.
For the specific exterior-character family, put
`rho=1+det+V+det V`, `chi_rho(g)=(1+det g)(1+Tr g)` and supply, for integer
`m>=1` and finite `k>0`, the Haar-normalized weight proportional to
`exp[2 k chi_rho(g)^m/(m 8^(m-1))]`. On the improper component its value is
one; on `SO(3)`, `chi_rho=2(1+chi_1)`.

Write `A=1+chi_1` and `a_m=2^(4-2m)/m`. The character coefficients of the
proper-component weight are

```text
b_ell = sum_(j>=0) M_ell(mj) (a_m k)^j/j!,
M_ell(t) = binom(2t,t-ell)-binom(2t,t-ell-1),
```

where out-of-range binomials vanish. To derive the multiplicities, lift to
`SU(2)`: `A` is the character of two spin-half factors. In `2t` such factors,
the spin-`ell` multiplicity is the difference between weight-`ell` and
weight-`ell+1` dimensions, exactly the displayed binomial difference. It is
nonnegative and is strictly positive whenever `t>=ell`. The exponential series
converges uniformly on the compact group; coefficient integration is therefore
termwise legitimate. For every fixed `ell`, some `mj>=ell`, so `b_ell>0`;
also `b_0>1` because the constant `j=0` contribution is one and positive
`j>=1` contributions exist. Equal Haar mass on the two components gives

```text
r_(0,+)=1,
r_(0,-)=(b_0-1)/(b_0+1)>0,
r_(ell,p)=b_ell/[(2ell+1)(b_0+1)]>0, ell>=1.
```

Thus positive-spin multipliers are independent of inversion parity in this
family. The theorem's coefficient identities also allow arbitrary real formal
multipliers for the signed and endpoint controls. The rational positive samples
in the runner test those identities; they are not asserted to arise from a
common `m,k`. No parameter or physical family is selected by this lemma.

| Supplied item | Role | If changed |
|---|---|---|
| symmetric multiplier halves | fix the plus sign in lemma T | a relative minus defines a different response |
| the specified `J_3/Q` | removes conditional coarse components by lemma H | another projector need not preserve the selected top branch |
| linkwise central crossing | assigns one scalar to each original-link irrep | noncentral or non-linkwise maps invalidate the census |
| positive family in lemma P | gives strict reinforcement | zeros or signed multipliers reach the cancellation loci |
| defining-vector action and arbitrary real `alpha_i` | fix spin-one fusion and placement amplitudes | another action irrep changes the top increment |

No observed value, fit, sample rank, literature constant, new axiom, or proposed
primitive enters the proof. No axiom or approved primitive is edited.

## Typed transport of the symmetric response

Let `R=I-Q`, let `M_i` multiply by the defining-vector character on plaquette
`p_i`, and put

```text
A_i=R M_i.                                          (3)
```

If `alpha_i` denotes the coefficient of that character in the supplied local
action, then the corresponding supplied term is

```text
B_i=alpha_i A_i J_3.
```

The relations proved in lemma T `C J_3=J_3 C_c` and `[C,Q]=0` give, with operators acting
right to left,

```text
B_i C_c+C B_i
 =alpha_i(A_i C+C A_i)J_3.                         (4)
```

Thus the complete two-order fine-packet core is
`S_i=A_i C+C A_i`. The common physical scalar is
`-epsilon alpha_i/2`; it multiplies both order contributions and cannot change
their relative sign. Equation (4) is a transport identity on `Ran J_3`, not an
assertion that the actual coarse-to-residual map can be composed with itself.

## Physical conditional Haar

Write

```text
rho_n=(n,(-1)^n),       V=rho_1.
```

Below, `r_n` abbreviates the supplied multiplier `r_(n,(-1)^n)`. For
positive spin the supplied exterior family is parity-independent; all labels
are nevertheless retained in the representation argument. Reversing a link
orientation dualizes a real `O(3)` irrep and does not change its multiplier.

At fixed coarse deltas, each individual first-cell plaquette variable has Haar
marginal under physical `J_3`. Hence for every nontrivial `rho_n`,

```text
E[chi_(rho_n)(p_i) | coarse]=0.                    (5)
```

The coarse first-cell loop is
`C0=(u0,u1,u2,h3,v2^-1,v1^-1,v0^-1,h0^-1)` and contains neither internal rung
`h1` nor `h2`. Every fixed plaquette top network carries `rho_n` on at least
one of those internal rungs: `p0` carries it on `h1`, `p1` on `h1,h2`, and
`p2` on `h2`. This linkwise representation is nontrivial while every
`Ran J_3` coarse function is trivial there. Exact Peter--Weyl orthogonality
therefore gives zero coarse projection channel by channel, including for the
`p2/C1` shared-rung decomposition. After multiplication by `V`, the top output
is `rho_(n+1)` on the same internal rung, so

```text
A_i : top(rho_n) -> top(rho_(n+1)) + lower spins,  (6)
```

with unit top coefficient. Physical `Q` here is conditional Haar and is not a static cup projector.

The scalar subtraction affects lower branches when the trivial irrep occurs;
it never removes the displayed positive-spin top output. This conclusion uses
the actual conditional-Haar projector and the supplied proper-subset geometry,
not a static cup-image analogy.

## Original-link reconstruction

The three fine plaquettes and the neighboring merged loop are

```text
p_i=(u_i,h_(i+1),v_i^-1,h_i^-1),                  (7)
C1 =(u_3,u_4,u_5,h_6,v_5^-1,v_4^-1,v_3^-1,h_3^-1). (8)
```

Therefore `p0` and `p1` are disjoint from `C1`. A spin-`n` plaquette character
times the `C1` vector character has four links labelled `rho_n` and eight
links labelled `V`, so its crossing eigenvalue is

```text
d_n^D=r_n^4 r_1^8.                                 (9)
```

The boundary plaquette `p2` shares exactly `h3` with opposite orientation.
On the unique highest-coupled channel, the three exclusive `p2` links carry
`rho_n`, the seven exclusive `C1` links carry `V`, and `h3` carries
`rho_(n+1)`. Thus

```text
d_n^S=r_n^3 r_1^7 r_(n+1).                        (10)
```

The shared rung is counted once in equation (10), in its coupled
representation. Treating the two loops as independent would incorrectly give
`r_n^4 r_1^8`; multiplying that by an extra shared factor would double count
the same original link.

For this shared network the two loop junctions join three paths with labels
`(n,1,n+1)`. The invariant intertwiner is one-dimensional at each junction:
in the `SU(2)` lift, `Sym^(2n) tensor Sym^2` contains the highest
`Sym^(2n+2)` exactly once, and multiplication of highest vectors
`x^(2n) x^2=x^(2n+2)` has coefficient one. Thus the chosen top network and
its raised output have an unambiguous unit highest-vector normalization.
This argument concerns this three-path graph; it makes no uniqueness claim
for arbitrary spin networks with more intertwiners.

The independent checker derives (10) from oriented links rather than from the
displayed powers. On a common maximal torus, choose weight `n` on `p2` and
weight `-1` on the oppositely oriented `C1` loop. The shared exponent is then
`n+1`, while every exclusive exponent saturates the labels above. The
conjugate monomial gives the opposite exponents. Both have coefficient one,
and multiplying by the action vector produces the unique shared exponent
`n+2`. This also establishes the unit top-fusion coefficient without importing
the primary formula.

## Both operator orders

Let `g_n^i` denote the selected top network for placement `i`; on a disjoint
placement it is the product character itself, while on `p2` it is the top
shared-rung component. Normalize the latter so that its two conjugate
saturated maximal-torus monomials have coefficient one, matching the character-
product normalization used above. With this convention the unique top fusion
coefficient is exactly one. Centrality gives

```text
C g_n^i=d_n^i g_n^i.                               (11)
```

The crossing-first contribution is

```text
A_i C g_n^i=d_n^i g_(n+1)^i+lower,                 (12)
```

and the action-first contribution is

```text
C A_i g_n^i=d_(n+1)^i g_(n+1)^i+lower.            (13)
```

They land on the same uniquely labelled top network. Because equation (4)
contains a plus sign,

```text
S_i g_n^i=(d_n^i+d_(n+1)^i)g_(n+1)^i+lower.       (14)
```

Substituting (9) and (10) gives equations (1) and (2). For every multiplier in
the supplied finite-positive family,

```text
s_n^D>0,       s_n^S>0.                            (15)
```

Hence the unique top branch used by the ordered calculation survives the
complete two-order local response on each fixed placement. It is reinforced,
not canceled.

## Exact cancellation loci and endpoints

The calculation also identifies where the conclusion stops. For real
multipliers and `r_1` nonzero,

```text
s_n^D=0  iff  r_n=r_(n+1)=0.                       (16)
```

The shared placement has the wider algebraic locus

```text
s_n^S=0  iff
r_(n+1)[r_n^3+r_(n+1)^2 r_(n+2)]=0.               (17)
```

Thus signed nonphysical multipliers can cancel a shared-placement layer. For
example, `r_n=r_(n+1)=1` and `r_(n+2)=-1` makes (17) vanish exactly. The
signed cancellation control lies outside the supplied positive multiplier domain.
At identity crossing every `d_n` is one and each symmetric factor is exactly
two. At the Haar endpoint the relevant nontrivial multipliers vanish, and at
`r_1=0` the vector spectator kills all three placement factors.

These are parameter boundaries of the coefficient formula. They are not
evidence for cancellation at a finite positive supplied crossing.

## Pure-placement all-layer coefficient

For the normalized selected fine-packet extension, start with `g_1^i` and
apply `S_i` repeatedly. The spin-`N` coefficient is

```text
T_N^D=product_(j=1)^(N-1) r_1^8(r_j^4+r_(j+1)^4),             (18)

T_N^S=product_(j=1)^(N-1)
      r_1^7[r_j^3 r_(j+1)+r_(j+1)^3 r_(j+2)].                 (19)
```

Restoring the parent scalar for a pure placement multiplies (18) or (19) by
`(-epsilon alpha_i/2)^(N-1)`. The induction is exact because every action
raises spin by at most one and the displayed top summand has multiplicity one.
No lower branch can reach spin `N` at layer `N`.

If the local action is kept formal as `sum_i alpha_i M_i`, equations (18)--(19)
are the coefficients of the pure monomials `alpha_i^(N-1)`. That statement
does not enumerate mixed monomials or assert their numerical behavior after a
particular amplitude specialization.

## Scope locks

The exact result is the complete two-order coefficient on each fixed local
placement and its pure-placement selected extension.

Here “complete two-order” means that both parent orders are included for the
selected defining-vector action component. It does not mean that every Fourier
irrep in the full supplied action has been iterated.

Mixed-placement histories are not evaluated by this coefficient theorem.

The full action exponential is not evaluated by this coefficient theorem.

No invariant-closure statement is proposed.

No global minimal-memory statement is proposed.

No statement about arbitrary `r/q`, physical time evolution, continuum
dynamics, gravity, or TOE closure is proposed. The selected formal iteration
is not identified with powers of the actual coarse-to-residual `L_epsilon`.

## Strongest missing lemma and next falsifier

The strongest missing lemma is an exact recoupling classification for every
mixed word in `S=sum_i alpha_i S_i`, with physical `Q` applied at each typed
domain transition. Such a classification must determine whether histories
from different placements enter distinct spin-network sectors or the same
sector with signed recoupling coefficients. The next falsifier is the shortest
mixed word containing both a disjoint placement and `p2`; compute all channels
that reach its maximum external labels and compare their exact coefficients at
the supplied positive multipliers.

## Prior-art and approach record

The original packet records a prior-art sweep and historical parent review
statuses. Those records are preserved for recovery, not reasserted as a fresh
novelty search or accepted authority. The retained calculations are the following.

The attempted approaches were:

1. **Disjoint character recurrence:** exact and used in the packet; it
   shows directly that the two ordered coefficients are `d_n^D` and
   `d_(n+1)^D`.
2. **Independent original-link census:** exact and retained; it reconstructs
   all loops and rejects altered `4/8` powers.
3. **Shared loop treated as disjoint:** rejected by the literal `h3`
   intersection and the coupled label `rho_(n+1)`.
4. **Shared rung counted twice:** rejected because central crossing acts once
   per original link; the torus monomial has one shared exponent.
5. **Maximal-torus highest monomial:** exact and retained; it independently
   establishes shared multiplicities `3/7/1` and top multiplicity one.
6. **Signed hostile cancellation:** exact as a counterfactual; it identifies
   the boundary (17) but lies outside the supplied positive domain.
7. **Sample-rank continuation:** not used; the universal coefficient follows
   from triangular representation labels rather than finite sampled rank.

## Verification and hostile falsifiers

The primary runner uses exact rational arithmetic. It constructs the full
disjoint `A C+C A` coefficient tables in two different ways, checks both
positive and signed samples, compares every placement to the independent
link-census oracle, tests identity/Haar/spectator-zero endpoints, and records
the exact signed shared-rung cancellation locus. The independent checker
imports no primary module and derives its labels from oriented loop incidence
and maximal-torus characters.

The optional legacy `--mutation-suite` contains seven algebraic counterfactual
comparisons and seven note-text scope substitutions. It is not fourteen actual
whole-source mutants. The original independent review separately altered actual
Haar subtraction and shared-link orientation: the first produced six failing
predicates; the second rejected execution with `KeyError(0)`. These historical
controls are preserved in the external review packet. They need no replay for
the present premise/input repair. The primary calls all twelve independent
checker predicates; its current cache records the genuine final execution.

The five-resolution stdout lines are scope bookkeeping, not additional
numerical checks or an audit verdict. This positive theorem invokes no no-go
classification or formal audit.

## Review record

This result answers the Block247 symmetric-order falsifier without accepting
the earlier broader ordered theorem. It replaces the provisional possibility of
two-order cancellation, on each fixed placement, with the exact reinforcement
formulas (1)--(2). The scope ends at fixed-placement top coefficients
and formal pure-placement monomials. The mixed-placement recoupling lemma and
the domain-correct physical carrier remain subsequent work. No audit verdict,
merge, PR creation, push, axiom edit, or primitive edit is part of this packet.
