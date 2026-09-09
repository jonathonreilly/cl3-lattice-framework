---
claim_id: ac_occupancy_grain_support_typed_formal_target_repair_bounded_theorem_note_2026-09-02
claim_type: bounded_theorem
claim_scope: "Conditional projective support identity, finite realification/Pfaffian algebra and supplied binary-law odds discriminator. No physical sector weights, matter action, event quotient, probability law or charged-lepton value is selected."
runner: scripts/ac_occupancy_grain_support_typed_target_repair_2026_09_02.py
required_parents:
  - minimal_axioms
actual_current_surface_status: conditional-support
authority: none
---

# Occupancy grain and determinant support

Date: 2026-09-02; corrected 2026-09-09 from original PR #7838.

Type: bounded_theorem

The [occupancy-grain target](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md)
asks for a physical matter action and measure that distinguish one K/CPT-orbit
cell from independently counted channels. A whole-carrier determinant power
does not, by itself, make that distinction. The exact support algebra below
specifies when an added factor changes the relative singlet/doublet count.
It leaves the physical carrier, action, measure, event partition and balance
map supplied or open. This source changes no obligation, axiom or audit status.

**Primary runner:** [symbolic and finite checks](../scripts/ac_occupancy_grain_support_typed_target_repair_2026_09_02.py).
The primary imports and calls the [independent arithmetic checker](../scripts/independent_ac_occupancy_grain_support_typed_target_repair_2026_09_02.py),
which uses separate Gaussian-integer and permutation-determinant implementations.
It is a computational cross-check, not an independent scientific verdict.
Both sources and both [primary](../logs/runner-cache/ac_occupancy_grain_support_typed_target_repair_2026_09_02.txt)
and [checker](../logs/runner-cache/independent_ac_occupancy_grain_support_typed_target_repair_2026_09_02.txt)
caches belong to the evidence closure. Neither runner imports the other in reverse.

## The support theorem and its domain

Let `nu_s,nu_d>0`. They are initially two supplied mathematical weights.
Interpreting them as physical cell multiplicities, determinant degrees or
energy weights requires a separate identification. Their projective class is
`[nu_s:nu_d]`. For physical additions take `q_s,q_d>=0`; the algebraic identity
also holds for real additions whenever `nu_s+q_s!=0`.

Under the supplied map `r(nu)=nu_d/(2 nu_s)`, subtraction gives

```text
r(nu+q)-r(nu)
 = (nu_s q_d - nu_d q_s)/(2 nu_s (nu_s+q_s)).
```

The denominator is nonzero on the stated domain. Therefore the ratio changes
if and only if `nu_s q_d - nu_d q_s != 0`. Since `nu_s>0`, vanishing is
exactly `q=(q_s/nu_s)nu`, including `q=0`. Common duplication `q=nu` is neutral;
a strictly positive doublet-only addition increases r; a strictly positive
singlet-only addition decreases it. This proves the criterion without a
finite census or a physical balance assumption hidden in the algebra.

For the conventional expressions `E_s=3a^2`, `E_d=6|b|^2`, with `a!=0`,
identifying `E_s:E_d=nu_s:nu_d` would give

```text
r=|b|^2/a^2=nu_d/(2nu_s),
Q=(1+2r)/3=(nu_s+nu_d)/(3nu_s).
```

That identification and the Q dictionary are supplied conditions, not derived
observables. `(1,1)` then gives r=1/2, Q=2/3; `(1,2)` gives r=1, Q=1.
No experimental mass value or preferred sector weights enter the derivation.

On the supplied finite set `{s,+,-}` with involution `s↦s,+↔-`, there is one
fixed point and two orbits. Counting atoms gives multiplicities `(1,2)`;
counting orbits gives `(1,1)`. Neither convention establishes a physical K/CPT
readout or the multiplicity of independent integration variables.

For a supplied conjugate-pair spectrum,
`D=lambda_s lambda_+ lambda_-=lambda_s|lambda_+|^2`, channel-degree coordinates
are `(1,2)`. Global `D conjugate(D)` doubles them to `(2,4)`. Aggregated
singlet/doublet-factor coordinates instead give `(1,1)→(2,2)` for that same
global operation. Both preserve the ray. By contrast, adding only one
independent doublet cell to `(1,1)` gives `(1,2)` and changes the ray. Sector
support must be specified before determinant powers can diagnose occupancy.

## Realification, Pfaffians and the Jacobian

For any complex square matrix `K=X+iY`, the real matrix

```text
R(K) = [[X,-Y],[Y,X]]
```

is similar over the complex numbers to `diag(K,conjugate(K))`: the invertible
coordinate map sends real-pair coordinates `(x,y)` to `(x+i y,x-i y)`.
Consequently `det_R R(K)=det_C K det_C conjugate(K)=|det_C K|^2`, including
singular K. This statement concerns the entire supplied carrier.

For the skew matrix `A_K=[[0,K],[-K^T,0]]` of size 2n, define the Pfaffian as
the top exterior coefficient of the two-form
`omega=(1/2) sum_ij A_ij e_i∧e_j`: `omega^n/n! = Pf(A)e_1∧...∧e_(2n)`.
Grouping the off-diagonal terms for A_K puts the n first-block coordinates
before the n second-block coordinates. The reordering sign is
`(-1)^(n(n-1)/2)` and the coefficient sum is the determinant expansion of K.
Thus `Pf(A_K)=(-1)^(n(n-1)/2)det(K)` in this coordinate order.

