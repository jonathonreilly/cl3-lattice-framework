---
claim_id: autonomous_intermittent_record_instrument_calibration_nonselection_bounded_theorem_note_2026-07-11
claim_type: bounded_theorem
claim_scope: "Exact finite-dimensional effect-surface classification and full CP-instrument normal form for normalized rank-one locked-output instruments with a no-record outcome under conditional repeat/exclusivity: the remaining no-record CP operation is an explicit free parameter. Also an auxiliary-register CPTP countermodel proving that, for a supplied finite system/register decomposition and supplied rank-one menu, absorbing locked-register sectors, reuse of the same map, and menu-family equivariance do not imply blank-sector cross-label exclusion. The approved minimal_axioms dependency chain-satisfies; every additional physical interface remains conditional/open and gains no premise authority here."
upstream_dependencies:
  - minimal_axioms
  - record_observable_quotient_and_rank_one_formation_outcome_operation_normal_form_bounded_theorem_note_2026-07-11
  - kraus_choi_representation_normalization_reconciled_narrow_theorem_note_2026-06-05
runner: scripts/autonomous_intermittent_record_instrument_calibration_nonselection_2026_07_11.py
---

# Autonomous Intermittent Record Instrument: Classification And Calibration Nonselection

**Date:** 2026-07-11

**Type:** bounded theorem

**Status authority:** independent audit only. This source changes no axiom,
approved primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/autonomous_intermittent_record_instrument_calibration_nonselection_2026_07_11.py`](../scripts/autonomous_intermittent_record_instrument_calibration_nonselection_2026_07_11.py)

**Cached output:**
[`logs/runner-cache/autonomous_intermittent_record_instrument_calibration_nonselection_2026_07_11.txt`](../logs/runner-cache/autonomous_intermittent_record_instrument_calibration_nonselection_2026_07_11.txt)

## Question

The previous finite-carrier results leave an apparent conflict. Raw exhaustive-menu
repeat certainty gives `E_i=P_i`, but an intermittent normalized instrument
with a no-record outcome has formation effects `(1-q)P_i` and empty effect
`qI`. The correct full-instrument question is therefore:

```text
what does cross-label exclusion select conditional on a formation event,
when the mathematical no-record outcome occurs on an attempt?
```

This note gives the exact finite answer and then tests whether autonomous reuse
and absorbing auxiliary locked-register sectors derive the needed calibration.

## Existing-science reading gate

The actual instrument stack was read and its runners replayed before this
theorem:

- the approved
  [`minimal axioms`](MINIMAL_AXIOMS_2026-06-29.md) supply Lattice, Qubit,
  Admissibility, generic Record occurrence, permanence, readability, and finite
  scalar readout additivity, but no formation rule, instrument, probability,
  update, context, time, or rate;

- finite normalized isometry implies Kraus completeness, a CPTP unconditional
  map, and positive normalized selective branches;
- the reconciled finite-dimensional
  [`Kraus--Choi authority`](KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md)
  supplies existence of a Kraus representation for a named CP map with the
  normalization convention kept explicit;
- any named normalized Kraus family gives an explicit block-column Stinespring
  isometry (`29/0`), but the physical family is not selected;
- the controlled-copy/fresh-fragment model gives projective `K_i=P_i`,
  dephasing, and repeat-stable one-hot labels (`75/0`) inside its named pointer,
  Darwinism, fresh-fragment, time, and calibration conditions;
- the kernel (`48/0`), pre-record (`38/0`), and selective-atom (`33/0`)
  interfaces correctly keep possible-outcome weights, realized atoms, and
  post-record histories as different object types;
- the composition-semigroup runner still passes `28/0`, but its cache wrapper
  carries an older runner hash and the theorem concerns classical weight
  convolution, not overlapping CP instruments;
- the live narrow no-go grants generic occurrence from Record but leaves the
  formation process, site, state, weight, and rate open (`6/0`).

The rank-one locked-output input used here is
[`RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md`](RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md):

```text
J_i(rho)=Tr(E_i rho) P_i,       E_i>=0.                    (1)
```

Apart from the named finite Kraus-representation authority, all algebra below
is proved directly. Earlier intermittent and raw-menu results are
comparators, not additional proof authority. Current audit and effective
statuses for every comparator above live only on the pipeline-derived ledger
and are not snapshotted here.

## 1. Full intermittent effect classification

Let `H=C^d`, and fix a complete rank-one menu
`P_i=|i><i|`, `sum_i P_i=I`. Consider a finite CP instrument with outcomes
`{empty,1,...,d}`. Let the nonempty branches have the locked-output form (1),
and let

```text
F := J_empty^*(I) >= 0                                      (2)
```

be the no-record effect. Full normalization is

```text
F + sum_i E_i = I.                                          (3)
```

Impose **conditional repeat/exclusivity** only:

```text
Tr(P_j E_i)=0        for i!=j.                              (4)
```

Equation (4) says that if the input already occupies locked possibility `j`,
a nonempty outcome cannot produce a cross-label outcome `i`. It does not demand
that a nonempty event occur on every attempt.

### Theorem

Equations (1)--(4) imply, for unique `0<=e_i<=1`,

```text
E_i = e_i P_i,
F   = sum_i (1-e_i)P_i.                                    (5)
```

**Proof.** For fixed `i`, equation (4) makes every diagonal entry of positive
`E_i` vanish except possibly the `i`th. For a positive semidefinite matrix,

```text
|(E_i)_(jk)|^2 <= (E_i)_(jj)(E_i)_(kk),                    (6)
```

so each zero diagonal kills its full row and column. Hence `E_i=e_iP_i` with
`e_i>=0`. Equation (3) gives the second formula in (5), and `F>=0` gives
`e_i<=1`. QED.

For input `P_j`, the no-record probability is `q_j=1-e_j`; conditional on a
nonempty outcome, the label is exactly `j` whenever `e_j>0`. At the admitted
boundary `e_j=0` (equivalently `q_j=1`) the conditioning event has weight
zero and the conditional label distribution is undefined; every conditional
statement in this note therefore carries an explicit positive-conditioning
guard. Thus conditional
cross-label exclusion fixes the direction of each formation effect but not its
event efficiency.

If the no-record event is permutation-neutral on the fixed menu,

```text
q_i=q  for every i,                                         (7)
```

then

```text
E_i=(1-q)P_i,       F=qI.                                  (8)
```

For an arbitrary input density operator and `q<1`,

```text
p(empty)=q,
p(i)=(1-q)Tr(P_i rho),
p(i | nonempty)=Tr(P_i rho).                               (9)
```

The conditional formula in (9) is defined because the conditioning weight
`1-q` is positive; at the admitted `q=1` boundary no nonempty outcome occurs
and the conditional is undefined. The last equality is Born-form conditional
weighting under the named CP/trace
and probability interpretation. This note does not derive probability
semantics from the four axioms.

Without (7), conditional selection is detection-biased:

```text
p(i | nonempty)
  = e_i Tr(P_i rho) / sum_j e_j Tr(P_j rho),                (10)
