---
claim_id: admissibility_exterior_character_time_refinement_semigroup_obstruction_bounded_theorem_note_2026-08-28
claim_type: bounded_theorem
claim_scope: "For every finite exterior-character member f_n of the supplied O(3) plaquette family, compute the exact determinant and vector convolution multipliers and prove that no continuous monotone common-clock reparameterization turns the Haar-normalized coupling family into a central probability convolution semigroup. The obstruction survives one supplied projected periodic-cycle specialization because both determinant and vector character spin networks survive the simultaneous local Haar projector. A separately supplied O(3) heat-plus-component-jump semigroup has a different exact channel law. A fixed nonconstant spatial half multiplier supplies only an anisotropic noncommutation boundary. This is not a theorem about every full transfer, a selected action, carrier refinement, physical time, Hamiltonian, continuum, Lorentz covariance, gravity, or fractional in-family roots."
depends_on:
  - admissibility_dirac_kahler_exterior_character_action_transfer_bounded_theorem_note_2026-08-28
  - minimal_axioms
runner: scripts/admissibility_exterior_character_time_refinement_semigroup_obstruction_2026_08_28.py
independent_checker: scripts/admissibility_exterior_character_time_refinement_semigroup_obstruction_independent_2026_08_28.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_exterior_character_action_transfer_bounded_theorem_note_2026-08-28
target_blocker_text: "A derived Admissibility law, a semigroup or strong-curvature condition, determinant data, metric/source coupling, or another framework-native criterion could distinguish the members."
source_of_blocker_text: frontier_question
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Supply an indexed carrier/coefficient/measure refinement map and test the co-scaled complete transfer; the present exact common-clock obstruction does not decide a different action family or a Trotterized refinement construction."
conditional_surface_status: "exact common-clock convolution-semigroup obstruction for every finite f_n and one supplied gauge-projected periodic-cycle specialization; no universal full-transfer, co-scaled refinement, continuum, or physical-time conclusion"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact O(3) component bookkeeping, tensor multiplicities, normalized irrep multipliers, common-clock contradiction, projected-cycle lift, and explicit heat/jump and fixed-multiplier boundaries prove the stated finite mathematical discriminator without fitted data"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Exterior-character time-refinement semigroup obstruction

**Date:** 2026-08-28

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — a review proposal, not an audit verdict.

## Result up front

The supplied exterior-character action family has positive crossing kernels and
a valid fixed-step spectral logarithm, but its coupling is not an exact common
semigroup clock.

For every integer `n>=1`, Haar-normalize the one-link `O(3)` crossing weight
from the linked [exterior-character action and transfer](ADMISSIBILITY_DIRAC_KAHLER_EXTERIOR_CHARACTER_ACTION_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md).
Let `r_det^(n)(kappa)` and `r_V^(n)(kappa)` be the scalar convolution
multipliers in the determinant and defining-vector irreducible channels.  As
`kappa` tends to zero through positive values, both vanish to first order, but

```text
lim r_det^(n)(kappa)/r_V^(n)(kappa) = (n+2)/n != 1.  (1)
```

If one continuous monotone clock `t(kappa)` made this family a central
probability convolution semigroup, its positive channel multipliers would be
`exp[-E_pi t(kappa)]`.  Equal small-`kappa` logarithmic orders force
`E_det=E_V`, so the two multipliers would have to agree for every `kappa`.
Equation (1) contradicts that conclusion.  No nonlinear reparameterization of
the coupling repairs the mismatch.

This obstruction is not lost under every gauge projection.  On one supplied
periodic spatial cycle with zero spatial half-action, tree gauge fixing leaves
the holonomy class Hilbert space.  Both determinant and vector character spin
networks survive the simultaneous local `O(3)` projector.  Their linkwise
transfer multipliers are `r_det^L` and `r_V^L`, so the same contradiction holds
for the complete top-normalized projected transfer on that specialization.

The result does not prove nonembeddability for every nonconstant full transfer.
It does not select a heat kernel, time spacing, component-jump rate, or action.
A separately supplied co-scaled or Trotterized family remains open.  Every
fixed positive injective step still has its support-qualified spectral log;
fractional spectral powers are not proved to be in-family positive-density
refinements.  There is no physical clock, no continuum limit, and no action
selection.

## Imports and open boundaries

The two load-bearing dependencies are the linked exterior-character parent and
the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).  The latter keep absent
physical identifications absent; they do not supply the action or a clock.

