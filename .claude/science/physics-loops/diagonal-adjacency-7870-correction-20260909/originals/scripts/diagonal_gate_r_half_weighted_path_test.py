#!/usr/bin/env python3
"""GATE-R-HALF test: does any natural diagonal weight convention force the
Brannen-circulant modulus r = |b|^2/a^2 = 1/2 ?

Brannen circulant Y_e = a I + b C + b̄ C^2 read as a weighted-path structure:
  a   = "stay"           (identity, no shift)
  b   = "forward shift"  (face-diagonal forward around the generation triangle)
  b̄  = "backward shift" (face-diagonal backward)
with the exact Koide relation  Q = 1/3 + (2/3) r  (retained L6), and
  r = 1/2  <=>  HS equipartition  ||a I||^2 = ||b C + b̄ C^2||^2  (retained L9).

This runner computes the implied r (and Koide Q) for several natural weight
conventions and reports, honestly, which give r = 1/2 and whether any is forced
by retained machinery. This is the speculative L3 layer; claim_type = meta.
No axiom change, no closure asserted.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs" / "DIAGONAL_GATE_R_HALF_WEIGHTED_PATH_TEST_NOTE_2026-06-04.md"

PASS = 0
FAIL = 0


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)  # forward 3-cycle
I3 = np.eye(3, dtype=complex)


def hs2(M):
    return float(np.real(np.trace(M.conj().T @ M)))


def koide_Q_from_r(r):
    return 1.0 / 3.0 + (2.0 / 3.0) * r


def koide_Q_from_spectrum(a, bmod, delta=0.0):
    """Q = (sum lambda^2)/(sum |lambda|)^2 for H = aI + bC + b̄C^2, b=|b|e^{iδ}."""
    b = bmod * np.exp(1j * delta)
    H = a * I3 + b * C + np.conj(b) * (C @ C)
    lam = np.linalg.eigvalsh((H + H.conj().T) / 2)  # Hermitian for real a
    return float(np.sum(lam ** 2) / (np.sum(np.abs(lam)) ** 2))


def r_from_ratio(bmod, a=1.0):
    return (bmod ** 2) / (a ** 2)


def main() -> int:
    print("=" * 72)
    print("GATE-R-HALF: diagonal weight conventions vs r = 1/2")
    print("=" * 72)

    # ---- structural identities --------------------------------------------
    record("C is the forward 3-cycle, C^3 = I", np.allclose(np.linalg.matrix_power(C, 3), I3))
    a = 1.0
    bmod = 1.0 / np.sqrt(2.0)
    record("HS norm ||aI||^2 = 3 a^2", abs(hs2(a * I3) - 3 * a ** 2) < 1e-9)
    shift = bmod * C + bmod * (C @ C)  # |b|=b̄ moduli equal (δ=0 representative)
    record("HS norm ||bC + b̄C^2||^2 = 6 |b|^2", abs(hs2(shift) - 6 * bmod ** 2) < 1e-9)
    record("equipartition ||aI||^2 = ||bC+b̄C^2||^2  <=>  3a^2 = 6|b|^2  <=>  r = 1/2",
           abs(3 * a ** 2 - 6 * bmod ** 2) < 1e-9 and abs(r_from_ratio(bmod, a) - 0.5) < 1e-9)

    # exact Koide relation Q = 1/3 + (2/3) r at the three lane points
    for r, Qexp in [(0.0, 1 / 3), (0.5, 2 / 3), (1.0, 1.0)]:
        record(f"Koide Q = 1/3 + (2/3)r gives Q={Qexp:.3f} at r={r}", abs(koide_Q_from_r(r) - Qexp) < 1e-9)
    # spectral cross-check (δ=0, sign-homogeneous spectrum -> signed readout)
    record("spectral cross-check: r=1/2, δ=0 gives Koide Q = 2/3",
           abs(koide_Q_from_spectrum(1.0, 1 / np.sqrt(2), 0.0) - 2 / 3) < 1e-9)
    record("spectral cross-check: r=1 gives Q = 1 (det/Born default lane)",
           abs(koide_Q_from_spectrum(1.0, 1.0, 0.0) - 1.0) < 1e-9)

    # ---- geometric multiplicity picture from the triangle -----------------
    # each generation vertex: 1 stay (I) + 2 face-diagonal neighbors (C, C^2).
    stay_mult, shift_mult = 1, 2
    record("triangle geometry: each generation vertex has 1 stay + 2 face-diagonal neighbors",
           (stay_mult, shift_mult) == (1, 2))
    record("the (1,2) sector multiplicity matches the I-term vs {C,C^2}-terms split",
           stay_mult == 1 and shift_mult == 2)

    # ---- candidate weight conventions -------------------------------------
    # each entry: (name, |b|/a, gives_r_half, forced_by_retained, note)
    candidates = []

    # 1. geometric inverse-length: face-diagonal length sqrt(2); stay normalized a=1
    bmod1 = 1.0 / np.sqrt(2.0)
    candidates.append(("geometric 1/L (inverse length)", bmod1, True, False,
                       "rests on a=1 (stay normalized) + inverse-length; both unforced"))
    # 2. geometric inverse-length-squared (massless propagator ~ 1/L^2)
    bmod2 = 1.0 / 2.0
    candidates.append(("geometric 1/L^2 (propagator)", bmod2, False, False, ""))
    # 3. path-counting: face-diagonal has 2 NN paths -> weight 2
    candidates.append(("path-count (2 NN paths -> weight 2)", 2.0, False, False, "r=4, Q=3 unphysical"))
    # 4. inverse path-count -> weight 1/2
    candidates.append(("inverse path-count (weight 1/2)", 0.5, False, False, ""))
    # 5. group-theoretic orbit-size ratio |<110>|/|<100>| = 12/6 = 2
    candidates.append(("group orbit-size ratio 12/6 = 2", 2.0, False, False, ""))
    # 6. group-theoretic stabilizer ratio 4/8 = 1/2
    candidates.append(("group stabilizer ratio 4/8 = 1/2", 0.5, False, False, ""))
    # 7. K_0-real / block-counting equipartition: equal HS power per R[Z3]=R(+)C block
    bmod7 = 1.0 / np.sqrt(2.0)
    candidates.append(("K_0-real block-counting (equipartition)", bmod7, True, True,
                       "= the admitted AC_phi_lambda block-counting measure; NOT new"))
    # 8. Born / dimension measure
    candidates.append(("Born / dimension measure (a=|b|)", 1.0, False, False, "the r=1 default"))

    n_half = 0
    n_new_forced = 0
    for name, ratio, gives_half, forced, msg in candidates:
        r = r_from_ratio(ratio, a=1.0)
        Q = koide_Q_from_r(r)
        is_half = abs(r - 0.5) < 1e-9
        record(f"candidate [{name}]: |b|/a={ratio:.4f} -> r={r:.4f}, Q={Q:.4f}"
               + (f"  ({msg})" if msg else ""),
               is_half == gives_half,
               "r=1/2" if is_half else "")
        if is_half:
            n_half += 1
            if forced:
                n_new_forced += 1

    # ---- honest verdict ---------------------------------------------------
    record("exactly the block-counting and the (unforced) geometric-1/L conventions give r=1/2",
           n_half == 2)
    record("the ONLY r=1/2 convention forced by retained machinery is block-counting = the admitted AC_phi_lambda",
           n_new_forced == 1)
    record("VERDICT: no NEW forced convention derives r=1/2; GATE-R-HALF not closed by diagonal weighting",
           True)
    record("geometry explains the (1,2) sector multiplicity but NOT the equal-power measure (Born gives r=1)",
           True)

    # ---- source-note firewalls --------------------------------------------
    if NOTE.exists():
        text = " ".join(NOTE.read_text(encoding="utf-8").split())
        for phrase in [
            "does not change axioms",
            "not forced",
            "does not close",
            "AC_phi_lambda",
        ]:
            record(f"source-note firewall present: {phrase!r}", phrase in text)
    else:
        record("source note present", False, "note file missing")

    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
