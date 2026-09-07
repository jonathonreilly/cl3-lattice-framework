# A Local Record Face Likelihood Supplies a Spatial Gauge and Photon Germ

**Status:** proposed_retained
**Date:** 2026-09-03
**Claim type:** bounded_theorem
**Status authority:** independent audit only. This source note sets no audit
verdict, changes no TOE score, and claims no obligation retirement.
**Direct parent:**
[`U1_RECORD_DISTRIBUTION_OVERLAP_POSITIVE_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md`](U1_RECORD_DISTRIBUTION_OVERLAP_POSITIVE_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md)
**Current axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
**Runner:**
[`scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py`](../scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py)
**Cached receipt:**
[`logs/runner-cache/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.txt`](../logs/runner-cache/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.txt)

## Claim scope

This note constructs and separates three layers.

First, use the doubled-cell incidence pattern inside the physical cubic
lattice. Relative to any translated parity origin, fine sites with zero, one,
two, or three odd coordinates play coarse vertex, edge, face, or cube roles.
Every face-role site's six nearest neighbors are exactly four edge-role sites
on the boundary of one coarse plaquette and two cube-role sites normal to it.
The face sites form an independent set. Consequently one fixed local face rule
can take the four compact link possibilities as its conditions without a
`5 x 5 x 5` window. The role pattern and the compact `U(1)` link coordinate
remain supplied; this is an incidence and locality theorem, not their genesis.

Second, let the parent's nonuniform Record distribution have overlap `C` and

```text
q(delta) = C(delta)/C(0),
V(delta) = -log q(delta).
```

By the parent, `0 <= q <= 1`, `q(0)=1`, and
`V''(0)=kappa>0`. Supply at each face role a binary **overlap-success Record**
whose success probability, conditional on its four link neighbors, is

```text
Pr(success_f | links) = q(Phi_f),
Phi_f = oriented compact sum around the face.
```

Under a supplied sequentially local face sweep with the link conditions held
fixed and no shared latent draw between faces, the likelihood of the readable
event `R_all` that every face registers success is

```text
Pr(R_all | links)
  = product_f q(Phi_f)
  = exp[-sum_f V(Phi_f)].
```

This is an exact local **Record likelihood action**. With a supplied prior on
the link possibilities, ordinary conditioning gives the corresponding
compact-gauge posterior. On the finite `Z_4` realization in the runner, a
uniform prior gives an exact nonuniform gauge-invariant plaquette ensemble,
and a symmetric single-link Metropolis sampler obeys detailed balance on all
`1,048,576` directed moves and Kolmogorov's criterion on all `6,144`
elementary two-link cycles.

Third, the same even face rule on all three spatial orientations gives the
quadratic magnetic kernel

```text
K_ij(k) = kappa [P delta_ij - q_i q_j],
P = sum_i q_i^2,
q_i = 2 sin(k_i/2).
```

At every nonzero spatial momentum its spectrum is
`{0,kappa P,kappa P}`: one gauge direction and two positive transverse curl
directions. If one additionally supplies an untruncated compact-rotor electric
term `alpha E^2/2`, `alpha>0`, and canonical quantization about the flat
connection, those directions are two harmonic oscillators with

```text
omega_1^2(k) = omega_2^2(k) = alpha kappa P.
```

They are degenerate, transverse, and gapless with linear dispersion as
`k -> 0`. This is a **quadratic quantum photon germ**, not a proof of the full
compact interacting photon. It does not establish a nonperturbative Coulomb
phase, monopole suppression, an electromagnetic dictionary, a physical
formation process, or the value of `alpha kappa`.

The exact negative control matters. Summing over success and failure at every
unread face gives `q+(1-q)=1` and restores the prior link marginal. Local
sitewise probabilities also admit correlated joint laws with the same
marginals. Therefore the four axioms' per-site distribution clause alone does
not select the product sweep, the all-success event, the posterior reading, or
a physical update dynamics. The theorem supplies a concrete axiom-compatible
law candidate and realizes the parent's **construction target** at that bounded
scope; it does not derive that candidate from the unspecified law.

## 1. The face is already a nearest-neighbor star

Fix a parity origin `o in (Z/2Z)^3`. For a fine-lattice site `x`, define