| Input | Role here | Provenance | Open boundary |
|---|---|---|---|
| `O(3)` edge carrier, full exterior representation, `Q=16-2 chi`, and every finite `f_n` | actual crossing family tested | linked exterior-character parent | no framework selection of this family |
| normalized Haar measure and central convolution orientation | probability normalization and Peter-Weyl multipliers | supplied finite mathematical convention inherited from the parent | no physical measure or time law |
| positive coupling `kappa` | index of the displayed family | supplied dimensionless coefficient | not a lattice spacing or clock |
| admissible common clock `t(kappa)` | object refuted | defined here as continuous, strictly monotone and nonconstant, with the identity approached at `t=0` and the Haar endpoint at arbitrarily large `t` | pathological relabelings without the semigroup endpoints are outside the claim |
| periodic oriented cycle `C_L`, `L>=1`, with linkwise crossing and no spatial plaquette/half-action | one complete projected specialization | supplied finite topology and temporal assembly | no theorem for trees, arbitrary graphs, or nonconstant half-actions |
| simultaneous local `O(3)` Haar projector | gauge-invariant cycle Hilbert space | supplied parent construction specialized to `C_L` | no physical-state identification |
| rotational diffusivity `D` and central component-jump rate `gamma` | comparison semigroup only | separately supplied comparator | neither rate is derived or selected |
| positive bounded nonconstant fixed half multiplier `M` | anisotropic endpoint/noncommutation control | separately supplied boundary family | not a co-scaled physical refinement |
| fixed-step spectral logarithm | mathematical support reconstruction | linked parent | no in-family root, clock, Hamiltonian, or continuum theorem |

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) explicitly do not choose a
Hamiltonian or transfer operator, transition weights, a time metric, or a
source/action identification.  Those absences remain load-bearing fences.

## `O(3)` irreducibles and the exterior character

Write the irreducible representations of `O(3)` as `(ell,p)`, where
`ell>=0`, `d_ell=2ell+1`, and central inversion `z=-I` acts by `p=+1` or
`p=-1`.  The four summands of the full exterior representation are

```text
rho = 1 + det + V + det V
    = (0,+) + (0,-) + (1,-) + (1,+).                (2)
```

For `g in O(3)`, the linked parent proves

```text
chi_rho(g)=(1+det g)(1+Tr g),
Q(g)=16-2 chi_rho(g).                                (3)
```

Consequently `chi_rho` vanishes on the entire improper component.  On the
proper component, write `g=R in SO(3)` and

```text
chi_A(R)=1+chi_1(R),       chi_rho(R)=2 chi_A(R).    (4)
```

For an improper element `g=zR`, the character of `(ell,p)` is
`p chi_ell(R)`.  Normalized Haar measure gives each component mass `1/2`.
These facts are group and measure inputs, not a determinant-sector selection.

## Linear member: exact component and Fourier coefficients

For `n=1`, remove the common factor `exp(-16 kappa)` and put

```text
b_ell(kappa)
 = integral_SO(3) exp[4 kappa chi_A(R)] chi_ell(R) dR. (5)
```

The normalized `SO(3)` class measure is
`(2/pi) sin^2(theta/2)dtheta`.  Direct integration gives

```text
b_ell(kappa)
 = exp(8kappa)[I_ell(8kappa)-I_(ell+1)(8kappa)]
 = sum_(m>=ell) M_ell(m) (4kappa)^m/m!,              (6)

M_ell(m)=C(2m,m-ell)-C(2m,m-ell-1).                 (7)
```

Equation (6) is only a compact notation for the directly derived integer
series (7); no tabulated Bessel value is imported.  Because nontrivial
`SO(3)` characters integrate to zero against the constant improper weight,
the Haar-normalized `O(3)` convolution multipliers are

```text
r_triv=1,
r_det=(b_0-1)/(b_0+1),
r_(ell,p)=b_ell/[(2ell+1)(b_0+1)],   ell>=1.          (8)
```

The proper and improper probability masses are respectively
`b_0/(b_0+1)` and `1/(b_0+1)`, so `r_det` is exactly their difference.
The constant improper density also gives

```text
r_V=r_(det V).                                       (9)
```

The first exact series from (7) are

```text
b_0=1+4k+16k^2+(160/3)k^3+(448/3)k^4+O(k^5),
b_1=  4k+24k^2+96k^3+(896/3)k^4+O(k^5),
b_2=       8k^2+(160/3)k^3+(640/3)k^4+O(k^5),
b_3=                  (32/3)k^3+(224/3)k^4+O(k^5). (10)
```

Substitution into (8) yields

