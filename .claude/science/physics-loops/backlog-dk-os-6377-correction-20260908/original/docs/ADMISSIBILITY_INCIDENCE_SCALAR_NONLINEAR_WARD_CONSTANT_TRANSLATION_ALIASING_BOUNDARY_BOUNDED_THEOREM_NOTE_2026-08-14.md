---
claim_id: admissibility_incidence_scalar_nonlinear_ward_constant_translation_aliasing_boundary_bounded_theorem_note_2026-08-14
claim_status: unretained
claim_type: bounded_theorem
claim_scope: "For the exact Block95 nearest-neighbour half-density scalar, the continuum Weyl-symbol analogue of its order-h phi^2 Ward equation closes with an explicit nonlinear tensor transformation and local scalar seagull. On the lattice, however, twenty-four exact L=24 constant-parameter mode pairs have zero free-symbol transfer difference, identical raw stress coordinates, zero linear geometry gauge variation, and opposite nonzero matter commutators of magnitude 3 sqrt(2)/8. Therefore, within the fixed Block95 flat-inner-product half-density contract, no quadratic matter seagull S_phi2, pure-gravity cubic S_g3, regular anti-Hermitian metric-dependent matter generator D1, or geometry-only nonlinear gauge transformation R1 can close the second-order Ward coefficient, irrespective of finite support enlargement. This is a support-independent fixed-contract obstruction, not a gravity no-go: a changed discrete differential calculus, changed matter action/vertex, geometry-dependent matter inner product, multi-degree/link carrier, or nonlocal/quasilocal replacement of M0/D0/V together with its translation representation remains live. The minimal axioms do not select Block95, so no axiom amendment is justified. There is no audit retention, obligation retirement, end-to-end theory, or TOE percentage movement."
depends_on:
  - admissibility_counterpropagating_scalar_bianchi_trace_shear_energy_current_exchange_boundary_bounded_theorem_note_2026-08-14
runner: scripts/admissibility_incidence_scalar_nonlinear_ward_constant_translation_aliasing_boundary_2026_08_14.py
---

# Incidence Scalar Nonlinear Ward: Constant-Translation Aliasing Boundary

Date: 2026-08-14

Campaign block: 98

Status: positive continuum completion plus a narrow fixed-carrier obstruction

Retention status: proposed only; independent retention remains open

## 1. Result Up Front

Block 97 left one deliberately time-boxed target: assemble the
`S_g3/S_phi2/R1/D1` second-order Ward system, solve it, or identify an exact
rank inconsistency and stop spending on the fixed carrier.  This block reaches
the third outcome, but only after a positive continuum control removes a bad
ansatz as an explanation.

For the continuum Weyl symbols corresponding to Block 95, one explicit
nonlinear tensor transformation cancels the momentum-quadratic commutator and
one local scalar seagull cancels the remaining connection term.  Thus the
continuum second-order identity works.

For the actual periodic lattice symbols, a constant parameter exposes a
different invariant.  There are twenty-four exact `L=24` pairs for which:

- the incoming and outgoing free symbols agree within each pair;
- the two members have identical centered and raw stress coordinates;
- the linear geometry gauge map is zero because the parameter transfer is
  zero; and
- the two matter commutators are opposite and nonzero, with magnitude
  `3 sqrt(2)/8`.

At this coefficient, `S_phi2` varies only through the zero linear geometry
gauge map, `S_g3` has no matter legs, and every regular anti-Hermitian `D1`
contributes the zero free-symbol difference.  A geometry-only `R1` sees the
same stress row at both members.  It would therefore have to produce two
opposite values from one tensor coefficient.  The coefficient matrix has rank
one and its augmentation has rank two for every pair.

The theorem is only for the fixed Block 95 carrier with its flat-inner-product
half-density contract.  This is not a gravity no-go.  Changed-carrier routes
remain live.  So does a geometry-dependent inner product on the same site
carrier.  In particular, a changed discrete differential calculus, changed
first-order matter vertex, multi-degree or link carrier, geometry-dependent
matter inner product, and a nonlocal or quasilocal replacement of `M0/D0/V`
together with its translation representation are outside the theorem.  A
merely nonlocal regular anti-Hermitian `D1` on the unchanged parent is not an
escape: it is still multiplied by the exact zero `Delta M0` on the witnesses.