Under an invertible matrix M, the top exterior coefficient transforms by
`det(M)`, giving `Pf(M^T A M)=det(M)Pf(A)`. The Berezin change of variables
has inverse Jacobian `det(M)^(-1)`, so the one-field integral is unchanged.
The coordinate orientation convention must be transported with the measure.
A change to Majorana-paired coordinates does not add an independently
integrated conjugate field. If such an independent field is supplied, its
separate determinant multiplies the original, yielding the second power.
These are finite algebra statements, not a physical action or measure selection.
The odd-dimensional real algebra `R⊕C` is not an ordinary realification of a
complex vector space; a mixed real/complex polarization must be specified.

The retained fixture is
`K=[[1+2i,3−i],[2,4+i]]`, with `det K=−4+11i`, `det R(K)=137`, and
`Pf(A_K)=4−11i`. Changing the upper-right realification block from −Y to +Y
in the actual matrix gives determinant −121. The original congruence matrix

```text
M0 = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,2]]
```

has determinant one; it checks congruence but cannot catch an omitted Jacobian.
The added `M1=diag(2,1,1,1)` has determinant two. The same residual function
returns zero with its divisor and `4−11i` when the divisor is actually omitted.
The separate integer implementation also checks this nonunit transformation.
The general proof is the exterior-power argument, not these fixtures alone.

## Historical sector-local comparison

The original #7340 comparison was pinned to head
`b2664db3fc277983cf657fc6ad47db860b7a49fe`. Its relevant supplied expression
was `F_c=det(record slice)/det(k=0 singlet fiber)=u^2`: the singlet fiber is
already removed before the doublet factor is compared with a fixed singlet.
At its quoted scalar fixture,

```text
u=(43/35)^2+(129/175)^2=62866/30625,
u^2=3952133956/937890625.
```

This arithmetic and the distinction between sector-local and global power
are retained. This note does not certify that PR's operator, reflection,
field-reality, no-registration or physical sewing chain. The reality choice
and slot-to-r map remain supplied/proposed. The expression is used as a
conditional comparator, not as an accepted physical determinant premise.
Other original PR comparisons and historical status claims remain recoverable
in the original note; they do not establish current open/closed PR status here.

## Supplied binary-law discriminator

For positive controlled x, stipulate a binary final-Record law
`p_n(1|x)=x^n/(1+x^n)`, `p_n(0|x)=1/(1+x^n)`. Its odds are `O_n(x)=x^n`,
so `O_n(4)/O_n(2)=2^n`: two for n=1 and four for n=2. This is an identity
between conditional law values; normalization and a common formation-rate
scale cancel from the odds. It does not supply a Record writer, actual repeated
trials, convergence of empirical frequencies or a source-to-probability map.
Physical use needs the same calibrated source, event codec and eligibility
conditions across both settings, as well as the physical sector identification.

## Physical obligations and present premise boundary

Five useful construction obligations remain: a physical carrier/action/measure;
a singlet/doublet/K event factorization; a support-to-energy/readout map;
a source/action-to-probability map for the operational route; and repeated-Record
eligibility/context with a common event codec. Their exact dependency relations
are unproved. The original ten-pair independence table is withdrawn: the
statements were not supported by implication proofs or matching countermodels.
A single physical construction may discharge several obligations together.
This note supplies no universal no-go or proof of pairwise physical independence.

The current [minimal memo](MINIMAL_AXIOMS_2026-06-29.md) leaves dynamics,
formation-site/rate, K/CPT structure and physical observable bridges downstream.
The August13 reset removed scalar finite Record additivity; this note does not
restore it. The [scale](SCALE_REFERENCE_PRIMITIVE_NOTE.md) declaration supplies
units, [kinetic isotropy](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) supplies
its stated normalization, and the [realized-state](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
declaration permits pointwise evaluation without selecting a state or weight.
Their current texts and the foundation registry are bound as premise-scope
context. No wider historical theorem linked by those texts is imported.

A useful future target is to derive `Z_phys=Z_s F_d^n Z_rest`, with fixed
singlet factor and normalization, derive the physical event/energy map, and
establish n from independent physical field content. A global conjugate copy
must be tracked separately because it changes the relative grain only when
its support is anisotropic. Physical action, alternate carrier, symmetry/reality,
and calibrated-writer approaches remain open. Additional approved premises,
if ever proposed, require the owner's separate authorization. No present
change to foundation or obligation registries follows from the algebra.

## Reproduction and recovery

Run the primary and checker commands linked above. Both mains run once on the
final frozen sources under 120 seconds/2 GiB each, BLAS1. The primary performs
its SymPy algebra and calls the independent finite arithmetic; the checker
also runs standalone. A normal static import registers it in both actual
helper consumers. Inputs include both source bodies, this note and only the
current target/premise contexts used here; the checker binds itself and this
note. Pins and caches cover the actual source/input union.

Old fixed ledger counts16/108/critical, whole-HEAD comparisons to the September2
base, and historical missing-path/hash checks have been removed from the
scientific predicates. They are preserved as dated custody evidence. The old
30-flag record is historical; label-only scope toggles receive no scientific
mutation credit. The original primary was blocked before launch, and the
original checker's12/1 count failure is preserved without a baseline retry.
The [correction history](../.claude/science/physics-loops/occupancy-grain-7838-correction-20260909/HISTORY.md)
accounts for every original claim/predicate and all30 endpoint bodies plus12
prior versions. These recovery files lie outside active note discovery.
Independent landing confirmation remains distinct from formal audit, which
is deferred. No physical TOE completion is claimed.