```text
r_det=2k+4k^2+(8/3)k^3-16k^4+O(k^5),
r_V  =(2/3)k+(8/3)k^2+(16/3)k^3+O(k^4),
r_(2,p)=(4/5)k^2+(56/15)k^3+O(k^4),
r_(3,p)=(16/21)k^3+O(k^4).                          (11)
```

All finite positive-`kappa` multipliers in these channels are strictly between
zero and one.  Strict positivity follows from the positive tensor-character
expansion in (6); strict contraction follows because the normalized density is
nonconstant and the relevant irreducible character is not almost-everywhere
constant.

## No common semigroup clock for `f_1`

A continuous central probability convolution semigroup with strictly positive
Fourier multipliers has, in each irreducible channel,

```text
r_pi(t)=exp(-E_pi t),       E_pi>=0.                 (12)
```

Indeed convolution gives `r_pi(t+s)=r_pi(t)r_pi(s)`; continuity and strict
positivity turn `-log r_pi` into a continuous additive nonnegative function,
hence `E_pi t`.  Every finite `kappa` here has a nonzero multiplier, so the
relevant `E_pi` are finite; the nontrivial Haar endpoint makes them positive.

Here the identity measure is approached as `kappa` grows, while `kappa=0` is
normalized Haar and kills every nontrivial channel.  An admissible clock is
therefore continuous and strictly decreasing in `kappa`, tends to zero at the
identity endpoint, and becomes arbitrarily large toward the Haar endpoint.

If (12) held after a common reparameterization, (11) would give

```text
E_det/E_V
 = lim_(k->0+) log r_det(k)/log r_V(k)=1.            (13)
```

Thus `E_det=E_V`, which forces `r_det(k)=r_V(k)` for every positive `k`.
But (11) instead gives

```text
lim_(k->0+) r_det(k)/r_V(k)=3.                       (14)
```

This contradicts the common-clock law.  An irrep-dependent prefactor is not
an escape: the identity element of a probability semigroup makes every such
prefactor one.  An irrep-dependent clock changes the claim and is not one
time parameter.

The higher channels give independent teeth.  Their small-coupling orders
would force `E_(ell,p)/E_det=ell`; hence a common clock would require
`r_(2,p)=r_det^2` and `r_(3,p)=r_det^3`.  Equation (11) instead gives the
leading ratios `1/5` and `2/21`.

## Every finite nonlinear member

For the linked action member

```text
f_n(Q)=2[8^n-(8-Q/2)^n]/[n 8^(n-1)],                (15)
```

the crossing weight is

```text
w_(n,k)(g)
 = exp(-16k/n) exp[2k chi_rho(g)^n/(n8^(n-1))].     (16)
```

On the proper component define

```text
alpha_n=2^(4-2n)/n,
b_ell^(n)(k)
 = sum_(m>=0) M_ell(nm)(alpha_n k)^m/m!.            (17)
```

The component calculation is unchanged, so (8) holds with `b_ell` replaced
by `b_ell^(n)`.  The first multiplicities are exact Catalan differences:

```text
M_0(n)=C_n,
M_1(n)=C_(n+1)-C_n=[3n/(n+2)]C_n.                  (18)
```

Therefore

```text
r_det^(n)(k)
 = [2^(3-2n) C_n/n] k+O(k^2),
r_V^(n)(k)
 = [2^(3-2n) C_n/(n+2)] k+O(k^2).                  (19)
```

Both channels again vanish to first order.  Their logarithmic ratio forces
equal semigroup energies, while their multiplier ratio tends to `(n+2)/n`.
This proves the common-clock obstruction for every finite `n>=1`, not merely
for the linear member.

## Gauge-projected periodic-cycle lift

Let `C_L` be a supplied oriented periodic spatial cycle with `L>=1` stored
edges.  Use normalized product Haar measure, the linked temporal crossing on
each edge, and zero spatial half-action.  This is one supplied projected
periodic-cycle specialization of the parent, not a cubical three-dimensional
volume claim.

On

```text
H_L=L^2(O(3)^L),                                    (20)
```

the local vertex gauge group acts at both endpoints of each edge.  Tree gauge
fixing identifies the range of the simultaneous Haar projector with

```text
P H_L isomorphic to L^2(O(3))^Ad                    (21)
```

through the based holonomy `W=U_L...U_1`.  The normalized character spin
networks

```text
Phi_(ell,p)(U)=chi_(ell,p)(W),       ||Phi||=1       (22)
```

all survive.  In particular, `Phi_det` distinguishes the two holonomy
components and `Phi_V` is a separate nonconstant gauge-invariant mode.

For independently applied linkwise crossings,

```text
P C_(n,k)^tensor L P Phi_pi = r_pi^(n)(k)^L Phi_pi. (23)
```