```

defined whenever the conditioning event has positive weight,
`sum_j e_j Tr(P_j rho) > 0`; when every `e_j Tr(P_j rho)` vanishes, no
nonempty outcome occurs and (10) is undefined rather than silently
normalized.

Permutation-neutral event gating, not normalization alone, removes that bias.

## 2. Complete CP-instrument normal form; channel selection remains free

Conversely, choose any numbers `0<=e_i<=1` and any CP map `J_empty`
whose effect is `F=sum_i(1-e_i)P_i`. Together with

```text
J_i(rho)=e_i Tr(P_i rho)P_i,                                (11)
```

these maps form a normalized instrument by equation (3). Thus equations
(5) and (11), plus the explicitly arbitrary CP map with complementary effect
`F`, are the complete abstract finite-cell normal form within the named
rank-one locked-output/conditional-repeat class. This parameterizes every
member; it does not select a unique instrument.

Let `{L_alpha}` be Kraus operators for `J_empty`. Equation (8) fixes only

```text
sum_alpha L_alpha^dag L_alpha = qI.                         (12)
```

For `q>0`, `J_empty/q` is an arbitrary CPTP channel. If the no-record
operation has one Kraus operator, polar decomposition gives

```text
L=sqrt(q)U,       U unitary.                                (13)
```

Thus the earlier one-Kraus unitary freedom is the rank-one special case of the
full classification. A unitary channel and a dephasing channel can have the
same effect `qI` while acting differently on coherence.

An explicit Stinespring isometry for the classified instrument is

```text
V|psi>
  = sum_alpha |empty,alpha> tensor L_alpha|psi>
    + sum_i |i> tensor sqrt(e_i)P_i|psi>,                   (14)