The minimal axioms do not select Block 95 or its generalized translation
generator.  No axiom amendment is justified.  The correct disposition is to
stop extending the fixed Block 95 nonlinear Ward coefficient census and pivot
to the typed-event/Record-law confluence seam.  A changed-contract gravity
repair—new carrier/action or an explicitly geometry-dependent inner
product—remains the only justified re-entry to this specific gravity seam.

## 2. Bound Authority And Exact Contract

The current authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) at
`origin/main eee6ab5874e2fc207db5526dc82d9f71ae550c7c`, with axiom blob
`bc23300becfe4e4db57153c0e94cfcdf2338da71`.

The immediate frozen parent is
[Block 97](ADMISSIBILITY_COUNTERPROPAGATING_SCALAR_BIANCHI_TRACE_SHEAR_ENERGY_CURRENT_EXCHANGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md)
at commit `213de9467339a124968e4b3433cbe76d67b284cb`.  It positively cancels the
leading reduced exchange defect and names the complete second-order Ward
coefficient system as the next stop gate.  The actual scalar operator,
generator, and stress come from
[Block 95](ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md).
The raw tensor gauge map comes from
[Block 77](ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md).

The narrow target contract fixes all of the following:

1. the Block 95 nearest-neighbour free symbol `M0`;
2. its finite anti-Hermitian half-density generator `D0`;
3. its derivative-bilinear first metric vertex `V`;
4. the Block 77 linear geometry gauge map `R0`;
5. a geometry-only `R1`, meaning its Fourier coefficient may depend on the
   geometry and parameter modes but not on a matter momentum;
6. a regular anti-Hermitian `D1`, so variation of `S0` remains a commutator and
   has no pole on an equal-`M0` transfer;
7. an arbitrary Hermitian quadratic matter seagull `S_phi2`; and
8. an arbitrary pure-gravity cubic `S_g3`.

No finite radius is imposed in the contradiction.  Bounded finite Laurent
support is the intended application, but enlarging its radius does not change
any zero or equality used below.

## 3. The Second-Order Matter Ward Coefficient

Write the candidate expansions schematically as

\[
 M[h]=M_0+V[h]+{1\over2}W_0[h,h]+O(h^3),
\]

\[
 D_\xi[h]=D_{0,\xi}+D_{1,\xi}[h]+O(h^2),
 \qquad
 R_\xi[h]=R_{0,\xi}+R_{1,\xi}[h]+O(h^2).
\]

For an incoming matter mode `k`, geometry transfer `r`, parameter transfer
`s`, and total transfer `Q=r+s`, the order-`h phi^2` coefficient is

\[
 \begin{split}
 {cal W}_2={}&
 V(H;k+s,r)D_0(\xi;k,s)
 -D_0(\xi;k+r,s)V(H;k,r)\\
 &+V(R_1(H,\xi);k,Q)
 +W_0(H,R_0\xi;k;r,s)
 +[M_0,D_1(H,\xi)]_{k+Q,k}.
 \end{split}                                           \tag{1}
\]

Here `W0` is symmetric in its two geometry arguments.  The explicit factor
`1/2` in the action expansion makes variation of the two equal placements
produce the single `W0(H,R0 xi)` contribution displayed in (1).  `S_g3`
belongs to the pure-geometry coefficient sector and contributes zero to (1).

At first order, the actual raw Block 95 identity remains

\[
 R_0(-q)^T t_r(q,k)
 +[M_0(k+q)-M_0(k)]d_r(q,k)=0.                         \tag{2}
\]

The runner rechecks (2) on 96 generic off-shell probes rather than treating
the new obstruction as a retrospective failure of the positive parent.

## 4. Positive Continuum Control

Before testing the lattice, replace every lattice sine by its affine
continuum momentum.  Put

\[
 A=\eta(k+(r+s)/2),\qquad \hat r=\eta r,
 \qquad \hat s=\eta s,
\]

and, for any transfer `u`, use

\[
 A_u(k)=\eta(k+u/2),\qquad
 V(H;k,u)=H(A_u(k),A_u(k)),\qquad
 D_0(\xi;k,s)=i\,\xi\mathbin\cdot\eta(k+s/2).
\]

Direct expansion of the first line of (1) gives