The constant character is the unique top for finite positive coupling.
Top normalization has already been included in `r_pi`.  Both decisive cycle
multipliers vanish to order `L`, so a common clock again forces equal channel
energies.  Their leading ratio is

```text
[(n+2)/n]^L !=1.                                    (24)
```

Thus the actual complete top-normalized projected transfer on this disclosed
zero-half-action cycle is not a reparameterized convolution semigroup.

A tree gauge quotient can collapse to constants.  In that topology the two
spin networks used in (24) are absent, so it is a genuine escape from this
cycle proof, not evidence against it.  A holonomy-level single convolution
would give `r_pi` rather than `r_pi^L`; the same two-channel contradiction
still holds, but it is a different temporal extension and is not conflated
with (23).

## Supplied heat plus component-jump comparator

Disconnected `O(3)` needs component dynamics in addition to rotational
diffusion.  As a comparison only, supply `D>0`, `gamma>=0`, central inversion
`z=-I`, and the generator

```text
L=(D/2) Delta_SO(3)+gamma(Z-I),       (Zf)(g)=f(zg). (25)
```

With `Delta chi_(ell,p)=-ell(ell+1)chi_(ell,p)`, its exact multipliers are

```text
h_(ell,p)(t)
 = exp[-D ell(ell+1)t/2-gamma(1-p)t],                (26)

h_det=e^(-2gamma t),
h_(det V)=e^(-Dt),
h_V=e^[-(D+2gamma)t]=h_det h_(det V).                (27)
```

Every exterior member instead obeys `r_V=r_(det V)` and
`0<r_det<1`.  Fitting `gamma t` to `r_det` and `Dt` to `r_(det V)` would
predict `h_V=r_det r_(det V)`, not `r_V=r_(det V)`.  No finite exterior step
equals this supplied two-rate comparator.

At `gamma=0`, rotational diffusion stays in `SO(3)` and `h_det=1`; it does not
mix the improper component.  A positive component-jump rate is an extra law,
not something selected by a bi-invariant Lie-algebra metric.  More general
central convolution semigroups may exist; (25) is a supplied comparator, not
a classification of all Lévy generators and not an action-selection theorem.

## Restriction and quotient escape tests

Removing the improper component removes the determinant channel, so the
`O(3)` proof cannot simply be quoted on `SO(3)`.  The `n=1` restriction has a
separate exact common-clock mismatch.  After dropping the constant in the
proper density, put `y=4 kappa`; the spin-one and spin-two multipliers begin as

```text
r_1^SO=y/3+O(y^2),       r_2^SO=y^2/10+O(y^3).       (28)
```

Their logarithmic orders would require the energy ratio two and hence
`r_2^SO=(r_1^SO)^2`; the leading coefficients `1/10` and `1/9` disagree.
This is a narrow `n=1` restriction check, not a claim about every possible
`SO(3)` action family.

Conversely, the determinant-only `Z_2` quotient has only one nontrivial
Fourier channel.  That one-channel family can be reparameterized by its sole
positive multiplier.  It is a genuine escape obtained by changing the
carrier and deleting the rotational channels.

## Fixed nonconstant half multiplier: anisotropic boundary only

The cycle theorem used `M=1`.  A fixed nonconstant positive gauge-invariant
half multiplier does not restore convolution.  On a supplied finite pure-gauge
carrier, restrict to `P H`, require `[M,P]=0`, require `M` to be genuinely
nonconstant there, and let all temporal exterior couplings vary together while
`M` stays fixed.  The normalized crossing endpoints are

```text
C_0=|1><1|,             C_k -> I strongly as k->infinity. (29)
```

The convergence to the identity is strong, not operator norm convergence;
each finite convolution remains compact.  The corresponding unnormalized
full transfers have limits

```text
T_0=M C_0 M=|M><M|,
T_infinity=M^2,                                           (30)

[T_0,T_infinity]=|M><M^3|-|M^3><M|.                      (31)
```

For strictly positive `M`, (31) vanishes only if `M^2` is constant almost
everywhere.  A one-parameter semigroup is commuting; positive scalar top
normalization cannot repair a nonzero commutator.  More explicitly, if every
finite top-normalized `T_k` belonged to one semigroup, all finite pairs would
commute.  Uniform boundedness together with the norm limit at zero and strong
limit at infinity would then force `T_0` and `T_infinity` to commute, contrary
to (31).  Hence this fixed-`M` anisotropic family also has no common semigroup
clock.