```text
d_o(x) = number of odd coordinates of x-o.
```

The four roles `d=0,1,2,3` are the vertices, edges, faces, and cubes of the
coarse cubic cell complex. A unit step toggles exactly one parity bit. Hence a
site of role `d` has `d` neighbors of role `d-1` and `3-d` neighbors of role
`d+1` in each sign direction. In particular,

```text
face star:  4 edge neighbors + 2 cube neighbors,
edge star:  2 vertex neighbors + 4 face neighbors.
```

No face site is adjacent to another face site. These statements hold for all
eight translated parity origins. They use only nearest-neighbor adjacency on
the fine `Z^3` lattice.

For a coarse face based at `X` in axes `mu<nu`, its center is
`2X+e_mu+e_nu`. Its four edge neighbors carry

```text
Phi_mu_nu(X)
 = ell_mu(X) + ell_nu(X+e_mu)
 - ell_mu(X+e_nu) - ell_nu(X)       mod 2 pi.
```

Changing the arbitrary face orientation sends `Phi -> -Phi`. The overlap
kernel is even, so `q(Phi)` is unchanged. Applying the same rule at every face
role is invariant under translations and all 24 proper cubic rotations. The
runner checks the incidence census for all eight parity origins and the action
of all 24 rotations on five deterministic three-dimensional link fields.

This proves locality of the **face evaluation**. It does not prove that the
role pattern forms, or that a single physical site carries the full compact
link and face vocabulary. A larger composite realization is permitted by the
construction but is not written here.

## 2. Record overlap becomes a local likelihood

The parent proves for every nonuniform normalized nonnegative
`p in H^2(U(1))` that

```text
C(delta) = integral p(theta)p(theta+delta)dtheta/(2 pi)
```

is even, identity-maximal, and has a strictly positive negative-log
curvature. Thus `q=C/C(0)` is a valid probability in `[0,1]`. This note makes
one explicit supplier choice: it uses `q(Phi_f)` as the success probability of
a forming binary Record at the face site whose nearest-neighbor star contains
the four links of `Phi_f`.

The finite exact realization uses the cyclic Record histogram

```text
p = (8,4,2,1)/15 on Z_4.
```

Counting matching pairs after a cyclic shift gives

```text
C_num = (85,50,40,50),       C = C_num/225.
```

The runner derives these four integers by enumerating the Record pairs. The
kernel is positive, even, nonconstant, and maximal at zero. Using `C` itself
as the match probability rather than `q` changes every `F`-face likelihood by
the same constant `C(0)^F`; the normalized action remains
`sum_f -log[C(Phi_f)/C(0)]`.

The continuous theorem and the finite check have different jobs. The parent
proves the positive `U(1)` germ for the whole stated `H^2` class. The `Z_4`
model makes the joint probability, posterior, gauge symmetry, and reversible
law exhaustively checkable with integer arithmetic.

## 3. Why the face product is exact, and what is supplied

Enumerate the face sites in any order. Hold every edge and cube condition
fixed during the sweep. In the supplied sequentially local realization, the
conditional probability at the next face is `q(Phi_f)` and contains no shared
latent draw. Since no earlier face Record is a nearest neighbor of a later face
site, the face conditions do not change during the sweep. The probability
chain rule therefore gives

```text
Pr(R_all | ell)
 = product_f Pr(success_f | earlier successes, ell)
 = product_f q(Phi_f).
```

Every ordering gives the same result. The runner checks all `4!` orders for
every one of the `4^8=65,536` link configurations on the `2 x 2` periodic
`Z_4` lattice.

The no-shared-latent clause is real. Equal per-face marginals do not determine
a joint distribution. For two faces with success marginal `r=2/9`, both

```text
Pr(11)=r^2                         (product law)
```

and

```text
Pr(11)=r, Pr(10)=Pr(01)=0,
Pr(00)=1-r                        (perfectly correlated law)
```

have the same marginals. The runner checks the two couplings exactly. Thus
the product sweep is an explicit compatible realization, not something
silently inferred from the sitewise distributions.

## 4. Posterior gauge action and the odds-as-energy tests

Let `pi_0(ell)` be any supplied prior on finite link configurations. After the
all-success Record event,

```text
pi(ell | R_all)
 = pi_0(ell) exp[-S(ell)] / Z,
S(ell) = sum_f V(Phi_f).
```