\[
 {C\over i}=2(\xi\cdot A)H(A,\hat s)
 -(\xi\cdot\hat r)H(A,A)
 -{1\over4}(\xi\cdot\hat r)H(\hat s,\hat s).          \tag{3}
\]

The nonlinear geometry coefficient

\[
 R_1(H,\xi)=i\left[(\xi\cdot\hat r)H
 -\xi\otimes(H\hat s)-(H\hat s)\otimes\xi\right]     \tag{4}
\]

cancels the first two terms of (3).  Let

\[
 J=R_0(s)\xi=-i(s\otimes\xi+\xi\otimes s).
\]

The symmetric local scalar seagull

\[
 W_0(H,J;r,s)
 ={1\over8}(r\cdot\eta s)\,H:J
 -{1\over4}(H\hat s)\cdot\eta(J\hat r)               \tag{5}
\]

uses `H:J=H_(mu nu) J^(mu nu)=H:(eta J eta)`.  With the `1/2`
normalization in the action expansion, (5) is exactly the complete seagull
variation in (1), with no omitted factor of two.

Substituting `J=R0(s)xi` into (5) gives
`+i (xi dot r-hat) H(s-hat,s-hat)/4` and cancels the final term.
The runner checks (3)--(5) on 192 full Lorentz-signature generic probes below
`1.1e-13`; the frozen-seed maximum is `1.0480505352461478e-13`.

This control matters.  The negative lattice result is not evidence that a
seagull was forgotten, that the tensor sign was guessed incorrectly, or that
second-order covariance is generically impossible.  The exact continuum
completion is the hostile positive comparator.

## 5. Exact Lattice Alias Pair

Return to the actual Block 95 symbols

\[
 M_0(k)=p(k)^T\eta p(k),\qquad p_\mu(k)=2\sin(k_\mu/2),
\]

\[
 a(k,r)=\eta\sin(k+r/2),\quad
 V(H;k,r)=H(a,a),\quad
 D_0(\xi;k,0)=i\,\xi\cdot\eta\sin k.                 \tag{6}
\]

Choose two distinct spatial axes `j != ell` and signs
`epsilon,delta in {minus one,plus one}`.  Set

\[
 r_j=\epsilon\pi/2,\qquad r_\ell=\delta\pi/2,
\]

\[
 \theta_j=\pi/3,\qquad
 \theta_\ell=-\epsilon\delta\pi/3,
 \qquad k=\theta-r/2,                                \tag{7}
\]

and define the reflected member by replacing only
`theta_j=pi/3` with `theta'_j=2pi/3`.  Take

\[
 H=e_j e_j^T,\qquad \xi=e_j.                          \tag{8}
\]

Every coordinate in (7) is an integer multiple of `2 pi/24`, so this is an
exact finite-periodic `L=24` witness, not an irrational generic probe.  Since
the two centers have the same sine,

\[
 a(k,r)=a(k',r),\qquad t_r(r,k)=t_r(r,k').             \tag{9}
\]

Also

\[
 M_0(k+r)-M_0(k)=2p(r)\cdot a(k,r)=0                 \tag{10}
\]

for both members.  A constant parameter has `R0(0)=0`.  But its matter
commutator is

\[
 C(k)=iV(H;k,r)\,\xi\cdot\eta[\sin k-\sin(k+r)]
 =-i\epsilon{3\sqrt2\over8},                         \tag{11}
\]

while reflection flips only the relevant cosine and gives