This is only a boundary control.  Holding a spatial half-action fixed while
changing every temporal coupling is not a physical time refinement.  A
genuine construction could scale `M_t`, change carriers, rescale measures, or
use a Trotter product.  Equations (29)–(31) do not decide such a family.

## Fixed-step logarithm and exact claim boundary

For each fixed positive coupling, the linked parent's positive injective
operator has a densely defined support-qualified logarithm

```text
H_k=-log(T_k/||T_k||).                                  (32)
```

Integer powers are repeated applications of that supplied step.  Equation
(32) does not imply that another exterior coupling represents half a step,
that a fractional spectral power has a positive exterior density, or that the
coupling is physical time.  The theorem distinguishes three objects:

1. a fixed operator and its spectral calculus;
2. the displayed coupling-indexed exterior action family;
3. an indexed carrier/measure/coefficient refinement construction.

Only the second is refuted as a common-clock convolution semigroup, plus the
one exact cycle lift and the fixed-`M` anisotropic boundary.  The third remains
unsupplied.  There is no physical Hamiltonian, clock, continuum limit, Lorentz
covariance, gravity dynamics, Record identification, or selected action.

## Proof-obligation graph

| Obligation | Disposition |
|---|---|
| exterior character and component split | inherited from the linked parent and recomputed in (2)–(4) |
| normalized component masses | derived in (8) |
| linear irrep series | derived from integer multiplicities in (6)–(11) |
| arbitrary common-clock contradiction | proved in (12)–(14) |
| every finite nonlinear `f_n` | proved by Catalan multiplicities in (15)–(19) |
| common gauge projector | explicitly typed by (20)–(22) |
| complete projected cycle lift | proved by (23)–(24) |
| disconnected heat comparator | separately supplied and exactly contrasted in (25)–(27) |
| `SO(3)` and `Z_2` escapes | bounded in (28) and the following paragraph |
| fixed nonconstant `M` | exact anisotropic noncommutation boundary (29)–(31) |
| physical time/refinement | open; expressly not supplied |

The proof disposition is `CLOSED` for the declared common-clock obstruction
and projected-cycle specialization, and `CONDITIONAL/OPEN` for a different
action family, co-scaled refinement, or physical interpretation.

## No-Go Discipline Gate

The theorem contains bounded negative statements, so the full N1–N8 packet is
recorded here.

### N1 -- failed attack routes

| Route | Attempt and exact failure | Evidence/locator | Marker |
|---|---|---|---|
| use `kappa` itself as additive time | compare determinant and vector exponentials; their normalized laws disagree | (11)–(14) | `ATTEMPTED` |
| choose a nonlinear common clock from `r_det` | use `r_det` to define the clock; the vector then has the same energy but leading ratio `(n+2)/n` | (18)–(19) | `ATTEMPTED` |
| insert representation-dependent prefactors | allow one constant per channel; the semigroup identity fixes every prefactor to one | (12) and its derivation | `ATTEMPTED` |
| project to the gauge-invariant cycle Hilbert space | apply the simultaneous local projector; both decisive character spin networks survive | (20)–(24) | `ATTEMPTED` |
| restrict to `SO(3)` | remove determinant parity; the linear restriction has the separate spin-one/spin-two mismatch | (28) | `ATTEMPTED` |
| collapse to the determinant `Z_2` quotient | retain only one nontrivial channel; it can be reparameterized, but this changes the carrier and deletes the theorem's rotational modes | restriction/quotient boundary after (28) | `ATTEMPTED` |
| fit an `O(3)` heat kernel | add rotational heat and a component-jump rate; the exact channel identity still disagrees | (25)–(27) | `ATTEMPTED` |
| restore a fixed nonconstant spatial half multiplier | hold `M` fixed while varying the crossing; the endpoint transfers do not commute | (29)–(31) | `ATTEMPTED` |

The live next routes are an explicitly co-scaled complete transfer, a
different central action family, and an actual carrier/measure refinement map.

### N2 -- independence of remaining walls

The five interfaces in the full problem are listed below.  `C` is closed for
the exterior family in this note; the table records why that closure neither
closes nor is closed by each still-open interface.

- `C`: convolution embeddability of the bare crossing family;
- `F`: composition of a nonconstant complete transfer `MPCM`;
- `R`: carrier/measure refinement and comparison maps;
- `T`: physical time or Hamiltonian identification;
- `S`: framework selection of an action family.

They are collapsed only where one closure logically consumes another.  Here
`No` means no implication in that direction and `I` is the independence
result.