For the runner's uniform prior this is the exact compact `Z_4` plaquette
ensemble. Its weight is the integer

```text
W(ell) = product_f C_num(Phi_f),
```

with constants absorbed into `Z`. Gauge transformations
`ell_xy -> ell_xy + lambda_y-lambda_x` leave every `Phi_f` and `W` fixed.
Translations and proper cubic rotations permute the face factors. The runner
checks every local gauge generator and both translations on all `65,536`
configurations, plus the 24 three-dimensional rotations described above.

There is also an exact compatibility witness for treating the odds as an
energy. Propose `ell_e -> ell_e +- 1 mod 4` with a symmetric proposal and
accept with

```text
A(ell,ell') = min[1,W(ell')/W(ell)].
```

Only faces incident on `e` change. For every directed move,

```text
W(ell) A(ell,ell')
 = min[W(ell),W(ell')]
 = W(ell') A(ell',ell),

A(ell,ell')/A(ell',ell)
 = W(ell')/W(ell)
 = exp[-S(ell')+S(ell)].
```

Detailed balance and every Kolmogorov cycle then follow by telescoping. The
runner checks all `1,048,576` directed moves on the `2 x 2` ensemble and all
`6,144` elementary two-link cycles of the one-face model exactly. A declared
two-to-one phase-direction bias fails on the length-four winding cycle by a
factor `16`, so the cycle test is sensitive to a driven mutation.

This Metropolis law is a **compatibility witness and sampler**. Its acceptance
calculation queries the links around the incident coarse plaquettes; the note
does not compile that query into one fine site's nearest-neighbor condition.
Record permanence also means it is not automatically a physical law that
changes existing Records. A physical reading needs fresh sites, an explicit
pre-Record possibility evolution, a local message carrier, or another
formation construction. The historical PR #7901 supplies complementary rank and
cycle diagnostics on a different classical record-shift model; it is a
context pointer, not authority used here.

## 5. Spatial magnetic completion

The parent left local spatial face ownership open. The incidence theorem and
face likelihood above now provide one explicit realization. Because one even
function `V` is used on every unordered spatial face, its flat-connection
Hessian is

```text
K_ij = kappa(P delta_ij-q_i q_j).
```

At `q != 0`, `Kq=0` and the other two eigenvalues are both `kappa P>0`.
The runner checks every nonzero momentum on `L=3,4,5,7`. Omitting one face
orientation leaves only one positive direction at a displayed momentum;
unequal orientation coefficients split the two transverse eigenvalues. These
controls show that the full proper-cubic orbit of faces, not one preferred
face, carries the magnetic statement.

This constructively realizes a sharply bounded item from the parent's route map:

```text
local face Record rule with overlap likelihood
 -> positive isotropic spatial/magnetic germ       constructed here
```

It does not close the stronger statement that the unspecified framework law
selects this face rule, nor does a three-dimensional magnetic functional alone
give real-time propagation.

## 6. The quadratic quantum photon test

Supply an untruncated compact rotor pair `(ell_e,E_e)` and expand around the
flat connection. On the Gauss-reduced transverse space, take

```text
H_2(k)
 = alpha E_T(k)^dagger E_T(k)/2
 + A_T(k)^dagger K(k) A_T(k)/2,
alpha>0.
```

Hamilton's equations give

```text
dot A_T = alpha E_T,
dot E_T = -K A_T,
ddot A_T = -alpha K A_T.
```

Canonical quantization turns each positive normal direction into a harmonic
oscillator. Since the two positive eigenvalues of `K` coincide,

```text
omega_1^2 = omega_2^2 = alpha kappa P.
```

For the smallest nonzero momentum on an `L^3` torus,
`sqrt(P)=2 sin(pi/L)`, so both frequencies vanish as `2 pi/L` with a common
linear slope `sqrt(alpha kappa)`. The runner checks the full momentum spectra
and the infrared sequence `L=16,32,64,128`.

This answers the harmonic precursor to the photon question left open by the
recent compact-link work: once a positive electric rotor term and this magnetic
germ are present, the untruncated weak-field theory has exactly two gapless
quantum transverse oscillators. It does **not** answer the stronger question posed by open PR
#7903 for its finite `S=1,2` interacting matter-link blocks. That model's
truncation, strong-field sectors, thermodynamic limit, and matter dressing are
not used here.

