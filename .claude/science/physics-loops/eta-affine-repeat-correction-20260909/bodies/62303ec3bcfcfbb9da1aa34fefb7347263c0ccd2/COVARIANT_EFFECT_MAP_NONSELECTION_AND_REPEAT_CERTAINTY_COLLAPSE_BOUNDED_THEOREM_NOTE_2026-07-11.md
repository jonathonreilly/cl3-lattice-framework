---
claim_id: covariant_effect_map_nonselection_and_repeat_certainty_collapse_bounded_theorem_note_2026-07-11
claim_type: bounded_theorem
claim_scope: "Exact finite-dimensional nonselection family for normalized, positive, orthogonally additive, noncontextual, unitary-covariant effect assignments, plus the theorem that exhaustive rank-one menu normalization and repeat certainty force E_i=P_i. POVM additivity and repeat certainty are named conditional hypotheses with zero premise weight and are not derived from the four axioms."
upstream_dependencies:
  - minimal_axioms
  - record_observable_quotient_and_rank_one_formation_outcome_operation_normal_form_bounded_theorem_note_2026-07-11
runner: scripts/covariant_effect_map_nonselection_repeat_certainty_collapse_2026_07_11.py
---

# Covariant Effect Nonselection And Repeat-Certainty Collapse

**Date:** 2026-07-11

**Type:** bounded theorem

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/covariant_effect_map_nonselection_repeat_certainty_collapse_2026_07_11.py`](../scripts/covariant_effect_map_nonselection_repeat_certainty_collapse_2026_07_11.py)

**Cached output:**
[`logs/runner-cache/covariant_effect_map_nonselection_repeat_certainty_collapse_2026_07_11.txt`](../logs/runner-cache/covariant_effect_map_nonselection_repeat_certainty_collapse_2026_07_11.txt)

## Question

The rank-one locked-output theorem leaves each formation outcome in the form

```text
J_P(rho) = Tr(E_P rho) P,       0 <= E_P <= I.
```

What selects `E_P=P`?

The existing Gleason and Busch lanes answer a different question. They show
that an already named conditional additive, normalized, nonnegative,
noncontextual
weight functional has trace form. They do not identify its representing
density operator with the input density operator, and they do not select the
projection-indexed formation-effect assignment.

This note proves two exact facts:

1. positivity, normalization, orthogonal additivity, noncontextuality, and
   unitary covariance still leave a continuous depolarizing freedom;
2. exhaustive rank-one menu normalization plus repeat certainty collapses the
   effect menu to `E_i=P_i`.

Within a named conditional effect/probability surface, the final algebraic
selector is the repeat-certainty condition of equation (11). Framework-Record
realization, readout probability semantics, and repeat certainty remain
separate physical bridges.

## Existing-science reading gate

The actual current lane was replayed before this theorem:

- the composite Gleason bridge reports `PASS=24 FAIL=0`; it assumes grading, orthogonal additivity,
  noncontextuality, full `M_4` projection menus including entangled
  resolutions, and the named Gleason theorem;
- the graded-interface v2 runner reports `PASS=7 FAIL=0`; its v2 interface is
  a candidate input rather than a registered premise;
- the qubit Busch/effect runner reports `40 PASS / 0 FAIL` and correctly proves
  trace form from named conditional POVM-effect axioms M1--M3, but it does not
  derive M1--M3;
- the post-record count firewall (`56/0`) and finite-frequency boundary
  (`35/0`) show that realized counts do not supply predictive weights, IID
  structure, or convergence;
- the finite ideal-record Born parent conditionally identifies a pre-record
  reference state.

These replayed rows are non-load-bearing comparators; their current audit and
effective statuses live only on the pipeline-derived ledger and are not
snapshotted here. The present nonselection, duality, and collapse proofs are
self-contained.
The Busch comparator is
`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`.
The arbitrary locked-output effect is derived, under that note's own named
conditions, in the record-observable quotient and rank-one formation-outcome
normal-form theorem
[`RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md`](RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md).

## 1. Exact covariant nonselection family

Let `H=C^d`. For every effect `0<=A<=I`, define, for `0<=a<=1`,

```text
T_a(A) = a A + (1-a) Tr(A) I/d.                         (1)
```

For a projection `P`, write `E_P^(a)=T_a(P)`, so
`Tr(P)=rank(P)`.

This family obeys:

```text
T_a(0)=0,       T_a(I)=I,
0 <= E_P^(a) <= I,
E_(P+Q)^(a)=E_P^(a)+E_Q^(a)       when PQ=0,
E_(UPU^dag)^(a)=U E_P^(a) U^dag.
```

For every projective resolution `sum_i P_i=I`, equation (1) gives

```text
sum_i E_(P_i)^(a)=I.                                      (2)
```

More generally, if `{A_i}` is any POVM, linearity and
`sum_i Tr(A_i)=Tr(I)=d` give `sum_i T_a(A_i)=I`. If `lambda` is an
eigenvalue of `A`, the corresponding eigenvalue of `T_a(A)` is
`a lambda+(1-a)Tr(A)/d`, which lies in `[0,1]`. Thus the family survives
the full effect/POVM M1--M3 surface, not only projective menus.

The assignment is a function of `A`, not of its embedding menu, so it is
noncontextual. Positivity, full effect/POVM additivity and normalization,
menu noncontextuality, and unitary covariance therefore do not select `a`.

For any density operator `rho` and any effect `A`,

```text
m_(rho,a)(A) := Tr(rho T_a(A))
  = Tr([a rho + (1-a)I/d] A).                             (3)