| Pair | First closes second? | Second closes first? | Exact separator | Result |
|---|---:|---:|---|---:|
| `C/F` | No | No | holding one positive nonconstant `M` fixed makes the displayed anisotropic `M C_k M` family noncommuting; a co-scaled `M_t` remains open | `I` |
| `C/R` | No | No | a convolution clock on one carrier supplies no coarse/fine embedding or measure comparison | `I` |
| `C/T` | No | No | a mathematical convolution parameter is not a physical clock | `I` |
| `C/S` | No | No | semigroup closure is an extra criterion and does not select itself | `I` |
| `F/R` | No | No | repeated same-carrier steps are not lattice refinement | `I` |
| `F/T` | No | No | a support log exists without a physical Hamiltonian interpretation | `I` |
| `F/S` | No | No | complete-transfer consistency does not derive the action | `I` |
| `R/T` | No | No | an isometric refinement map would still need a supplied time normalization | `I` |
| `R/S` | No | No | a refinement-compatible family remains imported unless derived | `I` |
| `T/S` | No | No | choosing a clock does not choose the coefficients or action form | `I` |

Thus no two of the five interfaces are silently identified.

### N3 -- hidden-wall scan

The occurrence scan covers `assume`, `assuming`, `suppose`, `choose`,
`supplied`, `canonical`, `background`, `by construction`, and `registered`,
plus `as is standard`, `framework provides`, `bridge context`, `naturally`,
`obviously`, and `standard QFT`.

| Hit family | Classification |
|---|---|
| `supplied` | every action, measure, topology, temporal assembly, comparator rate, and refinement convention is an Imports input |
| `inherited` | only the linked parent's exterior character and positive finite transfer are inherited |
| `admissible clock` | a definition of the response domain being refuted, not a physical-time import |
| `choose` | occurs only for a mathematical comparison or route; no physical value is selected |
| `canonical` | no theorem-body occurrence asserts a canonical action, time, jump rate, or refinement |
| `background` | no hidden physical background; the projected cycle and fixed-`M` carrier are explicit supplied specializations |
| `by construction` | no theorem-body occurrence is used to replace a proof; the runner derives every executable identity |
| `registered` | no theorem-body occurrence imports an unregistered primitive or authority |
| `Assume`/`assuming`/`suppose` | no theorem-body hits outside this occurrence-complete scan |
| `as is standard`, `framework provides`, `bridge context`, `naturally`, `obviously`, `standard QFT` | no theorem-body hits outside this occurrence-complete scan |

The word `physical` appears only in open-boundary or denial statements.

### N4 -- residual matching

| Residual source | Exact locator | Attacked residual | Claimed residual after this note | Match? |
|---|---|---|---|---:|
| exterior-action parent | `docs/ADMISSIBILITY_DIRAC_KAHLER_EXTERIOR_CHARACTER_ACTION_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md:445-468` | fixed-step log has no derived clock | (32) remains mathematical; no clock is promoted | yes |
| exterior-action parent | `docs/ADMISSIBILITY_DIRAC_KAHLER_EXTERIOR_CHARACTER_ACTION_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-28.md:470-500` | semigroup condition named as a possible discriminator | (12)–(24) refute the common-clock exterior family; other discriminators remain live | yes |
| minimal axioms | `docs/MINIMAL_AXIOMS_2026-06-29.md:114-130,173-190` | source/action and time remain outside axioms | no physical identification is promoted | yes |

The exact frontmatter blocker quote is the parent's lines 497–500.  This note
partially closes only its semigroup-discriminator branch.

### N5 -- rhetoric and resolution audit

`T/H` means tested here and holds; `U/N` means untested and no claim.

| Negative phrase | Per-element | Per-site | Per-mode | Per-block | Lattice-wide |
|---|---|---|---|---|---|
| no common clock for `f_1` | `T/H`: exact character coefficients | `T/H`: one crossing | `T/H`: determinant/vector and higher-spin teeth | `T/H`: projected cycle | `U/N`: checked and not executed — no carrier refinement family |
| no common clock for every finite `f_n` | `T/H`: Catalan counts | `T/H`: same supplied crossing | `T/H`: determinant/vector leading ratio | `T/H`: symbolic finite-`n` formula | `U/N`: checked and not executed — no `n=infinity` or continuum family |
| projection does not erase the obstruction on the cycle | `T/H`: link characters | `T/H`: local Haar action | `T/H`: determinant/vector spin networks | `T/H`: finite `C_L` lift | `U/N`: checked and not executed — arbitrary graph topology not claimed |
| exterior step is not the supplied heat/jump comparator | `T/H`: three channel identities | `T/H`: local convolution | `T/H`: determinant, vector, and det-vector | `T/H`: one comparator family | `U/N`: checked and not executed — no classification of all central semigroups |
| fixed log is not an in-family refinement | `T/H`: fixed operator calculus | `T/H`: one step | `T/H`: spectral powers distinguished | `T/H`: exact family mismatch | `U/N`: checked and not executed — no co-scaled refinement or physical time |