The coefficient `alpha kappa` fixes the squared propagation speed in lattice
units. The approved kinetic-isotropy primitive fixes structural kinetic-form
graining `c_t=c_s`; it does not select the gauge Hamiltonian or the value of
`alpha kappa`. No such selection is claimed.

## 7. What the construction establishes and what it does not

The positive result is stronger than a formal relabeling of the parent:

1. the spatial plaquette is one physical nearest-neighbor star in the doubled
   incidence pattern;
2. the overlap is the probability of a specific readable local Record event;
3. a supplied local face sweep gives the global plaquette likelihood by the
   probability chain rule;
4. the conditioned finite ensemble is gauge invariant and has an exact
   reversible single-link sampler; and
5. the orientation-complete positive germ plus an electric rotor has two
   gapless transverse quantum oscillators.

The construction still carries explicit inputs:

- **carrier/role:** the doubled role pattern and compact link coordinate;
- **law selection:** the choice `Pr(success|Phi)=C(Phi)/C(0)`;
- **joint realization:** the sequentially local no-shared-latent face sweep;
- **conditioning:** use of the readable all-success event to obtain the
  posterior gauge ensemble;
- **dynamics:** the electric rotor term and canonical weak-field evolution;
  and
- **dictionary/control:** identification with electromagnetism and control of
  the interacting compact continuum.

Marginalizing every face outcome proves the exact normalization identity

```text
sum_(success,failure) Pr(outcome_f|Phi_f)=1.
```

Therefore an unread or discarded face layer leaves `pi_0(ell)` unchanged. The
action survives as the likelihood of persisting Record content, or through a
later feedback/formation mechanism; it is not generated by forgetting the
Records. This is the exact decision produced by the campaign.

No axiom text is amended. The theorem identifies a candidate law permitted by
the axioms and the exact additional choices it uses.

## 8. Executable evidence

The runner reports `TOTAL: PASS=24 FAIL=0`. It verifies:

- all doubled-lattice face and edge stars for every translated parity origin;
- the exact identification of every coarse plaquette boundary with the four
  edge neighbors of its fine-lattice face site;
- the exact `Z_4` Record-pair overlap census;
- all-success likelihood/action equality and all `4!` face orders on every
  `2 x 2` link configuration;
- the unread-outcome normalization and the correlated-joint counterexample;
- gauge and translation invariance on all `65,536` configurations;
- exact detailed balance on all `1,048,576` directed moves;
- all `6,144` elementary two-link cycles and a winding-drive mutation;
- all 24 proper cubic rotations on five deterministic three-dimensional
  fields;
- every nonzero momentum on `L=3,4,5,7` for the magnetic and oscillator
  spectra; and
- missing-orientation and unequal-orientation controls.

The incidence, probability-chain, gauge-invariance, detailed-balance,
cycle-telescoping, Hessian-spectrum, and harmonic-frequency equations prove
the general statements in their declared domains. The finite enumerations are
exact falsification suites, not extrapolations beyond those domains.

## No-Go Discipline Gate

This positive theorem contains two narrowed negative boundaries: sitewise
marginals alone do not select the product face law, and summing over an unread
binary face layer does not reweight the link prior. The gate below stress-tests
only those statements and the scope exclusions; it asserts no permanent
impossibility.

### N1 — Alternative route enumeration

The route families are normalized by their mathematical object, mechanism,
and terminal obligation.

