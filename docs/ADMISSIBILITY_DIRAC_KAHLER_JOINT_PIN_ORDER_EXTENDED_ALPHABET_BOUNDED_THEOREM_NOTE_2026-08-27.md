---
claim_id: admissibility_dirac_kahler_joint_pin_order_extended_alphabet_bounded_theorem_note_2026-08-27
claim_type: bounded_theorem
claim_scope: "Exact linear-algebra observations for one supplied finite Dirac-Kahler fixture: two proposed sequential arrays, their l1 residual comparisons, one real-affine restoring system, three finite alphabet stacks, and fixed-coordinate residual representatives. No probability law, physical joint measurement, nonclassicality result, universal dependency-order theorem, classical no-go, parent theorem, action, axiom, premise, primitive, dynamics, continuum result, or gravity structure is supplied or adopted."
depends_on:
  - admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_bounded_theorem_note_2026-08-14
  - minimal_axioms
runner: scripts/admissibility_dirac_kahler_joint_pin_order_extended_alphabet_2026_08_27.py
---

# Joint-pin order and extended-alphabet finite diagnostics — corrected bounded note

**Historical block:** 212

**Repair date:** 2026-09-10

**Claim type:** `bounded_theorem`

**Claim status:** finite exact linear-algebra observations on one fixed fixture

**Premise status:** no object in this note is registered or adopted as an axiom, primitive, measurement law, conditional-probability law, dynamics, or gravity structure

**Primary runner:**
[`scripts/admissibility_dirac_kahler_joint_pin_order_extended_alphabet_2026_08_27.py`](../scripts/admissibility_dirac_kahler_joint_pin_order_extended_alphabet_2026_08_27.py)