The primary runner prints the same five resolution scales.  Untested
lattice-wide resolutions remain explicitly open rather than being inferred
from the finite cycle.

### N6 -- convention, primitive, and prior-art scan

The convention/reframe scan found no change of parameter name that repairs a
common-clock multiplier identity.  The vocabulary and primitive scans found
no approved primitive supplying a clock, heat generator, component-jump rate,
or action selection.  The in-flight scan treated the connection stack as
non-authority and found the action/transfer parent but no semigroup theorem.

The current-source sweep was refreshed at
`origin/main=66e478505e055faf4a5b9e6f4883211e44304718` with:

```text
git grep -n -i -E '(character.*semigroup|semigroup.*character|Wilson.*convolution|convolution.*Wilson|time refinement|refinement.*transfer)' origin/main -- docs scripts
git grep -n -i -E '(heat kernel.*O\(3\)|O\(3\).*heat kernel|improper.*heat kernel|component jump|determinant.*semigroup)' origin/main -- docs scripts
git grep -n -i -E '(diffusion.*kernel|kernel.*diffusion|composition.*semigroup|semigroup.*composition|Markov.*generator|generator.*Markov)' origin/main -- docs scripts
for pr in 7761 7763 7764 7765 7767 7768; do gh pr view "$pr" --json number,headRefOid,state,baseRefName; done
```

Current-source and separately scanned branch-local hits, all non-linking
method/prior-art only, were:

- `docs/ACTION_FAMILY_CHARACTER_SEMIGROUP_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md:15-28,73-129,154-240`: `U(1)` Wilson/heat/Manton finite-coupling and convolution-square discriminator, not the all-`f_n` `O(3)` component theorem.
- `docs/SEMIGROUP_CLOSURE_DOES_NOT_FORCE_HEAT_KERNEL_QUADRATIC_CONDITION_BOUNDED_NOTE_2026-07-02.md:150-229`: a `Z_5` counterexample showing that semigroup closure alone does not select a heat/Casimir law.
- `docs/HEAT_KERNEL_GAUGE_ACTION_NATIVE_RP_PLANE_CHARACTER_POSITIVITY_ALL_COMPACT_GROUPS_NARROW_THEOREM_NOTE_2026-07-09.md:32-69,102-120,167-187`: a supplied heat action and character semigroup, with no selected `O(3)` component-jump rate.
- `docs/GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md:42-125,255-277`: compact-group convolution diagonalization, but no time-semigroup conclusion.
- `docs/BRIDGE_GAP_HK_TIME_DERIVATION_NOTE_2026-05-06.md:21-52,215-234,271-300`: a leading small-field `SU(3)` comparator, not finite-coupling `O(3)` authority.
- `docs/HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08.md:28-67,72-99`: an earlier candidate-level heat-semigroup and Wilson/Manton nonsemigroup claim; its generator premise remains open and its live row is unaudited.
- `docs/RECORD_COMPOSITION_BRIDGE_SEMIGROUP_POSITIVITY_SELECTION_BOUNDED_NOTE_2026-07-02.md:80-120,151-206,221-257`: conditional composition-to-convolution and finite cyclic semigroup witnesses, not an adopted composition law or this `O(3)` action.
- `docs/RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md:27-32,139-160,174-176`: the exact boundary that transition rates, a generator, and a clock require a supplier; its current ledger is unaudited despite older source prose citing it more strongly.
- Branch-local commit `c36d11e...`, `docs/ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md:445-465,557-585`: an earlier finite-window nonsemigroup witness, not this action-derived all-`f_n` theorem.

The in-flight PR heads checked were `#7761@311036f`, `#7763@714ba06`,
`#7764@488c07b`, `#7765@6894cdd`, `#7767@5b9d9ef`, and
`#7768@9b8ae89`.  They are proposed stack inputs or neighboring results, not
current-source authority.  None contains (17)–(24).

### N7 -- steelman

The strongest hostile response is that any single positive injective transfer
has a spectral logarithm and hence abstract real powers.  That response is
correct and is preserved in (32).  It does not show that those powers have the
exterior-character density at another coupling, compose under one common
channel clock, or correspond to a carrier refinement.  The theorem therefore
rejects only the stronger same-family inference, not spectral calculus.