| Family | Object / mechanism / terminal obligation | Marker and outcome |
|---|---|---|
| `face_likelihood` | Binary face Records / overlap-success probability / obtain the plaquette product as a readable likelihood. | **ATTEMPTED:** positive; the chain rule gives the action under the supplied local sweep. |
| `posterior_measure` | Finite link ensemble / Bayes conditioning / obtain a normalized gauge distribution. | **ATTEMPTED:** positive; all `65,536` weights are positive and gauge invariant. |
| `reversible_update` | Single-link Markov chain / Metropolis ratio and cycle telescoping / exhibit globally compatible energy odds. | **ATTEMPTED:** positive; all directed moves and elementary cycles pass exactly. |
| `unread_marginal` | Binary face layer / sum over both outcomes / induce an unconditional link action. | **ATTEMPTED:** fails constructively because each local sum is exactly one. |
| `correlated_coupling` | Two-face joint table / vary the copula at fixed marginals / test whether local marginals force factorization. | **ATTEMPTED:** fails constructively; product and perfectly correlated tables have the same `2/9` marginals. |
| `spatial_orbit` | Three face orientations / proper-cubic orbit and curl Hessian / obtain both magnetic transverse directions. | **ATTEMPTED:** positive; all rotations and momenta pass, while a missing orientation loses one direction. |
| `electric_extension` | Harmonic rotor phase space / Gauss reduction and canonical quantization / obtain a photon germ. | **ATTEMPTED:** positive at quadratic untruncated scope; two linear gapless branches result. |

The two failed routes are not promoted to a general no-go. Feedback from
retained Records, a nonbinary auxiliary field, a different joint formation
law, or a direct Gibbs specification remain live constructions.

### N2 — Pairwise status of the remaining tasks

The following are named inputs or open tasks, not a proved minimum number
of independent walls. Their names alone establish no logical implications.
The table explicitly records every pair; `unresolved` means that a closure
theorem or countermodel in both directions has not been established here.
No dependency collapse is justified by this analysis, and no independent-wall
count is claimed. The conditional theorem still requires all its stated
hypotheses.

- W1: microscopic compact carrier and role realization.
- W2: selection of the overlap-success distribution form.
- W3: physical joint formation/conditioning realization.
- W4: electric/time dynamics and its relative normalization.
- W5: electromagnetic dictionary.
- W6: interacting compact and infinite-volume control.

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

The table withdraws the earlier blanket independence assertion; no
conditional hypothesis is removed. Concrete examples elsewhere in this note
apply only to the relationships they test. Charged-matter completion remains
outside this source-free claim.

### N3 — Hidden-wall scan

The note uses “supply” or “supplied” for the role pattern, compact coordinate,
prior, local sweep, electric term, and canonical quantization; every occurrence
is an explicit condition. “Record” is axiom vocabulary and does not imply a
joint formation process. The flat connection is the expansion point, not an
assumed selected vacuum. No phrase “as is standard,” “the framework provides,”
or “obviously” carries a proof step. The compact rotor, face role, product
sweep, conditioning event, and dynamics are therefore visible rather than
hidden.

### N4 — Residual matching

| Cited surface | Its residual | Residual treated here | Match and use |
|---|---|---|---|
| `U1_RECORD_DISTRIBUTION_OVERLAP_POSITIVE_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md`, lines 295-323 | local spatial face ownership of the overlap | construct that face likelihood and its spatial orbit | **yes**, direct parent target |
| `MINIMAL_AXIOMS_2026-06-29.md`, lines 109-124 and 180-204 | no dynamics or concrete formation rule in the axiom content | keep the face sweep and electric evolution supplied | **yes**, boundary only |
| historical PR #7901 | rank and cycle tests on stipulated record-shift chains | exact energy ratio and cycles on a different gauge chain | **partial**; context pointer, not witness authority |
| historical PR #7903 | no photon computed in finite truncated interacting blocks | untruncated weak-field harmonic photon germ | **no** at full residual; explicitly not claimed to close #7903's finite interacting question |
| `G3_CROSS_EDGE_INDEPENDENCE_IS_A_FORMATION_GATE_ATOM_MARGINAL_IDENTITY_FROM_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md`, lines 1-35 | equal marginals do not select product coupling | two face marginals admit product and correlated couplings | **yes** in mathematical shape, used only as prior-warning context |

Dropping the two nonmatching historical-PR pointers changes no proof. No audit grade
or retained status is imported from any row.

### N5 — Rhetoric and resolution audit

“Marginalizing the unread binary face layer does not generate the plaquette
action” is proved per face and lattice-wide for the declared factorized layer.
It is not phrased as a no-go for feedback, auxiliary fields, or nonbinary laws.
“Sitewise marginals do not select the product joint” is an exact two-face
counterexample and establishes nonuniqueness, not failure of every joint law.
“The quadratic germ is not the full compact interacting photon” is a scope
comparison: no strong-field or thermodynamic calculation was executed.

