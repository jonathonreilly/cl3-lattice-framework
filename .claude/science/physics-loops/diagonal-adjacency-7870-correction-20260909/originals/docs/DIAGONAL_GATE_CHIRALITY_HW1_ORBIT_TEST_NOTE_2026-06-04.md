---
claim_id: diagonal_gate_chirality_hw1_orbit_test_note_2026-06-04
claim_type_author_hint: bounded_theorem
---

# Diagonal GATE-CHIRALITY Test — hw=1 Orbit (Bounded, No-Escape)

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** bounded theorem (exact algebra; no-escape result)
**Status:** source-note proposal awaiting independent audit handling.
**Status authority:** independent audit lane only.
**Parent scope:** [`DIAGONAL_LATTICE_SCOPING_NOTE_2026-06-04.md`](DIAGONAL_LATTICE_SCOPING_NOTE_2026-06-04.md);
retained anchor [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md).
**Primary runner:**
[`scripts/diagonal_gate_chirality_hw1_orbit_test.py`](../scripts/diagonal_gate_chirality_hw1_orbit_test.py)
**Cached log:**
[`logs/runner-cache/diagonal_gate_chirality_hw1_orbit_test.txt`](../logs/runner-cache/diagonal_gate_chirality_hw1_orbit_test.txt)

## Claim (bounded, no-escape)

Adding a direct **face-diagonal** coupling between the hw=1 generation sites
does **not** escape the retained chirality no-go. Concretely, on the
3-generation factor `R^3` with cyclic shift `R` and chiral grading
`Γ_χ = (2/3)J − I`:

1. **Retained no-go reproduced:** `comm(R) ∩ anticomm(Γ_χ) ∩ Sym(R^3) = {0}`.
2. **The chiral family is 2-dimensional** (chiral operators do exist) and
   **every** nonzero chiral operator **breaks `C_3`-equivariance**.
3. **Pure face-diagonal couplings are never chiral.** The zero-diagonal
   symmetric subspace (the only structure a generation-to-generation
   face-diagonal hop supplies) intersects the chiral family in **dimension 0** —
   for **any** weights, equal or unequal.

So the face-diagonal extension fails on **two** counts at once: a
`C_3`-symmetric assignment (the natural one, since the three face-diagonals are
a **single `C_3` orbit**) is a circulant and lands squarely inside the no-go;
and even a symmetry-broken assignment, being purely off-diagonal, cannot be
chiral at all — chirality requires on-site (diagonal) terms the inter-generation
links do not supply. **The face-diagonal coupling does NOT escape the chirality
no-go natively.** This note **does not change axioms**.

## 1. Geometry: the hw=1 orbit is a single C_3 orbit of face-diagonals

The three generations are the hw=1 BZ-corner triplet
`{(1,0,0),(0,1,0),(0,0,1)}`
([`STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)).
They are pairwise at Hamming distance 2 — **face-diagonal** on the BZ-corner
cube — and the `C_3[111]` shift `R` cycles them. The three connecting
face-diagonals therefore form **one `C_3` orbit**: there is no `C_3`-invariant
way to weight them unequally. A symmetry-respecting face-diagonal coupling is
necessarily equal-weight.

## 2. The retained no-go and why Γ_χ-equivariance is the wall

`Γ_χ = (2/3)J − I = (−1/3)I + (2/3)(R + R^2)` is itself a circulant, so it
commutes with `R`. Any `R`-commuting (= `C_3`-equivariant) Hermitian `H` is a
circulant, hence commutes with `Γ_χ`; combined with `{H,Γ_χ}=0` this forces
`HΓ_χ=0`, so `H=0`. The runner reproduces
`comm(R) ∩ anticomm(Γ_χ) ∩ Sym = {0}` exactly.

## 3. The chiral family exists but is off-limits to face-diagonals

The full anti-commuting family `anticomm(Γ_χ) ∩ Sym(R^3)` has **dimension 2**.
In the `Γ_χ` eigenbasis it consists of operators mapping the `+1` eigenline to
the `−1` eigenplane — i.e. purely "off-block" between the trivial character and
the `(ω, ω^2)` plane. Two facts make it inaccessible to face-diagonal couplings:

- **(C_3-breaking)** every nonzero member has `[H,R] ≠ 0` — the chiral family
  is disjoint from the circulant algebra. A `C_3`-symmetric (equal-weight)
  face-diagonal coupling `M_sym = R + R^2 = J − I` is a circulant and is **not**
  chiral (`{M_sym, Γ_χ} ≠ 0`).
- **(needs on-site terms)** the chiral family's intersection with the
  zero-diagonal symmetric subspace is **dimension 0**. A face-diagonal qulink
  between two generations contributes an **off-diagonal** (hopping) term; pure
  off-diagonal symmetric operators on the triangle **cannot be chiral at all**,
  for any weights. Chirality requires diagonal/on-site structure that the
  inter-generation face-diagonal links do not provide.

## 4. The two named escapes, and why neither closes this gate

- **Escape (I) — drop `C_3`-equivariance (external input).** One could break
  the single-orbit symmetry by hand-tuning unequal weights *and* adding on-site
  terms. But (a) the unequal weighting of three symmetry-equivalent
  face-diagonals is an **external input**, exactly the no-go's escape (I) where
  "the specific `h` becomes an external input"; and (b) the pure-hop slice is
  non-chiral anyway, so the on-site terms must also be imported. This is not a
  derivation from the diagonal structure; it is the same admission the no-go
  already names.
- **Escape (II) — grading on a separate factor.** A chirality grading on the
  **qubit** factor (`I_3 ⊗ σ_z`) is a *different object* from the gate's `Γ_χ`
  on the **generation** factor (`Γ_χ ⊗ I_2`); the two commute (different tensor
  factors). Per the retained no-go §4 this multi-factor route is **open** and
  needs a separate bridge theorem. It is not the grading GATE-CHIRALITY asks
  for, so it sidesteps rather than closes this gate.

## 5. Verdict

**GATE-CHIRALITY is not closed by the diagonal extension.** The face-diagonal
coupling relocates the gap — from "no chiral operator exists" to "what supplies
the on-site terms and breaks the `C_3` symmetry among three equivalent
face-diagonals" — but closes nothing: both ingredients are external inputs. The
diagonal extension's only structural contribution here (a direct inter-generation
hop) is precisely the part that can **never** be chiral.

## 6. Boundary and residuals

- **Exact algebra; bounded:** dimensions `0` (off-diagonal chiral slice), `2`
  (full chiral family), `0` (no-go intersection) are exact and runner-checked.
- **Residual R1:** the separate-factor (qubit-grading) construction — escape
  (II) — remains open and is governed by the retained no-go §4, not by this
  note.
- **No axiom change; no status set.**

## 7. Runner certificate

```text
python3 scripts/diagonal_gate_chirality_hw1_orbit_test.py
```

Expected:

```text
SUMMARY: PASS=27 FAIL=0
```
