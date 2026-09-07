# The Role-Compiled Edge-Face Incidence Carries a Nearest-Neighbor Maxwell Generator, While the Static Law Leaves a Time-Selection Fork

**Status:** proposed_retained
**Date:** 2026-09-03
**Claim type:** bounded_theorem
**Status authority:** independent audit only. This note changes no audit
verdict, TOE score, axiom, or approved primitive.
**Direct parent:**
[`U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Static-measure parent:**
[`U1_AUXILIARY_FACE_LOCAL_CONDITIONALS_UNCONDITIONAL_GAUGE_MEASURE_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_AUXILIARY_FACE_LOCAL_CONDITIONALS_UNCONDITIONAL_GAUGE_MEASURE_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Kinetic normalization boundary:**
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
**Local-Hamiltonian comparison:**
[`MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md)
**Runner:**
[`scripts/u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03.py`](../scripts/u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03.py)
**Cached receipt:**
[`logs/runner-cache/u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03.txt`](../logs/runner-cache/u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03.txt)

## Result up front

The role compiler's edge and face sites already form the staggered incidence
geometry needed for first-order Maxwell evolution. Let `d_0` be the oriented
vertex-to-edge gradient, `C` the edge-to-face curl, and `d_2` the
face-to-cube divergence. On every periodic doubled cubic complex,

```text
C d_0 = 0,                 d_2 C = 0.
```

Every row of `C` reads four physical edge neighbors of one face site, and
every column meets four physical face neighbors of one edge site. Introduce
electric data `E` at edge-role sites and magnetic data `B` at face-role sites.
The supplied first-order law

```text
dot E = -beta C^T B,
dot B =  alpha C E
```

is therefore a physical nearest-neighbor generator. It conserves

```text
H = (alpha/2)||E||^2 + (beta/2)||B||^2,
```

preserves both Gauss constraints, is proper-cubic covariant, and has at every
nonzero momentum exactly two positive-frequency branches

```text
omega_1(k)=omega_2(k)=sqrt(alpha beta)
                         sqrt(sum_i 4 sin^2(k_i/2)).
```

With reciprocal coefficients

```text
beta=kappa,               alpha=1/kappa,
```

where `kappa>0` is the Record-overlap magnetic curvature, the speed is one in
lattice units. There are no centered-difference doublers. Omitting one face
orientation loses a transverse branch, unequal face stiffness splits the
pair, and a mass term gaps the zero-momentum control.

This is meaningful positive light-lane progress: the parent no longer needs
an abstract two-step `curl^T curl` update to assert that local dynamics can
carry its photon germ. The physical edge-face sites themselves carry a
first-order, norm-preserving, nearest-neighbor Maxwell generator.

It is still a **supplied dynamics**, not a consequence of the static
Admissibility distribution. A reversible Gaussian sampler of the same
mean-zero transverse harmonic measure has quadratic relaxation, while a two-reflection
Szegedy-style spectral lift of that sampler has a linear infrared phase. The
direct Maxwell generator and the spectral lift agree at long wavelength but
differ across the Brillouin zone. The static law therefore leaves a real
time-selection fork: dynamics form, tick normalization, and physical
interpretation still need selection or derivation.

## 1. Physical incidence on the doubled lattice

In one period-two role sector, the four role classes are:

```text
vertex: r=(0,0,0),
edge:   |r|=1,
face:   |r|=2,
cube:   r=(1,1,1).
```

An oriented edge on axis `i` connects the vertex sites one physical step on
either side. A face in plane `i<j` reads the four edge sites

```text
x-e_j, x+e_i, x+e_j, x-e_i
```

with signs `(+,+,-,-)`. A cube reads its six face neighbors with outward
signs. These definitions give the integer incidence sequence

```text
vertices --d_0--> edges --C--> faces --d_2--> cubes.
```

Each matrix entry is `0,+1,-1`. Opposite paths around a square or cube cancel
pairwise, proving

```text
C d_0=0,                  d_2 C=0
```

over the integers, before any weak-field approximation.

On the runner's `L=3` coarse torus the physical lattice has side six and the
role counts are

```text
27 vertices, 81 edges, 81 faces, 27 cubes.
```

The entire `81 x 81` curl is built from physical positions. Every face row
has four entries and every edge column has four entries. The runner verifies
both chain identities exactly and compares matrix curl with an independent
four-neighbor evaluation on a nonuniform field.

## 2. Magnetic action and the first-order local generator

In the quadratic basin, the parent's plaquette action is

```text
S_B(A) = (kappa/2)||C A||^2.
```

Writing `B=C A` turns its Hessian `kappa C^T C` into a first-order incidence
pair. Add an edge electric variable `E` and choose positive coefficients
`alpha,beta`:

```text
dot A =  alpha E,
dot E = -beta C^T B,
B     = C A.
```

Differentiating the constraint gives

```text
dot B = alpha C E.
```

Thus the closed `(E,B)` generator is

```text
G = [[0,       -beta C^T],
     [alpha C,  0       ]].
```

An edge derivative depends only on its four adjacent face sites. A face
derivative depends only on its four adjacent edge sites. `dot A=alpha E` is
onsite. The generator is therefore nearest-neighbor on the physical lattice,
even though eliminating `B` produces the two-incidence operator `C^T C`.

The field energy is

```text
H(E,B)=(alpha/2) E^T E +(beta/2) B^T B.
```

Direct differentiation gives

```text
dot H = -alpha beta E^T C^T B
        +alpha beta B^T C E = 0.
```

After rescaling `E'=sqrt(alpha)E`, `B'=sqrt(beta)B`, the generator is a real
skew matrix with coefficient `sqrt(alpha beta)`. Its exponential is unitary
on the complexified field space and orthogonal on the real field space.

The continuous exponential is not a one-tick radius-one cellular update; it
is evolution generated by a radius-one Hamiltonian. The local-Hamiltonian
comparison linked above makes the same distinction between local generator
support and a finite-time propagator. No sharper causal cone is claimed here.

## 3. Gauss constraints are preserved

Define the electric and magnetic constraint rows

```text
rho_E=d_0^T E,            rho_B=d_2 B.
```

Then

```text
dot rho_E = -beta d_0^T C^T B
           =-beta (C d_0)^T B=0,

dot rho_B = alpha d_2 C E=0.
```

The source-free sector is invariant under the update. The result is kinematic:
it does not derive a charge dictionary, show how matter sources enter, or
prove the interacting Gauss law on the compact carrier.

## 4. Exact spectrum and the two transverse branches

In the staggered Fourier presentation, rephase each component so the forward
difference symbol is real:

```text
s_i(k)=2 sin(k_i/2).
```

The curl block is the cross-product matrix

```text
C(k) = [[ 0,   -s_z,  s_y],
        [ s_z,  0,   -s_x],
        [-s_y,  s_x,  0  ]].
```

It obeys

```text
C(k)s=0,
C(k)^T C(k)=|s|^2 I-s s^T.
```

Hence its singular values are `(0,|s|,|s|)`. In energy-normalized variables,
`iG(k)` has spectrum

```text
(-c|s|,-c|s|,0,0,+c|s|,+c|s|),
c=sqrt(alpha beta).
```

At nonzero momentum the two zero rows are longitudinal electric and magnetic
directions; imposing Gauss leaves two positive-frequency polarizations.
At zero momentum the whole generator vanishes and harmonic fields survive
Gauss. Because
`|s|` vanishes only when every `k_i=0 mod 2pi`, there is no Nyquist doubler.

The runner checks every momentum on `L=3,4,5,7`, `559` blocks in all and 555
nonzero blocks. It separately diagonalizes the complete real-space curl on
the `L=3` torus and obtains the same singular-value multiset. Through
`L=16,32,64,128,256`, the ratio of the first-axis frequency to continuum
momentum converges monotonically to one.

## 5. The coefficient interface

The Record-overlap chain supplies `kappa>0` for the magnetic germ. The
canonical quadratic Hamiltonian family is

```text
H(A,E)=(alpha/2)||E||^2+(beta/2)||C A||^2.
```

Its wave speed is `sqrt(alpha beta)`. Choosing

```text
beta=kappa,               alpha=1/kappa
```

gives unit speed and keeps the coupling in reciprocal electric/magnetic
normalizations. This is the standard transfer/Hamiltonian relation, but it is
declared here rather than attributed to the static probability law.

The approved kinetic-isotropy primitive supplies equal matter kinetic form.
It does not identify the independent gauge coefficient product `alpha beta`
with that matter kinetic block. The reciprocal gauge normalization above is
therefore supplied; deriving a shared matter/gauge kinetic normalization is
open even after selecting this conservative family. The primitive also does
not select this generator, create `E`, or derive its transfer interpretation.

## 6. Proper cubic covariance and controls

For a proper signed-permutation matrix `R`,

```text
C(Rs)=R C(s) R^T.
```

The runner checks this identity on three generic momentum vectors under all
24 proper rotations. Since edge and face role labels transform with the same
orientation rules in the direct parent, the real-space generator is covariant
as well.

Three controls expose the ingredients:

- removing the `yz` face component at momentum `(0,1,1)` lowers curl rank
  from two to one and removes a transverse branch;
- weighting the three face orientations unequally splits the two nonzero
  eigenvalues at a generic momentum; and
- adding `m^2 I` gives a nonzero zero-momentum frequency.

Thus twofold transverse degeneracy, cubic isotropy, and gaplessness are not
artifacts of counting six variables.

## 7. The static-law time fork

The same harmonic spatial probability law does not determine the equations
above. On the finite periodic lattice, restrict to the mean-zero transverse
space `H = {A: d_0^T A=0, sum_x A_i(x)=0 for each i}`. This removes both
gradient directions and the three constant harmonic one-forms. The latter
survive the gauge quotient and would give zero stiffness and unconfined real
OU noise. On `H`, `C^T C` is positive definite and the normalized Gaussian is

```text
pi(A) proportional to exp[-(kappa/2) A^T C^T C A].
```

One compatible reversible gradient sampler is the Ornstein-Uhlenbeck law

```text
dA = -(1/4) C^T C A dt + sqrt(1/(2 kappa)) P_H dW,
A(0) in H,
```

where `P_H` is the orthogonal projector onto that space. For a nonzero
transverse mode its relaxation rate and stationary variance are

```text
rho(k)=|s|^2/4,
Var(A_k)=1/(kappa |s|^2).
```

The rate is quadratic at small momentum: this is diffusion, not light. The
runner verifies the three harmonic zero modes, their removal by the
projector, the variance identity at four nonzero curvatures, and the quadratic
infrared scaling. No normalized real stationary Gaussian is claimed on the
unrestricted gauge quotient. This comparison is consistent with rigorous work
on heat-bath dynamics of lattice Gaussian fields, where the stationary field
and its diffusive dynamics are separate objects.

This Ornstein-Uhlenbeck process is a supplied collapsed harmonic sampler. It
is not asserted to be the exact finite auxiliary heat-bath chain of the static
parent. Its role is to give an explicit reversible time law with the same
quadratic stationary measure and different infrared dynamics.

A different mathematical lift takes the reversible semigroup eigenvalue

```text
lambda(k)=exp[-tau rho(k)]
```

and forms the two-reflection block

```text
W_lambda = [[2lambda^2-1, -2lambda sqrt(1-lambda^2)],
            [2lambda sqrt(1-lambda^2), 2lambda^2-1]].
```

It is unitary and has eigenphases

```text
Omega_+/- = +/- 2 arccos(lambda).
```

For `tau=1/2`,

```text
Omega(k)=|s|+O(|s|^3),
```

again giving two unit-speed transverse infrared branches. This is the
spectral square-root behavior of Szegedy quantization. The runner constructs
every displayed `2x2` block directly; no external result carries the numeric
claim.

The lift is not the direct Maxwell law. It lives on an enlarged walk space,
its coherent transition oracle is not compiled into the site alphabet, and
`tau` changes its speed. Across the Brillouin zone its phase differs from
`|s|`. Using `1-lambda` as phase instead remains quadratic. These controls
show that the square-root spectral map and tick are physical choices.

The direct Yee generator, dissipative sampler, and Szegedy-style lift are
three mathematically compatible uses of the same spatial kernel:

| supplied time rule | infrared behavior | preserves the static measure? |
|---|---|---|
| gradient sampler | relaxation proportional to `k^2` | yes |
| two-reflection spectral lift | phase proportional to `|k|` | coherent stationary encoding |
| edge-face Maxwell generator | frequency proportional to `|k|` | conserves field energy rather than sampling |

Their inequivalence is the exact remaining time-selection issue.

## 8. Literature context, not proof authority

The staggered edge/face placement is the geometry introduced for finite
difference Maxwell evolution by K. S. Yee,
[DOI 10.1109/TAP.1966.1138693](https://doi.org/10.1109/TAP.1966.1138693).
The product-of-reflections spectral map is associated with M. Szegedy,
[arXiv:quant-ph/0401053](https://arxiv.org/abs/quant-ph/0401053). A modern
rigorous example separating a lattice Gaussian field from its heat-bath
dynamics is Ganguly and Gheissari,
[arXiv:2108.07791](https://arxiv.org/abs/2108.07791).

These references identify known mathematical constructions. The repository
claim is narrower and checked from scratch: the role-compiled physical lattice
has exactly the required incidence, the displayed generator has the stated
spectrum and symmetries, and the alternative time maps remain inequivalent.

## 9. TOE consequence and remaining obligations

The light/action route now has a positive end-to-end **linear candidate**:

```text
Record-varying compact distribution
 -> positive magnetic overlap curvature
 -> unconditional local gauge measure
 -> physical nearest-neighbor role compiler
 -> physical nearest-neighbor first-order Maxwell generator
 -> two unit-speed transverse gapless branches.
```

The last arrow is new. It removes “no physical-local photon dynamics has been
exhibited” as an existence concern for the weak-field candidate. It does not
retire the stronger derivation obligation because the generator is supplied.

The remaining light-lane priority stack is now:

1. select or derive the time rule, rather than merely exhibit it;
2. compile the enlarged `(A,E)` edge and `(B,h)` face payloads into the chosen
   one-site or spatial-composite possibility implementation;
3. connect Record formation and experimental sampling to the unrecorded field
   evolution;
4. control compact nonlinear interactions and the simultaneous continuum and
   thermodynamic limits; and
5. derive the electromagnetic dictionary and coupling to the matter carrier.

The direct generator is sufficiently explicit that the next decision is no
longer “can local Maxwell dynamics fit?” It is “what framework principle
selects this conservative first-order law over the equally compatible
dissipative and quantum-walk alternatives?” If no existing premise answers
that question, it is a candidate law choice or a narrowly identified axiom/
primitive issue.

## 10. Executable evidence

The runner reports `TOTAL: PASS=31 FAIL=0`. It checks:

- the full integer `d_0,C,d_2` complex on the `L=3` coarse / side-six physical
  torus;
- every row and column locality count, both nilpotent compositions, and an
  independent nonuniform field curl;
- equality of magnetic quadratic action and squared incidence curl;
- the entire real-space singular spectrum;
- skew/unitary evolution, canonical Hamiltonian conservation, reciprocal
  normalization, and both Gauss constraints;
- every Fourier momentum on `L=3,4,5,7`, both transverse modes, no doublers,
  and five infrared refinements;
- all 24 proper cubic rotations and the missing-orientation, anisotropy, and
  mass controls;
- diffusive sampler scaling and stationary variance; and
- unitary two-reflection blocks, their phases, tick dependence, direct-phase
  control, and whole-zone inequivalence.

## No-Go Discipline Gate

This positive theorem includes three bounded negative statements: the static
measure does not select among the displayed inequivalent time rules; deleting
one face orientation removes a branch in the named block; and the mode-level
Szegedy lift is not yet a physical site compiler. The gate below applies only
to those statements.

### N1 — Alternative routes and same-cycle evidence

These attempts were checked analytically or by the paired runners in this
47-path review unit. Positive and partial constructions remain positive or
partial; none is recast as a failed route to satisfy a count. Named check
labels, rather than old ordinal numbers, identify the evidence. Cross-note
comparisons below are scope tests, not extra premises of this note.

| Route | Actual attempt and evidence | Result within the stated scope |
|---|---|---|
| Electric rotor completion | **ATTEMPTED:** Use the supplied harmonic Hamiltonian and its reciprocal coefficient example (§5 and weighted-energy checks). | A conservative candidate exists, with its speed normalization supplied. |
| Physical edge-face generator | **ATTEMPTED:** Assemble the physical curl, gradient and divergence (§§1–4 and exact incidence checks). | The nearest-neighbor generator preserves both Gauss rows. |
| Reversible gradient sampler | **ATTEMPTED:** Construct the projected Gaussian OU law on nonzero transverse modes (§7 and harmonic/variance checks). | The same restricted static law admits diffusive relaxation. |
| Two-reflection spectral lift | **ATTEMPTED:** Construct the two-dimensional reflection product for each sampler eigenvalue (§7 and phase/unitarity checks). | A linear infrared phase exists at mode level; a physical local oracle is open. |
| Euclidean transfer reconstruction | **ATTEMPTED:** Compare the supplied reflection-positive Wilson transfer denominator with continuous time (Wilson §6 and transfer-dispersion controls). | The finite-lattice phases differ despite a matched infrared cone. |
| Finite-depth shear tick | **ATTEMPTED:** Replay the separate leapfrog construction in this unit (paired leapfrog inverse/metric/radius checks). | It is a positive local reversible alternative with a modified metric and a supplied step. |

Record-formation fronts and a microscopic physical-time selector remain
open. These examples establish a time-selection fork, not an exhaustive
classification of every dynamics compatible with the static measure.

### N2 — Pairwise status of the remaining tasks

The following are named inputs or open tasks, not a proved minimum number
of independent walls. Their names alone establish no logical implications.
The table explicitly records every pair; `unresolved` means that a closure
theorem or countermodel in both directions has not been established here.
No dependency collapse is justified by this analysis, and no independent-wall
count is claimed. The conditional theorem still requires all its stated
hypotheses.

- W1: physical time-rule selection.
- W2: tick/space normalization beyond structural isotropy.
- W3: enlarged payload and internal/composite compiler.
- W4: Record formation and sampling bridge.
- W5: compact interacting and simultaneous-limit control.
- W6: electromagnetic and matter-coupling dictionary.

| Pair | First closure implies second? | Second closure implies first? | Independence established? |
|---|---|---|---|
| W1, W2 | unresolved | unresolved | no |
| W1, W3 | unresolved | unresolved | no |
| W1, W4 | unresolved | unresolved | no |
| W1, W5 | unresolved | unresolved | no |
| W1, W6 | unresolved | unresolved | no |
| W2, W3 | unresolved | unresolved | no |
| W2, W4 | unresolved | unresolved | no |
| W2, W5 | unresolved | unresolved | no |
| W2, W6 | unresolved | unresolved | no |
| W3, W4 | unresolved | unresolved | no |
| W3, W5 | unresolved | unresolved | no |
| W3, W6 | unresolved | unresolved | no |
| W4, W5 | unresolved | unresolved | no |
| W4, W6 | unresolved | unresolved | no |
| W5, W6 | unresolved | unresolved | no |

The examples elsewhere in this note establish only their displayed positive
or negative cases. In particular, the leapfrog example changes both complete
map radius and energy metric; that single example does not establish those
restrictions’ independence. The strict radius-one sibling retains its own
explicit domain-relaxation table.

### N3 — Hidden-wall scan

“Supplied” marks `E`, `B`, the first-order generator, reciprocal coefficients,
the Gaussian sampler, its semigroup time, and the spectral lift. “Unitary” is
the exponential of the finite skew generator, not a claim that permanent
Records update unitarily. The Gaussian comparison removes both gauge modes
and the three harmonic one-forms, restricts the initial field to the mean-zero
transverse sector, and projects the noise there. The face magnetic payload
`B` is additional to the parent's auxiliary `h`; no claim says the old face
alphabet already contained a readable `B` slot.

### N4 — Residual matching

| Surface | Residual | Match here |
|---|---|---|
| direct role parent | physical dynamics absent | **exact existence match:** one nearest-neighbor conservative generator |
| static measure parent | electric/time law and relative normalization supplied | **partial:** explicit reciprocal family and unit-speed candidate, selection open |
| kinetic-isotropy primitive | equal matter kinetic form only | **no closure:** the gauge/matter kinetic identification and gauge normalization remain open or supplied |
| local-Hamiltonian comparison | local generator support does not equal finite-time locality | **exact boundary match:** same distinction retained |
| historical PR #7903 | finite compact matter/gauge join has no computed photon | **partial future join:** this weak-field photon is not its finite interacting spectrum |
| historical PR #7911 | spin-half ring is gapped and one-dimensional | **no conflict:** this theorem uses three spatial dimensions and a weak-field continuous payload |

Dropping the two historical-PR pointers changes no proof.

### N5 — Rhetoric and resolution audit

“Two photons” is not used; the theorem says two transverse branches of one
linear source-free field. “No doublers” refers only to zeros of the declared
forward-incidence symbol. “Static law does not select time” is witnessed by
three explicit inequivalent time maps, not promoted to a universal theorem
about every possible consistency principle.

The cached output carries:

```text
per_element: every physical incidence coefficient and each declared two-reflection spectral block is checked
per_site: every edge couples to four face neighbors and every face to four edge neighbors on the L3 block
per_mode: every momentum on L=3,4,5,7 has two Yee branches; five infrared refinements test both time lifts
per_block: gradient-curl-divergence complexes, Hamiltonian conservation, cubic covariance, and controls are checked
lattice_wide: the full 162-variable L3 edge-face generator and all 24 cubic rotations are executed
```

### N6 — Partial-closure paths and primitive check

The current approved primitive registry was reread. Kinetic isotropy supplies
the matter equality `c_t=c_s`; no theorem here identifies that block with the
gauge coefficient product. Gauge normalization and time selection remain
supplied. Scale reference fixes units only; realized-state evaluation supplies
no evolution.

Live positive paths are concrete:

- derive the conservative generator as the unique reversible norm-preserving
  first-order incidence law under a stated minimal consistency class;
- compile an exact local leapfrog/trotter tick and test its cone and zone
  spectrum;
- realize the Szegedy transition oracle on the role-encoded site alphabet;
- add compact nonlinear constitutive terms and test whether the two branches
  remain gapless in three dimensions; or
- couple the edge electric Gauss row to the independent fermion charge
  carrier without importing a continuum photon.

### N7 — Steelman

A hostile reviewer can say this is merely the known Yee discretization. The
matrix spectrum is indeed standard. The framework-specific advance is not a
new numerical method: the previously abstract role compiler independently
places exactly the required edge and face payload sites at physical nearest-
neighbor distance, and the Record-derived magnetic curvature supplies the
positive spatial term. The result closes an internal existence/locality gap,
not a historical Maxwell-theory gap.

The same reviewer can say a supplied generator is no derivation. That is
correct. The theorem moves the question from existence to selection and
exhibits why the distinction matters: another compatible time rule is
diffusive, and a third has the same infrared phase but different zone physics.

### N8 — Cross-cycle echo

The local-Hamiltonian comparison already warns that a supplied nearest-
neighbor Hamiltonian yields support control without becoming axiom-selected
dynamics. The kinetic-isotropy source makes the complementary warning that
equal kinetic form is not a dynamics selector. Both echoes are preserved.
The current theorem adds the explicit light-sector generator and the
three-way time discriminator.

**Gate result:** PASS for the three scoped boundaries. The listed routes were
separated, three were executed in the same harmonic kernel, the missing-face
control was corrected and rerun, and the stronger selection/compiler routes
remain open.

## Falsifiers

The bounded theorem fails if any of the following occurs:

- `C d_0` or `d_2 C` is nonzero on the displayed physical complex;
- an edge-face generator entry connects non-neighboring physical sites;
- the field energy or either Gauss constraint changes under the generator;
- a nonzero momentum has other than two positive transverse branches;
- the forward-incidence symbol has a nonzero-momentum zero;
- a proper cubic rotation changes the generator spectrum or incidence law;
- reciprocal coefficients fail to give speed one;
- the projected Gaussian sampler fails to have the stated variance on the
  mean-zero transverse sector;
- its relaxation is not quadratic at small momentum;
- the displayed two-reflection block is not unitary or lacks phase
  `2 arccos lambda`; or
- the direct and spectral-lift candidates coincide across the full zone after
  their infrared speeds are matched.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=31 FAIL=0
```

## Source status and trace

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "A selected framework-derived electromagnetic law and physical field/readout bridge remain open; the eventual physical consumer is not yet established."
source_of_blocker_text: "review_loop"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Use the conditional result with its stated inputs; establish the missing physical consumer and selection bridge before claiming framework closure."
conditional_surface_status: "Supplied linear edge-face dynamics and coefficient normalization; Gaussian comparison is restricted to the mean-zero transverse sector with projected noise."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The written derivation establishes only the declared conditional mathematical claim; finite checks and source review grant no retained status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Review correction — 2026-09-07

The original September 2–3 source and receipts are preserved at raw commit
`2814c6768e4d7b38048f70ad7883b4951cb12da3`. This revision supplies current
source status, explicit timeout/input-bound evidence and written boundary
checks. The conditional scope is stated in the status record above.
Independent source confirmation and current-main integration validation are
separate; no audit verdict or effective retained status is asserted.