A second steelman is the determinant-only quotient, where one channel can be
reparameterized.  That escape is also correct; it changes the carrier and is
stated explicitly rather than hidden.

The strongest live constructive response is not another coupling relabeling.
It is a co-scaled family `M_t C_t M_t`, assembled by an exact Trotter or other
composition law together with carrier/measure refinement maps
`J_j:H_j->H_(j+1)`.  Such a family can evade both the bare Fourier mismatch and
the fixed-`M` commutator because `M_t`, the carrier, and the measure all change.
The terminal test is an exact or controlled comparison
`T_(j+1)J_j` versus `J_jT_j`.  No such `J_j`, coefficient scaling, or error
bound is supplied here, so this route remains fully live.

### N8 -- cross-cycle echo and live status

| Prior row | Current status | Retired? | Mechanism and applicability |
|---|---|---:|---|
| `ACTION_FAMILY_CHARACTER_SEMIGROUP_DISCRIMINATOR...2026-07-02` | `bounded_theorem`, audit/effective `unaudited` | no | Fourier/convolution-square test blocks generic Wilson-vs-heat novelty, but not the `O(3)` all-`f_n` component/projected-cycle result |
| `SEMIGROUP_CLOSURE_DOES_NOT_FORCE_HEAT_KERNEL...2026-07-02` | `bounded_theorem`, audit/effective `unaudited` | no | finite-group counterexample blocks any inference semigroup implies heat selection |
| `HEAT_KERNEL_GAUGE_ACTION_NATIVE_RP...2026-07-09` | `bounded_theorem`, audit/effective `unaudited` | no | supplied heat coefficients only; no `O(3)` jump rate or retained premise |
| `GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL...2026-05-10` | `positive_theorem`, audit/effective `unaudited` | no | convolution factorization only |
| `BRIDGE_GAP_HK_TIME_DERIVATION...2026-05-06` | `bounded_theorem`, audit/effective `unaudited` | no | leading `SU(3)` comparator, not finite-coupling authority here |
| `HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL...2026-06-08` | `bounded_theorem`, intrinsic/effective `unaudited` | no | candidate heat-vs-Wilson claim; broad selection prose is not authority and has no all-`f_n` `O(3)` proof |
| `RECORD_COMPOSITION_BRIDGE_SEMIGROUP...2026-07-02` | `bounded_theorem`, intrinsic/effective `unaudited` | no | conditional composition/convolution method context only |
| `RECORD_CLASSICAL_SEMIGROUP_BOUNDARY...2026-06-06` | `bounded_theorem`, intrinsic/effective `unaudited` | no | rates/generators/clocks need suppliers; not a retained premise here |
| branch-local `c36d11e...` nonsemigroup note | `bounded_theorem`, `actual_current_surface_status: bounded-support`, `conditional_surface_status: audited_conditional expected (dependency_not_retained; Blocks 103–115 content-bound unaudited)`; no ledger/audit authority | no retirement mechanism exists on current authority | finite-window mechanism prevents a “first nonsemigroup transfer” claim |

No prior row is imported as retained authority.  The current-source rows remain
unaudited and non-linking.  The new load-bearing content is the exact
all-`f_n` `O(3)` component mismatch together with its projected-cycle lift.

## Runner certificate

The primary SymPy runner derives the exterior/component formulas, the four
linear series, the determinant/vector and higher-spin teeth, the symbolic
Catalan-ratio identity, the character conjugation contraction and linkwise
cycle power, the heat/jump mismatch, the narrow `SO(3)` control, and an exact
fixed-`M` commutator.  The independent checker uses only integers and
`Fraction`, reconstructs the multiplicities and series, enumerates proper and
improper signed-frame conjugations, and independently iterates the cycle
multiplier.  Its finite `n` samples cross-check rather than replace the
all-`n` proof in (18).

Every changed check family has a dedicated hostile mutation.  The normal
runner prints the five required N5 resolution scales.  Neither executable
uses fitted spectra, floating arithmetic, or float-to-exact reconstruction.

## Exact strongest remaining obligation

Supply a genuine indexed refinement family for the complete action:

```text
(H_j,mu_j,P_j,T_j),      J_j:H_j->H_(j+1),
```

with explicit carrier and measure maps, co-scaled spatial and temporal
coefficients, normalization, and an exact composition/comparison statement.
Then test whether `T_(j+1)J_j` agrees with `J_jT_j`, approximates it with a
controlled error, or requires a different effective action.  Without that
supplier, the coupling `kappa` is not a derived time or refinement spacing.

No claim in this note is a framework axiom, primitive, audit verdict, or
authority-state mutation.
