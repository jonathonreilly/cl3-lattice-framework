---
claim_id: diagonal_thinking_synthesis_note_2026-06-04
claim_type_author_hint: meta
---

# Diagonal-Thinking — Synthesis and Honest Verdict (meta)

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (synthesis / governance scoping; no theorem promotion)
**Status:** source-note proposal awaiting independent audit handling.
**Status authority:** independent audit lane only.
**Package parent:** [`DIAGONAL_LATTICE_SCOPING_NOTE_2026-06-04.md`](DIAGONAL_LATTICE_SCOPING_NOTE_2026-06-04.md).

## 0. What this package asked

Extend the Lattice axiom's adjacency from cubic nearest-neighbor (NN) to
"NN + face-diagonal + body-diagonal", with diagonal links allowed to carry their
own qubit-link connections, and ask whether any of three open gates closes:
**GATE-COLOR** (`SU(3)`), **GATE-CHIRALITY** (`Γ_χ` on the generation factor),
**GATE-R-HALF** (`r = |b|^2/a^2 = 1/2`). Three commitment levels were graded:
**L1** (diagonals = NN Wilson-line composites, free), **L2** (diagonals =
independent `u(2)` connections, primitive-level), **L3** (distance-weighted
nonlocal site-dependent connections, import-level).

## 1. Scorecard

| phase | artifact | runner | PASS | verdict |
|---|---|---|---|---|
| 1 — scoping | `DIAGONAL_LATTICE_SCOPING_NOTE` | `diagonal_lattice_scoping_enumerator` | **30/0** | enumeration fixed; no science change |
| 2 — L1 negative | `DIAGONAL_AS_WILSON_LINE_COMPOSITE_L1_NEGATIVE_NOTE` | `diagonal_l1_wilson_line_composite_demonstration` | **26/0** | L1 adds **zero** new content |
| 3 — L2 color | `DIAGONAL_L2_INDEPENDENT_CONNECTION_DIMENSION_AUDIT_NOTE` | `diagonal_l2_face_algebra_dimension_audit` | **29/0** | GATE-COLOR **not closed** |
| 4 — chirality | `DIAGONAL_GATE_CHIRALITY_HW1_ORBIT_TEST_NOTE` | `diagonal_gate_chirality_hw1_orbit_test` | **27/0** | GATE-CHIRALITY **not closed** |
| 5 — r=1/2 | `DIAGONAL_GATE_R_HALF_WEIGHTED_PATH_TEST_NOTE` | `diagonal_gate_r_half_weighted_path_test` | **27/0** | GATE-R-HALF **not closed** |

Total: **139 PASS / 0 FAIL** across 5 runners.

## 2. Per-gate verdict

- **GATE-COLOR — negative (clean).** On the 4-qubit face the joint connection
  Lie algebra is `(+)_4 su(2) (+) u(1)` (dim 13) in the gauge embedding and
  `su(4)` in the tight-binding embedding; **no faithful `su(3)`**, and the two
  face-diagonals **add 0** (the NN graph is already connected). The dimension
  coincidence "`4 + 4 = 8`" is not realized. `su(3)` appears in exactly one
  place — the hw=1 **generation triangle** of face-diagonals — but it is a
  **horizontal / family** `su(3)` that mixes generations, not an independent
  internal color (`3 × 3 = 9 ≠ 3`). Wrong physical slot.

- **GATE-CHIRALITY — negative (clean).** The retained no-go
  `comm(R) ∩ anticomm(Γ_χ) ∩ Sym = {0}` is reproduced. The chiral family is
  2-dimensional but **entirely `C_3`-breaking**, and its intersection with the
  pure face-diagonal (off-diagonal) subspace is **dimension 0**: a direct
  inter-generation hop is never chiral, at any weights. The three face-diagonals
  are one `C_3` orbit, so the symmetric coupling is a circulant — squarely
  inside the no-go. Escape needs imported on-site terms **and** `C_3`-breaking.