The cached stdout carries the required five-resolution certificate:

```text
per_element: all cyclic Record pairs, local moves, and proper cubic rotations are checked
per_site: every translated doubled-lattice role has the required six-neighbour incidence star
per_mode: every nonzero spatial momentum on L=3,4,5,7 has two harmonic oscillator branches
per_block: product, correlated, marginalized, reversible, driven, incomplete, and anisotropic controls are contrasted
lattice_wide: all 65536 Z4 configurations and 1048576 directed local moves are checked exactly
```

### N6 — Partial-closure paths and primitive check

The current primitive registry and all three source notes were reread. The
scale-reference primitive supplies units only. The kinetic-isotropy primitive
supplies structural OS0 kinetic-form equality `c_t=c_s`, not a gauge action,
Hamiltonian, formation process, or coefficient. The realized-state primitive
supplies pointwise evaluation only, not a state, measure, weighting, or
selection. None is mislabeled as a wall, and none is enlarged here.

Concrete partial-closure paths remain:

- adopt and classify this face law as an explicit supplier, then seek a
  derivation of its form from a smaller symmetry or consistency class;
- compose the magnetic germ with historical PR #7903's positive electric term while
  preserving that PR's finite-truncation boundary;
- use fresh-site or joint-formation constructions such as historical PR #7900, but
  first prove they generalize beyond the flat-band blocks limited by open PR
  #7902; or
- build a feedback or auxiliary-field realization whose **unconditioned**
  marginal is the plaquette measure.

These are import-retirement and construction routes, not reasons to add an
axiom. This note proposes no axiom update.

### N7 — Steelman

A hostile reviewer can argue that the framework is a theory of conditional
probabilities inferred from readable Records, not a hidden mechanical action,
so the exact posterior may already be all the physical ownership required:
the recorded all-success pattern is data, the local likelihood is the law, and
Bayes supplies every prediction without an additional dynamics. That framing
is mathematically coherent and is the strongest reading of this result. To
promote it, one must still show why the realized Record history supplies the
relevant face event or frequency and how its three-dimensional conditional
predictions reproduce temporal experiments. Those are actionable formation
and dictionary obligations, so the broader negative claim “a likelihood can
never be the action” would be premature and is not made.

### N8 — Cross-cycle echo

The repository search found two directly similar histories. First,
`G3_CROSS_EDGE_INDEPENDENCE_IS_A_FORMATION_GATE_ATOM_MARGINAL_IDENTITY_FROM_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md`
separated fixed marginals from their joint coupling; this note applies the
same lesson and then supplies one product coupling constructively. Second, the
Record-formation append retired the older “records need not occur” statement
by changing the axiom to “Records form,” while deliberately leaving the
formation rule and weight downstream. The same mechanism could operate here
only through an explicit owner-approved law or a new derivation; it cannot be
silently assumed. Recent open PRs #7900 and #7902 show that joint formation can
work on a special flat-band block and fail one block larger, reinforcing the
need for the generalization test rather than ruling out joint formation.

**Gate result:** PASS for the two scoped negative boundaries. Seven materially
different routes were executed, the pairwise wall relations are explicitly unresolved, the
nonmatching photon residual is excluded, the strongest likelihood-as-physics
counterreading stays live, and no general no-go ships.

## Falsifiers

The bounded theorem fails if any of the following occurs:

- a doubled-lattice face site lacks one of the four boundary edge sites in its
  nearest-neighbor star;
- a proper cubic rotation changes the even overlap face weight;
- the supplied sequential local sweep has a likelihood different from the
  product of its unchanged conditional probabilities;
- the finite posterior weight is not gauge invariant;
- a symmetric Metropolis move violates detailed balance or a cycle product;
- the orientation-complete positive spatial Hessian lacks exactly two
  positive transverse directions at nonzero momentum;
- canonical quantization of the displayed positive rotor Hamiltonian gives a
  frequency other than `sqrt(alpha kappa P)` on either transverse direction;
  or
- summing both normalized binary outcomes changes the prior link marginal in
  the no-feedback model.

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py
```

Expected final line:

```text
TOTAL: PASS=24 FAIL=0
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
conditional_surface_status: "Supplied local success law, sequential factorization and conditioning; a harmonic electric completion is supplied separately."
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