```

because `V^dag V=F+sum_iE_i=I`. The labels in (14) are mathematical outcome
registers. This note does not identify the external labels as framework
Records.

## 3. Autonomous auxiliary-register countermodel

The remaining auxiliary question is whether absorption plus reuse of one
CPTP channel on a supplied finite system/register decomposition forces (4). It
does not.

Let the register have basis `{|empty>,|1>,...,|d>}`. For `0<=a<=1` define

```text
w_(ij) = a delta_(ij) + (1-a)/d.                            (15)
```

Fix `0<=q<1`. On the blank register use the Kraus operators

```text
N       = sqrt(q) I tensor |empty><empty|,
B_(ij)  = sqrt((1-q)w_(ij)) |i><j| tensor |i><empty|.       (16)
```

On every already locked register sector use

```text
R_(ij) = |i><j| tensor |i><i|.                              (17)
```

The complete family `{N,B_(ij),R_(ij)}` obeys

```text
sum K^dag K
 = I tensor |empty><empty|
   + sum_i I tensor |i><i|
 = I.                                                       (18)
```

It is therefore one autonomous CPTP channel on the full blank-plus-locked
carrier. Its blank-sector formation effects are

```text
E_i=(1-q)[aP_i+(1-a)I/d],       F=qI.                       (19)
```

For every locked label `i`, equation (17) resets an **arbitrary** system
input on that locked register sector to `P_i` (the channel maps
`rho_sys tensor |i><i|` to `Tr(rho_sys) P_i tensor |i><i|` for every system
operator `rho_sys`, not only for the fixed point `P_i`), keeps
the auxiliary register in `|i>`, and is idempotent under reuse. The runner
verifies the reset on a fully generic symbolic system input and on an
off-menu coherent input, not only on the consistent fixed point. These are
absorbing register-label/system-reset statements; no physical readout map or
framework-Record realization has been constructed. Yet for `a<1`, a blank
input `P_j` has nonzero cross-label formation weight for `i!=j`.

The construction is equivariant as a supplied-menu family. If `C_P` denotes
the channel built from menu `{P_i}` and `W_U=U tensor I_register`, then direct
conjugation of every system matrix unit in (16)--(17) gives

```text
C_(UPU^dag)[ W_U X W_U^dag ]
  = W_U C_P[X] W_U^dag.                                   (20)
```

This is equivariance of a menu-parameterized family, not invariance of one
menu-independent framework law. The construction is finite on one supplied
system/register carrier, normalized, and stable under sequential reuse. It is
not yet framework-local on `Z^3`.

Therefore:

```text
absorbing locked-register sectors + same-map reuse + menu-family equivariance
  do not imply blank-sector cross-label exclusion.          (21)
```

The exact missing cross-sector condition is that blank-sector formation be
calibrated to locked-register stabilization. Calling that stabilization a
physical readout or Record permanence requires a separate framework
realization; the auxiliary construction supplies neither.

This is a narrow auxiliary-register countermodel, not a no-go against deriving
calibration from a stronger process theorem. A coupling law tying blank-sector
formation to locked-sector stabilization, overlapping-cell consistency, or a physical
coarse-graining theorem remains a live route.

## 4. Physical residuals

The theorem gives the complete effect surface and CP-instrument normal form on
one abstract finite cell, with the no-record CP operation left as an explicit
parameter. It is not a `Z^3` locality or overlapping-cell classification. The
following remain separate:

1. selecting the physical rank-one readout context;
2. realizing the mathematical locked register and a readout map as a framework Record on `Z^3`;
3. deriving conditional repeat/exclusivity across blank and locked sectors;
4. deriving permutation-neutral event gating rather than unequal `e_i`;
5. selecting `q`, the conditional no-record CPTP channel, and a stopping rule;
6. composing overlapping local instruments into one simultaneous lattice law;
7. selecting event order, physical time, and rate.

The last two items remain separate open composition/order questions. Disjoint
tensor composition is
exact, but overlapping instruments need not commute and are not classified by
the classical record-composition semigroup lane.

## 5. Boundaries

- The approved `minimal_axioms` dependency chain-satisfies. Finite
  CP-instrument interpretation, the supplied rank-one menu, system/register
  decomposition, label/menu association, probability semantics, physical
  readout, conditional repeat/exclusivity, event neutrality, and
  framework-Record realization remain conditional/open interfaces and acquire
  no chain-satisfying premise authority here.
- The autonomous countermodel is a finite mathematical register construction;
  it does not identify the external labels as framework Records.
- The theorem does not derive probability semantics, outcome realization, or
  a Born rule from empirical counts.
- It does not derive a pointer, Darwinism bridge, controlled-copy Hamiltonian,
  fresh-fragment supply, or register calibration from Record.
- It does not select event order, rate, or the no-record channel.
- It does not construct a translation-covariant overlapping-edge instrument,
  simultaneous cubic QCA, continuum limit, Standard Model, or GR sector.
- It does not establish that the axioms require amendment. The exact hostile
  channel leaves stronger process/composition derivations open.

## Reproduction

```bash
python3 scripts/autonomous_intermittent_record_instrument_calibration_nonselection_2026_07_11.py
```