**Finite supplied construction:** the helper uses only `EX`, `ET`, and
`shift_lifts()` from the current
[Block 105 finite construction](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md).
That link declares the source of those fixed matrices; this note does not adopt
Block 105's theorem scope, its parent chain, or any physical interpretation.
The current [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and
[premise registry](audit/data/axiom_premise_nodes.json) are read only as the
authority boundary confirming that this fixture is not a registered premise.

This correction retains the useful exact calculations from the historical Block 212 package and removes four unsupported inferences. It replaces the missing 42-module runtime closure with a reviewed helper containing only the definitions this calculation uses. The original four package bodies and the relevant historical helper bodies are preserved byte-for-byte in the dated recovery directory.

The calculation concerns a fixed `12 x 4` cover with antiperiodic half-cover fold, physical matrix size `24`, pinned links at time levels `0` and `1`, free levels `(2, 3, 4, 5)`, rational x-graded carrier data, and the self-edge differential selected by the historical runner. The symbols `W2` and `W9` below name two exact diagonal-profile constructions. Treating a `W9` profile as a formation weight or a pinned profile as a conditional distribution remains a proposed reading. The finite matrix calculation does not identify that reading.

## Corrections

1. **Consistency uses rank equality.** The single-readout system has shape `5 x 16` and measured ranks
   `rank(A) = rank([A|b]) = 4`. That equality proves real affine solvability for this instance. The fact that there are more unknowns than equations does not prove consistency. For example,
   `A = [[1,0,0],[1,0,0]]`, `b = [0,1]` is underdetermined but inconsistent, with ranks `(1,2)`. Nonnegative or simplex-constrained restoring weights were not tested.

2. **Residual comparisons use l1 norms.** The `10x`, `100x`, strict, and narrow-excess statements compare exact l1 norms. They are not componentwise inequalities. Componentwise magnitude counts are reported separately. Against the slot-4 single-pin residual, both two-pin l1 norms are strictly larger, while the excess is below one two-hundredth of the slot-4 norm. The forward comparison has only `3/4` larger component magnitudes; the reverse comparison has `4/4`.

3. **The raw Gram matrix is not singular at every rung.** At the `25 x 4` rung, `rank(A)=4`, so `A^T A` is positive definite and invertible. The raw `A^T A` is singular only at the `25 x 12` and `25 x 20` rungs, where the ranks are `8` and `12`. The implemented projector first selects the RREF pivot-column basis `C`; `C` has full column rank at every rung, so `C^T C` is positive definite and invertible at every rung.

4. **No universal dependency-order theorem follows.** Different values of two proposed sequential factorizations are a finite property of those formulas on this fixture. The simultaneous dictionary substitution commutes. Classical order-dependent response rules and a misspecified conditional reading remain available explanations. No theorem about all dependency orders, no nonclassicality theorem, and no priority claim is made.

## Reviewed finite fixture

The repaired runner imports `scripts/admissibility_dirac_kahler_released7753_fixture_2026_09_10.py`. That helper extracts these definitions:

- the sparse `12 x 4` cover and the physical `24 x 24` half-cover fold;
- the cover Hodge matrix with local moduli `(nu,a,b,mu)`;
- the selected chart-self-edge differential `d_(0,0)`;
- pins `b=0`, `a=nu` on links `0` and `1`;
- the x-graded carrier and record substitution;
- the Hermitian part and exact inverses needed for W2 and W9 diagonal profiles.

The helper imports current Block 105 for `EX`, `ET`, and `shift_lifts()`, with its exact file bytes pinned. For the selected self edge the source and target chart indices coincide, so the historical healing-weight difference is exactly zero. The helper therefore does not import the historical healing weights or construct the unused fifteen chart edges.

This extraction is a runtime closure, not a scientific dependency claim. Historical Blocks 165, 166, 170, and 171 supplied the old implementation. Their broader theorem prose, reflection construction, observable families, holonomy dials, action interpretation, and other imported claims are not live inputs and are not adopted here.

For a cell with positive volume `v` and `|sigma|<1`, the local cell contribution to the Hodge matrix has eigenvalues

```
v/4, 1/(4v), v/(4(1+sigma)), v/(4(1-sigma)).
```

They are positive on the tested carrier. The assembled cover Hodge and its tested antiperiodic half-cover fold are positive on this fixture. If

```
Q = H + i(H d + d^dagger H),
S = herm(Q),
```

then `S=H` for the fixed mass `m=1`, because `i(Hd+d^dagger H)` is anti-Hermitian. For invertible `Q`,

```
herm(Q^-1) = Q^(-dagger) S Q^-1,
```

so the diagonal entries used by W9 are positive; W2 uses `S^-1`. These identities explain full support for the tested profiles. They do not turn the normalized diagonals into a physical probability law.

## Joint-pin finite instrument

Let `P0(t)` be the record-free W9 profile at time level `t`. A record `(t,x)=0` substitutes zero shear at one free cell. The fixed joint slots are `2` and `4`; the read level is `5`.

The two proposed sequential arrays are

```
w_fwd(x,y) = P0(2)[x] * P_(2,x)(4)[y],
w_rev(x,y) = P0(4)[y] * P_(4,y)(2)[x].
```

Both arrays contain 16 exact nonnegative rational entries and sum exactly to one. For either array `w`, define the readout residual

```
r_w = P0(5) - sum_(x,y) w(x,y) P_(2,x;4,y)(5).
```

The exact run is expected to reproduce:

| quantity | forward | reverse |
|---|---:|---:|
| nonzero residual components | `4/4` | `4/4` |
| exact sign pattern | `(+,-,+,-)` | `(+,-,+,-)` |
| exact component sum | `0` | `0` |
| display only | `(+4.969e-04,-1.279e-03,+2.016e-03,-1.233e-03)` | `(+5.010e-04,-1.282e-03,+2.017e-03,-1.236e-03)` |

The exact numerators are fingerprinted by digit counts `(1403,1403,1401,1403)` and `(1381,1382,1380,1382)`. The decimal strings are display aids and are not used as tolerances.

Single-pin residual displays from the same environment cache are:

| slot | display only |
|---:|---|
| `2` | `(+6.972e-06,-1.088e-05,+8.217e-06,-4.311e-06)` |
| `3` | `(+9.178e-05,-2.297e-04,+1.328e-04,+5.072e-06)` |
| `4` | `(+4.964e-04,-1.274e-03,+2.012e-03,-1.234e-03)` |

For each two-pin order, exact l1 comparisons give:

| single slot | `10 ||r_single||_1 < ||r_joint||_1` | `100 ||r_single||_1 < ||r_joint||_1` | `||r_single||_1 < ||r_joint||_1` | `200 (||r_joint||_1-||r_single||_1) < ||r_single||_1` |
|---:|:---:|:---:|:---:|:---:|
| `2` | yes | yes | yes | no |
| `3` | yes | no | yes | no |
| `4` | no | no | yes | yes |

The component-magnitude counts `(number of i with |r_joint[i]|>|r_single[i]|)` are forward `(4,4,3)` and reverse `(4,4,4)` for slots `(2,3,4)`. This is why the l1 conclusion and the componentwise census must remain separate.

## Factorization order and restoring system

The two proposed arrays differ in `16/16` entries. Their maximum exact absolute difference occurs at outcome `(1,0)`, has numerator/denominator digit counts `(292,295)`, and displays as `+2.180e-04`. Their weighted readout residuals differ in `4/4` components and sum to the same normalized total.

Reversing insertion order in the simultaneous record dictionary changes `0/16` substituted matrices. Thus the measured distinction lies in the two proposed factorization formulas. It is not noncommutativity of the matrix substitution.

The single-readout restoring system places the sixteen joint profiles into the columns of a matrix and appends the affine row `sum(w)=1`. Its shape and ranks are

```
shape(A) = (5,16),
rank(A) = 4,
rank([A|b]) = 4.
```

Rank equality establishes real affine solutions on this instance. It does not establish a nonnegative solution. No simplex test and no multi-context joint stack is run.

## Extended finite alphabet

At the middle slot `3`, the tested class values are

```
{0, 1/5, -1/5, 2/5, -2/5}.
```

Four spatial cells give 20 columns. The six contexts are `(W9,W2) x (5,4,2)`, with four profile rows per context and one affine normalization row. The same 20 environment objects supply all three nested column sets.

| outcomes | shape | `rank(A)` | `rank([A|b])` | affine consistency |
|---:|---:|---:|---:|:---:|
| `4` | `25 x 4` | `4` | `5` | no |
| `12` | `25 x 12` | `8` | `9` | no |
| `20` | `25 x 20` | `12` | `13` | no |

These are three displayed points, not a rank-growth law. Six exact normalization-row relations cap the coefficient rank at `19`, so column count alone does not yield an outcome threshold. Different class values, additional outcomes, more slots, different profile families, and different levels remain untested.

The raw normal-matrix status is `(invertible, singular, singular)` for the 4-, 12-, and 20-column matrices. The projector actually uses pivot bases with sizes `(4,8,12)`, and every basis Gram matrix `C^T C` is invertible.

## Fixed-coordinate residual comparison

For each nested matrix `A_n`, the runner chooses RREF pivot columns `C_n` and forms

```
r_n = b - C_n (C_n^T C_n)^-1 C_n^T b.
```

The exact checks are `A_n^T r_n=0` and `r_n^T b != 0`. In the displayed row coordinates the three chosen residuals are pairwise nonproportional; all `300/300` pairwise 2x2 minors are nonzero for each pair, with the historical compact mod-101 fingerprints `(7,72,71)` recomputed by the repaired runner.

This refutes only the old, explicitly proposed statement that these particular fixed-coordinate representatives are the same direction under the tested class refinements. It does not define a representation-invariant obstruction. Because the outcome columns are nested, the 20-column residual is also a valid nonzero-pairing left-cokernel certificate for the smaller stacks. Existence of such a common certificate is preserved; uniqueness and canonicality are not.

## Evidence and historical attribution

The four original Block 212 bodies are archived exactly. The old cache reported `PASS=29 FAIL=0` at a different main snapshot and a runtime near `51.83s`. That cache is historical evidence only. No standalone artifact matching the old prose's “independent check” was found among the four package bodies, so the repaired package calls those strings historical cache fingerprints rather than independent validation.

The repaired canonical runner must be executed through the repository's existing cached wrapper after all source and input hashes are frozen. Its workload is 45 exact rational `24 x 24` environments plus `25 x 20` ranks and pivot-basis solves. A `60s` producer cap is too close to the historical runtime. The proposed bounded execution is a `120s` producer cap, `150s` outer cap, and `2 GiB` peak-RSS cap. The expensive producer is not part of the source preflight.

## Scope and disposition

Preserved finite calculations:

- exact nonnegative normalization of the two proposed arrays;
- exact failure of both finite mixture identities under the stated proposed reading;
- exact l1 and component-magnitude comparisons;
- exact factorization-array difference and commuting simultaneous substitution;
- exact single-readout rank equality and affine real consistency;
- exact nested-stack rank inequalities;
- exact normalization relations and rank ceiling;
- exact fixed-coordinate residual orthogonality and nonproportionality.

Rejected or left open:

- any physical joint-measurement or conditional-probability interpretation;
- nonnegative restoring weights for the `5 x 16` system;
- a multi-context joint-instrument exclusion;
- a complete classical outcome alphabet;
- a universal rank pattern or dependency-order theorem;
- a classical hidden-variable no-go, bound violation, generic-parameter theorem, continuum result, dynamics, or gravity claim;
- adoption of any historical parent theorem or broader closure claim.

## No-Go Discipline Gate (N1–N8)

This section stress-tests the negative-shaped wording in this note. The gate
passes only for the bounded positive claim above; it does not authorize a
general no-go, minimum-content claim, or universal dependency-order theorem.

- **N1 — alternatives:** at least six live routes remain open: other pin/read
  levels, other finite fixtures and parameter values, simplex feasibility,
  a multi-context joint-instrument stack, richer outcome alphabets, and other
  factorization or readout rules. None is closed by this calculation.
- **N2 — wall independence:** the rank, l1, raw-Gram, and factorization-order
  corrections are distinct finite observations, not an independent or
  exhaustive set of walls.
- **N3 — hidden assumptions:** the `W9` probability reading, conditional
  reading of pinned profiles, fixed Hodge data, chosen l1 norm, and fixed row
  coordinates are supplied choices. Changing them is outside this result.
- **N4 — residual matching:** every failed identity or inconsistent stack is
  tied to the arrays, contexts, and finite alphabet explicitly displayed
  above. No residual is promoted to a statement about an untested model class.
- **N5 — rhetoric:** the exact per-element through lattice-wide certificate is
  printed by the primary runner and repeated verbatim below. It separates the
  finite checks from the open physical and universal readings.
- **N6 — partial closure:** the calculation preserves exact normalization,
  ranks, and residual relations. The open routes require additional tests or a
  different supplied model; no new axiom is inferred from their being open.
- **N7 — steelman:** the strongest alternative explanation is that the order
  effect belongs to the two chosen sequential factorization formulas, while a
  classical or differently specified conditional rule could behave otherwise.
  The simultaneous record substitution commutes exactly, so this alternative
  is not excluded.
- **N8 — cross-cycle echo:** Block 105 supplies three fixed finite matrix
  constructions only. No Block 105 theorem, historical parent theorem,
  audit grade, action, or physical conditional law propagates into this
  claim.

**Gate result:** PASS for the corrected `bounded_theorem` wording; FAIL for any
classical no-go, nonclassicality conclusion, universal ordering theorem, or
claim that the tested alphabet is complete.

## N5 execution certificate

N5: per_element: THE STRUCTURAL DOUBLE-RECORD ACTION IS ONE SIMULTANEOUS DICTIONARY SUBSTITUTION; REVERSING INSERTION ORDER CHANGES ZERO OF SIXTEEN SUBSTITUTED MATRICES.
per_site: THE TWO PROPOSED CHAIN-RULE FACTORIZATION ARRAYS ARE COMPONENTWISE NONNEGATIVE, EACH SUMS EXACTLY TO ONE, AND THEY DIFFER IN SIXTEEN OF SIXTEEN WEIGHTS; THEIR MIXTURE RESIDUALS ARE NONZERO IN FOUR OF FOUR COMPONENTS.
per_mode: IN THE STATED l1 COMPARISON, THE SLOT-4 SINGLE PIN ALREADY CARRIES ALL BUT A SUB-PERCENT EXCESS OF THE TWO-PIN RESIDUAL; THE SINGLE-READOUT SIXTEEN-WEIGHT RESTORING SYSTEM IS REAL-AFFINE SOLVABLE BECAUSE rank(A) = rank([A|b]) = 4, AND NONNEGATIVITY AND MULTI-CONTEXT EXCLUSION REMAIN OPEN.
per_block: THE SIX-CONTEXT TWENTY-OUTCOME STACK IS INCONSISTENT AT RANKS (12, 13), REPRODUCING THE FINITE SERIES (4, 5), (8, 9), (12, 13); SIX EXACT NORMALIZATION-ROW RELATIONS CAP COEFFICIENT RANK AT 19, SO NO OUTCOME-COUNT THRESHOLD IS CLAIMED.
lattice_wide: THE THREE FIXED-ROW-COORDINATE EUCLIDEAN RESIDUALS ARE PAIRWISE NONPROPORTIONAL, REFUTING ONLY THE DECLARED REPRESENTATIVE-LEVEL INVARIANCE CONJECTURE; THIS IS NOT A REPRESENTATION-INVARIANT OBSTRUCTION, UNIVERSAL DEPENDENCY-ORDER THEOREM, CLASSICAL NO-GO, CONTINUUM RESULT, DYNAMICS, OR GRAVITY.