\[
 C(k')=+i\epsilon{3\sqrt2\over8}.                    \tag{12}
\]

There are six ordered spatial-axis pairs and four sign choices, hence the 24
runner witnesses.

## 6. Support-Independent Rank Contradiction

Evaluate (1) on either member of one fixed pair.

- `R0(0)=0`, so every variation of an arbitrary `S_phi2` is zero.
- `S_g3` has no `phi-bar phi` coefficient and is zero in this sector.
- Equation (10) makes `[M0,D1]=0` for every regular anti-Hermitian `D1`, no
  matter how large its finite support is.
- A geometry-only `R1(H,xi;r,0)` is one tensor coefficient.  By (9), its
  pairing with the two stress rows is identical.

Thus the two equations reduce to

\[
 t^T R_1=-C(k),\qquad t^T R_1=-C(k').                 \tag{13}
\]

The left sides are equal and the right sides are opposite nonzero numbers.
For each pair, the coefficient matrix has rank one and the augmented matrix
has rank two.  Its least-squares relative residual is exactly one to floating
roundoff.

This is stronger than the initially planned finite Laurent census.  Adding
more `S_phi2`, `S_g3`, or regular `D1` columns adds only zero columns on the
witness.  Adding more local structures to `R1` still produces one
matter-momentum-independent tensor and therefore the same duplicated row.
A singular `D1` proportional to the inverse free-symbol difference is not a
bounded-local Laurent operator and is explicitly outside the target.

The load-bearing issue is the periodic generalized translation velocity:
`sin k` has two centers with the same stress sine and opposite cosine.  In the
continuum, the affine generator has no such alias.

## 7. Scientific And Axiom Disposition

The fixed Block 95 carrier cannot be the nonlinear matter carrier for the
requested geometry Ward completion under its current flat-inner-product
half-density contract.
That is real route elimination.  It does not erase its valid first-order Ward,
source, recoil, constraint-cadence, or reduced-exchange results.

The live repairs change at least one primary object:

1. use a discrete differential calculus whose translations act as an exact
   derivation on the relevant product algebra, likely with link or
   multi-degree fields;
2. change `M0`, `D0`, and the first metric vertex together so their nonlinear
   representation closes;
3. use a geometry-dependent matter inner product, allowing the coordinate
   `D1` to be non-anti-Hermitian while the physical transformation remains
   skew with respect to that metric;
4. replace `M0/D0/V` together with a nonlocal or quasilocal exact translation
   representation; or
5. derive a Record-native event law without first representing gravity as a
   continuum-like local diffeomorphism on this scalar carrier.

The present axioms specify none of these and never selected Block 95.  The
failed candidate therefore does not expose an inconsistency in the axioms.
No axiom amendment is justified.  If a later owner decision requires a
bounded-local nonlinear gravity law, the missing scientific primitive is an
explicit nonlinear discrete differential calculus plus its Record compiler,
not a patch to one failed coefficient.

## 8. No-Go Discipline Gate

### N1 — Alternative Route Enumeration

| attack route | honesty marker | result against the narrow claim |
|---|---|---|
| arbitrary quadratic matter seagull | **ATTEMPTED** | its order-`h` variation contains `R0(0)=0`, so it contributes zero on every witness |
| arbitrary pure-gravity cubic term | **ATTEMPTED** | `S_g3` has no matter legs and cannot enter the `h xi phi-bar phi` coefficient |
| arbitrary regular anti-Hermitian D1 | **ATTEMPTED** | its `S0` variation is the free-symbol difference times a finite coefficient, which vanishes by (10) |
| arbitrary geometry-only R1 | **ATTEMPTED** | both modes have the same raw stress row, so one tensor coefficient cannot match opposite targets |
| larger same-symbol support | **ATTEMPTED** | support enlargement adds only zero `S_phi2/D1/S_g3` columns or more coefficients behind the same duplicated `R1` row |
| continuum nonlinear tensor plus seagull | **ATTEMPTED** | equations (3)--(5) close positively; substituting periodic sines reintroduces the exact cosine alias in (11)--(12) |
| regular second-order field redefinition | **ATTEMPTED** | it only redistributes finite `W/D1/R1` coefficients; the zero columns and duplicated row in (13) are invariant |

The first four routes attack distinct coefficient sectors; the continuum
completion is a concrete combined mechanism, and the field-redefinition route
attacks the formulation rather than one coefficient basis.  The support row
checks that none of those conclusions is a small-radius artifact.

The following changed-primary-object routes are deliberately **not counted**
toward the narrow N1 minimum.  They remain untested escapes and therefore make
any broad negative fail:

| broad escape | honesty marker | why it remains live |
|---|---|---|
| changed discrete differential calculus | **UNTESTED — LIVE** | link, degree-ladder, or enlarged carriers change the fixed target and must derive a new first-order source and nonlinear representation |
| geometry-dependent matter inner product | **UNTESTED — LIVE** | it changes the anti-Hermitian half-density contract and requires a new measure, action, and source derivation |
| nonlocal/quasilocal replacement of `M0/D0/V` and its derivative representation | **UNTESTED — LIVE** | it changes the parent representation and evades finite Laurent periodicity; changing `D1` alone does not evade the exact `Delta M0=0` witness |
| changed `M0/D0/V` action | **UNTESTED — LIVE** | it directly evades the fixed-parent theorem and is the strongest same-purpose gravity repair |

Narrow fixed-carrier status: PASS.  Broad gravity/axiom status: FAIL —
partial-narrowing.

### N2 — Wall-Independence Audit

The apparent four failures `S_phi2`, `S_g3`, `D1`, and `R1` collapse to one
terminal invariant: constant-parameter equal-level aliasing on the fixed
periodic half-density representation.  They are coefficient-sector
consequences of one two-row contradiction, not four independent walls.  With
one collapsed wall there is no pairwise independence table to inflate.

### N3 — Hidden-Wall Scan

The proof requires the exact `M0/D0/V/R0` parent symbols, a geometry-only
`R1`, a regular anti-Hermitian `D1`, and the usual separation between pure
gravity and matter coefficients.  All are explicit in Section 2.  It does not
assume a selected Standard Model scalar, a positive gravity Hamiltonian, a
Record compiler, a continuum limit, or audit retention.

| phrase hit | disposition |
|---|---|
| `we assume` / `by construction` / `as is standard` | scan vocabulary only; no proof step uses the phrase |
| `the framework provides` / `registered` / `canonical` | scan vocabulary only; the bound parents are named directly |
| `bridge context` / `background` | non-load-bearing explanatory context only |
| `naturally` / `obviously` / `standard QFT` | absent as load-bearing reasoning |

### N4 — Residual Matching

| cited witness | its residual | current residual | match |
|---|---|---|---|
| [Block 95, Sections 5 and 9](ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md) | positive first-order cochain; second-order completion explicitly open | order-`h phi^2` extension of those exact symbols | **yes**, as parent and open target |
| [Block 97, Sections 8 and 12](ADMISSIBILITY_COUNTERPROPAGATING_SCALAR_BIANCHI_TRACE_SHEAR_ENERGY_CURRENT_EXCHANGE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md) | `S_g3/S_phi2/R1/D1` coefficient system named as next gate | same coefficient system, restricted to a necessary constant-parameter matter subblock | **yes** |
| [Block 93, Sections 4--5](ADMISSIBILITY_RAW_GRAPH_WARD_COMPACT_PULLBACK_TRANSLATION_GENERATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md) | no finite-range exact shift logarithm or same-carrier smooth pullback | nonlinear alias of the generalized `sin k` generator | **no** as proof evidence; retained only as a similar periodic-symbol scope echo |
| continuum control, Section 4 here | affine Weyl-symbol second-order completion | lattice periodic-symbol completion | **no** as a negative witness; used only as a hostile positive control |

No nonmatching citation is borrowed to strengthen the rank proof.

### N5 — Rhetoric Audit

| resolution | executed statement |
|---|---|
| per-element | exact tensor, generator, commutator, continuum `R1`, and seagull coefficients are evaluated |
| per-site | checked and not executed — the theorem is Fourier-polynomial and support-independent, while no changed-carrier site action is constructed |
| per-mode | all twenty-four exact `L=24` pair witnesses are checked |
| per-block | the complete necessary second-order matter subblock is reduced to rank one versus augmented rank two |
| lattice-wide | checked and not executed — changed-carrier full action, full-`Z3` control, nonlinear gravity, Record compilation, selection, and retention remain open |

Forbidden broader rhetoric includes “gravity fails,” “no local nonlinear Ward
law exists,” “the axioms are inconsistent,” “a fifth axiom is required,” and
“the Block 95 first-order theorem was false.”

### N6 — Partial-Closure Path Scan

No owner ratification or vocabulary refactor can turn the two opposite numbers
in (13) into one number.  This is a mathematical candidate failure, not a
labeling wall.  Conversely, it is not an axiom failure because the candidate
carrier is unselected.

Existing positive partial-closure paths remain:

- Block 93's multi-degree spline escape changes the carrier and supplies an
  exact derivative/incidence diagram;
- Block 95 remains a valid first-order common-action/source construction;
- Block 97 remains a valid reduced energy-exchange construction; and
- a Record-native sequential law can bypass the demand that this scalar carry
  a continuum-like nonlinear diffeomorphism representation.

### N7 — Steelman

**Strongest steelman.**  A hostile builder should reject the premise that a
site half-density with a fixed flat inner product must carry nonlinear lattice
diffeomorphisms.  Introduce link or multi-degree matter variables and a
geometry-dependent inner product, derive `M0`, `D0`, and `V` together from one
finite graph action, and require skew-adjointness only in the physical
geometry-dependent norm.  Block 93 already gives an explicit degree-ladder
mechanism showing that a changed carrier can possess an exact local
derivative/incidence identity.  Such a construction can evade both the
anti-Hermitian `D1` zero and the duplicated stress row, then close a new
second-order Ward identity.  This defeats every broad gravity or axiom no-go,
but it does not satisfy the fixed Block 95 contract proved inconsistent here.

### N8 — Cross-Cycle Echo

| prior result | later mechanism | consequence here |
|---|---|---|
| Block 83 lacked a bounded-local pullback and graph Ward current | Block 93 changed the conserved primary object to raw graph edges and kept a degree-ladder carrier escape | do not universalize a same-carrier obstruction |
| Block 93 closed compact same-carrier continuous interpolation | Block 95 changed to a lattice half-density and obtained a positive first-order Ward cochain | changed carriers can retire real walls; nonlinear closure must be rederived rather than presumed |
| Block 96 exposed the homogeneous linearization singularity | a nonlinear trace branch repaired that source sector | preserve nonlinear/changed-formulation steelmen unless the exact invariant addresses them |
| Block 97 left a quartic coefficient target | this block executes a necessary subblock and finds a support-independent contradiction | stop only the fixed Block 95 continuation; do not stop gravity or Record-law searches |

The cross-cycle echo is decisive for scope: prior carrier changes succeeded,
so changed-carrier routes remain live.

Narrow fixed-carrier status: PASS.  Broad gravity/axiom status: FAIL —
partial-narrowing.

## 9. Validation And Falsifiers

The runner has eight gates:

1. current authority and frozen Block 97 dependency chain;
2. the still-positive Block 95 first-order cochain;
3. the explicit continuum nonlinear tensor plus seagull completion;
4. twenty-four exact `L=24` alias pairs;
5. the rank-one versus augmented-rank-two universal coefficient gate;
6. the landed N1--N8 packet;
7. the gravity, axiom, carrier, and retention firewall; and
8. the TOE score and portfolio stop rule.

Hostile mutations are:

```text
stale_axiom_authority
break_first_order_parent
drop_continuum_seagull
break_alias_pair
admit_singular_d1
weaken_no_go_packet
claim_gravity_no_go
claim_axiom_update
claim_toe_progress
claim_obligation_retirement
```

Each must produce exactly seven passes and one intended failure.

Baseline:

```bash
python3 scripts/admissibility_incidence_scalar_nonlinear_ward_constant_translation_aliasing_boundary_2026_08_14.py
```

## 10. TOE Map And Portfolio Decision

The strict map is unchanged:

| lane | exploratory | admissibility | retained | closure confidence |
|---|---:|---:|---:|---:|
| operational / Records | 95 | 92 | 50 | 99 |
| causal / time | 76 | 72 | 41 | 99 |
| inertia / matter | 95 | 96 | 75 | 99 |
| gravity / source / resources | 70 | 45 | 29 | 94 |
| Born / history | 84 | 63 | 34 | 99 |

There is zero obligation retirement.  No TOE percentage moves.  The
retained-positive end-to-end theory count remains zero.

The result materially changes portfolio ranking even though it does not move
the strict score.  Under geometry-only `R1` and regular flat-inner-product
anti-Hermitian `D1`, the fixed Block 95 nonlinear Ward route is closed at a
necessary coefficient subblock, so more Laurent-basis enlargement on that
contract is low value.  The ranking below is a portfolio inference from the
current root dependency structure, not a theorem consequence of this block;
it should be rechecked against a refreshed scorecard before the next long
campaign.  The next investment is:

1. pivot to the typed-event/Record-law confluence seam, where a positive
   retained end-to-end law has higher fanout across operational, causal, Born,
   and gravity-source typing; and
2. retain one explicitly changed-contract gravity repair as the only gravity
   re-entry: either rederive `M0/D0/V` on a changed carrier/action, or derive a
   geometry-dependent inner product before another nonlinear coefficient
   census.

No new axiom text should be proposed until one changed-carrier or
representation/inner-product construction either closes or localizes a
contract property that the current axioms must actually select.
