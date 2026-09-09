---
claim_id: diagonal_gate_r_half_weighted_path_test_note_2026-06-04
claim_type_author_hint: meta
---

# Diagonal GATE-R-HALF Test — Weighted Paths (Speculative L3, meta)

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (speculative L3 weighted-path exploration)
**Status:** source-note proposal awaiting independent audit handling.
**Status authority:** independent audit lane only.
**Parent scope:** [`DIAGONAL_LATTICE_SCOPING_NOTE_2026-06-04.md`](DIAGONAL_LATTICE_SCOPING_NOTE_2026-06-04.md) (L3 level);
value anchor [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md).
**Primary runner:**
[`scripts/diagonal_gate_r_half_weighted_path_test.py`](../scripts/diagonal_gate_r_half_weighted_path_test.py)
**Cached log:**
[`logs/runner-cache/diagonal_gate_r_half_weighted_path_test.txt`](../logs/runner-cache/diagonal_gate_r_half_weighted_path_test.txt)

## Claim (meta, negative-with-one-coincidence)

Reading the Brannen circulant `Y_e = a I + b C + b̄ C^2` as a weighted-path
structure (a = "stay", b/b̄ = forward/backward face-diagonal shift), and testing
several natural diagonal weight conventions against the charged-lepton modulus
`r = |b|^2/a^2 = 1/2`:

- **No weight convention forced by retained machinery derives `r = 1/2`.** Of
  the conventions tested, exactly two land on `r = 1/2`: (i) a **geometric
  inverse-length** convention, which is **not forced** (it rests on normalizing
  the stay term to unit weight *and* on an inverse-length hop weight, both
  unforced); and (ii) **block-counting / equipartition**, which is precisely the
  **already-admitted** Tier-A input `AC_phi_lambda` (`AC_φλ`) — not new.
- The diagonal **geometry does explain the `(1, 2)` sector multiplicity** — from
  each generation vertex there is 1 stay and 2 face-diagonal neighbors, matching
  the `I`-term vs `{C, C^2}`-terms split — but it does **not** supply the
  **equal-power measure** between the sectors. The Born/dimension measure on the
  same geometry gives `r = 1` (`Q = 1`), not `1/2`.

So the diagonal extension **does not close** GATE-R-HALF; it re-expresses the
existing admitted measure choice in geometric language and adds one seductive
but unforced numerical coincidence. This note **does not change axioms**.

## 1. The structure being weighted

The exact retained relations (chain-of-custody L6, L9, L10):

```text
Q = 1/3 + (2/3) r,      r = |b|^2 / a^2,
r = 1/2  <=>  ||a I||^2_HS = ||b C + b̄ C^2||^2_HS   (3 a^2 = 6 |b|^2).
```

The runner verifies `||aI||^2 = 3a^2`, `||bC+b̄C^2||^2 = 6|b|^2`, the
equipartition `<=> r=1/2`, and `Q = 1/3 + (2/3)r` at the three lane points
`r ∈ {0, 1/2, 1}` (with a spectral cross-check at `δ=0`, where the spectrum is
sign-homogeneous and the signed Koide readout applies). The `1 : 2` factor
between the stay sector (one term `I`) and the shift sector (two terms
`C, C^2`) is the whole reason equipartition gives `1/2`.

## 2. Candidate weight conventions and their implied r

| convention | `|b|/a` | `r` | `Q` | `r = 1/2`? |
|---|---|---|---|---|
| geometric `1/L` (inverse length, stay≡1) | `1/√2` | **1/2** | **2/3** | yes — **unforced** |
| geometric `1/L^2` (propagator) | `1/2` | `1/4` | `1/2` | no |
| path-count (face-diag = 2 NN paths → 2) | `2` | `4` | `3` | no (unphysical) |
| inverse path-count (→ 1/2) | `1/2` | `1/4` | `1/2` | no |
| group orbit-size ratio `12/6 = 2` | `2` | `4` | `3` | no |
| group stabilizer ratio `4/8 = 1/2` | `1/2` | `1/4` | `1/2` | no |
| **K_0-real block-counting (equipartition)** | `1/√2` | **1/2** | **2/3** | yes — **= admitted `AC_φλ`** |
| Born / dimension measure (`a=|b|`) | `1` | `1` | `1` | no (the default) |

Two land on `1/2`; the rest scatter to `r ∈ {1/4, 1, 4}`.

## 3. Why neither `r=1/2` hit closes the gate

- **Geometric `1/L`.** The hit `|b| = 1/√2` requires (a) the stay coefficient
  `a` to be normalized to the unit/NN reference even though the stay term has
  geometric length 0, and (b) the face-diagonal hop to be weighted by inverse
  length. Both are conventions; neither is a retained theorem. Change either
  (e.g. inverse-length-squared, the massless propagator) and `r` moves to `1/4`.
  So this is a coincidence resting on unforced choices — **not forced**.
- **Block-counting.** Equal HS power per minimal central block of
  `R[Z_3] = R ⊕ C` gives `3a^2 = 6|b|^2 → r = 1/2`. This is exactly the chain's
  "`det_C` / equal-power-per-block" selector — the operative reading of the
  admitted input `AC_phi_lambda`. It is **not** a new derivation; it is the
  admission, restated. The competing Born/dimension measure on the identical
  geometry gives `r = 1`.

The diagonal picture's genuine contribution is **geometric intuition for the
`(1, 2)` multiplicity** (1 stay + 2 face-diagonal directions per vertex), i.e.
*why the shift sector has multiplicity 2*. But the modulus `r` is fixed by the
**measure** placed on those sectors (equal-power vs Born), and the geometry does
not select the measure. That selection is the open content of `AC_φλ`.

## 4. Verdict and governance

**GATE-R-HALF is not closed by diagonal weighting.** No L3 weighted-path
convention forced by retained machinery yields `r = 1/2`; the one forced
convention that does (block-counting) is the existing admission. L3 itself is an
import-level commitment (distance-weighted, site-dependent connections) and is
authorized here only as the exploration framing, not as an adopted primitive.

## 5. Boundary and residuals

- **Speculative (meta):** the weight conventions are candidate readings, not
  derived; the inverse-length hit is explicitly flagged as **not forced**.
- **Residual:** the measure selection (equal-power/block-counting vs
  Born/dimension) remains the open `AC_φλ` content; geometry supplies the
  multiplicity, not the measure.
- **No axiom change; no status set.**

## 6. Runner certificate

```text
python3 scripts/diagonal_gate_r_half_weighted_path_test.py
```

Expected:

```text
SUMMARY: PASS=27 FAIL=0
```