- **GATE-R-HALF — negative (with one unforced coincidence).** No weight
  convention forced by retained machinery derives `r = 1/2`. Two of eight
  candidates hit it: a geometric inverse-length convention (**unforced**) and
  block-counting/equipartition (**= the already-admitted `AC_φλ`**). The
  diagonal triangle geometry explains the `(1, 2)` stay:shift multiplicity but
  not the equal-power **measure** (Born on the same geometry gives `r = 1`).

## 3. Net assessment

**No gate closes.** Stronger: the L2 dimension audit shows the diagonal
connections **add nothing to the gauge connection algebra** (the NN graph is
already connected), so paying L2's primitive-level governance cost buys no color
closure; and the L3 r=1/2 test shows no forced convention, so an L3 import would
buy only a restatement of `AC_φλ`. The thought experiment therefore does **not**
justify adopting an extended-adjacency convention or an extended-connection
primitive.

**The one coherent positive structural finding** is where the nontrivial content
concentrates: because the three generations are pairwise face-diagonal and
**not** NN, the diagonal extension's entire nontrivial content lives on the
hw=1 **generation triangle** — and in all three gates it lands exactly **one
structural ingredient short**:

| gate | what diagonals supply on the triangle | what is still missing |
|---|---|---|
| color | a family `su(3)` (dim 8) | an *independent* internal 3-carrier (not generations) |
| chirality | a direct inter-generation hop | on-site terms + `C_3`-breaking |
| r=1/2 | the `(1, 2)` sector multiplicity | the equal-power **measure** |

Every missing ingredient is **internal / measure data**, not adjacency geometry.
That is the actionable redirect (see §5).

## 4. Governance placement

- **L1:** empty; no governance step.
- **L2:** would be a **primitive-level** addition (new independent connection
  DOF) requiring **owner approval** per
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md).
  **Not recommended** — the audit shows it closes nothing.
- **L3:** would be an **import** requiring **explicit user authorization**.
  **Not recommended** — no forced convention yields `r = 1/2`.

Per policy §4, the correct disposition of a "would need a new
primitive/import to close" result is to **land a bounded boundary note** and
move on — which is exactly this package. No `axiom_premise_nodes.json` or
`tier_a_admissions.json` edit is requested; status is the audit lane's.

## 5. Recommendation (next move)

**Do not** open a convention proposal (L2) or an import petition (L3). The clean
negative is the deliverable: it **redirects future framework attacks away from
the adjacency surface** toward the internal/measure layer where all three
residuals actually live —

- **color:** an independent internal 3-dim carrier (extra multiplicity per
  site, e.g. a fiber enlargement), not a lattice-adjacency change;
- **chirality:** the separate-factor grading route (retained no-go §4, escape
  II) on the qubit factor, still open and needing a bridge theorem;
- **r=1/2:** the measure selection (equal-power/block-counting vs Born) inside
  `AC_φλ`, for which the diagonal geometry now provides a *picture* of the
  `(1,2)` multiplicity but not a derivation.

Optionally, the **generation-triangle family `su(3)`** is a real structure worth
recording as an observation (a horizontal symmetry the SM does not gauge), and
the `(1,2)`-multiplicity picture may be cited as intuition supporting the
`AC_φλ` sector structure — neither as a derivation.

## 6. Top open question raised

Color, chirality, and r=1/2 each fall one ingredient short on the **same**
object — the hw=1 generation triangle — and each missing ingredient is
internal/measure data, not geometry. **Is there a single internal enlargement of
the per-site carrier (beyond the one qubit) that simultaneously supplies the
independent color 3-carrier, the on-site chiral terms, and the equal-power
measure?** If one structure delivers all three, that — not adjacency — is where
the leverage is.

## 7. Disclaimers

- This package **does not change axioms**, sets no status, and modifies no
  parent note.
- Every claim is runner-checked (139 PASS / 0 FAIL); the negatives are honest
  and the one r=1/2 coincidence is explicitly flagged **unforced**.
- Status authority is the independent audit lane.