```

In particular, set `A=P` for a projection-indexed formation effect.
Accordingly, applying a scalar trace-representation theorem to the functional
on the left returns the depolarized representative

```text
sigma_a(rho)=a rho+(1-a)I/d,                              (4)
```

not the identification `sigma=rho`. Trace form alone does not close effect
selection.

## 2. Repeat certainty collapses the hostile family

For rank-one `P`, the self-weight is

```text
Tr(P E_P^(a)) = a + (1-a)/d.                              (5)
```

At finite `d>1`, imposing repeat certainty

```text
Tr(P E_P)=1                                               (6)
```

selects `a=1` inside (1), so `E_P=P`.

Equation (6) is not silently attributed to Record permanence. Permanence says
an existing framework Record remains locked. It does not say that the
formation effect for a future outcome is the same operational functional as a
deterministic readout of the existing record.

## 3. General exhaustive-menu collapse theorem

Let `{P_i=|i><i|}_{i=1}^d` be a complete rank-one projective menu. Let
`{E_i}` be effects satisfying

```text
E_i >= 0,        sum_i E_i=I,        Tr(E_i P_i)=1.        (7)
```

Then

```text
E_i=P_i  for every i.                                     (8)
```

**Proof.** In the basis defined by the menu, positivity gives
`<j|E_i|j>>=0`. Normalization and the last clause of (7) give

```text
sum_i <j|E_i|j>=1,       <j|E_j|j>=1,
```

so `<j|E_i|j>=0` for every `i!=j`. For a positive semidefinite matrix,

```text
|(E_i)_(jk)|^2 <= (E_i)_(jj) (E_i)_(kk).                  (9)
```

Every zero diagonal entry therefore kills its full row and column. `E_i`
annihilates every `|j>` with `j!=i`, while normalization and repeat certainty
give `E_i|i> = |i>`. Hence `E_i=P_i`. QED.

Both clauses are load-bearing. Repeat certainty alone admits `E_i=I` for all
`i`; joint normalization rules that family out. Joint normalization without
repeat certainty admits the continuous family (1).

Combining (8) with the locked-output normal form gives

```text
J_i(rho)=Tr(P_i rho)P_i.                                  (10)
```

This is the rank-one projective measure-and-prepare/Lueders instrument with
Born-form trace weights, conditional on the named CP/trace interpretation,
menu-normalization, and repeat-certainty hypotheses. Those hypotheses carry
zero framework-premise weight here. This is not a derivation of probability
semantics from the framework axioms.

## 4. Physical residual

The theorem does not derive the physical applicability of POVM additivity from
the four axioms. It also does not derive repeat certainty from Record
permanence. For the algebraic theorem the exact missing condition is simply

```text
RC_i: Tr(P_i E_i)=1  for every i.                           (11)
```

A physical derivation of (11) for the formation effects remains open. No repo
name is coined for that gap here; repeat certainty is not an approved
primitive, and it carries zero premise weight until derived. Before equation
(10) can be framework-native, three additional interfaces remain explicit: realize the
output as a framework Record on `Z^3`, identify a same-carrier readout as an
effect/probability functional, and derive deterministic repeat readout. Record
permanence alone supplies none of those identifications and does not prove
`RC_i` for formation.

If a candidate local instrument plus controlled coarse-graining derives
`RC_i` and the effect-menu hypotheses, equation (10) follows without a
preferred rank-one projective readout context: the argument applies
covariantly to every fixed rank-one menu under the theorem hypotheses. If not,
the depolarizing family (1) remains a hostile alternative.

## 5. Boundaries

- Effects, the rank-one menu, positivity, joint normalization, POVM/effect
  additivity, and repeat certainty are named conditional hypotheses carrying
  zero framework-premise weight.
- The theorem does not derive POVM additivity, noncontextuality, composite-menu
  eligibility, or the physical menu from Admissibility or Record.
- The theorem does not derive repeat certainty from Record permanence.
- The theorem does not identify an outcome label as a framework Record.
- The theorem fixes the formation-effect assignment only after the
  repeat-certainty condition (11) is supplied; it does not derive event
  occurrence, site/order/rate, reset/IID structure, a clock, or a continuum
  law.
- Counts and empirical frequencies are not used as predictive probabilities.
- The theorem does not establish that the axioms require amendment. The
  [`minimal axioms`](MINIMAL_AXIOMS_2026-06-29.md) leave the process surface
  downstream; a local process theorem could still derive the named bridge. An
  explicit primitive would carry zero premise weight until approval and a
  registry update.

## 6. No-Go Discipline summary

- **N1:** projective-only Gleason, composite Gleason, qubit POVM/Busch,
  covariance, and repeat-certainty routes are separated.
- **N2:** the exhaustive normalized menu and `RC_i` are the two independent
  algebraic walls. Record realization, readout probability semantics,
  deterministic repeat readout, and the repeat-certainty condition `RC_i`
  form a physical
  dependency chain; event/rate and continuum are downstream out-of-scope gates.
- **N3:** every effect, menu, normalization, covariance, and repeat-certainty
  hypothesis is explicit.
- **N4:** the result attacks effect identification, not the different count,
  frequency, reference-state, event-rate, or continuum residuals.
- **N5:** the collapse is per fixed finite rank-one menu under the theorem
  hypotheses; no lattice-wide or continuum statement is made.
- **N6:** composite-menu derivation and local-instrument coarse-graining remain
  live derivation routes; explicit primitive approval and registry update are
  a governance-only route with zero premise weight beforehand.
- **N7:** a hostile reviewer can reject `RC_i` as physically underived; the
  theorem agrees and leaves its process derivation as the next target.
- **N8:** prior Gleason/Busch work repeatedly closed representation form while
  leaving probability/additivity and identification of the representing
  density operator with the input density operator open; this theorem does not
  relabel those residuals as solved.

## Reproduction

```bash
python3 scripts/covariant_effect_map_nonselection_repeat_certainty_collapse_2026_07_11.py
```
